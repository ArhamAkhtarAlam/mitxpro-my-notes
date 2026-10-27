#formula_sheet #density_matrix #quantum_channel #noise
every formula from Course 3 Week 1 in one place, with an **eg.** under each formula showing how it's used, and each section ending with an **example** and an **exercise** (answers fold out, try them first). each section links to the note with the full explanation
## 1. Dirac notation and matrices
from [[Course 3/Week 1/Density matrices/Dirac notation|Dirac notation cheat sheet]] and [[Kets and bras combined]]

**basis, bras, inner products**
$$
|0\rangle=\begin{bmatrix}1\\0\end{bmatrix}\quad|1\rangle=\begin{bmatrix}0\\1\end{bmatrix}\qquad\langle0|=\begin{bmatrix}1&0\end{bmatrix}\quad\langle1|=\begin{bmatrix}0&1\end{bmatrix}\qquad\langle i|j\rangle=\begin{cases}1&i=j\\0&i\ne j\end{cases}
$$
> [!eg] eg.
> $\langle0|1\rangle=0$ (different basis states don't overlap). $\langle+|0\rangle=\frac1{\sqrt2}\begin{bmatrix}1&1\end{bmatrix}\begin{bmatrix}1\\0\end{bmatrix}=\frac1{\sqrt2}$

**any state, its length and its projector**
$$
\begin{aligned}
|\psi\rangle&=\alpha|0\rangle+\beta|1\rangle=\begin{bmatrix}\alpha\\\beta\end{bmatrix}\\
\big\||\psi\rangle\big\|&=\sqrt{\langle\psi|\psi\rangle}=\sqrt{|\alpha|^2+|\beta|^2}=1\\
|\psi\rangle\langle\psi|&=\begin{bmatrix}|\alpha|^2&\alpha\beta^*\\\beta\alpha^*&|\beta|^2\end{bmatrix}
\end{aligned}
$$
> [!eg] eg. $|\psi\rangle=\frac35|0\rangle+\frac45|1\rangle$
> length $\sqrt{\frac9{25}+\frac{16}{25}}=1$ ✅. projector $|\psi\rangle\langle\psi|=\frac1{25}\begin{bmatrix}9&12\\12&16\end{bmatrix}$

**2 qubits**
$$
\begin{aligned}
|\psi_{AB}\rangle&=\alpha|00\rangle+\beta|01\rangle+\gamma|10\rangle+\delta|11\rangle=\begin{bmatrix}\alpha\\\beta\\\gamma\\\delta\end{bmatrix}\\
\big\||\psi_{AB}\rangle\big\|&=\sqrt{|\alpha|^2+|\beta|^2+|\gamma|^2+|\delta|^2}
\end{aligned}
$$
> [!eg] eg.
> $\frac{|00\rangle+|11\rangle}{\sqrt2}=\frac1{\sqrt2}\begin{bmatrix}1\\0\\0\\1\end{bmatrix}$ (the order is $00,01,10,11$), length $\sqrt{\frac12+\frac12}=1$

**tensor products** (each number of the first × the whole second)
$$
\begin{bmatrix}\alpha\\\beta\end{bmatrix}\otimes\begin{bmatrix}\gamma\\\delta\end{bmatrix}=\begin{bmatrix}\alpha\gamma\\\alpha\delta\\\beta\gamma\\\beta\delta\end{bmatrix}\qquad A\otimes B=\begin{bmatrix}a_AB&c_AB\\b_AB&d_AB\end{bmatrix}
$$
$$
A\otimes I=\begin{bmatrix}a_A&0&c_A&0\\0&a_A&0&c_A\\b_A&0&d_A&0\\0&b_A&0&d_A\end{bmatrix}\qquad I\otimes A=\begin{bmatrix}a_A&c_A&0&0\\b_A&d_A&0&0\\0&0&a_A&c_A\\0&0&b_A&d_A\end{bmatrix}
$$
> [!eg] eg. $X\otimes I$ flips the first qubit
> $$
> X\otimes I=\begin{bmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{bmatrix}\qquad(X\otimes I)\begin{bmatrix}0\\1\\0\\0\end{bmatrix}=\begin{bmatrix}0\\0\\0\\1\end{bmatrix}:\ |01\rangle\to|11\rangle
> $$

**outer products build every matrix** ($|i\rangle\langle j|$ = a 1 in row $i$, column $j$)
![[Kets and bras combined#^outer-product-matrix]]

![[Kets and bras combined#^paulis-outer]]

> [!eg] eg.
> $|0\rangle\langle1|\,|1\rangle=|0\rangle\langle1|1\rangle=|0\rangle$ (it turns $1$ into $0$). $Z|+\rangle=\big(|0\rangle\langle0|-|1\rangle\langle1|\big)\frac{|0\rangle+|1\rangle}{\sqrt2}=\frac{|0\rangle-|1\rangle}{\sqrt2}=|-\rangle$
> [!example] example: $|0\rangle\otimes|+\rangle$ as a vector
> $$
> \begin{bmatrix}1\\0\end{bmatrix}\otimes\frac1{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix}=\frac1{\sqrt2}\begin{bmatrix}1\\1\\0\\0\end{bmatrix}=\frac{|00\rangle+|01\rangle}{\sqrt2}
> $$

> [!exercise] exercise
> (a) normalise $3|0\rangle+4i|1\rangle$ (b) write $|1\rangle\otimes|-\rangle$ as a column (c) find $\langle+|-\rangle$

> [!answer]- answer
> (a) length $\sqrt{|3|^2+|4i|^2}=\sqrt{9+16}=5$, so $\frac35|0\rangle+\frac{4i}5|1\rangle$
> (b) $\begin{bmatrix}0\\1\end{bmatrix}\otimes\frac1{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}=\frac1{\sqrt2}\begin{bmatrix}0\\0\\1\\-1\end{bmatrix}$
> (c) $\frac12\begin{bmatrix}1&1\end{bmatrix}\begin{bmatrix}1\\-1\end{bmatrix}=\frac12(1-1)=0$, they're orthogonal

## 2. projectors and measurement
from [[Projectors]]
$$
\Pi_\phi=|\phi\rangle\langle\phi|\qquad\Pi^2=\Pi\qquad\Pi^\dagger=\Pi\qquad\Pi_0+\Pi_1=I
$$

| what | formula |
|---|---|
| chance of result $i$ (pure state) | $P(i)=\langle\psi\vert\Pi_i\vert\psi\rangle=\vert\langle i\vert\psi\rangle\vert^2$ |
| chance of result $i$ (density matrix) | $P(i)=\text{tr}(\Pi_i\,\rho)$ |
| state after the measurement | $\vert\psi\rangle\to\dfrac{\Pi_i\vert\psi\rangle}{\sqrt{P(i)}}$ |
| measure only qubit A | $\Pi_{0_A}=\vert0\rangle\langle0\vert\otimes I$ |
| measure only qubit B | $I\otimes\vert0\rangle\langle0\vert$ |

> [!eg] eg. one for each row
> - $\Pi^2=\Pi$: $\Pi_+^2=\frac14\begin{bmatrix}1&1\\1&1\end{bmatrix}^2=\frac14\begin{bmatrix}2&2\\2&2\end{bmatrix}=\Pi_+$ (projecting twice = once)
> - **pure state**: $|\psi\rangle=\sqrt{0.7}|0\rangle+\sqrt{0.3}|1\rangle$, $P(1)=|\sqrt{0.3}|^2=0.3$
> - **density matrix**: $\rho=\begin{bmatrix}0.7&0\\0&0.3\end{bmatrix}$, $P(1)=\text{tr}(\Pi_1\rho)=$ the bottom right entry $=0.3$
> - **state after**: getting 1 from that $|\psi\rangle$ gives $\frac{\sqrt{0.3}|1\rangle}{\sqrt{0.3}}=|1\rangle$
> - **only qubit A**: on $\Phi^+=\frac{|00\rangle+|11\rangle}{\sqrt2}$, $(|0\rangle\langle0|\otimes I)\Phi^+=\frac{|00\rangle}{\sqrt2}$, so $P(A=0)=\frac12$ and the pair becomes $|00\rangle$
> [!example] example: $|\psi\rangle=\frac{|0\rangle+i|1\rangle}{\sqrt2}$
> $$
> P(0)=\Big|\tfrac1{\sqrt2}\Big|^2=\tfrac12\qquad P(+)=|\langle+|\psi\rangle|^2=\Big|\tfrac{1+i}2\Big|^2=\tfrac{1+1}4=\tfrac12
> $$
> 50/50 in both bases (it points along $+y$). take the **size** squared: $|1+i|^2=2$, not $(1+i)^2=2i$

> [!exercise] exercise
> $|\psi\rangle=\frac{\sqrt3}2|0\rangle+\frac12|1\rangle$. find (a) $P(0)$ and the state after getting 0 (b) $P(-)$ (c) for $\frac{|00\rangle+|01\rangle+|10\rangle}{\sqrt3}$, the chance that qubit A gives 0

> [!answer]- answer
> (a) $P(0)=\frac34$, and the state becomes $|0\rangle$
> (b) $\langle-|\psi\rangle=\frac1{\sqrt2}\big(\frac{\sqrt3}2-\frac12\big)$, so $P(-)=\frac{(\sqrt3-1)^2}8=\frac{2-\sqrt3}4\approx0.067$
> (c) $(\Pi_0\otimes I)$ keeps $\frac{|00\rangle+|01\rangle}{\sqrt3}$, length$^2$ $=\frac23$

## 3. density matrices
from [[Density matrix]] and [[Pure and mixed states]]

**definition**: $\rho$ is a density matrix if and only if
$$
\text{tr}(\rho)=1\qquad\text{and}\qquad\langle\varphi|\rho|\varphi\rangle\geq0\ \text{ for every }|\varphi\rangle
$$
> [!eg] eg.
> $\begin{bmatrix}1.2&0\\0&-0.2\end{bmatrix}$ has trace 1 but isn't positive ($\langle1|\rho|1\rangle=-0.2$), so it's **not** a density matrix. $\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}$ is (eigenvalues $1,0$)

**building and unravelling**
$$
\begin{aligned}
\rho&=\sum_kp_k\,|\psi_k\rangle\langle\psi_k|&&\text{(a mixture of states, }p_k\text{ = probabilities)}\\
\rho&=\sum_k\lambda_k\,|k\rangle\langle k|&&\text{(spectral decomposition: eigenvalues }\lambda_k\text{ add to 1)}\\
\rho&=\sum_kp_k\,\rho_k&&\text{(mixing density matrices gives a density matrix)}
\end{aligned}
$$
> [!eg] eg.
> - **mixture**: $0.7|0\rangle\langle0|+0.3|1\rangle\langle1|=\begin{bmatrix}0.7&0\\0&0.3\end{bmatrix}$
> - **spectral**: $\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}=1\cdot|+\rangle\langle+|+0\cdot|-\rangle\langle-|$ (eigenvalues $1,0$, so it's pure)
> - **mixing density matrices**: $\frac12|0\rangle\langle0|+\frac12\cdot\frac I2=\begin{bmatrix}\frac34&0\\0&\frac14\end{bmatrix}$

**a gate $U$ acting on a density matrix** (purity never changes, see [[Density matrix#how a gate changes a density matrix]])
$$
\rho\longrightarrow U\rho\,U^\dagger
$$
> [!eg] eg.
> $X\begin{bmatrix}0.7&0\\0&0.3\end{bmatrix}X=\begin{bmatrix}0.3&0\\0&0.7\end{bmatrix}$: the probabilities swap, purity stays $0.49+0.09=0.58$

**2 unravellings of the same $\rho$** are linked by a unitary $u$
$$
\rho=\sum_ip_i|\psi_i\rangle\langle\psi_i|=\sum_jq_j|\varphi_j\rangle\langle\varphi_j|\quad\Longleftrightarrow\quad\sqrt{p_i}\,|\psi_i\rangle=\sum_ju_{ij}\sqrt{q_j}\,|\varphi_j\rangle
$$
> [!eg] eg.
> $\frac I2=\frac12|0\rangle\langle0|+\frac12|1\rangle\langle1|=\frac12|+\rangle\langle+|+\frac12|-\rangle\langle-|$. with $\sqrt{\frac12}|\pm\rangle=\frac1{\sqrt2}\big(\sqrt{\tfrac12}|0\rangle\big)\pm\frac1{\sqrt2}\big(\sqrt{\tfrac12}|1\rangle\big)$, the unitary is $u=H$

**pure vs mixed**

| | pure | mixed |
|---|---|---|
| form | $\rho=\lvert\psi\rangle\langle\psi\rvert$ | $\rho=\sum_kp_k\lvert\psi_k\rangle\langle\psi_k\rvert$ |
| purity $\text{tr}(\rho^2)$ | $=1$ | $<1$ |
| $\rho^2=\rho$? | yes | no |

**purity of a mixture** of orthogonal states (squaring makes each $p_k<1$ smaller, so it's $<1$ unless one $p_k=1$)
$$
\text{tr}(\rho^2)=\sum_kp_k^2
$$
> [!eg] eg.
> $0.7|0\rangle\langle0|+0.3|1\rangle\langle1|$: $\text{tr}(\rho^2)=0.7^2+0.3^2=0.58$. a 50/50 mix gives the minimum, $0.25+0.25=0.5$

**on the [[Bloch sphere]]** (Bloch vector $\vec r$, length $r$)
$$
\rho=\frac{I+\vec r\cdot\vec\sigma}2\qquad\text{tr}(\rho^2)=\frac{1+r^2}{2}
$$
> [!eg] eg.
> $\begin{bmatrix}0.7&0\\0&0.3\end{bmatrix}$: $\vec r=(0,0,0.7-0.3)=(0,0,0.4)$, and $\frac{1+0.4^2}2=0.58$ ✅ the same purity as above

**the lecture's example**: $\sqrt{\tfrac34}\,|00\rangle+\sqrt{\tfrac14}\,|11\rangle$, B measured in 2 different ways
$$
\begin{aligned}
\rho_1&=\tfrac34|0\rangle\langle0|+\tfrac14|1\rangle\langle1|=\frac14\begin{bmatrix}3&0\\0&1\end{bmatrix}\\
\rho_2&=\frac18\begin{bmatrix}3&\sqrt3\\\sqrt3&1\end{bmatrix}+\frac18\begin{bmatrix}3&-\sqrt3\\-\sqrt3&1\end{bmatrix}=\frac14\begin{bmatrix}3&0\\0&1\end{bmatrix}=\rho_1
\end{aligned}
$$
> [!example] example: $\rho$ of $\frac{|0\rangle+i|1\rangle}{\sqrt2}$
> $$
> \rho=\frac12\begin{bmatrix}1\\i\end{bmatrix}\begin{bmatrix}1&-i\end{bmatrix}=\frac12\begin{bmatrix}1&-i\\i&1\end{bmatrix}\qquad\text{tr}(\rho^2)=\tfrac14(1+1+1+1)=1\ \text{(pure)}
> $$
> the bra has the **conjugate**, $-i$

> [!exercise] exercise: $\rho=0.6\,|0\rangle\langle0|+0.4\,|+\rangle\langle+|$
> (a) write the matrix (b) find its purity and Bloch vector (c) apply a Hadamard, does the purity change?

> [!answer]- answer
> (a) $0.6\begin{bmatrix}1&0\\0&0\end{bmatrix}+0.2\begin{bmatrix}1&1\\1&1\end{bmatrix}=\begin{bmatrix}0.8&0.2\\0.2&0.2\end{bmatrix}$
> (b) $\text{tr}(\rho^2)=0.64+0.04+2(0.04)=0.76$. $\vec r=(2\times0.2,\ 0,\ 0.8-0.2)=(0.4,0,0.6)$, and $\frac{1+r^2}2=\frac{1+0.52}2=0.76$ ✅
> (c) $H\rho H=\begin{bmatrix}0.7&0.3\\0.3&0.3\end{bmatrix}$, purity $0.49+0.09+2(0.09)=0.76$, **unchanged** (gates never change purity)

## 4. measuring one qubit of a pair
from [[Density matrix practice]]
$$
\begin{aligned}
p_{B,b}&=\langle\psi_{AB}|\,(I_A\otimes\Pi_b)\,|\psi_{AB}\rangle&&\text{(probability B gives }b\text{)}\\
|\psi_{AB}\rangle&\longrightarrow\frac{(I_A\otimes\Pi_b)|\psi_{AB}\rangle}{\sqrt{p_{B,b}}}&&\text{(state afterwards)}\\
\rho_A&=p_{B,0}\,|\psi_{A,0}\rangle\langle\psi_{A,0}|+p_{B,1}\,|\psi_{A,1}\rangle\langle\psi_{A,1}|&&\text{(A if you don't know B's result)}
\end{aligned}
$$
> [!example] example: measure B of $\frac{|00\rangle+|01\rangle+|10\rangle}{\sqrt3}$
> $$
> \begin{aligned}
> (I\otimes\Pi_0)|\psi\rangle&=\tfrac1{\sqrt3}(|00\rangle+|10\rangle)&p_{B,0}&=\tfrac23&\text{A}&=|+\rangle\\
> (I\otimes\Pi_1)|\psi\rangle&=\tfrac1{\sqrt3}|01\rangle&p_{B,1}&=\tfrac13&\text{A}&=|0\rangle\\
> \rho_A&=\tfrac23|+\rangle\langle+|+\tfrac13|0\rangle\langle0|=\tfrac13\begin{bmatrix}2&1\\1&1\end{bmatrix}
> \end{aligned}
> $$

> [!exercise] exercise
> measure B of the singlet $\frac{|01\rangle-|10\rangle}{\sqrt2}$. what are the chances, what's A left in, and what's $\rho_A$?

> [!answer]- answer
> B gives 0 (prob $\frac12$) → A is $|1\rangle$. B gives 1 (prob $\frac12$) → A is $|0\rangle$ (the minus sign is a global phase once normalised). so $\rho_A=\frac12|1\rangle\langle1|+\frac12|0\rangle\langle0|=\frac I2$

## 5. partial trace
from [[Partial trace]]
$$
\begin{aligned}
\rho_A&=\text{tr}_B(\rho_{AB})=\sum_j\big(I\otimes\langle j|\big)\,\rho\,\big(I\otimes|j\rangle\big)\\
\text{tr}_B\big(|a\rangle\langle a'|\otimes|b\rangle\langle b'|\big)&=|a\rangle\langle a'|\;\langle b'|b\rangle\\
(\rho_A)_{ik}&=\sum_j\rho_{(ij),(kj)}
\end{aligned}
$$
> [!eg] eg. the entry formula on $\Phi^+$ (rows/columns in the order $00,01,10,11$)
> $(\rho_A)_{00}=\rho_{00,00}+\rho_{01,01}=\frac12+0$ and $(\rho_A)_{01}=\rho_{00,10}+\rho_{01,11}=0+0$: you add up the entries where **B's bit matches** on both sides. so $\rho_A=\frac I2$

**blocks shortcut** (2 qubits)
$$
\rho_{AB}=\begin{bmatrix}P&Q\\R&S\end{bmatrix}\quad\Rightarrow\quad\rho_A=\begin{bmatrix}\text{tr}P&\text{tr}Q\\\text{tr}R&\text{tr}S\end{bmatrix}\qquad\rho_B=P+S
$$
**example**: half of a Bell pair is completely mixed
$$
\text{tr}_B\Big(\tfrac12\big(|00\rangle+|11\rangle\big)\big(\langle00|+\langle11|\big)\Big)=\frac I2
$$
> [!example] example: the blocks shortcut on $\frac{|00\rangle+|01\rangle+|10\rangle}{\sqrt3}$
> $$
> \rho_{AB}=\frac13\left[\begin{array}{cc|cc}1&1&1&0\\1&1&1&0\\\hline1&1&1&0\\0&0&0&0\end{array}\right]\quad\Rightarrow\quad\rho_A=\frac13\begin{bmatrix}1+1&1+0\\1+0&1+0\end{bmatrix}=\frac13\begin{bmatrix}2&1\\1&1\end{bmatrix}
> $$
> the same answer as measuring B and forgetting the result (section 4) ✅

> [!exercise] exercise
> find $\rho_A$ and $\rho_B$ for (a) $|+\rangle|0\rangle$ (b) $\frac{|00\rangle-|11\rangle}{\sqrt2}$

> [!answer]- answer
> (a) $\rho_{AB}=\frac12\begin{bmatrix}1&0&1&0\\0&0&0&0\\1&0&1&0\\0&0&0&0\end{bmatrix}$, so $\rho_A=\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}=|+\rangle\langle+|$ and $\rho_B=P+S=\begin{bmatrix}1&0\\0&0\end{bmatrix}=|0\rangle\langle0|$. a product, both pure
> (b) the corner entries $-\frac12$ sit in the blocks $Q$ and $R$, which have trace 0, so $\rho_A=\rho_B=\frac I2$

## 6. quantum channels
from [[Quantum channels]]

**dephasing** ([[Dephasing channel]]): $Z$ with probability $p$
$$
\begin{aligned}
\rho&\longrightarrow(1-p)\,\rho+p\,Z\rho Z\\
\begin{bmatrix}a&b\\b^*&c\end{bmatrix}&\longrightarrow\begin{bmatrix}a&(1-2p)\,b\\(1-2p)\,b^*&c\end{bmatrix}\\
(x,y,z)&\longrightarrow\big((1-2p)x,\ (1-2p)y,\ z\big)
\end{aligned}
$$
> [!eg] eg. dephasing in Bloch form
> $|+\rangle$ is $(1,0,0)$. with $p=0.1$: $(0.8,0,0)$. $|0\rangle$ is $(0,0,1)$ and stays $(0,0,1)$: dephasing only shrinks $x$ and $y$

**depolarizing** ([[Depolarizing channel]]): $X$, $Y$ or $Z$ each with probability $\frac p3$
$$
\begin{aligned}
\rho&\longrightarrow(1-p)\,\rho+\frac p3\big(\sigma_x\rho\sigma_x+\sigma_y\rho\sigma_y+\sigma_z\rho\sigma_z\big)\\
&=\Big(1-\tfrac43p\Big)\rho+\tfrac43p\,\frac I2\\
(x,y,z)&\longrightarrow\Big(1-\tfrac43p\Big)(x,y,z)
\end{aligned}
$$
the trick behind it: for **any** $\rho$
$$
\frac14\big(\rho+\sigma_x\rho\sigma_x+\sigma_y\rho\sigma_y+\sigma_z\rho\sigma_z\big)=\frac I2
$$
> [!eg] eg. the trick on $\rho=|0\rangle\langle0|$
> $X\rho X=|1\rangle\langle1|$, $Y\rho Y=|1\rangle\langle1|$, $Z\rho Z=|0\rangle\langle0|$, so $\frac14\big(2|0\rangle\langle0|+2|1\rangle\langle1|\big)=\frac I2$ ✅

**amplitude damping** ([[Amplitude damping channel]]): $|1\rangle$ decays to $|0\rangle$
$$
\begin{aligned}
\gamma&=1-e^{-t/T_1}\\
E_0&=\begin{bmatrix}1&0\\0&\sqrt{1-\gamma}\end{bmatrix}\qquad E_1=\begin{bmatrix}0&\sqrt\gamma\\0&0\end{bmatrix}\\
\rho&\longrightarrow E_0\,\rho\,E_0^\dagger+E_1\,\rho\,E_1^\dagger\\
\begin{bmatrix}a&b\\b^*&c\end{bmatrix}&\longrightarrow\begin{bmatrix}a+\gamma c&\sqrt{1-\gamma}\,b\\\sqrt{1-\gamma}\,b^*&(1-\gamma)\,c\end{bmatrix}\\
(x,y,z)&\longrightarrow\big(\sqrt{1-\gamma}\,x,\ \sqrt{1-\gamma}\,y,\ \gamma+(1-\gamma)z\big)
\end{aligned}
$$
> [!eg] eg. after one $T_1$
> $\gamma=1-e^{-1}\approx0.632$. on $|1\rangle$: $E_1|1\rangle=\sqrt\gamma\,|0\rangle$ (the "it decayed" jump, probability $\gamma$) and $E_0|1\rangle=\sqrt{1-\gamma}\,|1\rangle$ (no decay yet). each $E_k$ is a measurement operator $M_m$ from [[Chapter 2 formulas|the book's]] $\sum_mM_m\rho M_m^\dagger$

**binary symmetric channel** ([[Binary symmetric channel]]): each bit flips with probability $p$
$$
C=1-H(p)\qquad H(p)=-p\log_2p-(1-p)\log_2(1-p)
$$
> [!eg] eg.
> $p=0.1$: $H(0.1)=-0.1\log_20.1-0.9\log_20.9\approx0.469$, so $C\approx0.531$ bits per use
> [!example] example: dephasing $p=0.25$ on $|+\rangle$
> $$
> \frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}\longrightarrow\frac12\begin{bmatrix}1&0.5\\0.5&1\end{bmatrix}\qquad(1,0,0)\to(0.5,0,0)
> $$
> half the coherence is gone, the state is halfway to the centre

> [!exercise] exercise
> (a) depolarizing with $p=0.15$ on $|+\rangle$ (b) amplitude damping with $\gamma=0.5$ on $|1\rangle$ and on $|+\rangle$ (c) the capacity of a binary symmetric channel with $p=0.2$, and with $p=0.5$

> [!answer]- answer
> (a) shrink by $1-\frac43(0.15)=0.8$: $\frac12\begin{bmatrix}1&0.8\\0.8&1\end{bmatrix}$
> (b) $|1\rangle\to\begin{bmatrix}0.5&0\\0&0.5\end{bmatrix}$ (half decayed). $|+\rangle\to\begin{bmatrix}\frac{1+0.5}2&\frac{\sqrt{0.5}}2\\\frac{\sqrt{0.5}}2&\frac{0.5}2\end{bmatrix}\approx\begin{bmatrix}0.75&0.354\\0.354&0.25\end{bmatrix}$
> (c) $H(0.2)\approx0.722$, so $C\approx0.278$ bits per use. at $p=0.5$, $H=1$ and $C=0$: the output is pure coin flips

## 7. noise
from [[Noise power spectral density]], [[Rabi oscillation]] and [[Noise spectra]]

**time average vs ensemble average** (equal for an **ergodic** system)
$$
\begin{aligned}
\bar x&=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}x(t)\,dt&&\text{(time average, one run)}\\
\langle x(t_1)\rangle&=\lim_{N\to\infty}\frac1N\sum_{n=1}^Nx_n(t_1)=\int x\,p(x,t_1)\,dx&&\text{(ensemble average, many runs)}
\end{aligned}
$$
> [!eg] eg. a TV static pixel (random between 0 and 1)
> one pixel over time averages $0.5$, and all pixels at one moment average $0.5$: the 2 agree → ergodic

**mean square** (second moment)
$$
\begin{aligned}
\overline{x^2}&=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}x(t)^2\,dt&&\text{(time average)}\\
\langle x(t_1)^2\rangle&=\int x^2\,p(x,t_1)\,dx&&\text{(ensemble average)}
\end{aligned}
$$
> [!eg] eg.
> the same pixel: $\langle x^2\rangle=\int_0^1x^2\,dx=\frac13$ (not $0.5^2=0.25$, the difference $\frac1{12}$ is the variance)

**autocorrelation and covariance**
$$
\begin{aligned}
\overline{x(t)\,x(t+\tau)}&=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}x(t)\,x(t+\tau)\,dt\\
\langle x(t_1)\,x(t_2)\rangle&=\iint x_1x_2\,p(x_1,t_1;x_2,t_2)\,dx_1\,dx_2
\end{aligned}
$$
> [!eg] eg. $x(t)=\cos(\omega_0t)$
> $\overline{x(t)x(t+\tau)}=\frac12\cos(\omega_0\tau)$: it never dies away (a pure tone is correlated with itself forever). random noise loses its correlation after a time $\tau_c$

**power spectral density** (Wiener–Khinchin: the PSD and autocorrelation are a Fourier pair)
$$
\begin{aligned}
S_\lambda(\omega)&=\int_{-\infty}^{\infty}\langle\lambda(t)\lambda(t+\tau)\rangle\,e^{-i\omega\tau}\,d\tau&&\left[\tfrac{\lambda^2}{\text{Hz}}\right]\\
\langle\lambda(t)\lambda(t+\tau)\rangle&=\frac1{2\pi}\int_{-\infty}^{\infty}S_\lambda(\omega)\,e^{i\omega\tau}\,d\omega&&\left[\lambda^2\right]
\end{aligned}
$$
> [!eg] eg. 2 autocorrelations and their PSDs
> $$
> \begin{aligned}
> \langle\lambda(t)\lambda(t+\tau)\rangle&=\sigma^2\delta(\tau)&&\Rightarrow\ S(\omega)=\sigma^2&&\text{(no memory → flat, white noise)}\\
> \langle\lambda(t)\lambda(t+\tau)\rangle&=\sigma^2e^{-|\tau|/\tau_c}&&\Rightarrow\ S(\omega)=\frac{2\sigma^2\tau_c}{1+\omega^2\tau_c^2}&&\text{(memory }\tau_c\text{ → flat up to }\omega\approx\tfrac1{\tau_c}\text{, then falls)}
> \end{aligned}
> $$
> longer memory = power squeezed into lower frequencies

**noise spectra**

| noise | $S(\omega)$ | type |
|---|---|---|
| 1/f | $\propto\frac1f$, peaked at 0 | classical (symmetric) → dephasing |
| Johnson (thermal) | $\propto k_B\theta$, flat (white) | classical (symmetric) |
| Nyquist (quantum) | $\propto\hbar\omega$, positive frequencies only | quantum → spontaneous emission ($T_1$) |

> [!eg] eg.
> 1/f noise has $100\times$ more power at 1 Hz than at 100 Hz. slow drifts dominate, which is why it causes dephasing (the qubit frequency wanders slowly)

**Rabi oscillations**
$$
\begin{aligned}
\langle Z\rangle(t)&=\cos(\Omega t)&&\text{(ideal, }\Omega\propto\text{ drive amplitude)}\\
\langle Z\rangle(t)&=\cos(\Omega_0t)\,e^{-\sigma^2t^2/2}&&\text{(quasi-static amplitude noise: Gaussian decay)}
\end{aligned}
$$
> [!eg] eg.
> with $\Omega=2\pi\times5$ MHz, $\langle Z\rangle=\cos(\Omega t)$ first hits $-1$ (a full flip $|0\rangle\to|1\rangle$) at $t=\frac\pi\Omega=100$ ns
> [!example] example: how fast the Rabi envelope dies
> at $t=\frac2\sigma$: $e^{-\sigma^2t^2/2}=e^{-2}\approx0.135$, only 13.5% of the oscillation is left

> [!exercise] exercise
> (a) when is the envelope $e^{-\sigma^2t^2/2}$ down to half? (b) find the time average and mean square of $x(t)=\cos(\omega t)$ (c) each run of an experiment picks a random constant offset and keeps it. stationary? ergodic?

> [!answer]- answer
> (a) $\frac{\sigma^2t^2}2=\ln2$, so $t=\frac{\sqrt{2\ln2}}\sigma\approx\frac{1.18}\sigma$
> (b) $\bar x=0$ (it spends equal time above and below 0), $\overline{x^2}=\overline{\cos^2}=\frac12$
> (c) stationary (its statistics don't change in time) but **not** ergodic: one run's time average is just its own offset, not the average over all runs (like the bucket of batteries)

## 8. error correction (intro)
from [[Quantum Error Correction]]: the classical repetition code
$$
0\to000\qquad1\to111\qquad\text{(majority vote fixes 1 flipped bit)}
$$
> [!example] example: majority vote
> received $010$ → decode $0$. received $110$ → decode $1$

> [!exercise] exercise
> each bit flips independently with probability $p=0.1$. what's the chance the repetition code decodes wrongly?

> [!answer]- answer
> it fails if 2 or 3 bits flip: $3p^2(1-p)+p^3=3(0.01)(0.9)+0.001=0.028$. that's 2.8% instead of 10%, the code helps whenever $p<\frac12$


see also [[Density matrix]], [[Quantum channels]], [[Noise Processes]], [[Course 3/Week 1/Density matrices/Dirac notation|Dirac notation cheat sheet]]

worked examples for all of these: [[Week 1 examples]]
