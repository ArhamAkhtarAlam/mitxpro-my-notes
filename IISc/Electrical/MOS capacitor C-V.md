#vlsi #characterization #electrical #CV #MOS
## MOS capacitor C–V
a **metal–oxide–semiconductor** capacitor is a gate metal on an oxide ($\text{SiO}_2$) on a silicon substrate. it's the simplest gate stack, so $C$–$V$ is how you check one. part of [[Electrical characterization]] and [[Metrology and nano-characterization workshop]]

> [!important] the one idea
> ==the oxide is a fixed capacitor, and the silicon underneath adds a second, voltage-dependent capacitor in series==. sweeping the gate voltage pushes charge around in the silicon and changes that second capacitor, and the shape of the curve tells you about the oxide, the doping and the interface

## oxide capacitance
a parallel plate capacitor
$$
C_{ox}=\frac{\varepsilon_0\varepsilon_{ox}A}{d}
$$
^oxide-capacitance

thinner oxide $d$ or bigger area $A$ → more capacitance

> [!eg] a 100 µm × 100 µm capacitor with 10 nm of SiO₂ ($\varepsilon_{ox}=3.9$)
> $$
> \begin{aligned}
> A&=(100\times10^{-6})^2=10^{-8}\ \text{m}^2\\
> C_{ox}&=\frac{8.854\times10^{-12}\times3.9\times10^{-8}}{10\times10^{-9}}=3.45\times10^{-11}\ \text{F}=34.5\ \text{pF}
> \end{aligned}
> $$
> run it backwards and that's how you get the **oxide thickness** from the measured $C_{ox}$

> [!eg] high-k and EOT
> a 3 nm HfO₂ film ($\varepsilon\approx25$) gives the same $C_{ox}$ as an SiO₂ film of thickness
> $$
> \text{EOT}=d_{high\text{-}k}\,\frac{3.9}{\varepsilon_{high\text{-}k}}=3\times\frac{3.9}{25}=0.47\ \text{nm}
> $$
> the capacitance of half a nanometre of SiO₂, but physically 3 nm thick, so electrons can't tunnel through and leak. that's why chips switched to high-k (check its composition with [[XPS]] and its thickness with [[TEM]])

## three regions (p-type substrate)
sweep the gate voltage $V_G$ and measure the small-signal capacitance with an LCR meter

| region | gate voltage | what happens | $C$ |
|---|---|---|---|
| **accumulation** | $V_G<V_{FB}$ (negative) | holes pile up at the interface, the semiconductor acts like a metal | $C=C_{ox}$ |
| **depletion** | between $V_{FB}$ and $V_T$ | the surface is depleted of holes, a depletion layer of width $W$ grows and is in **series** with $C_{ox}$ | falls |
| **inversion** | $V_G>V_T$ | electrons (minority carriers) form a channel under the oxide | depends on frequency |

^mos-regions

![[MOS_CV_curves.png]]

in depletion, the depletion layer is another parallel plate capacitor (silicon, $\varepsilon_s=11.7$, thickness $W$), in series with the oxide
$$
\frac1C=\frac1{C_{ox}}+\frac1{C_{dep}}\qquad C_{dep}=\frac{\varepsilon_0\varepsilon_sA}{W}
$$
^series-capacitance

> [!eg] the same capacitor with a 100 nm depletion layer
> $$
> \begin{aligned}
> C_{dep}&=\frac{8.854\times10^{-12}\times11.7\times10^{-8}}{100\times10^{-9}}=10.4\ \text{pF}\\
> C&=\frac{C_{ox}C_{dep}}{C_{ox}+C_{dep}}=\frac{34.5\times10.4}{34.5+10.4}=8.0\ \text{pF}
> \end{aligned}
> $$
> two capacitors in series are always **smaller** than either one, so $C$ falls as $W$ grows

## low vs high frequency
- **low frequency**: the minority carriers can be generated and recombined fast enough to follow the AC signal, so the charge sits right under the oxide → $C$ goes **back up to $C_{ox}$**
- **high frequency**: minority carriers can't follow. the depletion layer stays at its maximum width $W_{max}$ → $C$ stays at the **minimum**
- the response time of the carriers is related to the temperature and the generation rate (frequency $\propto1/\tau$)

> [!eg] the minimum capacitance (high frequency, $N=10^{16}$ cm⁻³)
> the depletion layer stops growing once the surface inverts, at (extra, the standard formula)
> $$
> \begin{aligned}
> \phi_F&=\frac{kT}q\ln\frac N{n_i}=0.0259\ln\frac{10^{16}}{10^{10}}=0.357\ \text{V}\\
> W_{max}&=\sqrt{\frac{4\varepsilon_0\varepsilon_s\phi_F}{qN}}=\sqrt{\frac{4(1.036\times10^{-10})(0.357)}{(1.602\times10^{-19})(10^{22})}}=304\ \text{nm}\\
> C_{dep}&=\frac{1.036\times10^{-10}\times10^{-8}}{304\times10^{-9}}=3.41\ \text{pF}\qquad C_{min}=\frac{34.5\times3.41}{34.5+3.41}=3.1\ \text{pF}
> \end{aligned}
> $$
> ($N$ in m⁻³: $10^{16}$ cm⁻³ $=10^{22}$ m⁻³). so the curve drops from 34.5 pF to ~3.1 pF, and $\frac{C_{min}}{C_{ox}}$ depends on the doping, which is another way to get $N$

## what you extract
- **oxide thickness** from $C_{ox}$ (accumulation)
- **flat band voltage** $V_{FB}$ → fixed charge in the oxide, work function difference (the metal's work function from [[UPS]])
- **doping** from the depletion slope
- **interface trap density** from the stretch-out or a frequency dispersion of the curve
- **threshold voltage** $V_T$

$$
\frac{d(1/C^2)}{dV}=\frac2{q\varepsilon_0\varepsilon_sA^2N}
$$
^doping-slope

> [!eg] doping from the slope
> plot $\frac1{C^2}$ against $V$ in depletion and it's a straight line. say the slope is $1.2\times10^{23}\ \text{F}^{-2}\text{V}^{-1}$ (with $A=10^{-8}$ m²)
> $$
> \begin{aligned}
> N&=\frac2{q\varepsilon_0\varepsilon_sA^2\times\text{slope}}=\frac2{(1.602\times10^{-19})(1.036\times10^{-10})(10^{-16})(1.2\times10^{23})}\\
> &=\frac2{1.99\times10^{-22}}=1.0\times10^{22}\ \text{m}^{-3}=10^{16}\ \text{cm}^{-3}
> \end{aligned}
> $$
> ==steeper slope = lighter doping== (the depletion layer grows faster)

> [!eg] fixed charge shifts the curve (extra)
> $V_{FB}=\phi_{ms}-\frac{Q_f}{C_{ox}'}$ ($C_{ox}'$ per area). $10^{11}$ positive charges per cm² in the oxide, $C_{ox}'=\frac{34.5\ \text{pF}}{10^{-4}\ \text{cm}^2}=3.45\times10^{-7}$ F/cm²
> $$
> \Delta V_{FB}=-\frac{(10^{11})(1.602\times10^{-19})}{3.45\times10^{-7}}=-0.046\ \text{V}
> $$
> the whole curve slides 46 mV to the left. a thinner oxide (bigger $C_{ox}'$) shifts less for the same charge

## cables matter
at low currents and for $C$–$V$ the cabling decides the noise floor and the leakage

![[Coax_vs_triax.png]]
- **coax**: signal in the centre, shield (ground) around it. leakage can flow from the signal to the shield
- **triax**: an extra **guard** conductor held at the **same voltage as the signal**, so no voltage difference means no leakage current between them. use triax for pA and fA measurements ($I$–$V$ at low current, also for $C$–$V$ with guarded connections)

> [!exercise] try these
> ① a 200 µm × 200 µm MOS capacitor measures $C_{ox}=138$ pF in accumulation. how thick is the SiO₂?
> ② on n-type silicon, which way do you sweep to accumulate?
> ③ the high frequency curve stays low in inversion but the low frequency one comes back to $C_{ox}$. why?
> ④ a 2 nm high-k film has EOT 0.4 nm. what's its $\varepsilon$?

> [!answer]-
> ① $A=4\times10^{-8}$ m², $d=\frac{\varepsilon_0(3.9)A}{C}=\frac{8.854\times10^{-12}\times3.9\times4\times10^{-8}}{138\times10^{-12}}=10.0$ nm
> ② **positive** gate voltage: it pulls the majority carriers (electrons) up to the interface. everything is mirrored compared to p-type
> ③ at low frequency the minority electrons can be made and destroyed fast enough to follow the AC signal, so the charge sits right at the oxide. at high frequency they can't, so only the edge of the (maximum width) depletion layer responds
> ④ $\varepsilon=3.9\times\frac{2}{0.4}=19.5$

## the quantum connection
> [!extra] a transmon qubit is a capacitor
> a superconducting qubit is a Josephson junction across a **capacitor** ([[Sheet resistance and contacts#the quantum connection]]). the capacitor sets how much energy it costs to move one extra charge on, the **charging energy**
> $$
> \begin{aligned}
> E_C&=\frac{e^2}{2C}\\
> C=80\ \text{fF}:\quad\frac{E_C}h&=\frac{(1.602\times10^{-19})^2}{2(80\times10^{-15})(6.626\times10^{-34})}=242\ \text{MHz}
> \end{aligned}
> $$
> 80 fF is tiny: ~400× less than the 34.5 pF example above. a transmon makes $C$ big enough that $E_J\gg E_C$ (about 50× bigger), which makes it insensitive to stray charges, the main [[Noise Processes|noise]] of older designs. the capacitor's own oxide matters too: defects in it (the same **interface traps** C–V measures) absorb energy from the qubit and shorten its lifetime

> [!extra] the inversion layer is a particle in a box
> in strong inversion the electrons are squeezed against the oxide in a layer a few nm thick. that's a quantum well, a [[Particle in a box]] (triangle shaped)
> ![[Particle in a box#^energy-levels]]
>
> so the electron energies are **quantized** in the direction into the silicon, and the wavefunction has to go to zero at the oxide wall. ==the electrons' charge peaks ~1 nm **below** the interface, not right at it==, which adds ~0.3–0.4 nm to the effective oxide thickness measured by C–V. with 0.5 nm EOTs, that's a big deal

> [!extra] silicon spin qubits are MOS devices
> take a MOS capacitor, make the gate into a few tiny electrodes, and cool it to ~1 K: under the gate you can **accumulate** a puddle of just **one** electron (a quantum dot). its spin is a qubit (the same spin ½ as the [[XPS#the quantum connection|XPS doublets]]). it's the same accumulation / depletion physics as the C–V curve, and companies like Intel build them in normal chip fabs. the interface traps that stretch out a C–V curve are exactly the charge noise that makes these qubits lose their state

see also [[Electrical characterization]], [[Sheet resistance and contacts]], [[XPS]], [[UPS]], [[Metrology and nano-characterization workshop]]

formulas: [[Electrical formulas]]
