#textbook #density_matrix #bloch_sphere
*Quantum Computation and Quantum Information* §2.4.2 (p. 101–105). instead of building $\rho$ from an ensemble, this section says what a density operator **is** on its own, then rewrites all of quantum mechanics with it. part of [[Quantum Computation and Quantum Information]], previous: [[Ensembles of quantum states]]
## theorem 2.5: what makes something a density operator
> [!important] characterization of density operators
> ==an operator $\rho$ comes from some ensemble $\{p_i,|\psi_i\rangle\}$ **if and only if**==
> 1. **trace condition**: $\text{tr}(\rho)=1$
> 2. **positivity condition**: $\rho$ is positive, $\langle\varphi|\rho|\varphi\rangle\geq0$ for every $|\varphi\rangle$

> [!note]- proof
> **ensemble → conditions.** take $\rho=\sum_ip_i|\psi_i\rangle\langle\psi_i|$
> $$
> \begin{aligned}
> \text{tr}(\rho)&=\sum_ip_i\,\text{tr}(|\psi_i\rangle\langle\psi_i|)=\sum_ip_i=1\\
> \langle\varphi|\rho|\varphi\rangle&=\sum_ip_i\langle\varphi|\psi_i\rangle\langle\psi_i|\varphi\rangle=\sum_ip_i|\langle\varphi|\psi_i\rangle|^2\geq0
> \end{aligned}
> $$
> **conditions → ensemble.** a positive operator has a spectral decomposition $\rho=\sum_j\lambda_j|j\rangle\langle j|$ with orthonormal $|j\rangle$ and real $\lambda_j\geq0$. the trace condition gives $\sum_j\lambda_j=1$, so $\{\lambda_j,|j\rangle\}$ **is** an ensemble that gives $\rho$ ∎

so you can **define** a density operator as "positive, trace 1", no ensemble needed
## the postulates, rewritten with $\rho$
1. **state space**: a closed system is described by a positive operator $\rho$ with trace 1 on its Hilbert space. if it's in $\rho_i$ with probability $p_i$, the state is $\sum_ip_i\rho_i$
2. **evolution**: a closed system evolves by a unitary, $\rho'=U\rho\,U^\dagger$
3. **measurement**: operators $\{M_m\}$ with $\sum_mM_m^\dagger M_m=I$ (the completeness equation)
$$
p(m)=\text{tr}(M_m^\dagger M_m\rho)\qquad\qquad\rho\ \to\ \frac{M_m\rho M_m^\dagger}{\text{tr}(M_m^\dagger M_m\rho)}
$$
4. **composite systems**: the state space is the tensor product, and independent parts prepared in $\rho_1,\ldots,\rho_n$ give $\rho_1\otimes\rho_2\otimes\cdots\otimes\rho_n$

this is mathematically the same as the state vector version. ==$\rho$ really shines for 2 things: states you don't know exactly, and parts of bigger systems== ([[Reduced density operator]])
## the eigenvalues are NOT "what the state really is"
a common mistake: thinking the eigen decomposition tells you what's "really" in the mixture. take
$$
\rho=\tfrac34|0\rangle\langle0|+\tfrac14|1\rangle\langle1|
$$
it looks like "$|0\rangle$ 75% of the time, $|1\rangle$ 25%". but define
$$
|a\rangle=\sqrt{\tfrac34}|0\rangle+\sqrt{\tfrac14}|1\rangle\qquad|b\rangle=\sqrt{\tfrac34}|0\rangle-\sqrt{\tfrac14}|1\rangle
$$
and prepare each with probability $\frac12$
$$
\begin{aligned}
\tfrac12|a\rangle\langle a|+\tfrac12|b\rangle\langle b|&=\tfrac12\begin{bmatrix}\frac34&\frac{\sqrt3}4\\\frac{\sqrt3}4&\frac14\end{bmatrix}+\tfrac12\begin{bmatrix}\frac34&-\frac{\sqrt3}4\\-\frac{\sqrt3}4&\frac14\end{bmatrix}\\
&=\tfrac34|0\rangle\langle0|+\tfrac14|1\rangle\langle1|
\end{aligned}
$$
==2 different ensembles, the **same** $\rho$, and no measurement can tell them apart==. (it's the same pair as the course's [[Density matrix#bipartite state example]])
## theorem 2.6: unitary freedom in the ensemble
which ensembles give the same $\rho$? use **unnormalized** vectors $|\tilde\psi_i\rangle=\sqrt{p_i}\,|\psi_i\rangle$, so $\rho=\sum_i|\tilde\psi_i\rangle\langle\tilde\psi_i|$
> [!important] unitary freedom
> ==$\{|\tilde\psi_i\rangle\}$ and $\{|\tilde\varphi_j\rangle\}$ give the same $\rho$ if and only if $|\tilde\psi_i\rangle=\sum_ju_{ij}|\tilde\varphi_j\rangle$ for a unitary matrix $u$== (pad the smaller set with zero vectors so they're the same size). with normalized states:
> $$
> \sqrt{p_i}\,|\psi_i\rangle=\sum_ju_{ij}\sqrt{q_j}\,|\varphi_j\rangle
> $$

^unitary-freedom

> [!example] the example above is a Hadamard
> $|\tilde\varphi_0\rangle=\sqrt{\tfrac34}|0\rangle$, $|\tilde\varphi_1\rangle=\sqrt{\tfrac14}|1\rangle$ and $|\tilde\psi_{a}\rangle=\sqrt{\tfrac12}|a\rangle$, $|\tilde\psi_{b}\rangle=\sqrt{\tfrac12}|b\rangle$. then
> $$
> \begin{bmatrix}|\tilde\psi_a\rangle\\|\tilde\psi_b\rangle\end{bmatrix}=\frac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}\begin{bmatrix}|\tilde\varphi_0\rangle\\|\tilde\varphi_1\rangle\end{bmatrix}
> $$
> so $u=H$, which is unitary ✅

> [!note]- proof
> **unitary → same $\rho$.** if $|\tilde\psi_i\rangle=\sum_ju_{ij}|\tilde\varphi_j\rangle$
> $$
> \begin{aligned}
> \sum_i|\tilde\psi_i\rangle\langle\tilde\psi_i|&=\sum_{ijk}u_{ij}u_{ik}^*\,|\tilde\varphi_j\rangle\langle\tilde\varphi_k|=\sum_{jk}\Big(\sum_iu^\dagger_{ki}u_{ij}\Big)|\tilde\varphi_j\rangle\langle\tilde\varphi_k|\\
> &=\sum_{jk}\delta_{kj}\,|\tilde\varphi_j\rangle\langle\tilde\varphi_k|=\sum_j|\tilde\varphi_j\rangle\langle\tilde\varphi_j|
> \end{aligned}
> $$
> using $u^\dagger u=I$.
>
> **same $\rho$ → unitary.** write $A=\sum_k\lambda_k|k\rangle\langle k|$ with $\lambda_k>0$ and set $|\tilde k\rangle=\sqrt{\lambda_k}|k\rangle$. any $|\psi\rangle$ orthogonal to all the $|\tilde k\rangle$ gives $0=\langle\psi|A|\psi\rangle=\sum_i|\langle\psi|\tilde\psi_i\rangle|^2$, so every $|\tilde\psi_i\rangle$ lies in the span of the $|\tilde k\rangle$: $|\tilde\psi_i\rangle=\sum_kc_{ik}|\tilde k\rangle$. then $\sum_k|\tilde k\rangle\langle\tilde k|=\sum_{kl}\big(\sum_ic_{ik}c^*_{il}\big)|\tilde k\rangle\langle\tilde l|$, and since the $|\tilde k\rangle\langle\tilde l|$ are linearly independent, $\sum_ic_{ik}c_{il}^*=\delta_{kl}$. so the columns of $c$ are orthonormal and can be extended to a unitary $v$ with $|\tilde\psi_i\rangle=\sum_kv_{ik}|\tilde k\rangle$. the same for $|\tilde\varphi_j\rangle=\sum_kw_{jk}|\tilde k\rangle$, so $|\tilde\psi_i\rangle=\sum_ju_{ij}|\tilde\varphi_j\rangle$ with $u=vw^\dagger$, unitary ∎

this freedom matters a lot later for **noise** and **error correction** (chapters 8 and 10)
## the Bloch sphere for mixed states (exercise 2.72)
any 1 qubit density matrix can be written
$$
\rho=\frac{I+\vec r\cdot\vec\sigma}2=\frac12\begin{bmatrix}1+r_z&r_x-ir_y\\r_x+ir_y&1-r_z\end{bmatrix}\qquad\|\vec r\|\leq1
$$
^bloch-rho

- $\vec r$ is the **Bloch vector**
- $\rho=\frac I2$ is $\vec r=0$, the centre
- ==pure ⟺ $\|\vec r\|=1$== (on the surface), see [[Chapter 2 exercises#2.72 the Bloch sphere for mixed states]] and [[Bloch sphere]]

## minimal ensembles (exercise 2.73)
a **minimal ensemble** for $\rho$ has as many states as the rank of $\rho$. any $|\psi\rangle$ in the support of $\rho$ (the span of its eigenvectors with non-zero eigenvalue) can be in one, and it then has to appear with probability
$$
p=\frac1{\langle\psi|\rho^{-1}|\psi\rangle}
$$
($\rho^{-1}$ only on the support). eg. $\rho=\frac I2$: $\rho^{-1}=2I$, so any $|\psi\rangle$ appears with probability $\frac12$ (like $|+\rangle,|-\rangle$ at 50/50)

next: [[Reduced density operator]]
