#vlsi #characterization #MSA #MEMS
## micro system analyzer
a tool for measuring how **MEMS** (tiny moving machines on a chip) actually **move**, and what their surface looks like. all with light, so nothing touches the device. (eg. the Polytec MSA). part of [[Metrology and nano-characterization workshop]]

> [!important] the one idea
> ==every part of the MSA is interference of light==: the Doppler shift is read by beating against a reference beam, and the 3D height comes from where white light fringes appear

## three techniques in one

| technique | measures | how |
|---|---|---|
| **laser Doppler vibrometry (LDV)** | **out of plane** motion (velocity / displacement) | laser bounces off a moving surface, the frequency shifts by the **Doppler effect** |
| **stroboscopic video microscopy** | **in plane** motion | LED flashes in sync with the drive signal, camera captures the device at "frozen" phases of its motion |
| **white light interferometry (WLI)** | **3D topography** | scan in Z, find where interference fringes are strongest at each pixel |

^msa-techniques

### LDV
$$
f_D=\frac{2v}{\lambda}
$$
^doppler

- moving surface at speed $v$ shifts the laser frequency by $f_D$ (factor 2 as light goes there and back)
- mix with a reference beam (interferometer) → read off the shift → get velocity, integrate for displacement
- resolution down to picometres, bandwidth up to tens of MHz and beyond

> [!eg] a surface moving at 1 mm/s, HeNe laser (633 nm)
> $$
> \begin{aligned}
> f_D&=\frac{2\times10^{-3}}{633\times10^{-9}}\approx3.2\ \text{kHz}\\
> \text{if it vibrates at 50 kHz:}\quad d_{peak}&=\frac{v_{peak}}{2\pi f}=\frac{10^{-3}}{2\pi\times50\,000}=3.2\ \text{nm}
> \end{aligned}
> $$
> a 3 kHz shift on a light wave of $4.7\times10^{14}$ Hz is one part in $10^{11}$. you could never measure that directly, only by **beating** it against the unshifted beam

### stroboscopic video
- the device moves too fast for a camera, but if every frame is lit at the **same phase** of a repeating motion, you can step through phases and rebuild a slow motion video
- gives in plane displacement with **nm** precision using pattern matching
### white light interferometry
- broadband light has a **short coherence length**, so fringes only show up when the path lengths match **exactly**
- scan vertically and note where the fringe contrast peaks for each pixel → height map
- sub-nm vertical resolution over a big range, and non-contact (vs [[AFM]])

> [!eg] why white light and not a laser?
> coherence length $L_c\approx\frac{\lambda_0^2}{\Delta\lambda}$. white light, $\lambda_0=600$ nm and $\Delta\lambda=300$ nm: $L_c\approx\frac{600^2}{300}=1.2$ µm. a HeNe laser ($\Delta\lambda\sim0.002$ nm): $L_c\sim20$ cm. ==with a laser, every height gives fringes, so you can't tell which fringe is which. with white light, fringes only appear within ~1 µm of the exact height==

![[MSA_techniques.png]]
## what you get for a MEMS
- **resonance frequency** $f_0$ (sweep a frequency, find the peak)
- **mode shapes** (scan a grid of points, see the whole structure bend)
- **quality factor**, damping

$$
Q=\frac{f_0}{\Delta f}
$$
^quality-factor

> [!eg] a resonator at 50 kHz with a 100 Hz wide peak
> $Q=\frac{50\,000}{100}=500$. it rings for about $Q$ cycles before dying away, and when you drive it on resonance it moves $Q$ times more than when you push it slowly

![[MSA_resonance_and_modes.png]]
- **frequency response** and transient (step) response
- static shape / curvature / **residual stress** (bending of a released cantilever)
- 3D dimensions, **release** etch check
## what's it for
- cantilevers, accelerometers, gyroscopes, micro-mirrors, resonators, MEMS microphones, pressure sensors
- test of a whole wafer, can be done with a [[Electrical characterization#DC probe station|probe station]] to drive it electrically
- compare to simulation (FEM) to check design
- the cantilever of an [[AFM]] is itself a MEMS resonator

> [!exercise] try these
> ① LDV with a 633 nm laser reads $f_D=10$ kHz. how fast is the surface moving?
> ② a 1 MHz resonator has $Q=10\,000$. how wide is its peak?
> ③ why does LDV measure out of plane motion but not in plane?

> [!answer]-
> ① $v=\frac{f_D\lambda}2=\frac{10^4\times633\times10^{-9}}2=3.2$ mm/s
> ② $\Delta f=\frac{f_0}Q=\frac{10^6}{10^4}=100$ Hz
> ③ the Doppler shift only comes from motion **along** the laser beam. sideways motion doesn't change the path length, so that's what the stroboscopic video is for

## the quantum connection
> [!extra] interferometers are quantum circuits for light
> the LDV and WLI split a beam in two, send the halves along different paths and recombine them. the output depends on the **phase difference**, $\varphi=\frac{4\pi\Delta z}{\lambda}$. that's a Mach–Zehnder or Michelson interferometer, the same thing as in [[Beamsplitters]]: send in **one photon** and it still interferes, because it takes both paths at once. a beamsplitter is a [[Hadamard Gate|Hadamard]] for photons, and the path phase is a [[Phase shift|phase gate]]

> [!extra] Q factor for qubits
> a qubit is a resonator too, and its $Q$ says how long it keeps its energy. a superconducting qubit at 5 GHz with $T_1=100$ µs has a linewidth $\Delta f=\frac1{2\pi T_1}=1.6$ kHz
> $$
> Q=\frac{f_0}{\Delta f}=\frac{5\times10^9}{1.6\times10^3}\approx3\times10^6
> $$
> ==6000× better than the MEMS resonator above==, and it has to be, to survive thousands of gates ([[Noise Processes]], [[Rabi oscillation]])

> [!extra] MEMS in the quantum ground state
> a 350 kHz cantilever at room temperature holds $\frac{k_BT}{hf}\approx2\times10^7$ quanta of vibration (phonons). but a GHz mechanical resonator cooled to ~20 mK has almost **none**, it sits in its quantum ground state. in 2010 one was coupled to a superconducting qubit and put into a superposition of vibrating and not vibrating, the first quantum machine

see also [[AFM]], [[Electrical characterization]], [[Metrology and nano-characterization workshop]]

formulas: [[Microscopy formulas]]
