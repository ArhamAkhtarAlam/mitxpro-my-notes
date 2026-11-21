#mechanics #angular_momentum #collision #worked_example
## a rod with no pivot
a rod lying on a **smooth** table is free: when something hits it, it both moves and spins. nothing outside acts sideways, so three things can be kept. part of [[Rotational mechanics]]
1. **linear momentum**: $mu=mv+Mv_\text{cm}$
2. **angular momentum** about any fixed point, usually where the centre of mass is at the moment of the hit ([[Angular momentum#^l-i-omega]])
3. **kinetic energy**, only if the collision is elastic ([[Elastic collisions]])

after the hit, the centre of mass goes in a straight line at $v_\text{cm}$, and the rod spins about it at $\omega$. it's **not** pure rotation, so $v_\text{cm}\neq\frac L2\omega$

about a point that isn't the centre of mass, the angular momentum is the spin plus the "orbital" part:
$$
L=I_\text{cm}\,\omega+Mv_\text{cm}\,r_\perp
$$
^l-about-point

> [!important] the one idea
> ==a free body after a hit: the centre of mass moves like a particle (momentum), the body spins about the centre of mass (angular momentum about it), and for elastic hits the energy splits into $\frac12Mv_\text{cm}^2+\frac12I_\text{cm}\omega^2$==

## a ball hits the end and stops
a 12 kg rod, 2 m long, is hit at one end by a ball moving at 20 m/s ⊥ to the rod. the collision is elastic and the ball stops dead. find the ball's mass, $v_\text{cm}$ and $\omega$. ($I_\text{cm}=\frac{12\times2^2}{12}=4$ kg m², the end is 1 m from the centre)

![[Free_rod_hit_animation.png]]

$$
\begin{aligned}
\text{momentum: }m(20)&=12\,v_\text{cm}\\
\text{angular momentum about the centre: }m(20)(1)&=4\,\omega\\
\text{energy: }\tfrac12m(20)^2&=\tfrac12(4)\omega^2+\tfrac12(12)v_\text{cm}^2
\end{aligned}
$$

from the first two, $v_\text{cm}=\frac{5m}{3}$, $\omega=5m$. into the third:
$$
200m=2(25m^2)+6\cdot\frac{25m^2}{9}=\frac{200m^2}{3}\ \Rightarrow\ m=3\ \text{kg},\quad\omega=15\ \text{rad/s},\quad v_\text{cm}=5\ \text{m/s}
$$

> [!eg] the same problem about the far end
> take the axis at the far end of the rod (2 m from the ball's line, 1 m from the centre). [[#^l-about-point]]: $m(20)(2)=4\omega+12v_\text{cm}(1)$. with $m=3$: $120=60+60$ ✓. any fixed point works, as long as you include the $Mv_\text{cm}r_\perp$ part

## how far does it go while turning 90°?
hit a free uniform rod ⊥ at one end with **any** impulse $J$: $v_\text{cm}=\frac JM$ and $\omega=\frac{J\frac L2}{ML^2/12}=\frac{6J}{ML}$, so $\frac{v_\text{cm}}{\omega}=\frac L6$. a quarter turn takes $\frac{\pi/2}{\omega}$, and in that time the centre goes
$$
s=v_\text{cm}\frac{\pi}{2\omega}=\frac{\pi L}{12}
$$
whatever hit it and however hard. (for the 2 m rod: $0.52$ m)

## the hockey puck that stops
a stick ($M$, length $L$) lies on frictionless ice. a puck $m$ at speed $v$ hits it elastically at distance $d$ from the centre. what $m$ makes the puck stop?

kept: linear momentum, angular momentum, and KE (elastic)
$$
\begin{aligned}
mv&=Mv_\text{cm}\\
mvd&=\frac{ML^2}{12}\omega\\
\tfrac12mv^2&=\tfrac12Mv_\text{cm}^2+\tfrac12\frac{ML^2}{12}\omega^2
\end{aligned}
$$

put $v_\text{cm}=\frac{mv}{M}$ and $\omega=\frac{12mvd}{ML^2}$ in the energy:
$$
mv^2=\frac{m^2v^2}{M}+\frac{12m^2v^2d^2}{ML^2}\ \Rightarrow\ m=\frac{M}{1+\frac{12d^2}{L^2}}
$$
(at the centre, $d=0$: $m=M$, the equal masses swap rule. at the end, $d=\frac L2$: $m=\frac M4$, matching the 12 kg rod and 3 kg ball)

## a ball sticks to the end
now a 2 kg ball at 20 m/s hits the end of the same 12 kg, 2 m rod and **sticks**. the centre of mass of rod + ball is no longer the rod's centre:
$$
\text{from the rod's centre: }\frac{12(0)+2(1)}{14}=\frac17\ \text{m towards the ball (}\tfrac67\text{ m from the ball)}
$$

momentum: $2(20)=14\,v_\text{cm}$, so $v_\text{cm}=\frac{20}{7}$ m/s. angular momentum about the new centre of mass:
$$
\begin{aligned}
2(20)\left(\tfrac67\right)&=\left[\frac{12(2^2)}{12}+12\left(\tfrac17\right)^2+2\left(\tfrac67\right)^2\right]\omega\\
\frac{240}{7}&=\left[4+\frac{12}{49}+\frac{72}{49}\right]\omega=\frac{40}{7}\omega\\
\omega&=6\ \text{rad/s}
\end{aligned}
$$

(the rod's part uses the parallel axis theorem: $I=I_\text{cm}+Md^2$, see [[Moment of inertia]])

## a rod picks up a particle
two small balls A and B (mass $m$ each) on the ends of a light rod of length $L$ slide at $v_0$, ⊥ to the rod. a particle P (mass $m$) sits at rest in A's path and sticks to it. find the new $v_\text{cm}$, $\omega$, and the speeds of A and B

![[Rod_picks_up_particle_animation.png]]

**centre of mass**: $2m$ at A, $m$ at B, so it's $\frac L3$ from A. momentum: $2mv_0=3mv_\text{cm}$
$$
v_\text{cm}=\frac{2v_0}{3}
$$

**angular momentum** about the point where the new centre of mass is (A is $\frac L3$ from it, B is $\frac{2L}{3}$, on opposite sides, P at A is still):
$$
\begin{aligned}
mv_0\frac{2L}{3}-mv_0\frac L3&=\left[2m\left(\frac L3\right)^2+m\left(\frac{2L}{3}\right)^2\right]\omega\\
\frac{mv_0L}{3}&=\frac{6mL^2}{9}\omega\ \Rightarrow\ \omega=\frac{v_0}{2L}
\end{aligned}
$$

**speeds** right after: each end is $v_\text{cm}\pm\omega r$
$$
v_B=\frac{2v_0}{3}+\frac{v_0}{2L}\cdot\frac{2L}{3}=v_0,\qquad v_A=\frac{2v_0}{3}-\frac{v_0}{2L}\cdot\frac L3=\frac{v_0}{2}
$$

B carries on at $v_0$ for that instant: the hit only shares A's momentum with P ($mv_0=2m\cdot\frac{v_0}{2}$ ✓), and the rod then starts turning

> [!exercise] try these
> **1** a free rod is hit ⊥ at its centre. does it spin?
> **2** in the hockey puck problem, $L=1$ m and $d=0.25$ m. what $m$ stops the puck?
> **3** a 6 kg, 1 m rod on ice is hit at one end, receiving an impulse of 3 N s. find $v_\text{cm}$ and $\omega$

> [!answer]-
> **1** no: zero torque about the centre, it just slides
> **2** $m=\frac{M}{1+12/16}=\frac47M$
> **3** $v_\text{cm}=0.5$ m/s, $\omega=\frac{3(0.5)}{6/12}=3$ rad/s ($\frac{v_\text{cm}}{\omega}=\frac16$ ✓)

see also [[Angular momentum]], [[Coefficient of restitution]], [[Centre of mass]]

hub: [[Rotational mechanics]]
