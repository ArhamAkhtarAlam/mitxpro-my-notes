#formula_sheet #information_theory #entanglement #QKD
every formula from Course 3 Week 2 in one place, with an **eg.** under each formula showing how it's used, and an **exercise** for each section (answers fold out, try them first). each section links to the note with the full explanation. (all numbers checked numerically)
## 1. Shannon entropy
from [[Shannon entropy]]

**entropy** = how many bits of surprise (information) a random variable gives, on average
![[Shannon entropy#^shannon-entropy]]

> [!eg] eg.
> - **fair coin**: $-\big(\frac12\log_2\frac12+\frac12\log_2\frac12\big)=-\big(\frac12(-1)+\frac12(-1)\big)=1$ bit
> - **fair dice**: 6 outcomes at $\frac16$ each: $-6\cdot\frac16\log_2\frac16=\log_26\approx2.58$ bits
> - **uneven**: $p=\frac12,\frac14,\frac14$: $-\big(\frac12(-1)+\frac14(-2)+\frac14(-2)\big)=0.5+0.5+0.5=1.5$ bits
>
> (handy: $\log_2\frac12=-1$, $\log_2\frac14=-2$, $\log_2\frac18=-3$)

**binary entropy** (2 outcomes, chances $p$ and $1-p$)
![[Shannon entropy#^binary-entropy]]

> [!eg] eg. a coin that lands heads 10% of the time
> $$
> \begin{aligned}
> H(0.1)&=-0.1\log_2(0.1)-0.9\log_2(0.9)\\
> &=-0.1(-3.32)-0.9(-0.152)=0.332+0.137\approx0.469\text{ bits}
> \end{aligned}
> $$
> less than 1: you can usually guess the answer, so each flip tells you less

**mutual information** = how much knowing $Y$ tells you about $X$
![[Shannon entropy#^mutual-information]]

> [!eg] eg. a fair bit sent down a line that flips it 10% of the time
> before: $H(X)=1$. after seeing $Y$, the only doubt left is "was it flipped?", so $H(X|Y)=H(0.1)=0.469$. $I=1-0.469=0.531$ bits get through per use

> [!exercise] exercise
> (a) $H$ of a variable with chances $\frac14,\frac14,\frac14,\frac14$ (b) $H(0.2)$ (c) why is $H(0)=0$?

> [!answer]- answer
> (a) $-4\cdot\frac14\log_2\frac14=-(-2)=2$ bits (4 equal outcomes = 2 bits)
> (b) $-0.2\log_20.2-0.8\log_20.8=0.2(2.32)+0.8(0.322)=0.464+0.258\approx0.722$ bits
> (c) the outcome is certain, so there's no surprise (and $0\cdot\log_20$ counts as 0)

## 2. Von Neumann entropy
from [[Von Neumann entropy]]

the quantum version: Shannon entropy of the **eigenvalues** $\lambda_k$ of $\rho$
![[Von Neumann entropy#^von-neumann]]

> [!eg] eg. 3 states
> - **pure**, eg. $|+\rangle\langle+|$: eigenvalues $1,0$, so $S=-1\log_21=0$ (no uncertainty)
> - **completely mixed** $\frac I2$: eigenvalues $\frac12,\frac12$, so $S=1$ (the maximum for a qubit)
> - $\rho=\frac14\begin{bmatrix}3&0\\0&1\end{bmatrix}$: eigenvalues $\frac34,\frac14$ (already diagonal), so $S=H(0.25)\approx0.811$

> [!exercise] exercise
> find $S(\rho)$ for $\rho=\begin{bmatrix}0.8&0.2\\0.2&0.2\end{bmatrix}$

> [!answer]- answer
> **1. eigenvalues**: trace $=1$, determinant $=0.8\times0.2-0.2\times0.2=0.12$. they solve $\lambda^2-\lambda+0.12=0$
> $$
> \lambda=\frac{1\pm\sqrt{1-4(0.12)}}2=\frac{1\pm\sqrt{0.52}}2=\frac{1\pm0.721}2=0.861,\ 0.139
> $$
> **2. entropy**: $S=-0.861\log_2(0.861)-0.139\log_2(0.139)=0.861(0.217)+0.139(2.84)=0.186+0.396\approx0.58$
>
> careful: using the **diagonal** ($0.8,0.2$) instead would give $H(0.2)=0.72$, which is wrong. always use the eigenvalues

## 3. channel capacity
from [[Channel capacity]]

the most information per use you can send, choosing the best way to use the channel
![[Channel capacity#^capacity]]

**binary symmetric channel** (each bit flips with chance $p$)
$$
C=1-H(p)
$$
> [!eg] eg. $p=0.1$
> $C=1-H(0.1)=1-0.469=0.531$ bits per use. so to send 1000 bits reliably you need about $\frac{1000}{0.531}\approx1880$ uses (with good error correction)

**classical vs quantum** (sending classical or quantum information, through classical or quantum channels)
$$
C_{CC}\;\le\;C_{QC},\,C_{CQ}\;\le\;C_{QQ}
$$
> [!exercise] exercise
> capacity of a binary symmetric channel with (a) $p=0.25$ (b) $p=0.5$ (c) $p=0.9$

> [!answer]- answer
> (a) $1-H(0.25)=1-0.811=0.189$ bits
> (b) $1-H(0.5)=1-1=0$: the output is a pure coin flip, nothing gets through
> (c) $1-H(0.9)=1-0.469=0.531$, the same as $p=0.1$! if 90% of bits flip, just flip them all back

## 4. the CHSH game
from [[CHSH game]] and [[Quantum weirdness]]

the referee sends random questions $a,b\in\{0,1\}$, Alice and Bob answer $x,y\in\{0,1\}$ without talking. they **win** if
![[CHSH game#^chsh-rule]]

(answers must **differ** only when both questions are 1, otherwise they must **match**)

> [!eg] eg. the strategy "always answer 0"
>
> | $a,b$ | need $x\oplus y$ | they give $0\oplus0=0$ | win? |
> |---|---|---|---|
> | 0,0 | 0 | 0 | ✅ |
> | 0,1 | 0 | 0 | ✅ |
> | 1,0 | 0 | 0 | ✅ |
> | 1,1 | 1 | 0 | ✗ |
>
> wins 3 out of 4 question pairs: 75%

**the classical limit**
![[CHSH game#^classical-limit]]

> [!example] why 75% is the best: try to win all 4
> call Alice's answers $x_0,x_1$ (to question 0 and 1) and Bob's $y_0,y_1$. winning all 4 needs
> $$
> x_0+y_0=0\qquad x_0+y_1=0\qquad x_1+y_0=0\qquad x_1+y_1=1\pmod2
> $$
> add all 4: the left side is $2x_0+2x_1+2y_0+2y_1$, which is always even ($=0$ mod 2), but the right side is $1$. impossible, so at least 1 of the 4 must fail. random strategies are just mixtures of fixed ones, so they can't do better either

> [!exercise] exercise
> Alice always answers $x=a$ (her question), Bob always answers $y=0$. what's their win rate?

> [!answer]- answer
> $x\oplus y=a$. need $a\cdot b$. $(0,0)$: $0=0$ ✅. $(0,1)$: $0=0$ ✅. $(1,0)$: $1\neq0$ ✗. $(1,1)$: $1=1$ ✅. so 3/4 = 75% again

## 5. the CHSH inequality and the quantum strategy
from [[CHSH inequality]] and [[CHSH quantum strategy]]

**the inequality** (each $M$ is a measurement giving $\pm1$; local realism keeps the sum between $-2$ and $2$)
![[CHSH inequality#^chsh-inequality]]

**quantum** (with the singlet $|\Psi^-\rangle$): each term is $\pm\frac1{\sqrt2}$, all pointing the same way
$$
\langle Q\rangle=-\tfrac1{\sqrt2}-\tfrac1{\sqrt2}-\tfrac1{\sqrt2}-\tfrac1{\sqrt2}=-2\sqrt2\approx-2.83<-2
$$
**the link to the game**
![[CHSH inequality#^win-from-S]]

> [!eg] eg.
> classical best $S=2$: $\frac12+\frac28=0.75$ ✅. quantum $S=2\sqrt2$: $\frac12+\frac{2\sqrt2}8=0.5+0.354=0.854$

**entangled photons** ($\frac{|00\rangle+|11\rangle}{\sqrt2}$) measured by polarizers at angles $\theta_A,\theta_B$
![[CHSH quantum strategy#^same-answer]]

> [!eg] eg. the winning angles
> the strategy uses angles that are $22.5°=\frac\pi8$ apart for the 3 "match" question pairs: $P(\text{same})=\cos^2(22.5°)=0.924^2\approx0.854$ ✅. for the "differ" pair they're $67.5°$ apart: $P(\text{same})=\cos^2(67.5°)\approx0.146$, so $P(\text{differ})=0.854$ ✅. every question pair wins 85.4%

**from an average to a probability** (for a measurement $A$ with results $\pm1$)
$$
P(+1)=\frac{1+\langle A\rangle}2\qquad P(-1)=\frac{1-\langle A\rangle}2
$$
> [!eg] eg. Bob's measurement $B_s=\frac1{\sqrt2}(\sigma_x+\sigma_z)$ when his qubit is $|0\rangle$
> $$
> \begin{aligned}
> B_s&=\tfrac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}\qquad\langle0|B_s|0\rangle=\text{the top left entry}=\tfrac1{\sqrt2}\approx0.707\\
> P(y=0)&=\frac{1+0.707}2\approx0.854=\cos^2\tfrac\pi8
> \end{aligned}
> $$

> [!exercise] exercise
> (a) with $\frac{|00\rangle+|11\rangle}{\sqrt2}$, what's $P(\text{same})$ for polarizers $0°$ and $45°$? and $0°$ and $90°$? (b) what win rate does $S=2.4$ give (eg. a noisy experiment)?

> [!answer]- answer
> (a) $\cos^2(45°)=\frac12$ (no correlation at all). $\cos^2(90°)=0$ (always different)
> (b) $\frac12+\frac{2.4}8=0.5+0.3=0.8$: 80%, still above the classical 75%, so it still proves entanglement

## 6. entanglement and the Schmidt decomposition
from [[Defining entanglement]], [[Schmidt decomposition]] and [[Schmidt number]]

**entangled** = not a product of 2 separate states
![[Defining entanglement#^entangled-def]]

> [!eg] eg. a quick test for 2 qubits
> write $|\psi\rangle=\alpha|00\rangle+\beta|01\rangle+\gamma|10\rangle+\delta|11\rangle$. it's a **product** exactly when $\alpha\delta-\beta\gamma=0$
> - $\frac{|00\rangle+|01\rangle+|10\rangle+|11\rangle}2$: $\frac14-\frac14=0$ → product (it's $|+\rangle|+\rangle$)
> - $\frac{|00\rangle+|11\rangle}{\sqrt2}$: $\frac12-0=\frac12\neq0$ → entangled

**Schmidt decomposition**: any 2 part pure state can be written with matching basis states
![[Schmidt decomposition#^schmidt-form]]

the $\lambda_k$ are the eigenvalues of $\rho_A$ (and of $\rho_B$). the **Schmidt number** = how many $\lambda_k$ aren't 0. 1 = product, more = entangled

> [!eg] eg.
> - $\sqrt{0.9}|00\rangle+\sqrt{0.1}|11\rangle$ is already in Schmidt form: $\lambda=0.9,\ 0.1$, Schmidt number 2 (entangled, but only a bit)
> - 2 Bell pairs together, regrouped as 2 qubits on each side: $\frac12\sum_{x=0}^3|x\rangle_A|x\rangle_B$, Schmidt number 4

**maximally entangled** in dimension $d$
$$
\frac1{\sqrt d}\sum_{x=0}^{d-1}|x\rangle_A|x\rangle_B
$$
> [!exercise] exercise
> entangled or product? (a) $\frac{|00\rangle-|01\rangle+|10\rangle-|11\rangle}2$ (b) $\frac{|01\rangle+|10\rangle}{\sqrt2}$ (c) $\frac{|00\rangle+|01\rangle+|10\rangle}{\sqrt3}$

> [!answer]- answer
> (a) $\alpha\delta-\beta\gamma=\frac12\cdot(-\frac12)-(-\frac12)\cdot\frac12=-\frac14+\frac14=0$ → product. it's $|+\rangle|-\rangle$
> (b) $0\cdot0-\frac1{\sqrt2}\cdot\frac1{\sqrt2}=-\frac12\neq0$ → entangled (it's the Bell state $\Psi^+$)
> (c) $\frac1{\sqrt3}\cdot0-\frac1{\sqrt3}\cdot\frac1{\sqrt3}=-\frac13\neq0$ → entangled

## 7. entanglement entropy
from [[Entanglement entropy]]

how entangled a pure state is = the Von Neumann entropy of either half
$$
\rho_A=\text{tr}_B\big(|\psi\rangle\langle\psi|_{AB}\big)\qquad E(\psi)=S(\rho_A)=S(\rho_B)
$$
> [!eg] eg. the Bell state $\frac{|00\rangle+|11\rangle}{\sqrt2}$
> $$
> \rho_{AB}=\frac12\begin{bmatrix}1&0&0&1\\0&0&0&0\\0&0&0&0\\1&0&0&1\end{bmatrix}\quad\Rightarrow\quad\rho_A=\frac I2\quad\Rightarrow\quad S(\rho_A)=1
> $$
> 1 ebit: the most a pair of qubits can have

**the maximum** (in dimension $d$)
![[Entanglement entropy#^max-entanglement]]

> [!eg] eg.
> 2 qubits ($d=2$): 1 ebit. 2 Bell pairs ($d=4$): $\log_24=2$ ebits. a product state: 0

> [!exercise] exercise
> find $E$ for $\sqrt{0.9}|00\rangle+\sqrt{0.1}|11\rangle$

> [!answer]- answer
> it's in Schmidt form, so $\rho_A=\begin{bmatrix}0.9&0\\0&0.1\end{bmatrix}$ and $E=H(0.1)=0.469$ ebits: less than half a Bell pair's worth

## 8. entanglement fungibility (concentration)
from [[Entanglement fungibility]]

$n$ copies of a partly entangled state can be turned into about $n\,E(\psi)$ perfect Bell pairs (and back), using only local operations and classical communication
$$
n\text{ copies of }|\psi\rangle\ \longleftrightarrow\ \approx n\,E(\psi)\text{ EPR pairs}
$$
**for** $|\psi\rangle=\sqrt{1-p}\,|00\rangle+\sqrt p\,|11\rangle$
![[Entanglement fungibility#^fungibility-rate]]

> [!eg] eg. 1000 copies with $p=0.1$
> $1000\times H(0.1)=1000\times0.469\approx469$ perfect Bell pairs

**how it works**: measure $w$ = how many of the $n$ copies are in $|11\rangle$ (without learning which). the chance of each $w$ is binomial
![[Entanglement fungibility#^weight-probability]]

and you're left with an equal superposition of $\binom nw$ terms, worth $\log_2\binom nw$ Bell pairs. the most likely $w$ is $np$
![[Entanglement fungibility#^concentration-yield]]

> [!eg] eg. how good the approximation is ($p=0.1$)
>
> | $n$ | $\log_2\binom n{0.1n}$ | $nH(0.1)$ |
> |---|---|---|
> | 10 | 3.3 | 4.7 |
> | 100 | 44.0 | 46.9 |
> | 1000 | 464.4 | 469.0 |
>
> the ratio gets closer to 1 as $n$ grows: concentration only works well for **lots** of copies

> [!exercise] exercise
> with $n=4$ copies and $p=0.1$, what's the chance of each $w$, and which is most likely?

> [!answer]- answer
> $P(0)=0.9^4=0.656$, $P(1)=4(0.1)(0.9)^3=0.292$, $P(2)=6(0.01)(0.81)=0.049$, $P(3)=4(0.001)(0.9)=0.004$, $P(4)=0.0001$. most likely $w=0$ (which gives **no** Bell pairs, since $\binom40=1$ term). with so few copies you usually get nothing, another reason it needs large $n$

## 9. losing photons in fibre
from [[Long-distance quantum communication]]

**decibels**
$$
\text{loss in dB}=10\log_{10}\!\left(\frac{P_{\text{in}}}{P_{\text{out}}}\right)\qquad\Longleftrightarrow\qquad\frac{P_{\text{out}}}{P_{\text{in}}}=10^{-\text{dB}/10}
$$
> [!eg] eg.
> 3 dB: $10^{-0.3}\approx0.50$ (half lost). 10 dB: $10^{-1}=0.1$. 20 dB: $10^{-2}=0.01$. losses in dB **add**: 10 dB then 20 dB = 30 dB = $10^{-3}$

**fibre at 0.2 dB per km** ($L$ km is $0.2L$ dB)
$$
\text{fraction that arrives}=10^{-0.2\,L/10}=10^{-L/50}
$$
> [!eg] eg.
> 15 km: $10^{-0.3}\approx50\%$. 50 km: $10^{-1}=10\%$. 100 km: $10^{-2}=1\%$. every 50 km is another factor of 10

> [!exercise] exercise
> (a) what fraction survives 300 km? (b) how many km until only 1 in a million photons arrive? (c) a 50 km fibre plus a 3 dB connector: what fraction arrives?

> [!answer]- answer
> (a) $10^{-300/50}=10^{-6}$, one in a million
> (b) the same: $10^{-L/50}=10^{-6}$ → $L=300$ km
> (c) $50\times0.2=10$ dB, plus 3 dB = 13 dB: $10^{-1.3}\approx0.05$, so 5%

## 10. quantum repeaters
from [[Quantum repeaters]]

**entanglement swapping**: A–R and R–B pairs, R does a Bell measurement → A–B are entangled

> [!eg] eg. why splitting the distance helps (1000 km, 0.2 dB/km)
> - **direct**: $10^{-1000/50}=10^{-20}$ of photons arrive. at a billion photons per second that's one every few thousand years
> - **10 links of 100 km**: each link works $10^{-2}=1\%$ of the time, so about 100 tries per link. with **memories** holding finished links while the others keep trying, then swapping them together, the total effort grows **slowly** with distance instead of exponentially
> - **nested swapping**: 8 links join up in $\log_28=3$ rounds of swaps (8 → 4 → 2 → 1)

**the 50% limit for error correction nodes**: codes need less than half the qubits lost per hop, and 0.2 dB/km loses half in 15 km ($10^{-15/50}\approx0.5$), so you'd need a node every 15 km

> [!exercise] exercise
> 4 links in a row (A=R1, R1=R2, R2=R3, R3=B). where and in what order do you swap?

> [!answer]- answer
> round 1: swap at R1 (gives A=R2) and at R3 (gives R2=B), at the same time. round 2: swap at R2 → A=B. 2 rounds ($\log_24=2$)

## 11. QKD key rate
from [[QKD distance and key rate]], [[Increasing the key rate]] and [[Floodlight QKD]]

**single photons down a fibre** (rate $R$ per second, perfect detector)
![[QKD distance and key rate#^key-rate]]

> [!eg] eg.
> $R=10^9$ photons/s over 100 km: at most $10^9\times0.01=10^7$ arrive per second (before sifting and error correction take their share)

**high dimensional encoding**
![[Increasing the key rate#^bits-per-photon]]

> [!eg] eg. time bin frames
> $M=4$ slots → 2 bits, $M=16$ → 4 bits, $M=1024$ → 10 bits per photon

**wavelength multiplexing**: $N$ wavelength channels = $N\times$ the key rate

**floodlight QKD**
![[Floodlight QKD#^processing-gain]]

> [!eg] eg. the course's numbers
> 2 THz of light, Bob sends at 10 Gbit/s so each bit lasts $\frac1{10^{10}}=0.1$ ns
> $$
> \text{gain}=2\times10^{12}\times10^{-10}=200\qquad\text{photons per bit}=0.1\text{ photons/s/Hz}\times200=20
> $$

> [!exercise] exercise
> (a) BB84 does ~1 Mbit/s at 50 km. how much faster does it need to be for 1 Gbit/s, and how does the course get there? (b) floodlight with the same 2 THz but Bob at 1 Gbit/s: processing gain and photons per bit? (c) how many time slots per frame for 6 bits per photon?

> [!answer]- answer
> (a) $\frac{10^9}{10^6}=1000\times$: a 10× faster clock and 100 wavelength channels ($10\times100=1000$)
> (b) bit time $=\frac1{10^9}=1$ ns, gain $=2\times10^{12}\times10^{-9}=2000$, photons per bit $=0.1\times2000=200$
> (c) $\log_2M=6$ → $M=2^6=64$ slots

## 12. device independent QKD
from [[Quantum hacking]]

the key is secure, no matter who built the devices, if a [[CHSH game]] played with the same photons wins **more than 75%** (the classical limit). the quantum maximum is $\cos^2\frac\pi8\approx85.4\%$, so a real system has to land between the two

see also [[Quantum Communication]], [[Week 1 formulas]], [[Week 3 formulas]]
