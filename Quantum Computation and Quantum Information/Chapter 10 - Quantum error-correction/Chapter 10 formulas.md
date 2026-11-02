#formula_sheet #textbook #quantum_error_correction
every formula from chapter 10 (p. 425–449) of *Quantum Computation and Quantum Information* in one place, with an **eg.** showing how each is used and an **exercise** per section (answers fold out, try them first). the formulas are embedded from the notes, so each section links to the full explanation. part of [[Quantum Computation and Quantum Information]]
## 1. the repetition code
from [[Introduction to quantum error-correction]]. majority voting on $000$/$111$ fails with 2 or more flips

![[Introduction to quantum error-correction#^repetition-error]]

the quantum version encodes superpositions, not copies

![[Introduction to quantum error-correction#^bitflip-codewords]]

> [!eg] eg. a channel with $p=0.2$
> $p_e=3(0.04)-2(0.008)=0.104$, about half of $0.2$. at $p=0.5$ it's $0.75-0.25=0.5$: no help at all

> [!exercise] exercise: what $p$ gives $p_e=10^{-6}$?
> use $p_e\approx3p^2$

> [!answer]- answer
> $p\approx\sqrt{10^{-6}/3}=5.8\times10^{-4}$

## 2. syndromes and fidelity
from [[Syndrome diagnosis and recovery]]

![[Syndrome diagnosis and recovery#^syndrome-projectors]]

or measure $Z_1Z_2$ and $Z_2Z_3$

![[Syndrome diagnosis and recovery#^z-syndrome-table]]

the minimum fidelity, without and with the code

![[Syndrome diagnosis and recovery#^bitflip-fidelity]]

> [!eg] eg. $p=0.05$
> no code $\sqrt{0.95}=0.9747$. code $\geq\sqrt{1-0.0075+0.00025}=\sqrt{0.99275}=0.99637$

> [!exercise] exercise: which syndrome?
> the state is $a|001\rangle+b|110\rangle$. give $P_j$ and the $Z_1Z_2$, $Z_2Z_3$ outcomes

> [!answer]- answer
> $P_3$; $Z_1Z_2=+1$, $Z_2Z_3=-1$: flip qubit 3

## 3. the phase flip code
from [[Three qubit phase flip code]]

![[Three qubit phase flip code#^phaseflip-codewords]]

![[Three qubit phase flip code#^phase-observables]]

> [!eg] eg. a phase flip on qubit 3
> $a|{+}{+}{-}\rangle+b|{-}{-}{+}\rangle$: $X_1X_2=+1$, $X_2X_3=-1$, so apply $Z_3$

> [!exercise] exercise: the other way round
> what's $H^{\otimes3}X_1X_2H^{\otimes3}$?

> [!answer]- answer
> $Z_1Z_2$, since $HXH=Z$

## 4. the Shor code
from [[Shor nine qubit code]]

![[Shor nine qubit code#^shor-nine-codewords]]

any error on one qubit is a combination of four, and the syndrome measurement picks one

![[Shor nine qubit code#^error-expansion]]

> [!eg] eg. a $Y$ on qubit 8
> bit checks in block 3 point at qubit 8, phase checks point at block 3: apply $X_8$ and $Z_7Z_8Z_9$ (since $Y_8=iX_8Z_8$)

> [!exercise] exercise: a rotation
> the error $R_x(\theta)=\cos\frac\theta2I-i\sin\frac\theta2X$ hits qubit 1. what are the possible syndromes and their probabilities?

> [!answer]- answer
> "no error" with probability $\cos^2\frac\theta2$, "bit flip on qubit 1" with probability $\sin^2\frac\theta2$. either way the state is restored exactly

## 5. the error-correction conditions
from [[Quantum error-correction conditions]]. success means

![[Quantum error-correction conditions#^qec-success]]

and a correction exists if and only if

![[Quantum error-correction conditions#^qec-conditions]]

diagonalizing $\alpha$ makes the errors not overlap on the code

![[Quantum error-correction conditions#^qec-diagonal]]

> [!eg] eg. the bit flip code and $\{I,Z_1\}$
> $PZ_1P=|000\rangle\langle000|-|111\rangle\langle111|$, which is **not** proportional to $P$. so the bit flip code can't correct phase flips, as expected

> [!exercise] exercise: errors $\{X_1,X_2\}$
> find $\alpha$ for the bit flip code

> [!answer]- answer
> $PX_1X_1P=PX_2X_2P=P$, and $PX_1X_2P=0$ ($X_1X_2$ maps $|000\rangle\to|110\rangle$, outside the code). $\alpha=I_2$ ✓

## 6. discretization
from [[Discretization of the errors]]. checking the four Paulis on a qubit covers every error on it

![[Discretization of the errors#^pauli-conditions]]

> [!eg] eg. $T_1$ decay on a qubit
> amplitude damping's $E_0$ and $E_1$ are combinations of $I$, $Z$ and $X+iY$, so a code that corrects $X$, $Y$, $Z$ on that qubit corrects it

> [!exercise] exercise: how many conditions?
> how many $P\sigma_i^j\sigma_{i'}^{j'}P$ conditions are there for "any one Pauli on any of 9 qubits, or none"?

> [!answer]- answer
> $1+27=28$ errors, so $28^2=784$ entries of $\alpha$ (half of them follow from the others by Hermiticity)

## 7. independent noise
from [[Independent error models]]

![[Independent error models#^depolarizing-fidelity]]

![[Independent error models#^independent-fidelity]]

![[Independent error models#^amplitude-damping-corrected]]

> [!eg] eg. a 7 qubit code at $p=10^{-3}$
> $1-F\approx\frac{21}2\times10^{-6}=1.05\times10^{-5}$, vs $3.3\times10^{-4}$ unencoded

> [!exercise] exercise: where does it break even?
> with the $p^2$ estimate, when is the 9 qubit code no better than no code ($\frac{36}2p^2=\frac p3$)?

> [!answer]- answer
> $p=\frac1{54}\approx0.019$. below that the code helps (the estimate gets rough near there, but it gives the scale)

## 8. bounds on quantum codes
from [[Degenerate codes and the quantum Hamming bound]]

![[Degenerate codes and the quantum Hamming bound#^quantum-hamming-bound]]

![[Degenerate codes and the quantum Hamming bound#^hamming-one-qubit]]

![[Degenerate codes and the quantum Hamming bound#^quantum-singleton]]

> [!eg] eg. the 7 qubit code ($k=1$, $t=1$)
> Hamming: $2(1+21)=44\leq128$ ✓. Singleton: $7\geq5$ ✓

> [!exercise] exercise: encode 3 qubits, correct 1 error
> smallest $n$ by the Hamming bound?

> [!answer]- answer
> $8(1+3n)\leq2^n$: $n=7$ gives $176>128$ ✗, $n=8$ gives $200\leq256$ ✓. so $n\geq8$

## 9. classical linear codes
from [[Classical linear codes]]

![[Classical linear codes#^parity-check]]

![[Classical linear codes#^classical-syndrome]]

![[Classical linear codes#^code-distance]]

![[Classical linear codes#^hamming-7-4]]

![[Classical linear codes#^gilbert-varshamov]]

> [!eg] eg. the $[7,4]$ code, error on bit 3
> the syndrome is column 3, $(0,1,1)$ = binary 3

> [!exercise] exercise: how many errors?
> a $[n,k,7]$ code corrects how many errors? and what does the Singleton bound say about $n-k$?

> [!answer]- answer
> $7=2t+1$ gives $t=3$. $n-k\geq6$

see also [[Chapter 10 exercises]], [[Course 4 Week 1 formulas]]
