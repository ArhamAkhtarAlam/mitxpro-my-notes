#mechanics #power #circular_motion #worked_example
## two parts of the force
in circular motion the net force splits into two parts ([[Circular motion]]):
- **centripetal** (radial) $F_r=\frac{mv^2}{r}$, towards the centre: turns the velocity
- **tangential** $F_t=m\frac{dv}{dt}$, along the velocity: changes the speed

the centripetal part is always ⊥ to $\vec v$, so by [[Power#^power]] it delivers **no power**. all the power comes from the tangential part:
$$
P=F_t\,v=m\frac{dv}{dt}\,v=\frac{dK}{dt}
$$

> [!important] the one idea
> ==the centripetal force never does work; only the tangential force changes the KE, so $P=F_tv=\frac{dK}{dt}$==. in **uniform** circular motion there's no $F_t$, so $P=0$

part of [[Work, energy and power]]

## centripetal acceleration given: 2t²
$m=2$ kg, $r=2$ m. find the power as a function of $t$
$$
\begin{aligned}
\frac{v^2}{r}&=2t^2\ \Rightarrow\ v^2=2rt^2=4t^2\ \Rightarrow\ v=2t\\
a_t&=\frac{dv}{dt}=2\,\text{m/s}^2,\qquad F_t=ma_t=4\ \text{N}\\
P&=F_tv=4\times2t=8t
\end{aligned}
$$

the speed grows, so this is **non uniform** circular motion. watch the two power curves: the centripetal force grows like $t^2$ but its power stays at zero

![[Circular_power_animation.png]]

## KE given as a function of time: K = t²
$m=2$ kg, $r=2$ m. find the net force at $t=2$ s and the power
$$
\begin{aligned}
\tfrac12mv^2&=t^2\ \Rightarrow\ v=t\ \Rightarrow\ a_t=1\,\text{m/s}^2,\ F_t=2\ \text{N}\\
F_r&=\frac{mv^2}{r}=t^2=4\ \text{N at }t=2\\
F&=\sqrt{F_t^2+F_r^2}=\sqrt{4+16}=2\sqrt5\approx4.5\ \text{N}\\
P&=\frac{dK}{dt}=2t\qquad(\text{same as }F_tv=2\cdot t)
\end{aligned}
$$

## KE given as a function of distance: K = 2s²
$s$ = distance gone round the circle, $m=2$, $r=2$. since $dK=F_t\,ds$ (only $F_t$ works), the tangential force is the **slope of K against s**:
$$
F_t=\frac{dK}{ds}
$$
^tangential-force

$$
\begin{aligned}
F_t&=\frac{d}{ds}(2s^2)=4s\\
\tfrac12mv^2&=2s^2\ \Rightarrow\ v=\sqrt2\,s\\
P&=F_tv=4s\cdot\sqrt2\,s=4\sqrt2\,s^2\\
F_r&=\frac{mv^2}{r}=\frac{2\cdot2s^2}{2}=2s^2\\
F&=\sqrt{F_t^2+F_r^2}=\sqrt{16s^2+4s^4}=2s\sqrt{s^2+4}
\end{aligned}
$$

> [!eg] three derivatives of K
> the same $K$ gives three different things depending on what you differentiate by:
>
> | derivative | gives | why |
> |---|---|---|
> | $\frac{dK}{dt}$ | power $P$ | rate of doing work |
> | $\frac{dK}{ds}$ | tangential force $F_t$ | $dK=F_t\,ds$ |
> | $\frac{dK}{dv}$ | momentum $mv$ | $\frac{d}{dv}\tfrac12mv^2=mv$ |
>

> [!exercise] try these
> **1** a particle goes round a circle at a steady 5 m/s. power of the net force?
> **2** $K=3t^2$ for a 1.5 kg particle on a 1 m circle. find $F_t$ and $P$ at $t=1$ s
> **3** $K=s^2$, $m=2$ kg. find $F_t$ when $s=3$ m

> [!answer]-
> **1** zero: uniform circular motion, the force is all centripetal
> **2** $\tfrac12(1.5)v^2=3t^2$ → $v=2t$, $a_t=2$, $F_t=3$ N; $P=\frac{dK}{dt}=6t=6$ W (check $3\times2=6$ ✓)
> **3** $F_t=2s=6$ N

see also [[Power]], [[Leaving a circular track]]

hub: [[Work, energy and power]]
