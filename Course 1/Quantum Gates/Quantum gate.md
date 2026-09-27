#gate
## What it is
A quantum gate is an operation on qubits, like logic gates (AND, OR, NOT) in a normal computer

Every quantum gate is a [[Unitary Operation]] so it can be written as a matrix
- 1 qubit → $2\times2$ matrix
- 2 qubits → $4\times4$ matrix
- $n$ qubits → $2^n\times2^n$ matrix

On the [[Bloch sphere]] a single qubit gate is just a **rotation** of the sphere
> [!important] quantum gates are always reversible
> because they're unitary you can always undo them (apply $U^\dagger$). normal gates like AND aren't reversible, if AND gives 0 you can't tell what went in
## Single qubit gates
- [[Identity gate]]
- [[X gate]]
- [[Y gate]]
- [[Z gate]]
- [[Hadamard Gate]]
- [[Sqrt(X) Gate]]
- [[Phase shift]] (and the $S$ and $T$ gates)
## Multiqubit gates
- [[CNOT gate]]
- [[CZ gate]]
- [[SWAP gate]]
- [[Toffoli gate]]
