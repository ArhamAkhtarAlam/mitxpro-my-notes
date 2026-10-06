#formula_sheet #density_matrix #quantum_channel #noise
every formula from Course 3 Week 1 in one place. each section links to the note with the full explanation
## 1. Dirac notation and matrices
from [[Course 3/Week 1/Density matrices/Dirac notation|Dirac notation cheat sheet]] and [[Kets and bras combined]]

**basis, bras, inner products**
$$
|0\rangle=\begin{bmatrix}1\\0\end{bmatrix}\quad|1\rangle=\begin{bmatrix}0\\1\end{bmatrix}\qquad\langle0|=\begin{bmatrix}1&0\end{bmatrix}\quad\langle1|=\begin{bmatrix}0&1\end{bmatrix}\qquad\langle i|j\rangle=\begin{cases}1&i=j\\0&i\ne j\end{cases}
$$
**any state, its length and its projector**
$$
\begin{aligned}
|\psi\rangle&=\alpha|0\rangle+\beta|1\rangle=\begin{bmatrix}\alpha\\\beta\end{bmatrix}\\
\big\||\psi\rangle\big\|&=\sqrt{\langle\psi|\psi\rangle}=\sqrt{|\alpha|^2+|\beta|^2}=1\\
|\psi\rangle\langle\psi|&=\begin{bmatrix}|\alpha|^2&\alpha\beta^*\\\beta\alpha^*&|\beta|^2\end{bmatrix}
\end{aligned}
$$
**2 qubits**
$$
\begin{aligned}
|\psi_{AB}\rangle&=\alpha|00\rangle+\beta|01\rangle+\gamma|10\rangle+\delta|11\rangle=\begin{bmatrix}\alpha\\\beta\\\gamma\\\delta\end{bmatrix}\\
\big\||\psi_{AB}\rangle\big\|&=\sqrt{|\alpha|^2+|\beta|^2+|\gamma|^2+|\delta|^2}
\end{aligned}
$$
**tensor products** (each number of the first × the whole second)
$$
\begin{bmatrix}\alpha\\\beta\end{bmatrix}\otimes\begin{bmatrix}\gamma\\\delta\end{bmatrix}=\begin{bmatrix}\alpha\gamma\\\alpha\delta\\\beta\gamma\\\beta\delta\end{bmatrix}\qquad A\otimes B=\begin{bmatrix}a_AB&c_AB\\b_AB&d_AB\end{bmatrix}
$$
$$
A\otimes I=\begin{bmatrix}a_A&0&c_A&0\\0&a_A&0&c_A\\b_A&0&d_A&0\\0&b_A&0&d_A\end{bmatrix}\qquad I\otimes A=\begin{bmatrix}a_A&c_A&0&0\\b_A&d_A&0&0\\0&0&a_A&c_A\\0&0&b_A&d_A\end{bmatrix}
$$
**outer products build every matrix** ($|i\rangle\langle j|$ = a 1 in row $i$, column $j$)
$$
\begin{bmatrix}a&c\\b&d\end{bmatrix}=a\,|0\rangle\langle0|+c\,|0\rangle\langle1|+b\,|1\rangle\langle0|+d\,|1\rangle\langle1|
$$
$$
I=|0\rangle\langle0|+|1\rangle\langle1|\qquad X=|0\rangle\langle1|+|1\rangle\langle0|\qquad Z=|0\rangle\langle0|-|1\rangle\langle1|
$$
## 2. projectors and measurement
from [[Projectors]]
$$
\Pi_\phi=|\phi\rangle\langle\phi|\qquad\Pi^2=\Pi\qquad\Pi^\dagger=\Pi\qquad\Pi_0+\Pi_1=I
$$

| what | formula |
|---|---|
| chance of result $i$ (pure state) | $P(i)=\langle\psi\vert\Pi_i\vert\psi\rangle=\vert\langle i\vert\psi\rangle\vert^2$ |
| chance of result $i$ (density matrix) | $P(i)=\text{tr}(\Pi_i\,\rho)$ |
| state after the measurement | $\vert\psi\rangle\to\dfrac{\Pi_i\vert\psi\rangle}{\sqrt{P(i)}}$ |
| measure only qubit A | $\Pi_{0_A}=\vert0\rangle\langle0\vert\otimes I$ |
| measure only qubit B | $I\otimes\vert0\rangle\langle0\vert$ |

## 3. density matrices
from [[Density matrix]] and [[Pure and mixed states]]

**definition**: $\rho$ is a density matrix if and only if
$$
\text{tr}(\rho)=1\qquad\text{and}\qquad\langle\varphi|\rho|\varphi\rangle\geq0\ \text{ for every }|\varphi\rangle
$$
**building and unravelling**
$$
\begin{aligned}
\rho&=\sum_kp_k\,|\psi_k\rangle\langle\psi_k|&&\text{(a mixture of states, }p_k\text{ = probabilities)}\\
\rho&=\sum_k\lambda_k\,|k\rangle\langle k|&&\text{(spectral decomposition: eigenvalues }\lambda_k\text{ add to 1)}\\
\rho&=\sum_kp_k\,\rho_k&&\text{(mixing density matrices gives a density matrix)}
\end{aligned}
$$
**a gate $U$ acting on a density matrix** (purity never changes, see [[Density matrix#how a gate changes a density matrix]])
$$
\rho\longrightarrow U\rho\,U^\dagger
$$
**2 unravellings of the same $\rho$** are linked by a unitary $u$
$$
\rho=\sum_ip_i|\psi_i\rangle\langle\psi_i|=\sum_jq_j|\varphi_j\rangle\langle\varphi_j|\quad\Longleftrightarrow\quad\sqrt{p_i}\,|\psi_i\rangle=\sum_ju_{ij}\sqrt{q_j}\,|\varphi_j\rangle
$$
**pure vs mixed**

| | pure | mixed |
|---|---|---|
| form | $\rho=\lvert\psi\rangle\langle\psi\rvert$ | $\rho=\sum_kp_k\lvert\psi_k\rangle\langle\psi_k\rvert$ |
| purity $\text{tr}(\rho^2)$ | $=1$ | $<1$ |
| $\rho^2=\rho$? | yes | no |

**purity of a mixture** of orthogonal states (squaring makes each $p_k<1$ smaller, so it's $<1$ unless one $p_k=1$)
$$
\text{tr}(\rho^2)=\sum_kp_k^2
$$
**on the [[Bloch sphere]]** (Bloch vector $\vec r$, length $r$)
$$
\rho=\frac{I+\vec r\cdot\vec\sigma}2\qquad\text{tr}(\rho^2)=\frac{1+r^2}{2}
$$
**the lecture's example**: $\sqrt{\tfrac34}\,|00\rangle+\sqrt{\tfrac14}\,|11\rangle$, B measured in 2 different ways
$$
\begin{aligned}
\rho_1&=\tfrac34|0\rangle\langle0|+\tfrac14|1\rangle\langle1|=\frac14\begin{bmatrix}3&0\\0&1\end{bmatrix}\\
\rho_2&=\frac18\begin{bmatrix}3&\sqrt3\\\sqrt3&1\end{bmatrix}+\frac18\begin{bmatrix}3&-\sqrt3\\-\sqrt3&1\end{bmatrix}=\frac14\begin{bmatrix}3&0\\0&1\end{bmatrix}=\rho_1
\end{aligned}
$$
## 4. measuring one qubit of a pair
from [[Density matrix practice]]
$$
\begin{aligned}
p_{B,b}&=\langle\psi_{AB}|\,(I_A\otimes\Pi_b)\,|\psi_{AB}\rangle&&\text{(probability B gives }b\text{)}\\
|\psi_{AB}\rangle&\longrightarrow\frac{(I_A\otimes\Pi_b)|\psi_{AB}\rangle}{\sqrt{p_{B,b}}}&&\text{(state afterwards)}\\
\rho_A&=p_{B,0}\,|\psi_{A,0}\rangle\langle\psi_{A,0}|+p_{B,1}\,|\psi_{A,1}\rangle\langle\psi_{A,1}|&&\text{(A if you don't know B's result)}
\end{aligned}
$$
## 5. partial trace
from [[Partial trace]]
$$
\begin{aligned}
\rho_A&=\text{tr}_B(\rho_{AB})=\sum_j\big(I\otimes\langle j|\big)\,\rho\,\big(I\otimes|j\rangle\big)\\
\text{tr}_B\big(|a\rangle\langle a'|\otimes|b\rangle\langle b'|\big)&=|a\rangle\langle a'|\;\langle b'|b\rangle\\
(\rho_A)_{ik}&=\sum_j\rho_{(ij),(kj)}
\end{aligned}
$$
**blocks shortcut** (2 qubits)
$$
\rho_{AB}=\begin{bmatrix}P&Q\\R&S\end{bmatrix}\quad\Rightarrow\quad\rho_A=\begin{bmatrix}\text{tr}P&\text{tr}Q\\\text{tr}R&\text{tr}S\end{bmatrix}\qquad\rho_B=P+S
$$
**example**: half of a Bell pair is completely mixed
$$
\text{tr}_B\Big(\tfrac12\big(|00\rangle+|11\rangle\big)\big(\langle00|+\langle11|\big)\Big)=\frac I2
$$
## 6. quantum channels
from [[Quantum channels]]

**dephasing** ([[Dephasing channel]]): $Z$ with probability $p$
$$
\begin{aligned}
\rho&\longrightarrow(1-p)\,\rho+p\,Z\rho Z\\
\begin{bmatrix}a&b\\b^*&c\end{bmatrix}&\longrightarrow\begin{bmatrix}a&(1-2p)\,b\\(1-2p)\,b^*&c\end{bmatrix}\\
(x,y,z)&\longrightarrow\big((1-2p)x,\ (1-2p)y,\ z\big)
\end{aligned}
$$
**depolarizing** ([[Depolarizing channel]]): $X$, $Y$ or $Z$ each with probability $\frac p3$
$$
\begin{aligned}
\rho&\longrightarrow(1-p)\,\rho+\frac p3\big(\sigma_x\rho\sigma_x+\sigma_y\rho\sigma_y+\sigma_z\rho\sigma_z\big)\\
&=\Big(1-\tfrac43p\Big)\rho+\tfrac43p\,\frac I2\\
(x,y,z)&\longrightarrow\Big(1-\tfrac43p\Big)(x,y,z)
\end{aligned}
$$
the trick behind it: for **any** $\rho$
$$
\frac14\big(\rho+\sigma_x\rho\sigma_x+\sigma_y\rho\sigma_y+\sigma_z\rho\sigma_z\big)=\frac I2
$$
**amplitude damping** ([[Amplitude damping channel]]): $|1\rangle$ decays to $|0\rangle$
$$
\begin{aligned}
\gamma&=1-e^{-t/T_1}\\
E_0&=\begin{bmatrix}1&0\\0&\sqrt{1-\gamma}\end{bmatrix}\qquad E_1=\begin{bmatrix}0&\sqrt\gamma\\0&0\end{bmatrix}\\
\rho&\longrightarrow E_0\,\rho\,E_0^\dagger+E_1\,\rho\,E_1^\dagger\\
\begin{bmatrix}a&b\\b^*&c\end{bmatrix}&\longrightarrow\begin{bmatrix}a+\gamma c&\sqrt{1-\gamma}\,b\\\sqrt{1-\gamma}\,b^*&(1-\gamma)\,c\end{bmatrix}\\
(x,y,z)&\longrightarrow\big(\sqrt{1-\gamma}\,x,\ \sqrt{1-\gamma}\,y,\ \gamma+(1-\gamma)z\big)
\end{aligned}
$$
**binary symmetric channel** ([[Binary symmetric channel]]): each bit flips with probability $p$
$$
C=1-H(p)\qquad H(p)=-p\log_2p-(1-p)\log_2(1-p)
$$
## 7. noise
from [[Noise power spectral density]], [[Rabi oscillation]] and [[Noise spectra]]

**time average vs ensemble average** (equal for an **ergodic** system)
$$
\begin{aligned}
\bar x&=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}x(t)\,dt&&\text{(time average, one run)}\\
\langle x(t_1)\rangle&=\lim_{N\to\infty}\frac1N\sum_{n=1}^Nx_n(t_1)=\int x\,p(x,t_1)\,dx&&\text{(ensemble average, many runs)}
\end{aligned}
$$
**mean square** (second moment)
$$
\begin{aligned}
\overline{x^2}&=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}x(t)^2\,dt&&\text{(time average)}\\
\langle x(t_1)^2\rangle&=\int x^2\,p(x,t_1)\,dx&&\text{(ensemble average)}
\end{aligned}
$$
**autocorrelation and covariance**
$$
\begin{aligned}
\overline{x(t)\,x(t+\tau)}&=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}x(t)\,x(t+\tau)\,dt\\
\langle x(t_1)\,x(t_2)\rangle&=\iint x_1x_2\,p(x_1,t_1;x_2,t_2)\,dx_1\,dx_2
\end{aligned}
$$
**power spectral density** (Wiener–Khinchin: the PSD and autocorrelation are a Fourier pair)
$$
\begin{aligned}
S_\lambda(\omega)&=\int_{-\infty}^{\infty}\langle\lambda(t)\lambda(t+\tau)\rangle\,e^{-i\omega\tau}\,d\tau&&\left[\tfrac{\lambda^2}{\text{Hz}}\right]\\
\langle\lambda(t)\lambda(t+\tau)\rangle&=\frac1{2\pi}\int_{-\infty}^{\infty}S_\lambda(\omega)\,e^{i\omega\tau}\,d\omega&&\left[\lambda^2\right]
\end{aligned}
$$
**noise spectra**

| noise | $S(\omega)$ | type |
|---|---|---|
| 1/f | $\propto\frac1f$, peaked at 0 | classical (symmetric) → dephasing |
| Johnson (thermal) | $\propto k_B\theta$, flat (white) | classical (symmetric) |
| Nyquist (quantum) | $\propto\hbar\omega$, positive frequencies only | quantum → spontaneous emission ($T_1$) |

**Rabi oscillations**
$$
\begin{aligned}
\langle Z\rangle(t)&=\cos(\Omega t)&&\text{(ideal, }\Omega\propto\text{ drive amplitude)}\\
\langle Z\rangle(t)&=\cos(\Omega_0t)\,e^{-\sigma^2t^2/2}&&\text{(quasi-static amplitude noise: Gaussian decay)}
\end{aligned}
$$
## 8. error correction (intro)
from [[Quantum Error Correction]]: the classical repetition code
$$
0\to000\qquad1\to111\qquad\text{(majority vote fixes 1 flipped bit)}
$$

see also [[Density matrix]], [[Quantum channels]], [[Noise Processes]], [[Course 3/Week 1/Density matrices/Dirac notation|Dirac notation cheat sheet]]


