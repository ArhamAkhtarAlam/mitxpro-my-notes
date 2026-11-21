#mechanics #centre_of_mass
## from sums to integrals
for a solid body, chop it into tiny pieces $dm$ and the sums of [[Centre of mass#^cm-position]] become integrals: $\bar x=\frac{\int x\,dm}{\int dm}$. for uniform bodies $dm$ is just proportional to a length, area or volume, so the density cancels. part of [[Rotational mechanics]]

the trick in each case: pick a strip whose own centre you already know

| shape | strip | $(\bar x,\bar y)$ |
|---|---|---|
| area under $y(x)$, $a\le x\le b$ | vertical strip, height $y$, centre at $(x,\frac y2)$ | $\left(\dfrac{\int_a^bxy\,dx}{\int_a^by\,dx},\ \dfrac{\frac12\int_a^by^2\,dx}{\int_a^by\,dx}\right)$ |
| area beside $x(y)$ | horizontal strip, length $x$ | $\left(\dfrac{\frac12\int x^2\,dy}{\int x\,dy},\ \dfrac{\int xy\,dy}{\int x\,dy}\right)$ |
| area in polar, $r(\theta)$, $\alpha\le\theta\le\beta$ | thin triangle, centre at $\frac23r$ | $\left(\dfrac{\frac23\int r^3\cos\theta\,d\theta}{\int r^2\,d\theta},\ \dfrac{\frac23\int r^3\sin\theta\,d\theta}{\int r^2\,d\theta}\right)$ |
| a curve (thin wire) | tiny arc $ds$ | $\left(\dfrac{\int x\,ds}{\int ds},\ \dfrac{\int y\,ds}{\int ds}\right)$ |
| solid of revolution about $x$ | disc of area $\pi y^2$ | $\left(\dfrac{\int_a^bxy^2\,dx}{\int_a^by^2\,dx},\ 0\right)$ |
| surface of revolution about $x$ | ring of area $2\pi y\,ds$ | $\left(\dfrac{\int xy\,ds}{\int y\,ds},\ 0\right)$ |

($ds=\sqrt{dx^2+dy^2}$ is a tiny length along the curve)

> [!important] the one idea
> ==every centre of mass integral is the same: (position of a strip × its size) summed, divided by the total size==. choose strips so you already know where each strip's own centre is

## results worth knowing
![[Centre_of_mass_shapes.png]]

| body | centre of mass |
|---|---|
| sector of a circle, radius $a$, angle $2\alpha$ | $\frac{2a\sin\alpha}{3\alpha}$ from the centre |
| semicircular plate ($\alpha=\frac\pi2$) | $\frac{4a}{3\pi}$ from the centre |
| arc of a circle, angle $2\alpha$ (wire) | $\frac{a\sin\alpha}{\alpha}$ from the centre |
| semicircular wire | $\frac{2a}{\pi}$ |
| solid hemisphere | $\frac{3a}{8}$ from the flat face |
| hollow hemisphere (bowl) | $\frac a2$ from the flat face |
| solid cone, height $H$ | $\frac H4$ from the base |
| hollow cone (surface only) | $\frac H3$ from the base |

> [!eg] the solid hemisphere with the disc formula
> spin $y=\sqrt{a^2-x^2}$ ($0\le x\le a$) about the $x$ axis:
> $$
> \bar x=\frac{\int_0^ax(a^2-x^2)\,dx}{\int_0^a(a^2-x^2)\,dx}=\frac{a^4/4}{2a^3/3}=\frac{3a}{8}
> $$

> [!exercise] try these
> ① find $\bar x$ for the area under $y=x^2$ from $0$ to $1$
> ② a solid cone, height 12 cm, stands on its base. how high is its centre of mass?
> ③ use the sector formula to check the semicircular plate result

> [!answer]-
> ① $\frac{\int_0^1x^3dx}{\int_0^1x^2dx}=\frac{1/4}{1/3}=\frac34$
> ② $\frac{12}{4}=3$ cm
> ③ $\alpha=\frac\pi2$: $\frac{2a\cdot1}{3\pi/2}=\frac{4a}{3\pi}$ ✓

see also [[Centre of mass]]

hub: [[Rotational mechanics]]
