#extra #quantum_channel #dephasing #decoherence
**extra** (not in the course): losing phase information **without** losing energy, written the "physics" way with Kraus operators. it turns out to be the [[Dephasing channel]] in disguise
## what it does
$$
E_0=\begin{bmatrix}1&0\\0&\sqrt{1-\lambda}\end{bmatrix}\qquad E_1=\begin{bmatrix}0&0\\0&\sqrt\lambda\end{bmatrix}\qquad\rho\longrightarrow E_0\rho E_0^\dagger+E_1\rho E_1^\dagger
$$
- $E_1$: the environment "noticed" the qubit was in $|1\rangle$ (eg. a photon scattered off it without taking energy)
- $E_0$: it didn't notice, but $|1\rangle$ gets a bit smaller

(same style as the [[Amplitude damping channel]], which has $E_1$ moving $|1\rangle$ **down** to $|0\rangle$ instead)
## the effect
$$
\begin{bmatrix}a&b\\b^*&c\end{bmatrix}\longrightarrow\begin{bmatrix}a&\sqrt{1-\lambda}\,b\\\sqrt{1-\lambda}\,b^*&c\end{bmatrix}
$$
the populations (diagonal) stay the same, the coherences (off diagonal) shrink
> [!important] it's the same as dephasing
> the [[Dephasing channel]] multiplies the off diagonals by $1-2p$. so phase damping with $\lambda$ **is** dephasing with
> $$
> 1-2p=\sqrt{1-\lambda}
> $$
> eg. $\lambda=0.36$ gives $p=0.1$ (checked numerically: same output for every input). 2 very different stories (random $Z$ flips vs. the environment weakly measuring the qubit), one channel

## physically
this is the **pure dephasing** part of decoherence, the $T_\phi$ in
$$
\frac1{T_2}=\frac1{2T_1}+\frac1{T_\phi}
$$
(where $T_1$ is energy loss). caused by things like slow random changes in the qubit's frequency (see [[Noise Processes]] and [[Noise spectra]])

see also [[Dephasing channel]], [[Amplitude damping channel]], [[Quantum channels]]
