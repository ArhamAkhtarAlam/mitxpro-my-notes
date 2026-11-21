#mechanics #energy #circular_motion #worked_example
## the problem
a block is released from rest at height $2R$ above the bottom of a smooth track: it drops down a straight part into a circular part of radius $R$ and goes up the other side, **on the inside** of the circle. it starts only $R$ **above the centre**, so it can never reach the top of the circle. where does it leave the track, and how high does it get? part of [[Work, energy and power]]

![[Leaving_circular_track_animation.png]]

## where it leaves
let $\theta$ = the angle of the block's position above the horizontal through the centre (on the far side). two equations:

**energy** (take $U=0$ at the centre's level, [[Conservation of mechanical energy#^energy-conservation]]):
$$
\begin{aligned}
mgR&=\tfrac12mv^2+mgR\sin\theta\\
v^2&=2gR(1-\sin\theta)
\end{aligned}
$$

**towards the centre** ([[Circular motion]]): the normal force $N$ and the part of gravity pointing to the centre, $mg\sin\theta$, together give the centripetal force
$$
N+mg\sin\theta=\frac{mv^2}{R}
$$

it **loses contact** when the track stops pushing, $N=0$:
$$
\begin{aligned}
mg\sin\theta&=\frac{m}{R}\cdot2gR(1-\sin\theta)\\
\sin\theta&=2-2\sin\theta\\
\sin\theta&=\frac23,\qquad\theta=\sin^{-1}\tfrac23\approx41.8°
\end{aligned}
$$

and there $v^2=gR\sin\theta=\frac23gR$

> [!important] the one idea
> ==a body on the inside of a circular track leaves it where $N$ drops to zero: use energy for $v$, and $N=\frac{mv^2}{R}-(\text{gravity towards the centre})$==. in general $N=mg(2-3\sin\theta)$ here: $5mg$ at the bottom, $2mg$ at the centre's level, $0$ at $\sin\theta=\frac23$

## how high it gets
after leaving, it's a [[Projectile motion|projectile]]. its velocity is along the tangent, at angle $90°-\theta$ to the horizontal, so
- horizontal part (stays the same): $v\sin\theta$
- vertical part (gravity uses it up): $v\cos\theta$

the extra rise is $\frac{(v\cos\theta)^2}{2g}$:
$$
\begin{aligned}
h&=R\sin\theta+\frac{v^2\cos^2\theta}{2g}\\
&=R\sin\theta+\frac{gR\sin\theta\cos^2\theta}{2g}=R\sin\theta\left(1+\tfrac12\cos^2\theta\right)\\
&=\tfrac23R\left(1+\tfrac12\cdot\tfrac59\right)=\tfrac23R\cdot\tfrac{23}{18}=\frac{23}{27}R\approx0.85R
\end{aligned}
$$

above the centre, with speed $v\sin\theta=\sqrt{\tfrac23gR}\cdot\tfrac23=\tfrac23\sqrt{\tfrac23gR}$ at that highest point

> [!eg] check with energy
> it started at $R$ above the centre but only reaches $\frac{23}{27}R$: the missing $\frac{4}{27}mgR$ is the KE it still has at the top, $\tfrac12m\left(\tfrac23\right)^2\cdot\tfrac23gR=\tfrac{4}{27}mgR$ ✓

> [!exercise] try these
> **1** what's $N$ at the very bottom of the circle?
> **2** from what height above the bottom would you have to release it to just make it round the top of the circle?
> **3** a small ball sits on top of a smooth hemisphere of radius $R$ and is nudged. at what angle from the top does it fly off?

> [!answer]-
> **1** speed there: $v^2=2g(2R)=4gR$, so $N-mg=\frac{m\cdot4gR}{R}$, $N=5mg$
> **2** at the top it needs $v^2\ge gR$: $mg h=mg(2R)+\tfrac12mgR$, $h=2.5R$
> **3** the classic: $\cos\phi=\frac23$, $\phi\approx48.2°$ (same maths with the angle measured from the vertical)

see also [[Power in circular motion]], [[Conservation of mechanical energy]]

hub: [[Work, energy and power]]
