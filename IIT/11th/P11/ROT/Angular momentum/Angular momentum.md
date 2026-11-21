#mechanics #angular_momentum #rotation #worked_example
## the turning version of momentum
the **angular momentum** of a particle about a point O:
$$
\vec L=\vec r\times\vec p=m(\vec r\times\vec v),\qquad|\vec L|=r_\perp\,p=(r\sin\theta)\,p
$$
^angular-momentum

$\vec r$ is from O to the particle, $r_\perp$ is the ⊥ distance from O to the line the particle moves along. it depends on the point you choose. part of [[Rotational mechanics]]

> [!eg] moving in a straight line
> a particle moves at constant velocity parallel to the $x$ axis, a fixed distance $d$ from it. about the origin, $L=d\,mv$ the whole time: the ⊥ distance to its line never changes. so $L$ stays **the same** as it moves away (not bigger, not smaller)

## a projectile
fired at speed $u$ at $45°$ (maximum range) from O. take O as the reference point
$$
\begin{aligned}
\vec r&=\tfrac{u}{\sqrt2}t\,\hat i+\left(\tfrac{u}{\sqrt2}t-\tfrac12gt^2\right)\hat j\\
\vec v&=\tfrac{u}{\sqrt2}\,\hat i+\left(\tfrac{u}{\sqrt2}-gt\right)\hat j\\
\vec L=m(\vec r\times\vec v)&=m\left[x\,v_y-y\,v_x\right]\hat k\\
&=m\left[\tfrac{u}{\sqrt2}t\left(\tfrac{u}{\sqrt2}-gt\right)-\left(\tfrac{u}{\sqrt2}t-\tfrac12gt^2\right)\tfrac{u}{\sqrt2}\right]\hat k\\
&=-\frac{mgu\,t^2}{2\sqrt2}\,\hat k
\end{aligned}
$$

it grows like $t^2$, pointing into the page (clockwise). at the top, $t=\frac{u}{\sqrt2g}$:
$$
L_\text{top}=\frac{mu^3}{4\sqrt2\,g}
$$
same as the quick way: at the top the velocity is horizontal, $\frac{u}{\sqrt2}$, and its ⊥ distance from O is $h_\text{max}=\frac{u^2}{4g}$, so $L=m\frac{u}{\sqrt2}\cdot\frac{u^2}{4g}$ ✓

why it grows: gravity has a torque about O, $\tau=mg\,x$, and $\frac{dL}{dt}=\tau$

## rigid bodies
for a body spinning about a fixed axis, every bit moves in a circle, and adding up $r\times p$ gives
$$
\vec L=I\vec\omega,\qquad\vec\tau=\frac{d\vec L}{dt}
$$
^l-i-omega

with $I=\sum mr^2$ the [[Moment of inertia]]. so if the net torque is zero, $L$ can't change

> [!important] the one idea
> ==angular momentum is conserved about any axis about which no net outside torque acts: $I_1\omega_1=I_2\omega_2$==. in a collision with a pivot, take the pivot as the axis: the pivot's force has no torque about itself

useful moments of inertia: rod about its centre $\frac{ML^2}{12}$, rod about an end $\frac{ML^2}{3}$, disc about its centre $\frac{MR^2}{2}$, point mass $mr^2$

## particles dropped on a spinning disc
a disc ($M$, $R$) spins at $\omega$ about its axis. two particles of mass $m$ are placed gently on its rim and stick
$$
\begin{aligned}
\tfrac12MR^2\omega&=\left(\tfrac12MR^2+mR^2+mR^2\right)\omega'\\
\omega'&=\frac{M}{M+4m}\,\omega
\end{aligned}
$$

same angular momentum, bigger $I$, slower spin (like a skater opening their arms)

## two particles stick to a pivoted rod
a rod (mass $m$, length $l$) can turn about its centre on a smooth table. two particles of mass $m$, each at speed $v$, both moving to the right, hit it and stick: one at the top end ($\frac l2$ above the pivot), one $\frac l4$ below. they turn it opposite ways
$$
\begin{aligned}
mv\frac l2-mv\frac l4&=\left(\frac{ml^2}{12}+m\left(\frac l2\right)^2+m\left(\frac l4\right)^2\right)\omega\\
\frac{mvl}{4}&=ml^2\left(\frac{4+12+3}{48}\right)\omega=\frac{19}{48}ml^2\omega\\
\omega&=\frac{12v}{19l}
\end{aligned}
$$

## a particle sticks to a hanging rod
a rod ($M$, length $l$) hangs from a pivot at its top. a particle $m$ moving horizontally at $v$ hits the bottom end and sticks. initial $\omega$, and how far does the rod's centre rise?

**the hit** (angular momentum about the pivot):
$$
mvl=\left(\frac{Ml^2}{3}+ml^2\right)\omega\ \Rightarrow\ \omega=\frac{3mv}{(M+3m)\,l}
$$

**the swing** (energy, up to the highest angle $\theta$): the rod's centre rises $\frac l2(1-\cos\theta)$, the particle $l(1-\cos\theta)$
$$
\begin{aligned}
\tfrac12\cdot\frac{(M+3m)l^2}{3}\omega^2&=\left(\frac M2+m\right)gl(1-\cos\theta)\\
1-\cos\theta&=\frac{(M+3m)\,l\,\omega^2}{3(M+2m)\,g}=\frac{3m^2v^2}{(M+3m)(M+2m)\,gl}
\end{aligned}
$$

so the rod's centre rises
$$
x=\frac l2(1-\cos\theta)=\frac{3m^2v^2}{2g(M+3m)(M+2m)}
$$

> [!exercise] try these
> **1** a 2 kg disc of radius 0.5 m spins at 10 rad/s. a 0.5 kg lump sticks to its rim. new $\omega$?
> **2** find $L$ about the origin for a 2 kg particle at $(3,4)$ m with $\vec v=5\hat i$ m/s
> **3** in the hanging rod problem with $M=3m$, what's $\omega$?

> [!answer]-
> **1** $\frac12(2)(0.25)(10)=(0.25+0.125)\omega'$, $\omega'=6.7$ rad/s
> **2** $L=m(xv_y-yv_x)=2(0-20)=-40$ kg m²/s (clockwise)
> **3** $\omega=\frac{3mv}{6ml}=\frac{v}{2l}$

see also [[Free rod collisions]], [[Projectile motion]], [[Circular motion]]

hub: [[Rotational mechanics]]
