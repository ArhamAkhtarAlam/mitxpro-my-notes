#extra #partial_trace #density_matrix #trace
**extra** (not in the course): how to "forget" part of a system. gives you the [[Density matrix|density matrix]] of just the piece you care about
## the idea
you have 2 systems $A$ and $B$ in a joint state $\rho_{AB}$, but you can only see $A$. the **partial trace** over $B$ gives what $A$ looks like on its own
$$
\rho_A=\text{tr}_B\big(\rho_{AB}\big)
$$
^partial-trace

the rule: it acts like the normal [[Trace|trace]], but only on $B$'s part
$$
\text{tr}_B\big(|a\rangle\langle a'|\otimes|b\rangle\langle b'|\big)=|a\rangle\langle a'|\,\langle b'|b\rangle
$$
## the easy way (2 qubits)
write the $4\times4$ matrix $\rho_{AB}$ as four $2\times2$ blocks, then take the **trace of each block**
$$
\rho_{AB}=\begin{bmatrix}P&Q\\R&S\end{bmatrix}\quad\Rightarrow\quad\rho_A=\begin{bmatrix}\text{tr}P&\text{tr}Q\\\text{tr}R&\text{tr}S\end{bmatrix}
$$
(this uses the ordering $|00\rangle,|01\rangle,|10\rangle,|11\rangle$ with $A$ first, see [[Tensor product]])
## examples
> [!example] a product state: $|+\rangle|0\rangle$
> $$
> \rho_A=\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}=|+\rangle\langle+|
> $$
> still pure. forgetting a system that was never connected to $A$ doesn't change anything

> [!example] a Bell state: $\frac1{\sqrt2}(|00\rangle+|11\rangle)$
> $$
> \rho_A=\frac12\begin{bmatrix}1&0\\0&1\end{bmatrix}=\frac I2
> $$
> **completely mixed**, even though the whole pair is pure. that's entanglement: the information is in the **correlations**, not in either half (see [[Entanglement entropy]])

(both checked numerically)
## why it matters
- it's how noise enters: a qubit that gets entangled with its environment looks **mixed** once you trace out the environment ([[Noise Processes]], [[Quantum channels]])
- the mixedness of $\rho_A$ measures entanglement ([[Entanglement entropy]], [[Schmidt decomposition]])
- running it backwards (finding a pure state whose partial trace is $\rho$) is a [[Purification]]

see also [[Purification]], [[Density matrix]], [[Trace]], [[Entanglement entropy]]
