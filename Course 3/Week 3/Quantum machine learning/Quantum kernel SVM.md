#quantum_machine_learning #SVM #kernel #NISQ
IBM's experiment: a [[Support vector machines|support vector machine]] where a **quantum computer calculates the kernel**. part of [[Quantum machine learning]]
## the idea
for some kinds of data there's a feature map into **quantum states**, where the inner products are easy for a quantum computer but (for big enough problems) hard for a normal one
```mermaid
flowchart TD
    X["data point x"] --> FM["quantum feature map<br/>(gates depend on x)"] --> S["quantum state |φ(x)⟩"]
    S --> K["quantum computer estimates<br/>overlaps |⟨φ(x)|φ(y)⟩|²<br/>= the kernel"]
    K --> C["classical computer finds<br/>support vectors + classifies"]
```
> [!note] the split
> - **quantum**: estimate the kernel (the hard part)
> - **classical**: find the support vectors from the kernel (easy once you have it)

## the data set
a made up data set with **2 features** and **2 classes** (red and blue), with a **gap** between them to make it a bit easier. it's built so that a feature map into **2 qubit states** (2 qubit [[Density matrix|density matrices]]) works for it

if the same kind of data had way more dimensions, you'd need a bigger quantum computer (with low enough noise) to estimate the inner products, and it's chosen so those would be hard to calculate classically
## the quantum feature map
### 1 qubit (easy to picture)
the line from $0$ to $2\pi$ gets mapped onto a curve on the [[Bloch sphere]], using just basic gates ([[Hadamard Gate|H]]) and [[Phase shift|phase gates]] that depend on $x$
![[Feature_map_Bloch.png|500]]
(this example does H and a phase gate twice. it's my simulation, the exact gates in the experiment might differ)
### 2 qubits
same idea on each qubit, plus **entanglement** between them using [[CZ gate|CZ]] type interactions
## the experiment
```mermaid
flowchart TD
    T["training set:<br/>20 points per class"] --> M["map each point into<br/>a 2 qubit state"]
    M --> K["quantum processor estimates the<br/>inner product of every pair<br/>→ 40 × 40 kernel"]
    K --> SV["find the support vectors<br/>(classically)"]
    SV --> N["new points: quantum processor<br/>compares them with the<br/>support vectors only"]
    N --> R["which side of the cut?<br/>→ label"]
```
1. **training set**: 20 points per label
2. map each one into the 2 qubit space and use the quantum processor to estimate the [[Math/Dirac notation|inner product]] of **every pair** → the **kernel**, a $40\times40$ matrix (symmetric and positive semidefinite, from real quantum hardware)
3. find the **support vectors** from the kernel (done on a normal computer)
4. for each **new** point, use the quantum processor to get its inner products with just the support vectors (all the other training points can be forgotten), and see which side of the cut it lands on
### result
the new, randomly drawn points were classified with **100% success**

## my simulation of it
I re-ran the same steps in a simulation (not the real hardware data): a 2 qubit feature map with H, phase and entangling gates, a made up data set with a gap, 20 training points per class
![[Quantum_kernel_matrix.png|500]]
the kernel: bright = very similar states. the 2 bright blocks show points of the **same** class overlap a lot, and points of different classes don't. symmetric and positive semidefinite, like the real one
![[Quantum_kernel_SVM.png]]
9 support vectors (circled), and **100%** of the new points (squares) classified right, just like the experiment

> [!extra]- how a quantum computer measures an overlap (extra, not in the lecture)
> prepare $|\phi(y)\rangle$ by running the feature map circuit for $y$, then run the feature map for $x$ **backwards** ($U(x)^\dagger$), and measure. the chance of getting all 0s is
> $$
> |\langle0\ldots0|U(x)^\dagger U(y)|0\ldots0\rangle|^2=|\langle\phi(x)|\phi(y)\rangle|^2
> $$
> repeat many times to estimate it

## the classical version, step by step
### a classical kernel
the usual classical choice is the **Gaussian (RBF) kernel**
$$
K(x,y)=e^{-(x-y)^2/2}
$$
same point: $e^0=1$. the further apart, the bigger $(x-y)^2$, so the closer $K$ gets to 0. for 3 data points $x=0,\,1,\,3$, one pair at a time:
$$
\begin{aligned}
K(0,1):&\quad(0-1)^2=1\ \to\ e^{-1/2}\approx0.607\\
K(0,3):&\quad(0-3)^2=9\ \to\ e^{-9/2}\approx0.011\\
K(1,3):&\quad(1-3)^2=4\ \to\ e^{-4/2}=e^{-2}\approx0.135
\end{aligned}
$$
put them in a table: the diagonal is each point with itself (1), and it's symmetric since $K(x,y)=K(y,x)$
$$
K=\begin{bmatrix}1&0.607&0.011\\0.607&1&0.135\\0.011&0.135&1\end{bmatrix}
$$
just a formula per pair, done in a microsecond. this matrix goes into the SVM exactly like the quantum one does
### simulating the quantum kernel classically
the 1 qubit feature map is an $R_y(x)$ gate: $|\phi(x)\rangle=\cos\frac x2|0\rangle+\sin\frac x2|1\rangle$. kernel for $x=0$ and $y=0.5$:

**1. write each state as a vector** (top = amount of $|0\rangle$, bottom = amount of $|1\rangle$)
$$
|\phi(0)\rangle=\begin{bmatrix}\cos0\\\sin0\end{bmatrix}=\begin{bmatrix}1\\0\end{bmatrix}\qquad|\phi(0.5)\rangle=\begin{bmatrix}\cos0.25\\\sin0.25\end{bmatrix}=\begin{bmatrix}0.969\\0.247\end{bmatrix}
$$
**2. inner product** (multiply matching entries and add; all real here, so no conjugates needed)
$$
\langle\phi(0)|\phi(0.5)\rangle=1\times0.969+0\times0.247=0.969
$$
**3. square it** (the kernel is the overlap **squared**, because that's the probability a quantum computer actually measures: the chance of getting all 0s in the $U(x)^\dagger U(y)$ circuit)
$$
K(0,0.5)=0.969^2\approx0.939
$$
check with the shortcut $K=\cos^2\frac{x-y}2=\cos^2(0.25)\approx0.939$ ✅

easy for 1 qubit (2 numbers per state). but for $n$ qubits each state is $2^n$ numbers, and with entangling gates there's no shortcut formula, so at 50+ qubits a classical computer can't even store the states. ==that's the only place a quantum kernel can win: when the classical computer **can't** do steps 1–3==

## the honest bit
> [!warning] just a toy example
> ==the data set was made up and has no connection to real life data.== the point is to show the idea works on real quantum hardware. whether it beats classical methods on **real** problems is still an open question (see [[NISQ#where people are looking]])

see also [[Support vector machines]], [[Quantum machine learning]], [[NISQ]]
