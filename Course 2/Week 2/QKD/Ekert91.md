#QKD #Ekert91 #entanglement
![[Ekert91.png]]
This is [[Ekert91]] just like [[BBM92]] it uses [[Entangled Photons generation and detection|Entangled Photons]] and it is also a part of [[QKD]] unlike [[BB84]]

the Bell test it uses is the [[CHSH game]]: if Alice and Bob's results win more than 75% of the time the photons are really entangled, so nobody messed with them (see [[CHSH quantum strategy]])
```mermaid
sequenceDiagram
    participant Source as Entangled Source
    participant Alice
    participant Bob
    participant PublicChannel as Public Channel
    participant Eve

    autonumber 1
    Source->>Alice: Photon A (entangled)
    autonumber 1
    Source->>Bob: Photon B (entangled)

    Eve-->>Alice: (Optional) Intercept photon
    Note right of Eve: Measurement disturbs entanglement

    
    Alice->>Alice: Measure photon<br/>(random setting)
    autonumber 3
    Bob->>Bob: Measure photon<br/>(random setting)
    Note right of Alice: Independent measurements<br/>no causal order

    
    Alice->>PublicChannel: Announce measurement setting
    autonumber 4
    Bob->>PublicChannel: Announce measurement setting

    
    Alice->>PublicChannel: Reveal subset of outcomes
    autonumber 5
    Bob->>PublicChannel: Compute correlations<br/>(Bell test)
    Note right of PublicChannel: Bell inequality violation<br/>→ secure channel

    
    Alice->>Bob: Error correction
    Alice->>Bob: Privacy amplification
    Note right of Bob: Shared secret key

```
