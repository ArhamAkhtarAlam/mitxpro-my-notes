#fourier_transform
## What it is
It's basically the same thing as the [[Fourier Transform]] but instead of a continuous curve it's just a bunch of points and instead of doing integration we do summation  
## How it works
$X_k = \sum_{n=0}^{N-1} x_n \, e^{-i 2\pi \frac{k}{N} n}$ 
Finds area through summation instead of integration
==as this is a LINEAR TRANSFORMATION this can be represented with a MATRIX==
## MATRIX
$$
F_N =
\frac{1}{\sqrt{N}}
\begin{bmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & \omega & \omega^2 & \cdots & \omega^{N-1} \\
1 & \omega^2 & \omega^4 & \cdots & \omega^{2(N-1)} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \omega^{N-1} & \omega^{2(N-1)} & \cdots & \omega^{(N-1)(N-1)}
\end{bmatrix}
$$
^matrix

$$
\omega=e^{-\frac{2\pi i}{N}}
$$
> [!note] sign convention
> for the formula above $\omega=e^{-2\pi i/N}$ (minus sign). the [[Quantum Fourier Transform]] uses $\omega=e^{+2\pi i/N}$ (plus sign), so it's really the same matrix with the opposite sign in the exponent (the inverse DFT)
>
> the $\frac1{\sqrt N}$ in front makes the matrix [[Unitary Operation|unitary]], the formula above just leaves it out
