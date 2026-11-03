#textbook #classical_codes #linear_codes #hamming_code
*Quantum Computation and Quantum Information* §10.4 and §10.4.1 (p. 445–449). the classical theory that the big families of quantum codes (CSS, stabilizer) are built on. part of [[Quantum Computation and Quantum Information]], previous: [[Degenerate codes and the quantum Hamming bound]], course version: [[Quantum Error Correction#The classical idea: repetition code]]
## where this is going
we have a framework for quantum codes but hardly any examples. §10.4.1 tours classical **linear codes**, §10.4.2 uses them to build **Calderbank-Shor-Steane (CSS) codes**, and §10.5 does **stabilizer codes**, which are even more general. these pages cover §10.4.1
## the generator matrix
a **linear code** $C$ encoding $k$ bits in $n$ bits is given by an $n\times k$ **generator matrix** $G$ of zeros and ones (entries in $Z_2$). the $k$ bit message $x$ (a column vector) is encoded as $Gx$, with all arithmetic **modulo 2**. it's called an $[n,k]$ code

> [!eg] two repetition codes
> the $[3,1]$ repetition code, and repeating each of two bits three times, a $[6,2]$ code
> $$
> G=\begin{bmatrix}1\\1\\1\end{bmatrix}\qquad G=\begin{bmatrix}1&0\\1&0\\1&0\\0&1\\0&1\\0&1\end{bmatrix}
> $$
> the first gives $G[0]=(0,0,0)$ and $G[1]=(1,1,1)$. the second gives $G(0,0)=(0,0,0,0,0,0)$, $G(0,1)=(0,0,0,1,1,1)$, $G(1,0)=(1,1,1,0,0,0)$, $G(1,1)=(1,1,1,1,1,1)$. ($(a,b,\dots,z)$ means a column vector)

the code words are the vector space spanned by the columns of $G$. every message must get its own code word, so the columns must be **linearly independent**; that's the only constraint

==linear codes are compact==: a general code with $2^k$ code words of length $n$ takes $n2^k$ bits to write down, a linear code only the $kn$ bits of $G$, an **exponential** saving. encoding is fast too: multiplying by $G$ is $O(nk)$ operations. quantum stabilizer codes share both features
## the parity check matrix
$G$ makes encoding obvious, but not error correction. for that, use the equivalent **parity check** form: an $[n,k]$ code is all $n$ bit vectors $x$ with
$$
Hx=0
$$
^parity-check

where $H$ is an $(n-k)\times n$ matrix of zeros and ones, the **parity check matrix**. so the code is the **kernel** of $H$. it has $2^k$ code words, so the kernel must be $k$ dimensional, and $H$ needs linearly independent rows

**switching between them**
- $H\to G$: pick $k$ linearly independent vectors $y_1,\dots,y_k$ spanning the kernel of $H$, and make them the columns of $G$
- $G\to H$: pick $n-k$ linearly independent vectors $y_1,\dots,y_{n-k}$ orthogonal to the columns of $G$ (inner product $0$ mod 2), and make $y_1^T,\dots,y_{n-k}^T$ the rows of $H$

for the $[3,1]$ code, $(1,1,0)$ and $(0,1,1)$ are orthogonal to $(1,1,1)$
$$
H=\begin{bmatrix}1&1&0\\0&1&1\end{bmatrix}
$$
^repetition-parity-check

and $Hx=0$ only for $x=(0,0,0)$ and $(1,1,1)$. the rows compare bits 1, 2 and bits 2, 3: the classical version of measuring $Z_1Z_2$ and $Z_2Z_3$ ([[Syndrome diagnosis and recovery#^z-syndrome-table]])

**standard form**: adding one row of $H$ to another doesn't change the code, so by Gaussian elimination (and swapping bits) $H=[A|I_{n-k}]$, and then $G=\begin{bmatrix}I_k\\-A\end{bmatrix}$ (exercise 10.19; $-A=A$ mod 2). always $HG=0$
## the syndrome
encode $x$ as $y=Gx$, and noise adds an error $e$: $y'=y+e$ (bitwise mod 2). since $Hy=0$ for every code word
$$
Hy'=He
$$
^classical-syndrome

> [!important] the one idea
> ==the **error syndrome** $Hy'$ depends only on the error, not on the code word==: the classical version of a syndrome measurement that learns about the error but not the state

if one bit $j$ flipped, $e=e_j$ (a 1 in place $j$) and $He_j$ is just **column $j$ of $H$**. so if at most one error happens, compare $Hy'$ with the columns of $H$ to find which bit to flip
## distance
the **Hamming distance** $d(x,y)$ is the number of places where $x$ and $y$ differ, eg. $d\big((1,1,0,0),(0,1,0,1)\big)=2$. the **weight** $\text{wt}(x)\equiv d(x,0)$ is the number of 1s, and $d(x,y)=\text{wt}(x+y)$

for flip probability below $1/2$, the most likely code word sent is the $y$ that needs the fewest flips to reach $y'$, ie. minimizes $\text{wt}(e)=d(y,y')$. in principle you can always decode that way, but searching all $2^k$ code words is slow, so a lot of coding theory is about codes with structure that makes decoding efficient

the **distance of a code** is the smallest distance between two different code words. because the code is linear, $x+y$ is a code word, so
$$
d(C)\equiv\min_{x,y\in C,\ x\neq y}d(x,y)=\min_{x\in C,\ x\neq0}\text{wt}(x)
$$
^code-distance

write $[n,k,d]$. ==a code with distance at least $2t+1$ corrects errors on up to $t$ bits==: decode $y'$ to the unique code word with $d(y,y')\leq t$

two useful facts (exercises 10.20, 10.21)
- if any $d-1$ columns of $H$ are linearly independent but some $d$ columns aren't, the distance is $d$
- the **Singleton bound**: every $[n,k,d]$ code has $n-k\geq d-1$
## Hamming codes
for an integer $r\geq2$, let $H$ have as columns **all** $2^r-1$ nonzero bit strings of length $r$. this gives the **Hamming code**, $[2^r-1,\ 2^r-r-1,\ 3]$. the case $r=3$, a $[7,4]$ code, is especially important for quantum error correction
$$
H=\begin{bmatrix}0&0&0&1&1&1&1\\0&1&1&0&0&1&1\\1&0&1&0&1&0&1\end{bmatrix}
$$
^hamming-7-4

any two columns are different, so linearly independent, and the first three add to zero, so the distance is 3: it corrects any one error. ==column $j$ is $j$ written in binary==, so the syndrome $He_j$ literally **spells out** which bit to flip

each row of $H$ is a parity check on 4 of the bits, which you can draw as three overlapping circles

![[Hamming_7_4_venn.png]]

flip one bit and exactly the circles containing it go odd. every bit sits in a **different** set of circles (bit 7 in all three, bit 4 only in row 1, ...), so the odd circles point at one bit

> [!eg] decode a $[7,4]$ message
> $1110000$ is a code word: row 1 sees no 1s in places 4–7, row 2 sees places 2, 3 (two 1s), row 3 sees places 1, 3 (two 1s), all even. flip bit 6 and receive $y'=1110010$. then $Hy'$ = column 6 = $(1,1,0)$ = binary 6, so flip bit 6 back
## the Gilbert-Varshamov bound
are there good codes at all? for large $n$ there's an $[n,k]$ code correcting errors on $t$ bits with
$$
\frac kn\geq1-H\Big(\frac{2t}n\Big)
$$
^gilbert-varshamov

where $H(x)\equiv-x\log x-(1-x)\log(1-x)$ is the binary [[Shannon entropy]] (chapter 11). ==good codes exist, as long as you don't try to squeeze too many bits $k$ into too few $n$==. the proof is simple (exercise 10.23, in [[Chapter 10 exercises#10.23 the Gilbert-Varshamov bound]])
## dual codes
if $C$ is an $[n,k]$ code with generator $G$ and parity check $H$, its **dual** $C^\perp$ is the code with generator $H^T$ and parity check $G^T$. equivalently, $C^\perp$ is every $y$ orthogonal to all the code words of $C$
- **weakly self-dual**: $C\subseteq C^\perp$
- **strictly self-dual**: $C=C^\perp$

remarkably, the dual construction comes up naturally in quantum error correction: it's the key to the CSS codes ([[CSS codes]])

> [!exercise] try these
> ① receive $0011101$ with the $[7,4]$ Hamming code. which bit (if any) is wrong?
> ② what's the distance of the $[6,2]$ repetition code, and how many errors does it correct?
> ③ the Gilbert-Varshamov bound for $n=100$, $t=5$
> ④ find the dual of the $[3,1]$ repetition code. is it self-dual?

> [!answer]-
> ① places with a 1: 3, 4, 5, 7. row 1 (places 4–7): 4, 5, 7 → 3 ones → 1. row 2 (places 2, 3, 6, 7): 3, 7 → 0. row 3 (places 1, 3, 5, 7): 3, 5, 7 → 1. syndrome $(1,0,1)$ = 5: flip bit 5, giving $0011001$ (check: row 1 sees 4, 7, row 2 sees 3, 7, row 3 sees 3, 7, all even ✓)
> ② the smallest nonzero code word weight is 3 ($000111$), so $d=3$ and it corrects $t=1$
> ③ $H(0.1)=0.332+0.137=0.469$, so $k/n\geq0.531$: some code with $k\approx53$ data bits in 100 corrects any 5 errors
> ④ generator $H^T$, ie. spanned by $(1,1,0)$ and $(0,1,1)$: all even weight words $\{000,110,011,101\}$, a $[3,2]$ code. $C=\{000,111\}$ isn't inside it ($111$ has odd weight), so not even weakly self-dual

see also [[Binary symmetric channel]], [[Shannon entropy]], [[Channel capacity]], [[Degenerate codes and the quantum Hamming bound]]

next: [[Calderbank-Shor-Steane codes]]
