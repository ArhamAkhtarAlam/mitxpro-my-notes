#textbook #entanglement #bell_inequality
*Quantum Computation and Quantum Information* §2.6 (p. 112–115). the chapter ends with the clearest example of how quantum and classical physics **really** differ. part of [[Quantum Computation and Quantum Information]], previous: [[Schmidt decomposition and purifications]]. course versions: [[Quantum weirdness]], [[CHSH inequality]], [[CHSH game]]
> [!quote] the chapter's 3 quotes
> - Einstein once asked Abraham Pais whether he really believed **the moon exists only when he looks at it**
> - "quantum phenomena do not occur in a Hilbert space, they occur in a laboratory" (Asher Peres)
> - "what is proved by impossibility proofs is lack of imagination" (John Bell)

## 2 views of the world
- **classical**: an object (a person, a book, a tennis ball) has properties like position that exist **whether or not anyone looks**. measuring just **reveals** them
- **quantum**: an unobserved qubit does **not** have definite properties like "spin in the $z$ direction" ($\sigma_z$) or "spin in the $x$ direction" ($\sigma_x$). quantum mechanics only gives the **probabilities** of each result when a measurement is done. the properties come **from** the measurement

many physicists (most famously Einstein) rejected the quantum view
## the EPR argument
in the 1935 "EPR paper", Einstein, Podolsky and Rosen tried to show quantum mechanics is **incomplete**
> [!important] element of reality
> ==if you can predict a property's value **with certainty**, immediately before measuring it, then that property is an "element of reality"==. EPR's claim: a complete theory must include every element of reality

their aim was to find elements of reality that quantum mechanics leaves out. the key ingredient is the singlet:
## Box 2.7: perfect anti-correlation
the **spin singlet** (named for historical reasons)
$$
|\psi\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2}
$$
^singlet

==measure spin along **any** axis $\vec v$ ($\vec v\cdot\vec\sigma$) on both qubits, and the 2 results are **always opposite**==: $+1$ on one means $-1$ on the other, whichever $\vec v$ you pick
**why.** let $|a\rangle,|b\rangle$ be the eigenstates of $\vec v\cdot\vec\sigma$, and write $|0\rangle=\alpha|a\rangle+\beta|b\rangle$, $|1\rangle=\gamma|a\rangle+\delta|b\rangle$
$$
\begin{aligned}
|01\rangle-|10\rangle&=(\alpha|a\rangle+\beta|b\rangle)(\gamma|a\rangle+\delta|b\rangle)-(\gamma|a\rangle+\delta|b\rangle)(\alpha|a\rangle+\beta|b\rangle)\\
&=\alpha\gamma|aa\rangle+\alpha\delta|ab\rangle+\beta\gamma|ba\rangle+\beta\delta|bb\rangle-\gamma\alpha|aa\rangle-\gamma\beta|ab\rangle-\delta\alpha|ba\rangle-\delta\beta|bb\rangle\\
&=(\alpha\delta-\beta\gamma)\big(|ab\rangle-|ba\rangle\big)
\end{aligned}
$$
$\alpha\delta-\beta\gamma$ is the determinant of the unitary $\begin{bmatrix}\alpha&\beta\\\gamma&\delta\end{bmatrix}$, so it's a phase $e^{i\theta}$
$$
\frac{|01\rangle-|10\rangle}{\sqrt2}=e^{i\theta}\,\frac{|ab\rangle-|ba\rangle}{\sqrt2}
$$
the singlet looks **the same in every basis** (up to a global phase you can't see), and it only ever has $ab$ or $ba$, never $aa$ or $bb$ (checked numerically with a random basis)
## why EPR thought this breaks quantum mechanics
1. Alice and Bob share a singlet, far apart
2. Alice measures $\vec v\cdot\vec\sigma$ and gets $+1$. now she can predict **with certainty** that Bob will get $-1$ along $\vec v$
3. Alice can do this for **any** $\vec v$, without touching Bob's qubit. so by EPR's criterion, Bob's spin along every $\vec v$ is an element of reality
4. but quantum mechanics only gives probabilities for $\vec v\cdot\vec\sigma$, it doesn't contain these values. so (EPR said) it's **incomplete**

the hope: a more classical theory where systems **have** definite properties, with quantum mechanics just a rough version of it. most physicists didn't buy the argument, but it took about **30 years** to find a way to **test** it: ==Bell's inequality, which nature experimentally **breaks**==
## Bell's inequality (the common sense version)
forget quantum mechanics for now, and use only common sense ideas about how the world works

![[Bell_inequality_setup.png]]

**the experiment**
- Charlie prepares 2 particles (any way he likes, as long as he can repeat it) and sends one to Alice, one to Bob
- Alice measures **one** of 2 properties $P_Q$ or $P_R$, picked by a coin flip after the particle arrives. results $Q=\pm1$, $R=\pm1$
- Bob measures $P_S$ or $P_T$, results $S=\pm1$, $T=\pm1$
- they measure **at the same moment** (causally disconnected), so Alice's measurement can't disturb Bob's result, because influences can't go faster than light

**the 2 common sense assumptions**

| assumption | meaning |
|---|---|
| **realism** | $Q,R,S,T$ all **have** values before anyone measures, the measurement just reveals them (like light revealing where a tennis ball is) |
| **locality** | what Alice does can't affect Bob's results, and vice versa |

**the algebra**
$$
QS+RS+RT-QT=(Q+R)S+(R-Q)T
$$
$Q,R=\pm1$, so **either** $Q+R=0$ **or** $R-Q=0$. the other one is $\pm2$, and $S,T=\pm1$, so
$$
QS+RS+RT-QT=\pm2
$$
**average over many runs.** let $p(q,r,s,t)$ be the chance that, before measuring, $Q=q$, $R=r$, $S=s$, $T=t$ (it can depend on how Charlie prepares and on noise)
$$
\begin{aligned}
\text{E}(QS+RS+RT-QT)&=\sum_{qrst}p(q,r,s,t)\,(qs+rs+rt-qt)\\
&\leq\sum_{qrst}p(q,r,s,t)\times2=2
\end{aligned}
$$
the average of a sum is the sum of averages
$$
\begin{aligned}
\text{E}(QS+RS+RT-QT)&=\sum_{qrst}p\,qs+\sum_{qrst}p\,rs+\sum_{qrst}p\,rt-\sum_{qrst}p\,qt\\
&=\text{E}(QS)+\text{E}(RS)+\text{E}(RT)-\text{E}(QT)
\end{aligned}
$$
putting the 2 together gives the **Bell inequality** (this form is the CHSH inequality)
$$
\text{E}(QS)+\text{E}(RS)+\text{E}(RT)-\text{E}(QT)\leq2
$$
^bell-inequality

==any world that's both realistic and local has to obey this==. each $\text{E}(\cdot)$ can be measured in the lab, since Alice and Bob only ever need one property each per run
> [!tip] what happens next (the course already did this)
> with a singlet and the right axes, quantum mechanics gives **$2\sqrt2\approx2.83$**, breaking the inequality. eg. $Q=Z_1$, $R=X_1$, $S=\frac{-Z_2-X_2}{\sqrt2}$, $T=\frac{Z_2-X_2}{\sqrt2}$ gives $\text{E}(QS)=\text{E}(RS)=\text{E}(RT)=\frac1{\sqrt2}$ and $\text{E}(QT)=-\frac1{\sqrt2}$ (checked numerically). see [[CHSH quantum strategy]]. I'll fill in the book's version when the next pages come

see also [[Bell states]], [[Reduced density operator]]
