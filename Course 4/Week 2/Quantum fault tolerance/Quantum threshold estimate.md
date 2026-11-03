#threshold #fault_tolerance #steane_code
## a first estimate
classically the threshold came out at around $\frac16$, or $0.089$ for NAND gates ([[Threshold theorem#the classical thresholds]]). what about a quantum computer? put everything together for one encoded CNOT on the 7 qubit code ([[Transversal gates on stabilizer codes]]), and count the gates in the fault-tolerant procedure. part of [[Fault-tolerant quantum computing]]
## counting the gates

| part | count | why |
|---|---|---|
| the gate itself | 7 | a transversal CNOT: one per pair of qubits |
| error correction | $6\times4\times3=72$ | 6 stabilizer generators (3 $X$ type, 3 $Z$ type), each with 4 non-identity entries so 4 gates to measure it, and each measurement **repeated 3 times** for a majority vote, since the measurement itself is faulty ([[Fault-tolerant measurement]]) |
| **total** | **79** | |

^steane-cnot-count

==the error correction (72) far outweighs the gate (7)==
## the threshold
the construction should survive any **one** failure, so as in the [[Fault-tolerant NAND gate]], count every **pair** of the 79 gates as a fault path
$$
\begin{aligned}
c&=\binom{79}2=\frac{79\times78}2=3081\\
p_{th}&=\frac1c=\frac1{3081}\approx3.2\times10^{-4}
\end{aligned}
$$
^quantum-threshold

> [!important] the one idea
> ==a first estimate of the quantum threshold is around $10^{-4}$==, hundreds of times smaller than the classical ones. quantum fault tolerance is far more demanding, almost entirely because of the cost of measuring the syndromes fault tolerantly

| | gates per fault-tolerant step | fault paths $c$ | $p_{th}$ |
|---|---|---|---|
| classical NAND ([[Fault-tolerant NAND gate]]) | 6 | 15 | $\approx0.067$ |
| quantum CNOT, 7 qubit code | 79 | 3081 | $\approx3\times10^{-4}$ |

> [!extra] how rough is it?
> very. it leaves out the gates that make and check the cat states, the error correction on the **second** block, and the fact that the CNOT alone isn't universal ([[Transversal gates on stabilizer codes#but not universal]]). it also counts every pair of failures as fatal, which overcounts (like [[Fault-tolerant procedure#examples: computing NOT|15 being an overcount]] for the NAND). careful counts give thresholds from around $10^{-5}$ up to about $10^{-2}$ depending on the code and the noise model; the [[Surface code]] reaches about 1%

> [!exercise] try these
> ① with the threshold $\frac1{3081}$, is a gate with error $10^{-3}$ good enough? what about $10^{-4}$?
> ② if each syndrome measurement only had to be done **once**, what would the count and threshold be?
> ③ for $p=10^{-4}$, how many levels of recursion get each encoded gate below $10^{-15}$? (use [[Cost of fault tolerance#^levels-needed]] with $N/\epsilon$ replaced by $10^{15}$)

> [!answer]-
> ① $10^{-3}>3.2\times10^{-4}$: no, adding levels makes it worse. $10^{-4}$: yes, it's below
> ② $7+6\times4=31$ gates, $\binom{31}2=465$, so $p_{th}\approx2.2\times10^{-3}$. repeating the measurements costs almost a factor of 7 in the threshold
> ③ $p_{th}/p=3.25$, $\log_{10}3.25=0.511$. $\log_{10}(10^{15}/3081)=11.5$. so $2^k\geq22.5$ → $k=5$. close to the threshold, so lots of levels

see also [[Threshold theorem]], [[Cost of fault tolerance]], [[Fault-tolerant measurement]]

week hub: [[Principles of fault tolerance]]
