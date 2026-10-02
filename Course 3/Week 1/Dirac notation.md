#dirac_notation #density_matrix #tensor_product #cheat_sheet
the course's cheat sheet for the maths in Course 3 (from the "Density Matrices: Introduction" page). the matrix versions of everything in [[Math/Dirac notation]], for working through [[Density matrix]] problems
> [!warning] 2 corrections the course points out in the video
> - the [[Hadamard Gate|Hadamard]] maps $|0\rangle\to\frac{|0\rangle+|1\rangle}{\sqrt2}$ and $|1\rangle\to\frac{|0\rangle-|1\rangle}{\sqrt2}$
> - "mixture 2" in the density matrix video is missing the normalization $\frac1{\sqrt2}$. done properly:
> $$
> \rho_2=\frac18\begin{bmatrix}3&\sqrt3\\\sqrt3&1\end{bmatrix}+\frac18\begin{bmatrix}3&-\sqrt3\\-\sqrt3&1\end{bmatrix}=\frac18\begin{bmatrix}6&0\\0&2\end{bmatrix}=\frac14\begin{bmatrix}3&0\\0&1\end{bmatrix}
> $$
> (my [[Density matrix#bipartite state example]] already has the fixed version)

## single qubit
### the basis
the computational basis is the eigenvectors of the Pauli $Z$ ([[Z gate]])
$$
Z=\begin{bmatrix}1&0\\0&-1\end{bmatrix}\qquad|0\rangle=\begin{bmatrix}1\\0\end{bmatrix}\qquad|1\rangle=\begin{bmatrix}0\\1\end{bmatrix}
$$
their conjugate transposes (bras) are rows
$$
\langle0|=\begin{bmatrix}1&0\end{bmatrix}\qquad\langle1|=\begin{bmatrix}0&1\end{bmatrix}
$$
the basis is **orthonormal**: perpendicular, and length 1
$$
\langle1|0\rangle=\begin{bmatrix}0&1\end{bmatrix}\begin{bmatrix}1\\0\end{bmatrix}=0\qquad\langle0|1\rangle=0\qquad\sqrt{\langle0|0\rangle}=\sqrt{\langle1|1\rangle}=1
$$
### identity and projectors
$$
I=\begin{bmatrix}1&0\\0&1\end{bmatrix}\qquad\Pi_0=|0\rangle\langle0|=\begin{bmatrix}1&0\\0&0\end{bmatrix}\qquad\Pi_1=|1\rangle\langle1|=\begin{bmatrix}0&0\\0&1\end{bmatrix}
$$
($\Pi_0+\Pi_1=I$)
### any state
$$
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle=\begin{bmatrix}\alpha\\\beta\end{bmatrix}
$$
its **length** (norm), with $\alpha^*,\beta^*$ the [[Complex numbers|complex conjugates]]
$$
\big\||\psi\rangle\big\|=\sqrt{\langle\psi|\psi\rangle}=\sqrt{\begin{bmatrix}\alpha^*&\beta^*\end{bmatrix}\begin{bmatrix}\alpha\\\beta\end{bmatrix}}=\sqrt{|\alpha|^2+|\beta|^2}
$$
its **projector** (the density matrix of a pure state)
$$
|\psi\rangle\langle\psi|=\begin{bmatrix}\alpha\\\beta\end{bmatrix}\begin{bmatrix}\alpha^*&\beta^*\end{bmatrix}=\begin{bmatrix}|\alpha|^2&\alpha\beta^*\\\beta\alpha^*&|\beta|^2\end{bmatrix}
$$
^pure-projector

==the diagonal is the probabilities, the off diagonal is the superposition part==
### tensor product of 2 states
each number of the first vector times the whole second vector ([[Tensor product]])
$$
|\psi\rangle\otimes|\phi\rangle=\begin{bmatrix}\alpha\\\beta\end{bmatrix}\otimes\begin{bmatrix}\gamma\\\delta\end{bmatrix}=\begin{bmatrix}\alpha\begin{bmatrix}\gamma\\\delta\end{bmatrix}\\\beta\begin{bmatrix}\gamma\\\delta\end{bmatrix}\end{bmatrix}=\begin{bmatrix}\alpha\gamma\\\alpha\delta\\\beta\gamma\\\beta\delta\end{bmatrix}
$$
## two qubits
### the basis
$$
|00\rangle=\begin{bmatrix}1\\0\\0\\0\end{bmatrix}\qquad|01\rangle=\begin{bmatrix}0\\1\\0\\0\end{bmatrix}\qquad|10\rangle=\begin{bmatrix}0\\0\\1\\0\end{bmatrix}\qquad|11\rangle=\begin{bmatrix}0\\0\\0\\1\end{bmatrix}
$$
each one is a tensor product, eg.
$$
|0\rangle|0\rangle=\begin{bmatrix}1\\0\end{bmatrix}\otimes\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}1\begin{bmatrix}1\\0\end{bmatrix}\\0\begin{bmatrix}1\\0\end{bmatrix}\end{bmatrix}=\begin{bmatrix}1\\0\\0\\0\end{bmatrix}
$$
- shorthand: $|01\rangle\equiv|0\rangle|1\rangle$, $|10\rangle\equiv|1\rangle|0\rangle$, $|11\rangle\equiv|1\rangle|1\rangle$
- to say **which qubit**, add a subscript: $|0_A\rangle$ = the state $|0\rangle$ of qubit $A$
### identity and projectors
$I$ is the $4\times4$ identity, and the basis projectors are $\Pi_{00}=|00\rangle\langle00|$, $\Pi_{01}=|01\rangle\langle01|$, $\Pi_{10}=|10\rangle\langle10|$, $\Pi_{11}=|11\rangle\langle11|$
### any state
$$
|\psi_{AB}\rangle=\alpha|0_A0_B\rangle+\beta|0_A1_B\rangle+\gamma|1_A0_B\rangle+\delta|1_A1_B\rangle=\begin{bmatrix}\alpha\\\beta\\\gamma\\\delta\end{bmatrix}
$$
length
$$
\big\||\psi_{AB}\rangle\big\|=\sqrt{\langle\psi_{AB}|\psi_{AB}\rangle}=\sqrt{|\alpha|^2+|\beta|^2+|\gamma|^2+|\delta|^2}
$$
projector
$$
|\psi_{AB}\rangle\langle\psi_{AB}|=\begin{bmatrix}\alpha\\\beta\\\gamma\\\delta\end{bmatrix}\begin{bmatrix}\alpha^*&\beta^*&\gamma^*&\delta^*\end{bmatrix}=\begin{bmatrix}|\alpha|^2&\alpha\beta^*&\alpha\gamma^*&\alpha\delta^*\\\beta\alpha^*&|\beta|^2&\beta\gamma^*&\beta\delta^*\\\gamma\alpha^*&\gamma\beta^*&|\gamma|^2&\gamma\delta^*\\\delta\alpha^*&\delta\beta^*&\delta\gamma^*&|\delta|^2\end{bmatrix}
$$
## tensor products of matrices
same rule: each number of the first matrix times the **whole** second matrix
$$
A\otimes B=\begin{bmatrix}a_A&c_A\\b_A&d_A\end{bmatrix}\otimes\begin{bmatrix}a_B&c_B\\b_B&d_B\end{bmatrix}=\begin{bmatrix}a_AB&c_AB\\b_AB&d_AB\end{bmatrix}=\begin{bmatrix}a_Aa_B&a_Ac_B&c_Aa_B&c_Ac_B\\a_Ab_B&a_Ad_B&c_Ab_B&c_Ad_B\\b_Aa_B&b_Ac_B&d_Aa_B&d_Ac_B\\b_Ab_B&b_Ad_B&d_Ab_B&d_Ad_B\end{bmatrix}
$$
^matrix-tensor

> [!warning] $A\otimes I$ and $I\otimes A$ look really different
> **$A$ on the first qubit**: $A$'s numbers get spread out into little identity blocks
> $$
> A\otimes I=\begin{bmatrix}a_A&0&c_A&0\\0&a_A&0&c_A\\b_A&0&d_A&0\\0&b_A&0&d_A\end{bmatrix}
> $$
> **$A$ on the second qubit**: two copies of $A$ down the diagonal
> $$
> I\otimes A=\begin{bmatrix}a_A&c_A&0&0\\b_A&d_A&0&0\\0&0&a_A&c_A\\0&0&b_A&d_A\end{bmatrix}
> $$
> ==the first slot is the first qubit== (checked numerically)

see also [[Math/Dirac notation]], [[Tensor product]], [[Density matrix]], [[Math]]
