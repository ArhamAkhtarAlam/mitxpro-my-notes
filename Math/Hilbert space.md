#math #hilbert_space #linear_algebra
the "space" that quantum states live in. basically a vector space where you can measure lengths and angles
## what it is
a **Hilbert space** is a vector space (you can add states and multiply them by [[Complex numbers|complex numbers]]) with an **inner product** $\langle\psi|\phi\rangle$ ([[Dirac notation]])

the inner product gives you
- **length** (the norm): $\|\psi\|=\sqrt{\langle\psi|\psi\rangle}$. quantum states have length 1
- **angles / overlap**: $|\langle\psi|\phi\rangle|$, how similar 2 states are ([[State fidelity]])
- **orthogonal** states: $\langle\psi|\phi\rangle=0$, completely distinguishable

(technically it also has to be "complete", meaning no holes, which only matters for infinite dimensional spaces)
## the ones we use

| system | Hilbert space | dimension | basis |
|---|---|---|---|
| 1 qubit | $\mathbb C^2$ | 2 | $\lvert0\rangle,\lvert1\rangle$ |
| 2 qubits | $\mathbb C^2\otimes\mathbb C^2=\mathbb C^4$ | 4 | $\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle$ |
| $n$ qubits | $\mathbb C^{2^n}$ | $2^n$ | every $n$ bit string |
| a particle on a line | functions $\psi(x)$ | infinite | eg. the states in [[Particle in a box]] |

putting systems together = [[Tensor product|tensor product]] of their Hilbert spaces, so the **dimensions multiply**
> [!important] why quantum computers are powerful (and hard to simulate)
> ==every extra qubit **doubles** the dimension.== 300 qubits have a Hilbert space bigger than the number of atoms in the observable universe ($2^{300}\approx10^{90}$). that's why simulating them classically is hopeless ([[Simulating quantum systems]])

## useful facts
- any orthonormal basis works: eg. $|+\rangle,|-\rangle$ is just as good a basis for $\mathbb C^2$ as $|0\rangle,|1\rangle$
- [[Unitary Operation|unitaries]] are the "rotations" of a Hilbert space: they keep all lengths and angles the same
- observables are Hermitian operators on it, and their [[Eigenvalues and eigenvectors|eigenvectors]] form a basis

see also [[Dirac notation]], [[Tensor product]], [[Complex numbers]], [[Math]]
