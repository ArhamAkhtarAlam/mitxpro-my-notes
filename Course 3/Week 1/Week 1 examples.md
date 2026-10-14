#examples #density_matrix #quantum_channel #noise
every worked example from Course 3 Week 1 in one place, fully worked. goes with [[Week 1 formulas]]; each one links to the note it comes from
## 1. density matrices
### the lecture's pair, measured 2 ways
from [[Density matrix#bipartite state example]]
$$
|\psi_{AB}\rangle=\sqrt{\tfrac34}\,|00\rangle+\sqrt{\tfrac14}\,|11\rangle
$$
**mixture 1**: B measures in $0/1$
$$
\begin{aligned}
\text{B gets 0 }(\tfrac34)&\Rightarrow\text{A is }|0\rangle\qquad\text{B gets 1 }(\tfrac14)\Rightarrow\text{A is }|1\rangle\\
\rho_1&=\tfrac34|0\rangle\langle0|+\tfrac14|1\rangle\langle1|=\frac14\begin{bmatrix}3&0\\0&1\end{bmatrix}
\end{aligned}
$$
**mixture 2**: B does a Hadamard first, then measures
$$
\begin{aligned}
\text{B gets 0 or 1 }(\tfrac12\text{ each})&\Rightarrow\text{A is }\sqrt{\tfrac34}|0\rangle\pm\sqrt{\tfrac14}|1\rangle\\
\rho_2&=\frac18\begin{bmatrix}3&\sqrt3\\\sqrt3&1\end{bmatrix}+\frac18\begin{bmatrix}3&-\sqrt3\\-\sqrt3&1\end{bmatrix}=\frac14\begin{bmatrix}3&0\\0&1\end{bmatrix}
\end{aligned}
$$
==$\rho_1=\rho_2$: completely different mixtures, the same state==. what B does can't change what A looks like on its own
### measuring one qubit, step by step
from [[Density matrix practice]] (same pair). measuring only B uses $I_A\otimes\Pi_b$
$$
\begin{aligned}
(I_A\otimes\Pi_0)|\psi_{AB}\rangle&=\sqrt{\tfrac34}\,|0_A0_B\rangle&p_{B,0}&=\tfrac34&\text{A}&=|0_A\rangle\\
(I_A\otimes\Pi_1)|\psi_{AB}\rangle&=\sqrt{\tfrac14}\,|1_A1_B\rangle&p_{B,1}&=\tfrac14&\text{A}&=|1_A\rangle
\end{aligned}
$$
(probability = squared length of what's left, then normalize). with the Hadamard on B first, each result has probability $\frac12$ and A is $0.87|0_A\rangle\pm0.50|1_A\rangle$. either way
$$
\rho_A=0.75\begin{bmatrix}1&0\\0&0\end{bmatrix}+0.25\begin{bmatrix}0&0\\0&1\end{bmatrix}
$$
### pure vs mixed: $|+\rangle$ vs a coin flip
from [[Pure and mixed states]]
$$
\underbrace{|+\rangle\langle+|=\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}}_{\text{pure}}\qquad\underbrace{\tfrac12|0\rangle\langle0|+\tfrac12|1\rangle\langle1|=\frac12\begin{bmatrix}1&0\\0&1\end{bmatrix}}_{\text{mixed}}
$$

| measure in | $\lvert+\rangle$ | coin flip |
|---|---|---|
| $0/1$ | 50 / 50 | 50 / 50 |
| $+/-$ | **100% $+$** | 50 / 50 |
| purity $\text{tr}(\rho^2)$ | 1 | $\frac12$ |

same diagonal, the difference is the off diagonal (coherence)
### purity of the course's state
from [[Pure and mixed states]]
$$
\rho=\frac14\begin{bmatrix}3&0\\0&1\end{bmatrix}\quad\Rightarrow\quad\text{tr}(\rho^2)=\Big(\tfrac34\Big)^2+\Big(\tfrac14\Big)^2=\tfrac{10}{16}=0.625<1
$$
so it's **mixed**. on the Bloch sphere: $r_z=\frac34-\frac14=0.5$, halfway up the $z$ axis, and $\frac{1+r^2}2=\frac{1+0.25}2=0.625$ ✅
### the 3 kinds of 2 qubit state
from [[Pure and mixed states#the course's 3 examples (2 qubits)]]

| state | $\text{tr}(\rho^2)$ | |
|---|---|---|
| pure $\lvert10\rangle$ | 1 | one bar |
| a mixture | $<1$ | bars everywhere |
| Bell $\frac1{\sqrt2}(\lvert00\rangle-\lvert11\rangle)$ | **1** | pure, even though each half alone is $\frac I2$ |

## 2. projectors and measurement
from [[Projectors]] and [[Kets and bras combined]]
### one state, 2 different measurements
$|\psi\rangle=\sqrt{0.7}\,|0\rangle+\sqrt{0.3}\,|1\rangle$
$$
\begin{aligned}
P(0)&=\langle\psi|\Pi_0|\psi\rangle=0.7&&\text{(then the state becomes }|0\rangle)\\
P(+)&=\langle\psi|\Pi_+|\psi\rangle=\frac{(\sqrt{0.7}+\sqrt{0.3})^2}2\approx0.958
\end{aligned}
$$
### what a ket-bra does to a state
read $|a\rangle\langle b|$ as "turn $b$ into $a$, everything else becomes $0$"
$$
\begin{aligned}
|0\rangle\langle0|\,(\alpha|0\rangle+\beta|1\rangle)&=\alpha|0\rangle&&\text{(keeps the }|0\rangle\text{ part)}\\
|0\rangle\langle1|\,(\alpha|0\rangle+\beta|1\rangle)&=\beta|0\rangle&&\text{(moves the }|1\rangle\text{ part into }|0\rangle)
\end{aligned}
$$
## 3. partial trace
from [[Partial trace]]
### the Bell state, term by term
$$
\begin{aligned}
\rho&=\tfrac12\big(|00\rangle\langle00|+|00\rangle\langle11|+|11\rangle\langle00|+|11\rangle\langle11|\big)\\
\rho_A=\text{tr}_B\,\rho&=\tfrac12|0\rangle\langle0|\cdot1+0+0+\tfrac12|1\rangle\langle1|\cdot1=\frac I2
\end{aligned}
$$
the cross terms die because B's bits don't match ($\langle1|0\rangle=0$): pure pair, completely mixed half
### 2 more

| state | $\rho_A$ | |
|---|---|---|
| $\sqrt{\frac34}\lvert00\rangle+\sqrt{\frac14}\lvert11\rangle$ | $\frac14\begin{bmatrix}3&0\\0&1\end{bmatrix}$ | the same as mixture 1 |
| $\lvert+\rangle\lvert0\rangle$ (no entanglement) | $\lvert+\rangle\langle+\rvert$ | still pure |

## 4. quantum channels
### dephasing on $|+\rangle$
from [[Dephasing channel]]
![[Dephasing channel#^dephasing-plus]]

- $p=0.1$: off diagonals $\times0.8$, the state moves in towards the $z$ axis
- $p=\frac12$: off diagonals gone, a 50/50 classical mix
- $|0\rangle$ and $|1\rangle$ don't change at all (no off diagonal)
### depolarizing on $|0\rangle$
from [[Depolarizing channel]], $\rho\to(1-\frac43p)\rho+\frac43p\,\frac I2$
$$
|0\rangle\langle0|\longrightarrow\begin{bmatrix}1-\frac23p&0\\0&\frac23p\end{bmatrix}\qquad\text{eg. }p=0.3:\ \begin{bmatrix}0.8&0\\0&0.2\end{bmatrix}
$$
the Bloch vector shrinks from length 1 to $1-\frac43p=0.6$, in every direction equally (checked numerically)
### amplitude damping
from [[Amplitude damping channel]], waiting one $T_1$ gives $\gamma=1-e^{-1}\approx0.632$
$$
\begin{aligned}
|1\rangle\langle1|&\longrightarrow\begin{bmatrix}\gamma&0\\0&1-\gamma\end{bmatrix}=\begin{bmatrix}0.632&0\\0&0.368\end{bmatrix}&&\text{(63\% has decayed to }|0\rangle)\\
|+\rangle\langle+|&\longrightarrow\frac12\begin{bmatrix}1+\gamma&\sqrt{1-\gamma}\\\sqrt{1-\gamma}&1-\gamma\end{bmatrix}\approx\begin{bmatrix}0.816&0.303\\0.303&0.184\end{bmatrix}
\end{aligned}
$$
unlike dephasing, the state is also pushed **towards $|0\rangle$** (checked numerically)
### binary symmetric channel
from [[Binary symmetric channel]]: each bit flips with probability $p=0.1$
$$
C=1-H(0.1)=1-\big(-0.1\log_20.1-0.9\log_20.9\big)\approx1-0.469=0.531\text{ bits per use}
$$
## 5. noise
from [[Noise power spectral density]] and [[Rabi oscillation]]
### TV static (ergodic)
every pixel random between 0 (black) and 1 (white), independent, no memory
- time average of 1 pixel = average of all pixels at one moment = **0.5** (grey, not black) → **ergodic** and **wide sense stationary**
- zero correlation time → flat PSD → **white noise**
### a bucket of batteries (stationary but not ergodic)
pick one battery from a bucket of 9 V and 1.5 V batteries: its voltage is constant in time (**stationary**), but its time average (9 V) isn't the average over the whole bucket → **not ergodic**
### Rabi oscillations with amplitude noise
$$
\langle Z\rangle(t)=\cos(\Omega_0t)\,e^{-\sigma^2t^2/2}
$$
the oscillation keeps its frequency but dies away with a **Gaussian** envelope. at $t=\frac1\sigma$ the envelope is $e^{-1/2}\approx0.61$, so it's lost about 40% of its size. bigger noise $\sigma$ = faster decay

see also [[Week 1 formulas]], [[Noise in quantum systems]]
