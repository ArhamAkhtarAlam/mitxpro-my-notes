#textbook #quantum_error_correction #exercises
worked answers to the exercises on p. 428–474 of the book (10.1 to 10.61). part of [[Quantum Computation and Quantum Information]]
## 10.1 the encoding circuit works
from [[Introduction to quantum error-correction#the bit flip channel and the bit flip code]]. CNOT from qubit 1 to 2, then from 1 to 3
$$
\begin{aligned}
(a|0\rangle+b|1\rangle)|0\rangle|0\rangle&=a|000\rangle+b|100\rangle\\
\xrightarrow{\text{CNOT}_{12}}\ &a|000\rangle+b|110\rangle\\
\xrightarrow{\text{CNOT}_{13}}\ &a|000\rangle+b|111\rangle\ ✓
\end{aligned}
$$
## 10.2 the bit flip channel as a measurement
**show** $(1-p)\rho+pX\rho X=(1-2p)\rho+2pP_+\rho P_++2pP_-\rho P_-$, with $P_\pm=\frac{I\pm X}2$ the projectors onto $|\pm\rangle$
$$
\begin{aligned}
2pP_+\rho P_++2pP_-\rho P_-&=\tfrac p2\big[(I+X)\rho(I+X)+(I-X)\rho(I-X)\big]\\
&=\tfrac p2\big[2\rho+2X\rho X\big]&&\text{(the }X\rho+\rho X\text{ terms cancel)}\\
&=p\rho+pX\rho X
\end{aligned}
$$
add $(1-2p)\rho$ and you get $(1-p)\rho+pX\rho X$ ∎. so: with probability $1-2p$ nothing happens, and with probability $2p$ the environment measures the qubit in the $|+\rangle,|-\rangle$ basis
## 10.3 two observables = four projectors
the projectors of $Z_1Z_2$ and $Z_2Z_3$, in terms of [[Syndrome diagnosis and recovery#^syndrome-projectors|$P_0,\dots,P_3$]] (each $P_j$ is the pair of basis states with that pattern of agreements)
$$
\begin{aligned}
Z_1Z_2:&\quad Q_+=P_0+P_3\ \ (\text{qubits 1, 2 equal})\qquad Q_-=P_1+P_2\\
Z_2Z_3:&\quad R_+=P_0+P_1\ \ (\text{qubits 2, 3 equal})\qquad R_-=P_2+P_3
\end{aligned}
$$
all of these commute, and since the $P_j$ are orthogonal
$$
Q_+R_+=P_0\qquad Q_-R_+=P_1\qquad Q_-R_-=P_2\qquad Q_+R_-=P_3
$$
measuring $Z_1Z_2$ then $Z_2Z_3$ gives outcome pair $(a,b)$ with probability $\text{tr}(R_bQ_a\rho Q_aR_b)=\text{tr}(P_j\rho P_j)$ and leaves $P_j\rho P_j/\text{tr}(P_j\rho P_j)$: exactly the statistics and post-measurement states of measuring $\{P_j\}$, with the labels $(+,+)\to0$, $(-,+)\to1$, $(-,-)\to2$, $(+,-)\to3$ ∎
## 10.4 measuring in the computational basis instead
**(1)** the eight projectors $|xyz\rangle\langle xyz|$. read the syndrome by majority: $000$ or $111$ → no flip; $100$ or $011$ → bit 1 flipped; $010$ or $101$ → bit 2; $001$ or $110$ → bit 3

**(2)** recovery works for $|0_L\rangle$ and $|1_L\rangle$ (eg. $|001\rangle\to$ flip bit 3 $\to|000\rangle$). but for $a|0_L\rangle+b|1_L\rangle$ the measurement **collapses** the state to $|0_L\rangle$ (probability $|a|^2$) or $|1_L\rangle$ (probability $|b|^2$), so the superposition is lost. it only works for computational basis states

**(3)** with $q=1-3p^2+2p^3$ the chance of at most one flip, the output is
$$
\begin{aligned}
\rho&=q\big(|a|^2|0_L\rangle\langle0_L|+|b|^2|1_L\rangle\langle1_L|\big)+(1-q)\big(|a|^2|1_L\rangle\langle1_L|+|b|^2|0_L\rangle\langle0_L|\big)\\
F^2&=\langle\psi|\rho|\psi\rangle=q\big(|a|^4+|b|^4\big)+(1-q)\,2|a|^2|b|^2
\end{aligned}
$$
with $s=2|a|^2|b|^2\in[0,\frac12]$, $|a|^4+|b|^4=1-s$, so $F^2=q+s(1-2q)$. for $p<\frac12$, $q>\frac12$, so this is smallest at $s=\frac12$ ($|a|=|b|$): $F^2=\frac12$. ==the minimum fidelity is $1/\sqrt2$==, whatever $p$ is, worse than not encoding at all
## 10.5 the Shor code's phase syndrome
a block $|000\rangle\pm|111\rangle$ is an eigenstate of $X_1X_2X_3$: it swaps $|000\rangle\leftrightarrow|111\rangle$, so
$$
X_1X_2X_3\big(|000\rangle\pm|111\rangle\big)=|111\rangle\pm|000\rangle=\pm\big(|000\rangle\pm|111\rangle\big)
$$
so $X_1X_2X_3$ reads the **sign** of block 1. comparing the signs of blocks 1 and 2 is measuring the product $X_1X_2X_3\cdot X_4X_5X_6$ ($+1$ same, $-1$ different), and blocks 2 and 3 is $X_4X_5X_6X_7X_8X_9$ ∎
## 10.6 recovering with $Z_1Z_2Z_3$
$Z_1Z_2Z_3$ gives $|111\rangle$ the sign $(-1)^3=-1$ and leaves $|000\rangle$, so it maps $|000\rangle\pm|111\rangle\to|000\rangle\mp|111\rangle$: it flips block 1's sign back. a phase flip $Z_j$ on qubit $j\in\{1,2,3\}$ followed by $Z_1Z_2Z_3$ leaves $Z_kZ_l$ (the other two), which does nothing to the block ($|111\rangle$ gets $(-1)^2$). so it's recovered ∎
## 10.7 the error-correction conditions for the bit flip code
$P=|000\rangle\langle000|+|111\rangle\langle111|$, errors $E_0=\sqrt{(1-p)^3}\,I$ and $E_k=\sqrt{p(1-p)^2}\,X_k$ for $k=1,2,3$
- $i=j$: $E_i^\dagger E_i\propto I$, so $PE_0^\dagger E_0P=(1-p)^3P$ and $PE_k^\dagger E_kP=p(1-p)^2P$
- $PE_0^\dagger E_kP\propto PX_kP=0$: $X_k$ maps $|000\rangle$ and $|111\rangle$ to weight 1 and weight 2 strings, outside the code
- $PE_j^\dagger E_kP\propto PX_jX_kP=0$ for $j\neq k$: weight 2 and weight 1 strings, outside again

$$
\alpha=\text{diag}\big((1-p)^3,\ p(1-p)^2,\ p(1-p)^2,\ p(1-p)^2\big)
$$
Hermitian ✓, so the conditions hold ([[Quantum error-correction conditions#^qec-conditions]])
## 10.8 the phase flip code and $\{I,Z_1,Z_2,Z_3\}$
$Z_j$ turns the $j$-th $|\pm\rangle$ into $|\mp\rangle$. all the products $E_i^\dagger E_j$ are $I$ (when $i=j$), a single $Z_j$, or $Z_jZ_k$
- $Z_j|{+}{+}{+}\rangle$ has one $-$, so it's orthogonal to both $|{+}{+}{+}\rangle$ and $|{-}{-}{-}\rangle$; same for $Z_j|{-}{-}{-}\rangle$. so $PZ_jP=0$
- $Z_jZ_k$ ($j\neq k$) gives two $-$s (or two $+$s), again orthogonal to both code words: $PZ_jZ_kP=0$

so $\alpha=I_4$ ✓
## 10.9 projector errors on the phase flip code
$P_i=|0\rangle\langle0|_i=\frac{I+Z_i}2$ and $Q_i=|1\rangle\langle1|_i=\frac{I-Z_i}2$: linear combinations of $I$ and $Z_i$, which are correctable (10.8). by [[Discretization of the errors#theorem 10.2|theorem 10.2]] the same recovery corrects $\{I,P_1,Q_1,P_2,Q_2,P_3,Q_3\}$ ∎
## 10.10 the Shor code satisfies the conditions
errors $I$ and $X_j,Y_j,Z_j$ for $j=1,\dots,9$. each product $E_a^\dagger E_b$ is (up to a phase) a Pauli product on **at most 2 qubits**. use the [[Shor nine qubit code#^shor-nine-codewords|code words]]
- **it has an $X$ or $Y$ part** (on 1 or 2 qubits): it flips 1 or 2 bits, so inside some block the three bits no longer agree. no code word has that, so the result is orthogonal to the code: $PE_a^\dagger E_bP=0$
- **only $Z$s, one $Z_j$**: flips the sign of $j$'s block, giving eg. $(-)(+)(+)$ from $(+)(+)(+)$, which is orthogonal to both $|0_L\rangle$ and $|1_L\rangle$: $0$
- **$Z_jZ_k$, different blocks**: $(-)(-)(+)$, orthogonal to both: $0$
- **$Z_jZ_k$, same block**: does nothing at all to the code words (10.6): $PZ_jZ_kP=P$
- **$I$** (when $a=b$, or $X_jX_j$, etc.): $P$

so every $PE_a^\dagger E_bP$ is $0$ or a phase times $P$, and $\alpha$ is Hermitian because $(PE_a^\dagger E_bP)^\dagger=PE_b^\dagger E_aP$ ✓. the $Z_jZ_k$ entries are why it's [[Degenerate codes and the quantum Hamming bound|degenerate]]: $\alpha$ isn't diagonal in this basis
## 10.11 the completely randomizing channel
$\mathcal E(\rho)=I/2$ for every $\rho$. use $\rho+X\rho X+Y\rho Y+Z\rho Z=2\,\text{tr}(\rho)\,I$. it's linear, so check it on $I,X,Y,Z$: for $\rho=I$ both sides are $4I$, and for $\rho=X$ the left side is $X+X-X-X=0$ ($X$ commutes with $X$ and anticommutes with $Y$, $Z$), matching $\text{tr}(X)=0$. same for $Y$ and $Z$
$$
\mathcal E(\rho)=\tfrac14\big(\rho+X\rho X+Y\rho Y+Z\rho Z\big)=\frac I2\qquad\text{elements }\Big\{\tfrac I2,\ \tfrac X2,\ \tfrac Y2,\ \tfrac Z2\Big\}
$$
and $\sum_kE_k^\dagger E_k=4\cdot\frac14I=I$ ✓. these are all Paulis, so the Shor code corrects even this on any one qubit
## 10.12 the depolarizing channel's fidelity
$$
\begin{aligned}
\mathcal E(|0\rangle\langle0|)&=(1-p)|0\rangle\langle0|+\tfrac p3\big(|1\rangle\langle1|+|1\rangle\langle1|+|0\rangle\langle0|\big)=\big(1-\tfrac{2p}3\big)|0\rangle\langle0|+\tfrac{2p}3|1\rangle\langle1|\\
F&=\sqrt{\langle0|\mathcal E(|0\rangle\langle0|)|0\rangle}=\sqrt{1-2p/3}
\end{aligned}
$$
it's the minimum because it's the same for **every** state: using 10.11, $X\rho X+Y\rho Y+Z\rho Z=2I-\rho$, so $\mathcal E(\rho)=\big(1-\frac{4p}3\big)\rho+\frac{2p}3I$, and $\langle\psi|\mathcal E(|\psi\rangle\langle\psi|)|\psi\rangle=1-\frac{4p}3+\frac{2p}3=1-\frac{2p}3$ for all $|\psi\rangle$ ∎
## 10.13 the amplitude damping channel's fidelity
for $|\psi\rangle=a|0\rangle+b|1\rangle$, write $x=|b|^2$ and $s=\sqrt{1-\gamma}$, $c=1-s$
$$
\begin{aligned}
F^2&=|\langle\psi|E_0|\psi\rangle|^2+|\langle\psi|E_1|\psi\rangle|^2=\big(|a|^2+s|b|^2\big)^2+\gamma|a|^2|b|^2\\
&=(1-cx)^2+\gamma x(1-x)\\
&=1-c^2x-2cs\,x^2&&\text{(using }\gamma=1-s^2=c(2-c)\text{)}
\end{aligned}
$$
this falls as $x$ grows, so the minimum is at $x=1$, $|\psi\rangle=|1\rangle$: $F^2=1-c^2-2cs=1-(1-s)(1+s)=s^2=1-\gamma$. so $F_{\min}=\sqrt{1-\gamma}$ ∎
## 10.14 the $r$ times repetition code
$G=I_k\otimes(1,1,\dots,1)^T$: an $rk\times k$ matrix whose column $j$ has 1s in rows $(j-1)r+1$ to $jr$ and 0s elsewhere (the $[6,2]$ example is $r=3$, $k=2$)
## 10.15 adding columns of $G$
replace column $g_i$ by $g_i+g_j$. the span of $\{g_i+g_j,g_j,\dots\}$ is the same as of $\{g_i,g_j,\dots\}$ (add $g_j$ again to get back), and the columns stay independent. same span → same set of code words ∎
## 10.16 adding rows of $H$
replace row $h_i$ by $h_i+h_j$. if $h_i\cdot x=h_j\cdot x=0$ then $(h_i+h_j)\cdot x=0$, and back again, so the solutions of $Hx=0$ don't change. Gaussian elimination is just row additions (and row swaps), so with bit swaps to move the pivots to the right, $H$ becomes $[A|I_{n-k}]$
## 10.17 parity check for the $[6,2]$ code
need 4 independent rows orthogonal to $(1,1,1,0,0,0)$ and $(0,0,0,1,1,1)$
$$
H=\begin{bmatrix}1&1&0&0&0&0\\0&1&1&0&0&0\\0&0&0&1&1&0\\0&0&0&0&1&1\end{bmatrix}
$$
two copies of the $[3,1]$ parity check: $Hx=0$ only for $000000$, $111000$, $000111$, $111111$
## 10.18 $HG=0$
every code word $Gx$ satisfies $H(Gx)=0$, for every message $x$. taking $x$ to be each unit vector, $H$ times each column of $G$ is 0, so $HG=0$ ∎
## 10.19 standard form
$H=[A|I_{n-k}]$ and $G=\begin{bmatrix}I_k\\-A\end{bmatrix}$ give $HG=A\,I_k+I_{n-k}(-A)=0$. $G$ has $k$ independent columns (the $I_k$ block), so its columns span a $k$ dimensional subspace of $\ker H$, which is $k$ dimensional. so they span all of it, and $G$ generates the code ∎
## 10.20 distance from the columns of $H$
a code word $x$ of weight $w$ means $Hx$ = the sum of the $w$ columns where $x$ has 1s = 0, ie. those columns are linearly dependent (over $Z_2$, dependent = some subset adds to 0). any $d-1$ columns are independent, so no nonzero code word has weight $\leq d-1$. some $d$ columns are dependent, so some subset adds to 0, and it can't be smaller than $d$, so all $d$ do: a code word of weight $d$. by [[Classical linear codes#^code-distance]], $d(C)=d$ ∎
## 10.21 the Singleton bound
$H$ is $(n-k)\times n$ with rank $n-k$, so any $n-k+1$ columns are dependent. by 10.20, $d\leq n-k+1$, ie. $n-k\geq d-1$ ∎
## 10.22 Hamming codes have distance 3
the columns are all the distinct nonzero $r$ bit strings. over $Z_2$ two vectors are dependent only if one is 0 or they're equal, so any 2 columns are independent. $001+010+011=000$, so some 3 are dependent. by 10.20, $d=3$. $H$ contains the unit vectors, so its rank is $r$, and $k=n-r=2^r-1-r$: a $[2^r-1,\ 2^r-r-1,\ 3]$ code ∎
## 10.23 the Gilbert-Varshamov bound
pick the $n\times k$ matrix $G$ at **random**. for each nonzero message $x$, $Gx$ is uniformly random over all $2^n$ strings, so
$$
P\big(\text{wt}(Gx)\leq2t\big)=\frac{V}{2^n}\qquad V=\sum_{j=0}^{2t}\binom nj
$$
there are $2^k-1$ nonzero messages, so the chance that **any** of them has weight $\leq2t$ is at most $2^kV/2^n$. if that's $<1$, some $G$ has every nonzero code word of weight $\geq2t+1$ (so distance $\geq2t+1$, it corrects $t$ errors, and $Gx\neq0$ means its columns are independent). for $2t\leq n/2$, $V\leq2^{nH(2t/n)}$, so it's enough that
$$
2^k2^{nH(2t/n)}<2^n\quad\Leftrightarrow\quad\frac kn<1-H\Big(\frac{2t}n\Big)
$$
so for large $n$ you can get $k/n$ as close to $1-H(2t/n)$ as you like ∎ ([[Classical linear codes#^gilbert-varshamov]])

## 10.24 weakly self-dual
$C\subseteq C^\perp$ means every pair of code words (including a word with itself) has inner product 0 mod 2. the code words are combinations of the columns of $G$, so it's enough that every pair of **columns** is orthogonal: $(G^TG)_{ij}=g_i\cdot g_j=0$ for all $i,j$, ie. $G^TG=0$ ∎
## 10.25 the character sum
if $x\in C^\perp$, every $x\cdot y=0$, so $\sum_{y\in C}(-1)^{x\cdot y}=|C|$. if $x\notin C^\perp$, the map $y\mapsto x\cdot y$ is a nonzero linear map $C\to Z_2$, so exactly half of $C$ gives 0 and half gives 1: the sum is 0 ∎ (this is the step used for phase flips in [[Calderbank-Shor-Steane codes#correcting the errors]])
## 10.26 computing $H x$ with CNOTs
$(Hx)_i=\sum_jH_{ij}x_j$ mod 2. for every 1 in row $i$, column $j$ of $H$, do a CNOT from data qubit $j$ onto ancilla $i$. each ancilla starts at 0 and gets flipped once per 1 among its bits, so it ends holding the parity $(Hx)_i$
## 10.27 shifted CSS codes
$Z^u|x+y\rangle=(-1)^{u\cdot(x+y)}|x+y\rangle$, so
$$
\frac1{\sqrt{|C_2|}}\sum_{y\in C_2}(-1)^{u\cdot y}|x+y+v\rangle=(-1)^{u\cdot x}\,X^vZ^u|x+C_2\rangle
$$
$\text{CSS}_{u,v}$ is $\text{CSS}(C_1,C_2)$ with a fixed Pauli $X^vZ^u$ applied. conjugating any error by a fixed Pauli only changes its sign, so the same errors are detectable and correctable (the syndromes just get a fixed known offset)
## 10.28 the generator of the Hamming code
the transpose of (10.77) is the $7\times4$ matrix with columns $1000011$, $0100101$, $0010110$, $0001111$. each satisfies $Hx=0$ for the Hamming $H$ (checked: $HG=0$), and the $I_4$ block makes them independent, so they span the 4 dimensional kernel: it's a generator matrix for $[7,4,3]$ ∎
## 10.29 $V_S$ is a subspace
if $g|\psi\rangle=|\psi\rangle$ and $g|\varphi\rangle=|\varphi\rangle$ then $g(a|\psi\rangle+b|\varphi\rangle)=a|\psi\rangle+b|\varphi\rangle$, for every $g\in S$. and "fixed by every $g$" is literally "in the $+1$ eigenspace of every $g$", the intersection ∎
## 10.30 $-I\notin S\Rightarrow\pm iI\notin S$
$(\pm iI)^2=-I$, and $S$ is closed under multiplication ∎
## 10.31 commuting generators
if the generators commute pairwise, two products of generators commute, since you can move each factor past the others one at a time. the other way round is immediate, the generators are elements of $S$ ∎
## 10.32 the Steane generators stabilize the code words
the $X$ generators' rows are rows of the Hamming $H$, which are code words of $C_2=C^\perp$, so they map $|x+y\rangle\to|x+y+h\rangle$ with $y+h\in C_2$: the sum over $C_2$ is unchanged. the $Z$ generators give $(-1)^{h\cdot(x+y)}$, and $x+y\in C_1$ means $H(x+y)=0$: sign $+1$ ∎ (checked numerically on [[Calderbank-Shor-Steane codes#^steane-book-codewords]])
## 10.33 the twisted inner product
write $r(g)=(a|b)$ and $r(g')=(a'|b')$. then $r(g)\Lambda r(g')^T=a\cdot b'+b\cdot a'$. on qubit $j$ that adds 1 exactly when the two factors anticommute ($X$ against $Z$, $X$ against $Y$, ...: check the 9 cases, eg. $Y$ against $Y$ gives $1+1=0$). Pauli products commute when the number of anticommuting places is even, so they commute iff the sum is 0 mod 2 ∎
## 10.34 when $-I$ is in $S$
every Pauli product squares to $\pm I$. if some $g_j^2=-I$, or $g_j=-I$, then $-I\in S$. so $-I\notin S$ forces $g_j^2=I$ and $g_j\neq-I$. (for the reverse direction you also need that no **product** of generators equals $-I$: eg. $X$ and $-X$ each square to $I$ but multiply to $-I$)
## 10.35 $g^2=I$ and $g^\dagger=g$
any $g\in G_n$ has $g^2=\pm I$. if $-I\notin S$ then $g^2=I$, and since $g$ is unitary, $g^\dagger=g^{-1}=g$ ∎
## 10.36 the CNOT conjugations
the matrix product in the note gives $UX_1U^\dagger=X_1X_2$ ([[Unitary gates and the stabilizer formalism#^conjugation-table]]). the others work the same way: $X$ on the target commutes with the CNOT, $Z$ on the control commutes with it, and $Z$ on the target picks up the control's $Z$ (all checked numerically)
## 10.37 $UY_1U^\dagger$
$Y_1=iX_1Z_1\to i(X_1X_2)Z_1=Y_1X_2$
## 10.38 the conjugations fix the unitary
if $U$ and $V$ conjugate $Z_1,Z_2,X_1,X_2$ the same way, then $W=V^\dagger U$ commutes with all four. they generate (as an algebra) every $4\times4$ matrix, so $W$ commutes with everything and is $cI$: $U=V$ up to a global phase ∎
## 10.39 the phase gate
$$
SXS^\dagger=\begin{bmatrix}1&0\\0&i\end{bmatrix}\begin{bmatrix}0&1\\1&0\end{bmatrix}\begin{bmatrix}1&0\\0&-i\end{bmatrix}=\begin{bmatrix}0&-i\\i&0\end{bmatrix}=Y\qquad SZS^\dagger=Z
$$
($S$ and $Z$ are both diagonal, so they commute)
## 10.40 $H$, $S$, CNOT generate the normalizer (sketch)
**(1)** a one qubit normalizer gate sends $X\to\pm P$ and $Z\to\pm Q$ with $P\neq Q$ Paulis: 6 choices for $P$, 4 for $Q$, 24 in all, and products of $H$ and $S$ reach all 24 ([[Clifford group]])
**(2)** given $UZ_1U^\dagger=X_1\otimes g$ and $UX_1U^\dagger=Z_1\otimes g'$, the circuit of figure 10.9 (controlled-$g'$, $H$, controlled-$g$ around a smaller $U'$) does the same conjugations on qubit 1, and $U'$ is an $n$ qubit normalizer gate, built by induction. the controlled Paulis are $O(n)$ CNOTs, $H$ and $S$
**(3)** any $U\in N(G_{n+1})$ can be brought to the form in (2) by one qubit normalizer gates and swaps first, so $O(n)$ extra gates per level and $O(n^2)$ in total ∎
## 10.41 $T$ and Toffoli
$$
TXT^\dagger=\begin{bmatrix}0&e^{-i\pi/4}\\e^{i\pi/4}&0\end{bmatrix}=\frac1{\sqrt2}\begin{bmatrix}0&1-i\\1+i&0\end{bmatrix}=\frac{X+Y}{\sqrt2}
$$
and $TZT^\dagger=Z$ (both diagonal). the Toffoli: it flips qubit 3 when qubits 1, 2 are both 1, so $Z_1$, $Z_2$, $X_3$ commute with it. for $X_1$: $\frac{I+Z_2+X_3-Z_2X_3}2$ is $I$ when qubit 2 is 0 and $X_3$ when qubit 2 is 1, which is the extra flip of qubit 3 that $X_1$ causes. same for the others (checked numerically)
## 10.42 teleportation
worked in [[Measurement and the Gottesman-Knill theorem#theorem 10.7: Gottesman-Knill]] for the input $|0\rangle$; the input $|+\rangle$ ($X_1$) works the same way, with the $Z$ correction controlled by the first measurement
## 10.43 $S\subseteq N(S)$
the elements of $S$ commute, so for $h,g\in S$, $hgh^\dagger=g\in S$ ∎
## 10.44 $N(S)=Z(S)$
for Pauli products $EgE^\dagger=\pm g$. if $E\in N(S)$ and $EgE^\dagger=-g$ for some $g\in S$, then $-g$ and $g$ are both in $S$, so $-I\in S$: impossible. so $EgE^\dagger=g$ for all $g$, ie. $E\in Z(S)$. the other way round is clear ∎
## 10.45 located errors
the possible errors are all Pauli products on the known $d-1$ qubits. any $E_j^\dagger E_k$ is also supported on those qubits, so it has weight $\leq d-1<d$ and can't be in $N(S)-S$ (that set has minimum weight $d$). by theorem 10.8 they're all correctable ∎
## 10.46 the phase flip code's stabilizer
$X|\pm\rangle=\pm|\pm\rangle$, so $X_1X_2$ and $X_2X_3$ give $+1$ on $|{+}{+}{+}\rangle$ and on $|{-}{-}{-}\rangle$ (two equal signs). they're independent and commuting, $n-k=2$, so they generate the whole stabilizer ∎
## 10.47 the Shor generators
$Z_iZ_j$ in one block gives $+1$ on $|000\rangle$ and $|111\rangle$. $X_1\cdots X_6$ maps $(|000\rangle\pm|111\rangle)(|000\rangle\pm|111\rangle)$ to itself times $(\pm1)(\pm1)=+1$, because both blocks of a code word have the **same** sign. same for $X_4\cdots X_9$ ∎
## 10.48 the Shor code's logical operators
$X^{\otimes9}$ commutes with each $Z_iZ_j$ (2 places) and with the $X$ generators; $Z^{\otimes9}$ commutes with each $X$ generator (6 places). they anticommute with each other (9 places). on the code words: $X^{\otimes3}$ maps $|000\rangle\pm|111\rangle$ to $\pm(\text{itself})$, so $X^{\otimes9}$ gives $+1$ on $|0_L\rangle$ and $(-1)^3=-1$ on $|1_L\rangle$: a logical $Z$. $Z^{\otimes3}$ swaps $|000\rangle+|111\rangle\leftrightarrow|000\rangle-|111\rangle$, so $Z^{\otimes9}$ swaps $|0_L\rangle\leftrightarrow|1_L\rangle$: a logical $X$ ∎
## 10.49 the five qubit code corrects any single error
the 15 single-qubit errors have 15 different nonzero syndromes ([[Stabilizer codes]] lists them). the syndrome of a product is the XOR of the syndromes, so for two **different** errors $E_jE_k$ has a nonzero syndrome: it anticommutes with some generator and isn't in $N(S)$. by theorem 10.8 all single-qubit errors are correctable ∎
## 10.50 the five qubit code saturates the Hamming bound
$\sum_{j=0}^1\binom5j3^j\,2^1=(1+15)\times2=32=2^5$ ∎
## 10.51 the CSS check matrix
the rows of $H(C_2^\perp)$ are the $X$ type generators and the rows of $H(C_1)$ the $Z$ type ones, so the code words are the states with $x+y\in C_1$ ($Z$ checks) that are unchanged by adding words of $(C_2^\perp)^\perp=C_2$ ($X$ checks): the coset states of $\text{CSS}(C_1,C_2)$. for errors on $\leq t$ qubits, a product $E_j^\dagger E_k$ has $X$ part and $Z$ part of weight $\leq2t$. if it commuted with all the $Z$ checks its $X$ part would be in $C_1$, and with all the $X$ checks its $Z$ part in $C_2^\perp$; both codes have distance $\geq2t+1$, so those parts are 0 or code words that are stabilizers. so $E_j^\dagger E_k\notin N(S)-S$ ∎
## 10.52 the Steane logical operators
$|0_L\rangle$'s strings have weight 0 or 4 and $|1_L\rangle$'s weight 3 or 7, so $Z^{\otimes7}$ gives $+1$ and $-1$: logical $Z$. $X^{\otimes7}$ flips every bit, which maps each string of $|0_L\rangle$ onto one of $|1_L\rangle$ (eg. $0000000\leftrightarrow1111111$, $1010101\leftrightarrow0101010$): logical $X$ ∎
## 10.53 the encoded $Z$s are independent
$G_z=[000|A_2^T0I]$ has the $k\times k$ identity in its last block, so its $k$ rows are linearly independent, and by proposition 10.3 the operators are independent ∎
## 10.54 the encoded $X$s
$G_x=[0E^TI|C^T00]$: the identity block makes them independent of each other; against the generators and the $\bar Z$s, the twisted products work out to $E^T+E^T=0$, $C^T+C^T=0$ for the generators, and $I$ against $G_z$'s $I$, giving $\bar X_j$ anticommuting only with $\bar Z_j$
## 10.55 $\bar X$ for the Steane code in standard form
from [[Standard form and stabilizer circuits#^steane-standard-form]], $E=(1,1,0)^T$ and $C=0$, so $\bar X=X_4X_5X_7$ in the standard order, $X_3X_5X_6$ in the original labels (it's $X^{\otimes7}$ times the stabilizer $X_1X_2X_4X_7$). checked numerically
## 10.56 multiplying by a stabilizer
for $g\in S$ and a code state $|\psi\rangle$: $g\bar X|\psi\rangle=\bar Xg|\psi\rangle=\bar X|\psi\rangle$ ($\bar X$ commutes with $g$). so $g\bar X$ and $\bar X$ do the same thing on the code ∎
## 10.57 standard forms for the five and nine qubit codes
**five qubit code**: $r=4$, no qubit swaps needed
$$
\left[\begin{array}{ccccc|ccccc}
1&0&0&0&1&1&1&0&1&1\\
0&1&0&0&1&0&0&1&1&0\\
0&0&1&0&1&1&1&0&0&0\\
0&0&0&1&1&1&0&1&1&1
\end{array}\right]
$$
**nine qubit code**: $r=2$, after swapping qubits 2 and 4
$$
\left[\begin{array}{ccccccccc|ccccccccc}
1&0&1&1&0&0&1&1&1&0&0&0&0&0&0&0&0&0\\
0&1&0&0&1&1&1&1&1&0&0&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0&0&1&0&1&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0&0&1&0&0&1&0&0&0&0&0\\
0&0&0&0&0&0&0&0&0&0&1&0&0&1&0&0&0&0\\
0&0&0&0&0&0&0&0&0&0&1&0&0&0&1&0&0&0\\
0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&1\\
0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&1
\end{array}\right]
$$
(computed by Gaussian elimination: rows only get added to each other, so they generate the same stabilizer)
## 10.58 the measuring circuits
figure 10.13: $|0\rangle\to\frac{|0\rangle+|1\rangle}{\sqrt2}$, controlled-$M$ gives $\frac{|0\rangle|\psi\rangle+|1\rangle M|\psi\rangle}{\sqrt2}$, and the last $H$ gives $|0\rangle\frac{I+M}2|\psi\rangle+|1\rangle\frac{I-M}2|\psi\rangle$: outcome 0 projects onto the $+1$ eigenspace, 1 onto the $-1$ one. for $M=Z$, $H$-controlled-$Z$-$H$ on the ancilla is a CNOT with the roles swapped ($H\otimes I$ turns CZ's control into a CNOT target), which gives figure 10.15. for $M=X$, write $X=HZH$ on the data qubit
## 10.59 the all-CNOT syndrome circuit
replace each controlled-$X$ from an ancilla by $H$ on the data, controlled-$Z$, $H$ on the data, and each controlled-$Z$ by a CNOT from the data onto the ancilla (CZ is symmetric, and $H$ on the ancilla turns it into a CNOT). the $H$s on the data cancel between neighbouring gates, leaving one layer before and one after the $X$ checks: figure 10.17
## 10.60 syndrome circuits for the nine and five qubit codes
one ancilla per generator (8 for the Shor code, 4 for the five qubit code), each prepared with $H$, then a controlled-$X$ onto every qubit where the generator has an $X$, a controlled-$Z$ onto every $Z$ (and both for a $Y$), then $H$ and measure. eg. the five qubit code's first ancilla does controlled-$X$ on qubits 1 and 4 and controlled-$Z$ on 2 and 3
## 10.61 recovery for the Steane circuit
the three $X$ type ancillas detect $Z$ errors and the three $Z$ type ancillas detect $X$ errors. an $X$ error on qubit $j$ makes $(s_4,s_5,s_6)$ equal column $j$ of the right block of the standard form, so apply $X_j$; a $Z$ error on qubit $j$ makes $(s_1,s_2,s_3)$ equal column $j$ of the left block, so apply $Z_j$ (a $Y$ shows up in both). all 7 columns of each block are different and nonzero, so every single-qubit error is identified

see also [[Chapter 10 formulas]], [[Quantum error-correction conditions]], [[Classical linear codes]], [[Stabilizer code constructions]]
