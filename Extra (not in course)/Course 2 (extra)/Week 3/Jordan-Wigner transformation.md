#extra #quantum_chemistry #pauli #hamiltonian_simulation
**extra** (not in the course): how a molecule's electrons get turned into qubits so [[VQE]] or [[Trotterization]] can work on them. electrons are **fermions** and qubits aren't, so you need a translation
## the problem
an electron either is or isn't in each orbital (spin-orbital $j$). that's a 0 or 1, so one qubit per orbital: $|1\rangle$ = occupied
- **creation** $a_j^\dagger$ puts an electron in orbital $j$, **annihilation** $a_j$ removes one
- fermions **anticommute**: $a_ia_j^\dagger=-a_j^\dagger a_i$ for $i\neq j$. swapping two electrons gives a minus sign (that's the Pauli exclusion principle)
- but Pauli operators on **different** qubits commute. so the naive "$a_j^\dagger=|1\rangle\langle0|$ on qubit $j$" gets the signs wrong

## the fix: a string of $Z$s
$$
a_j^\dagger=Z_1Z_2\cdots Z_{j-1}\otimes\frac{X_j-iY_j}2,\qquad a_j=Z_1Z_2\cdots Z_{j-1}\otimes\frac{X_j+iY_j}2
$$
^jordan-wigner

$\frac{X-iY}2=|1\rangle\langle0|$ adds the electron. the $Z$ string in front counts how many electrons are in the orbitals **before** $j$ and gives $-1$ for each, which produces exactly the fermion signs

> [!important] the one idea
> ==Jordan–Wigner = "orbital $j$ is qubit $j$" plus a string of $Z$s on all earlier qubits to keep track of the fermion sign==. then any molecular Hamiltonian becomes a sum of [[Pauli matrices|Pauli strings]] a quantum computer can handle

## common pieces

| fermion term | qubit version |
|---|---|
| number of electrons in $j$: $a_j^\dagger a_j$ | $\frac{I-Z_j}2$ |
| hopping between neighbours: $a_j^\dagger a_{j+1}+a_{j+1}^\dagger a_j$ | $\frac12\left(X_jX_{j+1}+Y_jY_{j+1}\right)$ |
| hopping between $j$ and $k$ further apart | the same, with $Z$s on every qubit in between |

> [!eg] hydrogen
> H$_2$ in the smallest basis has 4 spin-orbitals → **4 qubits**. Jordan–Wigner turns its Hamiltonian into 15 Pauli strings like $Z_1$, $Z_1Z_2$, $X_1X_2Y_3Y_4$. using symmetries (the number of electrons and spin are fixed) it shrinks to 2 qubits, or even 1, which is the small [[VQE#^h2-hamiltonian|H₂ Hamiltonian]]

## the cost
the $Z$ strings can be as long as the number of orbitals, so one hop can touch $n$ qubits: deep circuits. alternatives:
- **Bravyi–Kitaev**: strings only $\sim\log n$ long
- **parity mapping**: makes it easy to drop two qubits using symmetry

all give the same physics, just different circuits

> [!exercise] try these
> **1** check $a^\dagger a=\frac{I-Z}2$ on one qubit
> **2** what does $\frac{X_1X_2+Y_1Y_2}2$ do to $|10\rangle$?
> **3** why can't you just use $a_j^\dagger=|1\rangle\langle0|_j$ with no $Z$ string?

> [!answer]-
> **1** $|1\rangle\langle0|\,|0\rangle\langle1|=|1\rangle\langle1|=\frac{I-Z}2$ ✓ (1 if occupied, 0 if empty)
> **2** $|01\rangle$: the electron hops from orbital 1 to orbital 2
> **3** then operators on different orbitals would commute, but fermion operators must anticommute (wrong signs, wrong energies)

see also [[VQE]], [[Simulating quantum systems]], [[Hamiltonian]], [[Hamiltonian simulation]], [[Density functional theory]]
