#math #entanglement #probability
a way to say one probability list is **more spread out** (more mixed, more uncertain) than another. it's what decides which entangled states can be turned into which ([[LOCC]], [[Entanglement as a resource]])
## the definition
take two lists $x$ and $y$ of $n$ numbers with the same total (eg. probabilities adding to 1). sort each **biggest first**: $x^\downarrow$, $y^\downarrow$. then $x$ is **majorized by** $y$, written $x\prec y$, if
$$
\sum_{i=1}^{k}x^\downarrow_i\le\sum_{i=1}^{k}y^\downarrow_i\quad\text{for every }k,\qquad\text{with equality at }k=n
$$
^majorization

in words: the biggest entry of $y$ is at least as big, the biggest two of $y$ add up to at least as much, and so on. $y$ is more **concentrated**, $x$ more **even**

> [!important] the one idea
> ==$x\prec y$ means $x$ can be made from $y$ by evening things out (moving probability from a bigger entry to a smaller one)==, so $x$ is "more mixed". draw the running sums: $y$'s curve is never below $x$'s

![[Majorization_curves.png]]

> [!eg] checking
> $x=(0.4,0.3,0.2,0.1)$, $y=(0.6,0.3,0.1,0)$. running sums: $x$: 0.4, 0.7, 0.9, 1. $y$: 0.6, 0.9, 1, 1. every one of $y$'s is $\ge$, so $x\prec y$
>
> $(0.5,0.5,0)$ vs $(0.6,0.2,0.2)$: sums 0.5, 1.0 vs 0.6, 0.8. the first says the second is bigger, the next says the opposite: **neither** majorizes the other. unlike numbers, two lists don't have to be comparable

## facts
- for any probability list $p$ of length $n$: $\left(\frac1n,\dots,\frac1n\right)\prec p\prec(1,0,\dots,0)$. uniform is the most mixed, certain is the least
- $x\prec y$ exactly when $x=Dy$ for a **doubly stochastic** matrix $D$ (rows and columns add to 1, a mix of permutations): "averaging" $y$
- **entropy goes down the order**: $x\prec y\Rightarrow H(x)\ge H(y)$ ([[Shannon entropy]]). the converse is false: incomparable lists still have entropies
- for density matrices: the diagonal of $\rho$ (in any basis) is majorized by its eigenvalues. so measuring in the eigenbasis gives the least random outcomes ([[Von Neumann entropy]])

## where it's used: entanglement
Nielsen's theorem ([[LOCC#^nielsen-locc]]): a pure state can be turned into another by LOCC exactly when the first one's squared Schmidt coefficients are majorized by the second's ([[Schmidt decomposition]])

> [!extra]- catalysis
> sometimes $x\not\prec y$ but $x\otimes c\prec y\otimes c$ for some extra state $c$ that you get back afterwards (a **catalyst**). eg. $x=(0.4,0.4,0.1,0.1)$, $y=(0.5,0.25,0.25,0)$: $0.4+0.4=0.8>0.75$, so no. but with $c=(0.6,0.4)$ the running sums of $x\otimes c$ are 0.24, 0.48, 0.64, 0.80, 0.86, 0.92, 0.96, 1 and those of $y\otimes c$ are 0.30, 0.50, 0.65, 0.80, 0.90, 1, 1, 1: it works. borrowing an entangled pair lets you do a conversion that was impossible without it

> [!exercise] try these
> **1** is $(0.5,0.3,0.2)\prec(0.7,0.2,0.1)$?
> **2** is $(0.6,0.4)\prec(0.5,0.5)$?
> **3** list any $p$ of length 3 that is not comparable with $(0.5,0.25,0.25)$

> [!answer]-
> **1** sums 0.5, 0.8 vs 0.7, 0.9: yes
> **2** no, $0.6>0.5$. it's the other way round: uniform is majorized by everything
> **3** eg. $(0.45,0.45,0.1)$: 0.45 < 0.5 but 0.9 > 0.75

see also [[Math]], [[Probability and expectation values]], [[Entanglement entropy]], [[Schmidt number]]
