#entropy #shannon_entropy #information_theory
the classical measure of information, used in [[Quantum Communication|classical communication]]
## what it is
$H(X)$ = the number of **bits** you need on average to faithfully represent a message $x$

if message $x$ happens with probability $p(x)$
$$
H(X)=-\sum_xp(x)\log_2p(x)
$$
basically: how **surprising** / random the message is
- always the same message → $H=0$ (no surprise, you don't need to send anything)
- all messages equally likely → $H$ is as big as it can be
## example: a coin
a coin that lands on 1 with probability $p$ (this is called the **binary entropy**)
$$
H(p)=-p\log_2p-(1-p)\log_2(1-p)
$$
- fair coin $p=\frac12$ → $H=1$ bit
- $p=0.9$ → $H\approx0.47$ bits (it's usually 1 so it's less surprising, and you can compress it)
- $p=0$ or $1$ → $H=0$

![[Binary_entropy_and_BSC_capacity.png]]
(left side, the right side is in [[Channel capacity]])
## mutual information
$I(X;Y)$ = how much info the received message $y$ gives you about the sent message $x$
$$
I(X;Y)=H(X)-H(X|Y)
$$
- $H(X|Y)$ is how much you still don't know about $x$ after seeing $y$
- no noise → $y$ tells you everything → $I=H(X)$
- total noise → $y$ tells you nothing → $I=0$

![[Mutual_information.png]]

it's what [[Channel capacity]] is built from

see also [[Von Neumann entropy]] (the quantum version)
