#gate #Y_gate
## What it does
It is a [[quantum gate]]
It's basically an [[X gate|X gate]] But with a [[Phase shift]]
on the [[Bloch sphere]] it's a $180^\circ$ rotation around $y$
(X, Y and Z are the **Pauli** gates, they're the errors in the [[Depolarizing channel]])
## Matrix
$$
\text Y=i
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
$$
## Qiskit implementation
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.y(0)
```
## Visual representation
```visual
   ┌───┐
q: ┤ Y ├
   └───┘
```
![[Y_gate.png]]
## Truth Table
$$
\begin{array}{c|c}
x&\text Y(x)\\ 
\hline
|0\rangle&i|1\rangle\\
|1\rangle&-i|0\rangle
\end{array}
$$
