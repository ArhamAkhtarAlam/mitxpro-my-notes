#gate #CNOT_gate #controlled_gate #entanglement
## What it does
It is a [[Quantum gate|quantum gate]] on 2 qubits: a **control** and a **target**
- control is $|0\rangle$ → do nothing
- control is $|1\rangle$ → apply an [[X gate]] to the target (flip it)

it's the main way to make **entanglement**: [[Hadamard Gate]] on the control then CNOT gives $\frac1{\sqrt2}(|00\rangle+|11\rangle)$
## Matrix
(order $|\text{control},\text{target}\rangle$)
$$
\text{CNOT}=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{bmatrix}
$$
## Qiskit implementation
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.cx(0, 1)   # control 0, target 1
```
> [!warning] Qiskit qubit order
> Qiskit writes states backwards ($|q_1q_0\rangle$) so the matrix Qiskit shows looks different from the one above, but it's the same gate
## Visual representation
```visual
q_0: ──■──
     ┌─┴─┐
q_1: ┤ X ├
     └───┘
```
## Truth Table
$$
\begin{array}{c|c}
x & \text{CNOT}(x)\\
\hline
|00\rangle & |00\rangle\\
|01\rangle & |01\rangle\\
|10\rangle & |11\rangle\\
|11\rangle & |10\rangle
\end{array}
$$
