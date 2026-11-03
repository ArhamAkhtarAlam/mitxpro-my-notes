#textbook #stabilizer_codes #steane_code #syndrome
*Quantum Computation and Quantum Information* §10.5.7 and §10.5.8 (p. 470–475). a tidy form for the check matrix that makes logical operators easy to read off, and the circuits that encode, measure syndromes and correct. part of [[Quantum Computation and Quantum Information]], previous: [[Stabilizer code constructions]]
## standard form
the check matrix of an $[n,k]$ code is $G=[G_1|G_2]$ ($n-k$ rows). three moves give an equivalent code
- swap rows = relabel generators
- swap a column on **both** sides = relabel qubits
- add one row to another = replace $g_i$ by $g_ig_j$

Gaussian elimination on $G_1$ ($r$ = its rank), then on the leftover block, then a few row additions bring it to the **standard form**
$$
\begin{array}{r}r\{\\n-k-r\{\end{array}\left[\begin{array}{ccc|ccc}I&A_1&A_2&B&0&C\\0&0&0&D&I&E\end{array}\right]
$$
^standard-form

(column blocks of width $r$, $n-k-r$, $k$ on each side). the procedure isn't unique, but any check matrix like this counts as standard form
## logical operators from the standard form
the $k$ logical $Z$s must be independent of the generators and each other, but commute with all of them. choose
$$
G_z=\left[\begin{array}{ccc|ccc}0&0&0&A_2^T&0&I\end{array}\right]\qquad G_x=\left[\begin{array}{ccc|ccc}0&E^T&I&C^T&0&0\end{array}\right]
$$
^standard-logicals

$G_z$ is only $Z$s, so its operators commute with each other. commuting with the generators comes from $I\times(A_2^T)^T+A_2=0$, and independence from having no $X$ part (vs the first $r$ generators) and no entries under the $I$ (vs the rest). similarly for $G_x$ (exercises 10.53, 10.54)
## the Steane code in standard form
here $n=7$, $k=1$, and the $X$ part has rank $r=3$. swap qubits 1↔4, 3↔4, 6↔7, then add row 6 to row 4, row 6 to row 5, and rows 4 and 5 to row 6
$$
\left[\begin{array}{ccccccc|ccccccc}
1&0&0&0&1&1&1&0&0&0&0&0&0&0\\
0&1&0&1&0&1&1&0&0&0&0&0&0&0\\
0&0&1&1&1&1&0&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&1&0&1&1&0&0&1\\
0&0&0&0&0&0&0&0&1&1&0&1&0&1\\
0&0&0&0&0&0&0&1&1&1&0&0&1&0
\end{array}\right]
$$
^steane-standard-form

reading off $A_2=(1,1,0)^T$ gives $G_z=[0000000|1100001]$: $\bar Z=Z_1Z_2Z_7$. undo the qubit swaps and that's $\bar Z=Z_2Z_4Z_6$ in the original labels. that looks different from [[Stabilizer code constructions#^steane-logical|$Z_1\cdots Z_7$]], but the two differ by $Z_1Z_3Z_5Z_7$, which is in the stabilizer, so ==they do the same thing to every code state== (multiplying a logical operator by a stabilizer never changes its action, exercise 10.56). (checked numerically: the standard form, with the swaps undone, stabilizes the same code)
## encoding by measuring
to prepare an encoded $|0\rangle^{\otimes k}$: start from any easy state, eg. $|0\rangle^{\otimes n}$, and **measure** $g_1,\dots,g_{n-k},\bar Z_1,\dots,\bar Z_k$ in turn. the result has stabilizer $\langle\pm g_1,\dots,\pm g_{n-k},\pm\bar Z_1,\dots,\pm\bar Z_k\rangle$, with signs set by the outcomes. fix the signs with Pauli products (the $g$ from [[The stabilizer formalism|proposition 10.4]] flips exactly one sign), then use $\bar X_j$ to reach any logical basis state. this isn't unitary (a unitary version uses the standard form, problem 10.3)

**decoding** often isn't needed at all: fault-tolerant methods compute on encoded data directly, and the answer can be read by **measuring the logical $Z$s**. if you do need it (eg. after sending a state down a channel), run the unitary encoder backwards

**error correction** is like encoding: measure every generator to get the syndrome $\beta_1,\dots,\beta_{n-k}$, then classical computation picks the recovery $E_j^\dagger$ ([[Stabilizer code constructions#theorem 10.8: the error-correction conditions for stabilizer codes]])
## measuring an operator
the key to all of these circuits is measuring an operator: project onto one of its eigenspaces **and** learn which one. for a $\pm1$ observable $M$ with a controlled-$M$ gate: ancilla $|0\rangle$, $H$, controlled-$M$, $H$, measure the ancilla (figure 10.13, the same idea as phase estimation). special cases
- **measuring $X$**: $H$, controlled-$X$, $H$ on the ancilla, or equivalently a CNOT **onto** the ancilla with Hadamards on the data qubit before and after (figure 10.14)
- **measuring $Z$**: just a CNOT from the data qubit onto an ancilla in $|0\rangle$, then measure the ancilla (figure 10.15)

nothing needs $M$ to be one qubit: it can be any $\pm1$ observable on many qubits, like the Pauli products we measure as generators
## the Steane syndrome circuit
from the standard form: the left block says where the controlled-$X$s go, the right block where the controlled-$Z$s go. six ancillas, one per generator (figure 10.16, qubits numbered in the standard form order)

![[Steane_syndrome_circuit.png]]

follow it with Pauli corrections and it's error correction. add a measurement of $\bar Z$ and fix the signs, and it prepares $|0_L\rangle$. with the identities above it can be redrawn using only Hadamards and CNOTs onto the ancillas (figure 10.17)

> [!warning] not fault tolerant yet
> each ancilla here touches 4 data qubits, so one ancilla error can spread to several of them. making this safe is the subject of §10.6 (course version: [[Fault-tolerant measurement]])

> [!exercise] try these
> ① find $\bar X$ for the Steane code in standard form (exercise 10.55)
> ② why does measuring $Z$ need only a CNOT and no Hadamards?
> ③ in the standard form, which generators does an $X$ error on qubit 1 (standard order) flip?

> [!answer]-
> ① $E=(1,1,0)^T$ and $C=0$, so $G_x=[0001101|0000000]$: $\bar X=X_4X_5X_7$ in the standard order, which is $X_3X_5X_6$ in the original labels (checked numerically: it commutes with every generator and anticommutes with $\bar Z$)
> ② a CNOT from the data onto $|0\rangle$ copies the data's $Z$ value onto the ancilla, $a|0\rangle+b|1\rangle\to a|00\rangle+b|11\rangle$, so measuring the ancilla is measuring $Z$ on the data
> ③ the $Z$ type generators with a 1 in column 1 of the right block: rows 4 and 6 (columns $1011001$ and $1110010$)

see also [[Stabilizer codes]], [[Fault-tolerant measurement]], [[Parity measurement]], [[Quantum Phase Estimation]]

next: [[Chapter 10 exercises]]
