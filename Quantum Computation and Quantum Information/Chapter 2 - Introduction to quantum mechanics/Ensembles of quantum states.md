#textbook #density_matrix #mixed_state #measurement
*Quantum Computation and Quantum Information* §2.4.1 (p. 98–101). the density operator is a different language for quantum mechanics: it says **exactly the same things** as state vectors, but it's much easier when you **don't know the state completely**. part of [[Quantum Computation and Quantum Information]], course version: [[Density matrix]]
## the definition
the system is in one of the pure states $|\psi_i\rangle$, with probability $p_i$. the set $\{p_i,|\psi_i\rangle\}$ is called an **ensemble of pure states**, and its density operator (or density matrix, the book uses both) is
$$
\rho\equiv\sum_ip_i\,|\psi_i\rangle\langle\psi_i|
$$
^ensemble-rho

## evolution
if the state was $|\psi_i\rangle$ with probability $p_i$, after a unitary $U$ it's $U|\psi_i\rangle$ with the same probability $p_i$. so
$$
\rho=\sum_ip_i|\psi_i\rangle\langle\psi_i|\ \xrightarrow{\ U\ }\ \sum_ip_i\,U|\psi_i\rangle\langle\psi_i|U^\dagger=U\rho\,U^\dagger
$$
## measurement
a measurement has operators $M_m$ (one per result $m$). work it out for one $|\psi_i\rangle$ first, then average over $i$ (law of total probability)
$$
\begin{aligned}
p(m|i)&=\langle\psi_i|M_m^\dagger M_m|\psi_i\rangle=\text{tr}\big(M_m^\dagger M_m|\psi_i\rangle\langle\psi_i|\big)&&\text{(using }\langle a|B|a\rangle=\text{tr}(B|a\rangle\langle a|))\\
p(m)&=\sum_ip(m|i)\,p_i=\sum_ip_i\,\text{tr}\big(M_m^\dagger M_m|\psi_i\rangle\langle\psi_i|\big)\\
&=\text{tr}\big(M_m^\dagger M_m\,\rho\big)
\end{aligned}
$$
==the chance of result $m$ is $\text{tr}(M_m^\dagger M_m\rho)$==. for a projective measurement $M_m=\Pi_m$, this is $\text{tr}(\Pi_m\rho)$, the mixed state version of $|\langle m|\psi\rangle|^2$

**the state afterwards**: each $|\psi_i\rangle$ becomes $\frac{M_m|\psi_i\rangle}{\sqrt{p(m|i)}}$, with the new probabilities $p(i|m)=\frac{p(m|i)\,p_i}{p(m)}$ (Bayes). putting it together
$$
\begin{aligned}
\rho_m&=\sum_ip(i|m)\,\frac{M_m|\psi_i\rangle\langle\psi_i|M_m^\dagger}{p(m|i)}=\sum_ip_i\,\frac{M_m|\psi_i\rangle\langle\psi_i|M_m^\dagger}{\text{tr}(M_m^\dagger M_m\rho)}\\
&=\frac{M_m\,\rho\,M_m^\dagger}{\text{tr}(M_m^\dagger M_m\rho)}
\end{aligned}
$$
> [!example] measuring $\rho=\frac14\begin{bmatrix}3&0\\0&1\end{bmatrix}$ in $0/1$
> $M_0=|0\rangle\langle0|$: $p(0)=\text{tr}(|0\rangle\langle0|\rho)=\frac34$, and afterwards $\rho_0=\frac{|0\rangle\langle0|\rho|0\rangle\langle0|}{3/4}=|0\rangle\langle0|$

## pure and mixed
- **pure state**: you know the state exactly, $\rho=|\psi\rangle\langle\psi|$ ([[Pure state]])
- **mixed state**: anything else, a **mixture** of the pure states in the ensemble
- the test: ==pure ⟺ $\text{tr}(\rho^2)=1$, mixed ⟺ $\text{tr}(\rho^2)<1$== (proved in [[Chapter 2 exercises#2.71 pure or mixed]])

> [!warning] 2 naming traps
> - some people say "mixed state" to mean **any** state (pure or not), just so they're not assuming it's pure
> - "pure state" is often used for the **state vector** $|\psi\rangle$ itself, to tell it apart from a density operator

## mixtures of mixtures
if the system is in the (maybe mixed) state $\rho_i$ with probability $p_i$, the total state is just
$$
\begin{aligned}
\rho&=\sum_{ij}p_ip_{ij}\,|\psi_{ij}\rangle\langle\psi_{ij}|&&\text{(each }\rho_i=\textstyle\sum_jp_{ij}|\psi_{ij}\rangle\langle\psi_{ij}|)\\
&=\sum_ip_i\,\rho_i
\end{aligned}
$$
this is how **noise** works: it adds ignorance about the state
## forgetting a measurement result
measure, but **lose the record** of which $m$ you got. then you have $\rho_m$ with probability $p(m)$
$$
\begin{aligned}
\rho&=\sum_mp(m)\,\rho_m=\sum_m\text{tr}(M_m^\dagger M_m\rho)\,\frac{M_m\rho M_m^\dagger}{\text{tr}(M_m^\dagger M_m\rho)}\\
&=\sum_mM_m\,\rho\,M_m^\dagger
\end{aligned}
$$
^forget-result

a compact formula that's the starting point for [[Operator-sum representation|quantum operations]] later
> [!example] measure $|+\rangle$ in $0/1$ and forget
> $$
> |0\rangle\langle0|\Big(\tfrac12\begin{bmatrix}1&1\\1&1\end{bmatrix}\Big)|0\rangle\langle0|+|1\rangle\langle1|\Big(\tfrac12\begin{bmatrix}1&1\\1&1\end{bmatrix}\Big)|1\rangle\langle1|=\frac12\begin{bmatrix}1&0\\0&1\end{bmatrix}=\frac I2
> $$
> the off diagonals are wiped out: a pure state became completely mixed. that's exactly the [[Dephasing channel]] at $p=\frac12$

next: [[General properties of the density operator]]
