#textbook #quantum_error_correction #bit_flip_code #syndrome #fidelity
*Quantum Computation and Quantum Information* §10.1.1 (p. 428–430). how the three qubit bit flip code finds and fixes an error **without** learning anything about the state. part of [[Quantum Computation and Quantum Information]], previous: [[Introduction to quantum error-correction]], course version: [[Parity measurement]], [[Decoding the bit flip code]]
## the two stages
the state $a|0\rangle+b|1\rangle$ has been perfectly encoded as $a|000\rangle+b|111\rangle$, each qubit goes through its own copy of the [[Bit flip channel]], and at most one qubit got flipped
### stage 1: error detection (syndrome diagnosis)
do a measurement that tells us **what error** happened. its result is the **error syndrome**. for the bit flip channel there are four syndromes, one per projector
$$
\begin{aligned}
P_0&\equiv|000\rangle\langle000|+|111\rangle\langle111|&&\text{no error}\\
P_1&\equiv|100\rangle\langle100|+|011\rangle\langle011|&&\text{bit flip on qubit one}\\
P_2&\equiv|010\rangle\langle010|+|101\rangle\langle101|&&\text{bit flip on qubit two}\\
P_3&\equiv|001\rangle\langle001|+|110\rangle\langle110|&&\text{bit flip on qubit three}
\end{aligned}
$$
^syndrome-projectors

say qubit one flipped, so the state is $a|100\rangle+b|011\rangle$. then $\langle\psi|P_1|\psi\rangle=1$: the syndrome is **certainly** 1, and measuring it **doesn't change the state** at all

> [!important] the one idea
> ==the syndrome only says which error happened, and nothing about $a$ or $b$==. that's why measuring it doesn't disturb the state: to learn anything about a quantum state you generally have to disturb it, and the syndrome learns nothing about it
### stage 2: recovery
use the syndrome to undo the error

| syndrome | meaning | do |
|---|---|---|
| 0 | no error | nothing |
| 1 | bit flip on qubit one | flip qubit one again |
| 2 | bit flip on qubit two | flip qubit two again |
| 3 | bit flip on qubit three | flip qubit three again |

each gets back $a|000\rangle+b|111\rangle$ with **perfect** accuracy, as long as that error really happened
## how often it works
it works whenever 0 or 1 qubits flip
$$
(1-p)^3+3p(1-p)^2=1-3p^2+2p^3
$$
so the chance of an error left over is the same as for the classical repetition code

![[Introduction to quantum error-correction#^repetition-error]]

and again the code helps when $p<1/2$
## a better error analysis: fidelity
that analysis is too crude. quantum errors aren't all equal: the "error" $X$ does **nothing** to $(|0\rangle+|1\rangle)/\sqrt2$, but turns $|0\rangle$ into $|1\rangle$. so measure how close the output is to what we wanted with the [[State fidelity|fidelity]] between a pure and a mixed state, $F(|\psi\rangle,\rho)=\sqrt{\langle\psi|\rho|\psi\rangle}$. error correction is about keeping it close to 1, so compare the **minimum** fidelity with and without the code

**without the code**, the qubit comes out as
$$
\begin{aligned}
\rho&=(1-p)|\psi\rangle\langle\psi|+pX|\psi\rangle\langle\psi|X\\
F&=\sqrt{\langle\psi|\rho|\psi\rangle}=\sqrt{(1-p)+p\,\langle\psi|X|\psi\rangle\langle\psi|X|\psi\rangle}
\end{aligned}
$$
the second term is $\geq0$, and $0$ for $|\psi\rangle=|0\rangle$, so the minimum is $F=\sqrt{1-p}$

**with the code**, protecting $|\psi\rangle=a|0_L\rangle+b|1_L\rangle$, after the noise and the correction
$$
\rho=\big[(1-p)^3+3p(1-p)^2\big]|\psi\rangle\langle\psi|+\dots
$$
where the $\dots$ are 2 or 3 flips. they're positive operators, so dropping them gives a **lower bound**
$$
\begin{aligned}
\text{no code:}\quad F_{\min}&=\sqrt{1-p}\\
\text{bit flip code:}\quad F&\geq\sqrt{(1-p)^3+3p(1-p)^2}=\sqrt{1-3p^2+2p^3}
\end{aligned}
$$
^bitflip-fidelity

better when $p<1/2$: the same conclusion as the crude analysis

![[Bit_flip_code_fidelity.png]]

the no-code line drops straight away (slope $-\frac12$), while the code's curve starts **flat**: for small $p$ its loss is only $\approx\frac32p^2$

> [!eg] $p=0.01$
> no code: $F_{\min}=\sqrt{0.99}=0.99499$, so $1-F\approx5\times10^{-3}$
> with the code: $F\geq\sqrt{0.999702}=0.999851$, so $1-F\approx1.5\times10^{-4}$, more than 30× smaller
## another way to see the syndrome: $Z_1Z_2$ and $Z_2Z_3$
this is the version that generalises. instead of the four projectors, measure two **observables**: $Z_1Z_2$ ($=Z\otimes Z\otimes I$) and $Z_2Z_3$. each has eigenvalues $\pm1$, so each gives one bit, two bits in all: four syndromes again. $Z_1Z_2$ **compares** qubits 1 and 2:
$$
Z_1Z_2=\big(|00\rangle\langle00|+|11\rangle\langle11|\big)\otimes I-\big(|01\rangle\langle01|+|10\rangle\langle10|\big)\otimes I
$$
^z1z2-decomposition

so it's a projective measurement giving $+1$ if qubits 1 and 2 are the same, and $-1$ if they're different. $Z_2Z_3$ does the same for qubits 2 and 3

in a circuit, each comparison is two CNOTs onto an ancilla ($SA$ for $Z_1Z_2$, $SB$ for $Z_2Z_3$), which ends up holding the **parity**, and then only the ancillas are measured

![[Bit_flip_syndrome_circuit.png]]

| $Z_1Z_2$ | $Z_2Z_3$ | most likely |
|---|---|---|
| $+1$ | $+1$ | no flip |
| $+1$ | $-1$ | qubit 3 flipped |
| $-1$ | $+1$ | qubit 1 flipped |
| $-1$ | $-1$ | qubit 2 flipped |

^z-syndrome-table

==neither measurement gives any information about $a$ and $b$==, so neither destroys the superposition we're protecting. (this is [[Parity measurement]] in the course notes, and exercise 10.3 shows it's the same as measuring $P_0,\dots,P_3$)

> [!extra] exercise 10.2: the bit flip channel as a measurement
> with $P_\pm$ the projectors onto $|\pm\rangle$, the same channel can be written $\mathcal E(\rho)=(1-2p)\rho+2pP_+\rho P_++2pP_-\rho P_-$: the qubit is left alone with probability $1-2p$, and **measured** in the $|+\rangle,|-\rangle$ basis by the environment with probability $2p$. worked in [[Chapter 10 exercises#10.2 the bit flip channel as a measurement]]

> [!exercise] try these
> ① the state after the channel is $a|010\rangle+b|101\rangle$. which $P_j$ fires, and what do you do?
> ② the minimum fidelity with and without the code at $p=0.1$
> ③ what do $Z_1Z_2$ and $Z_2Z_3$ give for a flip on qubit 2? check it with the formula for $Z_1Z_2$

> [!answer]-
> ① $P_2$, with certainty: flip qubit 2 back
> ② no code $\sqrt{0.9}=0.949$. code $\geq\sqrt{1-0.03+0.002}=\sqrt{0.972}=0.986$
> ③ both $-1$. eg. $|010\rangle$: qubits 1, 2 are $01$, which is in the $-$ part of $Z_1Z_2$, and qubits 2, 3 are $10$, also $-$

see also [[Parity measurement]], [[State fidelity]], [[Projectors]], [[Decoding the bit flip code]]

next: [[Three qubit phase flip code]]
