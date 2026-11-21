#extra #rotation #quantum_gates #bloch_sphere
**extra** (not in the course): the gates that turn the [[Bloch sphere]] by **any** angle about $x$, $y$ or $z$. the named gates ([[X gate]], [[Hadamard Gate]], [[Phase shift|S and T]]) are just special angles of these, and variational circuits ([[VQE]], [[QAOA]]) are built out of them
## the three rotations
$$
\begin{aligned}
R_x(\theta)&=e^{-i\theta X/2}=\begin{pmatrix}\cos\frac\theta2&-i\sin\frac\theta2\\-i\sin\frac\theta2&\cos\frac\theta2\end{pmatrix}\\
R_y(\theta)&=e^{-i\theta Y/2}=\begin{pmatrix}\cos\frac\theta2&-\sin\frac\theta2\\\sin\frac\theta2&\cos\frac\theta2\end{pmatrix}\\
R_z(\theta)&=e^{-i\theta Z/2}=\begin{pmatrix}e^{-i\theta/2}&0\\0&e^{i\theta/2}\end{pmatrix}
\end{aligned}
$$
^rotation-gates

each one turns the Bloch vector by $\theta$ about that axis (right-hand rule). about any axis $\hat n$:
$$
R_{\hat n}(\theta)=\cos\tfrac\theta2\,I-i\sin\tfrac\theta2\,(n_xX+n_yY+n_zZ)
$$
^rotation-any-axis

> [!important] the one idea
> ==$R_a(\theta)=e^{-i\theta P/2}$ turns the Bloch sphere by $\theta$ about axis $a$: the half angle in the matrix is because the sphere shows states up to a global phase==. a full turn $R(2\pi)=-I$ looks like doing nothing (it only changes the global phase)

## the named gates are rotations

| gate | as a rotation (up to a global phase) |
|---|---|
| $X$ | $R_x(\pi)$ (exactly $X=iR_x(\pi)$) |
| $Y$ | $R_y(\pi)$ |
| $Z$ | $R_z(\pi)$ |
| $S$ | $R_z(\frac\pi2)$ |
| $T$ | $R_z(\frac\pi4)$ |
| $\sqrt X$ ([[Sqrt(X) Gate]]) | $R_x(\frac\pi2)$ |
| $H$ | $R_x(\pi)\,R_y(\frac\pi2)$: a half turn about the axis halfway between $x$ and $z$ |

## any single-qubit gate from three rotations
every single-qubit unitary can be written as (the **Euler** or **ZYZ** decomposition)
$$
U=e^{i\alpha}\,R_z(\beta)\,R_y(\gamma)\,R_z(\delta)
$$
^zyz

like describing any orientation of a ball with three turns. that's how compilers turn any gate into what the hardware can do ([[Universal gate sets]])

> [!eg] making any amplitude
> $$
> R_y(\theta)|0\rangle=\cos\tfrac\theta2|0\rangle+\sin\tfrac\theta2|1\rangle
> $$
> so $P(1)=\sin^2\frac\theta2$: choose $\theta$ for any probability you want. $R_y(\frac\pi2)|0\rangle=|+\rangle$, and $R_y(\frac{2\pi}3)|0\rangle$ gives $P(1)=\frac34$

$R_z$ only changes the **relative phase**, so it never changes the $Z$ measurement probabilities. it spins the state around the equator, which shows up when you [[Measuring in other bases|measure in another basis]]

> [!exercise] try these
> **1** what's $R_x(\frac\pi2)|0\rangle$, and where is it on the Bloch sphere?
> **2** $R_y(\frac\pi3)|0\rangle$: chance of measuring 1?
> **3** show $R_z(\theta)$ and $R_z(\phi)$ combine to $R_z(\theta+\phi)$

> [!answer]-
> **1** $\frac1{\sqrt2}(|0\rangle-i|1\rangle)$, on the $-y$ side of the equator
> **2** $\sin^2\frac\pi6=\frac14$
> **3** both are diagonal: $e^{-i\theta/2}e^{-i\phi/2}=e^{-i(\theta+\phi)/2}$, same for the other entry

see also [[Quantum gate]], [[Unitary Operation]], [[Pauli matrices]], [[Universal gate sets]], [[Solovay-Kitaev theorem]]
