#H_gate #gate
## What it does
It is a [[quantum gate]]
Takes a $|0\rangle$ or a $|1\rangle$ and makes it into a 50/50 state
on the [[Bloch sphere]] it's a $180^\circ$ rotation around the axis halfway between $x$ and $z$ (so $|0\rangle\leftrightarrow|+\rangle$ and $|1\rangle\leftrightarrow|-\rangle$)
## Matrix
$$\text H=\frac1 {\sqrt 2}\begin{bmatrix}1 & 1 \\1 & -1\end{bmatrix}$$ 
## Qiskit Implementation
``` python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)
```
## Visual Representation
``` visual 
   ┌───┐ 
q: ┤ H ├ 
   └───┘
```
![[H_gate.png]]
## Truth Table
$$
\begin{array}{c|c}
x & \text H(x)\\
\hline
|0\rangle & \frac 1 {\sqrt 2}(|0\rangle+|1\rangle)\\
|1\rangle & \frac 1 {\sqrt 2}(|0\rangle-|1\rangle)
\end{array}
$$
these two outputs have names: $|+\rangle$ and $|-\rangle$
## On the Bloch sphere
![[H_gate_bloch.png|500]]
half a turn around the diagonal axis between $x$ and $z$. it swaps the $z$ axis and the $x$ axis, so it **switches between the $|0\rangle,|1\rangle$ basis and the $|+\rangle,|-\rangle$ basis**
## Properties
- $\text H\text H=I$, so doing it twice gets you back where you started
$$
\text H|+\rangle=|0\rangle\qquad\text H|-\rangle=|1\rangle
$$
- it turns X into Z and Z into X: $\text H\text X\text H=\text Z$ and $\text H\text Z\text H=\text X$
- the matrix is $\frac1{\sqrt2}(\sigma_x+\sigma_z)$, the same thing Bob measures in the [[CHSH quantum strategy]]
> [!important] 50/50 but not random
> $|+\rangle$ and $|-\rangle$ both give 0 or 1 with 50/50 when measured, but they're **not** the same as a coin flip: another H turns them back into a definite $|0\rangle$ or $|1\rangle$. a real 50/50 coin (the mixed state $\frac I2$, see [[Density matrix]]) can't be undone like that
## On many qubits
H on every qubit of $|00\ldots0\rangle$ gives an equal superposition of **every** bit string
$$
\text H^{\otimes n}|0\rangle^{\otimes n}=\frac1{\sqrt{2^n}}\sum_{x=0}^{2^n-1}|x\rangle
$$
eg. 2 qubits: $\frac12(|00\rangle+|01\rangle+|10\rangle+|11\rangle)$ (see [[Tensor product]])
## Where it's used
- the first step of almost every algorithm: [[Shor's algorithm]], [[Quantum Phase Estimation]], the [[Quantum Fourier Transform]]
- making Bell states: H then a [[CNOT gate]]
- switching bases, like the $|+\rangle,|-\rangle$ basis in [[BB84]]
