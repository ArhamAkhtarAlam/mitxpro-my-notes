#vlsi #formulas #diffraction #XRD
every formula for [[XRD]]. electron diffraction in the [[TEM]] uses the same idea, see [[Microscopy formulas#TEM]]. formulas that live in the XRD note are embedded from there, the extra ones are written out here. part of [[Metrology and nano-characterization workshop]]
## Bragg's law

![[XRD#^bragg]]

Cu $K_{\alpha1}$: $\lambda=1.5406$ Å (average $K_\alpha$ = 1.5418 Å). where it comes from: [[EDS#^moseley|Moseley's law]]
## plane spacing for each crystal system
cubic (worked for Si (400) in [[XRD#cubic crystals]])

![[XRD#^d-spacing]]

tetragonal and hexagonal
$$
\frac1{d^2}=\frac{h^2+k^2}{a^2}+\frac{l^2}{c^2}\qquad\qquad\frac1{d^2}=\frac43\,\frac{h^2+hk+k^2}{a^2}+\frac{l^2}{c^2}
$$
^d-spacing-other

> [!eg]- GaN (hexagonal, $a=3.189$ Å, $c=5.185$ Å), the (002) peak
> $\frac1{d^2}=0+\frac{4}{5.185^2}$, so $d=\frac{5.185}2=2.593$ Å, $\sin\theta=\frac{1.5406}{2\times2.593}=0.297$, $2\theta=34.6^\circ$

## lattice parameter from a peak
$$
a=d\sqrt{h^2+k^2+l^2}
$$
^lattice-parameter

## scattering vector
$$
q=\frac{4\pi\sin\theta}\lambda\qquad|G|=\frac{2\pi}d
$$
^scattering-vector

(Bragg condition: $q=|G|$. ==$G$ is a point of the reciprocal lattice, ie. a frequency in the crystal's Fourier transform==, that's the whole idea of [[XRD#the quantum connection]])
## structure factor and allowed peaks
$$
F_{hkl}=\sum_jf_j\,e^{2\pi i(hx_j+ky_j+lz_j)}\qquad I\propto|F_{hkl}|^2
$$
^structure-factor

- $f_j$ → atomic scattering factor of atom $j$ at fractional position $(x_j,y_j,z_j)$
- **diamond cubic (Si, Ge)**: allowed if $h,k,l$ are all odd, or all even with $h+k+l=4n$ → (111), (220), (311), (400) are allowed, **(200) is forbidden**
- fcc: $h,k,l$ all odd or all even. bcc: $h+k+l$ even

> [!eg]- why bcc (100) is missing
> bcc has atoms at $(0,0,0)$ and $(\frac12,\frac12,\frac12)$
> $$
> \begin{aligned}
> F_{hkl}&=f\left(1+e^{\pi i(h+k+l)}\right)\\
> (100):\quad F&=f(1+e^{\pi i})=f(1-1)=0\\
> (110):\quad F&=f(1+e^{2\pi i})=2f
> \end{aligned}
> $$
> the atom in the middle sits exactly halfway between the (100) planes and scatters exactly out of phase, so it cancels. this sum of phases $e^{2\pi i(\ldots)}$ is a [[Discrete Fourier Transform]] of the atoms in the cell, and the cancellation is the same **interference** that makes amplitudes cancel in a quantum algorithm

## crystallite size (Scherrer)

![[XRD#^scherrer]]

worked ($0.4^\circ$ → 21 nm) in [[XRD#Scherrer equation]]
## size and strain together (Williamson–Hall)
$$
\beta\cos\theta=\frac{K\lambda}D+4\varepsilon\sin\theta
$$
^williamson-hall

plot $\beta\cos\theta$ vs $\sin\theta$ for several peaks: intercept → size, slope → microstrain $\varepsilon$. (size broadening doesn't change with angle, strain broadening grows with it, so two or more peaks can tell them apart)
## strain from a peak shift
$$
\varepsilon=\frac{\Delta d}d=-\cot\theta\,\Delta\theta
$$
^peak-shift-strain

peak moves to lower $2\theta$ → bigger $d$ → tensile
> [!eg]- Si (400) moves from $2\theta=69.13^\circ$ to $69.00^\circ$
> $\Delta\theta=-0.065^\circ=-1.13\times10^{-3}$ rad, $\cot34.56^\circ=1.45$, so $\varepsilon=1.45\times1.13\times10^{-3}=0.16\%$ tensile (the same answer as [[XRD#limits|the XRD exercise]] ②, done the long way there)

## strain in an epitaxial film
mismatch
$$
f=\frac{a_s-a_f}{a_f}
$$
^mismatch

for biaxial strain, the out of plane strain follows the in plane
$$
\varepsilon_\perp=-\frac{2\nu}{1-\nu}\,\varepsilon_\parallel
$$
^biaxial-strain

(squeeze a film sideways and it gets taller, $\nu$ is Poisson's ratio. that's why the RSM sees both $Q_x$ and $Q_z$ change)

degree of relaxation (worked in [[XRD#strain and relaxation: reciprocal space map]])

![[XRD#^relaxation]]

## alloy composition (Vegard's law, SiGe)
$$
a(\text{Si}_{1-x}\text{Ge}_x)\approx(1-x)\,a_{Si}+x\,a_{Ge}
$$
^vegard

$a_{Si}=5.431$ Å, $a_{Ge}=5.658$ Å (real alloys have a small bowing: $a=5.431+0.2x+0.027x^2$)
> [!eg]- a relaxed SiGe layer measures $a=5.475$ Å
> $x=\frac{5.475-5.431}{5.658-5.431}=\frac{0.044}{0.227}=0.19$, so about Si$_{0.81}$Ge$_{0.19}$. on Si its mismatch is $f=\frac{5.431-5.475}{5.475}=-0.8\%$: it wants to be bigger, so on Si it's squeezed (compressive)

## XRR (reflectivity, thin film thickness)
$$
\theta_c\approx\sqrt{2\delta}\qquad\theta_m^2=\theta_c^2+\left(\frac{m\lambda}{2t}\right)^2\qquad t\approx\frac\lambda{2\,\Delta\theta}
$$
^xrr

- $\theta_c$ → critical angle for total external reflection ($\delta$ ∝ electron density)
- $\Delta\theta$ → spacing between neighbouring Kiessig fringes (in radians)
- $t$ → film thickness

> [!eg]- fringes $0.05^\circ$ apart with Cu $K_\alpha$
> $t\approx\frac{0.15406\ \text{nm}}{2\times0.05\times\frac\pi{180}}=\frac{0.15406}{1.745\times10^{-3}}=88$ nm. thinner film → wider fringes. (same idea as the [[UV-vis spectroscopy#^fringe-thickness|UV-vis fringes]], with X-rays at grazing angles)

## practice
> [!exercise] mixed
> ① which of Si's (111), (200), (220) give peaks?
> ② a peak is broadened by both size and strain. how do you separate them?
> ③ a SiGe film has $x=0.30$. what's its relaxed lattice parameter (no bowing)?

> [!answer]-
> ① (111) all odd ✅, (200) all even but $h+k+l=2$ isn't a multiple of 4 ❌, (220) sum 4 ✅
> ② measure several peaks and make a Williamson–Hall plot ([[#^williamson-hall]])
> ③ $0.7\times5.431+0.3\times5.658=5.499$ Å

see also [[Microscopy formulas]], [[Spectroscopy formulas]], [[Electrical formulas]], [[Metrology and nano-characterization workshop]]
