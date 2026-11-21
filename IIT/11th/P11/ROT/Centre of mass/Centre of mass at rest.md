#mechanics #centre_of_mass #worked_example
## the rule
if there's **no net outside force in some direction**, the centre of mass velocity in that direction can't change ([[Centre of mass#^cm-velocity]]). if it **started at rest**, its coordinate in that direction stays fixed, however the parts move around because of internal forces:
$$
\sum m_i\,\Delta x_i=0
$$
^cm-fixed

part of [[Rotational mechanics]]

> [!important] the one idea
> ==start at rest + no outside force ⇒ the centre of mass doesn't move: whatever one part moves forward, the rest moves back, weighted by mass==

the recipe: write $\bar x$ before, write $\bar x$ after (with the unknown shift $x$), set them equal. or, quicker, $\sum m_i\Delta x_i=0$ with each $\Delta x$ measured **relative to the ground**

## two balls on a smooth plane
a 4 kg ball at the origin and a 2 kg ball 4 m away are pushed apart by an internal force. the 2 kg ball moves 1 m to the **left**. where does the 4 kg ball go?
$$
4\,\Delta x_4+2(-1)=0\ \Rightarrow\ \Delta x_4=+0.5\ \text{m}
$$

0.5 m to the right. (check: $\bar x=\frac{8}{6}$ before, $\frac{4(0.5)+2(3)}{6}=\frac86$ after ✓)

## the monkey on a plank
a 10 kg monkey stands at the left end of a 40 kg plank 2 m long, on a smooth floor. it walks to the other end. how far does the plank move?

the monkey moves 2 m **relative to the plank**, so relative to the ground it moves $2+x$, where $x$ is the plank's shift:
$$
\begin{aligned}
40x+10(2+x)&=0\\
x&=-0.4\ \text{m}
\end{aligned}
$$

the plank slides 0.4 m back, and the monkey only gets $1.6$ m over the ground (the plank now runs from $-0.4$ to $1.6$)

## the man on a boat
a 40 kg man walks from one end of a 100 kg boat, 4 m long, to the other (no water resistance)

![[Boat_centre_of_mass_animation.png]]

$$
\begin{aligned}
100x+40(4+x)&=0\\
x&=-\frac{160}{140}=-\frac87\approx-1.14\ \text{m}
\end{aligned}
$$

> [!eg] the shortcut
> a body of mass $m$ moves a distance $d$ **relative to** a free body of mass $M$: the free body moves back $\frac{m}{m+M}d$. boat: $\frac{40}{140}\times4=\frac87$ ✓. plank: $\frac{10}{50}\times2=0.4$ ✓

## a ball rolling in a free bowl
a small ball (mass $m$, radius $r$) is let go at the rim of a hemispherical bowl (mass $M$, radius $R$) standing on a smooth table. how far has the bowl moved when the ball reaches the bottom?

the ball's centre goes $R-r$ sideways relative to the bowl, so by the shortcut
$$
x=\frac{m}{M+m}(R-r)
$$
the bowl moves that far the **other** way

## a block sliding down a free curved track
a 1 kg block slides down a smooth curved track of mass 10 kg standing on a smooth table, and leaves the end 2 m lower, moving at $60°$ above the horizontal **relative to the track**. find the speeds

horizontally there's no outside force, so horizontal momentum stays zero. call the track's speed $v_0$ (to the left) and the block's speed relative to the track $v$. the block's velocity over the ground is $(v\cos60°-v_0,\ v\sin60°)$
$$
\begin{aligned}
\text{momentum: }1\,(v\cos60°-v_0)&=10\,v_0\ \Rightarrow\ v=22\,v_0\\
\text{energy: }1(10)(2)&=\tfrac12(10)v_0^2+\tfrac12(1)\left[(10v_0)^2+(11\sqrt3\,v_0)^2\right]\\
20&=5v_0^2+231.5\,v_0^2=236.5\,v_0^2\ \Rightarrow\ v_0\approx0.29\ \text{m/s},\quad v\approx6.4\ \text{m/s}
\end{aligned}
$$

(energy uses the ground speeds: momentum only in $x$, energy is a scalar, see [[Conservation of mechanical energy]])

## exploding shells
a shell is fired at speed $u$ and angle $\theta$ and explodes into two equal halves at the top. the explosion is internal, so the **centre of mass carries on along the original parabola** and lands at the range $R$

![[Exploding_projectile_animation.png]]

### one half falls straight down
it lands right under the top, at $\frac R2$. the centre of mass lands at $R$:
$$
\frac{\frac m2\cdot\frac R2+\frac m2\,x}{m}=R\ \Rightarrow\ x=\frac{3R}{2}
$$
momentum at the top: $mu\cos\theta=\frac m2(0)+\frac m2v'$, so the other half leaves at $v'=2u\cos\theta$

### one half retraces its path
it goes back the way it came and lands at the launch point, 0. so $\frac{0+x}{2}=R$, $x=2R$. momentum: $mu\cos\theta=-\frac m2u\cos\theta+\frac m2v'$, so $v'=3u\cos\theta$

> [!exercise] try these
> ① a 60 kg person walks 3 m along a 120 kg raft. how far does the raft move?
> ② a shell explodes at the top into halves; one lands at the launch point. where's the other?
> ③ a 50 kg man at the back of a 150 kg boat is 10 m from the shore. he walks 4 m to the front (towards the shore). how far from the shore is he now?

> [!answer]-
> ① $\frac{60}{180}\times3=1$ m backwards
> ② at $2R$ (the retracing case)
> ③ the boat moves back $\frac{50}{200}\times4=1$ m, so he moves $3$ m towards the shore: 7 m away

see also [[Centre of mass]], [[Momentum]], [[Projectile motion]]

hub: [[Rotational mechanics]]
