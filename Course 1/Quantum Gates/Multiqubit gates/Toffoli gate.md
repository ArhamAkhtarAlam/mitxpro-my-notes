#gate #Toffoli_gate #controlled_gate
## What it does
It is a [[Quantum gate|quantum gate]] on 3 qubits: **2 controls** and a **target**
- if **both** controls are $|1\rangle$ → flip the target ([[X gate]])
- otherwise → do nothing

basically a [[CNOT gate]] with 2 controls. it can do a reversible AND: if the target starts as $|0\rangle$ it ends up as (control 1 AND control 2)
## Matrix
$8\times8$, it's the identity except the last 2 rows are swapped
$$
\text{Toffoli}=\begin{bmatrix}
1&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0\\
0&0&0&1&0&0&0&0\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&0&1\\
0&0&0&0&0&0&1&0
\end{bmatrix}
$$
## Qiskit implementation
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(3)
qc.ccx(0, 1, 2)   # controls 0 and 1, target 2
```
## Visual representation
```visual
q_0: ──■──
       │
q_1: ──■──
     ┌─┴─┐
q_2: ┤ X ├
     └───┘
```
## Truth Table
$$
\begin{array}{c|c}
x & \text{Toffoli}(x)\\
\hline
|000\rangle & |000\rangle\\
|001\rangle & |001\rangle\\
|010\rangle & |010\rangle\\
|011\rangle & |011\rangle\\
|100\rangle & |100\rangle\\
|101\rangle & |101\rangle\\
|110\rangle & |111\rangle\\
|111\rangle & |110\rangle
\end{array}
$$
