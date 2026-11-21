#mechanics #collision #spring #worked_example
## the problem
on a smooth floor, block A ($m$, speed $v$) hits block B ($m$) elastically. B is joined by a spring $k$ to block C ($m$), at rest. find the speeds of B and C at maximum compression, the maximum compression, and describe the motion after. part of [[Work, energy and power]]

![[Two_blocks_spring_collision.png]]

## step 1: the hit
A and B are equal masses colliding elastically, and the spring hasn't had time to do anything yet, so they swap velocities ([[Elastic collisions]]): **A stops**, B moves off at $v$, C is still at rest

## step 2: maximum compression
B is faster than C, so the gap closes and the spring squashes. once C gets faster than B, the gap opens again. so the squeeze is **biggest at the moment their speeds are equal**, $v_B=v_C=v'$

nothing outside pushes sideways on B + C, so their momentum is kept:
$$
mv=mv'+mv'\ \Rightarrow\ v'=\frac v2
$$

and energy (the spring is part of the system, no friction):
$$
\begin{aligned}
\tfrac12mv^2&=\tfrac12mv'^2+\tfrac12mv'^2+\tfrac12kx^2\\
\tfrac12mv^2&=\tfrac14mv^2+\tfrac12kx^2\\
x_\text{max}&=v\sqrt{\frac{m}{2k}}
\end{aligned}
$$
^max-compression

> [!important] the one idea
> ==two bodies joined by a spring: the spring is most squashed (or stretched) when they move at the **same** velocity, and then the KE that's left is the centre of mass's KE, which the spring can't touch==

## why equal speeds? (the proof)
take B's speed as $v_1$, C's as $v_2$. momentum: $v_1+v_2=v$, so $v_2=v-v_1$. energy:
$$
\begin{aligned}
\frac{kx^2}{m}&=v^2-v_1^2-(v-v_1)^2=2vv_1-2v_1^2\\
\frac{d}{dv_1}\left(\frac{kx^2}{m}\right)&=2v-4v_1=0\ \Rightarrow\ v_1=\frac v2=v_2
\end{aligned}
$$

the spring energy is biggest exactly when the KE is smallest, and for a fixed momentum the KE is smallest when both move together

## step 3: after that
the pair drifts on at the centre of mass speed $\frac v2$ forever, and **relative** to that, B and C oscillate in and out: [[Simple harmonic motion]]. each block obeys $m\ddot x=\mp kx$ with $x$ the stretch, and the stretch itself oscillates like a single mass $\mu$ on the spring, where $\mu$ is the **reduced mass**:
$$
T=2\pi\sqrt{\frac{\mu}{k}},\qquad\mu=\frac{m_1m_2}{m_1+m_2}
$$
^reduced-mass-period

here $\mu=\frac m2$, so $T=2\pi\sqrt{\frac{m}{2k}}$. the speeds of B and C cross at $\frac v2$ twice per period: once at max squeeze, once at max stretch

> [!eg] the energy split
> with $v=2$ m/s, $m=1$ kg: total KE 2 J. at max squeeze, the pair carries $\tfrac12(2m)(1)^2=1$ J of centre of mass KE, so only **1 J** goes into the spring. half the energy is always locked up in the drift

> [!exercise] try these
> ① same set up, but C has mass $2m$. speed at max compression?
> ② in the main problem, how fast are B and C going when the spring is back at its natural length for the first time?
> ③ $m=0.5$ kg, $k=100$ N/m. period of the oscillation?

> [!answer]-
> ① $mv=3mv'$ → $v'=\frac v3$; $\tfrac12mv^2=\tfrac12(3m)\frac{v^2}{9}+\tfrac12kx^2$ → $x=v\sqrt{\frac{2m}{3k}}$
> ② they've swapped: B at 0, C at $v$ (like an elastic collision through the spring)
> ③ $\mu=0.25$ kg, $T=2\pi\sqrt{0.0025}=0.1\pi\approx0.31$ s

see also [[Perfectly inelastic collisions]], [[Centre of mass]]

related beyond class 11: [[FTIR]] and [[Raman spectroscopy]]: a chemical bond is two atoms on a spring, vibrating with the same reduced mass $\mu$

hub: [[Work, energy and power]]
