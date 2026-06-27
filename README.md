# The Hybrid Density Matrix Framework (HDMF)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework: Qiskit](https://img.shields.io/badge/Framework-Qiskit-blueviolet.svg)](https://qiskit.org/)
[![Paper: arXiv](https://img.shields.io/badge/Paper-arXiv:XXXX.XXXXX-B31B1B.svg)](https://arxiv.org/) 

A structured diagnostic architecture that augments conventional density matrix representations with layered metadata (Noise, Uncertainty, Context, and History) to systematically evaluate **operational reliability** in Noisy Intermediate-Scale Quantum (NISQ) systems.

---

## 💡 The Core Insight: The "Screenshot Problem"

In modern quantum information processing, state quality is traditionally measured via **Fidelity ($\mathcal{F}$)**—essentially asking, *"How close is the final quantum state to our ideal target?"* However, looking at fidelity alone is like judging a complex, intensive video game by a single paused screenshot. The image might look flawless (high fidelity), but it entirely hides the fact that the console is overheating, the memory is corrupting, and the system is seconds away from a catastrophic crash. 

As circuits grow deeper, a quantum state can maintain geometric proximity to its target while the underlying hardware pathways entirely degrade. This framework exposes the **Hidden Reliability Region**: a parametric space where states look highly successful under conventional fidelity metrics ($\ge 90\%$), yet possess critically low operational trustworthiness.

---

## 🛠️ The Integration Architecture

The HDMF does not replace quantum mechanics, standard density matrices ($\rho$), or established benchmarking tools. Instead, it acts as a **unified diagnostic dashboard**, formalizing a multi-layered trust envelope:

$$\mathcal{H}_{\rho} = (\rho, \mathcal{N}, \mathcal{U}, \mathcal{C}, \mathcal{M})$$

### The Decoupled Multiplicative Trust Score ($R_{HDM}$)

Multiplying raw fidelity and raw purity together creates an *information-overlap problem*: under standard decoherence, both metrics drop, meaning their product unfairly double-penalizes the same underlying degradation. 

To resolve this, the HDMF isolates **Fidelity-Residual Purity ($\gamma_{\perp}$)**—the component of state purity *not* already explained by fidelity loss. The framework implements a decoupled weakest-link principle:

$$R_{HDM} = \mathcal{F} \cdot \gamma_{\perp} \cdot \mathcal{S}$$

* **$\mathcal{F}$ (State Accuracy):** Measured via standard Fidelity.
* **$\gamma_{\perp}$ (Structural Integrity):** Fidelity-Residual Purity. (e.g., $\frac{\mathrm{Tr}(\rho^2)}{2\mathcal{F}^2-1}$ under depolarizing conditions).
* **$\mathcal{S}$ (Hardware Viability):** Hardware Survival Probability mapped from randomized benchmarking error rates.

If any single pillar breaks down, overall confidence drops proportionally.

---

## 📊 Key Simulation Findings

As detailed in the primary manuscript, extensive classical simulation runs utilizing **Qiskit** yielded striking results:

1.  **Exposing the Mirage (Test 2 & 5):** Across 31,000 simulation trials, the framework successfully identified **537 distinct cases** locked inside the Hidden Reliability Region ($\mathcal{F} \ge 0.90$ alongside $R_{HDM} < 0.60$).
2.  **Predicting the Future (Test 3):** When predicting whether a quantum state would survive subsequent deep-circuit operations, standard checkpoint fidelity showed zero predictive power ($r \approx 0$). Conversely, the $R_{HDM}$ score predicted downstream survival with a remarkably strong linear correlation of **$r = 0.9717$**.

---

## 🚀 Getting Started

### Prerequisites & Installation

The codebase is engineered to run seamlessly within modern Python and **Qiskit** ecosystems. Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/BlakMajik/Hybrid-Density-Matrix-Framework.git](https://github.com/BlakMajik/Hybrid-Density-Matrix-Framework.git)
cd Hybrid-Density-Matrix-Framework
pip install -r requirements.txt
