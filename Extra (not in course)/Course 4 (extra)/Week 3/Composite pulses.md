#extra #systematic_noise #error_mitigation #rotation
**extra** (not covered in detail here): fixing **systematic** errors (the same every time) by replacing one pulse with a cleverly chosen string of pulses whose mistakes cancel. the partner of [[Dynamical decoupling]], which fights **random** noise ([[Quantum error mitigation]])
## the problem
a qubit gate is a rotation by an angle $\theta$, made by a pulse whose area sets $\theta$. if the amplitude is miscalibrated by a fraction $\varepsilon$, **every** pulse rotates by $\theta(1+\varepsilon)$ instead. for a $\pi$ pulse meant to flip $|0\rangle\to|1\rangle$:
$$
P(|1\rangle)=\sin^2\frac{\pi(1+\varepsilon)}2=\cos^2\frac{\pi\varepsilon}2\approx1-\left(\frac{\pi\varepsilon}2\right)^2
$$
a 5% error gives $P\approx0.994$. small, but it's the **same** small error every gate, so it adds up coherently over many gates (error grows like $N^2$ in probability, not $N$)

> [!important] the one idea
> ==a fixed error can be cancelled by design: choose pulse angles and phases so the first-order (and higher) mistakes of the pieces undo each other==, the same way a [[Rotary echo]] or spin echo cancels a slow drift

## the simplest: $90_x\,180_y\,90_x$
instead of one $\pi$ pulse about $x$: a $\frac\pi2$ about $x$, a $\pi$ about $y$, a $\frac\pi2$ about $x$ (all with the same $\varepsilon$). on the [[Bloch sphere]], the overshoot of the first pulse is swung round by the $y$ pulse so the last pulse cancels it. the chance of landing in $|1\rangle$ goes from $1-O(\varepsilon^2)$ to $1-O(\varepsilon^4)$

catch: it's robust for **starting in $|0\rangle$** only ("point to point"). as a gate on any input it's not the same unitary. for that you need a fully compensating sequence

## BB1: a robust gate
to do $\theta$ about $x$ robustly (Wimperis):
$$
\theta_0\ \ \pi_{\phi_1}\ \ 2\pi_{3\phi_1}\ \ \pi_{\phi_1},\qquad\phi_1=\arccos\left(-\frac\theta{4\pi}\right)
$$
^bb1

(subscripts are the phase = axis in the $xy$ plane). for $\theta=\pi$: $\phi_1\approx104.5°$, $3\phi_1\approx313.4°$. the extra pulses would do **nothing** if perfect ($\pi\,2\pi\,\pi$ = full turns), but with errors they exactly cancel the main pulse's error to second order, for **any** starting state

![[Composite_pulse_robustness.png]]

| sequence | $P(\|1\rangle)$ at $\varepsilon=10\%$ | works as a gate? |
|---|---|---|
| single $\pi$ | 0.976 | yes |
| $90_x180_y90_x$ | 0.9994 | no, only from $\|0\rangle$ |
| BB1 | 0.99999 | yes |

## other errors, other sequences
- **off-resonance** (the drive frequency is a bit off the qubit's): CORPSE
- both at once: combined sequences, or numerically optimized pulses (optimal control, DRAG for leakage to $|2\rangle$ in [[Superconducting qubits|transmons]])
- cost: longer sequences take more time, so more [[Amplitude damping channel|T₁]]/[[Dephasing and the filter function|T₂]] decay. worth it only when systematic errors dominate

> [!exercise] try these
> **1** a single $\pi$ pulse with $\varepsilon=2\%$. chance of ending in $|1\rangle$?
> **2** why does a fixed error hurt more than a random one of the same size over many gates?
> **3** what do the extra pulses in BB1 do if there's no error?

> [!answer]-
> **1** $\cos^2(0.01\pi)\approx0.9990$
> **2** fixed errors add up in angle ($N\varepsilon$, so error $\propto N^2\varepsilon^2$); random ones partly cancel (a random walk, $\propto N\varepsilon^2$)
> **3** nothing: $\pi+2\pi+\pi$ about various axes multiplies to the identity (up to a sign)

see also [[Quantum error mitigation]], [[Rotary echo]], [[Dynamical decoupling]], [[Rabi oscillation]], [[Gate fidelity]]
