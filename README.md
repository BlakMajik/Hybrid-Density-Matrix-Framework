# The Hybrid Density Matrix Framework (HDMF)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework: Qiskit](https://img.shields.io/badge/Framework-Qiskit-blueviolet.svg)](https://qiskit.org/)
[![Status: Academic Preprint](https://img.shields.io/badge/Status-Academic_Preprint-blue.svg)](#references)

A structured diagnostic architecture that augments conventional density matrix representations with layered metadata (Noise, Uncertainty, Context, and History) to systematically evaluate **operational reliability** in Noisy Intermediate-Scale Quantum (NISQ) systems.

---

## 💡 The Core Insight: The "Screenshot Problem"

In modern quantum information processing, state quality is traditionally measured via **Fidelity ($F$)**—essentially asking, *"How close is the final quantum state to our ideal target?"* However, looking at fidelity alone is like judging a complex, intensive video game by a single paused screenshot. The image might look flawless (high fidelity), but it entirely hides the fact that the console is overheating, the memory is corrupting, and the system is seconds away from a catastrophic crash. 

As circuits grow deeper, a quantum state can maintain geometric proximity to its target while the underlying hardware pathways entirely degrade. This framework exposes the **Hidden Reliability Region**: a parametric space where states look ~95% successful under conventional fidelity metrics, yet possess critically low (~50%) operational trustworthiness.

---

## 🛠️ The Integration Architecture

The HDMF does not replace quantum mechanics, standard density matrices ($\rho$), or established benchmarking tools. Instead, it acts as a **unified diagnostic dashboard**, formalizing a multi-layered trust envelope:

$$\mathcal{H}_{\rho} = (\rho, N, U, C, M)$$

* **$\rho$ (State Layer):** The conventional density matrix preserving physical observables.
* **$N$ (Noise Descriptor Layer):** Known or inferred noise channels (e.g., Amplitude Damping, Dephasing).
* **$U$ (Uncertainty Layer):** Local covariance structures or Bayesian posterior distributions.
* **$C$ (Context Layer):** Classical hardware data (calibration timestamps, topologies, drift).
* **$M$ (Measurement/Mitigation Layer):** Historical telemetry and error suppression history.

### The Multiplicative Trust Score ($\mathcal{R}_{HDM}$)

To map these intersecting layers into an actionable engineering metric, the framework implements a deliberate **weakest-link principle**:

$$\mathcal{R}_{HDM} = F \cdot \mathrm{Tr}(\rho^2) \cdot \prod_{i}(1-e_i)$$

Where **F** is Fidelity (State Accuracy), $\mathrm{Tr}(\rho^2)$ is Purity (Structural Integrity), and $\prod(1-e_i)$ is the Hardware Survival Probability ($S$) mapped from randomized benchmarking error rates ($e_i$). If any single pillar breaks down, overall confidence drops proportionally.

---

## 📊 Key Simulation Findings

As detailed in the companion paper, extensive classical simulation runs utilizing **Qiskit** yielded striking results:

1.  **Exposing the Mirage (Test 2):** Out of 10,000 baseline simulation runs, the framework successfully identified **190 distinct cases** locked inside the Hidden Reliability Region ($F > 0.90$ alongside $\mathcal{R}_{HDM} < 0.60$).
2.  **Predicting the Future (Test 3):** When predicting whether a quantum state would survive subsequent deep-circuit operations, standard checkpoint fidelity showed zero predictive power ($r \approx 0$). Conversely, the $\mathcal{R}_{HDM}$ score predicted downstream survival with a remarkably strong linear correlation of **$r = 0.9717$**.

---

## 🚀 Getting Started

### Prerequisites

The codebase is engineered to run seamlessly within modern Python and **Qiskit** ecosystems.

```bash
pip install qiskit numpy scipy matplotlib
