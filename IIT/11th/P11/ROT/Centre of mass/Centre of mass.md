#mechanics #centre_of_mass #worked_example
## one point for the whole system
the **centre of mass** is the mass weighted average position of all the particles. for masses $m_1,m_2,\dots$ at $(x_1,y_1),(x_2,y_2),\dots$
$$
\bar x=\frac{\sum m_ix_i}{\sum m_i}\qquad\bar y=\frac{\sum m_iy_i}{\sum m_i}
$$
^cm-position

part of [[Rotational mechanics]]. heavier masses pull it towards themselves; for two equal masses it's halfway between

differentiate once and twice (the masses don't change):
$$
\bar v_x=\frac{\sum m_iv_{ix}}{\sum m_i}\qquad\bar a_x=\frac{\sum m_ia_{ix}}{\sum m_i}
$$
^cm-velocity

(the same for $y$ and $z$). so $M\bar v=\sum m_iv_i$ is the **total momentum**, and $M\bar a=\sum m_ia_i=F_\text{ext}$: internal forces cancel in pairs ([[Newton's laws of motion|Newton's third law]])

> [!important] the one idea
> ==the centre of mass moves as if all the mass were there and only the outside forces acted on it: $M\bar a=F_\text{ext}$==. internal forces (explosions, people walking, springs) can't move it

## velocity of the centre of mass
three particles: 2 kg at 10 m/s along $+x$, 4 kg at rest, 2 kg at $20\sqrt2$ m/s pointing down and left at $45°$ (so $-20$ along $x$ and $-20$ along $y$)
$$
\begin{aligned}
\bar v_x&=\frac{2(10)+4(0)+2(-20)}{2+4+2}=-\frac{20}{8}=-2.5\ \text{m/s}\\
\bar v_y&=\frac{2(0)+4(0)+2(-20)}{8}=-5\ \text{m/s}
\end{aligned}
$$

## acceleration of the centre of mass: the Atwood machine
3 kg and 2 kg hang over a light pulley

![[Atwood_machine_cm.png]]

each block on its own ([[Newton's laws of motion]]):
$$
\begin{aligned}
3g-T&=3a\\
T-2g&=2a\\
a&=\frac{g}{5}=2\ \text{m/s}^2
\end{aligned}
$$

the 3 kg goes down ($-2$), the 2 kg goes up ($+2$):
$$
\bar a=\frac{3(-2)+2(+2)}{3+2}=-\frac25=-0.4\ \text{m/s}^2
$$

the centre of mass accelerates **down** at $0.4$ m/s², much less than $g$. check with $M\bar a=F_\text{ext}$: the outside forces are the weights (50 N down) and the pull of the pulley's support ($2T=48$ N up), net 2 N down, $\bar a=\frac{2}{5}$ ✓

> [!eg] the general Atwood result
> $\bar a=\left(\frac{m_1-m_2}{m_1+m_2}\right)^2g$, downwards. equal masses: the centre of mass doesn't accelerate at all

> [!exercise] try these
> **1** 1 kg at $(0,0)$, 2 kg at $(3,0)$, 3 kg at $(0,4)$. where's the centre of mass?
> **2** two skaters, 60 kg and 40 kg, push apart from rest. the 40 kg one moves at 3 m/s. how fast is the other, and what's $\bar v$?
> **3** Atwood with 4 kg and 1 kg: find $\bar a$

> [!answer]-
> **1** $\bar x=\frac{6}{6}=1$, $\bar y=\frac{12}{6}=2$: $(1,2)$
> **2** momentum: $60v=40(3)$, $v=2$ m/s the other way; $\bar v=0$ (it started at rest, no outside force)
> **3** $a=\frac35g=6$, $\bar a=\frac{4(-6)+1(6)}{5}=-3.6$ m/s² $=\left(\frac35\right)^2g$ ✓

see also [[Centre of mass at rest]], [[Centre of mass of continuous bodies]]

hub: [[Rotational mechanics]]
