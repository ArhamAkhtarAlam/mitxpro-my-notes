#extra #quantum_algorithm #oracle #phase_kickback
**extra** (not in the course): the first algorithm to show a quantum computer beating a classical one (Deutsch 1985, Deutsch–Jozsa 1992). a toy problem, but every idea in it ([[Phase kickback]], Hadamards before and after, interference) comes back in [[Bernstein-Vazirani algorithm|Bernstein–Vazirani]], [[Simon's algorithm|Simon]] and [[Shor's algorithm|Shor]]
## the problem
a black box computes $f:\{0,1\}^n\to\{0,1\}$, and you're **promised** $f$ is either
- **constant**: the same output for every input, or
- **balanced**: 0 for exactly half the inputs, 1 for the other half

which is it?

classically (with certainty) you might see the same answer $2^{n-1}$ times in a row and still not know, so worst case $2^{n-1}+1$ calls. quantumly: **one** call

## the circuit
![[Deutsch_Jozsa_circuit.png]]

(three input qubits here, the bottom qubit is the helper)
$$
\begin{aligned}
|0\rangle^{\otimes n}|1\rangle&\xrightarrow{H\text{ on all}}\frac1{\sqrt{2^n}}\sum_x|x\rangle\,|-\rangle\\
&\xrightarrow{U_f}\frac1{\sqrt{2^n}}\sum_x(-1)^{f(x)}|x\rangle\,|-\rangle\\
&\xrightarrow{H^{\otimes n}}\sum_y\left[\frac1{2^n}\sum_x(-1)^{f(x)+x\cdot y}\right]|y\rangle\,|-\rangle
\end{aligned}
$$

the middle step is [[Phase kickback]]: the helper in $|-\rangle$ turns "write $f(x)$" into "multiply by $(-1)^{f(x)}$"

look at the amplitude of $y=00\ldots0$:
$$
\frac1{2^n}\sum_x(-1)^{f(x)}=\begin{cases}\pm1&\text{constant}\\0&\text{balanced}\end{cases}
$$
^dj-amplitude

> [!important] the one idea
> ==the phases $(-1)^{f(x)}$ either all agree (and add up to $|00\ldots0\rangle$ with certainty) or exactly cancel (and $|00\ldots0\rangle$ never appears)==. measure: all zeros → constant, anything else → balanced

> [!eg] $n=2$, balanced $f(x_1x_2)=x_1$
> phases: $+1$ for 00, 01, $-1$ for 10, 11. the state after the oracle is $\frac12(|00\rangle+|01\rangle-|10\rangle-|11\rangle)=|-\rangle|+\rangle$. the Hadamards give $|1\rangle|0\rangle$: you measure **10**, not 00, so balanced ✓

with $n=1$ it's **Deutsch's algorithm**: is $f(0)=f(1)$? one call instead of two

## how impressive is it really
- against a **deterministic** classical computer: 1 call vs $2^{n-1}+1$, exponential
- against a **randomized** one: pick a few random inputs. if any two differ it's balanced; after $k$ equal answers, "constant" is wrong with probability at most $2^{1-k}$. so a handful of calls is enough in practice

so it's a proven separation, but only for exact answers and a black box ([[Quantum advantage]])

> [!exercise] try these
> **1** for constant $f=1$, what's the final state of the inputs?
> **2** run $n=2$ with $f=x_1\oplus x_2$. what do you measure?
> **3** why put the helper in $|1\rangle$ (then $|-\rangle$) and not $|0\rangle$?

> [!answer]-
> **1** $-|00\ldots0\rangle$: all zeros, with a global minus sign you can't see
> **2** phases $+,-,-,+$ = $|-\rangle|-\rangle$, Hadamards give **11**: balanced
> **3** with $|0\rangle$ the oracle writes $f(x)$ into the helper and entangles it, no phase kickback and no interference

see also [[Phase kickback]], [[Bernstein-Vazirani algorithm]], [[Hadamard Gate]], [[Grover's algorithm]]
