# Effects of T1 Noise on the Deutsch–Jozsa Algorithm

📄 **Paper:** `paper/aranda_deutsch_jozsa_t1_noise.pdf`  
📊 **Final Presentation:** `presentation/deutsch_jozsa_t1_noise_final.pptx`

This repository contains a **Hamiltonian-level investigation** of how **T1 (amplitude damping) noise** affects the Deutsch–Jozsa quantum algorithm.

Unlike typical circuit-level demonstrations, all quantum gates and noise processes in this project are **derived and applied manually** using first-principles quantum mechanics. The goal is to expose how physical noise mechanisms directly impact algorithmic behavior.

---

## Abstract

The Deutsch–Jozsa algorithm is one of the earliest quantum algorithms demonstrating a separation between classical and quantum computation under ideal conditions. However, real quantum hardware is subject to decoherence mechanisms that can significantly degrade algorithmic performance.

This project analyzes the effect of **T1 relaxation noise** on the Deutsch–Jozsa algorithm by modeling quantum gates via explicit Hamiltonians and injecting noise using the **Lindblad master equation**. Five experimental trials are conducted, beginning with an ideal noise-free case and progressing through increasing relaxation durations. The results visualize state relaxation and motivate **quantum error correction** as a potential mitigation strategy.

---

## Key Characteristics of This Work

This project intentionally avoids high-level abstractions in order to highlight the underlying physics.

- **Hamiltonian-based gate construction**
  - Hadamard and Z gates realized via explicit Hamiltonians
  - Gates applied using the unitary time evolution operator  
    `U(t) = exp(-i H t / ħ)`

- **Density-matrix formalism**
  - Two-qubit system represented using a ρ density matrix
  - Explicit normalization applied to preserve physical validity

- **Manual noise modeling**
  - No Qiskit noise models or built-in channels
  - T1 noise derived directly from the **Lindblad master equation**
  - Modified ladder operators tensored to target a single qubit

- **Physically meaningful timing**
  - π-rotation times derived analytically
  - Noise injected only after the final Hadamard gate, when excited states exist

This approach aligns more closely with **quantum control and hardware-aware modeling** than with standard circuit-level simulations.

---

## Repository Structure
```
deutsch-jozsa-t1-noise/
├── README.md
├── paper/
│ └── aranda_deutsch_jozsa_t1_noise.pdf
├── math/
│ ├── gate_hamiltonians.md
│ ├── lindblad_derivation.md
│ └── scans/
├── code/
│ ├── src/
│ │ ├── hamiltonians.py
│ │ ├── unitary_evolution.py
│ │ ├── lindblad_t1.py
│ │ └── deutsch_jozsa.py
│ └── requirements.txt
├── results/
│ ├── raw/
│ └── plots/
├── presentation/
│ └── deutsch_jozsa_t1_noise_final.pptx
├── CITATION.cff
└── LICENSE
```


---

## Experimental Overview

### Trial 1 — Ideal (Noise-Free)
- Constant and balanced oracle evaluations
- Correct identification of function type
- Expected measurement distributions

### Trials 2–5 — Increasing T1 Noise
- Noise injected after the final Hadamard gate
- Relaxation time increased from 1 to 4 seconds
- Progressive decay of the excited |01⟩ state
- Visualization of decoherence effects

---

## Key Insight

During early testing, non-physical probabilities (greater than 1 or less than 0) were observed due to loss of normalization during noise injection. This issue was resolved by renormalizing the density matrix using:

ρ → ρ / Tr(ρ)

yaml
Copy code

This observation motivated further investigation into **quantum error correction**, where auxiliary qubits can absorb noise without collapsing computational states.

---

## Why This Repository Exists (For Recruiters)

This repository exists to demonstrate **how I think and work as an engineer**, not just what tools I can use.

Most quantum computing examples rely on pre-built gates, simulators, and noise models. In contrast, this project shows my ability to:

- Translate mathematical models into working software
- Reason at the Hamiltonian and density-matrix level
- Implement physically motivated noise processes from first principles
- Debug non-obvious numerical and physical issues (e.g., normalization drift)
- Communicate complex technical ideas clearly in written and visual form

Although this work focuses on quantum computing, the skills demonstrated here are broadly applicable to:

- Scientific and numerical computing
- Simulation and modeling
- Systems-level reasoning
- Research-driven software engineering
- Working close to hardware constraints

This repository is representative of how I approach unfamiliar, complex technical problems: by breaking them down mathematically, implementing them carefully, and validating results rigorously.

---

## Technologies Used

- Python
- Qiskit (used only as a numerical platform)
- Linear algebra
- Density-matrix quantum mechanics
- Lindblad master equation

---

## Author

**Stephen Aranda**  
B.S. Computer Science — University of Texas at Dallas  

Focus areas:
- Quantum computing
- Hamiltonian-level modeling
- Noise and decoherence
- Reproducible scientific software

---

## Notes

This project was conducted as part of *PHYS 4346: Quantum Mechanics for Engineers and Programmers* and reflects original analytical and experimental work. All gates and noise processes were derived manually to emphasize physical realism over abstraction.