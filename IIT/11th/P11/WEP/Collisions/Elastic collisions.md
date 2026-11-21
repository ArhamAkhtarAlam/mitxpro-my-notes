#mechanics #collision #worked_example
## both kept
in an **elastic** collision both momentum **and** kinetic energy are kept. in 1D, ball 1 ($m_1$, $u_1$) catches ball 2 ($m_2$, $u_2<u_1$), and after the hit they move at $v_1$, $v_2$. part of [[Work, energy and power]]

**momentum**:
$$
m_1u_1+m_2u_2=m_1v_1+m_2v_2\ \Rightarrow\ m_1(u_1-v_1)=m_2(v_2-u_2)\qquad\textbf{1}
$$

**KE**:
$$
\tfrac12m_1u_1^2+\tfrac12m_2u_2^2=\tfrac12m_1v_1^2+\tfrac12m_2v_2^2\ \Rightarrow\ m_1(u_1^2-v_1^2)=m_2(v_2^2-u_2^2)\qquad\textbf{2}
$$

divide **2** by **1** (the difference of squares cancels against **1**):
$$
\begin{aligned}
u_1+v_1&=v_2+u_2\\
u_1-u_2&=v_2-v_1
\end{aligned}
$$
^elastic-relative

> [!important] the one idea
> ==in a 1D elastic collision, the speed they come together at equals the speed they fly apart at: $u_1-u_2=v_2-v_1$==. use this with momentum instead of the KE equation: two **linear** equations, no squares

that ratio is the **coefficient of restitution** ([[Coefficient of restitution]]):
$$
e=\frac{v_2-v_1}{u_1-u_2}
$$
$e=1$ elastic, $e=0$ perfectly inelastic ([[Perfectly inelastic collisions]]), in between: some KE lost

## equal masses swap velocities
with $m_1=m_2=m$:
$$
\begin{aligned}
u_1-u_2&=v_2-v_1&&(e=1)\\
u_1+u_2&=v_1+v_2&&(\text{momentum, }m\text{ cancels})\\
\text{add: }2u_1&=2v_2\ \Rightarrow\ v_2=u_1,\quad v_1=u_2
\end{aligned}
$$

so they just **exchange** velocities. if ball 2 was at rest, ball 1 stops dead and ball 2 leaves at $u_1$ (Newton's cradle)

![[Elastic_collision_equal_masses.png]]

## into a block on a spring
a block $m$ at speed $v$ hits an equal block $m$ elastically. the second one is at rest against a spring $k$ fixed to a wall. max compression?

they swap: the first stops, the second moves off at $v$ and squashes the spring until it stops:
$$
\tfrac12mv^2=\tfrac12kx^2\ \Rightarrow\ x=v\sqrt{\frac mk}
$$

(this time it's fine to set the KE equal to the spring energy: nothing was lost in the hit, and the first block keeps none)

if the spring has **another** free block on its far end, the answer changes: see [[Two blocks and a spring]]

> [!exercise] try these
> **1** a 2 kg ball at 3 m/s hits a 1 kg ball at rest, elastically. find both velocities after
> **2** a ball at 5 m/s hits an identical ball moving the **same** way at 2 m/s, elastically. after?
> **3** a ball is dropped from 1.8 m onto a floor with $e=0.5$. how high does it bounce?

> [!answer]-
> **1** $3-0=v_2-v_1$ and $2(3)=2v_1+v_2$: $v_1=1$ m/s, $v_2=4$ m/s
> **2** equal masses swap: $v_1=2$, $v_2=5$ m/s
> **3** it hits at 6 m/s, leaves at $0.5\times6=3$ m/s, rises $\frac{9}{20}=0.45$ m ($e^2$ times the height)

see also [[Momentum]], [[Perfectly inelastic collisions]]

related beyond class 11: [[FIB]]: ion beams knock atoms out by elastic collisions (a light ion hands a heavy atom little energy, equal masses hand over everything)

hub: [[Work, energy and power]]
