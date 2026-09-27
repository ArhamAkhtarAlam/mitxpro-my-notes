#bell #CHSH_game #entanglement #quantum_foundations
how Alice and Bob can win the [[CHSH game]] **more than 75%** of the time by sharing an [[Entangled Photons generation and detection|entangled pair]]
## the shared state
$$
\frac1{\sqrt2}(|00\rangle+|11\rangle)
$$
(not the singlet $\frac1{\sqrt2}(|01\rangle-|10\rangle)$ from [[Quantum weirdness]], because that one gives **opposite** answers and the game mostly wants the **same** answer)

> [!tip]- turning the singlet into this state
> Bob just applies an [[X gate]] then a [[Z gate]] to his qubit
> $$
> \tfrac1{\sqrt2}(|01\rangle-|10\rangle)\xrightarrow{X_B}\tfrac1{\sqrt2}(|00\rangle-|11\rangle)\xrightarrow{Z_B}\tfrac1{\sqrt2}(|00\rangle+|11\rangle)
> $$
## the key fact
> [!important] same measurement → same answer
> if Alice and Bob **both** measure the same observable
> $$
> \alpha\,\sigma_z+\beta\,\sigma_x\qquad(\alpha,\beta\text{ real},\ \alpha^2+\beta^2=1)
> $$
> they **always get the same outcome**
>
> these are all the measurements on the $x$–$z$ great circle of the [[Bloch sphere]] (the vertical slice)

but if they both measure $\sigma_y$ they always get **opposite** outcomes
### proof for the 2 easy cases
**$\alpha=1$ (that's $\sigma_z$):** they're both measuring in the $|0\rangle,|1\rangle$ basis, and the state is $|00\rangle$ or $|11\rangle$, so they either both get 0 or both get 1

**$\alpha=0$ (that's $\sigma_x$):** rewrite the state in the $|+\rangle,|-\rangle$ basis
$$
\frac1{\sqrt2}(|00\rangle+|11\rangle)=\frac1{\sqrt2}(|{+}{+}\rangle+|{-}{-}\rangle)
$$
so if Alice gets $+$, Bob's qubit is $|+\rangle$, and if Alice gets $-$, Bob's is $|-\rangle$. same answer again
> [!example]- proof for any α
> any measurement on that great circle is a basis $|v\rangle=\cos\theta|0\rangle+\sin\theta|1\rangle$ and $|v^\perp\rangle=-\sin\theta|0\rangle+\cos\theta|1\rangle$
>
> multiply it out and you get the same state back no matter what $\theta$ is
> $$
> \frac1{\sqrt2}(|00\rangle+|11\rangle)=\frac1{\sqrt2}(|vv\rangle+|v^\perp v^\perp\rangle)
> $$
> so whatever Alice gets, Bob gets the same

and when they measure in **different** bases, $\theta_A$ and $\theta_B$ apart
$$
P(\text{same answer})=\cos^2(\theta_A-\theta_B)
$$
## the strategy
| player | gets | measures in |
|---|---|---|
| Alice | $a=0$ | $\lvert0\rangle,\lvert1\rangle$ basis (angle $0^\circ$) |
| Alice | $a=1$ | $\lvert+\rangle,\lvert-\rangle$ basis (angle $45^\circ$) |
| Bob | $b=0$ | the $s$ basis (angle $+22.5^\circ$) |
| Bob | $b=1$ | the $t$ basis (angle $-22.5^\circ$) |

they output $0$ for the first basis state and $1$ for the other one

![[CHSH_quantum_strategy.png]]

> [!info] where the lecture stops
> the lecture defines the $s$ and $t$ axes but stops before giving their angles. the $\pm22.5^\circ$ above are the standard choice (checked numerically)
### why it wins 85.4%
| $a$ | $b$ | want | bases | angle apart | P(win) |
|---|---|---|---|---|---|
| 0 | 0 | same | $0/1$ vs $s$ | $22.5^\circ$ | $\cos^2 22.5^\circ\approx0.854$ |
| 0 | 1 | same | $0/1$ vs $t$ | $22.5^\circ$ | $\cos^2 22.5^\circ\approx0.854$ |
| 1 | 0 | same | $+/-$ vs $s$ | $22.5^\circ$ | $\cos^2 22.5^\circ\approx0.854$ |
| 1 | 1 | different | $+/-$ vs $t$ | $67.5^\circ$ | $1-\cos^2 67.5^\circ\approx0.854$ |

every case wins with the same probability so
$$
P(\text{win})=\cos^2\frac\pi8\approx85.4\%>75\%
$$
Bob's bases sit **in between** Alice's, so he's always close to what she measured, except in the $a=b=1$ case where he's far away, which is exactly when they want different answers

> [!note] angles on the Bloch sphere
> these angles are in the $\cos\theta|0\rangle+\sin\theta|1\rangle$ picture. on the [[Bloch sphere]] every angle **doubles**: $|0\rangle$ and $|+\rangle$ are $90^\circ$ apart, and $s,t$ are at $\pm45^\circ$
## why it matters
> [!important] quantum beats classical
> no classical strategy can beat 75% (see [[CHSH game#the best classical strategy wins 75%]]), but sharing entanglement gets 85.4%. that's Bell's result: quantum mechanics can't be explained by any **local hidden variable** theory
>
> 85.4% is also the best any quantum strategy can do (called **Tsirelson's bound**)

see also [[CHSH game]], [[Quantum weirdness]], [[Ekert91]]
