#vlsi #characterization #electrical #sheet_resistance #TLM
## sheet resistance and contacts
how to measure the resistance of a **thin film**, and how to separate it from the resistance of the **contacts** you used to measure it. part of [[Electrical characterization]] and [[Metrology and nano-characterization workshop]]

> [!important] the one idea
> ==never measure a voltage with the same wires that carry the current==: then the contacts' own resistance drops out. four-point probe, van der Pauw and TLM are all ways of doing that, or of measuring the contacts on purpose

## from drift to Ohm's law
(from your own notes) electrons in a wire of length $L$ and cross-section $A$, drift speed $v_d$, scattering time $\tau$
$$
\begin{aligned}
I&=n\,e\,A\,v_d\qquad v_d=\frac{\tau eE}{m}\qquad E=\frac VL\\
\Rightarrow\quad I&=\frac{n e^2\tau}{m}\frac AL\,V=\frac VR\qquad R=\rho\frac LA\qquad\rho=\frac m{ne^2\tau}
\end{aligned}
$$
^drude

(in words: more carriers $n$ or longer between collisions $\tau$ → less resistance)
## why sheet resistance is useful
for a uniform thin film of thickness $t$ the resistance of a rectangular strip is
$$
R=\rho\frac L{Wt}=R_{sh}\frac LW\qquad R_{sh}=\frac\rho t\ \ [\Omega/\text{sq}]
$$
^sheet-resistance

![[Sheet_resistance.png]]
- the **square count** $L/W$ is dimensionless, so $R_{sh}$ has units of Ω but is written Ω/sq. when $L=W$, $R=R_{sh}$
- ==a square of film has the same resistance whatever its size==: a 1 µm square and a 1 m square of the same film are both $R_{sh}$ (twice as long, but also twice as wide)
- useful for **comparing conductive films** when the thickness is known or controlled
- a **spatial map** of $R_{sh}$ reveals **non-uniformity**, but contact and geometry effects must be checked

> [!eg] a copper line
> Cu, $\rho=1.7\times10^{-8}\ \Omega\,\text{m}$, film $t=100$ nm, line 1 mm long and 10 µm wide
> $$
> \begin{aligned}
> R_{sh}&=\frac{1.7\times10^{-8}}{100\times10^{-9}}=0.17\ \Omega/\text{sq}\\
> \frac LW&=\frac{1000\ \text{µm}}{10\ \text{µm}}=100\ \text{squares}\\
> R&=0.17\times100=17\ \Omega
> \end{aligned}
> $$

## where does contact resistance enter?
a **two-point** measurement uses the same probes to push current and sense voltage, so the contact and lead resistances **add** to the result
$$
R_{meas}=R_{DUT}+2R_c+2R_{lead}
$$
^two-point

a **four-point** measurement forces current through the outer probes and senses voltage on the inner probes. the voltmeter draws almost no current, so the drop across the contacts stays out of the reading

![[Two_vs_four_point_probing.png]]

> [!eg] how wrong is two-point?
> a 10 Ω film, contacts 5 Ω each, leads 0.5 Ω each
> $$
> R_{meas}=10+2(5)+2(0.5)=21\ \Omega
> $$
> more than **double** the real value. for a 10 kΩ resistor the same 11 Ω would be a 0.1% error, which is why two-point is fine there

> [!tip] rule of thumb
> two-point is fine when the device resistance is **much larger** than the contacts. for thin films, low-resistance wires or contacts you care about, use four-point

### the four-point probe
four probes in a line, equally spaced, on a big thin film
$$
R_{sh}=\frac{\pi}{\ln2}\frac VI\approx4.53\frac VI
$$
^four-point

> [!eg] 1 mA in, 1 mV between the inner probes
> $R_{sh}=4.53\times\frac{1\ \text{mV}}{1\ \text{mA}}=4.53\ \Omega/\text{sq}$. if the film is 200 nm thick, $\rho=R_{sh}t=4.53\times200\times10^{-9}=9.1\times10^{-7}\ \Omega\,\text{m}$

## how contact formation can go wrong

| failure | what happens |
|---|---|
| **surface contamination** | residue or oxide between the metal and the film → high, unstable contact |
| **metal discontinuity** | poor step coverage, voids, cracks or adhesion issues |
| **wrong interface / recipe** | the metal and semiconductor don't react the way you wanted (annealing, work function mismatch) |
| **measurement interface** | the probe pad is dirty, probe tip is worn, or the probe damages the pad |

^contact-failures

metal contacts on the surface can also oxidise and then behave like a **rectifying (Schottky) contact** instead of an ohmic one (your note: "metal contacts on surface can get oxidised → rectifying Schottky effect")
- to **find** the contamination or oxide: [[XPS]] (only a few nm thick, exactly its range)
- the **work function mismatch** that sets the barrier: [[UPS#in VLSI|UPS]]
- to **see** the voids or cracks: [[SEM]], or cut a cross section with an [[FIB]] and look in a [[TEM]]
## TLM: transfer length method
make contact pads with **different spacings** $L$ on the same film. measure the total resistance $R_T$ between each pair
$$
R_T=\frac{R_{sh}}WL+2R_c
$$
^tlm

this is a straight line $y=mx+c$
- **slope** $=R_{sh}/W$ → sheet resistance
- **intercept** at $L=0$ → $2R_c$ (two contacts)
- intercept on the $L$ axis → $-2L_T$ (transfer length)

![[TLM_plot.png]]
the **transfer length** $L_T$ is the distance over which most of the current crosses from the metal into the film under the contact. the specific contact resistivity is
$$
\rho_c=R_{sh}L_T^2
$$
^contact-resistivity

> [!eg] a TLM measurement (pads 100 µm wide)
>
> | spacing $L$ (µm) | 5 | 10 | 20 | 40 |
> |---|---|---|---|---|
> | $R_T$ (Ω) | 22.5 | 25 | 30 | 40 |
>
> $$
> \begin{aligned}
> \text{slope}&=\frac{40-22.5}{40-5}=0.5\ \Omega/\text{µm}\quad\Rightarrow\quad R_{sh}=0.5\times100=50\ \Omega/\text{sq}\\
> \text{intercept}&=22.5-0.5(5)=20\ \Omega=2R_c\quad\Rightarrow\quad R_c=10\ \Omega\\
> \text{L axis}&:\ 0=0.5L+20\ \Rightarrow\ L=-40\ \text{µm}=-2L_T\quad\Rightarrow\quad L_T=20\ \text{µm}\\
> \rho_c&=50\times(20\times10^{-4}\ \text{cm})^2=2\times10^{-4}\ \Omega\,\text{cm}^2
> \end{aligned}
> $$
> ==read slope **and** intercept: don't force the line through zero, the intercept is the whole point==. at least 4 spacings, and check that the points are straight (non-linearity means non-uniform film or bad contacts)

## van der Pauw
four small contacts on the **edge** of a flat sample of **any shape** (no holes) of uniform thickness. no need to know the geometry
- configuration A: current $1\to2$, voltage across $3,4$: $R_A=V_{34}/I_{12}$
- configuration B: current $2\to3$, voltage across $4,1$: $R_B=V_{41}/I_{23}$

![[Van_der_Pauw.png]]
$$
R_{sh}=\frac\pi{\ln2}\cdot\frac{R_A+R_B}2\cdot f
$$
^van-der-pauw

- $f$ is a correction factor, $f=1$ if $R_A=R_B$ (symmetric sample)
- the exact form: $e^{-\pi R_A/R_{sh}}+e^{-\pi R_B/R_{sh}}=1$
- uses two measurements so **contact resistance cancels** (the voltage is measured with a separate pair)
- then $\rho=R_{sh}t$ and with a Hall measurement you also get mobility and carrier density

> [!eg] a square sample with $R_A=R_B=10\ \Omega$
> $$
> R_{sh}=\frac{\pi}{\ln2}\times10\times1=4.532\times10=45.3\ \Omega/\text{sq}
> $$
> check with the exact form: $e^{-\pi(10)/45.3}+e^{-\pi(10)/45.3}=2e^{-0.693}=2\times0.5=1$ ✅

## compare the methods

| method | good for | needs |
|---|---|---|
| **two-point** | high-value resistors | nothing |
| **four-point probe** | $R_{sh}$ of a big film | probes in line, [[#^four-point]] |
| **van der Pauw** | $R_{sh}$ of any shaped sample | 4 contacts on the edge |
| **TLM** | contact resistance + $R_{sh}$ | patterned pads at several spacings |

> [!exercise] try these
> ① a 50 nm Al film has $R_{sh}=0.6\ \Omega/\text{sq}$. what's $\rho$? (bulk Al is $2.7\times10^{-8}\ \Omega\,\text{m}$, why is the film worse?)
> ② how many squares is a line 2 mm long and 4 µm wide, and what's its resistance with $R_{sh}=0.6$?
> ③ TLM with $W=50$ µm gives slope $2\ \Omega$/µm and intercept $30\ \Omega$. find $R_{sh}$, $R_c$ and $L_T$
> ④ why does a probe station always set a compliance current?

> [!answer]-
> ① $\rho=0.6\times50\times10^{-9}=3.0\times10^{-8}\ \Omega\,\text{m}$. a bit worse than bulk: in a thin film electrons also scatter off the surfaces and grain boundaries, so $\tau$ in [[#^drude]] is shorter
> ② $\frac{2000}{4}=500$ squares, $R=0.6\times500=300\ \Omega$
> ③ $R_{sh}=2\times50=100\ \Omega/\text{sq}$, $R_c=15\ \Omega$, $L=-\frac{30}{2}=-15$ µm $=-2L_T$ so $L_T=7.5$ µm
> ④ so a short or a breakdown can't push a huge current and burn the device ([[Electrical characterization]])

## the quantum connection
> [!extra] Ω per square is the natural unit of 2D, and quantum mechanics has its own
> in 2D the resistance of a square doesn't depend on its size, so Ω/sq is the only unit that makes sense. and there's a **resistance quantum** built from nature's constants
> $$
> R_K=\frac h{e^2}=25\,812.8\ \Omega
> $$
> in the **quantum Hall effect** (a 2D electron gas, very cold, strong magnetic field) the Hall resistance locks onto $\frac{R_K}{\nu}$ for whole numbers $\nu$, the same in every sample to parts per billion, whatever the material or shape. it's how the ohm is defined now. and a 2D film with $R_{sh}$ near $\frac{h}{4e^2}\approx6.5$ kΩ/sq sits right at the edge between turning superconducting and turning insulating when cooled

> [!extra] a room temperature resistance sets a qubit's frequency
> a superconducting qubit (a **transmon**) is a capacitor ([[MOS capacitor C-V#the quantum connection]]) across a **Josephson junction**, two Al films with a ~1–2 nm oxide that electron pairs **tunnel** through ([[TEM#the quantum connection]]). you can't measure the junction cold on a probe station, but its **room temperature** resistance $R_n$ predicts how much supercurrent it carries cold (Ambegaokar–Baratoff, Al gap $\Delta\approx180$ µeV)
> $$
> \begin{aligned}
> I_cR_n&=\frac{\pi\Delta}{2e}=\frac{\pi\times180\ \text{µV}}{2}=283\ \text{µV}\\
> R_n=10\ \text{k}\Omega\ \Rightarrow\ I_c&=\frac{283\ \text{µV}}{10\ \text{k}\Omega}=28.3\ \text{nA}\\
> \frac{E_J}{h}&=\frac{I_c}{4\pi e}=\frac{28.3\times10^{-9}}{4\pi\times1.602\times10^{-19}}=14.0\ \text{GHz}
> \end{aligned}
> $$
> with a charging energy $E_C/h=0.24$ GHz (from the capacitor), the qubit frequency is $f\approx\sqrt{8E_JE_C}-E_C=\sqrt{8(14.0)(0.24)}-0.24\approx5.0$ GHz. ==so labs probe every junction at room temperature, two-point vs four-point and all, to check their qubits will land at the right frequency==

> [!extra] ohmic contacts work by tunnelling
> a metal on a semiconductor makes a Schottky barrier ([[UPS#in VLSI]]). to get an **ohmic** contact you dope the semiconductor very heavily right under the metal: that makes the barrier so **thin** that electrons tunnel straight through it, the same effect as the field emission gun in a [[TEM]]. that's why $\rho_c$ drops so steeply with doping

see also [[Electrical characterization]], [[MOS capacitor C-V]], [[XPS]], [[UPS]], [[Metrology and nano-characterization workshop]]

formulas: [[Electrical formulas]]
