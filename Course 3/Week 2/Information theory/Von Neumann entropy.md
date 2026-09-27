#entropy #von_neumann_entropy #information_theory #density_matrix
the quantum version of [[Shannon entropy]]
## what it is
$S(\rho)$ = the number of **qubits** you need to faithfully represent a [[Density matrix]] $\rho$ (asymptotically, so on average over lots of copies)
$$
S(\rho)=-\text{tr}(\rho\log_2\rho)=-\sum_k\lambda_k\log_2\lambda_k
$$
$\lambda_k$ are the **[[Eigenvalues and eigenvectors|eigenvalues]]** of $\rho$ (the spectral unravelling from [[Density matrix#unraveling (going the other way)]])

so it's just the Shannon entropy of the eigenvalues
## examples
| state                                                                     | eigenvalues       | $S(\rho)$     |
| ------------------------------------------------------------------------- | ----------------- | ------------- |
| any pure state $\lvert\psi\rangle\langle\psi\rvert$                       | $1,0$             | $0$           |
| fully mixed $\frac I2$ (middle of the [[Bloch sphere]])                   | $\frac12,\frac12$ | $1$           |
| $\frac34\lvert0\rangle\langle0\rvert+\frac14\lvert1\rangle\langle1\rvert$ | $\frac34,\frac14$ | $\approx0.81$ |

pure = no uncertainty = 0, fully mixed = most uncertain = 1 qubit
## similar but different from Shannon
> [!important] non-orthogonal states
> if you mix states that are **orthogonal** (like $|0\rangle$ and $|1\rangle$) then $S(\rho)$ = the Shannon entropy of the probabilities
>
> but if they're **not orthogonal** then $S(\rho)$ is **smaller** than the Shannon entropy

eg. send $|0\rangle$ or $|+\rangle$ with a 50/50 coin flip
- Shannon entropy of the coin flip = $1$ bit
- but the eigenvalues of $\rho=\frac12|0\rangle\langle0|+\frac12|+\rangle\langle+|$ are $\approx0.85$ and $0.15$
- so $S(\rho)\approx0.60$ qubits

you need fewer than 1 qubit per message because $|0\rangle$ and $|+\rangle$ overlap, they're partly "the same"

![[Shannon_vs_von_Neumann.png]]

see also [[Channel capacity]]


