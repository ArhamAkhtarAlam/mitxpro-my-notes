#tomography #density_matrix #bloch_sphere #IBM_Q
the course's IBM Q exercise: doing [[State tomography]] on a real quantum computer, step by step, with the actual numbers from IBM's 5 qubit **Tenerife** machine. part of [[Benchmarking quantum systems]]
## the recipe
1. write a circuit to measure the qubit in each Pauli basis: $X$, $Y$ and $Z$
2. run each one many times and turn the counts into probabilities
3. turn the probabilities into the 3 expectation values $S_1,S_2,S_3$
4. rebuild the density matrix from them, and compare with what you meant to make
## the formulas
any qubit's density matrix, written with the identity $\sigma_0=I$ and the Paulis $\sigma_1=X$, $\sigma_2=Y$, $\sigma_3=Z$
$$
\rho=\tfrac12S_0\sigma_0+\tfrac12S_1\sigma_1+\tfrac12S_2\sigma_2+\tfrac12S_3\sigma_3\qquad S_i=\text{tr}(\sigma_i\rho)
$$
each $S_i$ is "chance of the $+1$ result minus chance of the $-1$ result" in that basis
$$
\begin{aligned}
S_0&=P_{|0\rangle}+P_{|1\rangle}=1\\
S_1&=P_{|+\rangle}-P_{|-\rangle}&&\text{(X basis: }\tfrac{|0\rangle\pm|1\rangle}{\sqrt2})\\
S_2&=P_{|{+i}\rangle}-P_{|{-i}\rangle}&&\text{(Y basis: }\tfrac{|0\rangle\pm i|1\rangle}{\sqrt2})\\
S_3&=P_{|0\rangle}-P_{|1\rangle}&&\text{(Z basis)}
\end{aligned}
$$
then put them back together ($S_0=1$)
$$
\rho^E=\begin{bmatrix}\frac12+\frac12S_3&\frac12S_1-\frac12iS_2\\\frac12S_1+\frac12iS_2&\frac12-\frac12S_3\end{bmatrix}
$$
($S_1,S_2,S_3$ is exactly the Bloch vector $\vec r$, see [[State tomography#the key idea: the Bloch vector]])
## measuring in each basis
the hardware can only measure in the $Z$ basis ($|0\rangle$ or $|1\rangle$). to measure in another basis, first **rotate** that basis onto $Z$, then measure
- **Z basis**: just measure
- **X basis**: $H$ then measure. $H$ turns $|+\rangle\to|0\rangle$ and $|-\rangle\to|1\rangle$, so "got 0" means "was $|+\rangle$"
- **Y basis**: $S^\dagger$ then $H$ then measure. $S^\dagger$ turns $|{\pm i}\rangle$ into $|\pm\rangle$, then $H$ turns those into $|0\rangle,|1\rangle$

![[IBM_tomography_circuits.png]]

the QASM code for the $Y$ one (the others just leave out lines)
```
include "qelib1.inc";
qreg q[5];
creg c[5];
// state preparation
h q[0];
t q[0];
// Y basis
sdg q[0];
h q[0];
measure q[0] -> c[0];
```
## the worked example
### step 0: the state we're trying to make
$H$ then $T$ on $|0\rangle$
$$
\begin{aligned}
H|0\rangle&=\tfrac1{\sqrt2}\big(|0\rangle+|1\rangle\big)\\
T\big(\cdot\big)&=\tfrac1{\sqrt2}\big(|0\rangle+e^{i\pi/4}|1\rangle\big)&&(T\text{ multiplies the }|1\rangle\text{ part by }e^{i\pi/4}=\tfrac{1+i}{\sqrt2})\\
|\psi_1\rangle&=\tfrac1{\sqrt2}|0\rangle+\tfrac{1+i}2|1\rangle
\end{aligned}
$$
its density matrix (column times row, the row has complex conjugates)
$$
\rho_1=\begin{bmatrix}\frac1{\sqrt2}\\\frac{1+i}2\end{bmatrix}\begin{bmatrix}\frac1{\sqrt2}&\frac{1-i}2\end{bmatrix}=\begin{bmatrix}\frac12&\frac{1-i}{2\sqrt2}\\\frac{1+i}{2\sqrt2}&\frac12\end{bmatrix}\approx\begin{bmatrix}0.5&0.354-0.354i\\0.354+0.354i&0.5\end{bmatrix}
$$
so the ideal Bloch vector is $\vec r=(0.707,\ 0.707,\ 0)$: on the equator, halfway between $+x$ and $+y$

**what we expect to see** (using $P(+1)=\frac{1+r}2$): $P_{|0\rangle}=0.5$, $P_{|+\rangle}=P_{|{+i}\rangle}=\frac{1+0.707}2\approx0.854$
### step 1: the counts (1024 runs per basis)

| basis | result $+1$ | result $-1$ |
|---|---|---|
| $Z$ | $\lvert0\rangle$: 489 | $\lvert1\rangle$: 535 |
| $X$ | $\lvert+\rangle$: 835 | $\lvert-\rangle$: 189 |
| $Y$ | $\lvert{+i}\rangle$: 845 | $\lvert{-i}\rangle$: 179 |

### step 2: probabilities (divide by 1024)
$$
\begin{aligned}
P_{|0\rangle}&=\tfrac{489}{1024}=0.478&P_{|1\rangle}&=\tfrac{535}{1024}=0.522\\
P_{|+\rangle}&=\tfrac{835}{1024}=0.815&P_{|-\rangle}&=\tfrac{189}{1024}=0.185\\
P_{|{+i}\rangle}&=\tfrac{845}{1024}=0.825&P_{|{-i}\rangle}&=\tfrac{179}{1024}=0.175
\end{aligned}
$$
### step 3: the expectation values
$$
\begin{aligned}
S_1&=0.815-0.185=0.630\\
S_2&=0.825-0.175=0.650\\
S_3&=0.478-0.522=-0.044
\end{aligned}
$$
### step 4: rebuild $\rho$
$$
\begin{aligned}
\rho_1^E&=\begin{bmatrix}\frac12+\frac12(-0.044)&\frac12(0.630)-\frac12i(0.650)\\\frac12(0.630)+\frac12i(0.650)&\frac12-\frac12(-0.044)\end{bmatrix}\\
&=\begin{bmatrix}0.478&0.315-0.325i\\0.315+0.325i&0.522\end{bmatrix}
\end{aligned}
$$
compare with the ideal $\begin{bmatrix}0.5&0.354-0.354i\\0.354+0.354i&0.5\end{bmatrix}$: close, but not the same, because of **noise** and **sampling error**. the course concludes the state was prepared successfully
## how good was it? (extra, not in the course)
**the Bloch vector shrank**
$$
\|\vec r_E\|=\sqrt{0.630^2+0.650^2+0.044^2}\approx0.906\qquad(\text{ideal: }1)
$$
a length below 1 means the measured state is **mixed**: noise has pulled it inside the Bloch sphere. its purity is $\frac{1+0.906^2}2\approx0.91$

**the fidelity** with the state we wanted ([[State fidelity#noisy states (density matrices)]]), using $F^2=\frac{1+\vec r_E\cdot\vec n}2$ with the ideal direction $\vec n=(0.707,0.707,0)$
$$
\begin{aligned}
\vec r_E\cdot\vec n&=0.630(0.707)+0.650(0.707)+(-0.044)(0)=0.905\\
F^2&=\frac{1+0.905}2\approx0.95\qquad F\approx0.98
\end{aligned}
$$
**is the $Z$ result just bad luck?** with 1024 runs and $P=0.5$, the spread is $\sqrt{1024\times0.5\times0.5}=16$ counts. 489 is 23 below the expected 512, about $1.4$ spreads: normal sampling noise. but $X$ and $Y$ came out about 30–40 counts **below** the expected 874, where the spread is only $\sqrt{1024\times0.854\times0.146}\approx11$ (so 3 spreads or more), which is the real **noise** shrinking the Bloch vector (all checked numerically)

see also [[State tomography]], [[State fidelity]], [[Bloch sphere]], [[QASM]]
