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
## noisy Bell states (Werner states)
mix the Bell state with completely random noise
$$
\rho=p\,|\Phi^+\rangle\langle\Phi^+|+(1-p)\,\frac I4
$$
the smallest eigenvalue of the partial transpose is $\frac{1-3p}4$, which goes negative once $p>\frac13$
![[Partial_transpose_Werner.png]]
so ==a Bell state survives as entangled until about 2/3 of it has been replaced by noise== ($p=\frac13$). useful for knowing when noisy pairs can still be used, eg. in [[Entanglement purification]] (which needs $F>\frac12$, the same point, since $F=\frac{1+3p}4$)

see also [[Quantum operations]], [[Defining entanglement]], [[Bell states]], [[Density matrix]]
