#surface_code #quantum_error_correction #CNOT_gate #fault_tolerance
how to store a qubit in the [[Surface code]], measure it, and do gates on it, using mostly **measurements**
## logical qubits are long chains
look at the layout again: the red line is a chain of bit flips from top to bottom, the green line a chain of phase flips from left to right

![[Surface_code_layout.png]]

every blue shape the red line passes touches it **twice**, so its parity doesn't change: no detection events at all. ==a chain of errors stretching all the way across is invisible==. that's a weakness (if errors build up into a chain like that, the data is corrupted), but it's also exactly what lets the code store a qubit
- the red chain $X\cdots X$ is the **logical** $\bar X$
- the green chain $Z\cdots Z$ is the **logical** $\bar Z$
- they cross at one qubit, so they **anticommute**, like $X$ and $Z$ should

(any chain across in the same direction works, they all differ by checks. compare the Steane code's $\bar X=X_4X_5X_6$ in [[Steane code circuit]])
## preparing states

| want | start every data qubit in | then | then |
|---|---|---|---|
| $\lvert\bar0\rangle$ | $\lvert0\rangle$ | — | start the checks |
| $\lvert\bar1\rangle$ | $\lvert0\rangle$ | bit flip along the red line | start the checks |
| $\lvert\bar+\rangle$ | $\lvert+\rangle$ | — | start the checks |
| $\lvert\bar-\rangle$ | $\lvert+\rangle$ | phase flip along the green line | start the checks |

## measuring
**logical $Z$ measurement**: measure **every** data qubit in the $Z$ basis (a transversal measurement). correct the results using the final round of checks, then the answer is the **parity of the results along a green line** (the logical $\bar Z$)

**logical $X$**: the same with every data qubit measured in the $X$ basis, and the parity along a red line
## measuring several logical qubits at once
you can also measure **multi-qubit** logical operators, eg. $\bar Z\bar Z$ on two logical qubits: their **parity**, but without learning either one alone. it's the big fault-tolerant version of what one blue half circle does to two physical qubits

how: open up a strip of new checks between the two patches. the product of all the new blue shapes in the strip equals the product of the two green lines, so ==multiplying many small local parities gives one big logical parity==. this is called **lattice surgery**

![[Lattice_surgery_ZZ.png]]

each patch's $\bar Z$ is a row of $Z$s. the 4 new blue checks overlap each other on the fresh qubits, so those cancel, and what's left is the bottom row of patch 1 times the top row of patch 2: $\bar Z_1\bar Z_2$ (checked numerically). each new check is just a small parity, but their product is the logical parity

$\bar X\bar X$ works the same way with orange shapes, and even mixed operators like $\bar X\bar X\bar Z$ work: some shapes are then **half blue, half orange**, which just means the Hadamard (bit flip → phase flip detection) happens at different times on different qubits around the shape
## a CNOT made of measurements
with a logical ancilla $A$ between the control $C$ and the target $T$:
1. prepare $A$ in $|\bar0\rangle$
2. measure $\bar X_A\bar X_T$ (outcome $a$)
3. measure $\bar Z_C\bar Z_A$ (outcome $b$)
4. measure $A$ in the $X$ basis (outcome $c$)

the result is a CNOT from $C$ to $T$, up to Paulis: $X_T$ if $b=-1$, and $Z_C$ if $a\cdot c=-1$. those Paulis are never applied, the classical software just remembers them and flips later measurement results

![[Measurement_CNOT.png]]

the same trick gives a CNOT with **one control and many targets** at no extra cost: measure $\bar X_A\bar X_{T_1}\bar X_{T_2}\cdots$ in step 2

> [!extra] why the Paulis can wait
> a Clifford gate turns a Pauli into another Pauli: eg. a CNOT turns $X_C$ (before it) into $X_CX_T$ (after it), and $Z_T$ into $Z_CZ_T$. so a pending Pauli can be pushed through all the later Clifford gates, and it only ever changes **which** measurement results get flipped. this bookkeeping is the **Pauli frame**. the one place it can't wait is a $T$ gate, since $TXT^\dagger$ isn't a Pauli: that's where the $S$ correction in [[Magic state distillation]] comes from
>
> each lattice surgery measurement also takes about $d$ rounds of checks, not one, because a single round could have a measurement error in it (same reason as [[Parity measurement]] repeats). so a logical CNOT costs a few times $d$ check rounds

> [!important] the one idea
> ==on the surface code, gates become measurements: prepare, measure some big logical parities, track the Paulis in software==

> [!exercise] try these
> ① why can't the checks see the red chain, but they can see the same chain stopping in the middle of the grid?
> ② the grid has 5 data qubits along each side. what's the smallest number of bit flips that causes an undetected logical error?
> ③ in the measurement CNOT, the outcomes are $a=+1$, $b=-1$, $c=-1$. which Paulis does the software note down?
> ④ why measure $\bar Z\bar Z$ instead of measuring $\bar Z$ on each qubit and multiplying?

> [!answer]-
> ① across the grid, every blue shape it passes touches it twice. stopping in the middle, the blue shape at the end touches it only once, so it flips: a detection event at each loose end
> ② 5: a chain all the way across (the code distance $d=5$)
> ③ $b=-1$ → $X_T$; $a\cdot c=-1$ → $Z_C$. both
> ④ measuring each one would collapse each qubit and destroy any superposition or entanglement between them. $\bar Z\bar Z$ only reveals the parity, eg. it keeps $\alpha|\bar0\bar0\rangle+\beta|\bar1\bar1\rangle$ intact

see also [[Parity measurement]], [[CNOT gate]], [[Teleportation]], [[Transversal gates on stabilizer codes]]

part of [[Surface code]] · week hub: [[Quantum error mitigation]]
