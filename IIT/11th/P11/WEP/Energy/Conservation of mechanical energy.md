#mechanics #energy #spring #worked_example
## when energy is kept
some forces store the work they do and give it back: **gravity** and **springs**. their work only depends on where you start and end, not the path, so it can be written as minus a change in **potential energy** $U$ ([[Potential energy]]):
$$
U_\text{gravity}=mgh\qquad U_\text{spring}=\tfrac12kx^2
$$
^potential-energies

($x$ = how far the spring is stretched or squashed from its natural length). if only these forces do work (normal forces and tensions that do zero work are fine), the [[Work-energy theorem]] becomes
$$
K_1+U_1=K_2+U_2
$$
^energy-conservation

and with friction, the friction work is an energy **loss**: $K_1+U_1=K_2+U_2+|W_f|$. part of [[Work, energy and power]]

> [!important] the one idea
> ==pick a zero for $U$, write total energy at the start = total energy at the end (+ anything friction ate), and you never need the forces in between==

## a spring between two walls
a spring of natural length $\ell$ is attached between two walls that are $\ell+l_1+l_2$ apart (stretched $l_1$ at one end and $l_2$ at the other to reach them)
- stretch: $\Delta x=l_1+l_2$
- the spring pulls **each** wall inwards with $T=k(l_1+l_2)$ (one spring, one tension)
- stored energy: $\tfrac12k(l_1+l_2)^2$

## two springs on a ring
two blocks of mass $m$ slide on a smooth **horizontal** circular track of radius $R$, with two identical springs ($k$) between them around the ring. both blocks are pulled back through an angle $\theta$ (from Q, Q′ to P, P′) so that each spring is stretched or squashed by an arc $R\theta$, then released. speed when they're back at Q, Q′?

the track is horizontal, so gravity does nothing:
$$
\begin{aligned}
\tfrac12k(R\theta)^2+\tfrac12k(R\theta)^2+0&=0+\tfrac12mv^2+\tfrac12mv^2\\
kR^2\theta^2&=mv^2\\
v&=R\theta\sqrt{\frac km}
\end{aligned}
$$

## down a curve into a spring
a block starts at rest at height $H$ on a smooth curved track and slides down to a level part at height $\frac H2$, where it runs into a spring. max compression?

take $U=0$ on the level part. all the gravitational energy it loses ends up in the spring (it's momentarily stopped at max compression):
$$
\begin{aligned}
mg\frac H2&=\tfrac12kx^2\\
x&=\sqrt{\frac{mgH}{k}}
\end{aligned}
$$

## a rough patch and a spring
a block slides from rest down a smooth curve, from 2 m high, onto a smooth floor. on the floor there's a 2 m rough strip ($\mu_k=0.5$), and past it, on the smooth part, a spring against a wall. how much rough floor does it cross before it stops?

the spring just bounces it back (storing and returning energy, no loss), so friction has to eat **all** of $mgh$:
$$
\begin{aligned}
mgh&=\mu_kmg\,d\\
d&=\frac{h}{\mu_k}=\frac{2}{0.5}=4\ \text{m}
\end{aligned}
$$

4 m = across the strip (2 m), into the spring and back, then back across the strip (2 m): it stops **exactly** at the near edge of the rough part. ($m$ and $k$ don't matter)

## a block placed gently on a pan
a pan of mass $m$ sits on a spring ($k$), already squashed by $\frac{mg}{k}$. a block of the same mass $m$ is put on it **gently** (zero speed) and let go. how far down does the pan go?

the new rest point is another $\frac{mg}{k}$ down, but the pan doesn't stop there: it arrives with speed and overshoots

![[Block_on_pan_animation.png]]

let $y$ = how far it goes down, at the lowest point everything is still again. the pan + block ($2m$) lose $2mgy$ of gravitational energy, and the spring goes from squashed $\frac{mg}{k}$ to $\frac{mg}{k}+y$:
$$
\begin{aligned}
2mgy&=\tfrac12k\left(y+\frac{mg}{k}\right)^2-\tfrac12k\left(\frac{mg}{k}\right)^2\\
2mgy&=\tfrac12ky^2+mgy\\
y&=\frac{2mg}{k}
\end{aligned}
$$

twice the shift of the rest point: it oscillates about the new rest point with amplitude $\frac{mg}{k}$ ([[Simple harmonic motion]])

> [!eg] a load dropped onto a spring always overshoots
> put a load on a spring gently and let go: the max stretch is **twice** the stretch it would settle at. that's why sudden loads are twice as bad as slow ones for bridges and ropes

> [!exercise] try these
> **1** a 0.2 kg ball is pressed 10 cm into a spring ($k=200$ N/m) and fired straight up. how high does it go above the release point?
> **2** in the curve problem, what if the level part were at height $\frac H4$?
> **3** in the rough patch problem, what if the drop were 3 m instead?

> [!answer]-
> **1** $\tfrac12(200)(0.1)^2=1$ J $=mgh$ → $h=\frac{1}{0.2\times10}=0.5$ m
> **2** it drops $\frac{3H}{4}$: $x=\sqrt{\frac{3mgH}{2k}}$
> **3** $d=3/0.5=6$ m: across (2), back (2), across again (2): it stops at the **far** edge, next to the spring side

see also [[Leaving a circular track]], [[Chain sliding off a table]], [[Perfectly inelastic collisions]]

related beyond class 11: [[Hamiltonian]] (the quantum version of K + U) and [[Particle in a box]], [[AFM]] (the cantilever is a spring)

hub: [[Work, energy and power]]
