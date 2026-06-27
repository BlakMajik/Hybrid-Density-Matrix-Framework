import numpy as np
from qiskit.quantum_info import state_fidelity, DensityMatrix

class HDMObserver:
    """
    The Hybrid Density Matrix Framework (HDMF) Observer.
    Calculates operational trustworthiness using the decoupled metric:
    R_HDM = Fidelity * Fidelity-Residual Purity * Hardware Survival.
    """
    def __init__(self, num_qubits, target_state):
        self.num_qubits = num_qubits
        self.target_state = target_state

    def calculate_purity(self, observed_state):
        """Calculates the raw purity Tr(rho^2) of the observed state."""
        rho = DensityMatrix(observed_state)
        return np.real(np.trace(np.dot(rho.data, rho.data)))

    def calculate_fidelity_residual_purity(self, purity, fidelity):
        """
        Calculates Fidelity-Residual Purity (Gamma_perp).
        Uses the depolarizing relation expected purity = 2*F^2 - 1.
        """
        expected_purity = 2 * (fidelity ** 2) - 1
        
        # Prevent division by zero or negative bounds in extreme noise
        if expected_purity <= 0:
            return 0.0
            
        gamma_perp = purity / expected_purity
        return min(gamma_perp, 1.0) # Clipped to [0, 1] boundary condition

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
        Generates the full HDM diagnostic tuple and decoupled R_HDM score.
        """
        # 1. State Accuracy (Fidelity)
        fidelity = state_fidelity(self.target_state, observed_state)
        
        # 2. Structural Integrity (Fidelity-Residual Purity)
        raw_purity = self.calculate_purity(observed_state)
        gamma_perp = self.calculate_fidelity_residual_purity(raw_purity, fidelity)
        
        # 3. Hardware Viability (Survival Probability)
        survival = self.calculate_survival(gate_error_rates)
        
        # 4. Decoupled Multiplicative Trust Score (R_HDM)
        r_hdm = fidelity * gamma_perp * survival
        
        return {
            'fidelity': fidelity,
            'raw_purity': raw_purity,
            'gamma_perp': gamma_perp,
            'survival': survival,
            'R_HDM': r_hdm
        }
