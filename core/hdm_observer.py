import numpy as np
from qiskit.quantum_info import state_fidelity, DensityMatrix, partial_trace

class HDMObserver:
    """
    The Hybrid Density Matrix Framework (HDMF) Observer.
    Calculates operational trustworthiness of a quantum state based on
    State Accuracy (Fidelity), Structural Integrity (Purity), and Hardware Survival.
    """
    def __init__(self, num_qubits, target_state):
        self.num_qubits = num_qubits
        self.target_state = target_state

    def calculate_purity(self, observed_state):
        """Calculates the purity Tr(rho^2) of the observed state."""
        rho = DensityMatrix(observed_state)
        return np.real(np.trace(np.dot(rho.data, rho.data)))

    def calculate_survival(self, gate_error_rates):
        """
        Calculates the hardware survival probability S = Product(1 - e_i).
        Assumes independent gate failures.
        """
        survival_prob = 1.0
        for error_rate in gate_error_rates:
            survival_prob *= (1.0 - error_rate)
        return survival_prob

    def evaluate_state(self, observed_state, gate_error_rates):
        """
        Generates the full HDM diagnostic tuple and R_HDM score.
        """
        # 1. State Accuracy (Fidelity)
        fidelity = state_fidelity(self.target_state, observed_state)
        
        # 2. Structural Integrity (Purity)
        purity = self.calculate_purity(observed_state)
        
        # 3. Hardware Viability (Survival Probability)
        survival = self.calculate_survival(gate_error_rates)
        
        # 4. Multiplicative Trust Score (R_HDM)
        r_hdm = fidelity * purity * survival
        
        return {
            'fidelity': fidelity,
            'purity': purity,
            'survival': survival,
            'R_HDM': r_hdm
        }
