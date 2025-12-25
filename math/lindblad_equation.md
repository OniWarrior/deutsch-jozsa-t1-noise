# Lindblad-Based T1 Noise Modeling

This document describes how **T1 relaxation noise** was modeled and injected into
the Deutsch–Jozsa algorithm using the **Lindblad master equation**.

Unlike built-in noise models or abstract channels, all noise in this project was
derived analytically and applied directly to the system’s **density matrix**.
This approach allows precise control over timing, operator targeting, and
physical validity.

---

## Purpose and Scope

The goal of this document is to explain:

- Why the Lindblad formalism was chosen
- How T1 noise was mathematically modeled
- How relaxation was applied to a specific qubit
- How normalization issues were identified and resolved

This document focuses only on **noise modeling**. Gate construction is documented
separately in `gate_hamiltonians.md`.

---

## Why the Lindblad Formalism?

Real quantum systems are **open systems** that interact with their environment.
To model irreversible processes such as energy relaxation, unitary evolution
alone is insufficient.

The Lindblad master equation provides:

- A physically valid description of decoherence
- Completely positive, trace-preserving dynamics (when properly normalized)
- A natural framework for modeling T1 relaxation

This makes it well-suited for studying how noise affects algorithmic behavior.

---

## Density Matrix Evolution

All states in this project are represented using a **density matrix** ρ.

Unitary gate evolution is applied as:

ρ → U ρ U†

Noise processes are then applied to the same density matrix using non-unitary
time evolution governed by the Lindblad equation.

---

## Lindblad Master Equation for T1 Noise

T1 relaxation (amplitude damping) was modeled using the Lindblad master equation:

dρ/dt = γ [ σ₋ ρ σ₊ − 1/2 { σ₊ σ₋ , ρ } ]
dρ/dt​=γ(LρL†−21​{L†L,ρ})

Where:
- `γ` is the relaxation rate
- `σ₊` and `σ₋` are the raising and lowering operators
- or in the second version
- `L`

This equation describes irreversible decay from an excited state to the ground
state.

---

## Targeting a Specific Qubit

Because the Deutsch–Jozsa implementation uses a two-qubit system, noise needed to
be applied to **only one qubit**.

To accomplish this, modified ladder operators were constructed using tensor
products:

σ₋(2) = I ⊗ σ₋
σ₊(2) = I ⊗ σ₊

This ensures that relaxation occurs only on the second qubit while leaving the
first qubit unaffected.

---

## Timing of Noise Injection

T1 noise was injected **after the final Hadamard gate** in the algorithm.

This choice is physically motivated:
- Prior to the final Hadamard, no excited state exists to relax
- Injecting noise earlier would have no observable effect
- Injecting noise later isolates the effect of relaxation on the algorithm’s
  final measurement outcome

Noise was applied iteratively to represent different relaxation durations.

---

## Numerical Integration Strategy

The Lindblad equation was applied iteratively in discrete time steps using a
loop-based update of the density matrix.

Each iteration corresponds to a small time increment `Δt`, allowing the total
relaxation time to be controlled precisely.

This approach provides:
- Clear separation between gate dynamics and noise dynamics
- Direct control over relaxation duration
- Transparency in numerical behavior

---

## Normalization and Physical Validity

During early testing, non-physical probabilities (values greater than 1 or less
than 0) were observed.

This issue arose because non-unitary evolution can cause the trace of the density
matrix to drift.

To restore physical validity, the density matrix was renormalized after noise
injection using:

ρ → ρ / Tr(ρ)

This ensures:
- Probabilities remain valid
- The density matrix remains trace-normalized
- The system retains physical meaning throughout the experiment

---

## Experimental Trials

Five trials were conducted:

- Trial 1: Ideal, noise-free execution
- Trials 2–5: Increasing T1 relaxation durations

As relaxation time increased, the excited |01⟩ state decayed toward the ground
state, visually demonstrating the effects of T1 noise on algorithmic output.

---

## Key Insight

The need for explicit renormalization highlights an important principle:
noise modeling is not merely an implementation detail, but a core part of
physically accurate simulation.

This realization motivated further investigation into **quantum error
correction**, where noise can be detected and mitigated without destroying
computational states.

---

## Supporting Handwritten Derivations

Handwritten calculations used to derive and verify the Lindblad T1 noise model
are provided in:

- Lindblad master equation setup  
- Modified σ₊ and σ₋ operators  
- Density-matrix normalization  

See: `math/scans/`

---

## Note on σ⁺ / σ⁻ Convention

It is worth noting that the naming of ladder operators σ⁺ and σ⁻ is not
universal across the literature.

In some quantum mechanics texts,
σ⁺ is defined as the lowering operator and σ⁻ as the raising operator. In other
references, the opposite convention is used.

In this project, the operator labeled σ⁺ acts as a lowering operator on the
target qubit, mapping the excited state to the ground state. The physical action
of the operator, not its label, determines the T1 relaxation behavior.

---

## Summary

By modeling T1 noise using the Lindblad master equation and applying it directly
to the density matrix, this project provides a transparent and physically
grounded view of how relaxation degrades quantum algorithm performance.

This approach avoids black-box abstractions and exposes the underlying dynamics
that govern real quantum systems.