#benchmarking #tomography #NISQ
Course 3, Week 4: **how well do our quantum states and gates actually work?** measuring how good a quantum computer is at the physical level
## recap: where we are
- [[NISQ]] computers: about 50 to a few thousand qubits, available now or soon, and **not error corrected**
- so how useful they are is limited by
  - their **gate fidelity** (how close each gate is to perfect)
  - the **types of gates** the hardware can do
  - the **circuit depth** they can handle before noise takes over
- [[Quantum volume]] rolls all of that into **one number** to compare different machines
- NISQ machines will probably run small, specific algorithms, eg. as a **co-processor** for a normal computer, like [[VQE]] finding the ground state energy of atoms and molecules

> [!note] transcript slip
> the transcript says "NIST computers" a few times, it means **NISQ** computers
## why benchmark?
```mermaid
flowchart LR
    N["NISQ machines<br/>(no error correction)"] --> B["need to know how<br/>good each gate is"]
    F["future fault tolerant machines<br/>(error corrected)"] --> B
    B --> U["understand how well we can<br/>prepare, operate and measure<br/>a quantum system"]
```
> [!important] either way you need it
> - big, universal quantum computers need **error-protected** qubits to run deep circuits ([[Fault-tolerant quantum computing]])
> - but whether it's a NISQ machine or a future error corrected one, you have to know how well the gates work **at the physical level**, with noise ([[Noise Processes]])
>
> the tomography methods from this week come back all through course 4, with fault tolerant error correction and the [[Threshold theorem|threshold theorem]]
## this week's plan
```mermaid
flowchart LR
    S["benchmark states<br/>(state tomography)"] --> P["use that to benchmark gates<br/>(process tomography)"] --> E["practical side:<br/>how much work it takes"] --> R["randomized benchmarking<br/>(much less work)"]
```
1. [[State tomography]] → figuring out what quantum state you actually made
2. [[Process tomography]] → using state tomography to figure out what a **gate** actually does
3. the practical side: how many measurements tomography takes (the **overhead**)
4. [[Randomized benchmarking]] → a smarter way to measure gate quality with way less overhead
## this week's notes
- [[State tomography]] → measuring the Bloch vector to rebuild ρ, and how it scales to many qubits
- [[State fidelity]] → one number (0 to 1) for how close the state you made is to the one you wanted

see also [[Quantum volume]], [[NISQ]], [[Realistic quantum computation]]
