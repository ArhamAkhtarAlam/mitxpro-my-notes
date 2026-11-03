#textbook #stabilizer_codes #shor_code #five_qubit_code
*Quantum Computation and Quantum Information* §10.5.5 and §10.5.6 (p. 464–470). stabilizer codes, logical operators, the error-correction conditions in stabilizer language, and the bit flip, Shor, five qubit and CSS codes as examples. part of [[Quantum Computation and Quantum Information]], previous: [[Measurement and the Gottesman-Knill theorem]], extra version: [[Stabilizer codes]]
## the definition
an $[n,k]$ **stabilizer code** $C(S)$ is the space $V_S$ stabilized by a subgroup $S$ of $G_n$ with $-I\notin S$ and $n-k$ independent commuting generators, $S=\langle g_1,\dots,g_{n-k}\rangle$ ([[The stabilizer formalism#^stabilizer-dimension|$2^k$ dimensional]])
## logical operators
pick $\bar Z_1,\dots,\bar Z_k\in G_n$ so that $g_1,\dots,g_{n-k},\bar Z_1,\dots,\bar Z_k$ is an independent commuting set. $\bar Z_j$ is the logical $Z$ on logical qubit $j$, and the logical basis state $|x_1,\dots,x_k\rangle_L$ is the state with stabilizer
$$
\langle g_1,\dots,g_{n-k},\ (-1)^{x_1}\bar Z_1,\dots,(-1)^{x_k}\bar Z_k\rangle
$$
^logical-basis

$\bar X_j$ is the Pauli product that takes $\bar Z_j\to-\bar Z_j$ by conjugation and leaves the other $\bar Z_i$ and all the $g$s alone: a NOT on encoded qubit $j$
## which errors are a problem?
for an error $E\in G_n$
- $E$ **anticommutes** with some element of $S$: it takes the code to an **orthogonal** subspace, so it can be detected (and maybe corrected) by a measurement
- $E\in S$: no problem at all, it doesn't change the code
- ==the real danger: $E$ **commutes** with everything in $S$ but isn't in $S$==. it changes the code state and can't be seen

the elements that commute with all of $S$ form the **centralizer** $Z(S)$. for the stabilizers here it's the same as the **normalizer** $N(S)$, the elements with $EgE^\dagger\in S$ for all $g\in S$ (exercise 10.44)
## theorem 10.8: the error-correction conditions for stabilizer codes
> [!important] theorem 10.8
> ==if $\{E_j\}\subset G_n$ has $E_j^\dagger E_k\notin N(S)-S$ for all $j$ and $k$, then $\{E_j\}$ is a correctable set of errors for $C(S)$==

(for Hermitian errors the condition is $E_jE_k\notin N(S)-S$.) it's [[Quantum error-correction conditions|theorem 10.1]] translated into stabilizer language

**proof**: with $P$ the projector onto the code, either $E_j^\dagger E_k\in S$, and then $PE_j^\dagger E_kP=P$; or $E_j^\dagger E_k\in G_n-N(S)$, so it anticommutes with some generator, say $g_1$. writing
$$
P=\frac{\prod_{l=1}^{n-k}(I+g_l)}{2^{n-k}}\qquad E_j^\dagger E_kP=(I-g_1)\,E_j^\dagger E_k\,\frac{\prod_{l=2}^{n-k}(I+g_l)}{2^{n-k}}
$$
and $P(I-g_1)=0$ since $(I+g_1)(I-g_1)=0$, so $PE_j^\dagger E_kP=0$. either way the conditions hold ∎

**doing it in practice**: measure $g_1,\dots,g_{n-k}$ to get the syndrome $\beta_1,\dots,\beta_{n-k}$, where $E_jg_lE_j^\dagger=\beta_lg_l$. if only $E_j$ has that syndrome, apply $E_j^\dagger$. if $E_j$ and $E_{j'}$ share a syndrome, then $E_j^\dagger E_{j'}\in S$, so applying $E_j^\dagger$ after $E_{j'}$ still works. ==for each syndrome, pick any one error with it and undo that one==
## distance
the **weight** of $E\in G_n$ is its number of non-identity factors (eg. $X_1Z_4Y_8$ has weight 3). the **distance** of $C(S)$ is the smallest weight in $N(S)-S$, written $[n,k,d]$. by theorem 10.8 a code with distance $2t+1$ corrects any errors on $t$ qubits, just like classically ([[Classical linear codes#^code-distance]])
## the examples
### the three qubit bit flip code
stabilizer $\langle Z_1Z_2,Z_2Z_3\rangle$. every product of two errors from $\{I,X_1,X_2,X_3\}$ (other than $I$) anticommutes with a generator, so they're correctable. the syndromes are the same table as before ([[Syndrome diagnosis and recovery#^z-syndrome-table]]): eg. $X_1$ turns $Z_1Z_2$ into $-Z_1Z_2$, giving $-1,+1$. nothing new for this code: the formalism pays off for bigger ones
### the Shor code
eight generators, plus the logical operators (figure 10.11)

| | operator |
|---|---|
| $g_1$–$g_6$ | $ZZIIIIIII$, $IZZIIIIII$, $IIIZZIIII$, $IIIIZZIII$, $IIIIIIZZI$, $IIIIIIIZZ$ |
| $g_7$, $g_8$ | $XXXXXXIII$, $IIIXXXXXX$ |
| $\bar Z$ | $XXXXXXXXX$ |
| $\bar X$ | $ZZZZZZZZZ$ |

^shor-stabilizer

==yes, $\bar Z$ is made of $X$s and $\bar X$ of $Z$s==, the reverse of what you'd guess. every product of two single-qubit errors is either in $S$ or anticommutes with something in $S$ (eg. $X_1Y_4$ anticommutes with $Z_1Z_2$), so the Shor code corrects any single-qubit error
### the five qubit code
the smallest code that corrects any single-qubit error (§12.4.3)

| | operator |
|---|---|
| $g_1$ | $XZZXI$ |
| $g_2$ | $IXZZX$ |
| $g_3$ | $XIXZZ$ |
| $g_4$ | $ZXIXZ$ |
| $\bar Z$ | $ZZZZZ$ |
| $\bar X$ | $XXXXX$ |

^five-qubit-book

(the last three generators are the first shifted right.) its code words are messier: 16 terms each with signs
$$
\begin{aligned}
|0_L\rangle=\tfrac14\big[&|00000\rangle+|10010\rangle+|01001\rangle+|10100\rangle+|01010\rangle-|11011\rangle-|00110\rangle-|11000\rangle\\
-&|11101\rangle-|00011\rangle-|11110\rangle-|01111\rangle-|10001\rangle-|01100\rangle-|10111\rangle+|00101\rangle\big]\\
|1_L\rangle=\tfrac14\big[&|11111\rangle+|01101\rangle+|10110\rangle+|01011\rangle+|10101\rangle-|00100\rangle-|11001\rangle-|00111\rangle\\
-&|00010\rangle-|11100\rangle-|00001\rangle-|10000\rangle-|01110\rangle-|10011\rangle-|01000\rangle+|11010\rangle\big]
\end{aligned}
$$
(checked numerically: both are stabilized by $g_1$–$g_4$, $\bar Z|0_L\rangle=|0_L\rangle$ and $\bar X|0_L\rangle=|1_L\rangle$). being smallest doesn't make it the most useful: the Steane code is often more transparent
### CSS codes and the seven qubit code
for $C_2\subset C_1$, with $C_1$ and $C_2^\perp$ correcting $t$ errors, the check matrix
$$
\left[\begin{array}{c|c}H(C_2^\perp)&0\\0&H(C_1)\end{array}\right]
$$
^css-check-matrix

defines a stabilizer code: the commutation condition is $H(C_2^\perp)H(C_1)^T=[H(C_1)G(C_2)]^T=0$, true because $C_2\subset C_1$. it's exactly [[Calderbank-Shor-Steane codes|$\text{CSS}(C_1,C_2)$]], and it corrects any errors on $t$ qubits. the Steane code's check matrix is [[The stabilizer formalism#^steane-check-matrix]], with
$$
\bar Z\equiv Z_1Z_2Z_3Z_4Z_5Z_6Z_7\qquad\bar X\equiv X_1X_2X_3X_4X_5X_6X_7
$$
^steane-logical

> [!exercise] try these
> ① show the five qubit code saturates the quantum Hamming bound (exercise 10.50)
> ② is $Z_1Z_2$ a problem for the Shor code?
> ③ the bit flip code has $Z_1\in N(S)-S$. what's its distance, and what does that say?

> [!answer]-
> ① $n=5$, $k=1$, $t=1$: $(1+3\times5)\times2=32=2^5$, equality ([[Degenerate codes and the quantum Hamming bound#^quantum-hamming-bound]])
> ② no: $Z_1Z_2=g_1\in S$, so it does nothing to the code. that's why the Shor code can't tell $Z_1$ from $Z_2$ and doesn't need to
> ③ weight 1, so $d=1$: it corrects no **arbitrary** errors (a single $Z$ slips through), only bit flips

see also [[Stabilizer codes]], [[Shor nine qubit code]], [[Transversal gates on stabilizer codes]], [[Quantum error-correction conditions]]

next: [[Standard form and stabilizer circuits]]
