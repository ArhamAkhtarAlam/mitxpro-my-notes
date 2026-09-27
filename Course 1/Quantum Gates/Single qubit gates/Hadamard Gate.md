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