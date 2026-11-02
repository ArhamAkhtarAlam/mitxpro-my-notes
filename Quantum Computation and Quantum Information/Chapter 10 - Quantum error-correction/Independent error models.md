#textbook #quantum_error_correction #depolarizing #amplitude_damping #fidelity
*Quantum Computation and Quantum Information* §10.3.2 (p. 441–444). if each qubit gets its own **weak, independent** noise, a code that corrects one error turns a first order error into a second order one. part of [[Quantum Computation and Quantum Information]], previous: [[Discretization of the errors]], course version: [[Bit flip code#when does the code fail?]]
## the idea
how does error correction connect to doing reliable quantum information processing? assume the errors on different qubits are **independent**. then, if the noise is weak enough, correction should improve the fidelity of the stored state compared with not encoding it
## the depolarizing channel
$$
\mathcal E(\rho)=(1-p)\rho+\tfrac p3\big[X\rho X+Y\rho Y+Z\rho Z\big]
$$
nothing happens with probability $1-p$, and each of $X$, $Y$, $Z$ happens with probability $p/3$ ([[Depolarizing channel]]). it's the easy case, because it's literally "apply one of the four basic errors at random". its minimum fidelity for one qubit is
$$
F=\sqrt{1-2p/3}=1-p/3+O(p^2)
$$
^depolarizing-fidelity

(exercise 10.12). now encode one qubit in an $n$ qubit code that corrects any single qubit error, and let the channel act independently on each qubit
$$
\mathcal E^{\otimes n}(\rho)=(1-p)^n\rho+\sum_{j=1}^n\sum_{k=1}^3(1-p)^{n-1}\frac p3\,\sigma_k^j\rho\,\sigma_k^j+\dots
$$
the $\dots$ are higher order terms, which are positive and drop out of the bound. correction returns every written term to $\rho$
$$
\begin{aligned}
(\mathcal R\circ\mathcal E^{\otimes n})(\rho)&=\big[(1-p)^n+n(1-p)^{n-1}p\big]\rho+\dots\\
F&\geq\sqrt{(1-p)^{n-1}(1-p+np)}=1-\frac{\binom n2}2p^2+O(p^3)
\end{aligned}
$$
^independent-fidelity

![[Independent_errors_fidelity.png]]

on a log-log plot the code curves have **twice the slope**, so they always win for small enough $p$. bigger codes have more ways to get 2 errors ($\binom n2$), so their lines sit a little higher and cross the no-code line sooner

> [!important] the one idea
> ==a code that corrects any one error turns the $1-O(p)$ fidelity into $1-O(p^2)$==. so for small enough $p$, encoding always helps, however many qubits the code uses

> [!eg] the Shor code ($n=9$) at $p=0.01$
> no code: $F=\sqrt{1-0.00667}=0.99666$, so $1-F=3.3\times10^{-3}$
> Shor code: $F\geq\sqrt{0.99^8\times1.08}=\sqrt{0.99656}=0.99828$, so $1-F\approx1.7\times10^{-3}$ (the $p^2$ estimate gives $\frac{36}2\times10^{-4}=1.8\times10^{-3}$)
>
> only about 2× better here, because $\binom92=36$ is a big coefficient. the gain grows fast as $p$ falls: at $p=10^{-3}$ it's $3.3\times10^{-4}$ vs $1.8\times10^{-5}$
## the amplitude damping channel
many channels can't be read as random Paulis. [[Amplitude damping channel|amplitude damping]] has operation elements
$$
E_0=\begin{bmatrix}1&0\\0&\sqrt{1-\gamma}\end{bmatrix}\qquad E_1=\begin{bmatrix}0&\sqrt\gamma\\0&0\end{bmatrix}
$$
with $\gamma$ small and positive (no noise as $\gamma\to0$). you'd guess it has elements like $\{f(\gamma)I,E_1',E_2',\dots\}$ with $f(\gamma)\to1$. surprisingly **no such description exists**: for $\gamma>0$, no linear combination of $E_0$ and $E_1$ is proportional to $I$, so by theorem 8.2 no set of operation elements has an identity term. lots of physical noise is like this: close to the identity physically, but with no big identity part in any operator-sum form

it still works. the single qubit minimum fidelity is $\sqrt{1-\gamma}$ (exercise 10.13). write $E_{j,k}$ for $E_j$ acting on qubit $k$; to first order
$$
\mathcal E^{\otimes n}(\rho)=\big(E_{0,1}\otimes\dots\otimes E_{0,n}\big)\rho\big(E_{0,1}^\dagger\otimes\dots\otimes E_{0,n}^\dagger\big)+\sum_{j=1}^n\Big[E_{1,j}\otimes\bigotimes_{k\neq j}E_{0,k}\Big]\rho\Big[E_{1,j}^\dagger\otimes\bigotimes_{k\neq j}E_{0,k}^\dagger\Big]+O(\gamma^2)
$$
expand in Paulis: $E_0=(1-\gamma/4)I+\gamma Z/4+O(\gamma^2)$ and $E_1=\sqrt\gamma(X+iY)/2$
$$
\begin{aligned}
\mathcal E^{\otimes n}(\rho)=\Big(1-\frac\gamma4\Big)^{2n}\rho&+\frac\gamma4\Big(1-\frac\gamma4\Big)^{2n-1}\sum_{j=1}^n(Z_j\rho+\rho Z_j)\\
&+\frac\gamma4\Big(1-\frac\gamma4\Big)^{2n-2}\sum_{j=1}^n(X_j+iY_j)\rho(X_j-iY_j)+O(\gamma^2)
\end{aligned}
$$
what correction does to each kind of term
- $Z_j\rho$, $\rho Z_j$: if $Z_j$ takes the code to an orthogonal subspace, the syndrome measurement kills them (like $Z_j|\psi\rangle\langle\psi|$). similarly the cross terms $X_j\rho Y_j$ and $Y_j\rho X_j$
- $X_j\rho X_j$ and $Y_j\rho Y_j$: one qubit errors, so they go back to $\rho$

so $(X_j+iY_j)\rho(X_j-iY_j)\to2\rho$, and after correction
$$
\Big(1-\frac\gamma4\Big)^{2n}\rho+2n\frac\gamma4\Big(1-\frac\gamma4\Big)^{2n-2}\rho+O(\gamma^2)=\rho+O(\gamma^2)
$$
^amplitude-damping-corrected

==the fidelity goes from $\sqrt{1-\gamma}$ to $1-O(\gamma^2)$==, a net suppression just like the depolarizing case. the same argument works for other noise; from here on the book mostly uses Pauli noise models, where classical probability does the work

> [!exercise] try these
> ① the bound for a 5 qubit code at $p=0.01$
> ② check the $O(p^2)$ coefficient: expand $(1-p)^{n-1}(1+(n-1)p)$ to second order
> ③ check $E_0=(1-\gamma/4)I+\gamma Z/4$ to first order in $\gamma$

> [!answer]-
> ① $\sqrt{0.99^4\times1.04}=\sqrt{0.99902}=0.99951$, so $1-F\approx4.9\times10^{-4}$, vs $3.3\times10^{-3}$ unencoded (the estimate $\frac{10}2p^2=5\times10^{-4}$ ✓)
> ② $\big[1-(n-1)p+\binom{n-1}2p^2\big]\big[1+(n-1)p\big]=1+\big[\binom{n-1}2-(n-1)^2\big]p^2+\dots=1-\binom n2p^2+\dots$. the $p$ terms cancel; the square root halves the coefficient
> ③ $\sqrt{1-\gamma}\approx1-\gamma/2$, and $(1-\gamma/4)I+\frac\gamma4Z=\text{diag}(1,\ 1-\gamma/2)$ ✓

see also [[Depolarizing channel]], [[Amplitude damping channel]], [[State fidelity]], [[Operator-sum representation]]

next: [[Degenerate codes and the quantum Hamming bound]]
