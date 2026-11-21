#mechanics #power #worked_example
## how fast work is done
**power** is the rate of doing work. with $dW=\vec F\cdot d\vec r$ and $\frac{d\vec r}{dt}=\vec v$:
$$
P=\frac{dW}{dt}=\vec F\cdot\vec v
$$
^power

unit: watt, $1\,\text{W}=1\,\text{J/s}$. like work, it's a scalar and can be negative (the force is taking energy out). part of [[Work, energy and power]]

the **average** power over a time interval is the total work divided by the time, which is the same as the time average of $P(t)$:
$$
\bar P=\frac{W}{t_2-t_1}=\frac{1}{t_2-t_1}\int_{t_1}^{t_2}P(t)\,dt
$$
^power-avg

(the average of any function: $\bar f=\frac{1}{x_2-x_1}\int_{x_1}^{x_2}f(x)\,dx$)

> [!important] the one idea
> ==$P=\vec F\cdot\vec v$: a force puts energy in fastest when it pushes along the velocity, takes it out when it pushes against it, and does nothing when it's ⊥==

## x = t³/6 again
the 2 kg particle from [[Work by a variable force]]: $v=\frac{t^2}{2}$, $F=2t$
$$
\begin{aligned}
P&=Fv=2t\cdot\frac{t^2}{2}=t^3\qquad(\text{or }P=\tfrac{d}{dt}\tfrac{t^4}{4}=t^3)\\
P(2)&=8\ \text{W}\\
\bar P_{0\to2}&=\frac12\int_0^2t^3\,dt=\frac12\cdot4=2\ \text{W}
\end{aligned}
$$

the average (2 W) is far below the final value (8 W): the power keeps growing, so most of the work happens near the end

## a projectile
thrown at speed $v_0$ and angle $\theta$, no air. the only force is gravity:
- $\vec v=v_0\cos\theta\,\hat i+(v_0\sin\theta-gt)\,\hat j$
- $\vec F=-mg\,\hat j$

$$
P=\vec F\cdot\vec v=-mg(v_0\sin\theta-gt)
$$

- going **up** ($t<$ top): $P<0$, gravity takes KE out
- at the **top**: $v$ is horizontal, ⊥ to gravity, $P=0$
- coming **down**: $P>0$, gravity puts it back

![[Projectile_power_animation.png]]

over the whole flight, $T=\frac{2v_0\sin\theta}{g}$:
$$
\bar P=\frac1T\int_0^T-mg(v_0\sin\theta-gt)\,dt=-\frac{mg}{T}\left(v_0\sin\theta\,T-\frac{gT^2}{2}\right)=-mg\left(v_0\sin\theta-\frac{gT}{2}\right)=0
$$

which makes sense: it lands at the same height and the same speed, so gravity's total work, $\Delta K$, is zero ([[Work-energy theorem]])

> [!eg] numbers
> $m=1$ kg, $v_0=20$ m/s, $\theta=60°$: at launch $P=-10\times17.3=-173$ W, at the top 0, at landing $+173$ W. flight time $3.46$ s

> [!exercise] try these
> ① a car engine gives 30 kW at 20 m/s. what's the driving force?
> ② a 2 kg block is pulled at a steady 3 m/s across a floor with $\mu_k=0.25$. power of the pull?
> ③ in the $x=t^3/6$ example, at what time is the power equal to the average power over $0$–$2$ s?

> [!answer]-
> ① $F=P/v=30000/20=1500$ N
> ② steady speed, so pull = friction $=0.25\times20=5$ N, $P=5\times3=15$ W
> ③ $t^3=2$, $t=2^{1/3}\approx1.26$ s

see also [[Power in circular motion]], [[Projectile motion]]

hub: [[Work, energy and power]]
