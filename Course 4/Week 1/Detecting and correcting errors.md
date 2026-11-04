#quantum_error_correction #noise
Course 4, Week 1: **strategies for detecting and correcting errors** in quantum systems. simple quantum error correcting codes, and why parity measurements matter
## the problem
- a transistor fails about 1 in $10^{20}$ times, a qubit about 1 in $10^3$ to $10^4$
- big algorithms need far more gates than that, so we need qubits that are more **resilient**
- the fix: **redundancy**, spread one qubit over several, at the cost of **overhead**

```mermaid
flowchart TD
    P["physical qubits<br/>(error p)"] --> R["add redundancy<br/>(encode 1 qubit on 3)"]
    R --> T{"is p below<br/>the threshold?"}
    T -- "yes" --> W["logical error ~cp², a net win"]
    W --> S["find errors with parity checks<br/>(the syndrome), fix with X"]
    T -- "no" --> L["more qubits, more errors"]
```
## the bit flip code
- [[Bit flip code]] → encode $\alpha|0\rangle+\beta|1\rangle$ as $\alpha|000\rangle+\beta|111\rangle$ with two CNOTs, it fixes 1 flip, fails with $3p^2-2p^3$, the **threshold** $p<\frac1c$, correcting with $X$ gates, more redundancy and more levels
- [[Parity measurement]] → parity checks onto ancillas give the **syndrome** (if and where an error happened) without revealing $\alpha$ or $\beta$
- [[Decoding the bit flip code]] → the no-ancilla way: run the encoder backwards, measure qubits 2 and 3, fix qubit 1. and why a $\sigma_z$ on any qubit is a $\sigma_z$ on the encoded qubit
- [[Bit flip code practice]] → every case from $|\psi_0\rangle$ to $|\psi_3\rangle$, and why only $11$ needs a fix
## quantum codes
- [[Phase flip code]] → the bit flip code with Hadamards around it: $|0_L\rangle$ = even states, $|1_L\rangle$ = odd states. fixes one $\sigma_z$, but makes $\sigma_x$ errors 3× worse
- [[Phase flip code practice]] → the Hadamards turn a $\sigma_z$ into a $\sigma_x$, then it's the bit flip code again
- [[Shor code]] → concatenate the two: a phase code of bit codes, 9 qubits. fixes any $\sigma_x$, $\sigma_y$ or $\sigma_z$ on one qubit, and so **any** one qubit error (the Paulis are a basis, and the measurement makes the error discrete)
## reliable computation
- [[Computational capacity]] → Shannon's channel capacity: below it, codes make the error exponentially close to 0. the setup for the **threshold** for noisy computers
- [[Triple modular redundancy]] → von Neumann's question for **gates** plus noise: repeat a circuit 3 times and majority vote. it helps if $p<\frac13$, but the vote is a single point of failure and there's **no threshold** ($p<\frac1{3N}$ moves with circuit size)
## also this week
- [[Course 4 Week 1 formulas]] → every formula from this week on one page, with examples and exercises

next week: [[Principles of fault tolerance]] ([[Threshold theorem]], [[Fault-tolerant NAND gate]], [[Recursive fault tolerance]]) · coming up: [[Logical qubit]]

see also [[Quantum Error Correction]] (the intro from course 3), [[Noise Processes]], [[Quantum channels]]

course overview: [[Requirements for large scale quantum computation]]
