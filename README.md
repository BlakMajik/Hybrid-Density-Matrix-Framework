# The Hybrid Density Matrix Framework (HDMF)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework: Qiskit](https://img.shields.io/badge/Framework-Qiskit-blueviolet.svg)](https://qiskit.org/)
[![Status: Academic Preprint](https://img.shields.io/badge/Status-Academic_Preprint-blue.svg)](#references)

A structured diagnostic architecture that augments conventional density matrix representations with layered metadata (Noise, Uncertainty, Context, and History) to systematically evaluate **operational reliability** in Noisy Intermediate-Scale Quantum (NISQ) systems[span_1](start_span)[span_1](end_span).

---

## 💡 The Core Insight: The "Screenshot Problem"

In modern quantum information processing, state quality is traditionally measured via **Fidelity ($F$)**—essentially asking, *"How close is the final quantum state to our ideal target?"*[span_2](start_span)[span_2](end_span) 

However, looking at fidelity alone is like judging a complex, intensive video game by a single paused screenshot. The image might look flawless (high fidelity), but it entirely hides the fact that the console is overheating, the memory is corrupting, and the system is seconds away from a catastrophic crash. 

As circuits grow deeper, a quantum state can maintain geometric proximity to its target while the underlying hardware pathways entirely degrade[span_3](start_span)[span_3](end_span). This framework exposes the **Hidden Reliability Region**: a parametric space where states look $\sim95\%$ successful under conventional fidelity metrics, yet possess critically low ($\sim50\%$) operational trustworthiness[span_4](start_span)[span_4](end_span).

---

## 🛠️ The Integration Architecture

The HDMF does not replace quantum mechanics, standard density matrices ($\rho$), or established benchmarking tools[span_5](start_span)[span_5](end_span). Instead, it acts as a **unified diagnostic dashboard**, formalizing a multi-layered trust envelope[span_6](start_span)[span_6](end_span):

$$\mathcal{H}_{\rho} = (\rho, N, U, C, M)$$

*   **$\rho$ (State Layer):** The conventional density matrix preserving physical observables[span_7](start_span)[span_7](end_span).
*   **$N$ (Noise Descriptor Layer):** Known or inferred noise channels (e.g., Amplitude Damping, Dephasing)[span_8](start_span)[span_8](end_span).
*   **$U$ (Uncertainty Layer):** Local covariance structures or Bayesian posterior distributions[span_9](start_span)[span_9](end_span).
*   **$C$ (Context Layer):** Classical hardware data (calibration timestamps, topologies, drift)[span_10](start_span)[span_10](end_span).
*   **$M$ (Measurement/Mitigation Layer):** Historical telemetry and error suppression history[span_11](start_span)[span_11](end_span).

### The Multiplicative Trust Score ($\mathcal{R}_{HDM}$)

To map these intersecting layers into an actionable engineering metric, the framework implements a deliberate **weakest-link principle**[span_12](start_span)[span_12](end_span):

$$\mathcal{R}_{HDM} = F \cdot \mathrm{Tr}(\rho^2) \cdot \prod_{i}(1-e_i)$$

Where **F** is Fidelity (State Accuracy), $\mathrm{Tr}(\rho^2)$ is Purity (Structural Integrity), and $\prod(1-e_i)$ is the Hardware Survival Probability ($S$) mapped from randomized benchmarking error rates ($e_i$)[span_13](start_span)[span_13](end_span). If any single pillar breaks down, overall confidence drops proportionally[span_14](start_span)[span_14](end_span).

---

## 📊 Key Simulation Findings

As detailed in the companion paper, extensive classical simulation runs utilizing **Qiskit** yielded striking results[span_15](start_span)[span_15](end_span):

1.  **Exposing the Mirage (Test 2):** Out of 10,000 baseline simulation runs, the framework successfully identified **190 distinct cases** locked inside the Hidden Reliability Region ($F > 0.90$ alongside $\mathcal{R}_{HDM} < 0.60$)[span_16](start_span)[span_16](end_span).
2.  **Predicting the Future (Test 3):** When predicting whether a quantum state would survive subsequent deep-circuit operations, standard checkpoint fidelity showed zero predictive power ($r \approx 0$)[span_17](start_span)[span_17](end_span). Conversely, the $\mathcal{R}_{HDM}$ score predicted downstream survival with a remarkably strong linear correlation of **$r = 0.9717$**[span_18](start_span)[span_18](end_span).

---

## 🚀 Getting Started

### Prerequisites

The codebase is engineered to run seamlessly within modern Python and **Qiskit** ecosystems[span_19](start_span)[span_19](end_span).

```bash
pip install qiskit numpy scipy matplotlib
