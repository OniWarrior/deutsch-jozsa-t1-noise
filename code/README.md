# Running the Experiment

This directory contains the reference implementation of the Deutsch–Jozsa
algorithm with manually constructed Hamiltonian-based gates and Lindblad-modeled
T1 relaxation noise.

The code reproduces the numerical behavior and results described in the paper
and presentation included in the root of this repository.

---

## Setup

Create and activate a virtual environment (recommended):

```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

```


## Install Dependencies
pip install -r requirements.txt

## Running the Experiment

- cd into code/src
- python src/run_experiment.py

This executes the Deutsch–Jozsa algorithm using a two-qubit density-matrix
representation and produces a probability distribution over the computational
basis states.

---

## Experiment Parameters

Inside run_experiment.py, the following parameters control the experiment:

# Oracle type
- balanced = False   # Constant function
- balanced = True    # Balanced function

# T1 Relaxation Time

- total_time = 0.0   # Ideal, noise-free trial
- total_time = 1.0   # Trial with 1 second of T1 noise
- total_time = 2.0
- total_time = 3.0
- total_time = 4.0


## Outputs

# Plots
- Bar plots of measurement probabilities for the basis states:
  |00>, |01>, |10>, |11>

- Plots are displayed on screen and may be saved to results/plots/

---

## Notes on Implementation
- All quantum gates are realized using explicit Hamiltonians and unitary time
evolution.

- No circuit abstractions or built-in noise models are used.

- T1 relaxation is modeled using the Lindblad master equation.

- The density matrix is explicitly renormalized to maintain physical validity.

For mathematical details, see:

- math/gate_hamiltonians.md

- math/lindblad_derivation.md

---

## Reproduce Specific Trials
- Set balanced appropriately

- Set total_time to the desired relaxation duration

- Run the script

- Inspect the resulting plot and raw data


---

## Summary

This code is intended as a reference implementation demonstrating how
Hamiltonian-level modeling and Lindblad dynamics affect the Deutsch–Jozsa
algorithm under T1 noise.

It prioritizes physical transparency and reproducibility over performance or
framework abstraction.
