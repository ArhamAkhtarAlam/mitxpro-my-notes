#mechanics #momentum #worked_example
## force is the rate of change of momentum
Newton's second law in its real form is about **momentum**, $\vec p=m\vec v$:
$$
\vec F=\frac{d\vec p}{dt}=m\frac{d\vec v}{dt}+\vec v\frac{dm}{dt}
$$
^force-momentum

when $m$ is fixed this is just $F=ma$. when mass is being added or lost (sand, fuel, water), the second term matters. part of [[Rotational mechanics]]

for a body of mass $M$ that gains or loses mass at rate $\frac{dM}{dt}$, where that mass moves at $\vec u_\text{rel}$ **relative to the body**:
$$
M\frac{d\vec v}{dt}=\vec F_\text{ext}+\vec u_\text{rel}\frac{dM}{dt}
$$
^variable-mass

> [!important] the one idea
> ==only the relative velocity of the mass coming or going matters: mass that leaves at the body's own speed (sand through a hole) changes nothing, mass that arrives at rest (sand from a hopper) drags the body back==. rockets: gas leaves backwards fast, so it pushes forwards

## the angle between p and F
a particle moves in the $xy$ plane with $\vec p=2\sin(\pi t)\,\hat i+2\cos(\pi t)\,\hat j$. then
$$
\vec F=\frac{d\vec p}{dt}=2\pi\cos(\pi t)\,\hat i-2\pi\sin(\pi t)\,\hat j
$$
$\vec F\cdot\vec p=4\pi(\sin\pi t\cos\pi t-\cos\pi t\sin\pi t)=0$, so the angle is always $90°$. ($|\vec p|$ is constant: the force only turns the momentum, like [[Circular motion|circular motion]])

## bullets on a wall
100 bullets of 10 g, at 1000 m/s, hit a wall in 10 s and bounce straight back at the same speed. each one's momentum changes by $2mv$:
$$
F=\frac{\Delta p}{\Delta t}=\frac{100\times2\times0.01\times1000}{10}=200\ \text{N}
$$

## pebbles falling into a pan
$n$ pebbles per second, each of mass $m$, drop from height $h$ onto a weighing pan and stick. what does it read at time $t$?
- each lands at $\sqrt{2gh}$ and stops: momentum delivered per second $=nm\sqrt{2gh}$, a steady push
- by time $t$, $nt$ pebbles sit on it: weight $nt\,mg$

$$
\text{reading}=nm\sqrt{2gh}+nmgt
$$

## a flat car being loaded with sand
a flat car (mass $m_0$) is pulled by a constant force $F$ on a smooth track. sand falls onto it from a hopper at rest at $\mu$ kg/s. the sand arrives with no horizontal speed, so relative to the car it moves at $-v$
$$
\begin{aligned}
(m_0+\mu t)\frac{dv}{dt}&=F-\mu v\\
\frac{d}{dt}\big[(m_0+\mu t)v\big]&=F\qquad(\text{the same thing: }F=\tfrac{dp}{dt})\\
(m_0+\mu t)v&=Ft\\
v&=\frac{Ft}{m_0+\mu t},\qquad a=\frac{dv}{dt}=\frac{Fm_0}{(m_0+\mu t)^2}
\end{aligned}
$$

the speed creeps up towards $\frac F\mu$ but never reaches it: all the force goes into getting new sand up to speed

## a cart leaking sand
a cart full of sand (mass $m_0$ at $t=0$, at rest) is pulled by a constant force $F$. sand pours out of a hole in the floor at $\mu$ kg/s. the sand leaves at the **cart's own** speed, so $u_\text{rel}=0$ and it takes no momentum away from the cart
$$
\begin{aligned}
(m_0-\mu t)\frac{dv}{dt}&=F\\
\int_0^vdv&=\int_0^t\frac{F\,dt}{m_0-\mu t}\\
v&=\frac F\mu\ln\frac{m_0}{m_0-\mu t}
\end{aligned}
$$

the cart just gets lighter, so the same force accelerates it more and more

> [!eg] the two carts side by side
> $F=10$ N, $m_0=10$ kg, $\mu=1$ kg/s, after 5 s: the loading car has $v=\frac{50}{15}=3.3$ m/s; the leaking cart has $v=10\ln2=6.9$ m/s. with fixed mass it would be $5$ m/s

> [!exercise] try these
> **1** a hose sprays 2 kg/s of water at 10 m/s onto a wall, and the water stops. force on the wall?
> **2** a rocket of 1000 kg ejects gas at 2000 m/s relative to it, at 5 kg/s, in deep space. its acceleration?
> **3** in the bullet problem, what if the bullets stuck in the wall instead?

> [!answer]-
> **1** $F=\mu v=20$ N
> **2** $a=\frac{u\mu}{M}=\frac{2000\times5}{1000}=10$ m/s²
> **3** each loses only $mv$: $F=100$ N

see also [[Impulse]], [[Momentum]]

hub: [[Rotational mechanics]]
