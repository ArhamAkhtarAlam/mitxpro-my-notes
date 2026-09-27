#gate #X_gate
## What it does
It is a [[quantum gate]]
A quantum version NOT gate so $|0\rangle$ to $|1\rangle$ and $|1\rangle$ to $|0\rangle$
on the [[Bloch sphere]] it's a $180^\circ$ rotation around $x$. on real hardware it's a $\pi$ pulse, see [[Rabi oscillation]]
(X, Y and Z are the **Pauli** gates, they're the errors in the [[Depolarizing channel]])
## Matrix
$$
\text X =\begin{bmatrix}
0&1\\
1&0
\end{bmatrix}
$$
## Qiskit implementation
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.x(0)
```
## Visual representation
```visual
   ┌───┐
q: ┤ X ├
   └───┘
```
![[X_gate.png]]
## Truth Table
$$
\begin{array}{c|c}
x& \text X(x)\\
\hline
|0\rangle & |1\rangle\\
|1\rangle & |0\rangle
\end{array}
$$
