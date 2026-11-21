#mechanics #collision #spring #worked_example
## sticking together
in a **perfectly inelastic** collision the bodies stick and move off together ($e=0$, see [[Elastic collisions]]). during the hit, the forces between them are huge and short, so outside forces don't matter: **momentum is kept** ([[Momentum]]). kinetic energy is **not**: some turns into heat, sound and squashing
$$
mv+Mu_M=(m+M)u\qquad\text{(block at rest: }u=\frac{m}{m+M}v\text{)}
$$
^inelastic-velocity

part of [[Work, energy and power]]

> [!important] the one idea
> ==split it into two stages: the collision (only momentum is kept), then the motion after (now energy is kept). never use energy conservation across the collision itself==

> [!eg] bullet into a block
> a 1 g bullet at 1000 m/s gets stuck in a 1 kg block at rest:
> $10^{-3}\times1000=1.001\,u$, so $u\approx1$ m/s. KE before: 500 J, after: $\tfrac12(1.001)(1)^2\approx0.5$ J. **99.9%** of the KE is gone

## into a block on a spring
a bullet $m$, speed $v$, sticks in a block $M$ attached to a spring $k$ on a smooth floor. max compression?

wrong: $\tfrac12mv^2=\tfrac12kx^2$ (that pretends no energy is lost in the hit). right:
1. **collision**: $u=\frac{m}{M+m}v$
2. **compression**: now energy is kept, $\tfrac12(M+m)u^2=\tfrac12kx^2$

$$
x=u\sqrt{\frac{M+m}{k}}=\frac{mv}{\sqrt{k(M+m)}}
$$

watch how much energy disappears at the hit before the spring even gets any:

![[Bullet_spring_animation.png]]

## vertical springs
for these, measure spring PE from the **natural length** and gravitational PE from wherever is handy. the spring has $k=\frac{mg}{b}$, so a block $m$ hanging on it at rest stretches it by $b$

### a bullet from below
a bullet $m$ moving **up** at $v$ sticks in the hanging block $m$. how high does the block rise from where it was?

collision: $mv=2mv'$, so $v'=\frac v2$. then energy, with the block rising $h$ (the stretch goes from $b$ to $b-h$):
$$
\begin{aligned}
\tfrac12(2m)\left(\tfrac v2\right)^2+\tfrac12kb^2&=2mgh+\tfrac12k(b-h)^2\\
\frac{mv^2}{4}&=2mgh-kbh+\tfrac12kh^2\qquad(kb=mg)\\
\frac{v^2}{4g}&=h+\frac{h^2}{2b}\\
h&=\sqrt{b^2+\frac{bv^2}{2g}}-b
\end{aligned}
$$

### a bullet from above
a bullet $m$ moving **down** at $v=\sqrt{2gb}$ sticks in the hanging block $m$. how far down does the block go?

collision: $v'=\frac v2=\sqrt{\frac{gb}{2}}$. then energy, with the block going down $x$ (stretch from $b$ to $b+x$):
$$
\begin{aligned}
\tfrac12(2m)\frac{gb}{2}+2mgx&=\tfrac12k(b+x)^2-\tfrac12kb^2\\
\frac{mgb}{2}+2mgx&=\frac{mg}{2b}\left(2bx+x^2\right)\\
b^2+2bx&=x^2\\
x&=b(1+\sqrt2)
\end{aligned}
$$

> [!exercise] try these
> **1** a 10 g bullet at 400 m/s sticks in a 1.99 kg block on a spring, $k=800$ N/m. max compression?
> **2** what fraction of the KE is lost when a bullet $m$ sticks in a block $M$ at rest?
> **3** two 1 kg carts, one at 4 m/s, one at rest, couple together. KE lost?

> [!answer]-
> **1** $u=\frac{0.01\times400}{2}=2$ m/s, $x=2\sqrt{\frac{2}{800}}=0.1$ m
> **2** KE after / before $=\frac{m}{m+M}$, so the lost fraction is $\frac{M}{m+M}$
> **3** $u=2$ m/s; before 8 J, after $\tfrac12(2)(4)=4$ J: 4 J lost

see also [[Elastic collisions]], [[Conservation of mechanical energy]], [[Two blocks and a spring]]

hub: [[Work, energy and power]]
