# Quantum Computing Notes

My personal study notes from three **MIT xPRO** quantum computing courses, written in [Obsidian](https://obsidian.md).

## The courses

| folder                    | course                                                                                                                    | program                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `Course 1` | [Introduction to Quantum Computing](https://xpro.mit.edu/courses/course-v1:xPRO+QCFx1/)                                   | [Quantum Computing Fundamentals](https://xpro.mit.edu/programs/program-v1:xPRO+QCF/) (course 1 of 2) |
| `Course 2` | [Quantum Algorithms for Cybersecurity, Chemistry, and Optimization](https://xpro.mit.edu/courses/course-v1:xPRO+QCFx2/)   | [Quantum Computing Fundamentals](https://xpro.mit.edu/programs/program-v1:xPRO+QCF/) (course 2 of 2) |
| `Course 3` | [Practical Realities of Quantum Computation and Quantum Communication](https://xpro.mit.edu/courses/course-v1:xPRO+QCRx1) | [Quantum Computing Realities](https://xpro.mit.edu/programs/program-v1:xPRO+QCR/) (course 1 of 2)    |

## What's in here

- **Course 1** → quantum gates (single qubit and multi qubit), the Bloch sphere, unitary operations
- **Course 2** → Fourier transforms and the QFT, Shor's algorithm, quantum phase estimation, photons, polarization, and QKD (BB84, BBM92, Ekert91)
- **Course 3**
  - *Week 1* → density matrices, quantum channels (dephasing, depolarizing, amplitude damping), noise, Rabi oscillations, noise spectra
  - *Week 2* → information theory (Shannon and von Neumann entropy, channel capacity), EPR, Bell and the CHSH game
- **Math** → the maths behind all of it: complex numbers, Dirac notation, probability, modular arithmetic, eigenvalues, tensor products, the trace. Start at [`Math/Math.md`](Math/Math.md) if something doesn't make sense

## How to read these

The notes are made for **Obsidian**, so the best way to read them is to download this repo and open the folder as a vault in Obsidian (it's free). Then all the links between notes, the pictures, and the graph view work.

On GitHub the maths and diagrams show up fine, but Obsidian specific things like `[[links]]`, `![[image embeds]]` and callout boxes show up as plain text.

## Notes on the content

- These are **my own notes**, not official MIT material, and I'm not affiliated with MIT. If something's wrong it's my mistake, not the course's
- The pictures were made by me: diagrams and plots with Python (matplotlib), and circuit diagrams with [Qiskit](https://www.qiskit.org/)
- The original papers I read for Course 3 (EPR 1935 and Schrödinger 1935) aren't included because they're copyrighted, the notes link to them by DOI instead

## License

These notes and pictures are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (see [`LICENSE`](LICENSE)): you can share and adapt them for anything, as long as you give credit to [ArhamAkhtarAlam](https://github.com/ArhamAkhtarAlam) and link back here.

This doesn't cover MIT's course material (which isn't included) or the Obsidian theme in `.obsidian/themes/`, which belongs to its own creator.
