#textbook #schmidt_decomposition #purification #entanglement
*Quantum Computation and Quantum Information* §2.5 (p. 109–111). 2 more tools for composite systems, both "indispensable" later. part of [[Quantum Computation and Quantum Information]], previous: [[Reduced density operator]]. course versions: [[Schmidt decomposition]], [[Schmidt number]], [[Purification]]
## theorem 2.7: the Schmidt decomposition
> [!important] Schmidt decomposition
> ==any pure state $|\psi\rangle$ of a 2 part system $AB$ can be written as==
> $$
> |\psi\rangle=\sum_i\lambda_i\,|i_A\rangle|i_B\rangle
> $$
> with $|i_A\rangle$ orthonormal in $A$, $|i_B\rangle$ orthonormal in $B$, and real $\lambda_i\geq0$ with $\sum_i\lambda_i^2=1$ (the **Schmidt coefficients**)

^schmidt

**proof** (for $A$ and $B$ the same size; the general case is exercise 2.76). in any bases $|j\rangle$, $|k\rangle$
$$
\begin{aligned}
|\psi\rangle&=\sum_{jk}a_{jk}\,|j\rangle|k\rangle&&\text{(}a\text{ is a matrix of complex numbers)}\\
&=\sum_{ijk}u_{ji}\,d_{ii}\,v_{ik}\,|j\rangle|k\rangle&&\text{(singular value decomposition }a=udv\text{, }d\text{ diagonal}\geq0)\\
&=\sum_i\lambda_i\,|i_A\rangle|i_B\rangle&&\text{(}|i_A\rangle=\textstyle\sum_ju_{ji}|j\rangle,\ |i_B\rangle=\sum_kv_{ik}|k\rangle,\ \lambda_i=d_{ii})
\end{aligned}
$$
the new bases are orthonormal because $u$ and $v$ are unitary ∎
## the big consequence: both halves look alike
from the Schmidt form
$$
\rho^A=\sum_i\lambda_i^2\,|i_A\rangle\langle i_A|\qquad\qquad\rho^B=\sum_i\lambda_i^2\,|i_B\rangle\langle i_B|
$$
==for a pure state, $\rho^A$ and $\rho^B$ have the **same eigenvalues** $\lambda_i^2$==, so anything that depends only on the eigenvalues (purity, [[Entanglement entropy|entropy]]) is the same for both halves
> [!example] the book's example: $|\psi\rangle=\frac1{\sqrt3}(|00\rangle+|01\rangle+|11\rangle)$
> no obvious symmetry, but
> $$
> \begin{aligned}
> \rho^A&=\frac13\begin{bmatrix}2&1\\1&1\end{bmatrix}\qquad\rho^B=\frac13\begin{bmatrix}1&1\\1&2\end{bmatrix}\\
> \text{tr}\big((\rho^A)^2\big)&=\frac{4+1+1+1}9=\frac79=\text{tr}\big((\rho^B)^2\big)
> \end{aligned}
> $$
> the eigenvalues of both are $\lambda_i^2\approx0.873,\ 0.127$ (checked numerically)

## the Schmidt number
- the **Schmidt bases**: the $|i_A\rangle$ and $|i_B\rangle$
- the **Schmidt number**: how many $\lambda_i$ are non-zero. it measures (roughly) **how much entanglement** there is
- it **can't change** under a unitary on $A$ (or $B$) alone: $\sum_i\lambda_i(U|i_A\rangle)|i_B\rangle$ is the Schmidt form of $(U\otimes I)|\psi\rangle$, with the same $\lambda_i$

> [!tip] product test (exercise 2.78)
> ==$|\psi\rangle$ is a product state ⟺ Schmidt number 1 ⟺ $\rho^A$ (and $\rho^B$) is pure==

## purification
given a mixed state $\rho^A$, add a **reference system** $R$ and build a **pure** state $|AR\rangle$ with
$$
\rho^A=\text{tr}_R\big(|AR\rangle\langle AR|\big)
$$
$R$ is a made up system with no direct physical meaning, it's a maths trick to turn mixed states into pure ones
**the construction**: write $\rho^A=\sum_ip_i|i^A\rangle\langle i^A|$ (orthonormal), give $R$ the same size with basis $|i^R\rangle$, and set
$$
|AR\rangle\equiv\sum_i\sqrt{p_i}\,|i^A\rangle|i^R\rangle
$$
^purification

**check**
$$
\begin{aligned}
\text{tr}_R\big(|AR\rangle\langle AR|\big)&=\sum_{ij}\sqrt{p_ip_j}\,|i^A\rangle\langle j^A|\ \text{tr}\big(|i^R\rangle\langle j^R|\big)\\
&=\sum_{ij}\sqrt{p_ip_j}\,|i^A\rangle\langle j^A|\,\delta_{ij}=\sum_ip_i\,|i^A\rangle\langle i^A|=\rho^A\ ✅
\end{aligned}
$$
==a purification **is** a Schmidt decomposition==: the Schmidt basis of $A$ is the basis where $\rho^A$ is diagonal, and the Schmidt coefficients are $\sqrt{p_i}$, the square roots of $\rho^A$'s eigenvalues
> [!example] purifying $\frac I2$
> $p_0=p_1=\frac12$, so $|AR\rangle=\frac1{\sqrt2}(|0\rangle|0\rangle+|1\rangle|1\rangle)$, a Bell state. the completely mixed qubit is half of a maximally entangled pair

> [!tip] exercises
> 2.76–2.82 (more Schmidt decompositions, the freedom in purifications, purifying an ensemble) are in [[Chapter 2 exercises]]

next: [[EPR and the Bell inequality]]
