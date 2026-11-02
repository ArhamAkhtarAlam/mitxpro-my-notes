#formula_sheet #quantum_error_correction #threshold
every formula from Course 4 Week 1 on one page. formulas that live in a topic note are embedded from there (with a link to its worked example), the extra ones are written out here. each section has a folded **eg.** and an **exercise** (try it first). part of [[Detecting and correcting errors]]
## 1. the bit flip code
from [[Bit flip code]]

encode one qubit on three

![[Bit flip code#^encoding]]

it fails if 2 or 3 qubits flip

![[Bit flip code#^logical-error]]

it's only a win below the threshold (exactly $\frac12$ for $c=3$, $\frac1c=\frac13$ at leading order)

![[Bit flip code#^threshold]]

more levels: each one squares the error

![[Bit flip code#^concatenation]]

worked ($p=10^{-3}$, 330× better) in [[Bit flip code#when does the code fail?]]

> [!eg]- $p=0.02$
> $p_L=3(0.02)^2-2(0.02)^3=1.2\times10^{-3}-1.6\times10^{-5}=1.18\times10^{-3}$, about 17× better. ==the smaller $p$ is, the more the code gains==, since $\frac p{p_L}\approx\frac1{cp}$

> [!exercise] exercise
> (a) work out $p_L$ for $p=0.2$ and $p=0.6$. which one does the code help? (b) with $c=3$ and $p=10^{-2}$, what's $p^{(2)}$ (two levels, 9 qubits)?

> [!answer]-
> (a) $p=0.2$: $0.12-0.016=0.104$, better than $0.2$. $p=0.6$: $1.08-0.432=0.648$, **worse** than $0.6$ (above the exact threshold $\frac12$)
> (b) $\frac{(3\times0.01)^4}3=\frac{8.1\times10^{-7}}3=2.7\times10^{-7}$
## 2. parity checks and correction
from [[Parity measurement]] and [[Bit flip code#correcting the error]]

$s_A=q_1\oplus q_2$, $s_B=q_2\oplus q_3$, measured on ancillas

![[Parity measurement#^syndrome-table]]

then fix and reset

![[Bit flip code#^correction]]

worked step by step (a flip on qubit 1) in [[Parity measurement#why it doesn't destroy the state]]

> [!eg]- the state is $\alpha|010\rangle+\beta|101\rangle$
> qubits 1, 2 differ ($s_A=1$) and 2, 3 differ ($s_B=1$): syndrome $11$ → $X$ on qubit 2 → $\alpha|000\rangle+\beta|111\rangle$, then $X$ on both ancillas to reset them

> [!exercise] exercise
> qubits 2 **and** 3 both flip: $\alpha|011\rangle+\beta|100\rangle$. what syndrome comes out, what does the correction do, and what's the final state?

> [!answer]-
> $s_A=0\oplus1=1$, $s_B=1\oplus1=0$: syndrome $10$, which points at qubit 1. the $X$ on qubit 1 gives $\alpha|111\rangle+\beta|000\rangle$: a **logical** $X$, the code made it worse (2 flips is beyond what it can fix)
## 3. decoding without ancillas
from [[Decoding the bit flip code]]

run the encoder backwards, measure qubits 2 and 3, fix qubit 1 if they read $11$

![[Decoding the bit flip code#^decoding-table]]

worked case by case (the course's practice problem) in [[Bit flip code practice]]

> [!eg]- why a $\sigma_z$ slips through
> $\sigma_z$ on any qubit gives $\alpha|000\rangle-\beta|111\rangle$. decoding gives $(\alpha|0\rangle-\beta|1\rangle)|00\rangle$: measure $00$, "no error", but qubit 1 now has a phase flip ([[Decoding the bit flip code#what about phase errors?]])

> [!exercise] exercise
> work out what decoding gives for a $\sigma_x$ on qubit 3, $\alpha|001\rangle+\beta|110\rangle$

> [!answer]-
> CNOT $1\to2$: $\alpha|001\rangle+\beta|100\rangle$. CNOT $1\to3$: $\alpha|001\rangle+\beta|101\rangle=(\alpha|0\rangle+\beta|1\rangle)|01\rangle$. measure $01$, qubit 1 is already right, do nothing
## 4. the phase flip code
from [[Phase flip code]]

the bit flip code makes phase errors 3× worse

![[Phase flip code#^z-on-bit-code]]

so Hadamard it: even and odd states

![[Phase flip code#^phase-codewords]]

and the errors land in four orthogonal subspaces

![[Phase flip code#^phase-subspaces]]

the course's practice problem, case by case, in [[Phase flip code practice]]

> [!eg]- $q=0.05$
> on the bit flip code: $3(0.05)(0.95)^2+0.05^3=0.1355$, almost 3× the $0.05$ of one qubit. on the phase flip code it's $3q^2-2q^3=7.25\times10^{-3}$ instead

> [!exercise] exercise
> a qubit has $\sigma_x$ errors with $q=0.01$ and $\sigma_z$ errors with $q=0.001$. is the bit flip code or the phase flip code better, if you can only use one? (leading order is fine)

> [!answer]-
> bit flip code: $\sigma_x\to3(0.01)^2=3\times10^{-4}$, $\sigma_z\to3(0.001)=3\times10^{-3}$, total $\approx3.3\times10^{-3}$
> phase flip code: $\sigma_x\to3(0.01)=0.03$, $\sigma_z\to3(0.001)^2=3\times10^{-6}$, total $\approx0.03$
> the bit flip code wins, but both are worse than leaving it alone ($0.011$)! you need the [[Shor code]]
## 5. the Shor code
from [[Shor code]]

a phase code of bit codes

![[Shor code#^shor-codewords]]

what each error does

![[Shor code#^shor-errors]]

any single qubit error is a sum of Paulis

![[Shor code#^pauli-expansion]]

and a measurement makes a continuous error discrete

![[Shor code#^rz-expansion]]

a random $\pm\theta$ wobble is a dephasing channel

![[Shor code#^dephasing-rotation]]

> [!eg]- a $\pm0.1$ rad wobble
> $q=\sin^2(0.05)=2.5\times10^{-3}$: the same as a full $\sigma_z$ a quarter of a percent of the time

> [!exercise] exercise
> (a) what wobble $\theta$ gives $q=1\%$? (b) write the $S$ gate $\begin{bmatrix}1&0\\0&i\end{bmatrix}$ as $e_0I+e_3Z$. if it hits one qubit of the Shor code, which syndromes can come out, and how likely is each?

> [!answer]-
> (a) $\sin\frac\theta2=0.1$, so $\theta=2\arcsin0.1=0.200$ rad
> (b) $e_0+e_3=1$ and $e_0-e_3=i$, so $e_0=\frac{1+i}2$, $e_3=\frac{1-i}2$. "no error" or "$\sigma_z$ on that qubit", each with probability $|e|^2=\frac12$
## 6. computational capacity
from [[Computational capacity]]

the capacity of a channel

![[Channel capacity#^capacity]]

for a binary symmetric channel it's $C=1-H(p)$, with the binary entropy

![[Shannon entropy#^binary-entropy]]

repetition code with $n$ copies (odd) and majority vote: it fails if more than half flip
$$
P_n=\sum_{k>n/2}\binom nk\,p^k(1-p)^{n-k}\qquad\text{rate }\frac1n
$$
^repetition-error

worked ($p=0.1$: $C=0.53$, $P_3=0.028$, $P_5=0.0086$) in [[Computational capacity#why it works: error correcting codes]]

> [!eg]- $p=0.05$
> $H(0.05)=-0.05\log_20.05-0.95\log_20.95=0.216+0.070=0.286$, so $C=0.71$. three copies: $P_3=3(0.05)^2-2(0.05)^3=7.25\times10^{-3}$ at rate $\frac13$, well under the capacity

> [!exercise] exercise
> (a) $C$ for $p=0.11$ (use $H(0.11)=0.50$)? (b) $P_3$ and $P_5$ for $p=0.01$

> [!answer]-
> (a) $C=0.5$: every 2 uses of the channel carry 1 bit
> (b) $P_3=3(10^{-4})-2(10^{-6})=2.98\times10^{-4}$. $P_5=10p^3(1-p)^2+5p^4(1-p)+p^5\approx9.8\times10^{-6}$
## 7. triple modular redundancy
from [[Triple modular redundancy]]

a circuit of $N$ gates

![[Triple modular redundancy#^circuit-error]]

three copies and a perfect vote fail with $3p_{\text{circuit}}^2-2p_{\text{circuit}}^3$ (the same counting as section 1), so the break-even moves with $N$

![[Triple modular redundancy#^tmr-break-even]]

> [!eg]- $N=100$ gates, $p=10^{-3}$
> $p_{\text{circuit}}=1-0.999^{100}=0.095$. with TMR: $3(0.095)^2-2(0.095)^3=0.025$, about 4× better. ==the same gates in a 500 gate circuit barely gain anything==

> [!exercise] exercise
> (a) $N=500$, $p=10^{-3}$: $p_{\text{circuit}}$ and the TMR error? (b) the vote fails with $10^{-3}$. what's the TMR error for (a) now?

> [!answer]-
> (a) $p_{\text{circuit}}=1-0.999^{500}=0.394$. TMR: $3(0.394)^2-2(0.394)^3=0.343$, only a little better
> (b) about $0.343+0.001=0.344$: the vote's error adds on

see also [[Course 4 Week 2 formulas]], [[Week 1 formulas]] (course 3)

week hub: [[Detecting and correcting errors]]
