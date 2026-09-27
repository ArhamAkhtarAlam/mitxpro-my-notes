#math #eigenvalues #linear_algebra
the maths behind a lot of quantum stuff: measurements, the [[Density matrix]], [[Von Neumann entropy]], [[Quantum Phase Estimation]]
## the idea
a matrix $A$ is a **transformation**: you give it a vector and it gives you back a new vector (it can stretch it, squish it, rotate it...)

most vectors get **knocked off their line** (they change direction)

but some special vectors **stay on their own line**, the matrix only **stretches** them. those are the **eigenvectors**

how much they get stretched is the **eigenvalue**
$$
A\,\vec v=\lambda\,\vec v
$$
- $\vec v$ → the eigenvector (the direction that doesn't change)
- $\lambda$ → the eigenvalue (the stretch factor)

![[Eigenvectors.png]]
> [!tip] what the eigenvalue means
> - $\lambda=3$ → stretched to 3 times as long
> - $\lambda=1$ → stays exactly the same
> - $\lambda=0$ → squished to nothing
> - $\lambda=-1$ → flipped to point the other way (still on the same line!)
> - $\lambda=i$ or any [[Complex numbers|complex number]] → a phase (this is the quantum case)
## example
$$
A=\begin{bmatrix}2&1\\1&2\end{bmatrix}
$$
try a normal vector
$$
A\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}2\\1\end{bmatrix}
$$
that's a different direction, so $(1,0)$ is **not** an eigenvector

try $(1,1)$
$$
A\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}3\\3\end{bmatrix}=3\begin{bmatrix}1\\1\end{bmatrix}
$$
same direction, just 3 times longer → eigenvector with **eigenvalue 3**

try $(1,-1)$
$$
A\begin{bmatrix}1\\-1\end{bmatrix}=\begin{bmatrix}1\\-1\end{bmatrix}=1\begin{bmatrix}1\\-1\end{bmatrix}
$$
exactly the same → eigenvector with **eigenvalue 1**
## how to find them
> [!example]- step by step
> **1. find the eigenvalues:** solve
> $$
> \det(A-\lambda I)=0
> $$
> for our $A$
> $$
> \det\begin{bmatrix}2-\lambda&1\\1&2-\lambda\end{bmatrix}=(2-\lambda)^2-1=0
> $$
> so $2-\lambda=\pm1$, which gives $\lambda=3$ and $\lambda=1$
>
> **2. find the eigenvector for each one:** plug each $\lambda$ back into $(A-\lambda I)\vec v=0$
>
> for $\lambda=3$
> $$
> \begin{bmatrix}-1&1\\1&-1\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=0\;\Rightarrow\;x=y\;\Rightarrow\;\vec v=(1,1)
> $$
> for $\lambda=1$
> $$
> \begin{bmatrix}1&1\\1&1\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=0\;\Rightarrow\;x=-y\;\Rightarrow\;\vec v=(1,-1)
> $$

(a $2\times2$ matrix has 2 eigenvalues, an $n\times n$ matrix has $n$)
## why it matters in quantum
### gates
| gate | eigenvectors | eigenvalues |
|---|---|---|
| [[Z gate]] | $\lvert0\rangle$, $\lvert1\rangle$ | $+1$, $-1$ |
| [[X gate]] | $\lvert+\rangle$, $\lvert-\rangle$ | $+1$, $-1$ |
| [[Phase shift\|S gate]] | $\lvert0\rangle$, $\lvert1\rangle$ | $1$, $i$ |

eg. $X|-\rangle=-|-\rangle$: the X gate just flips the sign of $|-\rangle$, it doesn't change it into a different state

every [[Unitary Operation|unitary]] has eigenvalues of size 1, like $e^{i\varphi}$ (a pure phase), because unitaries can't stretch or shrink anything
### measurements
> [!important] measuring = eigenvalues + eigenvectors
> when you measure an observable like $\sigma_z$
> - the **possible results** are its **eigenvalues** ($+1$ or $-1$)
> - after measuring, the state **becomes the eigenvector** for the result you got ($|0\rangle$ or $|1\rangle$)
>
> that's why measuring $\sigma_z$ is "measuring in the $|0\rangle,|1\rangle$ basis" and measuring $\sigma_x$ is "measuring in the $|+\rangle,|-\rangle$ basis" (like in the [[CHSH quantum strategy]])
### density matrices
the eigenvalues of a [[Density matrix]] are **probabilities** (they're all $\geq0$ and add up to 1), and the eigenvectors are the states they go with. that's the spectral **unravelling**

eg. $\rho=\begin{bmatrix}\frac34&0\\0&\frac14\end{bmatrix}$ has eigenvalues $\frac34$ and $\frac14$, so it's $|0\rangle$ with probability $\frac34$ and $|1\rangle$ with probability $\frac14$

the [[Von Neumann entropy]] is just the [[Shannon entropy]] of these eigenvalues
### phase estimation
[[Quantum Phase Estimation]] finds the eigenvalue $e^{2\pi i\theta}$ of a unitary, and that's the core of [[Shor's algorithm]]

see also [[Unitary Operation]], [[Density matrix]], [[Math]]
