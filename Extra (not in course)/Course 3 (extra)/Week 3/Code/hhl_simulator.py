"""HHL simulator: solve A x = b with the HHL algorithm in Qiskit, and compare with the classical answer.

how to use
  1. pip install qiskit numpy scipy
  2. edit the EQUATIONS section below (or call solve(A, b) yourself)
  3. python hhl_simulator.py

any size, any matrix:
  - A doesn't have to be Hermitian: if it isn't, the code solves the bigger Hermitian system [[0, A], [A^†, 0]] instead
  - the size doesn't have to be a power of 2: the code pads with extra 1s on the diagonal
  - negative eigenvalues are fine (the clock is read as a signed number)
the answer comes out as a normalised state, exactly like real HHL. the code prints it next to the classical answer
(also normalised) plus the fidelity between them. more clock qubits = more accurate eigenvalues = higher fidelity
"""
import numpy as np
from scipy.linalg import expm
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import UnitaryGate, RYGate
from qiskit.quantum_info import Statevector
try:
    from qiskit.circuit.library import phase_estimation as _pe      # Qiskit >= 2.1
    PhaseEstimation = lambda m, U: _pe(m, U)
except ImportError:
    from qiskit.circuit.library import PhaseEstimation             # older Qiskit

# ---------------- EQUATIONS (edit these) ----------------
# one row per equation, one column per unknown. this is the 10 variable example from the note:
# a chain where each unknown is linked to its neighbours: -x(j-1) + 3 x(j) - x(j+1) = 1
A = [
    [ 3, -1,  0,  0,  0,  0,  0,  0,  0,  0],
    [-1,  3, -1,  0,  0,  0,  0,  0,  0,  0],
    [ 0, -1,  3, -1,  0,  0,  0,  0,  0,  0],
    [ 0,  0, -1,  3, -1,  0,  0,  0,  0,  0],
    [ 0,  0,  0, -1,  3, -1,  0,  0,  0,  0],
    [ 0,  0,  0,  0, -1,  3, -1,  0,  0,  0],
    [ 0,  0,  0,  0,  0, -1,  3, -1,  0,  0],
    [ 0,  0,  0,  0,  0,  0, -1,  3, -1,  0],
    [ 0,  0,  0,  0,  0,  0,  0, -1,  3, -1],
    [ 0,  0,  0,  0,  0,  0,  0,  0, -1,  3],
]
b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
CLOCK_QUBITS = 5      # how many qubits store the eigenvalue (more = more accurate, but the filter works less often)
SHOTS = 10_000        # for the "real experiment" style counts at the end
C_VALUE = None        # None = automatic (safe but small). if you know every |eigenvalue| >= some number, put it here (eg. 1.0)
# ---------------------------------------------------------


def prepare_system(A, b):
    """make A Hermitian and a power of 2 in size, so HHL can use it. returns (A_h, b_h, read) where
    read(v) picks out the entries of v that are the original unknowns x1, x2, ..."""
    A = np.array(A, dtype=complex); b = np.array(b, dtype=complex)
    n0 = len(b)
    if not np.allclose(A, A.conj().T):                       # Hermitian dilation: [[0, A], [A^†, 0]] (0, x) = (b, 0)
        A = np.block([[np.zeros_like(A), A], [A.conj().T, np.zeros_like(A)]])
        b = np.concatenate([b, np.zeros(n0)])
        read = lambda v: v[n0:2 * n0]                        # x sits in the second half
        print("A isn't Hermitian, so solving the Hermitian dilation [[0, A], [A†, 0]] instead")
    else:
        read = lambda v: v[:n0]
    N = 1 << int(np.ceil(np.log2(len(b))))                   # pad up to a power of 2
    if N != len(b):
        pad = N - len(b)
        A = np.block([[A, np.zeros((len(b), pad))], [np.zeros((pad, len(b))), np.eye(pad)]])
        b = np.concatenate([b, np.zeros(pad)])
        print(f"padded to {N}x{N} with 1s on the diagonal (the extra unknowns come out as 0)")
    return A, b, read


def build_hhl(A, b, m, t=None, C=None):
    """the HHL circuit: load b, phase estimation, controlled rotations, undo phase estimation"""
    n = int(np.log2(len(b)))
    lam = np.linalg.eigvalsh(A)
    signed = lam.min() < 0
    lmax = np.abs(lam).max()
    if t is None:      # pick t so the biggest eigenvalue fits on the clock (half a turn, or just under it if signed)
        t = np.pi / lmax if not signed else 2 * np.pi * (2 ** (m - 1) - 1) / (2 ** m * lmax)
    def clock_to_lambda(c):            # clock reading c means a phase of c/2^m of a full turn
        phi = c / 2 ** m
        if signed and phi >= 0.5: phi -= 1
        return 2 * np.pi * phi / t
    if C is None:                      # biggest allowed C: the smallest |λ| the clock can show
        C = min(abs(clock_to_lambda(c)) for c in range(1, 2 ** m))

    breg = QuantumRegister(n, "b"); clk = QuantumRegister(m, "clock"); anc = QuantumRegister(1, "anc")
    qc = QuantumCircuit(breg, clk, anc)
    qc.initialize(b / np.linalg.norm(b), breg)                               # step 1: load |b⟩
    qpe = PhaseEstimation(m, UnitaryGate(expm(1j * A * t), label="exp(iAt)"))
    qc.append(qpe, list(clk) + list(breg))                                   # step 3: eigenvalues onto the clock
    for c in range(1, 2 ** m):                                               # step 4: rotate the ancilla by C/λ
        ratio = np.clip(C / clock_to_lambda(c), -1, 1)
        # Qiskit's phase estimation leaves the clock bit-reversed (most significant bit on clock[0]),
        # so read the controls in reverse order to make ctrl_state = c mean "the clock says c"
        qc.append(RYGate(2 * np.arcsin(ratio)).control(m, ctrl_state=c), list(reversed(clk)) + [anc[0]])
    qc.append(qpe.inverse(), list(clk) + list(breg))                         # step 6: uncompute the clock
    return qc, t, C, n


def solve(A, b, m=CLOCK_QUBITS, shots=SHOTS, t=None, C=None):
    A_h, b_h, read = prepare_system(A, b)
    qc, t, C, n = build_hhl(A_h, b_h, m, t, C)
    print(f"\n{len(b_h)}x{len(b_h)} system: {n} qubits for b, {m} clock qubits, 1 ancilla = {n + m + 1} qubits")
    print(f"eigenvalues of the matrix HHL uses: {np.round(np.linalg.eigvalsh(A_h), 4)}   t = {t:.4f}   C = {C:.4f}")

    sv = Statevector(qc).data.reshape(2, 2 ** m, 2 ** n)     # index order: anc, clock, b (Qiskit is little endian)
    good = sv[1, 0, :]                                       # ancilla = 1 (filter worked), clock back to 0
    p_success = np.linalg.norm(good) ** 2
    x_hhl = good / np.linalg.norm(good)

    x_true = np.linalg.solve(A_h, b_h / np.linalg.norm(b_h))
    x_classical = read(np.linalg.solve(A_h, b_h))            # the real, unnormalised answer
    x_true_n = x_true / np.linalg.norm(x_true)
    overlap = np.vdot(x_true_n, x_hhl)
    x_hhl_aligned = x_hhl * np.conj(overlap) / abs(overlap)  # remove an unmeasurable global phase
    fidelity = abs(overlap) ** 2

    print(f"\nchance the filter works (ancilla = 1): {p_success:.4f}")
    print(f"classical answer x:              {np.round(x_classical.real, 5)}")
    print(f"classical, normalised:           {np.round(read(x_true_n).real, 4)}")
    print(f"HHL state (normalised):          {np.round(read(x_hhl_aligned).real, 4)}")
    print(f"fidelity |<x_true|x_hhl>|^2:     {fidelity:.6f}")
    # the size of x is lost in the state, but it's hidden in the success rate: P = C^2 ||A^-1 b||^2 (for |b| = 1)
    print(f"||x|| (for b scaled to length 1) from the success rate: {np.sqrt(p_success) / C:.4f}"
          f"   (true: {np.linalg.norm(x_true):.4f})")

    # what a real machine would give you: measure b many times, keeping only runs where the filter worked
    idx = read(np.arange(len(x_hhl)))                        # which basis states hold x1, x2, ...
    probs = np.abs(x_hhl[idx]) ** 2
    probs = probs / probs.sum()
    rng = np.random.default_rng(1)
    counts = np.bincount(rng.choice(len(probs), size=shots, p=probs), minlength=len(probs))
    print(f"\nsimulated measurement of b ({shots} successful runs), showing which unknown each result is:")
    true_probs = np.abs(x_true[idx]) ** 2 / np.sum(np.abs(x_true[idx]) ** 2)
    for i, cnt in enumerate(counts):
        print(f"  x{i + 1}  (|{idx[i]:0{n}b}>)  {cnt:6d}   ({cnt / shots:.3f})"
              f"   exact HHL {probs[i]:.3f}   true answer {true_probs[i]:.3f}")
    print("  -> these give |x_i|^2 / sum |x_j|^2 (sizes only, not signs)")
    return qc


if __name__ == "__main__":
    circuit = solve(A, b, C=C_VALUE)
    # to see the circuit:  print(circuit.draw())
