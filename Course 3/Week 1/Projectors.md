#projector #measurement #density_matrix #dirac_notation
a **projector** is the matrix that "picks out" one part of a state. it's how measurement works in the maths, and every pure [[Density matrix|density matrix]] is one. introduced on the [[Course 3/Week 1/Dirac notation|Dirac notation cheat sheet]]
## what it is
the projector onto a state $|\phi\rangle$ is its outer product with itself
$$
\Pi_\phi=|\phi\rangle\langle\phi|
$$
acting on any state, it keeps **only the part along $|\phi\rangle$**
$$
\Pi_\phi|\psi\rangle=|\phi\rangle\langle\phi|\psi\rangle=\underbrace{\langle\phi|\psi\rangle}_{\text{a number}}\ |\phi\rangle
$$
==a projector squashes a state onto one direction, like casting a shadow==
![[Projectors.png]]
## the basic ones
$$
\Pi_0=|0\rangle\langle0|=\begin{bmatrix}1&0\\0&0\end{bmatrix}\qquad\Pi_1=|1\rangle\langle1|=\begin{bmatrix}0&0\\0&1\end{bmatrix}\qquad\Pi_+=|+\rangle\langle+|=\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}
$$
eg. $\Pi_0(\alpha|0\rangle+\beta|1\rangle)=\alpha|0\rangle$: the $|1\rangle$ part is thrown away
## properties

| property | meaning |
|---|---|
| $\Pi^2=\Pi$ | projecting twice is the same as once (the shadow of a shadow is itself) |
| $\Pi^\dagger=\Pi$ | Hermitian, so it's a proper observable |
| eigenvalues $0$ and $1$ | "the part you keep" (1) and "the part you throw away" (0) |
| $\Pi_0\Pi_1=0$ | projectors onto **orthogonal** states kill each other |
| $\Pi_0+\Pi_1=I$ | a complete set adds up to the identity: every part of the state goes somewhere |

(all checked numerically, eg. for $\Pi_+$)
## projectors = measurement
measuring in a basis $\{|i\rangle\}$ is described by the projectors $\Pi_i=|i\rangle\langle i|$ (a **projective measurement**)
> [!important] the measurement rules with projectors
> ==the chance of result $i$ is $P(i)=\langle\psi|\Pi_i|\psi\rangle$==, the squared length of the shadow (the same as $|\langle i|\psi\rangle|^2$ from [[Math/Dirac notation|Dirac notation]])
>
> afterwards the state **collapses** to the projected state, renormalized
> $$
> |\psi\rangle\longrightarrow\frac{\Pi_i|\psi\rangle}{\sqrt{P(i)}}
> $$
> for a density matrix: $P(i)=\text{tr}(\Pi_i\,\rho)$ (see [[Trace]])

> [!example] $|\psi\rangle=\sqrt{0.7}\,|0\rangle+\sqrt{0.3}\,|1\rangle$
> - measure in $0/1$: $P(0)=\langle\psi|\Pi_0|\psi\rangle=0.7$, and the state becomes $|0\rangle$
> - measure in $\pm$: $P(+)=\langle\psi|\Pi_+|\psi\rangle=\frac{(\sqrt{0.7}+\sqrt{0.3})^2}2\approx0.958$
>
> same state, different projectors, different probabilities (checked numerically)

## projectors and density matrices
the density matrix of a **pure** state is just its projector
![[Course 3/Week 1/Dirac notation#^pure-projector]]

and a **mixed** state is a weighted mix of projectors, $\rho=\sum_kp_k|\psi_k\rangle\langle\psi_k|$. so ==$\rho$ is pure exactly when $\rho^2=\rho$== (when it's a projector), see [[Density matrix]]
## measuring just one qubit
on 2 qubits, to measure **only qubit A**, use the projector on A and do nothing ($I$) on B
$$
\Pi_{0_A}=|0\rangle\langle0|\otimes I
$$
> [!example] $\sqrt{\tfrac34}\,|00\rangle+\sqrt{\tfrac14}\,|11\rangle$
> $P(A=0)=\langle\psi|\Pi_{0_A}|\psi\rangle=\frac34$, and afterwards the pair is in $|00\rangle$ (checked numerically). this is the measurement behind "mixture 1" in [[Density matrix#bipartite state example]]. full step by step version: [[Density matrix practice]]

see also [[Kets and bras combined]] (all 16 combinations of $|0\rangle,|1\rangle,\langle0|,\langle1|$), [[Course 3/Week 1/Dirac notation|Dirac notation cheat sheet]], [[Density matrix]], [[Math/Dirac notation]], [[Tensor product]]
