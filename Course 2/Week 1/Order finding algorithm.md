#order_finding #shors_algorithm
the problem at the heart of [[Shor's algorithm]]
## the problem
given $a$ and $N$, find the **order** $r$: the smallest number where
$$
a^r \equiv 1 \pmod N
$$
eg. $a=2,\ N=15$: $2^1=2,\ 2^2=4,\ 2^3=8,\ 2^4=16\equiv1$ so $r=4$ (see [[Modular Exponentiation]])
## classical vs quantum
- classically this is really slow for big $N$
- a quantum computer can do it fast using [[Modular Exponentiation]] + the [[Quantum Fourier Transform]] (together this is [[Quantum Phase Estimation]]). that quantum part is what makes [[Shor's algorithm]] fast
