#vlsi #formulas #spectroscopy
every formula for the spectroscopy notes: [[EDS]], [[FTIR]], [[Raman spectroscopy]], [[XPS]], [[UPS]], [[REELS and other XPS modes]], [[UV-vis spectroscopy]]. formulas that live in a topic note are embedded from there (with a link to its worked example), the extra ones are written out here. part of [[Metrology and nano-characterization workshop]]
## the basics (all of them)
photon energy (also $E=h\nu=\frac{hc}\lambda$, and $E[\text{keV}]=\frac{1.2398}{\lambda[\text{nm}]}$ for X-rays)

![[UV-vis spectroscopy#^photon-energy]]

wavenumber (for IR and Raman)
$$
\tilde\nu=\frac1\lambda\ [\text{cm}^{-1}]\qquad\lambda[\mu\text{m}]=\frac{10^4}{\tilde\nu[\text{cm}^{-1}]}\qquad E[\text{eV}]=1.2398\times10^{-4}\,\tilde\nu[\text{cm}^{-1}]
$$
^wavenumber

> [!eg]- the same scale for everything
> 1000 cm⁻¹ = 10 µm = 0.124 eV (an IR vibration). 2 eV = 620 nm (red light, UV-vis). 1486.6 eV = 0.834 nm (Al $K_\alpha$, XPS). ==one formula covers FTIR, Raman, UV-vis, UPS, XPS and EDS==, they just live at different energies

## EDS
### Moseley's law

![[EDS#^moseley]]

worked (Si, Cu) in [[EDS#how it works]], where the 10.2 eV comes from in [[EDS#the quantum connection]]
### overvoltage and intensity
$$
U=\frac{E_0}{E_c}\ (\text{need }U>1,\text{ best }2\text{–}3)\qquad I\propto i_B(U-1)^{1.67}
$$
^overvoltage

> [!eg]- Cu K lines (edge $E_c=8.98$ keV) at 10 kV vs 20 kV
> $U=1.11$ vs $2.23$, intensity ratio $\left(\frac{1.23}{0.11}\right)^{1.67}\approx53$. at 10 kV Cu $K_\alpha$ barely shows up, so use ~20 kV (or the Cu $L$ line at ~0.93 keV)

### quantification
$$
\frac{C_A}{C_{std}}\approx\frac{I_A}{I_{std}}=k\qquad\frac{C_A}{C_{std}}=k\cdot Z\cdot A\cdot F
$$
^eds-quant

($Z$, $A$, $F$ → atomic number, absorption and fluorescence corrections). weight % to atomic %
$$
at\%_i=\frac{w_i/A_i}{\sum_jw_j/A_j}\times100
$$
^weight-to-atomic

### detector resolution
$$
\text{FWHM}=2.355\sqrt{F\varepsilon E+\sigma_{noise}^2}\qquad N=\frac E\varepsilon
$$
^eds-resolution

$F\approx0.115$ (Fano factor), $\varepsilon=3.8$ eV per pair in Si. worked (Mn $K_\alpha$ → ~120 eV) in [[EDS#limits]]
## FTIR
### bond vibration

![[FTIR#^bond-vibration]]

worked (C=O, C–H vs C–D) in [[FTIR#the idea]]
### absorbance (Beer–Lambert)

![[UV-vis spectroscopy#^beer-lambert]]

with transmittance in %: $A=2-\log_{10}(\%T)$, eg. 10% → $A=1$
### interferogram and spectrum

![[FTIR#^interferogram]]

### resolution and sampling

![[FTIR#^ftir-resolution]]

and the mirror has to be sampled finely enough for the highest wavenumber ($\Delta\delta$ → path step)
$$
\tilde\nu_{max}=\frac1{2\Delta\delta}
$$
^ftir-sampling

(the Nyquist rule: at least 2 samples per cycle of the fastest cosine, the same as in the [[Discrete Fourier Transform]])
### ATR penetration depth

![[FTIR#^atr-depth]]

## Raman
### Raman shift

![[Raman spectroscopy#^raman-shift]]

worked (Si with 532/633/785 nm) in [[Raman spectroscopy#the idea]]
### vibrational levels and polarizability

![[Raman spectroscopy#^vibrational-levels]]

![[Raman spectroscopy#^polarizability-change]]

### Stokes / anti-Stokes ratio (temperature)

![[Raman spectroscopy#^stokes-ratio]]

worked (Si at 300 K → 0.10) in [[Raman spectroscopy#Stokes vs anti-Stokes spectrum]]
### intensity
$$
I\propto I_0\,N\,(\tilde\nu_0-\tilde\nu_v)^4\left|\frac{\partial\alpha}{\partial Q}\right|^2
$$
^raman-intensity

needs a change in polarizability $\alpha$ with the vibration coordinate $Q$, and goes up as the 4th power of the frequency (bluer laser → more signal)
### stress shift (Si)
$$
\Delta\omega\approx-2\text{ cm}^{-1}\text{ per GPa}
$$
^raman-stress

tensile lowers, compressive raises (depends on the stress state). worked in [[Raman spectroscopy#classic examples]]
### peak shape
$$
I(\omega)=I_0\frac{(\Gamma/2)^2}{(\omega-\omega_0)^2+(\Gamma/2)^2}
$$
^lorentzian

$\Gamma$ → FWHM (sharper = more crystalline). a Lorentzian: the shape of anything that rings and decays, a phonon with lifetime $\tau$ has $\Gamma\propto\frac1\tau$ (the same linewidth–lifetime link as a qubit's $Q$ in [[MSA#the quantum connection]])
### spot size (confocal)
the [[Electron microscope#^resolution-limit|resolution limit]] again: 532 nm, NA 0.9 → 0.36 µm
### defect distance in graphene
$$
L_D^2[\text{nm}^2]\approx1.8\times10^{-9}\,\lambda_L^4\left(\frac{I_D}{I_G}\right)^{-1}\quad(\lambda_L\text{ in nm})
$$
^graphene-defects

> [!eg]- $I_D/I_G=0.5$ with a 532 nm laser
> $L_D^2=1.8\times10^{-9}\times532^4\times2=288$ nm², $L_D\approx17$ nm between defects. a bigger D peak → defects closer together

## XPS
### photoelectric equation

![[XPS#^xps-energy]]

worked (Cu 2p, Si 2p) in [[XPS#the energy levels]]
### Fermi, vacuum level, work function
$$
\phi=E_{vac}-E_F\qquad BE=E_{core}-E_F\qquad f(E)=\frac1{e^{(E-E_F)/k_BT}+1}
$$
^fermi-dirac

> [!eg]- how sharp is the Fermi edge at 300 K?
> 0.1 eV above $E_F$: $f=\frac1{e^{0.1/0.0259}+1}=\frac1{47.5+1}=0.02$. so within ~±0.1 eV the occupation goes from ~1 to ~0, the smeared edge in [[UPS#the quantum connection]]

### probability of escaping without energy loss

![[XPS#^escape-probability]]

$\lambda=3$ nm: 100%, 36.8%, 13.5%, 5%, 1.8% at $z=0,3,6,9,12$ nm. 63% of the signal comes from the top $\lambda$ and 95% from the top $3\lambda\cos\theta$
### path through an overlayer
$$
L=\frac d{\cos\theta}
$$
^overlayer-path

($d=2$ nm: 2, 4, 7.73 nm at 0°, 60°, 75°)
### ARXPS oxide thickness
substrate peak ratio, worked in [[XPS#angle resolved XPS (ARXPS)]]

![[XPS#^arxps-ratio]]

oxide-to-substrate ratio ($R_\infty$ → the same ratio for infinitely thick layers)

![[XPS#^arxps-overlayer]]

### composition
$$
C_x=\frac{I_x/S_x}{\sum_iI_i/S_i}
$$
^xps-quant

$I$ → peak area, $S$ → sensitivity factor. worked in [[XPS#what you get]]
### spin-orbit doublet area ratios
$$
\frac{I_{j_+}}{I_{j_-}}=\frac{2j_++1}{2j_-+1}
$$
^spin-orbit

p: 2:1, d: 3:2, f: 4:3. why: [[XPS#the quantum connection]]
### analyzer resolution and combining widths
$$
\frac{\Delta E}{E_{pass}}=\frac w{2R_0}+\frac{\alpha^2}4
$$
^analyzer-resolution

($w$ slit width, $R_0$ analyzer radius, $\alpha$ acceptance angle: lower pass energy → narrower $\Delta E$), and the total

![[XPS#^xps-resolution]]

### charge referencing and Auger parameter
$$
\Delta E_{shift}=284.8-BE_{C1s,\,measured}\qquad\alpha'=KE_{Auger}+BE_{photo}
$$
^charge-reference

> [!eg]- an insulator's C 1s shows up at 287.3 eV
> it's charged by $284.8-287.3=-2.5$ eV, so subtract 2.5 eV from every peak. the Auger parameter $\alpha'$ doesn't need this at all: the charging shift cancels between the two terms

## UPS
the same photoelectric equation as XPS, and the work function from the spectrum width (worked for Ag and Si in [[UPS#work function from the spectrum]])

![[UPS#^ups-work-function]]

He I $=21.22$ eV, He II $=40.81$ eV ([[UPS#^ups-lines]])
### KPFM work function

![[UPS#^kpfm]]

calibrate first: $\phi_{tip}=\phi_{ref}+CPD_{ref}$ (worked with HOPG in [[UPS#cross-check with KPFM]])
## REELS and ISS

![[REELS and other XPS modes#^energy-loss]]

onset of loss ≈ $E_g$ (Si: 1.12 eV)

![[REELS and other XPS modes#^iss-kinematic]]

## UV-vis
### absorbance and transmittance
the same Beer–Lambert as FTIR above. $A=1$ → $T=10\%$, $A=2$ → $T=1\%$
### absorption coefficient

![[UV-vis spectroscopy#^absorption-coefficient]]

with reflection from the front and back surfaces
$$
\alpha=-\frac1t\ln\frac{T}{(1-R)^2}
$$
^absorption-reflection

penetration depth $=1/\alpha$
### Tauc plot

![[UV-vis spectroscopy#^tauc]]

$n=\frac12$ (direct), $n=2$ (indirect)
### Kubelka–Munk (diffuse reflectance)
$$
F(R_\infty)=\frac{(1-R_\infty)^2}{2R_\infty}=\frac KS
$$
^kubelka-munk

### Urbach tail
$$
\alpha=\alpha_0\exp\!\left(\frac{E-E_g}{E_U}\right)
$$
^urbach

below the gap the absorption doesn't drop to zero at once, it fades exponentially. a bigger Urbach energy $E_U$ = more disorder (eg. $E_U=50$ meV: 0.1 eV below the gap, $\alpha$ is $e^{-2}=14\%$ of $\alpha_0$)
### thin film thickness from fringes

![[UV-vis spectroscopy#^fringe-thickness]]

### Fresnel reflection (normal incidence)
$$
R=\left(\frac{n-1}{n+1}\right)^2
$$
^fresnel

eg. glass $n=1.5$: $R=4\%$. silicon $n\approx3.9$: $R=35\%$, which is why bare Si wafers look shiny and solar cells need anti-reflection coatings
### quantum dot gap (Brus equation)
$$
E_g(R)\approx E_{g,bulk}+\frac{\hbar^2\pi^2}{2R^2}\left(\frac1{m_e^*}+\frac1{m_h^*}\right)-\frac{1.8\,e^2}{4\pi\varepsilon\varepsilon_0R}
$$
^brus

the middle term is the [[Particle in a box#^energy-levels|particle in a box]] energy ($n=1$) for both the electron and the hole, the last one is their Coulomb attraction
> [!eg]- CdSe dot of radius 2 nm ($m_e^*=0.13$, $m_h^*=0.45$, $\varepsilon=10.6$)
> confinement $\approx0.93$ eV, Coulomb $\approx0.12$ eV, so $E_g\approx1.74+0.93-0.12=2.55$ eV → $\frac{1240}{2.55}=486$ nm, blue-green instead of bulk's deep red (real dots this size are ~2.3–2.4 eV: the simple box overestimates). more in [[UV-vis spectroscopy#the quantum connection]]

## practice
> [!exercise] mixed
> ① a Raman peak at 1332 cm⁻¹ (diamond). what energy is that in meV?
> ② with Al $K_\alpha$, O 1s ($BE=531$ eV) comes out at what $KE$ (take $\phi=4.5$ eV)?
> ③ what fraction of XPS signal comes from deeper than 2λ?
> ④ a film shows $R=10\%$ reflection and $T=50\%$, $t=1$ µm. what's $\alpha$ with and without the reflection correction?

> [!answer]-
> ① $1.2398\times10^{-4}\times1332=0.165$ eV $=165$ meV ([[#^wavenumber]])
> ② $1486.6-531-4.5=951.1$ eV
> ③ $e^{-2}=13.5\%$
> ④ simple: $\frac1{10^{-4}\ \text{cm}}\ln\frac1{0.5}=6.9\times10^3$ cm⁻¹. corrected: $-\frac1{10^{-4}}\ln\frac{0.5}{0.81}=4.8\times10^3$ cm⁻¹. ignoring reflection blames reflected light on absorption

see also [[Microscopy formulas]], [[Diffraction formulas]], [[Electrical formulas]], [[Metrology and nano-characterization workshop]]
