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
## why the order lets you factor
if $r$ is **even**, then $a^r-1\equiv0\pmod N$ can be split up
$$
a^r-1=(a^{r/2}-1)(a^{r/2}+1)\equiv0\pmod N
$$
so $N$ divides the product, which means $N$ shares a factor with $a^{r/2}-1$ or $a^{r/2}+1$. [[Modular arithmetic#gcd|gcd]] finds it

eg. $a=2,\ N=15,\ r=4$: $a^{r/2}=4$
$$
\gcd(4-1,15)=3\qquad\gcd(4+1,15)=5\qquad3\times5=15\ ✅
$$
> [!warning] when it doesn't work
> - $r$ is **odd** → can't split it in half
> - $a^{r/2}\equiv-1\pmod N$ → the gcd just gives $1$ or $N$
>
> then just pick a different $a$ and try again. at least half of all $a$ values work, so it doesn't take many tries

```mermaid
flowchart TD
    R["order r"] --> E{"r even?"}
    E -- "no" --> T["try another a"]
    E -- "yes" --> M{"a^(r/2) ≡ −1 mod N?"}
    M -- "yes" --> T
    M -- "no" --> F["factors = gcd(a^(r/2) ± 1, N)"]
```
(from the order to the factors)

## how the quantum part finds $r$
1. make the gate $U|y\rangle=|a\,y\bmod N\rangle$ (multiply by $a$, see [[Modular Exponentiation]])
2. its [[Eigenvalues and eigenvectors|eigenvalues]] are $e^{2\pi i\,s/r}$ for $s=0,1,\ldots,r-1$, so $r$ is hiding in the **phase**
3. [[Quantum Phase Estimation]] measures a phase $\approx\frac sr$ for a random $s$
4. turn the measured number into a fraction to read off $r$

eg. with 8 counting qubits and $N=15,\ a=2$ you measure $0$, $64$, $128$ or $192$ (out of $256$)
- $\frac{64}{256}=\frac14$ → $r=4$ ✅
- $\frac{192}{256}=\frac34$ → $r=4$ ✅
- $\frac{128}{256}=\frac12$ → looks like $r=2$, but $2^2=4\not\equiv1$, so run again
- $0$ → tells you nothing, run again

see [[Shor's algorithm#Worked example (factoring 15)]] for the full thing
