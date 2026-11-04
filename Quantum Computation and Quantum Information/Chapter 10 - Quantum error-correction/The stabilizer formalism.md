#textbook #stabilizer_codes #pauli #group_theory
*Quantum Computation and Quantum Information* §10.5 and §10.5.1 (p. 453–459). describe a state (or a code) by the operators that leave it alone, instead of by its amplitudes. part of [[Quantum Computation and Quantum Information]], previous: [[Calderbank-Shor-Steane codes]], extra version: [[Stabilizer codes]]
## the idea
**stabilizer codes** (also called **additive** codes) are built the way classical linear codes are. the language for them, the **stabilizer formalism**, is useful far beyond error correction. the EPR state
$$
|\psi\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}
$$
satisfies $X_1X_2|\psi\rangle=|\psi\rangle$ and $Z_1Z_2|\psi\rangle=|\psi\rangle$: it's **stabilized** by $X_1X_2$ and $Z_1Z_2$. less obviously, it's the **unique** state (up to global phase) stabilized by both

> [!important] the one idea
> ==many quantum states, and many codes (CSS, the Shor code), are described far more easily by the operators that **stabilize** them than by their state vectors==. and errors, $H$, $S$, CNOT and computational basis measurements all have simple descriptions in this language
## the Pauli group
the single qubit Pauli group is all the Pauli matrices with factors $\pm1$, $\pm i$
$$
G_1\equiv\{\pm I,\pm iI,\pm X,\pm iX,\pm Y,\pm iY,\pm Z,\pm iZ\}
$$
^pauli-group

(the factors make it closed under multiplication, so it's a group). $G_n$ is all $n$-fold tensor products of Paulis, again with factors $\pm1,\pm i$
## stabilizers
for a subgroup $S$ of $G_n$, let $V_S$ be the set of $n$ qubit states fixed by **every** element of $S$. $V_S$ is the vector space **stabilized** by $S$, and $S$ is its **stabilizer**. $V_S$ is a subspace: the intersection of the $+1$ eigenspaces of the elements of $S$ (exercise 10.29)

> [!eg] three qubits
> $S=\{I,\ Z_1Z_2,\ Z_2Z_3,\ Z_1Z_3\}$. $Z_1Z_2$ fixes $|000\rangle,|001\rangle,|110\rangle,|111\rangle$, and $Z_2Z_3$ fixes $|000\rangle,|100\rangle,|011\rangle,|111\rangle$. the common ones are $|000\rangle$ and $|111\rangle$, so $V_S$ is spanned by them: the [[Bit flip code]]

**generators**: $g_1,\dots,g_l$ generate $G$ if every element is a product of them, $G=\langle g_1,\dots,g_l\rangle$. eg. $S=\langle Z_1Z_2,Z_2Z_3\rangle$ since $Z_1Z_3=(Z_1Z_2)(Z_2Z_3)$ and $I=(Z_1Z_2)^2$. a group of size $|G|$ has a set of at most $\log|G|$ generators, and to check a state is stabilized you only check the generators: a very compact description
## which $S$ give a non-trivial space?
not every subgroup works: $\{\pm I,\pm X\}$ only stabilizes $|\psi\rangle=0$, since $-I|\psi\rangle=|\psi\rangle$. two conditions are needed (and turn out to be enough)
1. **the elements of $S$ commute**. Paulis either commute or anticommute. if $MN=-NM$ for $M,N\in S$, then $|\psi\rangle=MN|\psi\rangle=-NM|\psi\rangle=-|\psi\rangle$, so $|\psi\rangle=0$
2. **$-I\notin S$**, or $-I|\psi\rangle=|\psi\rangle$ again forces $|\psi\rangle=0$

(it's enough to check that the generators commute, exercise 10.31)
## the Steane code as a stabilizer code
the six generators in figure 10.6 stabilize the Steane code ([[Calderbank-Shor-Steane codes#^steane-book-codewords]])

| name | operator |
|---|---|
| $g_1$ | $IIIXXXX$ |
| $g_2$ | $IXXIIXX$ |
| $g_3$ | $XIXIXIX$ |
| $g_4$ | $IIIZZZZ$ |
| $g_5$ | $IZZIIZZ$ |
| $g_6$ | $ZIZIZIZ$ |

^steane-generators-book

compare the messy state vectors with this clean list. $g_1$–$g_3$ have $X$s where the parity check matrix of $C_1$ has 1s, and $g_4$–$g_6$ have $Z$s where the one for $C_2^\perp$ has 1s (both the Hamming matrix). there's nothing special about the Steane code: it's just a subspace that happens to have a stabilizer description
## the check matrix
we want **independent** generators: removing any one makes the group smaller. to test that, write each generator $g$ as a $2n$ bit row $r(g)$: a 1 in column $j$ for an $X$ on qubit $j$, a 1 in column $n+j$ for a $Z$, both for a $Y$. stacking the $l$ rows gives the $l\times2n$ **check matrix** (the analog of the classical parity check matrix). for the Steane code
$$
\left[\begin{array}{ccccccc|ccccccc}
0&0&0&1&1&1&1&0&0&0&0&0&0&0\\
0&1&1&0&0&1&1&0&0&0&0&0&0&0\\
1&0&1&0&1&0&1&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0&0&0&1&1&1&1\\
0&0&0&0&0&0&0&0&1&1&0&0&1&1\\
0&0&0&0&0&0&0&1&0&1&0&1&0&1
\end{array}\right]
$$
^steane-check-matrix

it forgets the $\pm1,\pm i$ factors but keeps everything else. with $\Lambda=\begin{bmatrix}0&I\\I&0\end{bmatrix}$ ($I$ is $n\times n$), a "twisted" inner product tells you whether two Paulis commute
$$
g,\,g'\text{ commute}\quad\Longleftrightarrow\quad r(g)\,\Lambda\,r(g')^T=0\pmod2
$$
^twisted-product

and multiplying Paulis is adding rows: $r(g)+r(g')=r(gg')$
## three propositions
**proposition 10.3**: if $-I\notin S$, the generators are independent **if and only if** the rows of the check matrix are linearly independent. (every $g_i^2=I$, so a dependent set of rows means some product of generators is $I$, so one generator is a product of the others)

**proposition 10.4**: if $S=\langle g_1,\dots,g_l\rangle$ has independent generators and $-I\notin S$, then for each $i$ there's a $g\in G_n$ that **anticommutes** with $g_i$ and **commutes** with every other $g_j$. (the rows are independent, so solve $G\Lambda x=e_i$ for $x$, and let $r(g)=x^T$)

**proposition 10.5**: if $S$ has $n-k$ independent commuting generators and $-I\notin S$, then $V_S$ is $2^k$ dimensional
$$
\dim V_S=2^k\qquad\text{for }S=\langle g_1,\dots,g_{n-k}\rangle
$$
^stabilizer-dimension

**proof**: for $x\in Z_2^{n-k}$ define
$$
P_S^x\equiv\frac{\prod_{j=1}^{n-k}\big(I+(-1)^{x_j}g_j\big)}{2^{n-k}}
$$
$(I+g_j)/2$ projects onto the $+1$ eigenspace of $g_j$, so $P_S^{(0,\dots,0)}$ projects onto $V_S$. by proposition 10.4 there's a $g_x$ with $g_xP_S^{(0,\dots,0)}g_x^\dagger=P_S^x$, so every $P_S^x$ has the same dimension as $V_S$, and different $x$ give orthogonal projectors. finally $I=\sum_xP_S^x$: a $2^n$ dimensional space split into $2^{n-k}$ equal pieces, so each is $2^k$ dimensional ∎

==each independent generator halves the space==, just as you'd guess, since the $\pm1$ eigenspaces of a Pauli product are the same size. from now on, stabilizers always mean independent commuting generators with $-I\notin S$

> [!exercise] try these
> ① write the check matrix rows of $X_1Z_2$ and $Z_1X_2$, and use the twisted product to decide if they commute
> ② how many independent generators does the EPR state need, and why?
> ③ is $\langle X_1,Z_1\rangle$ a valid stabilizer?

> [!answer]-
> ① $r(X_1Z_2)=(1,0\,|\,0,1)$ and $r(Z_1X_2)=(0,1\,|\,1,0)$. $r\Lambda r'^T$ swaps the halves of $r'$: $(1,0,0,1)\cdot(1,0,0,1)=2=0$ mod 2, so they **commute** (they anticommute on both qubits)
> ② $n=2$ and $k=0$ (one state), so $n-k=2$: $X_1X_2$ and $Z_1Z_2$
> ③ no: $X_1$ and $Z_1$ anticommute, so they stabilize only the zero vector

see also [[Stabilizer codes]], [[Classical linear codes]], [[Bell states]], maths: [[Groups]], [[Pauli matrices]]

next: [[Unitary gates and the stabilizer formalism]]
