#quantum_annealing #optimization #d_wave #ising
basically [[Adiabatic quantum computing]] that's **allowed to leave the ground state**, then finds its way back down using quantum tunnelling and relaxation. for **classical** optimisation problems. part of [[Quantum optimization]]
## the name: annealing
in metallurgy, **annealing** means heating a metal so its structure can rearrange, then cooling it so it settles into a new, better arrangement. the heat's random jiggling lets it escape bad arrangements
## simulated annealing (classical)
a classical algorithm that copies this
1. start with a solution with energy (cost) $E$
2. pick a random nearby solution with energy $E'$
3. if it's **better** ($E'<E$), move there
4. if it's **worse**, **sometimes** move there anyway, with a chance that shrinks as the "temperature" $T$ drops (usually $e^{-(E'-E)/T}$)
5. slowly lower $T$ to zero, until it's **frozen** in a (hopefully global) minimum

taking worse steps on purpose helps it **escape local minima**, like thermal kicks
## quantum annealing
same idea, but with **quantum fluctuations** instead of thermal ones
- a wavefunction is **spread out**, not at one point, so repeated measurements give different results. that spread is the "quantum fluctuation"
- if the wavefunction spreads over **2 valleys** of the cost landscape, the system can **tunnel through** the barrier instead of having to jump over it
- the tunnelling is controlled by a **transverse field** (along $x$ or $y$ on the [[Bloch sphere]]) instead of a temperature

![[Annealing_tunneling.png]]
## the Hamiltonian
the cost function goes into an **Ising** [[Hamiltonian]] (spins with fields and pairwise couplings), whose ground state is the best answer
$$
H(s)=A(s)\,H_{\text{init}}+B(s)\,H_{\text{problem}}\qquad H_{\text{init}}=-\sum_iX_i\qquad H_{\text{problem}}=\sum_ih_iZ_i+\sum_{i<j}J_{ij}Z_iZ_j
$$
compare the [[Adiabatic quantum computing|AQC]] path, which is the same idea with $A=1-s$ and $B=s$
![[Adiabatic quantum computing#^adiabatic-path]]

- start: $A\gg B$, all qubits aligned with the big transverse field
- end: $A\approx0$, only the problem is left
- in the middle it passes the **minimum gap** and almost certainly leaves the ground state (noise, Landau–Zener). the hope is that tunnelling + dissipation bring it back to a low energy state

> [!warning] not the same as AQC
> ==the computer is **not** meant to end up in an excited state, the aim is still the ground state.== it's just **allowed** to leave and come back on the way. and quantum annealing is **not** proven to be a universal quantum computer

## D-Wave
the most advanced quantum annealers are the commercial **D-Wave** machines: at the time of the course more than **2000 superconducting qubits**, connected in a fixed pattern called the **chimera graph** (newer models have 5000+ qubits and better connectivity)
- a real engineering achievement (thousands of qubits calibrated by on-chip classical superconducting electronics)
- but to scale that fast they used **low coherence** qubits, **fixed** connectivity and only $ZZ$ type interactions

> [!question] does it actually beat classical computers?
> after years of testing, there's **no theoretical or experimental evidence** of a quantum speedup for general optimisation problems. better qubits, other interactions ($XX$, $YY$), multi qubit interactions and better connectivity might help. and even if annealers end up scaling "classically", they could still be useful if they beat existing computers on some problems

see also [[Adiabatic quantum computing]], [[QAOA]], [[Quantum optimization]]
