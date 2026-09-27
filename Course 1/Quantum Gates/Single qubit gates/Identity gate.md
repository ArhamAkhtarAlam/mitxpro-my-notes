#gate #I_gate
## What it does
It is a [[quantum gate]]
Basically a buffer
Whatever comes in that same thing comes out not even with a [[Phase shift]]
on the [[Bloch sphere]] nothing moves
## Matrix
$$
\text I=\begin{bmatrix}
1 & 0
\\
0 & 1
\end{bmatrix}
$$
## Qiskit implementation
``` python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.id(0)
```
## Visual representation
``` visual
   ┌───┐
q: ┤ I ├
   └───┘
```
![[I_gate.png]]
## Truth Table
$$
\begin{array}{c|c}
x & \text I(x)\\
\hline
|0\rangle & |0\rangle\\
|1\rangle & |1\rangle
\end{array}
$$
