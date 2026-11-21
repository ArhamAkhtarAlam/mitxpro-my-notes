#mechanics #work #worked_example
## the integral
when the force changes along the way, $W=Fs$ doesn't work any more. chop the path into tiny steps $d\vec r$, where the force is (almost) constant, and add up:
$$
W=\int\vec F\cdot d\vec r\qquad\text{in 1D: }W=\int_{x_1}^{x_2}F(x)\,dx
$$
^work-integral

so the work is the **area under the $F$–$x$ graph**. part of [[Work, energy and power]]

> [!eg] F = x² + x + 3
> a force $F=x^2+x+3$ N (x in m) acts along $+x$. work from the origin to $x=2$ m:
> $$
> W=\int_0^2(x^2+x+3)\,dx=\left[\frac{x^3}{3}+\frac{x^2}{2}+3x\right]_0^2=\frac83+2+6=\frac{32}{3}\approx10.7\ \text{J}
> $$

## when x is given as a function of time
if you know $x(t)$, change the variable: $dx=\frac{dx}{dt}dt=v\,dt$, so $W=\int F\,v\,dt$

> [!eg] x = t³/6 for a 2 kg particle
> $v=\frac{dx}{dt}=\frac{t^2}{2}$, $a=\frac{dv}{dt}=t$, so the net force is $F=ma=2t$ (4 N at $t=2$ s). work from $t=0$ to 2 s:
> $$
> W=\int_0^2F\,v\,dt=\int_0^2 2t\cdot\frac{t^2}{2}\,dt=\int_0^2t^3\,dt=\left[\frac{t^4}{4}\right]_0^2=4\ \text{J}
> $$
> check with the [[Work-energy theorem]]: $v(2)=2$ m/s, $\tfrac12(2)(2^2)=4$ J ✓. the power is in [[Power]]

## the trick: use the work energy theorem
often you **can't** integrate the force because you don't know it, but you know everything else. then let the [[Work-energy theorem]] do it: total work = $\Delta K$, so the unknown work is whatever is left over

### the slowly lifted pendulum
a 2 kg bob on a 2 m string is pushed by a variable force $F$ so it moves at **constant speed**, from hanging straight down to $60°$. how much work does $F$ do?

![[Pendulum_work_animation.png]]

- **tension**: always along the string, ⊥ to the motion: $W_T=0$
- **gravity**: the bob rises $h=L(1-\cos60°)=2(1-\tfrac12)=1$ m, so $W_g=-mgh=-20$ J
- **KE**: constant speed, so $\Delta K=0$

$$
\begin{aligned}
W_F+W_T+W_g&=\Delta K\\
W_F+0-20&=0\\
W_F&=20\ \text{J}
\end{aligned}
$$

no integral needed, and it doesn't matter **which way** $F$ points or how it changes: anything that moves the bob slowly from A to B does $+mgh$

> [!important] the one idea
> ==when a force is too messy to integrate, find its work from the work energy theorem: the work of everything else, plus the change in KE==

> [!extra]- what F actually is
> for a horizontal push, the bob is (almost) in balance at each angle $\phi$: $F\cos\phi=mg\sin\phi$, so $F=mg\tan\phi$, from 0 up to $20\sqrt3\approx34.6$ N at $60°$. and $\int F\,dx$ along the arc really gives 20 J: with $x=L\sin\phi$, $dx=L\cos\phi\,d\phi$,
> $$
> W=\int_0^{\pi/3}mg\tan\phi\,L\cos\phi\,d\phi=mgL\int_0^{\pi/3}\sin\phi\,d\phi=mgL(1-\cos60°)=20\ \text{J}
> $$

> [!exercise] try these
> ① a spring force $F=-kx$. how much work does the spring do as it's stretched from 0 to $x$?
> ② $F=\frac{6}{x^2}$ N acts along $+x$. find the work from $x=1$ m to $x=3$ m
> ③ a 0.5 kg ball tied to a 1 m string is pulled slowly from hanging down to horizontal. work done by the pull?

> [!answer]-
> ① $\int_0^x(-kx)\,dx=-\tfrac12kx^2$ (the spring fights the stretch; that energy is stored, see [[Conservation of mechanical energy]])
> ② $\int_1^3 6x^{-2}dx=[-6/x]_1^3=-2+6=4$ J
> ③ $W=mgL=0.5\times10\times1=5$ J

see also [[Work done by a force]], [[Power]]

hub: [[Work, energy and power]]
