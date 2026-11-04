#textbook #quantum_error_correction #pauli #depolarizing
*Quantum Computation and Quantum Information* §10.3.1 (p. 438–441). why a code that fixes four Pauli errors fixes **every** error on that qubit. part of [[Quantum Computation and Quantum Information]], previous: [[Quantum error-correction conditions]], course version: [[Shor code#what about every other error?]]
## the problem
[[Quantum error-correction conditions|theorem 10.1]] protects against one specific noise process $\mathcal E$. but usually we **don't know** exactly what noise is hitting the system, so we want one code and one $\mathcal R$ that protects against a whole **class** of noise. the conditions give that almost for free
## theorem 10.2
let $C$ be a code and $\mathcal R$ the error-correction operation built in the proof of theorem 10.1 to recover from $\mathcal E$, with operation elements $\{E_i\}$. if $\mathcal F$ is a quantum operation whose elements $\{F_j\}$ are **linear combinations** of the $E_i$,
$$
F_j=\sum_im_{ji}E_i
$$
for some complex matrix $m_{ji}$, then ==the same $\mathcal R$ also corrects $\mathcal F$ on $C$==

**proof**: as in theorem 10.1 we can pick the $E_i$ so that $\alpha_{ij}=d_{ij}$ is diagonal and real. $\mathcal R$ has operation elements $U_k^\dagger P_k$, chosen so that for any $\rho$ in the code
$$
U_k^\dagger P_kE_i\sqrt\rho=\delta_{ki}\sqrt{d_{kk}}\sqrt\rho
$$
(from the proof of theorem 10.1: [[Quantum error-correction conditions#^qec-recovery]]). substitute $F_j=\sum_im_{ji}E_i$
$$
\begin{aligned}
U_k^\dagger P_kF_j\sqrt\rho&=\sum_im_{ji}\delta_{ki}\sqrt{d_{kk}}\sqrt\rho=m_{jk}\sqrt{d_{kk}}\sqrt\rho\\[4pt]
\mathcal R(\mathcal F(\rho))&=\sum_{kj}U_k^\dagger P_kF_j\rho F_j^\dagger P_kU_k\\
&=\sum_{kj}|m_{jk}|^2d_{kk}\,\rho\ \propto\ \rho
\end{aligned}
$$
as required ∎
## talking about error operators
so instead of "the noise processes $\mathcal E$ that a code corrects", talk about a set of **error operators** (or just **errors**) $\{E_i\}$ that are correctable, meaning
$$
PE_i^\dagger E_jP=\alpha_{ij}P
$$
theorems 10.1 and 10.2 together: ==any noise whose operation elements are built from linear combinations of correctable errors gets corrected by the same $\mathcal R$==

## why four Paulis are enough
any operation element on one qubit is a combination of the Pauli matrices $\sigma_0,\sigma_1,\sigma_2,\sigma_3$ ($I,X,Y,Z$). so to show the Shor code corrects **arbitrary** errors on qubit 1, it's enough to check
$$
P\sigma_i^1\sigma_j^1P=\alpha_{ij}P
$$
^pauli-conditions

where $\sigma_i^1$ is a Pauli on the first qubit (exercise 10.10, worked in [[Chapter 10 exercises#10.10 the Shor code satisfies the conditions]]). once that's done, **any** error process on qubit 1 can be corrected

> [!important] the one idea
> ==to fight the continuum of possible errors on a qubit, it's enough to win against a finite set: the four Paulis==. quantum errors can be **discretized**

this explains why so many papers use the [[Depolarizing channel]]
$$
\mathcal E(\rho)=(1-p)\rho+\tfrac p3(X\rho X+Y\rho Y+Z\rho Z)
$$
it looks like a very special noise model, but it isn't a limitation: correcting the depolarizing channel automatically means correcting **every** single qubit quantum operation, since its elements are $I,X,Y,Z$ and they span everything
## digital, not analog
this is very different from error correction for **analog** classical systems, which is extremely hard: there are infinitely many different error syndromes. digital classical error correction works far better because there are only finitely many. ==quantum error correction turns out to be much more like classical **digital** error correction than analog==, even though quantum states are continuous

> [!eg] a small rotation
> a rotation $R_z(\theta)=e^{-i\theta Z/2}$ on qubit 1 is
> $$
> R_z(\theta)=\cos\tfrac\theta2\,I-i\sin\tfrac\theta2\,Z
> $$
> a combination of $I$ and $Z_1$. the syndrome measurement finds "no error" with probability $\cos^2\frac\theta2$ and "$Z_1$" with probability $\sin^2\frac\theta2$, and either way the state comes back perfectly. for $\theta=\pi/263$ that's "$Z_1$" only $3.6\times10^{-5}$ of the time

> [!exercise] try these
> ① write the amplitude damping element $E_1=\begin{bmatrix}0&\sqrt\gamma\\0&0\end{bmatrix}$ as a combination of Paulis
> ② same for $E_0=\begin{bmatrix}1&0\\0&\sqrt{1-\gamma}\end{bmatrix}$
> ③ the projectors $|0\rangle\langle0|$ and $|1\rangle\langle1|$ on one qubit are errors too (exercise 10.9). why does the phase flip code correct them?

> [!answer]-
> ① $E_1=\sqrt\gamma\,\frac{X+iY}2$, since $\frac{X+iY}2=\frac12\Big(\begin{bmatrix}0&1\\1&0\end{bmatrix}+\begin{bmatrix}0&1\\-1&0\end{bmatrix}\Big)=\begin{bmatrix}0&1\\0&0\end{bmatrix}$
> ② $E_0=\frac{1+\sqrt{1-\gamma}}2I+\frac{1-\sqrt{1-\gamma}}2Z$
> ③ $|0\rangle\langle0|=\frac{I+Z}2$ and $|1\rangle\langle1|=\frac{I-Z}2$, combinations of $I$ and $Z$, which the phase flip code corrects. so by theorem 10.2 it corrects them too

see also [[Depolarizing channel]], [[Pauli channel]], [[Shor code]], maths: [[Pauli matrices]]

next: [[Independent error models]]
