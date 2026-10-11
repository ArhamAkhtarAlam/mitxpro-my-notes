#formula_sheet #NISQ #quantum_volume #HHL #quantum_machine_learning
every formula from Course 3 Week 3, **with the maths worked out** step by step so you can see where each one comes from, plus an **eg.** for each formula and an **exercise** for each section (answers fold out, try them first). each section links to the full note. (all numbers checked numerically)
## 1. why NISQ machines are limited
from [[NISQ]]

if every gate works with probability $1-\epsilon$, the chance a circuit of $g$ gates has **no** error is
$$
\begin{aligned}
P(\text{no error})&=(1-\epsilon)^g\\
&\approx e^{-g\epsilon}&&\text{(since }1-\epsilon\approx e^{-\epsilon}\text{ for small }\epsilon)
\end{aligned}
$$
==so you can only run about $g\approx\frac1\epsilon$ gates before an error is likely==
> [!example] example
> $\epsilon=0.001$ (99.9% gates), $g=1000$ gates: $(0.999)^{1000}\approx e^{-1}\approx0.37$, only a 37% chance of no error. that's the depth limit of the NISQ era

> [!question] exercise
> (a) $\epsilon=0.005$ and $g=200$ gates: chance of no error? (b) with $\epsilon=0.001$, how many gates until the chance of no error falls to 50%?

> [!success]- answer
> (a) $0.995^{200}\approx e^{-1}\approx0.37$
> (b) $e^{-g\epsilon}=\frac12$ → $g=\frac{\ln2}\epsilon\approx693$ gates

## 2. quantum volume
from [[Quantum volume]]

**step 1: errors add up.** 2 CNOTs in a row, each with error $\epsilon$
$$
F=(1-\epsilon)^2=1-2\epsilon+\epsilon^2\approx1-2\epsilon
$$
so to first order **errors just add**. a general 2 qubit gate $U_4$ needs 3 CNOTs, so it has an effective error $\epsilon_{\text{eff}}\approx3\epsilon$

**step 2: how deep can you go?** a layer on $n$ qubits has about $n$ gates, so after $d$ layers the total error is about $n\,d\,\epsilon_{\text{eff}}$. keeping that below about 1 gives
$$
d(n)\approx\frac1{n\,\epsilon_{\text{eff}}}
$$
**step 3: the useful size.** you need a square circuit ($n$ qubits × $n$ layers), so the usable size is whichever runs out first, maximised over how many qubits you try
$$
m=\max_{n}\ \min\big(n,\,d(n)\big)\qquad\qquad V_Q=2^m
$$
**step 4: the best size.** $n=d(n)$ when $n=\frac1{n\,\epsilon_{\text{eff}}}$, so
$$
n^2=\frac1{\epsilon_{\text{eff}}}\quad\Rightarrow\quad n^*\approx\frac1{\sqrt{\epsilon_{\text{eff}}}}
$$
> [!example] worked example: CNOT error $\epsilon=0.01$
> $\epsilon_{\text{eff}}\approx3\times0.01=0.03$, so $n^*\approx\frac1{\sqrt{0.03}}\approx5.8$
>
> | $n$ | $d(n)=\frac1{0.03n}$ | $\min(n,d)$ |
> |---|---|---|
> | 4 | 8.3 | 4 |
> | 5 | 6.7 | **5** |
> | 6 | 5.6 | **5** |
> | 7 | 4.8 | 4 |
>
> the best is $m=5$, so $V_Q=2^5=32$. adding qubits doesn't help, only **better gates** do: halving $\epsilon$ moves $n^*$ up by $\sqrt2$

> [!question] exercise: better gates
> the CNOT error improves to $\epsilon=0.0025$. find $\epsilon_{\text{eff}}$, $n^*$, $m$ and $V_Q$

> [!success]- answer
> $\epsilon_{\text{eff}}=0.0075$, $n^*=\frac1{\sqrt{0.0075}}\approx11.5$
>
> | $n$ | $d(n)$ | $\min(n,d)$ |
> |---|---|---|
> | 10 | 13.3 | 10 |
> | 11 | 12.1 | **11** |
> | 12 | 11.1 | **11** |
> | 13 | 10.3 | 10 |
>
> $m=11$, $V_Q=2^{11}=2048$. 4× smaller error → 64× the quantum volume

## 3. learning parity with noise
from [[Learning parity with noise]]

**the parity function**: data bits $D$ and a secret key $k$ (both $n$ bits)
$$
a=D\cdot k\bmod2=\bigoplus_{i:\,k_i=1}D_i
$$
(XOR together the data bits where the key has a 1). eg. $k=101$, $D=111$: $a=1\oplus1=0$

**the quantum learner, derived** (the key fact: $H^{\otimes n}|D\rangle=\frac1{\sqrt{2^n}}\sum_y(-1)^{D\cdot y}|y\rangle$)
$$
\begin{aligned}
&\text{1. Hadamards on the data:}&&\tfrac1{\sqrt{2^n}}\textstyle\sum_D|D\rangle|0\rangle_a\\
&\text{2. oracle writes the parity:}&&\tfrac1{\sqrt{2^n}}\textstyle\sum_D|D\rangle|D\cdot k\rangle_a\\
&\text{3. Hadamard on }a:\ |c\rangle\to\tfrac{|0\rangle+(-1)^c|1\rangle}{\sqrt2}&&\tfrac1{\sqrt{2^{n+1}}}\textstyle\sum_D|D\rangle\big(|0\rangle_a+(-1)^{D\cdot k}|1\rangle_a\big)\\
&\text{4. Hadamards on the data again:}&&\tfrac1{\sqrt2}\big(|0\ldots0\rangle|0\rangle_a+|k\rangle|1\rangle_a\big)
\end{aligned}
$$
step 4 uses $H^{\otimes n}\sum_D|D\rangle=\sqrt{2^n}\,|0\ldots0\rangle$ and $H^{\otimes n}\sum_D(-1)^{D\cdot k}|D\rangle=\sqrt{2^n}\,|k\rangle$ (everything else cancels)

==so half the time $a=1$ and the data qubits **are** the key $k$==. classically each query only gives you one equation about $k$ (checked numerically for $k=101$: only $0000$ and $1011$ appear, $\frac12$ each)
> [!question] exercise
> key $k=110$. (a) find the parity $a$ for $D=011$ and $D=111$ (b) with $n=4$ and $k=1011$, which outcomes can the quantum learner give? (c) how many noiseless classical queries do you need for $n=4$?

> [!success]- answer
> (a) $011$: $0\cdot1+1\cdot1+1\cdot0=1$. $111$: $1+1+0=2\equiv0$
> (b) only $0000\,|\,0$ and $1011\,|\,1$ (data, then ancilla), $\frac12$ each
> (c) each query is one linear equation for $k$, so 4 independent ones (and with noise it gets **much** harder classically, but the quantum learner still just reads off $k$)

## 4. support vector machines
from [[Support vector machines]]

**the cut**: a line (hyperplane) $\vec w\cdot\vec x+b=0$. points with $\vec w\cdot\vec x+b>0$ are one class, $<0$ the other

**the margin**: scale $\vec w,b$ so the closest points (the **support vectors**) have $\vec w\cdot\vec x+b=\pm1$. the gap between those 2 parallel lines is
$$
\text{margin}=\frac2{\|\vec w\|}
$$
so a **bigger** margin means a **smaller** $\|\vec w\|$, and training is
$$
\min_{\vec w,b}\ \tfrac12\|\vec w\|^2\qquad\text{such that}\qquad y_i(\vec w\cdot\vec x_i+b)\geq1\ \text{for every point}
$$
($y_i=\pm1$ is the label of point $i$). eg. $\vec w=(1,1)$: margin $=\frac2{\sqrt2}\approx1.41$

**the kernel trick**: map data to more dimensions with $\phi$, where a straight cut works. you only ever need inner products
$$
K(x,y)=\phi(x)\cdot\phi(y)\qquad K_{ij}=\phi(x_i)\cdot\phi(x_j)
$$
> [!example] 1D → 2D
> $\phi(x)=(x,\ x^2)$ turns points on a line into points on a parabola, where a straight line can separate "middle" from "outside". then $K(x,y)=xy+x^2y^2$, eg. $K(2,3)=6+36=42$, the same as $\phi(2)\cdot\phi(3)=(2,4)\cdot(3,9)=42$, without ever building $\phi$

**classifying a new point** (only the support vectors have $\alpha_i\neq0$)
$$
f(x)=\text{sign}\Big(\sum_i\alpha_i\,y_i\,K(x_i,x)+b\Big)
$$
> [!example] eg. 2 support vectors
> $\vec x_1=(1,1)$ with $y_1=+1$, $\vec x_2=(-1,-1)$ with $y_2=-1$, $\alpha_1=\alpha_2=\frac14$, $b=0$, plain kernel $K(\vec x,\vec y)=\vec x\cdot\vec y$. classify $\vec x=(2,0)$:
> $$
> f=\text{sign}\Big(\tfrac14(+1)\underbrace{(1,1)\cdot(2,0)}_{2}+\tfrac14(-1)\underbrace{(-1,-1)\cdot(2,0)}_{-2}\Big)=\text{sign}(0.5+0.5)=+1
> $$
> (this is the same as $\vec w=\sum_i\alpha_iy_i\vec x_i=(\frac12,\frac12)$, and $\vec w\cdot\vec x_1=1$: the support vectors sit exactly on the margin)

> [!question] exercise
> $\vec w=(3,4)$, $b=-5$. (a) the margin (b) classify $(1,1)$ and $(0,1)$ (c) with $\phi(x)=(x,x^2)$, find $K(1,-2)$

> [!success]- answer
> (a) $\frac2{\|\vec w\|}=\frac25=0.4$
> (b) $(1,1)$: $3+4-5=2>0$ → class $+1$. $(0,1)$: $4-5=-1$ → class $-1$, and it's exactly on the margin line, so it's a **support vector**
> (c) $1\cdot(-2)+1^2(-2)^2=-2+4=2$

## 5. quantum kernel SVM
from [[Quantum kernel SVM]]

**the feature map** is a circuit $U(x)$: $|\phi(x)\rangle=U(x)|0\ldots0\rangle$. the kernel is the overlap of 2 such states
$$
K(x,y)=|\langle\phi(x)|\phi(y)\rangle|^2=|\langle0\ldots0|U(x)^\dagger U(y)|0\ldots0\rangle|^2
$$
so: run $U(y)$, then $U(x)$ **backwards**, measure, and $K$ = the chance of getting all 0s
> [!example] 1 qubit: $U(x)=R_y(x)$
> $$
> \begin{aligned}
> |\phi(x)\rangle&=\cos\tfrac x2\,|0\rangle+\sin\tfrac x2\,|1\rangle\\
> \langle\phi(x)|\phi(y)\rangle&=\cos\tfrac x2\cos\tfrac y2+\sin\tfrac x2\sin\tfrac y2=\cos\tfrac{x-y}2\\
> K(x,y)&=\cos^2\tfrac{x-y}2
> \end{aligned}
> $$
> eg. $x=0.7$, $y=2$: $K=\cos^2(0.65)\approx0.634$. points close together → $K\approx1$, far apart → $K\approx0$

> [!question] exercise
> with $K(x,y)=\cos^2\frac{x-y}2$: (a) $K(0,\pi)$ (b) $K(0,\frac\pi2)$ (c) with 2 qubits, $U(\vec x)=R_y(x_1)\otimes R_y(x_2)$, find $K\big((0,0),(\frac\pi2,\frac\pi2)\big)$

> [!success]- answer
> (a) $\cos^2\frac\pi2=0$: $|0\rangle$ and $|1\rangle$ don't overlap at all
> (b) $\cos^2\frac\pi4=\frac12$
> (c) product states multiply: $K=\cos^2\frac{x_1-y_1}2\cos^2\frac{x_2-y_2}2=\frac12\cdot\frac12=\frac14$

## 6. quantum simulation
from [[Quantum simulation]]

storing a general state of $n$ qubits takes $2^n$ complex numbers (16 bytes each)
$$
\text{memory}=16\times2^n\text{ bytes}\qquad n=50:\ 16\times2^{50}\approx1.8\times10^{16}\text{ bytes}\approx18\text{ petabytes}
$$
every extra qubit **doubles** it. for molecules it's worse: if each of 80 particles can be in ~100 states, that's $100^{80}=10^{160}$ numbers, far more than atoms in the universe ($\sim10^{80}$)
> [!question] exercise
> memory for (a) 30 qubits (b) 40 qubits

> [!success]- answer
> (a) $16\times2^{30}\approx1.7\times10^{10}$ bytes ≈ 17 GB, a good laptop
> (b) $16\times2^{40}\approx1.8\times10^{13}$ bytes ≈ 18 TB, $2^{10}=1024$ times more for 10 extra qubits

## 7. linear systems of equations
from [[Linear systems of equations]]

**the problem**: $N$ equations, $N$ unknowns
$$
A\,\vec x=\vec b\qquad\text{eg. }\begin{bmatrix}3&0&1\\0&1&-i\\-2&1&0\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}5\\0\\-1\end{bmatrix}
$$
**the condition number** (for Hermitian $A$: biggest over smallest eigenvalue size)
$$
\kappa=\|A\|\,\|A^{-1}\|=\frac{\sigma_{\max}}{\sigma_{\min}}\qquad\frac{\|\delta\vec x\|}{\|\vec x\|}\leq\kappa\,\frac{\|\delta\vec b\|}{\|\vec b\|}
$$
==a small error in $\vec b$ can grow by up to $\kappa$ times in $\vec x$==
> [!example] a badly conditioned system
> $$
> \begin{bmatrix}1&1\\1&1.001\end{bmatrix}\vec x=\begin{bmatrix}2\\2.001\end{bmatrix}\Rightarrow\vec x=\begin{bmatrix}1\\1\end{bmatrix}\qquad\text{but}\qquad\vec b=\begin{bmatrix}2\\2.002\end{bmatrix}\Rightarrow\vec x=\begin{bmatrix}0\\2\end{bmatrix}
> $$
> changing $\vec b$ by $0.001$ completely changes the answer, because $\kappa\approx4000$ (the 2 rows are almost the same equation)

**the costs**

| method | time | |
|---|---|---|
| Gaussian elimination | $O(N^3)$ | any matrix |
| iterative (gradient descent) | $O(N\,s\,\kappa\log\frac1\epsilon)$ | sparse ($s$ = non-zeros per row) |
| HHL (quantum) | $O(\log N\cdot s^2\kappa^2/\epsilon)$ | gives $\lvert x\rangle$ as a quantum state |

the big win is $\log N$ instead of $N$, but only if $s$ and $\kappa$ are small and you only need a property of $\vec x$, not every entry
> [!example] eg. how big the difference is
> $N=10^6$ unknowns, $s=10$, $\kappa=10$, $\epsilon=0.01$ (so $\log_2N\approx20$, $\log\frac1\epsilon\approx4.6$)
>
> | method | steps |
> |---|---|
> | Gaussian elimination | $N^3=10^{18}$ |
> | gradient descent | $N\,s\,\kappa\log\frac1\epsilon\approx10^6\cdot10\cdot10\cdot4.6\approx5\times10^8$ |
> | HHL | $\log N\cdot s^2\kappa^2/\epsilon\approx20\cdot100\cdot100/0.01=2\times10^7$ |
>
> HHL wins here, but make $\kappa=1000$ and it's $2\times10^{11}$, worse than gradient descent ($5\times10^{10}$). $\kappa$ matters a lot

> [!question] exercise
> (a) $\kappa$ of $\begin{bmatrix}2&0\\0&0.5\end{bmatrix}$ and of $\begin{bmatrix}2&1\\1&2\end{bmatrix}$ (b) for the second one, $\vec b$ has a 1% error. how big can the error in $\vec x$ be?

> [!success]- answer
> (a) $\frac2{0.5}=4$. the second has eigenvalues $3$ and $1$ (eigenvectors $\frac{(1,1)}{\sqrt2}$, $\frac{(1,-1)}{\sqrt2}$), so $\kappa=3$
> (b) up to $\kappa\times1\%=3\%$

## 8. the HHL algorithm
from [[HHL algorithm]]

**the steps** (write $|b\rangle$ in the eigenvectors $|a_i\rangle$ of $A$, eigenvalues $\lambda_i$)
$$
\begin{aligned}
&|b\rangle=\textstyle\sum_ib_i\,|a_i\rangle&&\text{(start)}\\
\xrightarrow{\text{phase estimation on }e^{iAt}}\ &\textstyle\sum_ib_i\,|a_i\rangle|\lambda_i\rangle&&\text{(eigenvalues written in a register)}\\
\xrightarrow{\text{controlled rotation}}\ &\textstyle\sum_ib_i\,|a_i\rangle|\lambda_i\rangle\Big(\sqrt{1-\tfrac{C^2}{\lambda_i^2}}\,|0\rangle+\tfrac C{\lambda_i}|1\rangle\Big)&&\text{(ancilla qubit)}\\
\xrightarrow{\text{measure ancilla }=1,\text{ undo phase estimation}}\ &\textstyle\sum_i\frac{b_i}{\lambda_i}\,|a_i\rangle\ \propto\ A^{-1}|b\rangle=|x\rangle
\end{aligned}
$$
($C\leq\lambda_{\min}$ so the rotation is allowed). the chance the ancilla gives 1 is $C^2\sum_i\frac{|b_i|^2}{\lambda_i^2}$, which shrinks when $\kappa$ is big, that's where the $\kappa^2$ in the cost comes from
> [!example] worked 2×2 example
> $$
> A=\begin{bmatrix}1&\frac12\\\frac12&1\end{bmatrix}\qquad|b\rangle=|0\rangle
> $$
> **eigenvectors**: $|a_1\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}$ with $\lambda_1=\frac32$, and $|a_2\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}$ with $\lambda_2=\frac12$ (so $\kappa=3$)
>
> **write $|b\rangle$ in them**: $|0\rangle=\frac1{\sqrt2}|a_1\rangle+\frac1{\sqrt2}|a_2\rangle$
>
> **divide by the eigenvalues**:
> $$
> \begin{aligned}
> |x\rangle&\propto\frac1{\sqrt2}\cdot\frac23\,|a_1\rangle+\frac1{\sqrt2}\cdot2\,|a_2\rangle\\
> &=\frac13\big(|0\rangle+|1\rangle\big)+\big(|0\rangle-|1\rangle\big)=\frac43|0\rangle-\frac23|1\rangle\\
> &\propto\frac1{\sqrt5}\big(2|0\rangle-|1\rangle\big)
> \end{aligned}
> $$
> **check classically**: $A^{-1}\binom10=\binom{4/3}{-2/3}$ ✅ (same direction)
>
> **success chance** with $C=\lambda_{\min}=\frac12$: $\frac14\Big(\frac{1/2}{9/4}+\frac{1/2}{1/4}\Big)=\frac14\big(0.222+2\big)\approx0.56$

> [!question] exercise: HHL by hand
> $A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$, $|b\rangle=|0\rangle$. find $|x\rangle$ the HHL way, check it classically, and find the success chance with $C=\lambda_{\min}$

> [!success]- answer
> eigenvalues $3$ ($|a_1\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}$) and $1$ ($|a_2\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}$), and $|0\rangle=\frac1{\sqrt2}(|a_1\rangle+|a_2\rangle)$
> $$
> \begin{aligned}
> |x\rangle&\propto\frac1{\sqrt2}\Big(\frac13|a_1\rangle+|a_2\rangle\Big)=\frac16(|0\rangle+|1\rangle)+\frac12(|0\rangle-|1\rangle)=\frac23|0\rangle-\frac13|1\rangle\\
> &\propto\frac1{\sqrt5}\big(2|0\rangle-|1\rangle\big)
> \end{aligned}
> $$
> classically $A^{-1}=\frac13\begin{bmatrix}2&-1\\-1&2\end{bmatrix}$, so $A^{-1}\binom10=\binom{2/3}{-1/3}$ ✅. success with $C=1$: $\frac12\cdot\frac19+\frac12\cdot1\approx0.56$ (the same as the worked example: this $A$ is just twice that one)

see also [[Realistic quantum computation]], [[Week 1 formulas]]
