#single_photon #photons #detectors
# Single photon generation
There are two main methods for single photon generation
- Attenuation(aka just making a coherent source of light less intense)
- optically active quantum dot(aka just a crystal with some electron stuff)
This is done so we can [[Polarization|polarize]] a single photon
## Attenuation
Attenuation is making a coherent source of light sooo dim that it might just emit 1 photon (but it's kinda bad cuz most of the time no photons come, and sometimes 2 come at once)

## Optically active quantum dot
It's just a tiny piece of semiconductor that can be excited so that the electron will jump to a higher energy state and then come back releasing a photon

# Single photon detecting
most of the time they use an **avalanche photodiode** (SPAD, single photon avalanche diode) like the picture below
![[Single photon detection.png]]
so when a photon comes it makes an electron (-) and hole (+) pair, they get separated, and the electron speeds up and breaks more pairs which breaks even more pairs, an avalanche that makes a large current you can measure

used in [[QKD]] methods like [[BB84]]
