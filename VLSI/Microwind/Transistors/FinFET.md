#vlsi #transistor #FinFET
the transistor of the **14 nm to 5 nm** nodes: the channel is a set of thin vertical **fins** with the gate wrapped over 3 sides. part of [[Microwind course]], shape comparison in [[Transistor evolution]]

## the parameters
a MOSFET is set by its width $W$ (6–12 λ) and length $L$ (2 λ). a FinFET instead has

| parameter | typical | 14 nm (λ = 8 nm) |
|---|---|---|
| number of fins $N_F$ | 2–5 | |
| fin pitch $P_F$ | 6 λ | 48 nm |
| fin thickness $T_F$ | 1 λ | 8 nm |
| fin length = gate length $L_G$ | 2 λ | 16 nm |
| fin height $H_F$ | fixed by the process | 30–45 nm |

the width is no longer something you draw: ==you can only choose **how many fins**==, so the current comes in steps

![[Transistor evolution#^weq-finfet]]

## layout
- instead of one wide diffusion strip, the channel is made of parallel fins
- same $I_{on}$ in a **smaller area**, and lower $I_{off}$ at the same $I_{on}$
- comes with **dummy gates** on both sides (unused gate lines that keep the pattern regular for manufacturing)

![[FinFET_inverter_layout.png|400]]

### 2 drawing styles

| style | fins | used for |
|---|---|---|
| (smallest) | 1 | very dense cells like SRAM |
| **HD**, high density | 2 | most logic |
| **HP**, high performance | 4 | fast cells |
| more | 5+ | driving big loads (strong currents) |

## device options
industry offers up to ~10 flavours of transistor, [[Microwind]] has 3

| option | threshold | n-FinFET $I_{on}$ | p-FinFET $I_{on}$ | $I_{off}$ | when |
|---|---|---|---|---|---|
| **low leakage** (RVT, regular $V_T$) | normal | 1.4 mA/µm | 1.2 mA/µm | 1 nA | nearly always, the default |
| **high speed** (LVT, low $V_T$) | lower | 1.7 mA/µm | 1.5 mA/µm | 10 nA | rarely, to speed up critical paths |
| **high voltage** (I/O, 1 V) | higher | | | | very rarely, I/O and RF |

(all per µm of equivalent width, at 0.65 V. 14 fins ≈ 1 µm)

lowering $V_T$ gives about 20% more current but **10× more leakage**, which is why it's used sparingly

![[FinFET_Vt_options.png]]

the p-FinFET is **almost as good** as the n-FinFET (holes are slower than electrons), thanks to gate, drain and source engineering and strain

## 7 nm vs 5 nm
- λ stays the same (4 nm), so there's no big shrink
- 5 nm has **taller fins**: $H_{fin}=45$ nm instead of 35, so **11 fins** give 1 µm instead of 14
- taller fins → 3 or 2 fins are enough in cells, no need for 4
- better speed and power, at least in simulation (see [[Ring oscillator]])

## variability
real fins aren't all identical. a Monte-Carlo simulation on process parameters gives a spread of $I_{on}$ curves (roughly 1.0 to 1.8 mA at the same voltage). the corners:
- **minimum**: slow process, high temperature, low voltage
- **maximum**: fast process, low temperature, high voltage

misaligned fins make this spread worse (see [[FinFET cell design#layout rules]])

![[Fin_alignment.png]]

## the real model
industry simulates FinFETs with **BSIM-CMG** (common multi-gate, from Berkeley, versions 100–110 for FinFET, 111 adds nanosheets). [[Microwind]] uses a simplified BSIM4 with the equivalent width trick instead (see [[MOS models and BSIM]])

> [!exercise] try this
> a 5 nm n-FinFET (high speed, $H_{fin}=45$ nm) needs 0.5 mA. roughly how many fins?

> [!answer]-
> 11 fins ≈ 1 µm gives about 1.7 mA, so each fin gives about $1.7/11\approx0.155$ mA. $0.5/0.155\approx3.2$ → **4 fins** (you round up, since 3 isn't quite enough)

see also [[Transistor evolution]], [[Nanosheet FET]], [[FinFET cell design]]
