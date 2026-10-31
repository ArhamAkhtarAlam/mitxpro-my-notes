#quantum_error_correction #parity #measurement
## the problem
we've encoded a qubit with the [[Bit flip code]]

![[Bit flip code#^encoding]]

now, how do we find out if one of the three qubits flipped? we can't just measure them: that would collapse $\alpha|000\rangle+\beta|111\rangle$ and destroy the information we're trying to protect

the answer is a kind of **majority vote**, done with measurements called **parity checks** between neighbouring qubits
- two qubits in the **same** state ($00$ or $11$) have the **same parity**
- two qubits in **different** states ($01$ or $10$) have **different parity**

the outputs of the parity measurements together are the **syndrome**, and it tells us **if** and **where** a single error happened

> [!important] the one idea
> ==a parity measurement tells you whether two qubits are the same or different, but never which state they're in==, so it can find an error without projecting out (destroying) the quantum information. it's the backbone of quantum error detection

## the circuit
compute the XOR of two qubits onto an extra **ancilla** qubit, then measure only the ancilla
- $s_A=q_1\oplus q_2$ (parity of qubits 1 and 2), stored on ancilla $S_A$
- $s_B=q_2\oplus q_3$ (parity of qubits 2 and 3), stored on ancilla $S_B$

the XOR is two [[CNOT gate|CNOTs]] in a row with the ancilla as the target: flip $S_A$ if qubit 1 is $|1\rangle$, then flip it again if qubit 2 is $|1\rangle$. both ancillas start in $|0\rangle$

![[Bit_flip_syndrome_circuit.png]]

| $q_1$ | $q_2$ | $s_A=q_1\oplus q_2$ | meaning |
|---|---|---|---|
| 0 | 0 | 0 | same parity, no error here |
| 1 | 1 | 0 | same parity, no error here |
| 0 | 1 | 1 | different parity, one of them flipped |
| 1 | 0 | 1 | different parity, one of them flipped |

$s_B$ works the same way for qubits 2 and 3
## the syndrome
each error gives a different pair $(s_A,s_B)$

| error | state | $s_A$ (1 vs 2) | $s_B$ (2 vs 3) | syndrome |
|---|---|---|---|---|
| none | $\alpha\vert000\rangle+\beta\vert111\rangle$ | same | same | $00$ |
| qubit 1 | $\alpha\vert100\rangle+\beta\vert011\rangle$ | different | same | $10$ |
| qubit 2 | $\alpha\vert010\rangle+\beta\vert101\rangle$ | different | different | $11$ |
| qubit 3 | $\alpha\vert001\rangle+\beta\vert110\rangle$ | same | different | $01$ |

^syndrome-table

> [!quote]- the course's key image: the syndrome table
> ![[Course 4 week 1 key images.pdf#page=1]]

==the syndrome uniquely says if a single bit flip happened, and on which qubit==. qubit 2 is the only one in **both** checks, so it's the only one that lights up both
## why it doesn't destroy the state
> [!eg] a flip on qubit 1, step by step
> the state is $\alpha|100\rangle+\beta|011\rangle$, ancillas $|S_AS_B\rangle=|00\rangle$ (written after the data qubits)
> $$
> \begin{aligned}
> &\alpha|100\rangle|00\rangle+\beta|011\rangle|00\rangle\\
> \xrightarrow{\text{CNOT }1\to S_A}\ &\alpha|100\rangle|10\rangle+\beta|011\rangle|00\rangle\\
> \xrightarrow{\text{CNOT }2\to S_A}\ &\alpha|100\rangle|10\rangle+\beta|011\rangle|10\rangle\\
> \xrightarrow{\text{CNOT }2\to S_B}\ &\alpha|100\rangle|10\rangle+\beta|011\rangle|11\rangle\\
> \xrightarrow{\text{CNOT }3\to S_B}\ &\alpha|100\rangle|10\rangle+\beta|011\rangle|10\rangle\\
> =\ &\big(\alpha|100\rangle+\beta|011\rangle\big)\otimes|10\rangle
> \end{aligned}
> $$
> the ancillas end up in $|10\rangle$ in **both** parts of the superposition, so they're not entangled with the data ([[Tensor product]]). measuring them gives $10$ with certainty and leaves $\alpha|100\rangle+\beta|011\rangle$ untouched. $\alpha$ and $\beta$ are never touched

that's the trick: in each part of the superposition, the two qubits being compared are **both** different ($10$ and $01$) or **both** the same, so the parity has the same value everywhere. the measurement never projects the qubits onto $|0\rangle$ or $|1\rangle$, it only learns the parity

> [!extra] parity is the $Z_1Z_2$ operator
> measuring $s_A$ is the same as measuring the operator $Z_1Z_2=Z\otimes Z\otimes I$: its eigenvalue is $+1$ for even parity ($|00\rangle,|11\rangle$) and $-1$ for odd ($|01\rangle,|10\rangle$), so $s_A=0\leftrightarrow+1$ and $s_A=1\leftrightarrow-1$. the code states are $+1$ eigenstates of both $Z_1Z_2$ and $Z_2Z_3$, these operators are called the code's **stabilizers**. measuring an operator only projects onto its eigenspaces ([[Projectors]]), and here a whole eigenspace contains $\alpha|000\rangle+\beta|111\rangle$, so nothing collapses

next: what to do with the syndrome, [[Bit flip code#correcting the error]]

> [!exercise] try these
> ① work out $s_A$ and $s_B$ step by step for a flip on qubit 3, $\alpha|001\rangle+\beta|110\rangle$
> ② why not just measure all three qubits and take a majority vote?
> ③ what syndrome do you get if qubits 1 **and** 2 both flip?

> [!answer]-
> ① $S_A$: $q_1\oplus q_2=0\oplus0=0$ in the $\alpha$ part and $1\oplus1=0$ in the $\beta$ part, so $s_A=0$. $S_B$: $q_2\oplus q_3=0\oplus1=1$ and $1\oplus0=1$, so $s_B=1$. syndrome $01$ → qubit 3
> ② measuring them projects onto $|000\rangle$ (with probability $|\alpha|^2$) or $|111\rangle$: you'd learn the logical bit, but lose the superposition
> ③ $\alpha|110\rangle+\beta|001\rangle$: qubits 1, 2 the same, 2, 3 different → $01$, which **looks like** a flip on qubit 3. the correction then makes it worse, see [[Bit flip code#when it breaks]]

see also [[Decoding the bit flip code]] (the same parities without ancillas), [[Phase flip code]] (the same checks in the $|\pm\rangle$ basis), [[Bit flip code]], [[CNOT gate]], [[Quantum Error Correction]]

week hub: [[Detecting and correcting errors]]
