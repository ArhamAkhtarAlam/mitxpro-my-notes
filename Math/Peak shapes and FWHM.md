#math #data_analysis #fourier_transform
spectra and diffraction patterns are made of **peaks**. a peak has a position (what it is), a height (how much) and a **width** (often the most interesting part). the two shapes that turn up again and again are the Gaussian and the Lorentzian
## FWHM
the **full width at half maximum**: go to half the peak height and measure the width there. it's the standard way to give a peak's width, whatever its shape

![[Peak_shapes.png]]
(a Gaussian and a Lorentzian with the same FWHM)
## Gaussian
$$
I(x)=I_0\,e^{-(x-x_0)^2/2\sigma^2}\qquad\text{FWHM}=2\sqrt{2\ln2}\,\sigma\approx2.355\,\sigma
$$
^gaussian-peak

**where it comes from**: many small **random** contributions added up (the central limit theorem). eg.
- the energy resolution of an EDS detector, from counting statistics ([[EDS]]: $\text{FWHM}\approx2.355\sqrt{F\varepsilon E}$)
- Doppler broadening from atoms moving randomly
- a spread of qubit frequencies from slow (quasi-static) noise, which is why a noisy [[Rabi oscillation#with noise|Rabi oscillation]] decays as a Gaussian in time
## Lorentzian
![[Spectroscopy formulas#^lorentzian]]

**where it comes from**: anything that **rings and decays**. a signal $e^{-t/\tau}\cos(\omega_0t)$ has a Lorentzian spectrum with
$$
\Gamma=\frac2\tau\quad(\text{in }\omega)\qquad\Delta f=\frac1{\pi\tau}\quad(\text{in Hz})
$$
^lifetime-width

so ==a shorter lifetime means a wider peak==: a Raman phonon in a disordered crystal, a damped cantilever ([[MSA]]), a qubit line broadened by $T_2$
## telling them apart

| | Gaussian | Lorentzian |
|---|---|---|
| cause | many random small shifts | a finite lifetime (decay) |
| tails | die very fast ($e^{-x^2}$) | long ($1/x^2$) |
| Fourier partner | another Gaussian | an exponential decay |
| examples | EDS peaks, Doppler | Raman lines, resonators |

real peaks are often a mix (a **Voigt** profile: a Lorentzian smeared by a Gaussian, a convolution). fitting software usually lets you choose
## width and Fourier transforms
==a narrow feature in one domain is a wide one in the other==: that's the [[Fourier Transform]]. it's behind several "width" formulas in the notes
- **XRD**: a small crystal has few repeats, so its diffraction peaks are broad ([[XRD#^scherrer]])
- **decay ↔ linewidth**: the Lorentzian above
- **a rectangle in time ↔ a sinc in frequency**: the filter functions of [[Dynamical decoupling]]
- **phase estimation**: more counting qubits, sharper peaks ([[Quantum Phase Estimation]])

> [!important] the one idea
> ==a peak's width tells you about either randomness (Gaussian) or lifetime (Lorentzian), and width in one domain is always one over width in the other==

> [!exercise] try these
> ① a Gaussian peak has $\sigma=0.4$. what's its FWHM?
> ② a resonance has $\Delta f=1$ MHz (FWHM). how long does the oscillation take to decay ($\tau$)?
> ③ you see a peak with long tails. is it more likely from detector noise or from a short lifetime?

> [!answer]-
> ① $2.355\times0.4=0.94$
> ② $\tau=\frac1{\pi\Delta f}=\frac1{\pi\times10^6}=0.32\,\mu$s
> ③ a short lifetime: long tails are the Lorentzian signature

see also [[Straight line fits]], [[Logarithms and exponentials]], [[Noise power spectral density]], [[Math]]
