#vlsi #formulas #electrical #probe_station
every formula for [[Electrical characterization]], [[Sheet resistance and contacts]] and [[MOS capacitor C-V]]. formulas that live in a topic note are embedded from there (with a link to its worked example), the extra ones are written out here. part of [[Metrology and nano-characterization workshop]]
## resistance and sheet resistance
### Ohm's law from drift

![[Sheet resistance and contacts#^drude]]

### a thin-film strip

![[Sheet resistance and contacts#^sheet-resistance]]

worked (a Cu line, 100 squares) in [[Sheet resistance and contacts#why sheet resistance is useful]]
### two-point measurement

![[Sheet resistance and contacts#^two-point]]

## four-point probe
thin sheet, much bigger than the probe spacing

![[Sheet resistance and contacts#^four-point]]

thick sample (probe spacing $s\ll t$)
$$
\rho=2\pi s\frac VI
$$
^four-point-thick

> [!eg]- $V=10$ mV, $I=1$ mA
> thin sheet: $R_s=4.532\times10\ \Omega=45.3\ \Omega/\square$. a thick block with $s=1$ mm: $\rho=2\pi(10^{-3})(10)=0.063\ \Omega\,\text{m}$. same reading, different formula: ==check which case your sample is==

## TLM (contact resistance)

![[Sheet resistance and contacts#^tlm]]

![[Sheet resistance and contacts#^contact-resistivity]]

plot $R_T$ vs spacing $L$: intercept at $L=0$ is $2R_c$, intercept on the $L$ axis is $-2L_T$. full worked table in [[Sheet resistance and contacts#TLM: transfer length method]]
## van der Pauw

![[Sheet resistance and contacts#^van-der-pauw]]

$R_A=\frac{V_{34}}{I_{12}}$, $R_B=\frac{V_{41}}{I_{23}}$, exact form $e^{-\pi R_A/R_{sh}}+e^{-\pi R_B/R_{sh}}=1$, $f=1$ for a symmetric sample
## diode (Shockley)

![[Electrical characterization#^shockley]]

$n$ → ideality factor, from the slope of $\ln I$ vs $V$ (worked in [[Electrical characterization#$I$–$V$ curves]])
### Schottky diode
$$
I_s=AA^*T^2e^{-q\phi_B/k_BT}
$$
^schottky-diode

$A^*$ → Richardson constant (~120 A/cm²K² for free electrons), $\phi_B$ → barrier height (from the work functions, [[UPS#in VLSI]])
> [!eg]- a 100 µm × 100 µm contact, $\phi_B=0.7$ eV, $A^*=120$ A/cm²K², 300 K
> $I_s=(10^{-4}\ \text{cm}^2)(120)(300^2)e^{-0.7/0.02585}=1080\times1.7\times10^{-12}\approx1.9$ nA. drop the barrier by 0.1 eV and $I_s$ goes up $e^{0.1/0.02585}=48\times$: ==the barrier height controls everything, exponentially==

## MOSFET
### oxide capacitance
per area, the same parallel plate as in [[MOS capacitor C-V#^oxide-capacitance]] divided by $A$: $C_{ox}=\frac{3.9\,\varepsilon_0}{t_{ox}}$. eg. $t_{ox}=2$ nm → $1.73\times10^{-2}$ F/m² $=1.73$ µF/cm²
### drain current
linear region ($V_{DS}<V_{GS}-V_{th}$)

![[Electrical characterization#^mosfet-linear]]

saturation (worked: 1.25 mA in [[Electrical characterization#transistor (MOSFET)]])

![[Electrical characterization#^mosfet-saturation]]

### transconductance and output conductance
$$
g_m=\frac{\partial I_D}{\partial V_{GS}}\qquad g_d=\frac{\partial I_D}{\partial V_{DS}}\qquad r_o=\frac1{g_d}
$$
^transconductance

in saturation $g_m=\mu C_{ox}\frac WL(V_{GS}-V_{th})$ (just the derivative of the square law)
### threshold voltage
$$
V_{th}=V_{FB}+2\phi_F+\frac{\sqrt{2q\varepsilon_{Si}N_A(2\phi_F)}}{C_{ox}}\qquad\phi_F=\frac{k_BT}q\ln\frac{N_A}{n_i}
$$
^threshold-voltage

$$
V_{FB}=\phi_{MS}-\frac{Q_{ox}}{C_{ox}}
$$
^flat-band

(worked fixed-charge shift in [[MOS capacitor C-V#what you extract]])
> [!eg]- $N_A=10^{17}$ cm⁻³, $t_{ox}=2$ nm, $V_{FB}=-0.5$ V
> $$
> \begin{aligned}
> \phi_F&=0.02585\ln\frac{10^{17}}{10^{10}}=0.417\ \text{V}\qquad2\phi_F=0.833\ \text{V}\\
> \frac{\sqrt{2(1.602\times10^{-19})(1.036\times10^{-10})(10^{23})(0.833)}}{1.73\times10^{-2}}&=0.096\ \text{V}\\
> V_{th}&=-0.5+0.833+0.096=0.43\ \text{V}
> \end{aligned}
> $$
> with a thin oxide the depletion charge term is small, so $V_{th}$ is mostly set by $V_{FB}$ (the gate metal's work function) and the doping

- extracting it from data: the **linear extrapolation** method → find the max $g_m$ point on the $I_D$–$V_{GS}$ curve, draw the tangent, its $V_{GS}$ intercept is $V_{th}+V_{DS}/2$
### mobility (from the linear region at small $V_{DS}$)
$$
\mu_{eff}=\frac{g_d\,L}{W\,C_{ox}(V_{GS}-V_{th})}
$$
^mobility

### subthreshold swing
the ideal limit is in [[Electrical characterization#^subthreshold-swing]]. in a real device the depletion capacitance steals some of the gate's control
$$
SS=\left(\frac{\partial\log_{10}I_D}{\partial V_{GS}}\right)^{-1}=\frac{k_BT}q\ln10\left(1+\frac{C_d}{C_{ox}}\right)\ge60\text{ mV/dec at 300 K}
$$
^ss-general

### other figures of merit
$$
\frac{I_{on}}{I_{off}}\qquad DIBL=\frac{V_{th}(V_{DS,low})-V_{th}(V_{DS,high})}{V_{DS,high}-V_{DS,low}}\ \ [\text{mV/V}]
$$
^dibl

## MOS capacitor $C$–$V$
accumulation: $C=C_{ox}$ ([[MOS capacitor C-V#^oxide-capacitance]]). depletion: in series with the depletion layer

![[MOS capacitor C-V#^series-capacitance]]

$$
W=\sqrt{\frac{2\varepsilon_s\psi_s}{qN}}\qquad W_{max}=\sqrt{\frac{4\varepsilon_s\phi_F}{qN_A}}
$$
^depletion-width

($\psi_s$ → surface potential. worked: $W_{max}=304$ nm and $C_{min}=3.1$ pF in [[MOS capacitor C-V#low vs high frequency]])

doping from the slope in depletion (worked in [[MOS capacitor C-V#what you extract]])

![[MOS capacitor C-V#^doping-slope]]

## power (set a compliance current!)
$$
P=IV
$$
^power

eg. a 1 µm² transistor at 1 V letting through 10 mA dissipates 10 mW in a tiny volume: it melts. the compliance current stops that
## practice
> [!exercise] mixed
> ① four-point on a 500 nm film reads $V/I=0.2\ \Omega$. find $R_{sh}$ and $\rho$
> ② a MOSFET in saturation: $I_D=0.5$ mA at $V_{GS}-V_{th}=0.5$ V. what's $g_m$?
> ③ why is $\phi_F$ bigger for heavier doping, and what does that do to $V_{th}$?

> [!answer]-
> ① $R_{sh}=4.532\times0.2=0.91\ \Omega/\text{sq}$, $\rho=0.91\times500\times10^{-9}=4.5\times10^{-7}\ \Omega\,\text{m}$
> ② square law: $g_m=\frac{2I_D}{V_{GS}-V_{th}}=\frac{2\times0.5}{0.5}=2$ mS
> ③ $\phi_F=\frac{k_BT}q\ln\frac{N_A}{n_i}$ grows with $N_A$, and so does the depletion term, so $V_{th}$ goes **up**: more doping is harder to invert

see also [[Microscopy formulas]], [[Spectroscopy formulas]], [[Diffraction formulas]], [[Metrology and nano-characterization workshop]]
