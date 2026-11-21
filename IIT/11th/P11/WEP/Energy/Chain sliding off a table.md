#mechanics #energy #friction #worked_example
## the problem
a uniform chain, mass $M$, length $L$, lies on a rough table ($\mu_k=\mu$) with **a third** of it hanging over the edge. it starts to slide. what's its KE just as the last bit leaves the table? part of [[Work, energy and power]]

the chain's parts are at different heights and the friction changes as it slides, so this needs integrals. energy balance ([[Conservation of mechanical energy]]):
$$
\text{PE lost}=\text{KE gained}+\text{work done against friction}
$$

![[Chain_off_table_animation.png]]

take $U=0$ at the table top. mass per length: $\frac ML$

## PE at the start and the end
**start**: the hanging third, mass $\frac M3$, has its centre $\frac L6$ below the table (a piece $dx$ at depth $x$ has $dU=-\frac ML g\,x\,dx$):
$$
U_1=-\int_0^{L/3}\frac MLg\,x\,dx=-\frac MLg\cdot\frac{L^2}{18}=-\frac{MgL}{18}
$$

**end**: the whole chain hangs, centre at $\frac L2$ below: $U_2=-\frac{MgL}{2}$

$$
\text{PE lost}=-\frac{MgL}{18}+\frac{MgL}{2}=\frac{8MgL}{18}=\frac{4MgL}{9}
$$

## the friction
after the chain has slid a distance $x$, the part still on the table is $\frac{2L}3-x$ long, so the friction is $\mu\frac MLg\left(\frac{2L}3-x\right)$. it shrinks to zero as the chain leaves:
$$
\begin{aligned}
W_f&=\int_0^{2L/3}\mu\frac MLg\left(\frac{2L}{3}-x\right)dx=\mu\frac{Mg}{L}\left[\frac{2L}{3}x-\frac{x^2}{2}\right]_0^{2L/3}\\
&=\mu\frac{Mg}{L}\left(\frac{4L^2}{9}-\frac{2L^2}{9}\right)=\frac29\mu MgL
\end{aligned}
$$

## the KE
$$
\begin{aligned}
K&=\frac{4MgL}{9}-\frac{2\mu MgL}{9}\\
&=\frac{2MgL}{9}(2-\mu)
\end{aligned}
$$

> [!important] the one idea
> ==for chains and ropes, find the PE from the centre of mass of each part, and integrate the friction because the length on the table keeps changing==

> [!eg] numbers
> $M=1$ kg, $L=3$ m, $\mu=0.2$, $g=10$: PE lost $=13.3$ J, friction $1.3$ J, $K=12$ J, so $v=\sqrt{2K/M}\approx4.9$ m/s. with no friction, $K=\frac{4MgL}{9}=13.3$ J

> [!extra]- will it even start?
> the hanging part pulls with $\frac{Mg}3$, the static friction can hold up to $\mu_s\frac{2Mg}{3}$. it slides only if $\frac13>\frac23\mu_s$, ie. $\mu_s<\frac12$

> [!exercise] try these
> ① a smooth table ($\mu=0$), half the chain hanging. speed when it leaves?
> ② in the problem above, why can't you just use the friction at the start times the distance?
> ③ what's the friction force at the start, and when the chain has slid $\frac L3$?

> [!answer]-
> ① PE lost $=\frac{MgL}{2}-\frac{MgL}{8}=\frac{3MgL}{8}=\tfrac12Mv^2$ → $v=\sqrt{\frac{3gL}{4}}$
> ② the friction isn't constant: it falls as less chain is on the table. constant friction would give $\frac49\mu MgL$, twice the real value
> ③ start: $\frac23\mu Mg$; after $\frac L3$: $\frac13\mu Mg$

see also [[Work by a variable force]], [[Centre of mass]], [[Friction]]

hub: [[Work, energy and power]]
