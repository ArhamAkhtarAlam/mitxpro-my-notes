#math #logarithms
$e^x$ and $\ln x$ undo each other, and between them they describe anything that decays, grows, or spans many orders of magnitude: qubit $T_1$ decay, light absorbed in a film, a diode's current, decibels
## exponentials
$$
y=y_0\,e^{-t/\tau}
$$
^exp-decay

- $\tau$ is the **time constant**: every $\tau$, $y$ gets multiplied by $1/e\approx0.37$
- the **half-life** is $t_{1/2}=\tau\ln2\approx0.69\,\tau$
- after $3\tau$ about 5% is left, after $5\tau$ under 1%

the key property: ==an exponential loses the **same fraction** in every equal time step==, not the same amount. that happens whenever the rate of loss is proportional to how much is left ($\frac{dy}{dt}=-\frac y\tau$)

| where | what decays | time constant |
|---|---|---|
| [[Amplitude damping channel]] | excited state population | $T_1$ |
| [[Dephasing and the filter function]] | phase coherence | $T_2$ |
| [[UV-vis spectroscopy]] | light intensity going into a film | $1/\alpha$ (a length) |
| [[MSA]] | a cantilever's ringing | $\propto Q$ |

## the three logs

| written | base | used for |
|---|---|---|
| $\ln x$ | $e\approx2.718$ | anything with $e$ in it: decay, diodes, thermal $k_BT$ |
| $\log_{10}x$ | 10 | absorbance, decibels, "per decade" |
| $\log_2x$ | 2 | bits and qubits |

switch between them with $\log_ba=\frac{\ln a}{\ln b}$. the two worth memorising: $\ln10\approx2.303$ and $\ln2\approx0.693$. all the rules:

![[Big O notation#^log-rules]]
## why logs turn curves into lines
take the log of $y=y_0e^{-t/\tau}$:
$$
\ln y=\ln y_0-\frac t\tau
$$
a straight line in $t$, with slope $-1/\tau$. so ==plot $\ln y$ (or use a log axis) and an exponential becomes a straight line whose slope gives the time constant== (more in [[Straight line fits]])

![[Exponential_log_axis.png]]
## where the notes use it
**absorbance** is a $\log_{10}$ of the transmitted fraction:

![[UV-vis spectroscopy#^beer-lambert]]

and the absorption coefficient of a film is the $\ln$ version ([[UV-vis spectroscopy#^absorption-coefficient]]): intensity falls as $e^{-\alpha t}$

**decibels**: $\text{dB}=10\log_{10}\frac{P_{in}}{P_{out}}$. every 10 dB is a factor of 10, every 3 dB a factor of 2

**a diode** ([[Electrical characterization]]): $I\approx I_se^{qV/nk_BT}$, so $\ln I$ against $V$ is a line with slope $\frac q{nk_BT}$, which gives the ideality factor $n$. on a $\log_{10}$ axis the same line needs $n\frac{k_BT}q\ln10\approx n\times59.5$ mV per decade at 300 K: that's where the **60 mV/dec** limit on a transistor's subthreshold swing comes from

**the four-point probe**: $R_{sh}=\frac\pi{\ln2}\frac VI$ ([[Sheet resistance and contacts#^four-point]]), the $\ln2$ coming from integrating the current spreading out from a point

> [!eg] $T_1$ numbers
> $T_1=100\,\mu$s. after a $1\,\mu$s gate, the chance the qubit has **not** relaxed is $e^{-0.01}\approx0.990$, so about a 1% error. small $x$ shortcut: $e^{-x}\approx1-x$. after $69\,\mu$s ($T_1\ln2$) it's 50/50

> [!exercise] try these
> ① a film transmits 25% of the light. what's its absorbance?
> ② a fibre loses 0.2 dB per km. what fraction of the light is left after 100 km?
> ③ a signal drops to 10% in $46\,\mu$s. what's its time constant?
> ④ why is the $\ln$ (not $\log_{10}$) the natural one for a diode?

> [!answer]-
> ① $A=-\log_{10}0.25=0.60$
> ② $0.2\times100=20$ dB = a factor $10^{20/10}=100$: 1% is left
> ③ $e^{-46/\tau}=0.1$ → $\tau=\frac{46}{\ln10}=20\,\mu$s
> ④ the current comes from a Boltzmann factor $e^{-E/k_BT}$, so $e$ is built in. $\log_{10}$ is just for reading plots in decades, at the cost of the $\ln10$ factor

see also [[Big O notation]] (log rules, growth rates), [[Probability and expectation values]] ($\log_2$ and entropy), [[Peak shapes and FWHM]], [[Math]]
