#quantum_error_correction #bit_flip_code
## the quantum repetition code
a second way to correct the [[Bit flip code]], with **no ancillas**: undo the encoding and measure. same code as before, "quantized"

$$
0\to000\qquad1\to111
$$

becomes

![[Bit flip code#^encoding]]

(not cloning, which is impossible, see [[No-cloning theorem]])

it should fix a single **bit error**: a $\sigma_x$ ($=X$) applied to any one of the three qubits. but we want to find **which** bit is different **without** measuring all three. measuring all three would collapse the superposition, and we want the same $\alpha|0\rangle+\beta|1\rangle$ to come out of the code after decoding as went in

> [!important] the one idea
> ==run the encoding circuit backwards and measure qubits 2 and 3: they tell you which bit was wrong, and qubit 1 is left holding the state==. if both read 1, qubit 1 itself was the bad one, so flip it

## the circuit
encode, (maybe) an error, then the **decoding circuit**: the same two CNOTs again (a CNOT is its own inverse, so this is the encoding circuit backwards), measure qubits 2 and 3, and apply $X$ to qubit 1 if both measurements are 1

![[Bit_flip_decoding_circuit.png]]

(the "If" box is the classical control: `0x3` means the two measured bits are $11$)

> [!eg] no error
> $$
> \begin{aligned}
> \alpha|000\rangle+\beta|111\rangle\ &\xrightarrow{\text{CNOT }1\to2}\ \alpha|000\rangle+\beta|101\rangle\\
> &\xrightarrow{\text{CNOT }1\to3}\ \alpha|000\rangle+\beta|100\rangle\\
> &=(\alpha|0\rangle+\beta|1\rangle)\otimes|00\rangle
> \end{aligned}
> $$
> measure $00$, and qubit 1 is back to the original state

an error on qubit 2 ($\sigma_x$ on the second bit): $|\psi_{err}\rangle=\alpha|010\rangle+\beta|101\rangle$
$$
\begin{aligned}
\alpha|010\rangle+\beta|101\rangle\ &\xrightarrow{\text{CNOT }1\to2}\ \alpha|010\rangle+\beta|111\rangle\\
&\xrightarrow{\text{CNOT }1\to3}\ \alpha|010\rangle+\beta|110\rangle\\
&=(\alpha|0\rangle+\beta|1\rangle)\otimes|10\rangle
\end{aligned}
$$
measure $10$: that says the **second** bit was wrong, and qubit 1 already holds $\alpha|0\rangle+\beta|1\rangle$. nothing to fix

an error on qubit 1: $\alpha|100\rangle+\beta|011\rangle$
$$
\begin{aligned}
\alpha|100\rangle+\beta|011\rangle\ &\xrightarrow{\text{CNOT }1\to2}\ \alpha|110\rangle+\beta|011\rangle\\
&\xrightarrow{\text{CNOT }1\to3}\ \alpha|111\rangle+\beta|011\rangle\\
&=(\alpha|1\rangle+\beta|0\rangle)\otimes|11\rangle
\end{aligned}
$$
measure $11$: qubit 1 is flipped, so apply $X$ to it → $\alpha|0\rangle+\beta|1\rangle$

| error | after decoding | measure (Q2 Q3) | qubit 1 | fix |
|---|---|---|---|---|
| none | $(\alpha\vert0\rangle+\beta\vert1\rangle)\vert00\rangle$ | $00$ | right | nothing |
| $\sigma_x$ on qubit 1 | $(\alpha\vert1\rangle+\beta\vert0\rangle)\vert11\rangle$ | $11$ | flipped | $X$ on qubit 1 |
| $\sigma_x$ on qubit 2 | $(\alpha\vert0\rangle+\beta\vert1\rangle)\vert10\rangle$ | $10$ | right | nothing |
| $\sigma_x$ on qubit 3 | $(\alpha\vert0\rangle+\beta\vert1\rangle)\vert01\rangle$ | $01$ | right | nothing |

^decoding-table

in every case qubits 2 and 3 come out in a **definite** state, not entangled with qubit 1, so measuring them doesn't touch $\alpha$ and $\beta$
## vs the parity check version
after decoding, qubit 2 holds $q_1\oplus q_2$ and qubit 3 holds $q_1\oplus q_3$: these are **parities** too, just compared with qubit 1 instead of with the neighbour ([[Parity measurement]])

| | [[Parity measurement\|parity checks]] | decoding |
|---|---|---|
| measures | $q_1\oplus q_2$, $q_2\oplus q_3$ | $q_1\oplus q_2$, $q_1\oplus q_3$ |
| extra qubits | 2 ancillas | none |
| afterwards | still **encoded**, ready for the next round | **decoded**, back to one qubit |

==decoding is simpler, but it throws the protection away==, so it's for the end of a computation or a transmission (eg. over a noisy channel). to keep a qubit safe for a long time you check parities again and again without decoding

> [!extra] a fully quantum fix
> instead of measuring and using a classical "if", put a **Toffoli** ([[Toffoli gate|CCNOT]]) controlled by qubits 2 and 3 on qubit 1. it flips qubit 1 exactly when both are $|1\rangle$, with no measurement at all. qubits 2 and 3 then hold the record of the error, and the noise's "mess" ends up in them instead of in the data. you have to reset or replace them before you use them again

## what about phase errors?
not every error is a $\sigma_x$. there are $\sigma_z$ ($=Z$) errors too. apply $\sigma_z$ to any one of the three qubits:
$$
\begin{aligned}
\sigma_z^{(1)},\ \sigma_z^{(2)}\text{ or }\sigma_z^{(3)}:\quad\alpha|000\rangle+\beta|111\rangle\ &\longrightarrow\ \alpha|000\rangle-\beta|111\rangle\\
&=\alpha|0_L\rangle-\beta|1_L\rangle
\end{aligned}
$$
all three give the **same** state: a $Z$ on the encoded qubit ($|111\rangle$ has a 1 in every slot, so any one $Z$ gives it a minus sign)

> [!warning] the 3 qubit bit error correcting code
> ==if you get a $\sigma_x$, it corrects it. if you get a $\sigma_z$ on any qubit, you've applied $\sigma_z$ to the encoded qubit==, and the code can't even tell. with three qubits there are three times as many places for it to happen, see [[Phase flip code#how bad are phase errors?]]

> [!exercise] try these
> ① decode $\alpha|001\rangle+\beta|110\rangle$ (an error on qubit 3) step by step. what do you measure?
> ② why does an error on qubit 1 need a fix but errors on qubits 2 and 3 don't?
> ③ what happens if you decode $\alpha|011\rangle+\beta|100\rangle$ (errors on qubits 2 and 3)?

> [!answer]-
> ① CNOT $1\to2$: $\alpha|001\rangle+\beta|100\rangle$. CNOT $1\to3$: $\alpha|001\rangle+\beta|101\rangle=(\alpha|0\rangle+\beta|1\rangle)|01\rangle$. measure $01$, qubit 1 is fine
> ② the decoded state comes out on qubit 1. an error on 2 or 3 only changes what you measure there, which you throw away anyway
> ③ CNOT $1\to2$: $\alpha|011\rangle+\beta|110\rangle$. CNOT $1\to3$: $\alpha|011\rangle+\beta|111\rangle=(\alpha|0\rangle+\beta|1\rangle)|11\rangle$. you measure $11$ and "fix" qubit 1 to $\alpha|1\rangle+\beta|0\rangle$: two errors fool the code ([[Bit flip code#when it breaks]])

see also [[Bit flip code]], [[Parity measurement]], [[Phase flip code]], [[CNOT gate]]

week hub: [[Detecting and correcting errors]]
