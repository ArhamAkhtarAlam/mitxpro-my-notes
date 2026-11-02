#formula_sheet #fault_tolerance #threshold
every formula from Course 4 Week 2 on one page. formulas that live in a topic note are embedded from there (with a link to its worked example), the extra ones are written out here. each section has a folded **eg.** and an **exercise** (try it first). part of [[Principles of fault tolerance]]
## 1. the threshold theorem
from [[Threshold theorem]]

![[Threshold theorem#^threshold-theorem]]

worked ("what polylog buys you") in [[Threshold theorem#the theorem]]

> [!eg]- vs triple modular redundancy
> TMR needs $p<\frac1{3N}$ ([[Triple modular redundancy#^tmr-break-even]]): $3.3\times10^{-4}$ for 1000 gates, $3.3\times10^{-10}$ for $10^9$. a threshold theorem with $p_{th}=0.01$ says **one** number, $0.01$, works for both. ==that independence of $N$ is the whole point==

> [!exercise] exercise
> the overhead factor is $(\log_{10}\frac N\epsilon)^3$. how many gates for $N=10^6$ and $\epsilon=10^{-4}$? what if you want $\epsilon=10^{-10}$?

> [!answer]-
> $\log_{10}10^{10}=10$, so $10^3N=10^9$ gates. for $\epsilon=10^{-10}$: $\log_{10}10^{16}=16$, $16^3=4096$, so $4.1\times10^9$ gates: a million times more accurate for about 4× the gates
## 2. the encoded NAND gate
from [[Fault-tolerant NAND gate]]

the gate

![[Fault-tolerant NAND gate#^nand-truth]]

3 NANDs + 3 majority gates, wrong only if 2 of the 6 fail

![[Fault-tolerant NAND gate#^nand-fail]]

![[Fault-tolerant NAND gate#^nand-threshold]]

worked ($p=0.01$ and $0.05$) in [[Fault-tolerant NAND gate#the probability of failure]]

> [!eg]- $p=0.02$
> $15(0.02)^2=6\times10^{-3}$, about 3.3× better than one gate

> [!exercise] exercise
> (a) $p=0.1$: is the encoded gate better or worse than one gate? (b) a different construction uses 10 gates per encoded gate. what are its bound and threshold?

> [!answer]-
> (a) $15(0.01)=0.15>0.1$, worse: $0.1$ is above $\frac1{15}=0.067$
> (b) $\binom{10}2=45$, so $p_{\text{fail}}\leq45p^2$ and $p_{th}=\frac1{45}=0.022$
## 3. recursion
from [[Recursive fault tolerance]]

level 2

![[Recursive fault tolerance#^level-two]]

every level

![[Recursive fault tolerance#^recursion-table]]

so $p_{\text{fail}}^{(k)}=\frac{(cp)^{2^k}}c$ (the same as [[Bit flip code#^concatenation]]). the cost: each level replaces every gate by 6 and every wire by 3
$$
\text{gates per logical gate}=6^k\qquad\text{wires per logical bit}=3^k
$$
^recursion-cost

worked ($p=0.01$, levels 0 to 5) in [[Recursive fault tolerance#the probability of failure]]

> [!eg]- $p=0.02$, $c=15$ ($cp=0.3$)
>
> | level $k$ | gates $6^k$ | $p_{\text{fail}}$ |
> |---|---|---|
> | 1 | 6 | $6\times10^{-3}$ |
> | 2 | 36 | $5.4\times10^{-4}$ |
> | 3 | 216 | $4.4\times10^{-6}$ |
> | 4 | 1296 | $2.9\times10^{-10}$ |
> | 5 | 7776 | $1.2\times10^{-18}$ |
>

> [!exercise] exercise
> $p=0.03$, $c=15$. how many levels to get below $10^{-12}$, and how many gates and wires per logical bit does that take?

> [!answer]-
> $cp=0.45$: level 4 gives $\frac{0.45^{16}}{15}=1.9\times10^{-7}$, level 5 gives $\frac{0.45^{32}}{15}=5.3\times10^{-13}$. so **5 levels**: $6^5=7776$ gates per logical gate, $3^5=243$ wires per bit
## 4. the classical thresholds
from [[Threshold theorem#the classical thresholds]]

the upper bound for gates with $k$ inputs
$$
p_{th}\leq\frac12-\frac1{2\sqrt k}
$$
^k-input-bound

it creeps up to $\frac12$ as $k\to\infty$, and at $\frac12$ a gate just outputs noise

> [!eg]- $k=3$
> $\frac12-\frac1{2\sqrt3}=0.5-0.289=0.211$. the Hajek and Weller 3 input threshold ($\frac16=0.167$) sits under it, as it must

> [!exercise] exercise
> how many inputs $k$ would a gate need for the bound to reach $0.45$?

> [!answer]-
> $\frac1{2\sqrt k}=0.05$, so $\sqrt k=10$, $k=100$

see also [[Course 4 Week 1 formulas]]

week hub: [[Principles of fault tolerance]]
