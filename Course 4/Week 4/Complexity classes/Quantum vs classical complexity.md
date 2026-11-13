#complexity #complexity_class #BQP
where **BQP** (what a quantum computer can do efficiently) sits among the classical classes, and which problems get a real quantum speed up. part of [[Complexity classes]]

## the picture
![[Complexity_hierarchy.png]]

- **P ⊆ BQP**: a quantum computer can do anything a classical one can, using reversible gates
- **BQP reaches outside P**: factoring and discrete logarithms are in BQP ([[Shor's algorithm]]), but no polynomial classical algorithm for them is known
- **BQP doesn't seem to contain the NP-complete problems** ([[NP-complete]])
- **BQP ⊆ PSPACE**: a classical computer can find a quantum circuit's output probability by adding up the amplitudes **one path at a time**, reusing the same memory. it takes exponential time but only polynomial memory. so a quantum computer never solves anything outside PSPACE

the full chain is in [[Complexity classes#^containments]]

## where the speed ups come from
> [!important] structure
> ==quantum computers win big when a problem has a mathematical structure they can exploit==, eg. the hidden period in factoring that the [[Quantum Fourier Transform]] picks out. without that structure the best you usually get is Grover's square root

| problem | best classical | quantum | speed up |
|---|---|---|---|
| factoring an $n$ bit number | about $e^{c\,n^{1/3}(\log n)^{2/3}}$ (number field sieve) | polynomial ([[Shor's algorithm]]) | exponential (believed) |
| search $N$ unsorted items | $\frac N2$ tries on average, $N$ at worst | about $\frac\pi4\sqrt N$ ([[Grover's algorithm]]) | quadratic |
| NP-complete, $n$ bits (eg. circuit SAT) | about $2^n$ | about $2^{n/2}$ with Grover | quadratic, still exponential |
| multiplying two numbers | about $n^2$ | no better | none |

> [!eg] searching a million items
> classically about $500\,000$ checks on average. Grover needs about $\frac\pi4\sqrt{10^6}\approx785$. a huge saving, but only a **polynomial** one: it doesn't move a problem from one class to another

## none of it is proven
- nobody has proven factoring isn't in P. a clever classical algorithm could exist: unlikely, but not impossible
- even P ≠ BQP is unproven, and it would be very hard to prove: since P ⊆ BQP ⊆ PSPACE, proving P ≠ BQP would also prove **P ≠ PSPACE**, a famous open problem
- so every claim of [[Quantum advantage|quantum advantage]] rests on the best **known** classical algorithms plus conjectures. that's why demonstrations ([[Quantum supremacy]]) pick problems where the evidence is strongest, like sampling from random circuits

> [!exercise] try these
> ① about how many Grover iterations does it take to search $10^{12}$ items? how many classical checks on average?
> ② why can't a quantum computer efficiently solve a problem that needs more than polynomial memory on a classical computer?
> ③ someone finds a fast classical algorithm for factoring. does that prove BPP = BQP?
> ④ a company says its quantum computer solves an NP-complete problem exponentially faster. why be sceptical?

> [!answer]-
> ① $\frac\pi4\sqrt{10^{12}}=\frac\pi4\times10^6\approx7.9\times10^5$ iterations, vs about $5\times10^{11}$ classical checks
> ② BQP ⊆ PSPACE: anything a quantum computer does in polynomial time, a classical computer can also do with polynomial memory (slowly). so a problem that really needs more memory can't be in BQP
> ③ no. factoring would just stop being an example of a quantum speed up. BPP = BQP needs a fast classical algorithm for a BQP-complete problem like [[Quantum circuit evaluation]]
> ④ there's no known quantum algorithm that does it, and NP-complete problems don't seem to have the structure quantum speed ups need. Grover alone only gives a square root, which is still exponential

previous: [[Quantum circuit evaluation]]

see also [[Promise, sampling and relation problems]], [[Quantum volume]]

week hub: [[Computational complexity]]
