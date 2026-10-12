#partial_transpose #entanglement #PPT #density_matrix
transposing just **one part** of a 2 qubit density matrix. it's not a physical operation (see [[Quantum operations#the transpose example (positive, but not completely positive)|why]]), but it's a great **test for entanglement**
## what it does
write the $4\times4$ density matrix as four $2\times2$ blocks. the partial transpose on the second qubit, $\rho^{T_B}$, transposes **each block**
$$
\rho=\begin{bmatrix}P&Q\\R&S\end{bmatrix}\quad\longrightarrow\quad\rho^{T_B}=\begin{bmatrix}P^T&Q^T\\R^T&S^T\end{bmatrix}
$$
(ordering $|00\rangle,|01\rangle,|10\rangle,|11\rangle$, see [[Tensor product]]). the trace stays 1, but the eigenvalues can change
## the PPT test (Peres–Horodecki)
> [!important] the test
> ==if $\rho^{T_B}$ has a **negative** eigenvalue, the state is **entangled**==
>
> for 2 qubits (and a qubit with a qutrit) it works both ways: **no** negative eigenvalue means **not** entangled

("PPT" = positive partial transpose = passes, not entangled)
> [!example]- why it works
> an unentangled state is a mixture of product states, $\rho=\sum_ip_i\,\rho_i^A\otimes\rho_i^B$. the partial transpose only transposes each $\rho_i^B$, which is still a legal state (same eigenvalues). so $\rho^{T_B}$ is still a mixture of legal states, so it's positive
>
> so a negative eigenvalue can **only** come from entanglement ([[Defining entanglement]])

## examples

| state | eigenvalues of $\rho^{T_B}$ | entangled? |
|---|---|---|
| product state, eg. $\lvert0\rangle\lvert+\rangle$ | all $\geq0$ | no |
| Bell state $\frac1{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$ | $-\frac12,\ \frac12,\ \frac12,\ \frac12$ | **yes** |
| noisy Bell state (below) | smallest is $\frac{1-3p}4$ | only if $p>\frac13$ |

(all checked numerically)
## the course's worked example
**a product state stays legal.** for $|\psi_A\rangle=\alpha|0\rangle+\beta|1\rangle$ and $|\psi_B\rangle=\gamma|0\rangle+\delta|1\rangle$, the partial transpose just swaps B's off diagonal entries ($\gamma\delta^*\leftrightarrow\gamma^*\delta$)
$$
\rho_{AB}=\begin{bmatrix}|\alpha|^2&\alpha\beta^*\\\alpha^*\beta&|\beta|^2\end{bmatrix}\otimes\begin{bmatrix}|\gamma|^2&\gamma\delta^*\\\gamma^*\delta&|\delta|^2\end{bmatrix}\quad\to\quad\rho_{AB}^{T_B}=\begin{bmatrix}|\alpha|^2&\alpha\beta^*\\\alpha^*\beta&|\beta|^2\end{bmatrix}\otimes\begin{bmatrix}|\gamma|^2&\gamma^*\delta\\\gamma\delta^*&|\delta|^2\end{bmatrix}
$$
that's B's Bloch vector **flipped across the xz plane** ($y\to-y$), which is still a valid state, so nothing goes negative

**an entangled state doesn't.** for $|\Psi^+\rangle=\frac{|01\rangle+|10\rangle}{\sqrt2}$
$$
\rho_{AB}=\frac12\begin{bmatrix}0&0&0&0\\0&1&1&0\\0&1&1&0\\0&0&0&0\end{bmatrix}\quad\xrightarrow{T_B}\quad\rho_{AB}^{T_B}=\frac12\begin{bmatrix}0&0&0&1\\0&1&0&0\\0&0&1&0\\1&0&0&0\end{bmatrix}\quad\xrightarrow{\text{diagonalize}}\quad\frac12\begin{bmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}
$$
(the 1s in the off diagonal blocks $Q$ and $R$ moved to the corners when each block was transposed). the trace is still 1, but one eigenvalue is $-\frac12$ → entangled
### a shortcut: leading minors (Sylvester's criterion)
you only need to know if **some** eigenvalue is negative, not what it is. take determinants of the top left $1\times1$, $2\times2$, $3\times3$ and $4\times4$ corners (without the $\frac12$)
$$
|0|=0\qquad\begin{vmatrix}0&0\\0&1\end{vmatrix}=0\qquad\begin{vmatrix}0&0&0\\0&1&0\\0&0&1\end{vmatrix}=0\qquad\begin{vmatrix}0&0&0&1\\0&1&0&0\\0&0&1&0\\1&0&0&0\end{vmatrix}=-1
$$
the whole determinant is the **product** of the eigenvalues, so a negative one means an odd number of negative eigenvalues: not positive → entangled. often quicker than diagonalizing
> [!warning] it only works one way (extra)
> a negative leading minor **proves** a negative eigenvalue. but all leading minors $\geq0$ (with some $=0$, like the first 3 here) doesn't prove positivity: for that you need every principal minor, not just the top left ones

### how entangled? the partial **trace**
once you know it's entangled: if tracing out one half gives $\frac I2$ (a diagonal matrix with equal entries), the state is **maximally** entangled. for $|\Psi^+\rangle$
$$
\rho_A=\text{tr}_B\,\rho_{AB}=\frac{|0\rangle\langle0|+|1\rangle\langle1|}2=\frac I2
$$
the same for all 4 [[Bell states]]: the pair is pure, but each half alone is completely mixed ([[Partial trace]], [[Entanglement entropy]])

## noisy Bell states (Werner states)
mix the Bell state with completely random noise
$$
\rho=p\,|\Phi^+\rangle\langle\Phi^+|+(1-p)\,\frac I4
$$
the smallest eigenvalue of the partial transpose is $\frac{1-3p}4$, which goes negative once $p>\frac13$
![[Partial_transpose_Werner.png]]
so ==a Bell state survives as entangled until about 2/3 of it has been replaced by noise== ($p=\frac13$). useful for knowing when noisy pairs can still be used, eg. in [[Entanglement purification]] (which needs $F>\frac12$, the same point, since $F=\frac{1+3p}4$)

see also [[Quantum operations]], [[Defining entanglement]], [[Bell states]], [[Density matrix]]
