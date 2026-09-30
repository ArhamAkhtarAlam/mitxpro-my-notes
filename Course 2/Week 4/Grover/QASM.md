#QASM #IBM_quantum #programming #lab
**OpenQASM** (Open Quantum Assembly Language): a simple text language for writing quantum circuits, used by IBM's quantum computers. the Week 4 lab. part of [[Quantum optimization]]
## IBM Quantum
- IBM lets anyone run circuits on **real** quantum computers over the internet (or on a classical simulator)
- you can build circuits by dragging gates in the graphical **composer**, or write them as QASM text
- you pick how many times to run it (**shots**) and which machine (**backend**)
- runs wait in a **queue**, because the hardware is shared worldwide
- (IBM now needs everyone to have their **own** free account, which is why the course switched to that)
## the composer picture
- each horizontal line is a **qubit wire**, time goes left to right, qubits are labelled `q[0]`, `q[1]`, ...
- every qubit starts in $|0\rangle$
- the grey double line `c` is the **classical register** that stores measurement results
- a measurement block draws a line down to the classical bit it saves into
## syntax
```c
include "qelib1.inc";
qreg q[5];
creg c[5];

// This is a comment
measure q[0] -> c[0];
```

| line | what it does |
|---|---|
| `include "qelib1.inc";` | loads the standard gate library (X, Y, Z, H, CNOT...) |
| `qreg q[5];` | a quantum register of 5 qubits |
| `creg c[5];` | a classical register of 5 bits for results |
| blank line | fine, just for organising |
| `// ...` | a comment, ignored |
| `measure q[0] -> c[0];` | measure qubit 0 and store it in bit 0 (keeping `q[i] → c[i]` is tidy) |

> [!warning] the usual mistakes
> - **every** statement ends with a semicolon `;` (eg. `creg c[5]` without one is an error)
> - the file name in `include` needs its **quotes**
> - the composer always draws **all** the machine's qubits (eg. 5), even if you only use 2

## Grover in QASM
[[Grover's algorithm]] for 2 qubits, marked item $|11\rangle$. one iteration is enough for $N=4$
```c
include "qelib1.inc";
qreg q[2];
creg c[2];

// 1. equal superposition
h q[0];
h q[1];

// 2. oracle: flip the sign of |11>
cz q[0],q[1];

// 3. diffuser: reflect about the average
h q[0];
h q[1];
x q[0];
x q[1];
cz q[0],q[1];
x q[0];
x q[1];
h q[0];
h q[1];

measure q[0] -> c[0];
measure q[1] -> c[1];
```
on a perfect machine this gives `11` **100%** of the time (checked numerically). on real hardware you'll see a bit of noise in the other 3 results
> [!tip] the diffuser, piece by piece
> `h` then `x` on every qubit turns $|s\rangle$ into $|11\rangle$, the `cz` flips its sign, then `x` and `h` turn it back. so it flips the sign of $|s\rangle$ relative to everything else, which (up to a global phase) is the reflection $2|s\rangle\langle s|-I$

> [!info] today
> newer IBM systems use **OpenQASM 3** and most people write circuits in Python with **Qiskit**, but the idea is identical

see also [[Grover's algorithm]], [[Hadamard Gate]], [[CZ gate]], [[X gate]]
