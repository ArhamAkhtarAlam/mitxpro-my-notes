#mechanics #momentum #impulse #worked_example
## a big force for a short time
in a hit, the force is huge and brief, and you usually don't know it at every instant. but integrate $F=\frac{dp}{dt}$ ([[Variable mass systems#^force-momentum]]) over the time of the hit and you get something easy:
$$
\vec J=\int\vec F\,dt=\vec p_f-\vec p_i=\Delta\vec p
$$
^impulse

the **impulse** $\vec J$ (units N s = kg m/s) is the area under the $F$–$t$ graph, and it equals the change in momentum. part of [[Rotational mechanics]]

> [!important] the one idea
> ==impulse = area under force vs time = change in momentum. you never need the force itself, only its total effect==

## a force that grows with time
a 2 kg particle moving at $\vec v=20\hat i+20\hat j$ m/s gets hit by $\vec F=2\times10^3t\,\hat i+4\times10^3t\,\hat j$ N for 0.1 s
$$
\begin{aligned}
\vec J&=\int_0^{0.1}\vec F\,dt=2\times10^3\frac{(0.1)^2}{2}\hat i+4\times10^3\frac{(0.1)^2}{2}\hat j=10\hat i+20\hat j\ \text{N s}\\
\Delta\vec v&=\frac{\vec J}{m}=5\hat i+10\hat j\\
\vec v_f&=25\hat i+30\hat j\ \text{m/s},\qquad\vec p_f=50\hat i+60\hat j\ \text{kg m/s}
\end{aligned}
$$

## impulse from an x–t graph
a 2 kg particle's position follows straight line pieces: up at 100 m/s (slope), flat, down at 100 m/s, up again, flat. the velocity is the **slope**, so an impulse acts only at the **corners**, where the slope jumps: $J=m(\text{slope after}-\text{slope before})$

![[Impulse_x_t_graph.png]]

| point | slope before → after | impulse |
|---|---|---|
| A (start) | $0\to+100$ | $+200$ N s |
| B (middle of a line) | $+100\to+100$ | $0$ |
| C | $+100\to0$ | $-200$ N s |
| D (middle of flat) | $0\to0$ | $0$ |
| E | $0\to-100$ | $-200$ N s |
| F (bottom corner) | $-100\to+100$ | $+400$ N s |
| G | $+100\to+100$ | $0$ |
| H | $+100\to0$ | $-200$ N s |

## impulse from an F–t graph
the force rises steadily from 0 to $20\times10^3$ N in 2 ms, stays there until 4 ms, then falls along a straight line through 0 at 5 ms down to $-20\times10^3$ N at 6 ms

![[Impulse_F_t_graph.png]]

areas (1 ms × $20\times10^3$ N $=20$ N s):
$$
\begin{aligned}
J_{0\to5}&=\underbrace{\tfrac12(2)(20)}_{\text{rise}}+\underbrace{2(20)}_{\text{flat}}+\underbrace{\tfrac12(1)(20)}_{\text{fall}}=20+40+10=70\ \text{N s}\\
J_{5\to6}&=-\tfrac12(1)(20)=-10\ \text{N s}\\
J_{0\to6}&=70-10=60\ \text{N s}
\end{aligned}
$$

area below the axis counts as **negative** impulse

> [!exercise] try these
> **1** a 0.15 kg cricket ball at 20 m/s is hit straight back at 30 m/s. impulse? if the contact lasts 5 ms, average force?
> **2** a 3 kg body's $x$–$t$ graph has slope 4 m/s, then turns sharply to slope $-2$ m/s. impulse at the corner?
> **3** a force of 10 N acts for 2 s, then 20 N for 1 s, on a 5 kg body at rest. final speed?

> [!answer]-
> **1** $0.15\times50=7.5$ N s; $F=\frac{7.5}{0.005}=1500$ N
> **2** $3(-2-4)=-18$ N s
> **3** $J=20+20=40$ N s, $v=8$ m/s

see also [[Coefficient of restitution]], [[Variable mass systems]]

hub: [[Rotational mechanics]]
