#extra #qubit #hamiltonian #T1
**extra** (not in the course): the qubits inside IBM's and Google's machines. they aren't atoms, they're **electrical circuits** cooled until they behave like one big artificial atom. the "big things are quantum too" point in [[Quantum simulation]]
## an LC circuit is a quantum oscillator
a capacitor and an inductor slosh charge back and forth at $\omega=\frac1{\sqrt{LC}}$. make it out of a **superconductor** (no resistance, so nothing wastes energy) and cool it down: the sloshing is quantized, just like a mass on a spring, with energies
$$
E_n=\hbar\omega\left(n+\tfrac12\right)
$$

the problem: the gaps are **all equal**. a microwave tone at $\omega$ that drives $|0\rangle\to|1\rangle$ also drives $|1\rangle\to|2\rangle\to|3\rangle\dots$, so you can't keep it a qubit

## the Josephson junction fixes it
swap the inductor for a **Josephson junction**: two superconductors with a ~1–2 nm oxide barrier between them, which electron pairs (Cooper pairs) **tunnel** through ([[TEM#the quantum connection|seen in a TEM cross-section]]). it acts like an inductor whose inductance depends on the current, so the energy well is a cosine instead of a parabola, and the levels **bunch up** as they go up

![[Transmon_levels.png]]

the most common design, the **transmon**, has
$$
H=4E_C\,(\hat n-n_g)^2-E_J\cos\hat\varphi
$$
^transmon-hamiltonian

- $\hat n$ = Cooper pairs that crossed the junction, $\hat\varphi$ = the phase across it
- $E_C$ = charging energy (from the capacitor), $E_J$ = Josephson energy (from the junction). transmons use $E_J\approx50\,E_C$, which makes them almost immune to stray charges ($n_g$)
- qubit frequency $f_{01}\approx\frac{\sqrt{8E_JE_C}-E_C}h$, usually **4–6 GHz** (microwaves, like wifi)
- **anharmonicity**: $f_{12}-f_{01}\approx-\frac{E_C}h\approx-200$ to $-300$ MHz. that's the gap difference that lets a pulse at $f_{01}$ touch only $|0\rangle\leftrightarrow|1\rangle$

> [!important] the one idea
> ==a superconducting qubit is an oscillator made **unevenly spaced** by a Josephson junction, so its bottom two levels can be driven on their own==. everything else (gates, readout, noise) is microwave engineering around that

## why so cold
the energy of one 5 GHz photon against thermal energy at 20 mK:
$$
\frac{hf}{k_BT}=\frac{6.63\times10^{-34}\times5\times10^{9}}{1.38\times10^{-23}\times0.02}\approx12,\qquad e^{-12}\approx6\times10^{-6}
$$
so the qubit sits in $|0\rangle$ by itself, and the aluminium is far below its superconducting temperature (1.2 K). that's why the chips live at the bottom of a **dilution refrigerator**

## running it

| job | how |
|---|---|
| single-qubit gates | a microwave pulse at $f_{01}$, ~20–50 ns: the length/amplitude sets the angle, the phase sets the axis ([[Rabi oscillation]]) |
| $Z$ gates | free: just shift the phase of later pulses in software |
| two-qubit gates | couple neighbours through a capacitor or a tunable coupler: CZ by tuning frequencies, or cross-resonance (drive one qubit at the other's frequency), ~50–300 ns |
| readout | the qubit shifts the frequency of a little resonator next to it, so a microwave tone bounced off the resonator comes back with a phase that depends on $\|0\rangle$ or $\|1\rangle$ |

## how good they are

| | typical (good chips) |
|---|---|
| $T_1$ ([[Amplitude damping channel]]) | ~100–300 µs |
| $T_2$ ([[Dephasing and the filter function]]) | similar, up to $2T_1$ |
| single-qubit gate error | ~$10^{-4}$ |
| two-qubit gate error | ~$10^{-3}$–$5\times10^{-3}$ |
| qubits per chip | ~100–1000+ |

a gate takes ~50 ns and $T_1$ ~100 µs, so a few thousand gates fit before things decay. not enough for big algorithms, which is why they need [[Logical qubit|logical qubits]] and the [[Surface code]] (a 2D grid of nearest neighbours is exactly what these chips are good at)

where the noise comes from ([[Noise Processes]])
- **two-level systems (TLS)**: tiny defects in the oxides and surfaces that steal energy at random frequencies
- flux noise ($1/f$) on tunable qubits, stray photons in the readout resonator, quasiparticles (broken Cooper pairs), even cosmic rays that hit the whole chip at once

## pros and cons

| good | bad |
|---|---|
| made like computer chips (lithography, [[SEM]], [[FIB]]) | every qubit is slightly different, needs calibrating |
| fast gates (ns) | short lifetimes (µs to ms) |
| easy to put on a 2D grid | only talks to neighbours, needs a fridge, lots of wiring |

the main rival: trapped ions and neutral atoms (identical by nature, long lifetimes, but ~1000× slower gates)

> [!eg] the numbers from the VLSI notes
> the junction's resistance at room temperature predicts $E_J$ (and so the qubit frequency) before the chip is ever cooled. that's why [[Sheet resistance and contacts#the quantum connection|junction resistance]] is measured on every wafer

> [!exercise] try these
> **1** why can't a plain LC circuit be a qubit?
> **2** at 100 mK, is a 5 GHz qubit still mostly in $|0\rangle$?
> **3** a gate takes 40 ns and $T_1=120$ µs. roughly how many gates before $1/e$ of the excitation is lost?

> [!answer]-
> **1** equally spaced levels: a pulse meant for $0\leftrightarrow1$ also climbs to $|2\rangle,|3\rangle\dots$
> **2** $\frac{hf}{k_BT}\approx2.4$, $e^{-2.4}\approx0.09$: about 9% excited, too much. hence ~10–20 mK
> **3** $\frac{120\,\mu\text{s}}{40\,\text{ns}}=3000$

see also [[Quantum simulation]], [[Rabi oscillation]], [[NISQ]], [[Logical qubit]], [[Quantum advantage]], VLSI: [[TEM]], [[SEM]], [[Metrology and nano-characterization workshop]]
