#vlsi #formulas #microscopy
every formula for the microscopy notes: [[Electron microscope]], [[SEM]], [[TEM]], [[FIB]], [[AFM]], [[MSA]]. formulas that live in a topic note are embedded from there (with a link to its worked example), the extra ones are written out here. part of [[Metrology and nano-characterization workshop]]
## electron microscope (shared)
### resolution limit

![[Electron microscope#^resolution-limit]]

worked examples (light vs a TEM): [[Electron microscope#why electrons have a short wavelength]]
### de Broglie wavelength

![[SEM#^de-broglie]]

relativistic (needed above ~50 kV), worked at 200 kV in [[TEM#the wavelength]]

![[TEM#^relativistic-wavelength]]

### lens aberrations
- spherical: $r_s=C_s\alpha^3$
- chromatic: $r_c=C_c\alpha\dfrac{\Delta E}{E_0}$
- diffraction: $r_d=\dfrac{0.61\lambda}{\alpha}$
- best compromise (spherical gets worse with a bigger $\alpha$, diffraction gets worse with a smaller one)

$$
\alpha_{opt}\approx0.77\left(\frac{\lambda}{C_s}\right)^{1/4}\qquad d_{min}\approx0.91\left(C_s\lambda^3\right)^{1/4}
$$
^aberrations

## SEM
### magnification and pixel size
$$
M=\frac{L_{display}}{L_{scan}}\qquad\text{pixel size}=\frac{L_{scan}}{N_{pixels}}
$$
^magnification

### charge balance and yields
$$
i_B=i_{BSE}+i_{SE}+i_S\qquad\delta=\frac{i_{SE}}{i_B}\qquad\eta=\frac{i_{BSE}}{i_B}
$$
^electron-yields

- no charging when $\delta+\eta=1$ (as many electrons leave as arrive, that's why low kV helps insulators, [[SEM#problems]])
- $\eta$ goes up with $Z$ (≈0.05 for C, ≈0.5 for Au)
### contrast and noise
$$
C=\frac{S_A-S_B}{S_A}\qquad SNR=\sqrt N,\ \ N=\frac{i_Bt}{e}
$$
^sem-snr

$t$ → dwell time per pixel
> [!eg]- 100 pA beam, 10 µs per pixel
> $N=\frac{(100\times10^{-12})(10\times10^{-6})}{1.602\times10^{-19}}=6240$ electrons, $SNR=\sqrt{6240}=79$. ==to double the SNR you need 4× the electrons==: 4× the dwell time (more drift) or 4× the current (bigger spot)

### interaction depth (Kanaya–Okayama)
$$
R=\frac{0.0276\,A\,E_0^{1.67}}{Z^{0.889}\rho}\ \ \mu\text{m}
$$
^kanaya-okayama

$E_0$ in keV, $A$ in g/mol, $\rho$ in g/cm³
> [!eg]- silicon at 20 kV
> $$
> R=\frac{0.0276\times28.09\times20^{1.67}}{14^{0.889}\times2.33}=\frac{0.0276\times28.09\times148.9}{10.44\times2.33}\approx4.7\ \mu\text{m}
> $$
> at 5 kV only ~0.47 µm. that's why [[EDS]] in an SEM can't see anything smaller than ~1 µm

### probe size
$$
d_{eff}=\sqrt{d_g^2+d_s^2+d_c^2+d_d^2}
$$
^probe-size

(geometric, spherical, chromatic, diffraction. the same "add in quadrature" rule as [[XPS#^xps-resolution|XPS peak widths]])
## TEM
### Bragg's law (electrons) and spacing

![[XRD#^bragg]]

![[XRD#^d-spacing]]

for electrons $\theta$ is tiny, so $\theta\approx\frac\lambda{2d}$. worked for Si (111) in [[TEM#Bragg's law in a TEM]]
### camera equation (diffraction pattern)
$$
Rd=\lambda L
$$
^camera-equation

- $R$ → distance from the centre spot to a diffracted spot on the screen, $L$ → camera length
> [!eg]- 200 kV ($\lambda=2.51$ pm), planes with $d=0.2$ nm, $L=1$ m
> $\theta=\frac\lambda{2d}=6.3$ mrad (0.36°), and the spot lands $R=\frac{\lambda L}d=\frac{2.51\times10^{-12}\times1}{0.2\times10^{-9}}=12.6$ mm from the centre. measure $R$, know $\lambda L$ (the "camera constant"), get $d$

### mass-thickness contrast
$$
I=I_0\,e^{-t/\Lambda}
$$
^mass-thickness

$\Lambda$ → mean free path for scattering (the same exponential as [[UV-vis spectroscopy#Beer–Lambert law|Beer–Lambert]]. a sample half a mean free path thick lets $e^{-0.5}=61\%$ through unscattered)
### HAADF STEM
$$
I_{HAADF}\propto Z^{n},\quad n\approx1.6\text{–}2
$$
^haadf

### EELS
the energy loss as in [[REELS and other XPS modes#REELS: reflection electron energy loss spectroscopy|REELS]], but for transmitted electrons

![[REELS and other XPS modes#^energy-loss]]

thickness from the zero loss peak $I_0$ ($\lambda$ → inelastic mean free path)
$$
\frac t\lambda=\ln\frac{I_{total}}{I_0}
$$
^eels-thickness

## FIB
### ion energy and mass
$$
E=qV\qquad\frac{m_{Ga}}{m_e}\approx69.72\times1823\approx1.3\times10^5
$$
^ion-mass

### how much energy one collision can hand over

![[FIB#^max-energy-transfer]]

worked (Ga vs electron on Si) in [[FIB#why ions cut and electrons don't]]
### ions per second and dose
$$
\dot N=\frac Iq\qquad D=\frac{It}{qA}\ \ [\text{ions/cm}^2]
$$
^ion-dose

### sputter yield and milling rate
$$
Y=\frac{\text{atoms removed}}{\text{incident ion}}\qquad\frac{dV}{dt}=Y\,\frac Iq\,\frac{M}{\rho N_A}\qquad t=\frac{V}{dV/dt}
$$
^milling-rate

$M/(\rho N_A)$ → volume of one atom
> [!eg]- Si at 1 nA, $Y\approx2.5$
> $$
> \begin{aligned}
> \text{volume per atom}&=\frac{28.09}{2.33\times6.022\times10^{23}}\ \text{cm}^3=0.020\ \text{nm}^3\\
> \frac{dV}{dt}&=2.5\times\frac{10^{-9}}{1.602\times10^{-19}}\times0.020=2.5\times6.2\times10^9\times0.020\approx3\times10^8\ \text{nm}^3/\text{s}\approx0.3\ \mu\text{m}^3/\text{s}
> \end{aligned}
> $$
> a $10\times10\times5\ \mu$m trench ($500\ \mu\text{m}^3$) → ~27 min (slower in practice, redeposition)

### ion range
$R_p\approx20\text{–}30$ nm for 30 kV Ga in Si (from SRIM), the depth of the damaged layer ([[FIB#downsides]])
## AFM
### cantilever spring (Hooke)

![[AFM#^hooke]]

for a rectangular beam ($E$ Young's modulus, Si ≈ 169 GPa, $w$ width, $t$ thickness, $L$ length)
$$
k=\frac{E\,w\,t^3}{4L^3}
$$
^cantilever-stiffness

> [!eg]- $w=30$ µm, $t=4$ µm, $L=125$ µm
> $k=\frac{169\times10^9\times30\times10^{-6}\times(4\times10^{-6})^3}{4\times(125\times10^{-6})^3}\approx42$ N/m, a stiff tapping cantilever. the $t^3$ means ==half the thickness = 8× softer==

### resonant frequency

![[AFM#^cantilever-resonance]]

for a rectangular beam
$$
f_0\approx0.1615\,\frac t{L^2}\sqrt{\frac E\rho}
$$
^beam-resonance

> [!eg]- tapping Si cantilever
> $t=4\ \mu$m, $L=125\ \mu$m, $\rho=2330$ kg/m³
> $$
> f_0=0.1615\times\frac{4\times10^{-6}}{(125\times10^{-6})^2}\times\sqrt{\frac{169\times10^9}{2330}}=0.1615\times256\times8517\approx350\text{ kHz}
> $$

### optical lever (laser detection)
$$
\Delta y\approx\frac{3Dz}L\qquad\text{signal}=\frac{(A+B)-(C+D)}{A+B+C+D}
$$
^optical-lever

$D$ → cantilever to photodiode distance, $A$–$D$ → quadrants
> [!eg]- $D=3$ cm, $L=125$ µm, tip moves $z=1$ nm
> $\Delta y=\frac{3\times0.03\times10^{-9}}{125\times10^{-6}}=0.72$ µm on the photodiode, a 700× magnification for free

### tip-sample force

![[AFM#^lennard-jones]]

van der Waals between a sphere (tip radius $R$, Hamaker constant $H$) and a flat surface at distance $z$
$$
F_{vdW}=-\frac{HR}{6z^2}
$$
^van-der-waals

### quality factor and thermal noise

![[MSA#^quality-factor]]

$$
\langle z^2\rangle=\frac{k_BT}{k}
$$
^thermal-noise

> [!eg]- 300 K
> $k=40$ N/m → $\sqrt{\frac{1.38\times10^{-23}\times300}{40}}=0.010$ nm noise. $k=0.1$ N/m → 0.2 nm. soft cantilevers feel small forces but jiggle more

### roughness

![[AFM#^roughness]]

### tip convolution
$$
W_{apparent}\approx4\sqrt{Rr}
$$
^tip-convolution

sphere of radius $r$ imaged by a tip of radius $R$. eg. a 5 nm particle ($r=5$) with a 10 nm tip looks $4\sqrt{50}=28$ nm wide, but its **height** is still right
## MSA
### Doppler shift

![[MSA#^doppler]]

worked (1 mm/s → 3.2 kHz) in [[MSA#LDV]]
### velocity to displacement
$$
d(t)=\int v\,dt\qquad d_{peak}=\frac{v_{peak}}{2\pi f}
$$
^peak-displacement

### interferometer phase
$$
\varphi=\frac{4\pi\Delta z}{\lambda}
$$
^interferometer-phase

one fringe ($2\pi$) = $\lambda/2$ of height, because the light goes there and back
### white light interferometry
$$
L_c\approx\frac{\lambda_0^2}{\Delta\lambda}
$$
^coherence-length

(worked in [[MSA#white light interferometry]])
### beam modes
$$
f_n=\frac{\beta_n^2}{2\pi}\frac t{L^2}\sqrt{\frac E{12\rho}}\qquad\beta_1=1.875,\ \beta_2=4.694,\ \beta_3=7.855
$$
^beam-modes

the modes aren't harmonics: $f_2=\left(\frac{4.694}{1.875}\right)^2f_1=6.27f_1$, $f_3=17.6f_1$
### $Q$ and damping
$$
\zeta=\frac1{2Q}
$$
^damping

eg. $f_0=50$ kHz, $\Delta f=100$ Hz → $Q=500$, $\zeta=0.001$
### driven resonator
$$
A(f)=\frac{F_0/k}{\sqrt{\left(1-\frac{f^2}{f_0^2}\right)^2+\left(\frac f{Qf_0}\right)^2}}\qquad A_{res}=Q\,\frac{F_0}k
$$
^driven-resonator

### stroboscopic phase
$$
\varphi=360^\circ\times f\,t_d
$$
^strobe-phase

### residual stress (Stoney)
$$
\sigma_f=\frac{E_s\,t_s^2}{6(1-\nu_s)\,t_f\,R}
$$
^stoney

> [!eg]- a 1 µm film bends a 500 µm Si wafer to a 50 m radius ($E_s=169$ GPa, $\nu_s=0.064$)
> $\sigma_f=\frac{169\times10^9\times(500\times10^{-6})^2}{6(0.936)(10^{-6})(50)}=150$ MPa

## practice
> [!exercise] mixed
> ① what's the electron wavelength at 2 kV, and why does a low kV SEM still resolve ~1 nm?
> ② an SAED spot is 8.0 mm from the centre with $\lambda L=2.51$ pm·m. what's $d$?
> ③ how long to mill a 5×5×2 µm box in Si at 1 nA?
> ④ a cantilever is made twice as long. what happens to $k$ and $f_0$?

> [!answer]-
> ① $\frac{1.226}{\sqrt{2000}}=0.027$ nm. resolution is set by the spot and interaction volume, not $\lambda$, and low kV shrinks the interaction volume ([[#^kanaya-okayama]])
> ② $d=\frac{\lambda L}R=\frac{2.51\times10^{-12}}{8.0\times10^{-3}}=0.31$ nm
> ③ $V=50\ \mu\text{m}^3$, at 0.3 µm³/s → ~170 s, about 3 min
> ④ $k\propto\frac1{L^3}$ → 8× softer. $f_0\propto\frac1{L^2}$ → 4× lower

see also [[Spectroscopy formulas]], [[Diffraction formulas]], [[Electrical formulas]], [[Metrology and nano-characterization workshop]]
