#mechanics #work
## work by a constant force
a force $\vec F$ moves something through a displacement $\vec s$. the **work** it does is the dot product: only the part of the force **along** the motion counts
$$
W=\vec F\cdot\vec s=Fs\cos\theta
$$
^work-dot

$\theta$ is the angle between the force and the displacement. unit: joule, $1\,\text{J}=1\,\text{N m}$. work is a **scalar** (a number, no direction), but it can be negative. part of [[Work, energy and power]]

| angle | $\cos\theta$ | work | the force... |
|---|---|---|---|
| $0°$ | $1$ | $+Fs$ (most) | pushes along the motion: speeds it up |
| $0°<\theta<90°$ | $+$ | positive | helps |
| $90°$ | $0$ | **zero** | is sideways: does nothing to the speed |
| $90°<\theta<180°$ | $-$ | negative | fights the motion |
| $180°$ | $-1$ | $-Fs$ | pushes straight back (eg. kinetic friction) |

> [!important] the one idea
> ==a force does work only through its component along the displacement: a force at right angles to the motion does zero work, however big it is==

so these forces do **no** work:
- the **normal force** on a block sliding along a surface (the block moves along the surface, $N$ is ⊥ to it)
- **gravity** on a block moving horizontally
- the **tension** in a pendulum string (the bob moves along a circle, the string points to the centre)
- the **centripetal force** in circular motion (see [[Power in circular motion]])

## in components
with $\vec F=F_x\hat i+F_y\hat j+F_z\hat k$ and $\vec s=\Delta x\,\hat i+\Delta y\,\hat j+\Delta z\,\hat k$, the dot product is just
$$
W=F_x\Delta x+F_y\Delta y+F_z\Delta z
$$
and with several forces acting at once, add them first (the work of the **net** force is the sum of the separate works)

> [!eg] three constant forces
> $\vec F_1=(3\hat i+4\hat j-2\hat k)$ N, $\vec F_2=(2\hat i+2\hat j)$ N, $\vec F_3=(3\hat i+3\hat j+3\hat k)$ N move a particle from $\vec r_1=2\hat i+2\hat j+2\hat k$ to $\vec r_2=-2\hat i+4\hat k$ (m)
> - net force: $\vec F=8\hat i+9\hat j+\hat k$ N
> - displacement: $\vec s=\vec r_2-\vec r_1=-4\hat i-2\hat j+2\hat k$ m
> - $W=8(-4)+9(-2)+1(2)=-32-18+2=-48$ J
>
> negative: overall the forces pointed **against** the way the particle went

## work by gravity
gravity is $mg$ straight down, so only the **vertical** part of the displacement matters: going down by $h$, gravity does $+mgh$; going up by $h$, it does $-mgh$. the path in between doesn't matter (that's what makes gravity a **conservative** force, see [[Conservation of mechanical energy]])

> [!eg] block moved 4 m up a 30° slope
> $m=2$ kg, $g=10$. the displacement is at $120°$ to gravity (gravity points down, the slope goes $30°$ up): $W=mgs\cos120°=20\times4\times(-\tfrac12)=-40$ J. same as $-mgh$ with $h=4\sin30°=2$ m

> [!exercise] try these
> ① a 5 N force at $60°$ above the horizontal drags a box 4 m along the floor. how much work does it do?
> ② $\vec F=2\hat i-3\hat j$ N moves a particle from $(1,1)$ to $(4,-1)$ m. find $W$
> ③ a satellite goes round in a circle. how much work does gravity do on it in one orbit? in half an orbit?

> [!answer]-
> ① $W=5\times4\times\cos60°=10$ J
> ② $\vec s=3\hat i-2\hat j$, $W=6+6=12$ J
> ③ zero both times: gravity points to the centre, always ⊥ to the velocity

see also [[Work-energy theorem]], [[Work by a variable force]]

hub: [[Work, energy and power]]
