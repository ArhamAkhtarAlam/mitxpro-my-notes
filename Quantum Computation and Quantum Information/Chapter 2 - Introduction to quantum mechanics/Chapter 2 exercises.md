#textbook #density_matrix #entanglement #exercises
worked answers to the exercises on p. 98–111 of the book. part of [[Quantum Computation and Quantum Information]]. (all numbers checked numerically)
## 2.69 the Bell basis is orthonormal
the 4 Bell states, labelled by the 2 bits Alice sends in [[Superdense coding]] ($00\to\Phi^+$, $01\to\Phi^-$, $10\to\Psi^+$, $11\to\Psi^-$)
$$
|\Phi^+\rangle=\tfrac{|00\rangle+|11\rangle}{\sqrt2}\quad|\Phi^-\rangle=\tfrac{|00\rangle-|11\rangle}{\sqrt2}\quad|\Psi^+\rangle=\tfrac{|10\rangle+|01\rangle}{\sqrt2}\quad|\Psi^-\rangle=\tfrac{|01\rangle-|10\rangle}{\sqrt2}
$$
- **normalized**: each is 2 basis states with amplitude $\pm\frac1{\sqrt2}$, so $\frac12+\frac12=1$
- **orthogonal**: $\Phi^+,\Phi^-$ only use $|00\rangle,|11\rangle$, and $\Psi^+,\Psi^-$ only use $|01\rangle,|10\rangle$, so any pair across the 2 groups has overlap 0. within a group: $\langle\Phi^+|\Phi^-\rangle=\frac12(1-1)=0$ and $\langle\Psi^+|\Psi^-\rangle=\frac12(1-1)=0$
- 4 orthonormal vectors in a 4 dimensional space → a basis ∎
## 2.70 Eve learns nothing in superdense coding
for any operator $E$ on Alice's qubit, $\langle\psi|E\otimes I|\psi\rangle=\text{tr}\big((E\otimes I)\rho\big)=\text{tr}(E\rho^A)$ ([[Reduced density operator#why the partial trace? (Box 2.6)|Box 2.6]]). every Bell state has $\rho^A=\frac I2$ (exercise 2.75), so
$$
\langle\psi|E\otimes I|\psi\rangle=\text{tr}\big(E\tfrac I2\big)=\tfrac12\text{tr}(E)\qquad\text{for all 4 Bell states}
$$
==Eve only gets Alice's qubit, and it looks exactly the same ($\frac I2$) whichever of $00,01,10,11$ Alice sent==, so no measurement on it tells her anything
## 2.71 pure or mixed
**show** $\text{tr}(\rho^2)\leq1$, with $=1$ only for a pure state. write $\rho=\sum_i\lambda_i|i\rangle\langle i|$ ($\lambda_i\geq0$, $\sum_i\lambda_i=1$)
$$
\begin{aligned}
\text{tr}(\rho^2)&=\sum_i\lambda_i^2\\
&\leq\Big(\sum_i\lambda_i\Big)^2=1&&\text{(the cross terms }2\lambda_i\lambda_j\geq0\text{ are dropped)}
\end{aligned}
$$
equality needs every cross term $\lambda_i\lambda_j=0$, so only one $\lambda_i$ is non-zero (and it's 1). then $\rho=|i\rangle\langle i|$, a pure state ∎ (see [[Pure state#how to check if a state is pure]])
## 2.72 the Bloch sphere for mixed states
**(1)** $I,X,Y,Z$ are a basis for $2\times2$ matrices. $\rho$ is Hermitian, so its coefficients are real, and $\text{tr}(\rho)=1$ fixes the $I$ part
$$
\rho=\frac{I+r_xX+r_yY+r_zZ}2=\frac12\begin{bmatrix}1+r_z&r_x-ir_y\\r_x+ir_y&1-r_z\end{bmatrix}
$$
the eigenvalues are $\frac{1\pm\|\vec r\|}2$, and positivity needs both $\geq0$, so $\|\vec r\|\leq1$

**(2)** $\rho=\frac I2$ → $\vec r=0$, the centre of the ball

**(3)** $\text{tr}(\rho^2)=\big(\frac{1+r}2\big)^2+\big(\frac{1-r}2\big)^2=\frac{1+\|\vec r\|^2}2$, which is 1 exactly when $\|\vec r\|=1$

**(4)** for $|\psi\rangle=\cos\frac\theta2|0\rangle+e^{i\varphi}\sin\frac\theta2|1\rangle$, matching $|\psi\rangle\langle\psi|$ to the matrix above gives
$$
\vec r=(\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta)
$$
the same point as the [[Bloch sphere]] picture for pure states ✅
## 2.73 minimal ensembles
the idea: if $|\psi\rangle$ is in the support, write $\rho=\sum_k|\tilde k\rangle\langle\tilde k|$ with $|\tilde k\rangle=\sqrt{\lambda_k}|k\rangle$. by [[General properties of the density operator#theorem 2.6: unitary freedom in the ensemble|unitary freedom]], a minimal ensemble containing $\sqrt p\,|\psi\rangle$ needs $\sqrt p\,|\psi\rangle=\sum_ku_k|\tilde k\rangle$ with $\sum_k|u_k|^2=1$ (one row of a unitary). solving, $u_k=\sqrt p\,\frac{\langle k|\psi\rangle}{\sqrt{\lambda_k}}$, so
$$
1=\sum_k|u_k|^2=p\sum_k\frac{|\langle k|\psi\rangle|^2}{\lambda_k}=p\,\langle\psi|\rho^{-1}|\psi\rangle\quad\Rightarrow\quad p=\frac1{\langle\psi|\rho^{-1}|\psi\rangle}
$$
and the rest of the unitary fills in the other members
## 2.74 a product state has pure halves
$$
\rho^A=\text{tr}_B\big(|a\rangle\langle a|\otimes|b\rangle\langle b|\big)=|a\rangle\langle a|\ \langle b|b\rangle=|a\rangle\langle a|
$$
which is pure ∎
## 2.75 the reduced states of the Bell states
the same calculation as for $|\Phi^+\rangle$ in [[Reduced density operator#example 2: a Bell state]]: each Bell state is 2 terms whose bits **both** differ, so the cross terms vanish under either partial trace

| state | $\rho^A$ | $\rho^B$ |
|---|---|---|
| $\lvert\Phi^+\rangle,\lvert\Phi^-\rangle$ | $\frac I2$ | $\frac I2$ |
| $\lvert\Psi^+\rangle,\lvert\Psi^-\rangle$ | $\frac I2$ | $\frac I2$ |

all 8 are completely mixed
## 2.76 Schmidt for different sizes
same proof, but $a$ is now an $m\times n$ matrix. its SVD is $a=udv$ with $u$ ($m\times m$) and $v$ ($n\times n$) unitary and $d$ an $m\times n$ "diagonal" matrix. there are only $\min(m,n)$ diagonal entries, so the sum $\sum_i\lambda_i|i_A\rangle|i_B\rangle$ has at most $\min(m,n)$ terms
## 2.77 no Schmidt form for 3 systems
try $|\psi\rangle=|0\rangle\otimes\frac{|00\rangle+|11\rangle}{\sqrt2}$ on $ABC$. suppose it were $\sum_i\lambda_i|i_A\rangle|i_B\rangle|i_C\rangle$. then
$$
\rho^A=\sum_i\lambda_i^2|i_A\rangle\langle i_A|\qquad\rho^B=\sum_i\lambda_i^2|i_B\rangle\langle i_B|
$$
have the same eigenvalues. but $\rho^A=|0\rangle\langle0|$ (pure, eigenvalues $1,0$) and $\rho^B=\frac I2$ (eigenvalues $\frac12,\frac12$). contradiction, so it can't be written that way ∎
## 2.78 product ⟺ Schmidt number 1 ⟺ pure halves
- **product → Schmidt number 1**: $|a\rangle|b\rangle$ is already a Schmidt form with one term
- **Schmidt number 1 → product**: $\lambda_1|1_A\rangle|1_B\rangle$ with $\lambda_1=1$ is a product
- **Schmidt number 1 ⟺ $\rho^A$ pure**: $\rho^A=\sum_i\lambda_i^2|i_A\rangle\langle i_A|$ is pure exactly when only one $\lambda_i$ is non-zero ∎
## 2.79 three Schmidt decompositions
**(a)** $\frac{|00\rangle+|11\rangle}{\sqrt2}$ is already one: $\lambda=\frac1{\sqrt2},\frac1{\sqrt2}$ with the bases $|0\rangle,|1\rangle$

**(b)** $\frac{|00\rangle+|01\rangle+|10\rangle+|11\rangle}2=\frac{|0\rangle+|1\rangle}{\sqrt2}\otimes\frac{|0\rangle+|1\rangle}{\sqrt2}=|+\rangle|+\rangle$, Schmidt number 1 (not entangled)

**(c)** $\frac{|00\rangle+|01\rangle+|10\rangle}{\sqrt3}$: the matrix is $a=\frac1{\sqrt3}\begin{bmatrix}1&1\\1&0\end{bmatrix}$. it's symmetric, with eigenvalues $\frac{1\pm\sqrt5}2$, ie. $\phi\approx1.618$ and $-\frac1\phi\approx-0.618$ ($\phi$ = the golden ratio)
$$
\begin{aligned}
|e_1\rangle&\approx0.851|0\rangle+0.526|1\rangle\qquad|e_2\rangle\approx0.526|0\rangle-0.851|1\rangle\\
|\psi\rangle&=\frac\phi{\sqrt3}|e_1\rangle|e_1\rangle+\frac1{\phi\sqrt3}|e_2\rangle\big(-|e_2\rangle\big)\approx0.934\,|e_1\rangle|e_1\rangle+0.357\,|e_2\rangle\big(-|e_2\rangle\big)
\end{aligned}
$$
(the minus sign goes into $B$'s basis vector so $\lambda_i\geq0$). check: $0.934^2+0.357^2=1$ ✅
## 2.80 same Schmidt coefficients → related by local unitaries
$|\psi\rangle=\sum_i\lambda_i|i_A\rangle|i_B\rangle$ and $|\varphi\rangle=\sum_i\lambda_i|i'_A\rangle|i'_B\rangle$. let $U$ map $|i'_A\rangle\to|i_A\rangle$ and $V$ map $|i'_B\rangle\to|i_B\rangle$ (unitary, since they map one orthonormal basis to another). then $(U\otimes V)|\varphi\rangle=\sum_i\lambda_i|i_A\rangle|i_B\rangle=|\psi\rangle$ ∎
## 2.81 freedom in purifications
2 purifications $|AR_1\rangle$, $|AR_2\rangle$ of the same $\rho^A$ both have Schmidt forms with $A$'s basis = the eigenvectors of $\rho^A$ and coefficients $\sqrt{p_i}$. so they have the same Schmidt coefficients, and by 2.80 they differ by a unitary on $R$ only (the one on $A$ can be the identity, since the $A$ bases already match): $|AR_1\rangle=(I_A\otimes U_R)|AR_2\rangle$ ∎
## 2.82 purifying an ensemble
**(1)** $|AR\rangle=\sum_i\sqrt{p_i}|\psi_i\rangle|i\rangle$ ($|\psi_i\rangle$ don't need to be orthogonal, the $|i\rangle$ are)
$$
\text{tr}_R\big(|AR\rangle\langle AR|\big)=\sum_{ij}\sqrt{p_ip_j}\,|\psi_i\rangle\langle\psi_j|\,\langle j|i\rangle=\sum_ip_i|\psi_i\rangle\langle\psi_i|=\rho\ ✅
$$
**(2)** measure $R$ in $|i\rangle$: the projector $I\otimes|i\rangle\langle i|$ leaves $\sqrt{p_i}|\psi_i\rangle|i\rangle$, so you get $i$ with probability $p_i$ and $A$ is left in $|\psi_i\rangle$

**(3)** any purification differs from the one in (1) by a unitary $U_R$ on $R$ (2.81). so measure $R$ in the basis $U_R|i\rangle$ instead, and you get $i$ with probability $p_i$ and $A$ in $|\psi_i\rangle$ ∎

==so every way of writing $\rho$ as an ensemble comes from measuring some purification==
