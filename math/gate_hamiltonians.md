# Gate Hamiltonians

This document describes how the quantum gates used in this project were
**physically realized using Hamiltonians and unitary time evolution**.

Rather than relying on abstract circuit primitives, all gates were constructed
from first principles to reflect how quantum operations arise from controlled
Hamiltonian dynamics.

---

## Purpose and Scope

The goal of this document is to explain:

- Why Hamiltonian-based gate construction was chosen
- Which Hamiltonians were used
- How unitary time evolution produces the desired gates
- How these constructions map directly to the software implementation

This document focuses only on **gate realization**. Noise modeling is handled
separately in `lindblad_derivation.md`.

---

## Why Hamiltonian-Based Gates?

In most quantum computing demonstrations, gates are treated as ideal,
instantaneous operations. While useful for abstraction, this hides the physical
mechanism by which gates are actually implemented.

In this project, gates were realized using:

- Explicit Hamiltonians
- Finite evolution times
- Physically meaningful rotation angles

This approach allows:
- Precise control over timing
- Clear separation between gate dynamics and noise processes
- Direct compatibility with density-matrix evolution

---

## Unitary Time Evolution

All gates in this project are applied using the unitary time evolution operator:

U(t) = exp(-i H t / ħ)

Where:
- `H` is the Hamiltonian governing the system
- `t` is the evolution time
- `ħ` is the reduced Planck constant

For each gate, the evolution time was chosen to produce a π rotation consistent
with the desired unitary transformation.

---

## Hadamard Gate Realization

### Single-Qubit Hamiltonian

The Hadamard gate was realized using the Hamiltonian:

H = -b (X + Z) / (2√2)

Where:
- `X` and `Z` are Pauli operators
- `b` is a system-dependent constant that represents the product of γ, the gyromagnetic - ratio, ħ, reduced Planck constant, and Bz, the z-component of the magnetic field. 

This Hamiltonian generates a rotation that produces the Hadamard transformation
when evolved for the appropriate time.

### Two-Qubit Extension

Because the Deutsch–Jozsa implementation in this project uses a two-qubit density
matrix, the single-qubit Hamiltonian was extended via tensor products:

H₁₂ = H ⊗ H

This allows the Hadamard gate to be applied simultaneously to both qubits.

### Evolution Time

The evolution time was chosen such that:

t = π ħ / b

At this time, the unitary evolution operator implements the Hadamard gate on both
qubits.

---

## Z Gate Realization

### Single-Qubit Hamiltonian

The Z gate was realized using the Hamiltonian:

H<sub>z</sub> = (b / 2) Z

This Hamiltonian produces a phase flip when evolved for a π rotation.

### Targeting a Single Qubit

To flip only the second qubit, the Hamiltonian was extended as:

H<sub>Z2</sub> = I ⊗ H_Z

Where:
- `I` is the identity operator
- The tensor product ensures that only the second qubit is affected

The same π-rotation time was used to apply the gate.

---

## Implementation Notes

In the software implementation:

- Hamiltonians are constructed explicitly as matrices
- Unitary operators are computed via matrix exponentiation
- Gates are applied through density-matrix evolution:

ρ → U ρ U†

This approach ensures consistency between the mathematical model and the
numerical implementation, and it allows noise processes to be injected
independently of gate dynamics.

---

## Supporting Handwritten Derivations

Original handwritten derivations used during this project are included for
reference and verification:

- Hadamard gate Hamiltonian construction  
- Tensor-product extensions to two qubits  
- Unitary time evolution calculations  

See: `math/scans/`

---

## Summary

This Hamiltonian-based approach to gate construction provides:

- Physical realism
- Clear timing semantics
- Compatibility with Lindblad noise modeling
- A transparent link between theory and implementation

By explicitly modeling gates at the Hamiltonian level, this project avoids
treating quantum operations as black-box abstractions and instead exposes the
underlying dynamics that govern real quantum systems.
