#gate #Z_gate
## What it does 
It is a [[quantum gate]]
Just does a [[Phase shift]] by $\pi$
on the [[Bloch sphere]] it's a $180^\circ$ rotation around $z$
it's the error in the [[Dephasing channel]]
(X, Y and Z are the **Pauli** gates, they're the errors in the [[Depolarizing channel]])
## Matrix
$$
\text Z=
\begin{bmatrix}
1&0
\\
0&-1
\end{bmatrix}
$$
## Qiskit implementation
```python
from qiskit import QuantumCircuit
qc = QuantumCircuit(1)
qc.z(0)
```
## Visual representation
```visual
   ┌───┐
q: ┤ Z ├
   └───┘
```
![[Z_gate.png]]
## Truth Table
$$
\begin{array}{c|c}
x&\text Z(x)\\
\hline
|0\rangle&|0\rangle\\
|1\rangle&-|1\rangle
\end{array}
$$