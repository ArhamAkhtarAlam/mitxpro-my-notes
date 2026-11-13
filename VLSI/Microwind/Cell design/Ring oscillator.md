#vlsi #ring_oscillator #benchmark
the standard way to measure how **fast** and how **power hungry** a technology is. part of [[Microwind course]]

## the circuit
an **odd** number of inverters in a loop. there's no stable state (every inverter flips the signal, and an odd number of flips can't agree with itself), so it oscillates

![[Ring_oscillator.png]]

the usual benchmark is **RO3, FO3**: 3 stages, each driving a **fan-out of 3** (3 inverter inputs as load), so it looks like a real circuit where outputs drive several gates

each node is the one before it, flipped, one stage delay later:

![[Ring_oscillator_waveforms.png]]

each stage is one CMOS inverter:

![[CMOS_inverter.png|260]]

## what you measure
- the **frequency** → speed of one stage
- the **power per stage** → energy per switch

plot power against frequency while sweeping $V_{DD}$ (eg. 0.5 → 0.8 V): higher voltage = faster but more power. a better technology sits **lower and further right**

## results

| comparison | result |
|---|---|
| 14 nm FinFET (0.8 V) vs 45 nm MOSFET (1 V) | **4× faster** at the same power, or **3× less power** at the same speed |
| 5 nm FinFET: high performance vs low power | HP is faster at the same voltage but uses more power ($I_{off}$ 20 nA vs 2 nA) |
| 3 nm nanosheet vs 5 nm FinFET | **56% less** power at the same frequency, **30% faster** at the same power |
| 1 nm CFET (not yet calibrated) | about 535 GHz, 17 µW per stage |

![[NS_vs_FinFET_power.png]]

the Microwind 5 nm results land close to published 5 nm ring oscillators, and the 3 nm nanosheet close to published 3 nm and 2 nm points

> [!extra]- frequency from the stage delay
> a rising edge has to go round the loop twice (once to flip everything, once to flip it back) for one full period, so
> $$
> f=\frac1{2Nt_d}
> $$
> for $N$ stages each with delay $t_d$
>
> > [!eg]
> > 3 stages at 100 GHz: $t_d=\frac1{2\times3\times100\times10^9}\approx1.7$ ps per stage

> [!exercise] try this
> why must the number of inverters be odd?

> [!answer]-
> with an even number the loop has 2 stable states (eg. 0,1,0,1 all agree), so it just sits there like a latch. with an odd number, going round the loop gives the opposite of what you started with, so it can never settle

see also [[FinFET cell design]], [[Nanosheet FET]], [[Technology scaling]]
