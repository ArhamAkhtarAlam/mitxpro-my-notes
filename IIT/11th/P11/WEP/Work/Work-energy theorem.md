#mechanics #work #energy #worked_example
## the theorem
the **total** work done by **all** the forces on a body equals the change in its kinetic energy
$$
W_\text{total}=\Delta K=\tfrac12mv^2-\tfrac12mu^2
$$
^work-energy

why: the total work is the work of the net force, $F_\text{net}=ma$, and with constant $a$, $v^2=u^2+2as$, so $F_\text{net}\,s=ma\,s=\tfrac12m(v^2-u^2)$. it holds for variable forces too ([[Work by a variable force]]). part of [[Work, energy and power]]

> [!important] the one idea
> ==add up the work of every force (pull, gravity, friction, normal...) and you get exactly the change in kinetic energy==. forces that do negative work (friction, gravity going up) take KE away

the recipe for every problem below:
1. draw all the forces (free body diagram), find the acceleration from $F_\text{net}=ma$ ([[Newton's laws of motion]])
2. find the displacement from $s=ut+\tfrac12at^2$
3. work of each force: $W=Fs\cos\theta$ ([[Work done by a force#^work-dot]])
4. add them up and compare with $\tfrac12mv^2-\tfrac12mu^2$

all start from rest, $g=10\,\text{m/s}^2$, run for 2 s

## **1** pulled along a rough floor
a 2 kg block, a $10\sqrt2$ N pull at $45°$ above the horizontal, $\mu_k=0.1$
- the pull has parts $10\sqrt2\cos45°=10$ N forward and $10$ N up
- vertical: $N+10=20$, so $N=10$ N (the pull lifts some of the weight, so friction is smaller)
- friction $f=\mu_kN=1$ N, so $10-1=2a$, $a=4.5\,\text{m/s}^2$
- in 2 s: $s=\tfrac12(4.5)(2^2)=9$ m, $v=9$ m/s

watch the bars: the pull adds energy, friction takes a bit away, gravity and the normal force do nothing, and the total always matches the KE:

![[Work_energy_floor_animation.png]]

$$
\begin{aligned}
W_\text{pull}&=10\times9=90\ \text{J}\qquad W_f=1\times9\times\cos180°=-9\ \text{J}\qquad W_g=W_N=0\\
W_\text{total}&=90-9=81\ \text{J}\\
\Delta K&=\tfrac12(2)(9^2)-0=81\ \text{J}\ ✓
\end{aligned}
$$

## **2** pushed up a smooth 30° slope
2 kg, force $F$ along the slope, it accelerates **up** at $2\,\text{m/s}^2$
- along the slope: $F-mg\sin30°=ma$, so $F-10=4$, $F=14$ N
- ⊥ to the slope: $N=mg\cos30°=10\sqrt3$ N
- in 2 s: $s=\tfrac12(2)(4)=4$ m, $v=4$ m/s

$$
\begin{aligned}
W_F&=14\times4=56\ \text{J}\qquad W_N=0\qquad W_g=20\times4\times\cos120°=-40\ \text{J}\\
W_\text{total}&=56-40=16\ \text{J}\\
\Delta K&=\tfrac12(2)(4^2)=16\ \text{J}\ ✓
\end{aligned}
$$

## **3** held back on a rough 60° slope
2 kg, $\mu_k=0.1$, a force $F$ up the slope, and the block slides **down** with $a=0.4\,\text{m/s}^2$
- ⊥ to the slope: $N=mg\cos60°=10$ N, so $f=1$ N, pointing **up** the slope (against the motion)
- along the slope (down = positive): $mg\sin60°-F-f=ma$, so $10\sqrt3-F-1=0.8$, $F=10\sqrt3-1.8\approx15.5$ N
- in 2 s: $s=\tfrac12(0.4)(4)=0.8$ m down the slope, $v=0.8$ m/s

$$
\begin{aligned}
W_F&=-(10\sqrt3-1.8)(0.8)=-8\sqrt3+1.44\ \text{J}\quad\text{(F points up, motion is down)}\\
W_f&=-1\times0.8=-0.8\ \text{J}\qquad W_N=0\\
W_g&=20\times0.8\times\cos30°=+8\sqrt3\ \text{J}\quad\text{(gravity is }30°\text{ from the motion)}\\
W_\text{total}&=-8\sqrt3+1.44-0.8+8\sqrt3=0.64\ \text{J}\\
\Delta K&=\tfrac12(2)(0.8^2)=0.64\ \text{J}\ ✓
\end{aligned}
$$

## **4** pushed horizontally up a rough 30° slope
2 kg, $\mu_k=0.1$, a **horizontal** force $F$, the block goes up the slope at $a=2\,\text{m/s}^2$. now $F$ also presses the block into the slope, so it changes $N$ and the friction
- ⊥ to the slope: $N=mg\cos30°+F\sin30°=10\sqrt3+\frac F2$
- along the slope: $F\cos30°-mg\sin30°-\mu_kN=ma$

$$
\begin{aligned}
\tfrac{\sqrt3}{2}F-10-0.1\left(\tfrac F2+10\sqrt3\right)&=4\\
F\left(\tfrac{\sqrt3}{2}-\tfrac{0.1}{2}\right)&=14+\sqrt3\\
F&=\frac{2(14+\sqrt3)}{\sqrt3-0.1}\approx19.3\ \text{N}
\end{aligned}
$$

so $N\approx27.0$ N and $f\approx2.7$ N. in 2 s, $s=4$ m and $v=4$ m/s:

![[Work_energy_incline_animation.png]]

$$
\begin{aligned}
W_F&=F\cos30°\times4\approx66.8\ \text{J}\qquad W_g=-40\ \text{J}\qquad W_f\approx-10.8\ \text{J}\qquad W_N=0\\
W_\text{total}&\approx66.8-40-10.8=16\ \text{J}=\Delta K\ ✓
\end{aligned}
$$

> [!eg] the same 16 J twice
> **2** and **4** both end at 4 m/s after 4 m, so both have $\Delta K=16$ J. the forces are completely different (**4** pushes harder, but wastes some of it pressing into the slope and on friction); the **total** comes out the same

> [!exercise] try these
> **1** a 1 kg ball is thrown straight up at 10 m/s. use the theorem to find how high it goes
> **2** a 4 kg block slides 5 m on a floor with $\mu_k=0.2$ and stops. how fast was it going?
> **3** in **1** of the worked problems, what would the KE be after 2 s if the floor were smooth?

> [!answer]-
> **1** only gravity works: $-mgh=0-\tfrac12mu^2$, $h=\frac{u^2}{2g}=5$ m
> **2** $-\mu_kmgs=0-\tfrac12mu^2$: $u=\sqrt{2\mu_kgs}=\sqrt{20}\approx4.5$ m/s
> **3** $a=5\,\text{m/s}^2$, $s=10$ m, $W=10\times10=100$ J $=\Delta K$ (check: $v=10$, $\tfrac12(2)(100)=100$ ✓)

see also [[Work done by a force]], [[Friction]], [[Conservation of mechanical energy]]

related beyond class 11: [[SEM]]: an electron accelerated through a voltage $V$ gains $K=eV$, the work the electric field did

hub: [[Work, energy and power]]
