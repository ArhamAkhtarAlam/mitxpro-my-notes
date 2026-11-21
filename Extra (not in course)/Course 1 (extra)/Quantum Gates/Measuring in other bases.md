#extra #measurement #bloch_sphere #hadamard
**extra** (not in the course as its own topic): real hardware only measures in the $Z$ basis ($|0\rangle$ or $|1\rangle$). to measure anything else, **rotate first, then measure**
## the rule
the chance of outcome $|b\rangle$ is the overlap squared (the **Born rule**):
$$
P(b)=|\langle b|\psi\rangle|^2
$$
^born-rule

to measure in a basis $\{U|0\rangle,U|1\rangle\}$: apply $U^\dagger$, then measure $Z$. the rotation turns the basis you want into the one the machine has

| basis | states | apply before measuring | outcome 0 means |
|---|---|---|---|
| $Z$ | $\|0\rangle,\|1\rangle$ | nothing | $\|0\rangle$ |
| $X$ | $\|+\rangle,\|-\rangle$ | $H$ | $\|+\rangle$ |
| $Y$ | $\|{+i}\rangle,\|{-i}\rangle$ | $S^\dagger$ then $H$ | $\|{+i}\rangle$ |

![[Measuring_in_other_bases.png]]

(top: $Z$, middle: $X$, bottom: $Y$)

> [!important] the one idea
> ==a measurement only sees one axis of the Bloch sphere. to look along $x$ or $y$, turn that axis onto $z$ first==. that's how [[State tomography]] builds the whole Bloch vector

## what each basis sees

| state | $Z$ basis | $X$ basis | $Y$ basis |
|---|---|---|---|
| $\|0\rangle$ | always 0 | 50/50 | 50/50 |
| $\|+\rangle$ | 50/50 | always 0 | 50/50 |
| $\|-\rangle$ | 50/50 | always 1 | 50/50 |
| $\|{+i}\rangle$ | 50/50 | 50/50 | always 0 |

$|+\rangle$ and $|-\rangle$ look **identical** to a $Z$ measurement (both 50/50). they differ only in **relative phase**, and the $X$ basis is what can see it. a **global** phase ($-|\psi\rangle$ vs $|\psi\rangle$) no basis can ever see

## expectation values
repeat many times and average $\pm1$:
$$
\langle X\rangle=P(+)-P(-),\qquad\langle Y\rangle=P(+i)-P(-i),\qquad\langle Z\rangle=P(0)-P(1)
$$
and $(\langle X\rangle,\langle Y\rangle,\langle Z\rangle)$ **is** the Bloch vector. in [[VQE]], the energy is a sum of Pauli strings, so each term is measured in its own rotated basis

> [!exercise] try these
> **1** $|\psi\rangle=\cos\frac\pi8|0\rangle+\sin\frac\pi8|1\rangle$. chance of $+$ in the $X$ basis?
> **2** why does the $Y$ measurement need $S^\dagger$ before $H$?
> **3** a qubit gives 0 every time in $Z$ and 50/50 in $X$ and $Y$. what is it?

> [!answer]-
> **1** $|\langle+|\psi\rangle|^2=\frac12(\cos\frac\pi8+\sin\frac\pi8)^2=\frac12(1+\sin\frac\pi4)\approx0.854$
> **2** $S^\dagger$ turns $|{+i}\rangle$ into $|+\rangle$, then $H$ turns that into $|0\rangle$
> **3** $|0\rangle$ (Bloch vector $(0,0,1)$)

see also [[Bloch sphere]], [[Hadamard Gate]], [[Rotation gates]], [[Projectors]], [[Probability and expectation values]]
