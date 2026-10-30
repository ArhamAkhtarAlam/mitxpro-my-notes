#quantum_error_correction #shor_code #bit_flip_code #phase_flip_code
## the problem
we have two codes, and each one only squeezes the errors one way

| code | fixes | makes 3× as likely |
|---|---|---|
| [[Bit flip code]] | $\sigma_x$ (bit) errors | $\sigma_z$ errors |
| [[Phase flip code]] | $\sigma_z$ (phase) errors | $\sigma_x$ errors (a $\sigma_x$ on any qubit swaps $\vert0_L\rangle\leftrightarrow\vert1_L\rangle$) |

squeeze on the phase errors and the bit errors blow up, squeeze on the bit errors and the phase errors blow up. so how do you fix this?
## concatenation
**combine** the two codes so they fix both. in classical coding theory this is called **concatenating** the codes
1. encode the qubit with one code: the **outer** code, here the phase code
2. then encode **each** of its qubits with the other: the **inner** code, here the bit code

so one qubit goes into $3\times3=9$ qubits
$$
\begin{aligned}
|0\rangle\ \to\ |0_L\rangle&=\tfrac1{\sqrt8}\big(|000\rangle+|111\rangle\big)\big(|000\rangle+|111\rangle\big)\big(|000\rangle+|111\rangle\big)\\
|1\rangle\ \to\ |1_L\rangle&=\tfrac1{\sqrt8}\big(|000\rangle-|111\rangle\big)\big(|000\rangle-|111\rangle\big)\big(|000\rangle-|111\rangle\big)
\end{aligned}
$$
^shor-codewords

> [!important] the one idea
> ==the nine qubit (Shor) code is a phase flip code whose qubits are each a bit flip code==: the inner bit codes fix any $\sigma_x$, the outer phase code fixes any $\sigma_z$, and together they fix **any** error on one qubit

(the outer phase code here is the $|{+}{+}{+}\rangle,|{-}{-}{-}\rangle$ version, see [[Phase flip code#Hadamard the code]], with each $|\pm\rangle$ replaced by $\frac1{\sqrt2}(|000\rangle\pm|111\rangle)$)

![[Shor_code_encoding_circuit.png]]

- the first two CNOTs and the three Hadamards are the outer phase code, spreading the qubit over qubits 1, 4, 7
- each of those then gets its own bit flip encoder (two CNOTs) to make the blocks 1–3, 4–6, 7–9

it's the same recursion as in [[Bit flip code#more levels (recursion)]], but with a **different** code at each level
## correcting a $\sigma_x$ error
first correct the **inner** code. it's just the bit flip code, so if there's a bit error, you correct it

> [!eg] $\sigma_x$ on qubit 5
> the middle block is hit:
> $$
> \tfrac1{\sqrt8}\big(|000\rangle\pm|111\rangle\big)\big(|010\rangle\pm|101\rangle\big)\big(|000\rangle\pm|111\rangle\big)
> $$
> ($+$ for $|0_L\rangle$, $-$ for $|1_L\rangle$). within the middle block, ask which bit is different ([[Parity measurement]]: qubits 4, 5 differ and 5, 6 differ → qubit 5), then flip it back. the $\pm$ signs are never looked at
## correcting a $\sigma_z$ error
> [!eg] $\sigma_z$ on qubit 5
> a $\sigma_z$ on any qubit of a block puts a minus sign on its $|111\rangle$:
> $$
> \big(|000\rangle+|111\rangle\big)_{456}\ \to\ \big(|000\rangle-|111\rangle\big)_{456}
> $$
> it flips the middle block's sign, which **is** a logical error for that block's bit code (it's a $\sigma_z$ on that block's encoded qubit, [[Decoding the bit flip code#what about phase errors?]])

so give the two block states names
$$
|0_x\rangle=\tfrac1{\sqrt2}\big(|000\rangle+|111\rangle\big)\qquad|1_x\rangle=\tfrac1{\sqrt2}\big(|000\rangle-|111\rangle\big)
$$
then the code is just a **bit flip code made of blocks**
$$
\begin{aligned}
|0_L\rangle&=|0_x\,0_x\,0_x\rangle\qquad|1_L\rangle=|1_x\,1_x\,1_x\rangle\\
\sigma_z^{(5)}:\quad|0_x\,0_x\,0_x\rangle&\to|0_x\,1_x\,0_x\rangle
\end{aligned}
$$
a $\sigma_z$ in the middle block is a **bit error on the middle "qubit"**, so we correct it exactly the same way: compare the three blocks and take the **majority** of whether they have a $+$ or a $-$. (the circuit for that is rather complicated, so the lecture skipped it)

> [!tip] any $\sigma_z$ in a block does the same thing
> $\sigma_z^{(4)}$, $\sigma_z^{(5)}$ and $\sigma_z^{(6)}$ all flip the same block's sign, so you don't need to know **which** qubit it was, only which **block**. you fix it with a $\sigma_z$ on any qubit of that block

## $\sigma_y$ errors
$\sigma_y=i\sigma_x\sigma_z$ ([[Y gate]]), so a $\sigma_y$ error is just a $\sigma_x$ error **and** a $\sigma_z$ error on the same qubit at once. correcting the $\sigma_x$ (inside the block) doesn't interfere with the $\sigma_z$ (the block signs), so you correct that afterwards. the overall phase $i$ doesn't matter

| error on one qubit | what it does | fixed by |
|---|---|---|
| $\sigma_x$ | flips one bit inside a block | the inner bit code (majority inside the block) |
| $\sigma_z$ | flips the sign of one block | the outer code (majority of the 3 block signs) |
| $\sigma_y$ | both | both, one after the other |

^shor-errors

==so the nine qubit code corrects one error of any of $\sigma_x$, $\sigma_y$, $\sigma_z$==
## what about every other error?
there are lots and lots of errors that aren't $\sigma_x$, $\sigma_y$ or $\sigma_z$. you could apply a [[Hadamard Gate|Hadamard]] to one of the qubits, or a small rotation, or measure it, or throw it away and put a $|1\rangle$ in its place. does the code correct those too?

> [!important] the theorem
> ==if a code can correct the identity (no error, on all the qubits) and $\sigma_x$, $\sigma_y$, $\sigma_z$ on any single qubit, it can correct **any** error on one qubit==: a removed and replaced qubit, a Hadamard, a rotation of any kind, a measurement. so you only ever need to correct $\sigma_x$, $\sigma_y$ and $\sigma_z$

the reason: $I$, $X$, $Y$, $Z$ are a basis for all $2\times2$ matrices, so any error on one qubit is a sum
$$
E=e_0I+e_1X+e_2Y+e_3Z
$$
^pauli-expansion

the syndrome measurement then **projects** the state onto one of the terms (no error, or an $X$, $Y$ or $Z$ on that qubit), and that one you know how to fix
### the phase code version
the simplest case: if a code can correct no error and a $\sigma_z$ on any qubit (like the [[Phase flip code]]), it can correct **any** phase error on any qubit, eg. a small $z$ rotation by $\theta$
$$
\begin{aligned}
R_z(\theta)&=e^{-i\theta Z/2}=\cos\tfrac\theta2\,I-i\sin\tfrac\theta2\,Z\\
R_z^{(1)}(\theta)\,|\psi_L\rangle&=\cos\tfrac\theta2\,|\psi_L\rangle-i\sin\tfrac\theta2\,\sigma_z^{(1)}|\psi_L\rangle
\end{aligned}
$$
the first part is in the "no error" subspace and the second in the "$\sigma_z$ on qubit 1" subspace ([[Phase flip code#^phase-subspaces]]). measuring which subspace gives
- "no error" with probability $\cos^2\frac\theta2$ → the state **is** $|\psi_L\rangle$ again, do nothing
- "$\sigma_z$ on qubit 1" with probability $\sin^2\frac\theta2$ → the state is $\sigma_z^{(1)}|\psi_L\rangle$, apply $\sigma_z$ to qubit 1

either way you get $|\psi_L\rangle$ back. ==the measurement turns a continuous error into a discrete one==, which is why "errors can be continuous" ([[Quantum Error Correction#Why quantum is harder]]) isn't a problem after all

this is closely related to the fact that the [[Dephasing channel]] can also be made by a small phase rotation $+\theta$ with probability $\frac12$ and the opposite one $-\theta$ with probability $\frac12$: the cross terms cancel and you're left with
$$
\rho\ \to\ \cos^2\tfrac\theta2\,\rho+\sin^2\tfrac\theta2\,Z\rho Z
$$
a dephasing channel with $q=\sin^2\frac\theta2$. "a random small rotation" and "a $Z$ with probability $q$" are the **same channel**, so a code that fixes one fixes the other

> [!eg] a $0.2$ rad phase wobble
> $q=\sin^2(0.1)=0.00997\approx1\%$. a qubit that randomly turns by $\pm0.2$ rad (11°) is the same as one that gets a full $\sigma_z$ 1% of the time

> [!exercise] try these
> ① a $\sigma_y$ hits qubit 2. what happens to the blocks, and how is it fixed?
> ② what happens if $\sigma_z$ hits qubits 4 **and** 5 (two errors in the same block)?
> ③ write a Hadamard error as a sum of Paulis. which syndromes can the measurement give?
> ④ how many qubits would you need to concatenate the Shor code with itself once more?

> [!answer]-
> ① the first block becomes $|010\rangle\mp|101\rangle$ (one bit flipped **and** the sign flipped). the inner code finds and flips qubit 2 back, leaving $|000\rangle\mp|111\rangle$, then the outer code sees the first block's sign disagree with the other two and fixes it with a $\sigma_z$ on qubits 1–3
> ② two $\sigma_z$'s on $|111\rangle$ give $(-1)^2=+1$, so the block is **unchanged**: no error at all. the Shor code doesn't even notice (it's a **degenerate** code: different errors can do the same thing)
> ③ $H=\frac1{\sqrt2}(X+Z)$, so the measurement gives "$\sigma_x$ on that qubit" or "$\sigma_z$ on that qubit", each with probability $\frac12$, and you fix whichever you get
> ④ $9\times9=81$ qubits

see also [[Bit flip code]], [[Phase flip code]], [[Decoding the bit flip code]], [[Pauli channel]], [[Quantum Error Correction]]

week hub: [[Detecting and correcting errors]]
