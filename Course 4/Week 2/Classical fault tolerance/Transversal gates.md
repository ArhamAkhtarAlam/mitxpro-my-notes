#fault_tolerance #transversal #classical_computing
## gates between two blocks
the [[Fault-tolerant procedure]] examples so far act on one encoded bit. now a gate between **two** blocks, drawn with quantum circuit symbols but still classical: a controlled NOT from block $A$ to block $B$, both in the triple redundancy code, so each block is $000$ or $111$

> [!important] the one idea
> ==do your gates bitwise in parallel: bit $i$ of one block only ever talks to bit $i$ of the other==. then an error can only spread between the bits that interact, so one failure puts at most one error in each block. this is a **transversal** gate, and the same idea gives fault-tolerant **quantum** gates
## the shortcut that isn't fault tolerant
all three bits of $A$ should be the same, so why not use just the top one as the control for all three CNOTs?

![[CNOT_blocks_not_fault_tolerant.png]]

with no errors this is a perfectly fine controlled NOT between the blocks. but if wire $A_1$ fails, all three targets flip the wrong way: **3 errors in block $B$** from one failure. another single point of failure, so not fault tolerant
## the transversal CNOT
CNOT $A_1\to B_1$, $A_2\to B_2$, $A_3\to B_3$

![[CNOT_blocks_transversal.png]]

the same failure on $A_1$ now only reaches $B_1$: one error in $A$, one error in $B$, and the next round of majority votes fixes both

it's still the right **logical** gate. with $A=a\,a\,a$ and $B=b\,b\,b$
$$
\begin{aligned}
\text{CNOT}_{A_i\to B_i}\ \text{for }i=1,2,3:\quad(a\,a\,a,\ b\,b\,b)&\longrightarrow(a\,a\,a,\ b{\oplus}a\ \ b{\oplus}a\ \ b{\oplus}a)\\
&=\text{CNOT}_{A\to B}\ \text{on the logical bits}
\end{aligned}
$$

| | control | one failure on $A_1$ | fault tolerant? |
|---|---|---|---|
| shortcut | $A_1$ for all three | 1 error in $A$, **3** in $B$ | no |
| transversal | $A_i$ for target $B_i$ | 1 error in $A$, 1 in $B$ | yes |

you've already seen transversal gates: the 3 NOTs of the fault-tolerant NOT, and the 3 NANDs of the [[Fault-tolerant NAND gate]] (NAND $i$ takes $A_i$ and $B_i$) are both bitwise in parallel
## towards quantum
the same construction will be used for fault-tolerant **quantum** circuits ([[Fault-tolerant quantum computing]]). it matters even more there, because a quantum CNOT spreads errors **both ways**: a bit flip ($X$) on the control copies onto the target, and a phase flip ($Z$) on the target copies onto the control

> [!extra] the week 1 encoder is the "shortcut" pattern
> the [[Bit flip code]] encoder uses qubit 1 as the control for both CNOTs, so an $X$ on qubit 1 before them ends up on all three: $|111\rangle$ instead of $|000\rangle$. that's fine for encoding a fresh qubit (there's no code yet to protect), but between two encoded blocks you always want the transversal version

> [!exercise] try these
> ① in the shortcut circuit, wire $B_2$ fails instead. how many errors in each block?
> ② a Toffoli between three blocks, done transversally (Toffoli $i$ on $A_i$, $B_i$, $C_i$). is it fault tolerant?
> ③ check the transversal CNOT gives the right logical answer for $A=111$, $B=111$
> ④ a quantum $X$ error sits on $A_2$ before a transversal CNOT $A\to B$. where are the errors afterwards?

> [!answer]-
> ① only $B_2$ is wrong: 0 errors in $A$, 1 in $B$. the shortcut's problem is only its shared control
> ② yes: a failure in Toffoli $i$ can only touch bit $i$ of each block, so at most one error per block
> ③ each $B_i$ becomes $1\oplus1=0$, so $B=000$: logical $1\oplus1=0$ ✓
> ④ on $A_2$ and $B_2$: one error in each block, which each block's code can correct

see also [[Fault-tolerant procedure]], [[CNOT gate]], [[Fault-tolerant NAND gate]]

week hub: [[Principles of fault tolerance]]
