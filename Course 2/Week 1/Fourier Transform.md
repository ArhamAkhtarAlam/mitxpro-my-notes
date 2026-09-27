#fourier_transform
continuous version of [[Discrete Fourier Transform]]
## What it does
It takes a continuous curve (eg $f\left(x\right)=\sin\left(x\right)+\cos\left(4x\right)+2\cos\left(6x\right)+10\sin\left(2x\right)+4\sin\left(3x\right)+\sin\left(4x\right)+\sin\left(5x\right)$ )
and converts it into the frequency and amplitude.

## How it works
the trick is that waves with different frequencies cancel out when you multiply them and integrate
$$
\int_0^{2\pi}\sin (x)\sin(x)\,dx=\pi\qquad\int_0^{2\pi}\sin(x)\sin(2x)\,dx=0
$$
so if you multiply the curve by a wave of one frequency and integrate, only the part of the curve with **that same frequency** survives, and how big the answer is tells you its amplitude

do that for every frequency and you get the whole spectrum
$$
X(\omega) = \int_{-\infty}^{\infty} x(t)\, e^{-i \omega t}\, dt
$$
