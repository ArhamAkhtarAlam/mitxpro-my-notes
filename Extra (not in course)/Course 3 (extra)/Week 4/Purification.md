#extra #purification #density_matrix #fidelity
**extra** (the course says "see standard textbooks"): every mixed state can be seen as **part of a bigger pure state**. used in the definition of [[State fidelity]]
## the idea
a purification of a mixed state $\rho$ (on system $A$) is a **pure** state $|\psi\rangle$ on $A$ + an extra helper system $R$, such that forgetting the helper gives back $\rho$
$$
\text{tr}_R\,|\psi\rangle\langle\psi|=\rho
$$
("forgetting" = the [[Partial trace]])
## how to build one
write $\rho$ in terms of its [[Eigenvalues and eigenvectors|eigenvalues]] $\lambda_i$ and eigenvectors $|i\rangle$
$$
\rho=\sum_i\lambda_i|i\rangle\langle i|\qquad\Rightarrow\qquad|\psi\rangle=\sum_i\sqrt{\lambda_i}\,|i\rangle_A|i\rangle_R
$$
> [!example] $\rho=\begin{bmatrix}0.75&0\\0&0.25\end{bmatrix}$
> $$
> |\psi\rangle=\sqrt{0.75}\,|00\rangle+\sqrt{0.25}\,|11\rangle
> $$
> tracing out the second qubit gives back $\rho$ exactly (checked numerically). and for the fully mixed $\frac I2$ you get a [[Bell states|Bell state]]

this is just the [[Schmidt decomposition]] run backwards: the Schmidt coefficients squared are the eigenvalues of $\rho$
```mermaid
flowchart LR
    M["mixed state ρ"] -- "add a helper,<br/>entangle it" --> P["pure state ψ<br/>(system + helper)"]
    P -- "partial trace:<br/>forget the helper" --> M
```
## not unique
any unitary $U$ on the helper alone gives another valid purification, $(I\otimes U)|\psi\rangle$, since the helper gets thrown away anyway. **all** purifications of the same $\rho$ are related like this
## why it's useful
- **fidelity** (Uhlmann's theorem): the fidelity of 2 states is the **best overlap** between their purifications, which gives $\sqrt{\langle\phi|\rho|\phi\rangle}$ when one state is pure ([[State fidelity#the purification trick]])
- **noise**: any noisy process can be pictured as the system becoming entangled with an environment, a purification of what you see
- the slogan: "the church of the larger Hilbert space". if a mixed state is awkward, make it pure in a bigger space ([[Hilbert space]])

see also [[Partial trace]], [[State fidelity]], [[Schmidt decomposition]], [[Density matrix]]
