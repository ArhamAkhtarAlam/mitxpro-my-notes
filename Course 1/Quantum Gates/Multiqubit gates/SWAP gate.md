#gate #SWAP_gate
## What it does
It is a [[Quantum gate|quantum gate]] on 2 qubits
Swaps the states of the 2 qubits

used at the end of the [[Quantum Fourier Transform]] to put the qubits back in the right order
## Matrix
$$
\text{SWAP}=\begin{bmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{bmatrix}
$$
## Qiskit implementation
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.swap(0, 1)
```
## Visual representation
```visual
q_0: ─X─
      │
q_1: ─X─
```
## Truth Table
$$
\begin{array}{c|c}
x & \text{SWAP}(x)\\
\hline
|00\rangle & |00\rangle\\
|01\rangle & |10\rangle\\
|10\rangle & |01\rangle\\
|11\rangle & |11\rangle
\end{array}
$$
> [!tip]
> a SWAP is the same as 3 [[CNOT gate|CNOTs]] in a row (the middle one upside down)
