#hamiltonian #schrodinger_equation #energy
the operator for the **total energy** of a system. it decides how a quantum state changes in time. part of [[Simulating quantum systems]]
## what it is
for a **closed** system (cut off from its surroundings), the Hamiltonian is kinetic + potential energy. for one particle
$$
\hat H=\frac{\hat p^2}{2m}+\hat V(x)
$$
- $\frac{\hat p^2}{2m}$ = kinetic energy, with momentum operator $\hat p=-i\hbar\frac{\partial}{\partial x}$
- $\hat V(x)$ = potential energy
## what it does
**1. its eigenvalues are the energies** ([[Eigenvalues and eigenvectors]])
$$
\hat H|E_k\rangle=E_k|E_k\rangle
$$
the lowest one is the **ground state** energy, which is what chemists usually want. and $\langle\psi|\hat H|\psi\rangle$ is the average energy of a state ([[Probability and expectation values]])

**2. it drives the time evolution**: the Schrödinger equation (1925, Nobel prize 1933)
$$
i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle=\hat H|\psi(t)\rangle
$$
($\hbar=\frac h{2\pi}$). if $\hat H$ doesn't change in time, the solution is
$$
|\psi(t)\rangle=e^{-i\hat Ht/\hbar}|\psi(0)\rangle
$$
^time-evolution

$U(t)=e^{-i\hat Ht/\hbar}$ is a [[Unitary Operation|unitary]], just like a [[Quantum gate|quantum gate]]. every gate is really "let some Hamiltonian act for some time"
> [!example] one qubit: $\hat H=\frac{\hbar\omega}2Z$
> $$
> e^{-i\hat Ht/\hbar}=\begin{bmatrix}e^{-i\omega t/2}&0\\0&e^{i\omega t/2}\end{bmatrix}
> $$
> that's a rotation around $z$ on the [[Bloch sphere]] (a [[Phase shift]] up to a global phase): the state just spins at speed $\omega$

## why it's hard to simulate
for $n$ qubits (or $n$ spins), $\hat H$ is a $2^n\times2^n$ matrix. 50 qubits → a matrix with about $10^{15}$ rows. solving the Schrödinger equation exactly becomes impossible on a normal computer, which is why we want [[Hamiltonian simulation]] on a quantum one
> [!tip] qubit Hamiltonians are sums of Paulis
> on qubits, a Hamiltonian is usually written as a weighted sum of Pauli strings ([[X gate|X]], [[Y gate|Y]], [[Z gate|Z]], $I$), eg. the hydrogen molecule in [[VQE]]
> ![[VQE#^h2-hamiltonian]]

> [!warning] what a Hamiltonian does NOT tell you directly
> ==it gives energies and time evolution, and the gates of a quantum computer come from Hamiltonians.== but it doesn't directly give the **amount of entanglement** of a state (that's [[Entanglement entropy]])

see also [[Particle in a box]], [[Hamiltonian simulation]], [[Unitary Operation]]
