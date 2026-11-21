#extra #quantum_error_correction #surface_code #threshold
**extra** (not in the course as its own topic): the protected qubit you get by spreading one qubit of information over many physical ones. it's what the [[Bit flip code]], [[Shor code]], Steane code and [[Surface code]] are all building
## physical vs logical
- **physical qubit**: one actual device ([[Superconducting qubits|a transmon]], an ion, an atom). errors around $10^{-3}$ per gate
- **logical qubit**: the information stored in a **code**, as $|0_L\rangle$ and $|1_L\rangle$, spread over $n$ physical qubits. errors are caught by measuring stabilizers ([[Parity measurement]]) and fixed before they pile up

> [!important] the one idea
> ==a logical qubit only helps below threshold: if the physical error rate is under $p_{th}$, making the code bigger makes the logical error **exponentially** smaller==. above threshold, bigger codes just add more ways to fail ([[Threshold theorem]])

## how many physical qubits
a code is written $[\![n,k,d]\!]$: $n$ physical qubits, $k$ logical qubits, **distance** $d$ (the fewest single-qubit errors that can turn one code word into another). it fixes any $\left\lfloor\frac{d-1}2\right\rfloor$ errors

| code | $[\![n,k,d]\!]$ | fixes |
|---|---|---|
| [[Bit flip code]] | 3 qubits, bit flips only | 1 bit flip |
| [[Shor code]] | $[\![9,1,3]\!]$ | any 1 error |
| Steane ([[From Hamming to Steane]]) | $[\![7,1,3]\!]$ | any 1 error |
| 5-qubit code | $[\![5,1,3]\!]$ | any 1 error (the smallest possible) |
| [[Surface code]] | $[\![d^2,1,d]\!]$, plus $d^2-1$ measure qubits | $\frac{d-1}2$ errors |

## how fast the error drops
for the surface code, roughly
$$
p_L\approx A\left(\frac p{p_{th}}\right)^{\frac{d+1}2}
$$
^logical-error

with $A\sim0.1$ and $p_{th}\approx1\%$. every time $d$ goes up by 2, $p_L$ is divided by $\Lambda=\frac{p_{th}}p$

![[Logical_error_vs_distance.png]]

> [!eg] how big for $10^{-12}$?
> physical error $p=0.1\,p_{th}$, so $\Lambda=10$. need $0.1\times10^{-\frac{d+1}2}=10^{-12}$, so $\frac{d+1}2=11$, $d=21$
> $$
> 2d^2-1=2(441)-1=881\ \text{physical qubits per logical qubit}
> $$
> about a thousand. and a useful algorithm needs ~100–1000 logical qubits, so ~$10^5$–$10^6$ physical ones ([[Cost of fault tolerance]])

## milestones
- **break-even**: the logical qubit lasts longer than the best physical qubit in it. reached in the early 2020s (bosonic codes, then ions and superconducting chips)
- **below threshold**: Google's 105-qubit Willow chip (2024) ran surface codes with $d=3,5,7$ and the logical error dropped by $\Lambda\approx2.1$ each step, the first clear "bigger is better"
- **many logical qubits**: neutral-atom machines (Harvard/QuEra, 2023) ran circuits on dozens of logical qubits at once

## computing on them
storing isn't enough, you need logical gates
- **transversal** gates: do the gate qubit by qubit, errors can't spread ([[Transversal gates]], [[Transversal gates on stabilizer codes]])
- no code has a transversal universal gate set, so the missing $T$ gate comes from [[Magic state distillation]]
- on the surface code: moving and merging patches ([[Surface code logical operations]])

> [!exercise] try these
> **1** a $[\![7,1,3]\!]$ code: how many errors does it fix?
> **2** with $\Lambda=2$, how much bigger must $d$ get to cut $p_L$ by 1000?
> **3** why can't you just copy a qubit 3 times like the classical repetition code?

> [!answer]-
> **1** $\left\lfloor\frac{3-1}2\right\rfloor=1$
> **2** $2^{10}\approx1000$: 10 steps of +2, so $d$ goes up by 20
> **3** [[No-cloning theorem|no-cloning]]: the code spreads $\alpha|0\rangle+\beta|1\rangle$ into $\alpha|000\rangle+\beta|111\rangle$, it doesn't copy it

see also [[Detecting and correcting errors]], [[Principles of fault tolerance]], [[Fault-tolerant quantum computing]], [[NISQ]], [[Quantum Error Correction]]
