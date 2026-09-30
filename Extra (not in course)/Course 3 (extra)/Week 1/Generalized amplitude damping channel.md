#extra #quantum_channel #amplitude_damping #temperature
**extra** (not in the course): the [[Amplitude damping channel]] at a **non-zero temperature**. the environment can now give energy **to** the qubit, not just take it away
## the idea
the normal amplitude damping channel assumes the environment is at absolute zero, so $|1\rangle$ only ever falls down to $|0\rangle$. a warm environment can also kick $|0\rangle$ **up** to $|1\rangle$
- with probability $p$: the environment acts **cold** → amplitude damping towards $|0\rangle$
- with probability $1-p$: it acts **hot** → amplitude damping towards $|1\rangle$
$$
E_0=\sqrt p\begin{bmatrix}1&0\\0&\sqrt{1-\gamma}\end{bmatrix}\quad E_1=\sqrt p\begin{bmatrix}0&\sqrt\gamma\\0&0\end{bmatrix}\quad E_2=\sqrt{1-p}\begin{bmatrix}\sqrt{1-\gamma}&0\\0&1\end{bmatrix}\quad E_3=\sqrt{1-p}\begin{bmatrix}0&0\\\sqrt\gamma&0\end{bmatrix}
$$
## where it ends up
run it forever and every qubit ends up in the **thermal state**
$$
\rho_{\text{thermal}}=\begin{bmatrix}p&0\\0&1-p\end{bmatrix}
$$
not $|0\rangle$ (checked numerically). $p=1$ is zero temperature (the normal amplitude damping channel), $p=\frac12$ is infinite temperature (50/50)
## on the Bloch sphere
$$
(r_x,r_y,r_z)\longrightarrow\big(\sqrt{1-\gamma}\,r_x,\ \sqrt{1-\gamma}\,r_y,\ (1-\gamma)\,r_z+\gamma(2p-1)\big)
$$
(checked numerically). the sphere shrinks and slides towards the point $(0,0,2p-1)$, which is only the north pole when $p=1$
> [!tip] why qubits are kept so cold
> superconducting qubits sit in fridges at about $10$ millikelvin so that $p$ is extremely close to $1$. if the environment were warm, qubits would randomly start in $|1\rangle$ and heat would keep flipping them

see also [[Amplitude damping channel]], [[Quantum channels]], [[Noise Processes]]
