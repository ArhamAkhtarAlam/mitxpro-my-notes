#extra #solovay_kitaev #gate_synthesis #universal_gates
**extra** (not in the course): any single qubit gate can be built **efficiently** out of a small fixed set of gates. why every machine only needs a few native gates ([[Quantum volume]])
## the problem
real hardware can only do a handful of gates directly, eg. [[Hadamard Gate|H]] and $T$ (a $\frac\pi4$ [[Phase shift]]). but algorithms want **any** rotation, like $R_z(0.3)$. you can't make most rotations **exactly** from H and T, only approximately
## the theorem
> [!important] Solovay–Kitaev
> ==if a finite gate set is **universal** (its products can get arbitrarily close to any gate), then any single qubit gate can be approximated to accuracy $\varepsilon$ using only==
> $$
> O\big(\log^c(1/\varepsilon)\big)
> $$
> gates from the set, with $c\approx3$ to $4$ in the original algorithm (and there's a matching algorithm to actually find the sequence)

a **polylog** cost: 10× more accuracy only costs a few more gates. brute force search would need exponentially long searches
## trying it by brute force
![[Solovay_Kitaev_search.png]]
(my brute force search over every H/T sequence up to length 32, about 6 million sequences, aiming at one fixed gate: the error drops, but slowly and in jumps)

the Solovay–Kitaev algorithm does much better: it starts from a rough approximation and **recursively** fixes the leftover error using commutators of shorter sequences
## why it matters
- **compilers**: turning an algorithm's arbitrary rotations into what the hardware can run
- **error correction**: fault tolerant codes can only do a few gates (like H, S, CNOT and T) safely, so everything must be built from those ([[Fault-tolerant quantum computing]])
- the number of **T gates** is often the main cost of a fault tolerant algorithm, and modern methods (better than Solovay–Kitaev) get about $3\log_2(1/\varepsilon)$ T gates per rotation

see also [[Quantum gate]], [[Quantum volume]], [[Phase shift]]
