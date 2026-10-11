#formula_sheet #textbook #density_matrix #entanglement
every formula from chapter 2 (p. 98–115) of *Quantum Computation and Quantum Information* in one place, with an **eg.** under each formula showing how it's used, and a worked **example** and **exercises** per section (answers fold out, try them first). each section links to the note with the full explanation. part of [[Quantum Computation and Quantum Information]]
## 1. the Bell basis
from [[Chapter 2 exercises#2.69 the Bell basis is orthonormal]] and [[Superdense coding]]. the bits in front are what Alice sends in superdense coding
$$
00:\ |\Phi^+\rangle=\tfrac{|00\rangle+|11\rangle}{\sqrt2}\quad01:\ |\Phi^-\rangle=\tfrac{|00\rangle-|11\rangle}{\sqrt2}\quad10:\ |\Psi^+\rangle=\tfrac{|10\rangle+|01\rangle}{\sqrt2}\quad11:\ |\Psi^-\rangle=\tfrac{|01\rangle-|10\rangle}{\sqrt2}
$$
> [!example] eg. making them: $H$ on the first qubit, then a CNOT
> $$
> \begin{aligned}
> |00\rangle&\xrightarrow{H}\tfrac{(|0\rangle+|1\rangle)|0\rangle}{\sqrt2}\xrightarrow{\text{CNOT}}\tfrac{|00\rangle+|11\rangle}{\sqrt2}=|\Phi^+\rangle\\
> |10\rangle&\xrightarrow{H}\tfrac{(|0\rangle-|1\rangle)|0\rangle}{\sqrt2}\xrightarrow{\text{CNOT}}\tfrac{|00\rangle-|11\rangle}{\sqrt2}=|\Phi^-\rangle
> \end{aligned}
> $$
> and $|01\rangle\to|\Psi^+\rangle$, $|11\rangle\to|\Psi^-\rangle$. run it backwards (CNOT then $H$) and you **measure** in the Bell basis

> [!example] example: Bell states in the $+/-$ basis
> $$
> |\Phi^+\rangle=\frac{|{+}{+}\rangle+|{-}{-}\rangle}{\sqrt2}\qquad|\Phi^-\rangle=\frac{|{+}{-}\rangle+|{-}{+}\rangle}{\sqrt2}
> $$
> both always match in $0/1$, but in $+/-$ the first matches and the second is opposite. the only difference is the relative phase

> [!question] exercise: which Bell state do you get?
> start from $|\Phi^+\rangle$ and apply (a) $Z\otimes I$ (b) $X\otimes I$ (c) $XZ\otimes I$

> [!success]- answer
> (a) $Z$ flips the sign of $|1\rangle$: $\frac{|00\rangle-|11\rangle}{\sqrt2}=|\Phi^-\rangle$
> (b) $X$ flips the first bit: $\frac{|10\rangle+|01\rangle}{\sqrt2}=|\Psi^+\rangle$
> (c) $Z$ first, then $X$: $\frac{|10\rangle-|01\rangle}{\sqrt2}=-|\Psi^-\rangle$, the same as $|\Psi^-\rangle$ up to a global phase. that's superdense coding: Alice's 4 choices $I,Z,X,XZ$ give the 4 Bell states

## 2. ensembles and the density operator
from [[Ensembles of quantum states]]

**the definition** (state $|\psi_i\rangle$ with probability $p_i$)
$$
\rho=\sum_ip_i\,|\psi_i\rangle\langle\psi_i|\qquad\qquad\text{pure: }\rho=|\psi\rangle\langle\psi|
$$
> [!example] eg. a machine makes $|0\rangle$ 70% of the time and $|1\rangle$ 30%
> $$
> \rho=0.7\,|0\rangle\langle0|+0.3\,|1\rangle\langle1|=\begin{bmatrix}0.7&0\\0&0.3\end{bmatrix}
> $$
> compare the **pure** $\sqrt{0.7}|0\rangle+\sqrt{0.3}|1\rangle$: $\rho=\begin{bmatrix}0.7&0.458\\0.458&0.3\end{bmatrix}$. same diagonal, but it has off diagonals

**evolution**
$$
\rho\ \xrightarrow{\ U\ }\ U\rho\,U^\dagger
$$
> [!example] eg. a Hadamard on $|0\rangle\langle0|$, and on a coin flip
> $$
> H\begin{bmatrix}1&0\\0&0\end{bmatrix}H=\frac12\begin{bmatrix}1&1\\1&-1\end{bmatrix}\begin{bmatrix}1&0\\0&0\end{bmatrix}\begin{bmatrix}1&1\\1&-1\end{bmatrix}=\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}=|+\rangle\langle+|\qquad H\tfrac I2H=\tfrac I2
> $$
> you multiply on **both** sides (a ket gets $U$, a bra gets $U^\dagger$). a complete coin flip stays a coin flip whatever gate you use

**measurement** with operators $M_m$
$$
\begin{aligned}
p(m)&=\text{tr}(M_m^\dagger M_m\,\rho)&&\text{(for projectors: }\text{tr}(\Pi_m\rho))\\
\rho_m&=\frac{M_m\,\rho\,M_m^\dagger}{\text{tr}(M_m^\dagger M_m\,\rho)}&&\text{(the state after getting }m)\\
\sum_mM_m^\dagger M_m&=I&&\text{(completeness)}
\end{aligned}
$$
> [!info] what $M_m$ means
> a measurement is a list of matrices, **one for each possible result** $m$. $M_m$ is what happens to the state if you get result $m$: the state becomes $M_m|\psi\rangle$ (then normalise). the chance is the squared length of that, $\langle\psi|M_m^\dagger M_m|\psi\rangle$, which is where the $M_m^\dagger M_m$ comes from. completeness just says the chances add to 1

> [!example] eg. 1: an ordinary measurement in $0/1$ on $|+\rangle$
> $M_0=|0\rangle\langle0|=\begin{bmatrix}1&0\\0&0\end{bmatrix}$, $M_1=|1\rangle\langle1|=\begin{bmatrix}0&0\\0&1\end{bmatrix}$, $\rho=\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}$
> $$
> \begin{aligned}
> M_0^\dagger M_0+M_1^\dagger M_1&=\begin{bmatrix}1&0\\0&0\end{bmatrix}+\begin{bmatrix}0&0\\0&1\end{bmatrix}=I\ ✅\\
> p(0)&=\text{tr}(M_0^\dagger M_0\rho)=\text{tr}\begin{bmatrix}\frac12&\frac12\\0&0\end{bmatrix}=\tfrac12\\
> \rho_0&=\frac{M_0\rho M_0^\dagger}{p(0)}=\frac{\frac12\begin{bmatrix}1&0\\0&0\end{bmatrix}}{\frac12}=|0\rangle\langle0|
> \end{aligned}
> $$
> here $M_m^\dagger M_m=M_m$ (projectors), so this is just the [[Projectors|projector]] rule

> [!example] eg. 2: a gentle measurement, where $M_m$ is NOT a projector
> $M_0=\begin{bmatrix}1&0\\0&\sqrt{0.5}\end{bmatrix}$, $M_1=\begin{bmatrix}0&0\\0&\sqrt{0.5}\end{bmatrix}$ (a detector that only clicks on $|1\rangle$, half the time). on $\rho=|+\rangle\langle+|$
> $$
> \begin{aligned}
> M_0^\dagger M_0+M_1^\dagger M_1&=\begin{bmatrix}1&0\\0&0.5\end{bmatrix}+\begin{bmatrix}0&0\\0&0.5\end{bmatrix}=I\ ✅\\
> p(1)&=\text{tr}\Big(\begin{bmatrix}0&0\\0&0.5\end{bmatrix}\tfrac12\begin{bmatrix}1&1\\1&1\end{bmatrix}\Big)=\tfrac12\cdot0.5=0.25&&\rho_1=|1\rangle\langle1|\ \text{(it clicked, so it was 1)}\\
> p(0)&=1-0.25=0.75&&\rho_0=\frac{M_0\rho M_0^\dagger}{0.75}=\begin{bmatrix}\frac23&0.471\\0.471&\frac13\end{bmatrix}
> \end{aligned}
> $$
> no click doesn't collapse it to $|0\rangle$, it just **nudges** it towards $|0\rangle$: $|+\rangle\to\sqrt{\frac23}|0\rangle+\sqrt{\frac13}|1\rangle$ (still pure). that's why you need $M_m^\dagger M_m$ and not just $M_m$ (checked numerically)

**mixtures, and forgetting the result**
$$
\rho=\sum_ip_i\,\rho_i\qquad\qquad\rho\ \to\ \sum_mM_m\,\rho\,M_m^\dagger
$$
> [!example] eg. mixing, and forgetting the gentle measurement
> **mixing**: half $|0\rangle\langle0|$, half $\frac I2$
> $$
> \tfrac12\begin{bmatrix}1&0\\0&0\end{bmatrix}+\tfrac12\begin{bmatrix}\frac12&0\\0&\frac12\end{bmatrix}=\begin{bmatrix}\frac34&0\\0&\frac14\end{bmatrix}
> $$
> **forgetting**: do eg. 2 above but lose the result
> $$
> M_0\rho M_0^\dagger+M_1\rho M_1^\dagger=\begin{bmatrix}0.5&0.354\\0.354&0.25\end{bmatrix}+\begin{bmatrix}0&0\\0&0.25\end{bmatrix}=\begin{bmatrix}0.5&0.354\\0.354&0.5\end{bmatrix}
> $$
> no $\div p(m)$ here: you add up the **unnormalised** results. purity drops from 1 to $0.75$

> [!example] example: half $|0\rangle$, half $|+\rangle$
> $$
> \begin{aligned}
> \rho&=\tfrac12\begin{bmatrix}1&0\\0&0\end{bmatrix}+\tfrac12\cdot\tfrac12\begin{bmatrix}1&1\\1&1\end{bmatrix}=\begin{bmatrix}\frac34&\frac14\\\frac14&\frac14\end{bmatrix}\\
> p(0)&=\text{tr}(|0\rangle\langle0|\rho)=\tfrac34\qquad\text{then }\rho_0=|0\rangle\langle0|\\
> \text{tr}(\rho^2)&=\tfrac9{16}+\tfrac1{16}+2\cdot\tfrac1{16}=\tfrac34<1\ \text{ (mixed)}
> \end{aligned}
> $$

> [!question] exercise: evolve it, then forget a measurement
> with the same $\rho$: (a) find $X\rho X$ (b) measure in $0/1$ and forget the result, what's $\sum_mM_m\rho M_m^\dagger$?

> [!success]- answer
> (a) $X$ swaps $0\leftrightarrow1$ in both the rows and the columns: $X\rho X=\begin{bmatrix}\frac14&\frac14\\\frac14&\frac34\end{bmatrix}$ (now half $|1\rangle$, half $|+\rangle$)
> (b) $|0\rangle\langle0|\rho|0\rangle\langle0|+|1\rangle\langle1|\rho|1\rangle\langle1|$ keeps only the diagonal: $\begin{bmatrix}\frac34&0\\0&\frac14\end{bmatrix}$. the coherence is gone, purity drops from $0.75$ to $0.625$

## 3. what a density operator is
from [[General properties of the density operator]]

**theorem 2.5**: $\rho$ is a density operator ⟺
$$
\text{tr}(\rho)=1\qquad\text{and}\qquad\langle\varphi|\rho|\varphi\rangle\geq0\ \text{ for all }|\varphi\rangle
$$
> [!example] eg. checking $\rho=\begin{bmatrix}\frac34&\frac14\\\frac14&\frac14\end{bmatrix}$
> trace $\frac34+\frac14=1$ ✅. positivity: you can't try every $|\varphi\rangle$, so check the **eigenvalues** are $\geq0$ (same thing). here they're $0.854$ and $0.146$ ✅. eg. with $|\varphi\rangle=|-\rangle$: $\langle-|\rho|-\rangle=\frac12\big(\frac34-\frac14-\frac14+\frac14\big)=\frac14\geq0$

**pure or mixed**
$$
\text{tr}(\rho^2)=\sum_i\lambda_i^2\leq1\qquad\begin{cases}=1&\text{pure}\\<1&\text{mixed}\end{cases}
$$
> [!example] eg. the same $\rho$
> $0.854^2+0.146^2=0.729+0.021=0.75<1$, mixed. (squaring the matrix and taking the trace gives the same $0.75$)

**theorem 2.6, unitary freedom**: 2 ensembles give the same $\rho$ ⟺
$$
\sqrt{p_i}\,|\psi_i\rangle=\sum_ju_{ij}\sqrt{q_j}\,|\varphi_j\rangle\qquad(u\text{ unitary})
$$
> [!example] eg. the book's 2 recipes for $\frac34|0\rangle\langle0|+\frac14|1\rangle\langle1|$
> recipe 1: $|0\rangle$ (prob $\frac34$), $|1\rangle$ (prob $\frac14$). recipe 2: $|a\rangle,|b\rangle=\sqrt{\frac34}|0\rangle\pm\sqrt{\frac14}|1\rangle$ (prob $\frac12$ each)
> $$
> \sqrt{\tfrac12}\,|a\rangle=\tfrac1{\sqrt2}\Big(\sqrt{\tfrac34}|0\rangle\Big)+\tfrac1{\sqrt2}\Big(\sqrt{\tfrac14}|1\rangle\Big)\qquad\sqrt{\tfrac12}\,|b\rangle=\tfrac1{\sqrt2}\Big(\sqrt{\tfrac34}|0\rangle\Big)-\tfrac1{\sqrt2}\Big(\sqrt{\tfrac14}|1\rangle\Big)
> $$
> the numbers $\frac1{\sqrt2},\pm\frac1{\sqrt2}$ form $u=H$, a unitary, so both recipes give the same $\rho$

**the Bloch vector** for 1 qubit
$$
\begin{aligned}
\rho&=\frac{I+\vec r\cdot\vec\sigma}2=\frac12\begin{bmatrix}1+r_z&r_x-ir_y\\r_x+ir_y&1-r_z\end{bmatrix}\qquad\|\vec r\|\leq1\\
\text{eigenvalues}&=\frac{1\pm\|\vec r\|}2\qquad\text{tr}(\rho^2)=\frac{1+\|\vec r\|^2}2\\
\text{pure}:\ \vec r&=(\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta)
\end{aligned}
$$
**minimal ensemble**: $|\psi\rangle$ has to appear with probability
$$
p=\frac1{\langle\psi|\rho^{-1}|\psi\rangle}
$$
> [!example] eg. can $|+\rangle$ be part of a 2 state recipe for $\rho=\begin{bmatrix}\frac34&0\\0&\frac14\end{bmatrix}$?
> $$
> \begin{aligned}
> \rho^{-1}&=\begin{bmatrix}\frac43&0\\0&4\end{bmatrix}\qquad\langle+|\rho^{-1}|+\rangle=\tfrac12\big(\tfrac43+4\big)=\tfrac83\qquad p=\tfrac38\\
> \rho-\tfrac38|+\rangle\langle+|&=\begin{bmatrix}\frac9{16}&-\frac3{16}\\-\frac3{16}&\frac1{16}\end{bmatrix}=\tfrac58\,|\chi\rangle\langle\chi|\qquad|\chi\rangle=\tfrac{3|0\rangle-|1\rangle}{\sqrt{10}}
> \end{aligned}
> $$
> so $\rho=\frac38|+\rangle\langle+|+\frac58|\chi\rangle\langle\chi|$: yes, and $|+\rangle$ **has** to come with probability $\frac38$

> [!example] example: the Bloch vector of $\rho=\begin{bmatrix}\frac34&\frac14\\\frac14&\frac14\end{bmatrix}$
> match it to $\frac12\begin{bmatrix}1+r_z&r_x-ir_y\\r_x+ir_y&1-r_z\end{bmatrix}$: $r_z=\frac34-\frac14=\frac12$, $r_x=2\cdot\frac14=\frac12$, $r_y=0$
> $$
> \|\vec r\|=\tfrac1{\sqrt2}\approx0.707\qquad\text{eigenvalues }\tfrac{1\pm0.707}2=0.854,\ 0.146\qquad\text{tr}(\rho^2)=\tfrac{1+0.5}2=0.75\ ✅
> $$
> inside the ball, halfway between $|0\rangle$ (north pole) and $|+\rangle$ ($+x$), as you'd expect for a 50/50 mix of them

> [!question] exercise: is it a density matrix?
> (a) $\begin{bmatrix}0.5&0.6\\0.6&0.5\end{bmatrix}$ (b) $\frac12\begin{bmatrix}1&-\frac i2\\\frac i2&1\end{bmatrix}$: if yes, find $\vec r$ and say if it's pure

> [!success]- answer
> (a) trace 1, but the eigenvalues are $0.5\pm0.6=1.1$ and $-0.1$. a negative eigenvalue breaks positivity, so **no** (it would give a "probability" of $-0.1$). equivalently $\|\vec r\|=1.2>1$
> (b) yes: $\frac{r_x-ir_y}2=-\frac i4$ gives $r_y=\frac12$, $r_x=r_z=0$. $\|\vec r\|=\frac12<1$, so **mixed**, with $\text{tr}(\rho^2)=\frac{1+0.25}2=0.625$

> [!question] exercise: unitary freedom
> show that $\{\frac12,|+\rangle\},\{\frac12,|-\rangle\}$ gives the same $\rho$ as $\{\frac12,|0\rangle\},\{\frac12,|1\rangle\}$, and find the unitary $u$

> [!success]- answer
> $\frac12|+\rangle\langle+|+\frac12|-\rangle\langle-|=\frac14\begin{bmatrix}1&1\\1&1\end{bmatrix}+\frac14\begin{bmatrix}1&-1\\-1&1\end{bmatrix}=\frac I2$, the same as $\frac12|0\rangle\langle0|+\frac12|1\rangle\langle1|$. with $|\tilde\psi\rangle=\frac1{\sqrt2}|\pm\rangle$ and $|\tilde\varphi\rangle=\frac1{\sqrt2}|0\rangle,\frac1{\sqrt2}|1\rangle$: $|\tilde\psi_\pm\rangle=\frac1{\sqrt2}(|\tilde\varphi_0\rangle\pm|\tilde\varphi_1\rangle)$, so $u=H$

## 4. the reduced density operator
from [[Reduced density operator]]
$$
\begin{aligned}
\rho^A&=\text{tr}_B(\rho^{AB})\\
\text{tr}_B\big(|a_1\rangle\langle a_2|\otimes|b_1\rangle\langle b_2|\big)&=|a_1\rangle\langle a_2|\,\langle b_2|b_1\rangle\\
\text{tr}_B(\rho\otimes\sigma)&=\rho\\
\text{tr}(M\rho^A)&=\text{tr}\big((M\otimes I_B)\,\rho^{AB}\big)&&\text{(why it's the right definition)}
\end{aligned}
$$
> [!example] eg. each line
> - **the rule**: $\text{tr}_B\big(|0\rangle\langle1|\otimes|1\rangle\langle1|\big)=|0\rangle\langle1|\,\langle1|1\rangle=|0\rangle\langle1|$, but $\text{tr}_B\big(|0\rangle\langle1|\otimes|1\rangle\langle0|\big)=|0\rangle\langle1|\,\langle0|1\rangle=0$. B's ket and bra have to **match** to survive
> - **a product**: $\text{tr}_B\big(|+\rangle\langle+|\otimes\frac I2\big)=|+\rangle\langle+|\cdot\text{tr}\frac I2=|+\rangle\langle+|$
> - **the measurement check**: Bell state, $M=|0\rangle\langle0|$ on A. the whole pair: $\langle\Phi^+|\,(|0\rangle\langle0|\otimes I)\,|\Phi^+\rangle=\frac12$. using $\rho^A=\frac I2$: $\text{tr}\big(|0\rangle\langle0|\frac I2\big)=\frac12$ ✅ the same

**examples**
$$
\text{Bell state}:\ \rho^A=\frac I2\qquad\qquad\text{Bob in teleportation, before the bits arrive}:\ \rho^B=\frac I2
$$
> [!example] example: $|\psi\rangle=\sqrt{\frac34}|00\rangle+\sqrt{\frac14}|11\rangle$
> $$
> \rho^A=\tfrac34|0\rangle\langle0|\,\langle0|0\rangle+\tfrac{\sqrt3}4|0\rangle\langle1|\,\langle1|0\rangle+\tfrac{\sqrt3}4|1\rangle\langle0|\,\langle0|1\rangle+\tfrac14|1\rangle\langle1|\,\langle1|1\rangle=\begin{bmatrix}\frac34&0\\0&\frac14\end{bmatrix}
> $$
> the cross terms die because $B$'s bits differ. purity $0.625$, so the pair is entangled

> [!question] exercise: find $\rho^A$ and $\rho^B$
> (a) $\frac{|00\rangle+|01\rangle}{\sqrt2}$ (b) $\frac{|00\rangle+|01\rangle+|11\rangle}{\sqrt3}$

> [!success]- answer
> (a) it's $|0\rangle\otimes|+\rangle$, a product, so $\rho^A=|0\rangle\langle0|$ and $\rho^B=|+\rangle\langle+|$. both pure, not entangled
> (b) $\rho^A=\frac13\begin{bmatrix}2&1\\1&1\end{bmatrix}$ and $\rho^B=\frac13\begin{bmatrix}1&1\\1&2\end{bmatrix}$. different matrices, but both have $\text{tr}(\rho^2)=\frac79$ and eigenvalues $0.873,\ 0.127$ (Schmidt)

## 5. Schmidt decomposition and purification
from [[Schmidt decomposition and purifications]]

**any pure 2 part state**
$$
|\psi\rangle=\sum_i\lambda_i\,|i_A\rangle|i_B\rangle\qquad\lambda_i\geq0,\quad\sum_i\lambda_i^2=1
$$
> [!example] eg. already in Schmidt form
> $\sqrt{0.8}|00\rangle+\sqrt{0.2}|11\rangle$: $\lambda_1=\sqrt{0.8}$, $\lambda_2=\sqrt{0.2}$, both bases $|0\rangle,|1\rangle$. $0.8+0.2=1$ ✅. but $\frac{|00\rangle+|01\rangle+|11\rangle}{\sqrt3}$ isn't: it has 3 terms, and you need the SVD below

**how to find it** (singular value decomposition)
$$
|\psi\rangle=\sum_{jk}a_{jk}|j\rangle|k\rangle,\quad a=udv\quad\Rightarrow\quad|i_A\rangle=\sum_ju_{ji}|j\rangle,\ \ |i_B\rangle=\sum_kv_{ik}|k\rangle,\ \ \lambda_i=d_{ii}
$$
> [!example] eg. $\frac{|00\rangle+|01\rangle+|11\rangle}{\sqrt3}$
> put the amplitudes in a grid (row = A's bit, column = B's bit): $a=\frac1{\sqrt3}\begin{bmatrix}1&1\\0&1\end{bmatrix}$. its singular values are $\frac{1.618}{\sqrt3}$ and $\frac{0.618}{\sqrt3}$, so $\lambda\approx0.934,\ 0.357$. 2 non-zero → Schmidt number 2, entangled. (for a $2\times2$ grid: $\det a=0$ ⟺ product)

**both halves have the same eigenvalues**
$$
\rho^A=\sum_i\lambda_i^2|i_A\rangle\langle i_A|\qquad\rho^B=\sum_i\lambda_i^2|i_B\rangle\langle i_B|
$$
> [!example] eg. the same state
> $\lambda^2\approx0.873,\ 0.127$ are the eigenvalues of both $\rho^A=\frac13\begin{bmatrix}2&1\\1&1\end{bmatrix}$ and $\rho^B=\frac13\begin{bmatrix}1&1\\1&2\end{bmatrix}$

**product test**: product ⟺ Schmidt number 1 ⟺ $\text{tr}\big((\rho^A)^2\big)=1$
> [!example] eg.
> $|0\rangle|+\rangle$: $\rho^A=|0\rangle\langle0|$, purity 1 → product. $\Phi^+$: $\rho^A=\frac I2$, purity $\frac12$ → entangled


**purification** of $\rho^A=\sum_ip_i|i^A\rangle\langle i^A|$
$$
|AR\rangle=\sum_i\sqrt{p_i}\,|i^A\rangle|i^R\rangle\qquad\text{tr}_R\big(|AR\rangle\langle AR|\big)=\rho^A
$$
> [!example] eg. purify $\frac I2$
> $p_0=p_1=\frac12$ → $|AR\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}=\Phi^+$. a coin flip qubit is "half of a Bell pair"

**2 purifications differ only on $R$**: $|AR_1\rangle=(I_A\otimes U_R)|AR_2\rangle$
> [!example] eg.
> $\Psi^+=\frac{|01\rangle+|10\rangle}{\sqrt2}$ also purifies $\frac I2$, and $\Psi^+=(I\otimes X)\,\Phi^+$: an $X$ on $R$ only

> [!example] example: Schmidt form by spotting a product
> $$
> \frac{|00\rangle+|01\rangle+|10\rangle+|11\rangle}2=\frac{|0\rangle+|1\rangle}{\sqrt2}\otimes\frac{|0\rangle+|1\rangle}{\sqrt2}=|+\rangle|+\rangle
> $$
> one term, $\lambda_1=1$: Schmidt number 1, a product state

> [!question] exercise: Schmidt and purification
> (a) what are the Schmidt coefficients and bases of $\frac{|01\rangle+|10\rangle}{\sqrt2}$?
> (b) purify $\rho=\begin{bmatrix}0.7&0\\0&0.3\end{bmatrix}$
> (c) purify $\rho=\begin{bmatrix}\frac34&\frac14\\\frac14&\frac14\end{bmatrix}$ without finding its eigenvectors (hint: it's half $|0\rangle$, half $|+\rangle$)

> [!success]- answer
> (a) it's already in Schmidt form: $\lambda=\frac1{\sqrt2},\frac1{\sqrt2}$, with $A$'s basis $|0\rangle,|1\rangle$ and $B$'s basis $|1\rangle,|0\rangle$ (paired up as $0\leftrightarrow1$)
> (b) $|AR\rangle=\sqrt{0.7}\,|0\rangle|0\rangle+\sqrt{0.3}\,|1\rangle|1\rangle$
> (c) use the ensemble purification (exercise 2.82): $|AR\rangle=\sqrt{\frac12}\,|0\rangle|0\rangle+\sqrt{\frac12}\,|+\rangle|1\rangle$. tracing out $R$ gives $\frac12|0\rangle\langle0|+\frac12|+\rangle\langle+|=\rho$ ✅. (the eigenvector version, with $\sqrt{0.854}$ and $\sqrt{0.146}$, differs from this one only by a unitary on $R$)

## 6. EPR and the Bell inequality
from [[EPR and the Bell inequality]]

**the singlet** looks the same in every basis
$$
\frac{|01\rangle-|10\rangle}{\sqrt2}=e^{i\theta}\,\frac{|ab\rangle-|ba\rangle}{\sqrt2}\qquad e^{i\theta}=\alpha\delta-\beta\gamma=\det\begin{bmatrix}\alpha&\beta\\\gamma&\delta\end{bmatrix}
$$
> [!example] eg. the singlet in the $+/-$ basis
> $|0\rangle=\frac{|+\rangle+|-\rangle}{\sqrt2}$, $|1\rangle=\frac{|+\rangle-|-\rangle}{\sqrt2}$, so $\alpha=\beta=\gamma=\frac1{\sqrt2}$, $\delta=-\frac1{\sqrt2}$
> $$
> e^{i\theta}=\alpha\delta-\beta\gamma=-\tfrac12-\tfrac12=-1\qquad\Rightarrow\qquad\frac{|01\rangle-|10\rangle}{\sqrt2}=-\frac{|{+}{-}\rangle-|{-}{+}\rangle}{\sqrt2}
> $$
> still always opposite, now in $+/-$

**the Bell (CHSH) inequality**, with $Q,R,S,T=\pm1$
$$
\begin{aligned}
QS+RS+RT-QT&=(Q+R)S+(R-Q)T=\pm2\\
\text{E}(QS)+\text{E}(RS)+\text{E}(RT)-\text{E}(QT)&\leq2&&\text{(realism + locality)}\\
\text{quantum (singlet)}&=2\sqrt2\approx2.83&&\text{(breaks it)}
\end{aligned}
$$
> [!example] example: one run of the Bell experiment
> $Q=+1,\ R=-1,\ S=+1,\ T=-1$
> $$
> (Q+R)S+(R-Q)T=0\cdot(+1)+(-2)(-1)=2
> $$
> trying all 16 choices of $\pm1$ only ever gives $\pm2$, so a classical average can never beat 2

> [!example] the singlet's correlations
> for spin along unit vectors $\vec a$ (Alice) and $\vec b$ (Bob), the singlet gives
> $$
> \text{E}\big((\vec a\cdot\vec\sigma)\otimes(\vec b\cdot\vec\sigma)\big)=-\,\vec a\cdot\vec b
> $$
> same axis → $-1$ (always opposite, Box 2.7). at right angles → $0$ (no correlation)

> [!question] exercise: break the inequality
> use the singlet with $Q=Z$, $R=X$ on Alice's side and $S=\frac{-Z-X}{\sqrt2}$, $T=\frac{Z-X}{\sqrt2}$ on Bob's side. find the 4 averages and the Bell sum

> [!success]- answer
> as vectors: $Q=\hat z$, $R=\hat x$, $S=\frac{-\hat z-\hat x}{\sqrt2}$, $T=\frac{\hat z-\hat x}{\sqrt2}$. using $\text{E}=-\vec a\cdot\vec b$
> $$
> \begin{aligned}
> \text{E}(QS)&=-\hat z\cdot\tfrac{-\hat z-\hat x}{\sqrt2}=\tfrac1{\sqrt2}\qquad\text{E}(RS)=-\hat x\cdot\tfrac{-\hat z-\hat x}{\sqrt2}=\tfrac1{\sqrt2}\\
> \text{E}(RT)&=-\hat x\cdot\tfrac{\hat z-\hat x}{\sqrt2}=\tfrac1{\sqrt2}\qquad\text{E}(QT)=-\hat z\cdot\tfrac{\hat z-\hat x}{\sqrt2}=-\tfrac1{\sqrt2}\\
> \text{sum}&=\tfrac3{\sqrt2}+\tfrac1{\sqrt2}=\tfrac4{\sqrt2}=2\sqrt2\approx2.83>2
> \end{aligned}
> $$
> (checked numerically). so realism + locality can't both be true

see also [[Chapter 2 exercises]], [[Week 1 formulas]]
