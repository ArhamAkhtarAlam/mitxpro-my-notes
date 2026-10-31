#information_theory #channel_capacity #threshold #fault_tolerance
## where this is going
the start of a journey: **how do you build a computer out of noisy components?**
1. a **computational capacity** idea, borrowed from communication (this note)
2. that sets the stage for the **threshold**: below some error rate, noisy parts can still compute reliably ([[Threshold theorem]])
3. the principles that make this possible for **classical** computation
4. then generalising them to the **quantum** case ([[Fault-tolerant quantum computing]])
## Shannon's channel capacity
the idea of **capacity** came out of communication: a seminal result by **Claude Shannon** in the 1940s ([[Channel capacity]], [[Shannon entropy]])

two parties have a communication link, but the link is **noisy**: a wire plus noise. what's the **maximum rate** (eg. bits per second) they can communicate at, despite the noise?

> [!quote]- Shannon 1948: A mathematical theory of communication
> *The Bell System Technical Journal* **27**, pp. 379–423 and 623–656 (July and October 1948)
> - defines entropy as the measure of information, and the capacity of a channel
> - the noisy channel coding theorem: below the capacity the error can be made as small as you like, above it it can't
>
> ![[Shannon 1948 - A mathematical theory of communication.pdf#height=500]]
### pre-Shannon
plot the probability of error (0 to 1) against the rate
- the faster you talk, the more mistakes: talk at an in-between speed and some people understand you and some don't
- so the error grows steadily as the rate goes up. that seems quite reasonable
### Shannon
Shannon proved you can do **much** better than this
- you can get the error **exponentially close to zero** (asymptotically)
- for every rate up to a magical point, the **capacity** $C$ of the channel
- only above $C$ does the error shoot up

![[Channel_capacity_error_vs_rate.png]]

> [!important] the one idea
> ==noise doesn't force errors: below the capacity, error correcting codes make communication essentially perfect, and above it nothing can==. the error jumps from "basically zero" to "a lot" at one point, instead of creeping up

the capacity is the best mutual information you can get over the channel

![[Channel capacity#^capacity]]

### why it works: error correcting codes
as long as the error rate is low enough, repeat the message three times, repeat the message three times, repeat the message three times. if you catch it two of the three times you can use **majority voting** to work out what was meant, even when I'm talking fast. it's the classical version of the [[Bit flip code]]

> [!eg] a binary symmetric channel that flips 10% of bits
> - capacity: $C=1-H(0.1)=1-0.469=0.53$ bits per use ([[Binary symmetric channel]])
> - repeat 3 times and majority vote: error $3p^2-2p^3=0.028$, but the rate drops to $\frac13$
> - repeat 5 times: error $\binom53p^3(1-p)^2+\binom54p^4(1-p)+p^5=0.0086$, rate $\frac15$
>
> repetition makes the error smaller, but the rate goes to **zero** as you repeat more. ==Shannon's surprise is that smarter (longer) codes push the error to zero while keeping the rate fixed, anywhere below 0.53==
## the analogy for computation
this is a **discrete jump** in what a channel can do despite errors. the same kind of jump will happen for computation

| | communication (Shannon) | computation |
|---|---|---|
| noisy thing | a wire / channel | gates, components |
| fixed by | error correcting codes | error correction, done fault tolerantly |
| the magic point | the **capacity** $C$ (a rate) | the **threshold** $p_{th}$ (an error rate per gate) |
| below it | error exponentially close to 0 | as long a computation as you want, with tiny error |

we already saw the seed of this: the bit flip code only helps if $p$ is below a threshold ([[Bit flip code#the threshold]])

> [!exercise] try these
> ① a binary symmetric channel flips 1% of bits. what's its capacity? (use $H(0.01)=0.081$)
> ② you want an error below $10^{-3}$ on the 10% channel using only repetition. is 5 copies enough? what about 7?
> ③ why can't you communicate reliably over a channel that flips 50% of bits, however clever the code?

> [!answer]-
> ① $C=1-0.081=0.92$ bits per use: you lose only 8% of the rate to noise, even though fixing it needs a code
> ② 5 copies gives $0.0086$, not enough. 7 copies fails with 4 or more flips: $\binom74p^4(1-p)^3+\binom75p^5(1-p)^2+\dots\approx0.0027$, still not enough (9 copies gives about $0.00089$). the rate is only $\frac19$ by then, which is why repetition is a bad code
> ③ $C=1-H(0.5)=1-1=0$: the output is a fair coin flip, independent of the input, so no information gets through

next: von Neumann asks the same question for gates, [[Triple modular redundancy]]

see also [[Channel capacity]], [[Bit flip code]], [[Quantum Communication]]

week hub: [[Detecting and correcting errors]]
