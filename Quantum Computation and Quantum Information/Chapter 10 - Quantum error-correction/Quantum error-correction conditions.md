#textbook #quantum_error_correction #kraus_operators #quantum_operations
*Quantum Computation and Quantum Information* §10.3 and Box 10.1 (p. 435–439). a general theory: one equation that tells you whether a code can correct a given noise. part of [[Quantum Computation and Quantum Information]], previous: [[Shor nine qubit code]], course version: [[Operator-sum representation#why this matters for error correction]]
## the general picture
a **quantum error-correcting code** is a subspace $C$ of some larger Hilbert space, with projector $P$ onto it (for the bit flip code, $P=|000\rangle\langle000|+|111\rangle\langle111|$). states are encoded into $C$ by a unitary, noise acts, a **syndrome measurement** finds out what error happened, and a **recovery** operation puts the system back to its original state

> [!important] the one idea
> ==the different errors must take the code to **orthogonal**, **undeformed** copies of itself== (figure 10.5)
> - **orthogonal**, or the syndrome measurement can't reliably tell them apart
> - **undeformed**, ie. each error keeps orthogonal code words orthogonal, or the error can't be undone
>
> that picture is all the error-correction conditions say

![[Code_space_packing.png]]

on the left the images of $C$ overlap (can't tell the errors apart) and are squashed (can't undo them). on the right each error $E_k$ moves $C$ to its own separate, same-shaped copy

to assume as little as possible, there are only two assumptions
1. the noise is a quantum operation $\mathcal E$
2. the whole correction (detection **and** recovery in one) is a **trace-preserving** quantum operation $\mathcal R$, the **error-correction operation**

it succeeds if, for every state $\rho$ supported in $C$,
$$
(\mathcal R\circ\mathcal E)(\rho)\propto\rho
$$
^qec-success

why $\propto$ and not $=$? if $\mathcal E$ is trace preserving, taking the trace of both sides makes it $=$. but sometimes we want to correct non-trace-preserving $\mathcal E$, like a measurement. $\mathcal R$ has to succeed with probability 1, which is why it's trace preserving
## theorem 10.1: the error-correction conditions
let $C$ be a code with projector $P$, and $\mathcal E$ a quantum operation with operation elements $\{E_i\}$. an error-correction operation $\mathcal R$ correcting $\mathcal E$ on $C$ exists **if and only if**
$$
PE_i^\dagger E_jP=\alpha_{ij}P
$$
^qec-conditions

for some Hermitian matrix $\alpha$ of complex numbers. the $E_i$ are the **errors**, and if $\mathcal R$ exists, $\{E_i\}$ is a **correctable set of errors**

reading it: $i=j$ says every error shrinks every code word by the same factor $\alpha_{ii}$ (undeformed), and $i\neq j$ says the overlap between two errors' images is the same for every code word, so measuring it tells you nothing about the encoded state
## proof that it's enough
build $\mathcal R$ as detection followed by recovery, so this also shows that two stage procedure always works

**diagonalize** $\alpha$: it's Hermitian, so $d=u^\dagger\alpha u$ for a unitary $u$ and a diagonal $d$. define $F_k\equiv\sum_iu_{ik}E_i$. by theorem 8.2 (unitary freedom) $\{F_k\}$ is also a set of operation elements for $\mathcal E$, and
$$
\begin{aligned}
PF_k^\dagger F_lP&=\sum_{ij}u_{ki}^\dagger u_{jl}PE_i^\dagger E_jP\\
&=\sum_{ij}u_{ki}^\dagger\alpha_{ij}u_{jl}P\\
&=d_{kl}P
\end{aligned}
$$
^qec-diagonal

the same conditions, but now diagonal: different $F_k$ don't overlap at all on the code

**the syndrome measurement**: by the polar decomposition, $F_kP=U_k\sqrt{PF_k^\dagger F_kP}=\sqrt{d_{kk}}\,U_kP$ for some unitary $U_k$. so $F_k$ just **rotates** the code into the subspace with projector
$$
P_k\equiv U_kPU_k^\dagger=\frac{F_kPU_k^\dagger}{\sqrt{d_{kk}}}
$$
and these are orthogonal: for $k\neq l$
$$
P_lP_k=P_l^\dagger P_k=\frac{U_lPF_l^\dagger F_kPU_k^\dagger}{\sqrt{d_{ll}d_{kk}}}=0
$$
measure $\{P_k\}$ (plus one extra projector if needed so that $\sum_kP_k=I$)

**recovery**: apply $U_k^\dagger$. together, $\mathcal R(\sigma)=\sum_kU_k^\dagger P_k\sigma P_kU_k$. for $\rho$ in the code
$$
\begin{aligned}
U_k^\dagger P_kF_l\sqrt\rho&=U_k^\dagger P_k^\dagger F_lP\sqrt\rho\\
&=\frac{U_k^\dagger U_kPF_k^\dagger F_lP\sqrt\rho}{\sqrt{d_{kk}}}\\
&=\delta_{kl}\sqrt{d_{kk}}\,P\sqrt\rho=\delta_{kl}\sqrt{d_{kk}}\sqrt\rho\\[4pt]
\mathcal R(\mathcal E(\rho))&=\sum_{kl}U_k^\dagger P_kF_l\rho F_l^\dagger P_kU_k\\
&=\sum_{kl}\delta_{kl}d_{kk}\rho\ \propto\ \rho
\end{aligned}
$$
^qec-recovery

as required ∎
## proof that it's needed
suppose $\mathcal R$, with operation elements $\{R_j\}$, perfectly corrects $\{E_i\}$. define $\mathcal E_C(\rho)\equiv\mathcal E(P\rho P)$. $P\rho P$ is in the code for every $\rho$, so $\mathcal R(\mathcal E_C(\rho))=c\,P\rho P$, where $c$ can't depend on $\rho$ if both sides are linear. written out
$$
\sum_{ij}R_jE_iP\rho PE_i^\dagger R_j^\dagger=c\,P\rho P
$$
so the operation with elements $\{R_jE_i\}$ is the same as the one with the single element $\sqrt c\,P$. theorem 8.2 then says $R_kE_iP=c_{ki}P$ for some numbers $c_{ki}$. taking the adjoint, $PE_i^\dagger R_k^\dagger=c_{ki}^*P$, so $PE_i^\dagger R_k^\dagger R_kE_jP=c_{ki}^*c_{kj}P$. $\mathcal R$ is trace preserving, $\sum_kR_k^\dagger R_k=I$, so summing over $k$
$$
PE_i^\dagger E_jP=\alpha_{ij}P\qquad\alpha_{ij}\equiv\sum_kc_{ki}^*c_{kj}
$$
and $\alpha$ is Hermitian ∎

checking the conditions directly is easy but slow. §10.4 and §10.5 build codes (CSS, stabilizer) that satisfy them automatically

> [!eg] the bit flip code (exercise 10.7)
> errors $\{\sqrt{(1-p)^3}\,I,\ \sqrt{p(1-p)^2}\,X_1,\ \sqrt{p(1-p)^2}\,X_2,\ \sqrt{p(1-p)^2}\,X_3\}$ (2 and 3 flips left out, so it's not trace preserving). $PX_jP=0$ and $PX_jX_kP=0$, because each sends both code words outside the code. so $\alpha=\text{diag}\big((1-p)^3,\ p(1-p)^2,\ p(1-p)^2,\ p(1-p)^2\big)$ ✓. worked in [[Chapter 10 exercises#10.7 the error-correction conditions for the bit flip code]]
## Box 10.1: error correction without measurement
measurements are hard in some real systems, so it helps that correction can be done with **only unitaries and an ancilla**. say the syndrome measurement has measurement operators $M_i$ and the matching correction is $U_i$. add an ancilla with basis states $|i\rangle$, one per syndrome, starting in $|0\rangle$, and define
$$
U|\psi\rangle|0\rangle\equiv\sum_i(U_iM_i|\psi\rangle)|i\rangle
$$
this preserves inner products
$$
\begin{aligned}
\langle\varphi|\langle0|U^\dagger U|\psi\rangle|0\rangle&=\sum_{ij}\langle\varphi|M_i^\dagger U_i^\dagger U_jM_j|\psi\rangle\delta_{ij}\\
&=\sum_i\langle\varphi|M_i^\dagger M_i|\psi\rangle\\
&=\langle\varphi|\psi\rangle
\end{aligned}
$$
so it extends to a unitary on everything, and its effect on the system is $\mathcal R(\sigma)=\sum_iU_iM_i\sigma M_i^\dagger U_i^\dagger$: exactly the measure and correct operation. ==it needs a **fresh** ancilla every round==: the ancilla ends up holding the syndrome, ie. the error gets moved onto it

> [!exercise] try these
> ① show $\alpha$ is always Hermitian, straight from $PE_i^\dagger E_jP=\alpha_{ij}P$
> ② bit flip code, errors $\{I,X_1\}$. find $\alpha$
> ③ why can't the ancilla in Box 10.1 be reused without resetting it?

> [!answer]-
> ① take the adjoint: $(PE_i^\dagger E_jP)^\dagger=PE_j^\dagger E_iP=\alpha_{ji}P$, and also $=(\alpha_{ij}P)^\dagger=\alpha_{ij}^*P$. so $\alpha_{ji}=\alpha_{ij}^*$
> ② $PIP=P$, $PX_1^\dagger X_1P=P$, $PX_1P=0$: $\alpha=\begin{bmatrix}1&0\\0&1\end{bmatrix}$
> ③ $U$ is only defined to do the right thing on $|\psi\rangle|0\rangle$. after a round the ancilla is in some $|i\rangle$ (entangled with which error happened), so the next round would start from the wrong state. the error information has to be thrown away somewhere, and that's what resetting the ancilla does

see also [[Operator-sum representation]], [[Quantum operations]], [[Projectors]]

next: [[Discretization of the errors]]
