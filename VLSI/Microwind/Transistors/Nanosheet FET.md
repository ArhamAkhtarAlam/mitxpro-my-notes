#vlsi #transistor #nanosheet #GAA
the transistor from **3 nm** on: the fin is replaced by a **stack of horizontal silicon sheets**, with the gate wrapped all the way around each one. part of [[Microwind course]], shape comparison in [[Transistor evolution]]

## many names, one device
- **nanosheet FET** (NSFET)
- **gate all around** (GAA)
- **multi-bridge channel FET** (MBCFET, Samsung's name)
- **RibbonFET** (Intel's name)

Samsung went first (3 nm, 2022–23), TSMC stayed with FinFET for its 3 nm and moves to nanosheets at 2 nm, Intel at 20A (2024). the search for a successor started long ago: a vertical "DELTA" device in 1991 (the first fin-like transistor) and Samsung's multi-bridge channel MOSFET in 2004

## the device
![[Nanosheet_3D.png]]

- **3 stacked sheets** (what all three companies seem to use)
- each sheet is 5 nm thick, with 10 nm between sheets

| parameter | value |
|---|---|
| gate length | 8 nm (2 λ) |
| sheet thickness | 5 nm |
| sheet spacing | 10 nm |
| sheet width | 16 nm (slow, 4 λ) or 32 nm (fast, 8 λ) |
| number of sheets | 3 |
| device height | 45 nm |
| $V_{DD}$ | 0.65 V |
| subthreshold slope | 60 mV/decade |

(these sit in the middle of published 3 nm designs, which use 3–4 sheets, widths 13–42 nm and 0.6–0.7 V)

![[Nanosheet_stack.png]]

![[Transistor evolution#^weq-table]]

## width is continuous again
a FinFET can only have whole fins, so its current jumps 1, 2, 3, 4 fins. a nanosheet's width is drawn, so ==you can set the current to anything you want== (from 4 λ up)

![[Ion_vs_width.png]]

## slow and fast, low power and high performance

| n-device | $I_{on}$ | $I_{off}$ |
|---|---|---|
| low power, slow (4 λ) | 250 µA | 0.25 nA |
| low power, fast (8 λ) | 400 µA | 0.41 nA |
| high performance, fast | 500 µA | 4.7 nA (**10×**!) |

the slow low power device has $W_{eq}=144$ nm and an **effective** current $I_{eff}=100$ µA (the average current while it switches, a better guide to speed than $I_{on}$). the p-device is close: 214 µA on, 90 µA effective, 0.3 nA off

each device has a gate capacitance of about **100 aF** ($10^{-16}$ F)

> [!eg] current per µm
> $I_{on}/W_{eq}=250\ \mu\text{A}/0.144\ \mu\text{m}\approx1.7$ mA/µm, a bit better than the regular FinFET's 1.4 mA/µm

## why bother
steeper turn-on than FinFET (closer to the 60 mV/decade limit), so less leakage for the same on current:

![[Id_Vg_three_devices.png]]

3 nm nanosheet vs 5 nm FinFET, in a 3-stage [[Ring oscillator]]:

![[NS_vs_FinFET_power.png]]

- at the **same frequency**: about 56% less power per stage
- at the **same power**: about 30% faster

> [!important] easier to design with than FinFET
> nanosheet layout looks like old MOSFET layout (draw a width), and it's **simpler**, because there's no n-well (see [[Nanosheet cell design]]). it should cover high-end chips from 2025 to 2030, including 6G

> [!exercise] try this
> you need 300 µA from a low power n-device. the slow one (4 λ) gives 250 µA and the fast one (8 λ) 400 µA. if current grows roughly linearly with width, what width do you draw?

> [!answer]-
> 150 µA per 4 λ step from 4 to 8 λ, so 37.5 µA per λ. you need 50 µA more than the slow one: $50/37.5\approx1.3$ λ more → about **5.3 λ**, round to **6 λ** to be safe. a FinFET couldn't do this: it would have to jump to the next whole fin

see also [[FinFET]], [[Buried power rails and CFET]], [[Nanosheet cell design]]
