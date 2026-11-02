#textbook #quantum_error_correction #degenerate_codes #hamming_bound
*Quantum Computation and Quantum Information* §10.3.3 and §10.3.4 (p. 444–445). a property classical codes can't have, and a counting argument for how small a code can be. part of [[Quantum Computation and Quantum Information]], previous: [[Independent error models]], course version: [[Shor code]]
## degenerate codes
in most ways quantum codes are like classical ones: measure the syndrome, then correct. but some quantum codes, the **degenerate** codes, have a property no classical code has. the Shor code shows it: the errors $Z_1$ and $Z_2$ have **the same effect** on both code words (they each flip the sign of block 1, see [[Shor nine qubit code#phase flips]]). for classical codes, errors on different bits always give **different** corrupted code words

> [!important] the one idea
> ==in a degenerate code, different errors can do the same thing to the code, so they don't need to land in orthogonal subspaces==. the correction can't tell $Z_1$ from $Z_2$, and it doesn't need to: undoing either one undoes both

it's good news and bad news
- **bad**: some classical proof techniques for bounds on error correction don't work for degenerate codes (eg. the quantum Hamming bound below)
- **good**: degenerate codes seem to be among the most interesting quantum codes. in a sense they "pack more information in", since distinct errors don't each need their own orthogonal space, and it may be (though not yet shown) that some degenerate code stores quantum information more efficiently than any non-degenerate one
## the quantum Hamming bound
we want the "best" codes, so we want rules for whether a code with given properties can exist. take a **non-degenerate** code encoding $k$ qubits in $n$ qubits that corrects errors on any $t$ or fewer qubits
- $j$ errors ($j\leq t$) can be in $\binom nj$ sets of positions
- each position can get one of 3 errors, $X$, $Y$, $Z$, so $3^j$ errors per set
- the total number of errors on $t$ or fewer qubits ($j=0$ is the "error" $I$)

$$
\sum_{j=0}^t\binom nj3^j
$$
non-degenerate means each of these errors needs its own **orthogonal** $2^k$ dimensional subspace, and they all have to fit in the $2^n$ dimensions of $n$ qubits
$$
\sum_{j=0}^t\binom nj3^j2^k\leq2^n
$$
^quantum-hamming-bound

==the quantum Hamming bound==. for one qubit ($k=1$) and any one error ($t=1$) it reads
$$
2(1+3n)\leq2^n
$$
^hamming-one-qubit

| $n$ | $2(1+3n)$ | $2^n$ | allowed? |
|---|---|---|---|
| 3 | 20 | 8 | no |
| 4 | 26 | 16 | no |
| 5 | 32 | 32 | yes, exactly |
| 6 | 38 | 64 | yes |
| 9 | 56 | 512 | yes |

![[Quantum_Hamming_bound.png]]

the errors grow linearly with $n$ but the room grows exponentially, so the curves cross once, at $n=5$. so there's **no non-degenerate code** encoding one qubit in fewer than five that protects against every single qubit error. (at $n=5$ the space is filled exactly: a "perfect" code)
## only a rule of thumb
not all codes are non-degenerate, so the bound is more a rule of thumb than a hard limit. (when the book was written, no code was known that broke it, even allowing degenerate ones.) a bound that holds for **all** codes is the **quantum Singleton bound** (§12.4.3): a code encoding $k$ qubits in $n$ that corrects errors on any $t$ qubits needs
$$
n\geq4t+k
$$
^quantum-singleton

so the smallest code that encodes one qubit and corrects any single error has $n\geq4+1=5$, and the book soon gives a five qubit code that does it

> [!extra] the Shor code is wasteful
> 9 qubits when 5 would do. it's easy to understand because of its concatenated structure, not because it's efficient. and it's degenerate, so it doesn't need all of the $2^9$ dimensions the counting suggests: only $2\times(1+3\times9)=56$ of the 512 for its 28 errors, and fewer still because $Z_1,Z_2,Z_3$ act the same

> [!exercise] try these
> ① smallest $n$ allowed by the quantum Hamming bound for $k=1$, $t=2$
> ② what does the quantum Singleton bound say for $k=1$, $t=2$?
> ③ for $k=2$, $t=1$, what's the smallest $n$ allowed by the Hamming bound?

> [!answer]-
> ① need $2\big(1+3n+9\binom n2\big)\leq2^n$. $n=9$: $2(1+27+324)=704>512$ ✗. $n=10$: $2(1+30+405)=872\leq1024$ ✓. so $n\geq10$ for a non-degenerate code
> ② $n\geq4\times2+1=9$
> ③ need $4(1+3n)\leq2^n$. $n=6$: $76>64$ ✗. $n=7$: $88\leq128$ ✓. so $n\geq7$

see also [[Shor code]], [[Classical linear codes]]

next: [[Classical linear codes]]
