#extra #HHL #linear_systems #qiskit
**extra** (not in the course): the [[HHL algorithm]] on a system of **10 equations in 10 unknowns**, every step worked out, plus Qiskit code to simulate it (and any system you type in yourself). the 2×2 version is in [[HHL algorithm#worked example: solving a system with HHL, step by step]]

this one is harder than the 2×2 in 3 ways
- **10 isn't a power of 2**, so it has to be padded up to 16 (4 qubits)
- **the eigenvalues aren't whole numbers**, so the clock can only read them **approximately**
- finding the eigenvalues by hand needs a **trig identity**
## the equations
a chain of 10 unknowns, each linked to its neighbours (like 10 masses joined by springs, or the temperature at 10 points along a rod)
$$
\begin{aligned}
3x_1-x_2&=1\\
-x_1+3x_2-x_3&=1\\
-x_2+3x_3-x_4&=1\\
&\ \,\vdots\\
-x_8+3x_9-x_{10}&=1\\
-x_9+3x_{10}&=1
\end{aligned}
\qquad\text{ie.}\qquad-x_{j-1}+3x_j-x_{j+1}=1
$$
$$
A=\begin{bmatrix}3&-1&&&&\\-1&3&-1&&&\\&-1&3&-1&&\\&&\ddots&\ddots&\ddots&\\&&&-1&3&-1\\&&&&-1&3\end{bmatrix}\ (10\times10,\text{ blanks are }0)\qquad\vec b=(1,1,1,1,1,1,1,1,1,1)
$$
the classical answer (to compare at the end)
$$
\vec x\approx(0.618,\ 0.854,\ 0.944,\ 0.978,\ 0.989,\ 0.989,\ 0.978,\ 0.944,\ 0.854,\ 0.618)
$$
(symmetric, because the chain looks the same from both ends. the middle is close to 1 because $-1+3-1=1$, and the ends dip because they only have 1 neighbour)
> [!tip]- why $x_1\approx0.618$, the golden ratio (extra)
> try $x_j=1-r^j$ in the middle equations: $-(1-r^{j-1})+3(1-r^j)-(1-r^{j+1})=1$ needs $r^2-3r+1=0$, so $r=\frac{3-\sqrt5}2\approx0.382$. then $x_1\approx1-0.382=0.618=\frac1\varphi$ (the true value is $0.61798$, the tiny difference comes from the far end of the chain)

## step 0: understanding $A$
(HHL doesn't need any of this, the circuit finds the eigenvalues by itself. it's here so we can follow along)

**(a) Hermitian?** real and symmetric (the $-1$s above the diagonal mirror the ones below) ✅. sparsity $s=3$ (at most 3 non-zeros per row)

**(b) the eigenvectors: guess sine waves.** try $v_j=\sin(j\theta)$ for $j=1,\ldots,10$. row $j$ of $A\vec v$ is
$$
\begin{aligned}
(A\vec v)_j&=-\sin\big((j-1)\theta\big)+3\sin(j\theta)-\sin\big((j+1)\theta\big)\\
&=3\sin(j\theta)-\big[\sin(j\theta-\theta)+\sin(j\theta+\theta)\big]\\
&=3\sin(j\theta)-2\sin(j\theta)\cos\theta&&\text{(using }\sin(a-b)+\sin(a+b)=2\sin a\cos b)\\
&=(3-2\cos\theta)\,\sin(j\theta)
\end{aligned}
$$
so $\vec v$ is an eigenvector with eigenvalue $3-2\cos\theta$, **as long as the ends work**: row 1 has no $x_0$ and row 10 has no $x_{11}$, so we need $\sin(0\cdot\theta)=0$ (always true) and $\sin(11\theta)=0$. that means $\theta=\frac{k\pi}{11}$
$$
\lambda_k=3-2\cos\frac{k\pi}{11}\qquad v_k=\sqrt{\tfrac2{11}}\Big(\sin\tfrac{k\pi}{11},\ \sin\tfrac{2k\pi}{11},\ \ldots,\ \sin\tfrac{10k\pi}{11}\Big)\qquad k=1,\ldots,10
$$
($\sqrt{\frac2{11}}$ makes each one length 1)

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| $\lambda_k$ | 1.081 | 1.318 | 1.690 | 2.169 | 2.715 | 3.285 | 3.831 | 4.310 | 4.683 | 4.919 |

**(c) condition number**: $\kappa=\frac{4.919}{1.081}\approx4.55$ (small, so HHL should work well)
## step 1: pad to 16 and load $\vec b$
**1a. pad.** qubits hold $2^n$ numbers, so 10 becomes 16 ($n=4$ qubits). add 6 extra unknowns with $1$ on the diagonal and $0$ on the right side: they just say $x_{11}=\cdots=x_{16}=0$. (this adds 6 eigenvalues equal to 1, but $\vec b$ has nothing in them, so they never matter)

**1b. normalise.** $\|\vec b\|=\sqrt{10}$, so
$$
|b\rangle=\tfrac1{\sqrt{10}}\big(\underbrace{1,1,\ldots,1}_{10},\underbrace{0,\ldots,0}_{6}\big)
$$
remember the $\sqrt{10}$ for the end. **1c. the qubits**

| register | qubits | job |
|---|---|---|
| $b$ | 4 | holds the vector ($2^4=16$ entries) |
| clock | 5 | holds the eigenvalue ($2^5=32$ readings) |
| ancilla | 1 | the filter |
| **total** | **10** | |

## step 2: rewrite $|b\rangle$ in the eigenvectors
$b_k=\langle v_k|b\rangle=\frac1{\sqrt{10}}\sqrt{\frac2{11}}\sum_{j=1}^{10}\sin\frac{jk\pi}{11}$

**half of them are 0**: for even $k$ the sine wave is **antisymmetric** (the second half is minus the first half, mirrored), so the sum cancels. $\vec b$ is symmetric, so only the symmetric (odd $k$) eigenvectors are needed

| $k$ | 1 | 3 | 5 | 7 | 9 | even $k$ |
|---|---|---|---|---|---|---|
| $b_k$ | 0.938 | 0.295 | 0.156 | 0.087 | 0.040 | 0 |
| $b_k^2$ | 0.879 | 0.087 | 0.024 | 0.008 | 0.002 | 0 |

check: $0.879+0.087+0.024+0.008+0.002=1$ ✅. so
$$
|b\rangle=0.938\,|v_1\rangle+0.295\,|v_3\rangle+0.156\,|v_5\rangle+0.087\,|v_7\rangle+0.040\,|v_9\rangle
$$
## step 3: phase estimation (now approximate)
**3a. pick $t$.** $t=\frac\pi{\lambda_{\max}}=\frac\pi{4.919}=0.639$. the clock counts in $\frac1{32}$ of a turn, so each tick is worth
$$
\Delta\lambda=\frac{2\pi}{32\,t}=\frac{2\times4.919}{32}=0.307\qquad\text{clock reading }c\ \leftrightarrow\ \lambda\approx0.307\,c
$$
**3b. the problem**: $\lambda_1=1.081$ would need a reading of $\frac{1.081}{0.307}=3.52$, which isn't a whole number. when that happens, phase estimation **splits** the amplitude between the nearest readings (mostly the 2 neighbours, with a little further out)

| eigenvalue | exact reading | most likely readings (chance) |
|---|---|---|
| $\lambda_1=1.081$ | 3.52 | **4** (43%), **3** (38%), 5 (5%) |
| $\lambda_3=1.690$ | 5.50 | **5** (41%), **6** (40%), 4 (5%) |
| $\lambda_5=2.715$ | 8.83 | **9** (91%), 8 (4%) |
| $\lambda_7=3.831$ | 12.46 | **12** (47%), **13** (34%), 11 (5%) |
| $\lambda_9=4.683$ | 15.23 | **15** (84%), 16 (8%) |

(the closer the exact reading is to a whole number, the cleaner: 8.83 is mostly 9, but 3.52 is split almost in half)

**3c. after phase estimation**
$$
\sum_{k\text{ odd}}b_k\,|v_k\rangle\Big(\sum_c\alpha_{k,c}\,|c\rangle_{\text{clock}}\Big)
$$
where $|\alpha_{k,c}|^2$ are the chances in the table: each eigenvector has a **blurry** reading of its eigenvalue next to it
## step 4: the filter
for clock reading $c$, the estimate is $\tilde\lambda=0.307\,c$. the code picks $C$ = the smallest value the clock can show = one tick = $0.307$ (it doesn't know the real eigenvalues, so it plays safe). then
$$
\frac C{\tilde\lambda}=\frac{0.307}{0.307\,c}=\frac1c\qquad\theta=2\arcsin\frac1c
$$

| clock $c$ | $\tilde\lambda$ | $\lvert1\rangle$ amplitude $\frac1c$ | $\theta$ |
|---|---|---|---|
| 3 | 0.922 | 0.333 | $38.9°$ |
| 4 | 1.230 | 0.25 | $29.0°$ |
| 5 | 1.537 | 0.2 | $23.1°$ |
| 6 | 1.845 | 0.167 | $19.2°$ |
| 9 | 2.767 | 0.111 | $12.8°$ |
| 12 | 3.689 | 0.083 | $9.6°$ |
| 13 | 3.997 | 0.077 | $8.8°$ |
| 15 | 4.612 | 0.067 | $7.7°$ |

(the circuit has one controlled rotation for **every** reading 1 to 31, since it doesn't know which will show up)
## step 5: measure the ancilla, keep "1"
**5a. the chance**, if the clock were perfect
$$
P(1)\approx C^2\sum_kb_k^2\frac1{\lambda_k^2}=0.307^2\Big(\tfrac{0.879}{1.081^2}+\tfrac{0.087}{1.690^2}+\tfrac{0.024}{2.715^2}+\tfrac{0.008}{3.831^2}+\tfrac{0.002}{4.683^2}\Big)\approx0.0945\times0.787\approx0.074
$$
the simulation gives **0.077** (the blurry readings shift it a little). so only about 1 run in 13 works, because $C$ was chosen so small (see the $C=1$ run below for the fix)

**5b. what's left**: $\propto\sum_kb_k\sum_c\alpha_{k,c}\frac1c\,|v_k\rangle|c\rangle$. each eigenvector gets multiplied by roughly $\frac1{\lambda_k}$, averaged over its blurry readings
## step 6: uncompute
run phase estimation backwards. because each eigenvector's readings were all multiplied by **nearly** the same factor, the clock goes back to $|00000\rangle$ almost perfectly
$$
\propto\sum_k\frac{b_k}{\lambda_k}|v_k\rangle\qquad\text{(approximately)}
$$
## step 7: the answer
**the exact version** (what a perfect clock would give, times $\sqrt{10}$ to undo step 1b)
$$
x_j=\sum_{k\text{ odd}}\frac{\sqrt{10}\,b_k}{\lambda_k}\,v_k(j)
$$
**$x_1$ worked out**, one eigenvector at a time ($v_k(1)=\sqrt{\frac2{11}}\sin\frac{k\pi}{11}$)

| $k$ | $\sqrt{10}\,b_k$ | $\lambda_k$ | $v_k(1)$ | term |
|---|---|---|---|---|
| 1 | 2.966 | 1.081 | 0.1201 | 0.3296 |
| 3 | 0.934 | 1.690 | 0.3223 | 0.1780 |
| 5 | 0.492 | 2.715 | 0.4221 | 0.0765 |
| 7 | 0.274 | 3.831 | 0.3879 | 0.0277 |
| 9 | 0.125 | 4.683 | 0.2305 | 0.0062 |
| | | | **total** | **0.6180** ✅ |

**all 10** (5 clock qubits, the simulation)

| unknown | classical | classical normalised | HHL (normalised) |
|---|---|---|---|
| $x_1$ | 0.6180 | 0.2203 | 0.2205 |
| $x_2$ | 0.8539 | 0.3044 | 0.3049 |
| $x_3$ | 0.9438 | 0.3364 | 0.3374 |
| $x_4$ | 0.9775 | 0.3484 | 0.3486 |
| $x_5$ | 0.9888 | 0.3525 | 0.3508 |
| $x_6$ | 0.9888 | 0.3525 | 0.3508 |
| $x_7$ | 0.9775 | 0.3484 | 0.3486 |
| $x_8$ | 0.9438 | 0.3364 | 0.3374 |
| $x_9$ | 0.8539 | 0.3044 | 0.3049 |
| $x_{10}$ | 0.6180 | 0.2203 | 0.2205 |

==fidelity 0.999992==: even with the blurry clock, the answer is almost exact. the biggest error is in the middle, $0.3508$ vs $0.3525$
## step 8: reading it out
- measuring $b$ on the runs that passed gives $x_j^2/\sum x^2$: eg. $x_1$ came up 494 times out of 10,000 (true 0.049), $x_6$ 1258 times (true 0.124)
- **the sizes, not the signs** (all positive here anyway)
- **the length**: $\|\vec x\|=\sqrt{10}\times\frac{\sqrt{P(1)}}C=\sqrt{10}\times\frac{\sqrt{0.0771}}{0.307}=\sqrt{10}\times0.903=2.86$, vs the true $2.81$. close but not exact, because of the blurry clock
## the circuit
![[HHL_10_variable_circuit.png]]
(each block is many gates: phase estimation has controlled $U,U^2,U^4,U^8,U^{16}$ on 4 qubits plus a 5 qubit inverse QFT, and the middle block is 31 rotations, each controlled by all 5 clock qubits)
## simulation results
I ran `hhl_simulator.py` (Qiskit 2, exact statevector simulation, then 10,000 sampled measurements)
### run 1: the 10 variable example (5 clock qubits)
![[HHL_10_variable_results.png]]

- **fidelity 0.999992**, even though none of the eigenvalues sit exactly on the clock
- **the filter worked 7.7%** of the time
- **$\|\vec x\|$ from the success rate**: $0.903$ for $\vec b$ scaled to length 1 (true $0.887$)
- every measured fraction is within about 0.004 of the true one

> [!example]- the full output
> ```
> padded to 16x16 with 1s on the diagonal (the extra unknowns come out as 0)
>
> 16x16 system: 4 qubits for b, 5 clock qubits, 1 ancilla = 10 qubits
> eigenvalues of the matrix HHL uses: [1.     1.     1.     1.     1.     1.     1.081  1.3175 1.6903 2.1692
>  2.7154 3.2846 3.8308 4.3097 4.6825 4.919 ]   t = 0.6387   C = 0.3074
>
> chance the filter works (ancilla = 1): 0.0771
> classical answer x:              [0.61798 0.85393 0.94382 0.97753 0.98876 0.98876 0.97753 0.94382 0.85393
>  0.61798]
> classical, normalised:           [0.2203 0.3044 0.3364 0.3484 0.3525 0.3525 0.3484 0.3364 0.3044 0.2203]
> HHL state (normalised):          [0.2205 0.3049 0.3374 0.3486 0.3508 0.3508 0.3486 0.3374 0.3049 0.2205]
> fidelity |<x_true|x_hhl>|^2:     0.999992
> ||x|| (for b scaled to length 1) from the success rate: 0.9030   (true: 0.8871)
>
> simulated measurement of b (10000 successful runs), showing which unknown each result is:
>   x1  (|0000>)     494   (0.049)   exact HHL 0.049   true answer 0.049
>   x2  (|0001>)     941   (0.094)   exact HHL 0.093   true answer 0.093
>   x3  (|0010>)    1115   (0.112)   exact HHL 0.114   true answer 0.113
>   x4  (|0011>)    1182   (0.118)   exact HHL 0.122   true answer 0.121
>   x5  (|0100>)    1221   (0.122)   exact HHL 0.123   true answer 0.124
>   x6  (|0101>)    1258   (0.126)   exact HHL 0.123   true answer 0.124
>   x7  (|0110>)    1212   (0.121)   exact HHL 0.122   true answer 0.121
>   x8  (|0111>)    1130   (0.113)   exact HHL 0.114   true answer 0.113
>   x9  (|1000>)     944   (0.094)   exact HHL 0.093   true answer 0.093
>   x10  (|1001>)     503   (0.050)   exact HHL 0.049   true answer 0.049
>   -> these give |x_i|^2 / sum |x_j|^2 (sizes only, not signs)
> ```

**more clock qubits** (same system)

| clock qubits | total qubits | error $1-F$ | filter works |
|---|---|---|---|
| 4 | 9 | $2.6\times10^{-4}$ | 24.3% |
| 5 | 10 | $8.2\times10^{-6}$ | 7.7% |
| 6 | 11 | $1.1\times10^{-6}$ | 1.9% |
| 7 | 12 | $1.5\times10^{-6}$ | 0.47% |
| 8 | 13 | $1.5\times10^{-6}$ | 0.12% |
| 9 | 14 | $1.8\times10^{-6}$ | 0.03% |

![[HHL_clock_tradeoff.png]]

==a finer clock gives a more accurate answer, but the filter works less often==. why: the code sets $C$ to one tick of the clock (the smallest $|\lambda|$ it **could** show), and a finer clock has smaller ticks, so $C$ and every $\frac C\lambda$ shrink. the error stops improving after about 6 clock qubits, at around $10^{-6}$: phase estimation's leftover leakage, not the clock size, is the limit there
### run 1b: choosing $C$ yourself
here every eigenvalue is above 1 (step 0), so $C=1$ is allowed. set `C_VALUE = 1.0` in the code:
- **the filter works 66%** of the time instead of 7.7% (8.6× more often)
- **fidelity 0.99965**, a bit lower: clock reading 3 means $\tilde\lambda=0.922<1$, which would need an amplitude above 1, so the code has to cap it, and $\lambda_1$'s blurry readings land there 38% of the time

so knowing a **lower bound on the eigenvalues** is worth a lot: that's how real HHL proposals choose $C$

> [!example]- the full output (C = 1)
> ```
> padded to 16x16 with 1s on the diagonal (the extra unknowns come out as 0)
>
> 16x16 system: 4 qubits for b, 5 clock qubits, 1 ancilla = 10 qubits
> eigenvalues of the matrix HHL uses: [1.     1.     1.     1.     1.     1.     1.081  1.3175 1.6903 2.1692
>  2.7154 3.2846 3.8308 4.3097 4.6825 4.919 ]   t = 0.6387   C = 1.0000
>
> chance the filter works (ancilla = 1): 0.6619
> classical answer x:              [0.61798 0.85393 0.94382 0.97753 0.98876 0.98876 0.97753 0.94382 0.85393
>  0.61798]
> classical, normalised:           [0.2203 0.3044 0.3364 0.3484 0.3525 0.3525 0.3484 0.3364 0.3044 0.2203]
> HHL state (normalised):          [0.2289 0.31   0.3373 0.3445 0.3451 0.3451 0.3445 0.3373 0.31   0.2289]
> fidelity |<x_true|x_hhl>|^2:     0.999648
> ||x|| (for b scaled to length 1) from the success rate: 0.8136   (true: 0.8871)
>
> simulated measurement of b (10000 successful runs), showing which unknown each result is:
>   x1  (|0000>)     525   (0.052)   exact HHL 0.052   true answer 0.049
>   x2  (|0001>)     971   (0.097)   exact HHL 0.096   true answer 0.093
>   x3  (|0010>)    1120   (0.112)   exact HHL 0.114   true answer 0.113
>   x4  (|0011>)    1150   (0.115)   exact HHL 0.119   true answer 0.121
>   x5  (|0100>)    1187   (0.119)   exact HHL 0.119   true answer 0.124
>   x6  (|0101>)    1204   (0.120)   exact HHL 0.119   true answer 0.124
>   x7  (|0110>)    1194   (0.119)   exact HHL 0.119   true answer 0.121
>   x8  (|0111>)    1133   (0.113)   exact HHL 0.114   true answer 0.113
>   x9  (|1000>)     969   (0.097)   exact HHL 0.096   true answer 0.093
>   x10  (|1001>)     547   (0.055)   exact HHL 0.052   true answer 0.049
>   -> these give |x_i|^2 / sum |x_j|^2 (sizes only, not signs)
> ```

### run 2: the 3 equations from Gaussian elimination
$2x+y-z=8$, $-3x-y+2z=-11$, $-2x+y+2z=-3$ (answer $(2,3,-1)$, see [[Linear systems of equations#worked example: Gaussian elimination, step by step]]), with 6 clock qubits: `h.solve([[2,1,-1],[-3,-1,2],[-2,1,2]], [8,-11,-3], m=6)`
- $A$ isn't symmetric, so the code solved the $6\times6$ Hermitian version $\begin{bmatrix}0&A\\A^\dagger&0\end{bmatrix}$, padded to $8\times8$
- HHL gives $(0.584,\ 0.784,\ -0.210)$ vs the true $(0.535,\ 0.802,\ -0.267)$, fidelity **0.9939**
- the filter only worked **0.19%** of the time: the dilated matrix has eigenvalues as small as $\pm0.114$, so $\kappa\approx45$ and $C$ is tiny

| clock qubits | fidelity | filter works |
|---|---|---|
| 3 | 0.9754 | 20.5% |
| 4 | 0.9754 | 3.8% |
| 5 | 0.9777 | 0.82% |
| 6 | 0.9939 | 0.19% |
| 7 | **0.99996** | 0.05% |
| 8 | 0.99994 | 0.01% |

> [!example]- the full output (6 clock qubits)
> ```
> A isn't Hermitian, so solving the Hermitian dilation [[0, A], [A†, 0]] instead
> padded to 8x8 with 1s on the diagonal (the extra unknowns come out as 0)
>
> 8x8 system: 3 qubits for b, 6 clock qubits, 1 ancilla = 10 qubits
> eigenvalues of the matrix HHL uses: [-5.1034 -1.7152 -0.1142  0.1142  1.      1.      1.7152  5.1034]   t = 0.5963   C = 0.1646
>
> chance the filter works (ancilla = 1): 0.0019
> classical answer x:              [ 2.  3. -1.]
> classical, normalised:           [ 0.5345  0.8018 -0.2673]
> HHL state (normalised):          [ 0.5844  0.7839 -0.2098]
> fidelity |<x_true|x_hhl>|^2:     0.993904
> ||x|| (for b scaled to length 1) from the success rate: 0.2668   (true: 0.2686)
>
> simulated measurement of b (2000 successful runs), showing which unknown each result is:
>   x1  (|011>)     679   (0.340)   exact HHL 0.342   true answer 0.286
>   x2  (|100>)    1230   (0.615)   exact HHL 0.614   true answer 0.643
>   x3  (|101>)      91   (0.045)   exact HHL 0.044   true answer 0.071
>   -> these give |x_i|^2 / sum |x_j|^2 (sizes only, not signs)
> ```

### run 3: a negative eigenvalue
$x_1+2x_2=1$, $2x_1+x_2=0$ (eigenvalues $3$ and $-1$), with 5 clock qubits: `h.solve([[1,2],[2,1]], [1,0], m=5)`
- the clock is read as a **signed** number, so $-1$ works fine: fidelity **1.000000**, HHL gives $(-0.447,\ 0.894)$, exactly the true $(-\frac13,\frac23)$ normalised
- the minus sign on $x_1$ is in the state, but a plain measurement only shows sizes: $x_1$ 19.1% (true 20%), $x_2$ 80.9% (true 80%)

> [!example]- the full output
> ```
> 2x2 system: 1 qubits for b, 5 clock qubits, 1 ancilla = 7 qubits
> eigenvalues of the matrix HHL uses: [-1.  3.]   t = 0.9817   C = 0.2000
>
> chance the filter works (ancilla = 1): 0.0222
> classical answer x:              [-0.33333  0.66667]
> classical, normalised:           [-0.4472  0.8944]
> HHL state (normalised):          [-0.4472  0.8944]
> fidelity |<x_true|x_hhl>|^2:     1.000000
> ||x|| (for b scaled to length 1) from the success rate: 0.7454   (true: 0.7454)
>
> simulated measurement of b (2000 successful runs), showing which unknown each result is:
>   x1  (|0>)     382   (0.191)   exact HHL 0.200   true answer 0.200
>   x2  (|1>)    1618   (0.809)   exact HHL 0.800   true answer 0.800
>   -> these give |x_i|^2 / sum |x_j|^2 (sizes only, not signs)
> ```

## simulate it yourself (Qiskit)
the file is in the vault at `Extra (not in course)/Course 3 (extra)/Week 3/Code/hhl_simulator.py` (Obsidian hides `.py` files, open it from Finder). it's the same code as below
**to run**
1. `pip install qiskit numpy scipy`
2. `python hhl_simulator.py` (runs the 10 variable example above)
3. **your own equations**: edit `A` (one row per equation, one column per unknown) and `b` at the top, then run again. or from Python: `import hhl_simulator as h; h.solve(A, b, m=6)`
4. **settings**: `CLOCK_QUBITS` (accuracy vs filter success), `C_VALUE` (leave `None`, or set a lower bound on the eigenvalues)

**it handles any system**
- **not Hermitian?** it solves the bigger Hermitian system $\begin{bmatrix}0&A\\A^\dagger&0\end{bmatrix}\begin{bmatrix}0\\\vec x\end{bmatrix}=\begin{bmatrix}\vec b\\0\end{bmatrix}$ instead (the standard trick, costs 1 more qubit)
- **not a power of 2?** it pads with extra 1s on the diagonal (the extra unknowns come out as 0)
- **negative eigenvalues?** the clock is read as a signed number
- **eigenvalues not on the clock?** the answer is approximate, raise `CLOCK_QUBITS` to improve it

**what it prints**: the success chance, the classical answer, the HHL state next to the normalised classical answer, the fidelity between them, $\|\vec x\|$ recovered from the success rate, and simulated measurement counts with the true values next to them

> [!warning] one thing that tripped me up
> Qiskit's `phase_estimation` leaves the clock **bit reversed** (the most significant bit is on `clock[0]`). the first version of the code read it the normal way and got a fidelity of 0.16 instead of 1. the code flips the order of the controls for the rotations to fix it

```python
"""HHL simulator: solve A x = b with the HHL algorithm in Qiskit, and compare with the classical answer.

how to use
  1. pip install qiskit numpy scipy
  2. edit the EQUATIONS section below (or call solve(A, b) yourself)
  3. python hhl_simulator.py

any size, any matrix:
  - A doesn't have to be Hermitian: if it isn't, the code solves the bigger Hermitian system [[0, A], [A^†, 0]] instead
  - the size doesn't have to be a power of 2: the code pads with extra 1s on the diagonal
  - negative eigenvalues are fine (the clock is read as a signed number)
the answer comes out as a normalised state, exactly like real HHL. the code prints it next to the classical answer
(also normalised) plus the fidelity between them. more clock qubits = more accurate eigenvalues = higher fidelity
"""
import numpy as np
from scipy.linalg import expm
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import UnitaryGate, RYGate
from qiskit.quantum_info import Statevector
try:
    from qiskit.circuit.library import phase_estimation as _pe      # Qiskit >= 2.1
    PhaseEstimation = lambda m, U: _pe(m, U)
except ImportError:
    from qiskit.circuit.library import PhaseEstimation             # older Qiskit

# ---------------- EQUATIONS (edit these) ----------------
# one row per equation, one column per unknown. this is the 10 variable example from the note:
# a chain where each unknown is linked to its neighbours: -x(j-1) + 3 x(j) - x(j+1) = 1
A = [
    [ 3, -1,  0,  0,  0,  0,  0,  0,  0,  0],
    [-1,  3, -1,  0,  0,  0,  0,  0,  0,  0],
    [ 0, -1,  3, -1,  0,  0,  0,  0,  0,  0],
    [ 0,  0, -1,  3, -1,  0,  0,  0,  0,  0],
    [ 0,  0,  0, -1,  3, -1,  0,  0,  0,  0],
    [ 0,  0,  0,  0, -1,  3, -1,  0,  0,  0],
    [ 0,  0,  0,  0,  0, -1,  3, -1,  0,  0],
    [ 0,  0,  0,  0,  0,  0, -1,  3, -1,  0],
    [ 0,  0,  0,  0,  0,  0,  0, -1,  3, -1],
    [ 0,  0,  0,  0,  0,  0,  0,  0, -1,  3],
]
b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
CLOCK_QUBITS = 5      # how many qubits store the eigenvalue (more = more accurate, but the filter works less often)
SHOTS = 10_000        # for the "real experiment" style counts at the end
C_VALUE = None        # None = automatic (safe but small). if you know every |eigenvalue| >= some number, put it here (eg. 1.0)
# ---------------------------------------------------------


def prepare_system(A, b):
    """make A Hermitian and a power of 2 in size, so HHL can use it. returns (A_h, b_h, read) where
    read(v) picks out the entries of v that are the original unknowns x1, x2, ..."""
    A = np.array(A, dtype=complex); b = np.array(b, dtype=complex)
    n0 = len(b)
    if not np.allclose(A, A.conj().T):                       # Hermitian dilation: [[0, A], [A^†, 0]] (0, x) = (b, 0)
        A = np.block([[np.zeros_like(A), A], [A.conj().T, np.zeros_like(A)]])
        b = np.concatenate([b, np.zeros(n0)])
        read = lambda v: v[n0:2 * n0]                        # x sits in the second half
        print("A isn't Hermitian, so solving the Hermitian dilation [[0, A], [A†, 0]] instead")
    else:
        read = lambda v: v[:n0]
    N = 1 << int(np.ceil(np.log2(len(b))))                   # pad up to a power of 2
    if N != len(b):
        pad = N - len(b)
        A = np.block([[A, np.zeros((len(b), pad))], [np.zeros((pad, len(b))), np.eye(pad)]])
        b = np.concatenate([b, np.zeros(pad)])
        print(f"padded to {N}x{N} with 1s on the diagonal (the extra unknowns come out as 0)")
    return A, b, read


def build_hhl(A, b, m, t=None, C=None):
    """the HHL circuit: load b, phase estimation, controlled rotations, undo phase estimation"""
    n = int(np.log2(len(b)))
    lam = np.linalg.eigvalsh(A)
    signed = lam.min() < 0
    lmax = np.abs(lam).max()
    if t is None:      # pick t so the biggest eigenvalue fits on the clock (half a turn, or just under it if signed)
        t = np.pi / lmax if not signed else 2 * np.pi * (2 ** (m - 1) - 1) / (2 ** m * lmax)
    def clock_to_lambda(c):            # clock reading c means a phase of c/2^m of a full turn
        phi = c / 2 ** m
        if signed and phi >= 0.5: phi -= 1
        return 2 * np.pi * phi / t
    if C is None:                      # biggest allowed C: the smallest |λ| the clock can show
        C = min(abs(clock_to_lambda(c)) for c in range(1, 2 ** m))

    breg = QuantumRegister(n, "b"); clk = QuantumRegister(m, "clock"); anc = QuantumRegister(1, "anc")
    qc = QuantumCircuit(breg, clk, anc)
    qc.initialize(b / np.linalg.norm(b), breg)                               # step 1: load |b⟩
    qpe = PhaseEstimation(m, UnitaryGate(expm(1j * A * t), label="exp(iAt)"))
    qc.append(qpe, list(clk) + list(breg))                                   # step 3: eigenvalues onto the clock
    for c in range(1, 2 ** m):                                               # step 4: rotate the ancilla by C/λ
        ratio = np.clip(C / clock_to_lambda(c), -1, 1)
        # Qiskit's phase estimation leaves the clock bit-reversed (most significant bit on clock[0]),
        # so read the controls in reverse order to make ctrl_state = c mean "the clock says c"
        qc.append(RYGate(2 * np.arcsin(ratio)).control(m, ctrl_state=c), list(reversed(clk)) + [anc[0]])
    qc.append(qpe.inverse(), list(clk) + list(breg))                         # step 6: uncompute the clock
    return qc, t, C, n


def solve(A, b, m=CLOCK_QUBITS, shots=SHOTS, t=None, C=None):
    A_h, b_h, read = prepare_system(A, b)
    qc, t, C, n = build_hhl(A_h, b_h, m, t, C)
    print(f"\n{len(b_h)}x{len(b_h)} system: {n} qubits for b, {m} clock qubits, 1 ancilla = {n + m + 1} qubits")
    print(f"eigenvalues of the matrix HHL uses: {np.round(np.linalg.eigvalsh(A_h), 4)}   t = {t:.4f}   C = {C:.4f}")

    sv = Statevector(qc).data.reshape(2, 2 ** m, 2 ** n)     # index order: anc, clock, b (Qiskit is little endian)
    good = sv[1, 0, :]                                       # ancilla = 1 (filter worked), clock back to 0
    p_success = np.linalg.norm(good) ** 2
    x_hhl = good / np.linalg.norm(good)

    x_true = np.linalg.solve(A_h, b_h / np.linalg.norm(b_h))
    x_classical = read(np.linalg.solve(A_h, b_h))            # the real, unnormalised answer
    x_true_n = x_true / np.linalg.norm(x_true)
    overlap = np.vdot(x_true_n, x_hhl)
    x_hhl_aligned = x_hhl * np.conj(overlap) / abs(overlap)  # remove an unmeasurable global phase
    fidelity = abs(overlap) ** 2

    print(f"\nchance the filter works (ancilla = 1): {p_success:.4f}")
    print(f"classical answer x:              {np.round(x_classical.real, 5)}")
    print(f"classical, normalised:           {np.round(read(x_true_n).real, 4)}")
    print(f"HHL state (normalised):          {np.round(read(x_hhl_aligned).real, 4)}")
    print(f"fidelity |<x_true|x_hhl>|^2:     {fidelity:.6f}")
    # the size of x is lost in the state, but it's hidden in the success rate: P = C^2 ||A^-1 b||^2 (for |b| = 1)
    print(f"||x|| (for b scaled to length 1) from the success rate: {np.sqrt(p_success) / C:.4f}"
          f"   (true: {np.linalg.norm(x_true):.4f})")

    # what a real machine would give you: measure b many times, keeping only runs where the filter worked
    idx = read(np.arange(len(x_hhl)))                        # which basis states hold x1, x2, ...
    probs = np.abs(x_hhl[idx]) ** 2
    probs = probs / probs.sum()
    rng = np.random.default_rng(1)
    counts = np.bincount(rng.choice(len(probs), size=shots, p=probs), minlength=len(probs))
    print(f"\nsimulated measurement of b ({shots} successful runs), showing which unknown each result is:")
    true_probs = np.abs(x_true[idx]) ** 2 / np.sum(np.abs(x_true[idx]) ** 2)
    for i, cnt in enumerate(counts):
        print(f"  x{i + 1}  (|{idx[i]:0{n}b}>)  {cnt:6d}   ({cnt / shots:.3f})"
              f"   exact HHL {probs[i]:.3f}   true answer {true_probs[i]:.3f}")
    print("  -> these give |x_i|^2 / sum |x_j|^2 (sizes only, not signs)")
    return qc


if __name__ == "__main__":
    circuit = solve(A, b, C=C_VALUE)
    # to see the circuit:  print(circuit.draw())
```

see also [[HHL algorithm]], [[Linear systems of equations]], [[Quantum Phase Estimation]], [[Week 3 formulas]]
