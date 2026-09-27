#QKD #BBM92 #entanglement
![[Course 2/Week 2/Images/BBM92.png]]
This is the [[BBM92]] protocol it is a part of [[QKD]]
so in here we need another person to supply [[Entangled Photons generation and detection|entangled photons]] just like [[Ekert91]] unlike [[BB84]]

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
    Note over Eve: Disturbs entanglement

    Note over Alice,Bob: Random measurement bases
    Alice->>Alice: Measure photon
    autonumber 3
    Bob->>Bob: Measure photon

    Alice->>PublicChannel: Announce bases
    autonumber 4
    Bob->>PublicChannel: Announce bases

    Note over Alice,Bob: Keep matching bases

    Alice->>PublicChannel: Reveal sample bits
    Bob->>PublicChannel: Check error rate

    Note over Alice,Bob: High error → Eve detected

    Alice->>Bob: Error correction
    Alice->>Bob: Privacy amplification

    Note over Alice,Bob: Shared secret key

```

 