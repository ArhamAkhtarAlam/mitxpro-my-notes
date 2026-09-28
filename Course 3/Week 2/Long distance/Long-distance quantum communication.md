#quantum_communication #quantum_internet #photons #long_distance
why sending quantum information far is so hard, and why we want to. part of [[Quantum Communication]]
## the problem: no amplifiers
normal (classical) communication uses **amplifiers** and **repeaters** all the time: when a signal gets weak, you just copy it, make it louder and send it on

quantum communication **can't** do that because of the **no-cloning theorem**: you can't copy an unknown quantum state
```mermaid
flowchart LR
    subgraph classical
    A1["weak signal"] --> B1["amplifier<br/>(copy + boost)"] --> C1["strong signal ✓"]
    end
    subgraph quantum
    A2["weak quantum state"] --> B2["amplifier?"] --> C2["not allowed ✗<br/>(no-cloning)"]
    end
```
> [!note] double edged
> no-cloning is exactly what makes [[QKD]] secure (Eve can't copy the photons), but it's also what stops us from amplifying them
## losing photons
photons are the best carriers of quantum information (they're fast, don't interact much with stuff, and we already have fibre everywhere), but fibre still **absorbs** them

the loss is **exponential** (the **Beer–Lambert law**). good fibre loses $0.2$ dB per km
$$
\text{fraction that arrives}=10^{-0.2\,L/10}\qquad(L\text{ in km})
$$
![[Fiber_loss.png]]

| distance | photons that arrive |
|---|---|
| 15 km | 50% |
| 100 km | 1% |
| 1000 km | $10^{-20}$ |

since you can't amplify, the error rate grows exponentially with distance. at some point the real photons are so rare that the detector's **dark counts** (fake clicks, see [[Single Photon making and detecting]]) drown them out

> [!info] where QKD is today
> that's why [[QKD]] in fibre only works up to about **100 km** in practice, nowhere near the global reach of the normal internet
## the quantum internet
the dream is a **quantum internet**: quantum computers and sensors all connected, sharing entanglement (most famously described by Jeff Kimble in *Nature* in 2008)

what it would be used for
- **blind quantum computing** → run your program on someone else's quantum computer in the cloud, and they can't see what you're computing
- **distributed quantum computing** → link smaller quantum computers into a bigger one
- **quantum sensing** → entanglement over long distances can make measurements more precise
- and longer distance [[QKD]]
## getting qubits onto photons (transduction)
lots of qubits aren't photons, so they have to be **converted** first, without destroying the quantum state
```mermaid
flowchart LR
    SC["superconducting qubit<br/>(microwave, only works super cold)"] --> T["transducer<br/>(keeps the quantum state)"]
    SP["electron / nuclear spin"] --> T
    ION["trapped ion<br/>(already optical, wrong colour)"] --> FC["frequency conversion"]
    T --> O["optical photon"]
    FC --> O
    O --> F["fibre (telecom wavelength)"]
```
- **superconducting qubits** (like IBM's) store the qubit in **microwaves**, which only stay clean at extremely low temperatures, so they can't just be sent down a fibre
- **spins** (electron or nuclear) have to be turned into light first
- **trapped ions** already give out light, but at the wrong frequency for fibre, so it has to be converted

the fix for all the loss is the **quantum repeater**, see [[Quantum repeaters]]

see also [[Quantum Communication]], [[QKD]]
