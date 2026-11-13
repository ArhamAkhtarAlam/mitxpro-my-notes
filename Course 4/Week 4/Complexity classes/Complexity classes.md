#complexity #complexity_class
we have **problems** ([[Languages]]) and **models of computing** ([[Circuit model|circuits]], [[Turing machine|Turing machines]], random, quantum). put them together and you get **complexity classes**: groups of problems that all have about the same cost. part of [[Computational complexity]]

## a first example: DTIME
**deterministic time**. a language $L$ is in $\text{DTIME}(f(n))$ if there's a Turing machine $M$ such that, for every input $x$
- $M(x)$ always halts with the **right answer**: accept if $x\in L$, reject if $x\notin L$
- and it takes **fewer than $f(|x|)$ steps**

$$
L\in\text{DTIME}\big(f(n)\big)\iff\exists M:\ M(x)=\begin{cases}\text{accept}&x\in L\\\text{reject}&x\notin L\end{cases}\ \text{ in }<f(|x|)\text{ steps}
$$
^dtime

> [!eg]
> $\text{DTIME}(100n^3)$ = the languages you can decide in at most $100n^3$ steps on an $n$ bit input. for $n=10$ that's $100\,000$ steps

## time and memory
a computer has two budgets: **time** (number of steps) and **memory** (bits it can store). they can scale very differently

> [!eg] a made up problem
>
> | variables $n$ | memory | steps |
> |---|---|---|
> | 2 | 100 | 4 |
> | 3 | 1000 | 9 |
> | 4 | 10 000 | 16 |
>
> the steps grow like $n^2$ (polynomial), but the memory grows like $10^n$ (exponential): the memory is what kills it

the class of problems that need only **polynomial memory**, however long they take, is **PSPACE**. it's huge: it contains everything below, including games like $n\times n$ chess and Go

![[Complexity_hierarchy.png]]

### efficient isn't the same as fast
multiplying two $n$ bit numbers by long multiplication takes about $n^2$ steps: every bit of one times every bit of the other

> [!eg] $3\times3=9$ in binary
> $11\times11=11+110=1001$: two bits each, so $2^2=4$ bit products. with 3 bits it's $3^2=9$ bit products, and so on

so multiplication is in P. but for $n=10^{100}$ bits that's $10^{200}$ steps, which would never finish. "efficient" only means it **scales** better: an exponential algorithm on the same input would need about $2^{10^{100}}$ steps

## the main classes

| class | computer | must be right | in time |
|---|---|---|---|
| **P** | deterministic | always | polynomial: $\text{DTIME}(n^c)$ for some constant $c$ |
| **BPP** | randomized ([[Randomized and quantum computation]]) | with probability $\ge\frac23$ | polynomial |
| **BQP** | quantum (uniform circuit family) | with probability $\ge\frac23$ | polynomial |
| **[[NP]]** | nondeterministic ([[Nondeterminism]]) | a "yes" has a short proof you can check | polynomial |
| **PSPACE** | deterministic | always | any, but polynomial **memory** |

^class-table

(the $\frac23$ isn't special: repeat and take the majority to push the error as low as you like, see the box at the bottom)

## how they fit together
$$
\text{P}\subseteq\text{BPP}\subseteq\text{BQP}\subseteq\text{PSPACE}\qquad\text{P}\subseteq\text{NP}\subseteq\text{PSPACE}
$$
^containments

**P** is the weakest: everything else contains it. a random computer can ignore its random bits (P ⊆ BPP), and a quantum computer can simulate coin flips (BPP ⊆ BQP). at the top, PSPACE contains them all: you can try every certificate one by one, or add up a quantum circuit's amplitudes one path at a time, reusing the same polynomial memory ([[Quantum vs classical complexity]]). but the two branches, NP and BQP, look like they may be **incomparable**: problems in NP that aren't in BQP, and the other way round

![[Complexity_class_map.png]]

### what people believe (none of it proven)

| conjecture | why people think so |
|---|---|
| P ≠ NP | finding a solution seems much harder than checking one |
| **P = BPP** | pseudo random numbers seem to work as well as real ones (below) |
| BPP ≠ BQP | the whole reason to build a quantum computer: it can do things a random classical one can't |

> [!important] P = BPP? the pseudo randomness argument
> your computer's random numbers come from a **pseudo random number generator**: a deterministic sequence. there **is** a pattern in it, but finding that pattern seems to be computationally too hard (the same intuition as P ≠ NP: some patterns exist but can't be extracted efficiently). so a program fed pseudo random numbers should do just as well as one fed real randomness. ==randomness probably doesn't add power to classical computers, but quantum probably does==. there are theorems pointing that way, but it's still a conjecture

## why only "polynomial"?
the classes only ask whether the time is **polynomial** or not. $n^2$, $n^3$ and $100n^3$ all count as fast, and only exponential counts as slow

![[Polynomial_vs_exponential.png]]

that's crude: in practice $n^2$ vs $n^3$ matters a lot. but it makes the classes **robust**: they don't depend on details like the exact gate set or the machine model, because switching model only costs a polynomial factor, and a polynomial of a polynomial is still a polynomial. finer versions of the same tools give finer answers

> [!extra]- why BPP and BQP use $\frac23$
> any constant above $\frac12$ works. if one run is right with probability $\frac23$, run it $k$ times and take the majority: the chance the majority is wrong falls like $e^{-ck}$ (a Chernoff bound, the same counting as the [[Bit flip code]]). about 50 runs already gets the error below one in a million, a constant factor that doesn't change "polynomial"

> [!exercise] try these
> ① a problem is in $\text{DTIME}(n^2)$. is it in $\text{DTIME}(n^3)$? is it in P?
> ② an algorithm takes $2^{n/100}$ steps. is it polynomial? which is bigger at $n=1000$, $2^{n/100}$ or $n^2$? at $n=10\,000$?
> ③ why is P ⊆ BPP?
> ④ if someone proved BPP = BQP, what would it mean for quantum computers?
> ⑤ in the made up problem above, how much memory do 10 variables need, and how many steps?

> [!answer]-
> ① yes ($n^2<n^3$, so the same machine works) and yes ($c=2$)
> ② no, it's exponential. $n=1000$: $2^{10}=1024$ vs $10^6$, so $n^2$ is bigger. $n=10\,000$: $2^{100}\approx10^{30}$ vs $10^8$: the exponential wins eventually, which is all the classes care about
> ③ a deterministic algorithm is a randomized one that never reads its random bits, and it's right with probability 1 ≥ $\frac23$
> ④ every problem a quantum computer solves in polynomial time could also be solved by a classical randomized computer in polynomial time: no exponential [[Quantum advantage|quantum advantage]] for yes/no problems (polynomial speed ups like Grover's could still exist)
> ⑤ memory $10^{10}$, steps $10^2=100$. the steps are trivial, the memory is ten billion units

next: [[NP]], then [[NP-complete]], [[Quantum circuit evaluation]] and [[Quantum vs classical complexity]]

see also [[Big O notation]], [[Nondeterminism]], [[Randomized and quantum computation]]

week hub: [[Computational complexity]]
