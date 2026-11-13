#vlsi #microwind #formulas
all the formulas and key numbers from [[Microwind course]] in one place

## 1. equivalent width
![[Weq_cross_sections.png]]

![[Transistor evolution#^weq-table]]

![[Transistor evolution#^weq-finfet]]

> [!eg]
> 7 nm, 14 fins of 35 × 4 nm: $(70+4)\times14=1036$ nm ≈ 1 µm. 5 nm uses 45 nm tall fins, so 11 fins ≈ 1 µm

## 2. lambda rules
![[Microwind#^lambda-rules]]

## 3. cell height
![[Cell_tracks.png]]

![[Nanosheet cell design#^track-count]]

> [!eg]
> 7 tracks × 24 nm + rails = 192 nm (7 nm FinFET), 5 × 24 = 120 nm (3 nm), 5 × 20 = 100 nm (2 nm with buried rails)

## 4. the current (simplified BSIM4)
![[MOS models and BSIM#^ids-bsim]]

## 5. device numbers

| device | $I_{on}$ | $I_{off}$ |
|---|---|---|
| n-FinFET, low leakage | 1.4 mA/µm | 1 nA |
| n-FinFET, high speed | 1.7 mA/µm | 10 nA |
| p-FinFET, low leakage / high speed | 1.2 / 1.5 mA/µm | 1 / 10 nA |
| n-nanosheet, LP slow (4 λ) | 250 µA | 0.25 nA |
| n-nanosheet, LP fast (8 λ) | 400 µA | 0.41 nA |
| n-nanosheet, HP fast | 500 µA | 4.7 nA |

## 6. metal stack
![[Metal_stack.png]]

![[FinFET cell design#^metal-stack]]

## 7. the node table
![[Technology scaling#^node-table]]

## 8. ring oscillator
$$
f=\frac1{2Nt_d}
$$
($N$ stages, delay $t_d$ each, see [[Ring oscillator]])
