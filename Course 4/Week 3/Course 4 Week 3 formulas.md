#formula_sheet #dynamical_decoupling #noise
every formula from Course 4 Week 3 on one page. formulas that live in a topic note are embedded from there (with a link to its worked example), the extra ones are written out here. each section has a folded **eg.** and an **exercise** (try it first). part of [[Quantum error mitigation]]
## 1. continuous errors are linear
from [[Correcting continuous errors]]

![[Correcting continuous errors#^rotation-as-paulis]]

> [!eg]- eg. a small rotation
> $\theta=0.2$: $e^{0.2iZ}=0.980\,I+0.199i\,Z$. after the syndrome measurement: no error with probability $0.980^2=0.961$, one $Z$ error (then fixed) with probability $0.199^2=0.039$. they add to 1

> [!exercise] exercise
> a rotation $e^{i\theta Z}$ with $\theta=\pi/2$. what is it as a Pauli combination, and what does the syndrome measurement find?

> [!answer]-
> $\cos\frac\pi2\,I+i\sin\frac\pi2\,Z=iZ$: a phase flip (times a global phase). the syndrome finds $Z$ with certainty
## 2. relaxation and dephasing
from [[Dephasing and the filter function]]

![[Phase damping channel#^t2-relation]]

> [!eg]- eg. the $T_2$ limit
> $T_1=80\,\mu$s and no dephasing: $T_2=2T_1=160\,\mu$s. with $T_\phi=80\,\mu$s too: $\frac1{T_2}=\frac1{160}+\frac1{80}=\frac3{160}$, so $T_2\approx53\,\mu$s

> [!exercise] exercise
> you measure $T_1=40\,\mu$s and $T_2=50\,\mu$s. what's $T_\phi$?

> [!answer]-
> $\frac1{T_\phi}=\frac1{50}-\frac1{80}=\frac{3}{400}$, so $T_\phi\approx133\,\mu$s
## 3. free evolution
from [[Dephasing and the filter function#example: a flux qubit]]

![[Dephasing and the filter function#^free-evolution]]

> [!eg]- eg. phase per nanosecond
> $E_{01}/h=6$ GHz: $\varphi=2\pi\times6\times10^9\times10^{-9}=12\pi$ rad every nanosecond. a $1$ MHz wobble adds $2\pi\times10^6\times t$, so $\pi$ of error after $0.5\,\mu$s

> [!exercise] exercise
> how long until a 100 kHz frequency offset adds $\pi/2$ of phase error?

> [!answer]-
> $2\pi\times10^5\,t=\pi/2$ → $t=2.5\,\mu$s
## 4. the dephasing formula
from [[Dephasing and the filter function#how much it dephases]]

![[Dephasing and the filter function#^dephasing-decay]]

![[Dephasing and the filter function#^filter-function]]

> [!eg]- eg. white noise and Ramsey
> for flat (white) noise $S_\Phi(\omega)=S_0$, and with no pulses $\frac1{2\pi}\int\text{sinc}^2(\omega t/2)\,d\omega=\frac1t$. the exponent becomes $-\frac{t}{2\hbar^2}\left(\frac{\partial E_{01}}{\partial\Phi}\right)^2S_0$: **linear** in $t$, an ordinary exponential decay. (1/f noise instead gives roughly $t^2$, a Gaussian-like decay)

> [!exercise] exercise
> double the sensitivity $\partial E_{01}/\partial\Phi$. what happens to the exponent?

> [!answer]-
> it's squared, so the exponent is 4× bigger: the coherence decays as the old one to the 4th power
## 5. spin echo and CPMG
from [[Dynamical decoupling]]

![[Dynamical decoupling#^echo-filter]]

CPMG with $n$ pulses: pulses at $\frac{j-1/2}n\,t$, filter peak near $\omega\approx\pi n/t$

> [!eg]- eg. the echo filter blocks slow noise
> at small $\omega$, $\sin(\omega t/4)\approx\omega t/4$, so $g_{\text{echo}}\approx(\omega t/4)^2\to0$, while Ramsey's $\text{sinc}^2\to1$. at $\omega t=2\pi$ (one full cycle), $g_{\text{echo}}=\frac{\sin^4(\pi/2)}{(\pi/2)^2}=\frac4{\pi^2}\approx0.41$ and Ramsey's is $0$

> [!exercise] exercise
> CPMG over $t=50\,\mu$s, and you want the filter near 1 MHz. roughly how many pulses?

> [!answer]-
> $f\approx n/(2t)$ → $n\approx2\times50\times10^{-6}\times10^6=100$ pulses
## 6. rotary echo
from [[Rotary echo]]

![[Rotary echo#^rotary-echo]]

> [!eg]- eg. a 10% weak drive
> each half rotates by $0.9\pi$ instead of $\pi$: $+0.9\pi$ then $-0.9\pi$, total $0$. without the echo, a full $2\pi$ Rabi cycle would stop at $1.8\pi$, missing $|0\rangle$ by $0.2\pi$

> [!exercise] exercise
> a rotary echo with 3 reversals (4 equal segments, alternating $+x$ and $-x$). does it still end at $|0\rangle$ for any amplitude?

> [!answer]-
> yes: $+\theta-\theta+\theta-\theta=0$ for any $\theta$. more reversals also cancel noise that changes during the run

## 7. magic state distillation
from [[Magic state distillation]]

![[Magic state distillation#^t-state]]

![[Magic state distillation#^distill-error]]

> [!eg]- eg. two levels at $p=5\times10^{-4}$
> level 1: $35\times(5\times10^{-4})^3=35\times1.25\times10^{-10}\approx4.4\times10^{-9}$. level 2: $35\times(4.4\times10^{-9})^3\approx3\times10^{-24}$

> [!exercise] exercise
> what physical error rate $p$ makes one level of 15 to 1 give $p_{out}=10^{-10}$?

> [!answer]-
> $p^3=10^{-10}/35\approx2.9\times10^{-12}$, so $p\approx1.4\times10^{-4}$
## 8. decoder numbers
from [[Decoding the surface code#how much data]]

bits per second $\approx\frac{N_{\text{qubits}}/2}{t_{\text{round}}}$, about 1 in 20 of them detection events at $p\sim0.1\%$, and about 1 CPU core per 100 physical qubits

> [!eg]- eg. a million qubits
> $\frac{5\times10^5}{10^{-6}\text{ s}}=5\times10^{11}$ bits/s, $2.5\times10^{10}$ detection events/s, $10^4$ cores

> [!exercise] exercise
> a slower chip takes 5 µs per round with 50,000 qubits. how many bits per second?

> [!answer]-
> $\frac{25{,}000}{5\times10^{-6}}=5\times10^9$ bits/s

see also [[Course 4 Week 2 formulas]]

week hub: [[Quantum error mitigation]]
