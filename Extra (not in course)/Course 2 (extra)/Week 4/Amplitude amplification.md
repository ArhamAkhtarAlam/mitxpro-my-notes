#extra #amplitude_amplification #grover #quantum_algorithm
**extra** (not in the course as its own topic): [[Grover's algorithm]] made general. if **any** algorithm succeeds with probability $p$, you can boost it to almost 1 with about $\frac1{\sqrt p}$ repeats, instead of the $\frac1p$ tries classical repetition needs
## the setup
an algorithm $\mathcal A$ (any circuit) makes
$$
\mathcal A|0\rangle=\sin\theta\,|\text{good}\rangle+\cos\theta\,|\text{bad}\rangle,\qquad p=\sin^2\theta
$$
Grover is the special case $\mathcal A=H^{\otimes n}$ with $p=\frac MN$

## one round = two reflections
- **1** flip the sign of the good part ($S_\chi$, an oracle that recognises good answers)
- **2** reflect about the starting state $\mathcal A|0\rangle$ (that's $\mathcal AS_0\mathcal A^\dagger$, with $S_0$ flipping the sign of $|0\rangle$)

two reflections make a **rotation** by $2\theta$, always towards $|\text{good}\rangle$

![[Amplitude_amplification_rotation.png]]

after $k$ rounds
$$
P(\text{good})=\sin^2\big((2k+1)\theta\big),\qquad k\approx\frac\pi{4\theta}\approx\frac\pi4\frac1{\sqrt p}
$$
^amplitude-amplification

> [!important] the one idea
> ==amplitude amplification turns "succeeds with probability $p$" into "succeeds almost surely" in $O(1/\sqrt p)$ steps: a quadratic speed up for anything with a checkable answer==

> [!eg] $p=0.06$
> $\theta=\arcsin\sqrt{0.06}\approx14.2°$
>
> | rounds $k$ | angle $(2k+1)\theta$ | $P(\text{good})$ |
> |---|---|---|
> | 0 | 14° | 0.06 |
> | 1 | 43° | 0.46 |
> | 2 | 71° | 0.89 |
> | 3 | 99° | **0.97** |
> | 4 | 128° | 0.63 (overshot) |
>
> classically you'd expect $\frac1{0.06}\approx17$ tries

## careful
- **overshooting**: too many rounds rotate past $|\text{good}\rangle$ and $P$ goes back down. you need to know $p$ roughly. if you don't: try a random number of rounds, or use fixed-point versions that never overshoot
- **amplitude estimation**: run the rounds inside [[Quantum Phase Estimation]] to **measure** $\theta$, so you learn $p$ to accuracy $\varepsilon$ with $\sim\frac1\varepsilon$ uses of $\mathcal A$ instead of $\frac1{\varepsilon^2}$ classical samples (quadratic speed up for Monte Carlo, eg. pricing in finance)
- it's used inside [[HHL algorithm|HHL]] to boost its success chance, and in many search and optimization ideas ([[Quantum optimization]])

> [!exercise] try these
> **1** $p=\frac14$: how many rounds?
> **2** $p=10^{-6}$: about how many rounds vs classical tries?
> **3** why does the speed up stop being useful if each round is very expensive?

> [!answer]-
> **1** $\theta=30°$, one round gives $3\theta=90°$: $P=1$ exactly
> **2** $\frac\pi4\times1000\approx785$ rounds vs ~$10^6$ classical tries
> **3** it's only quadratic: if a round costs much more than a classical try, $\sqrt{N}$ expensive steps can lose to $N$ cheap ones

see also [[Grover's algorithm]], [[Quantum optimization]], [[Quantum Phase Estimation]], [[Phase kickback]]
