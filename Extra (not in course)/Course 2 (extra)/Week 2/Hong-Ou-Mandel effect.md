#extra #photons #beamsplitter #single_photon
**extra** (not in the course): send two **identical** photons into a 50:50 [[Beamsplitters|beamsplitter]], one from each side, at the same moment, and they **always leave together** through the same output. never one each. (Hong, Ou and Mandel, 1987)
## why: two paths cancel
for the photons to come out in **different** outputs, either both pass straight through or both reflect

| what happens | amplitude |
|---|---|
| both transmit | $t\cdot t=\frac1{\sqrt2}\cdot\frac1{\sqrt2}=\frac12$ |
| both reflect | $r\cdot r=\frac{i}{\sqrt2}\cdot\frac{i}{\sqrt2}=-\frac12$ |
| **total** (one in each output) | $\frac12-\frac12=0$ |

identical photons make these two cases **indistinguishable**, so you add amplitudes, not probabilities, and they cancel. (a reflection picks up a phase $i$, so two reflections give $-1$)

with operators: each input photon splits as $a^\dagger\to\frac{c^\dagger+d^\dagger}{\sqrt2}$, $b^\dagger\to\frac{c^\dagger-d^\dagger}{\sqrt2}$ (one sign convention), so
$$
a^\dagger b^\dagger\to\frac12\left(c^{\dagger2}-c^\dagger d^\dagger+d^\dagger c^\dagger-d^{\dagger2}\right)=\frac12\left(c^{\dagger2}-d^{\dagger2}\right)
$$
^hom

the cross terms cancel (photons are bosons, $c^\dagger d^\dagger=d^\dagger c^\dagger$): you get $|2,0\rangle$ or $|0,2\rangle$, half the time each

> [!important] the one idea
> ==two photons that can't be told apart interfere with **each other**, and the "one in each output" possibility cancels completely==. any difference (arrival time, colour, polarization) makes them distinguishable and the effect goes away

## the HOM dip
delay one photon and count coincidences (both detectors clicking at once)

![[HOM_dip.png]]

- big delay: the photons don't overlap, they act like classical particles: coincidences half the time
- zero delay: coincidences drop to **zero**
- the width of the dip is the length of the photon's wavepacket (femtoseconds to picoseconds), and how deep it goes measures how **identical** the photons are

## what it's used for
- **testing single-photon sources**: two photons from the same source should give a deep dip ([[Single Photon making and detecting]])
- **Bell-state measurement**: the same interference picks out the $|\Psi^-\rangle$ [[Bell states|Bell state]], which is how entanglement swapping and [[Quantum repeaters]] join links
- **photonic quantum computing** and **boson sampling** ([[Quantum advantage]]) are big versions of this interference

> [!exercise] try these
> **1** the two photons arrive with perpendicular polarizations. coincidence rate?
> **2** what if two classical (distinguishable) balls hit the beamsplitter at once?
> **3** the dip only goes down to 0.1 instead of 0. what does that tell you?

> [!answer]-
> **1** $\frac12$: they're distinguishable, no dip
> **2** each goes either way independently: $\frac12$ chance they leave through different outputs
> **3** the photons aren't perfectly identical (or sometimes there are 2 photons in a pulse): visibility $\frac{0.5-0.1}{0.5}=80\%$

see also [[Beamsplitters]], [[Polarization]], [[Entangled Photons generation and detection]], [[Quantum cryptography]]
