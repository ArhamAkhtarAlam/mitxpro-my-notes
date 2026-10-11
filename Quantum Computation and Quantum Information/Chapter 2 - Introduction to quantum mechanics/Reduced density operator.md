#textbook #partial_trace #density_matrix #entanglement #teleportation
*Quantum Computation and Quantum Information* §2.4.3 (p. 105–108). "perhaps the deepest use" of the density operator: describing **one part** of a bigger system. part of [[Quantum Computation and Quantum Information]], previous: [[General properties of the density operator]], course version: [[Partial trace]]
## the definition
for systems $A$ and $B$ in the state $\rho^{AB}$, the **reduced density operator** of $A$ is
$$
\rho^A\equiv\text{tr}_B(\rho^{AB})
$$
where the **partial trace** over $B$ is defined on product operators, and extended to everything by linearity
$$
\text{tr}_B\big(|a_1\rangle\langle a_2|\otimes|b_1\rangle\langle b_2|\big)\equiv|a_1\rangle\langle a_2|\ \text{tr}\big(|b_1\rangle\langle b_2|\big)=|a_1\rangle\langle a_2|\ \langle b_2|b_1\rangle
$$
^partial-trace-def

==keep $A$'s part, and replace $B$'s $|b_1\rangle\langle b_2|$ by the number $\langle b_2|b_1\rangle$==
## example 1: a product state
$\rho^{AB}=\rho\otimes\sigma$
$$
\rho^A=\text{tr}_B(\rho\otimes\sigma)=\rho\ \text{tr}(\sigma)=\rho\qquad\rho^B=\sigma
$$
what you'd expect: no correlations, so each part is just its own state
## example 2: a Bell state
$$
\begin{aligned}
\rho&=\Big(\tfrac{|00\rangle+|11\rangle}{\sqrt2}\Big)\Big(\tfrac{\langle00|+\langle11|}{\sqrt2}\Big)=\frac{|00\rangle\langle00|+|11\rangle\langle00|+|00\rangle\langle11|+|11\rangle\langle11|}2\\
\rho^1=\text{tr}_2(\rho)&=\frac{|0\rangle\langle0|\langle0|0\rangle+|1\rangle\langle0|\langle0|1\rangle+|0\rangle\langle1|\langle1|0\rangle+|1\rangle\langle1|\langle1|1\rangle}2\\
&=\frac{|0\rangle\langle0|+|1\rangle\langle1|}2=\frac I2
\end{aligned}
$$
$\text{tr}\big((\frac I2)^2\big)=\frac12<1$, so it's **mixed**
> [!important] the hallmark of entanglement
> ==the whole pair is pure (known **exactly**), but each qubit alone is mixed (we **don't** have full knowledge of it)==. a pure joint state with mixed parts is another sign of entanglement (see [[Pure state#pure states of 2 qubits]])

## why the partial trace? (Box 2.6)
it's the **only** choice that gives the right measurement results for the part
1. measuring an observable $M$ on $A$ alone is the same as measuring $\tilde M=M\otimes I_B$ on $AB$. (if $AB$ is in $|m\rangle|\psi\rangle$ with $|m\rangle$ an eigenstate of $M$, the device must give $m$ for sure, so the projectors are $P_m\otimes I_B$ and $\tilde M=\sum_mm\,P_m\otimes I_B=M\otimes I_B$)
2. so whatever "the state of $A$" is, it must give the same averages
$$
\text{tr}(M\rho^A)=\text{tr}\big((M\otimes I_B)\,\rho^{AB}\big)\quad\text{for every observable }M
$$
3. $\rho^A=\text{tr}_B(\rho^{AB})$ satisfies this. and it's **unique**: expand any such $f(\rho^{AB})$ in an orthonormal basis of Hermitian operators $M_i$ (with the inner product $\text{tr}(XY)$)
$$
f(\rho^{AB})=\sum_iM_i\,\text{tr}\big(M_if(\rho^{AB})\big)=\sum_iM_i\,\text{tr}\big((M_i\otimes I_B)\rho^{AB}\big)
$$
so $f$ is completely fixed by the condition, and the partial trace is the one function that does it
## teleportation can't send signals faster than light
just before Alice measures in [[Teleportation]], the 3 qubits are
$$
|\psi_2\rangle=\tfrac12\Big[|00\rangle(\alpha|0\rangle+\beta|1\rangle)+|01\rangle(\alpha|1\rangle+\beta|0\rangle)+|10\rangle(\alpha|0\rangle-\beta|1\rangle)+|11\rangle(\alpha|1\rangle-\beta|0\rangle)\Big]
$$
Alice gets each of $00,01,10,11$ with probability $\frac14$, leaving Bob with the matching state in brackets. **before Bob hears the result**, his state is the mixture of all 4
$$
\begin{aligned}
\rho^B&=\tfrac14\Big[(\alpha|0\rangle+\beta|1\rangle)(\alpha^*\langle0|+\beta^*\langle1|)+(\alpha|1\rangle+\beta|0\rangle)(\alpha^*\langle1|+\beta^*\langle0|)\\
&\qquad+(\alpha|0\rangle-\beta|1\rangle)(\alpha^*\langle0|-\beta^*\langle1|)+(\alpha|1\rangle-\beta|0\rangle)(\alpha^*\langle1|-\beta^*\langle0|)\Big]\\
&=\frac{2(|\alpha|^2+|\beta|^2)|0\rangle\langle0|+2(|\alpha|^2+|\beta|^2)|1\rangle\langle1|}4&&\text{(the cross terms cancel in pairs)}\\
&=\frac{|0\rangle\langle0|+|1\rangle\langle1|}2=\frac I2
\end{aligned}
$$
==Bob's state doesn't depend on $|\psi\rangle$ at all until the 2 classical bits arrive==, and those can't travel faster than light. so no faster than light signalling
> [!tip] exercises
> 2.74 (a product $|a\rangle|b\rangle$ has a pure reduced state) and 2.75 (the reduced states of all 4 Bell states) are worked in [[Chapter 2 exercises]]

next: [[Schmidt decomposition and purifications]]
