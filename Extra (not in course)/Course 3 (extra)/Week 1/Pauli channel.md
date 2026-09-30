#extra #pauli #quantum_channel #bloch_sphere
**extra** (not in the course): the general channel where the qubit randomly gets an $X$, $Y$ or $Z$ error, each with its **own** probability. [[Dephasing channel|dephasing]], [[Depolarizing channel|depolarizing]], [[Bit flip channel|bit flip]] and [[Bit-phase flip channel|bit-phase flip]] are all special cases
## what it does
- probability $p_I=1-p_X-p_Y-p_Z$ → nothing
- probability $p_X$ → [[X gate|X]], probability $p_Y$ → [[Y gate|Y]], probability $p_Z$ → [[Z gate|Z]]
$$
\rho\longrightarrow p_I\,\rho+p_X\,X\rho X+p_Y\,Y\rho Y+p_Z\,Z\rho Z
$$
^pauli-channel

## on the Bloch sphere
each axis shrinks by its own factor. an axis is only **safe** from the Pauli error along that same axis, and gets flipped by the other 2
$$
(r_x,r_y,r_z)\longrightarrow\Big(\big(1-2(p_Y+p_Z)\big)r_x,\ \big(1-2(p_X+p_Z)\big)r_y,\ \big(1-2(p_X+p_Y)\big)r_z\Big)
$$
(checked numerically). so the sphere becomes an **ellipsoid** lined up with the axes, and the centre never moves
![[Pauli_channels_3d.png]]

| channel | $p_X$ | $p_Y$ | $p_Z$ | what survives |
|---|---|---|---|---|
| [[Bit flip channel]] | $p$ | 0 | 0 | the $x$ axis |
| [[Bit-phase flip channel]] | 0 | $p$ | 0 | the $y$ axis |
| [[Dephasing channel]] | 0 | 0 | $p$ | the $z$ axis |
| [[Depolarizing channel]] | $\frac p3$ | $\frac p3$ | $\frac p3$ | nothing, shrinks evenly by $1-\frac43p$ |

## why it matters
- it's the standard **error model** for [[Quantum Error Correction]]: codes are built to catch $X$, $Z$ (and so $Y=iXZ$) errors
- **Pauli twirling**: surround any noisy gate with random Pauli gates (and undo them afterwards) and, on average, **any** noise turns into a Pauli channel. that's why Pauli channels are used so much in benchmarking (see [[Randomized benchmarking]])

see also [[Quantum channels]], [[Depolarizing channel]], [[Dephasing channel]]
