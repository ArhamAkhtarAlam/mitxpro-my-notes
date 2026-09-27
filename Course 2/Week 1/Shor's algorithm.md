#shors_algorithm
Uses quantum [[Order finding algorithm|order finding]] to find the factors of an integer $N$
## Quantum circuit
The quantum circuit consists of 2 Quantum Registers each of 2L qubits
There are 4 main steps in Shor's Algorithm
- [[Hadamard Gate|Hadamard Gates]] in the first Quantum Register
- [[Modular Exponentiation|Modular exponentiation]] [[Unitary Operation]] on both the registers
- [[Quantum Fourier Transform|QFT (aka Quantum Fourier Transform)]] on the first register
- Measure the qubits in the first Register

![[Shor_algo.png]]
example by IBM
![[IBM_demonstrations.png]]