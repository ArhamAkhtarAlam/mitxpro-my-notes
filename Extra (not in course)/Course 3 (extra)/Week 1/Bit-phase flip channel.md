#extra #quantum_channel #bloch_sphere
**extra** (not in the course): the qubit randomly gets a [[Y gate|Y]], which is a bit flip **and** a phase flip at the same time ($Y=iXZ$)
## what it does
- probability $1-p$ → nothing
- probability $p$ → apply $Y$
$$
\rho\longrightarrow(1-p)\,\rho+p\,Y\rho Y
$$
eg. $|0\rangle\to i|1\rangle$ and $|+\rangle\to-i|-\rangle$, so both the $0/1$ pattern and the $\pm$ sign get flipped (the $i$'s are global phases and don't matter)
## on the Bloch sphere
$$
(r_x,r_y,r_z)\longrightarrow\big((1-2p)r_x,\ r_y,\ (1-2p)r_z\big)
$$
only the $y$ axis survives, because $|{+i}\rangle$ and $|{-i}\rangle$ are eigenstates of $Y$. $x$ and $z$ shrink (see the picture in [[Pauli channel]])
> [!note] it's rare to see alone
> real hardware mostly has $Z$ ([[Dephasing channel|dephasing]]) and energy loss ([[Amplitude damping channel|amplitude damping]]) errors. $Y$ errors usually show up as part of the [[Depolarizing channel]] or a general [[Pauli channel]]

see also [[Pauli channel]], [[Bit flip channel]], [[Y gate]]
