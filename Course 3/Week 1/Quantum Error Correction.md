#quantum_error_correction #noise
> [!info] intro only
> this is just the basic idea so the links from the other notes go somewhere, fill it in when the course gets to QEC
## Why we need it
[[Noise Processes|noise]] causes errors, and the [[Quantum channels]] show what that does: the [[Bloch sphere]] gets squished and quantum information is lost

QEC is about getting that information back
## The classical idea: repetition code
send each bit 3 times
$$
0\to000\qquad1\to111
$$
if one bit flips ($000\to010$) you take a **majority vote** and still get $0$

this protects against the [[Binary symmetric channel]] as long as only 1 of the 3 bits flips
## Why quantum is harder
- **can't copy** a qubit (no-cloning theorem), so you can't just send $|\psi\rangle|\psi\rangle|\psi\rangle$
- **measuring destroys** superpositions, so you can't just look at the qubits to check for errors
- errors can be **continuous** (small rotations) not just flips
## The trick
- spread 1 **logical qubit** over many **physical qubits** using entanglement, eg. $\alpha|0\rangle+\beta|1\rangle\to\alpha|000\rangle+\beta|111\rangle$ (not a copy!)
- measure **only whether** an error happened and where (the **syndrome**), not the state itself
- fix it with a gate

this is where the ideas from [[Density matrix]] come in: unravellings and purification explain why fixing a few discrete errors is enough to fix any error
