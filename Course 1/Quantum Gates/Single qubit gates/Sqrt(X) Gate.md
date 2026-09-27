#sqrt_X_gate #gate
## What it does
It is a [[quantum gate]]
It's like if you do two of these then it will become a regular [[X gate]]
on the [[Bloch sphere]] it's a $90^\circ$ rotation around $x$
on real hardware it's a $\frac\pi2$ pulse, see [[Rabi oscillation]]
## Matrix
$$
\sqrt {\text X}=
\frac 1 2
\begin{bmatrix}
1+i & 1-i\\1-i & 1+i
\end{bmatrix}
$$
## Qiskit implementation
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.sx(0)
```
## Visual representation
```visual
   ┌────┐
q: ┤ √X ├
   └────┘
```
## Truth Table
$$
\begin{array}{c|c}
x & \sqrt{\text X}(x)\\
\hline
|0\rangle & \frac 1 2\big((1+i)|0\rangle+(1-i)|1\rangle\big)\\
|1\rangle & \frac 1 2\big((1-i)|0\rangle+(1+i)|1\rangle\big)
\end{array}
$$
