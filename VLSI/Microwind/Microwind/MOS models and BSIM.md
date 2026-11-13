#vlsi #microwind #MOS_model #BSIM
how a simulator works out a transistor's current from its voltages. part of [[Microwind course]]

## the curve it has to reproduce
$I_{ds}$ against $V_{ds}$ for a few gate voltages

- **linear** (triode): small $V_{ds}$, the current rises almost in a straight line
- **saturated**: the current levels off, but still creeps up (channel length modulation)
- **impact ionization**: at high $V_{ds}$ fast carriers knock out new ones and the current shoots up again (substrate current induced body effect)

![[MOSFET_curves.png]]

## models get bigger

| model | year | parameters |
|---|---|---|
| Level 1 | 1970s | ~5 |
| Level 3 | 1980s | ~20 |
| BSIM3 / BSIM4 | 2000s | ~300–500 |
| BSIM-CMG (multi-gate: FinFET, nanosheet) | 2010s | ~500+ |
| BSIM6 | 2020 | ~1000 |

a real FinFET model has about **500 parameters per transistor** and over 20 000 lines of C. [[Microwind]] uses Level 1, Level 3 and a **simplified BSIM4** with 25 parameters and 250 lines of code. ==fine for learning, but it makes many simplifications== (roughly: under 10 parameters is fine for students, a few dozen for teachers, hundreds for real simulators)

## the simplified BSIM4
### threshold voltage
$$
V_{th}=V_{TH0}+K_1\left(\sqrt{\Phi_s-V_{bs}}-\sqrt{\Phi_s}\right)-K_2V_{bs}+\Delta V_{t,SCE}+\Delta V_{t,NULD}+\Delta V_{t,DIBL}
$$
- $V_{TH0}$: threshold for a long channel, no body bias
- the $K_1$, $K_2$ terms: **body effect** (a substrate bias $V_{bs}$ shifts $V_{th}$)
- the $\Delta$ terms: short channel corrections

short channel effect (the threshold drops in short channels)
$$
\Delta V_{t,SCE}=-\frac{0.5\,DVT0}{\cosh\!\left(DVT1\,\dfrac{L_{eff}}{l_t}\right)-1}\,(V_{bi}-\Phi_s)
$$
non-uniform lateral doping (pocket implants raise $V_{th}$ in short channels)
$$
\Delta V_{t,NULD}=K_1\left(\sqrt{1+\frac{LPE0}{L_{eff}}}-1\right)\sqrt{\Phi_s}
$$

### mobility
carriers slow down when the vertical field pulls them against the oxide
$$
\mu_{eff}=\frac{U_0}{1+(U_A+U_C\,V_{bs})\left(\dfrac{V_{gsteff}+2(V_{TH0}-V_{fb}-\Phi_s)}{TOXE}\right)^{EU}}
$$

### smooth everything
real simulators hate sudden jumps between regions, so BSIM uses smooth "effective" voltages that blend them. the effective gate overdrive works below and above threshold
$$
V_{gsteff}=\max\!\left(V_{OFF},\ \frac{n v_t\ln\!\left(1+e^{(V_{gs}-V_{th})/nv_t}\right)}{1+n\,e^{-(V_{gs}-V_{th})/nv_t}}\right)
$$
- far above $V_{th}$ it's just $V_{gs}-V_{th}$
- below $V_{th}$ it falls **exponentially**: the subthreshold leakage
- $V_{OFF}$ stops it falling forever (real devices bottom out at some leakage floor)

![[Vgsteff_smoothing.png]]

the effective drain voltage switches smoothly from $V_{ds}$ to the saturation voltage
$$
V_{dseff}=V_{dsat}-\frac12\left(V_{dsat}-V_{ds}-\delta+\sqrt{(V_{dsat}-V_{ds}-\delta)^2+4\delta V_{dsat}}\right)
$$

### the current
$$
I_{ds0}=\frac{W_{eff}}{L_{eff}}\,\mu_{eff}\,\frac{\varepsilon_0\varepsilon_r}{TOXE}\,V_{gsteff}\left(1-\frac{A_{bulk}V_{dseff}}{2V_{gsteff}+4v_t}\right)\frac{V_{dseff}}{1+\dfrac{V_{dseff}}{E_{sat}L_{eff}}}
$$
then the saturation-region creep from impact ionization and channel length modulation
$$
I_{ds}=I_{ds0}\left(1+\frac{V_{ds}-V_{dseff}}{V_{ASCBE}}\right)\left(1+\frac1{C_{clm}}\ln\frac{V_{ASAT}+V_{ACLM}}{V_{ASAT}}\right)
$$
^ids-bsim

## FinFET and nanosheet: the same equations
[[Microwind]] keeps the **same** equations for MOSFET, FinFET and nanosheet. it only changes the width it feeds in

![[Weq_cross_sections.png]]

![[Transistor evolution#^weq-table]]

what it **doesn't** model: quantum confinement (the electrons' energy levels in a 5 nm sheet), centroid shift, sub-band separation, changes in effective mass. industry's BSIM-CMG does

> [!extra]- why $\ln(1+e^x)$?
> the "softplus" $\ln(1+e^x)$ is $\approx x$ for big $x$ and $\approx e^x$ for very negative $x$, with no kink in between. so one formula gives the linear "above threshold" behaviour and the exponential subthreshold tail. it's the same smooth step used in machine learning activation functions

see also [[Transistor evolution]], [[FinFET]], [[MOS capacitor C-V]]
