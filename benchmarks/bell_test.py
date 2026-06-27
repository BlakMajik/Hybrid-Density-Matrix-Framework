import sys
import os
import numpy as np

# Ensure the core module can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.hdm_observer import HDMObserver

from qiskit import QuantumCircuit
from qiskit.quantum_info import DensityMatrix, BellState
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit_aer import AerSimulator

def run_bell_benchmark():
    print("--- HDM Framework: Bell State Benchmark ---")
    
    # Define the ideal target state
    target_state = BellState.phi_plus()
    observer = HDMObserver(num_qubits=2, target_state=target_state)
    
    # Build the Bell State circuit
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    
    # Simulate a noisy NISQ environment
    noise_model = NoiseModel()
    error_rate = 0.10  # 10% depolarizing noise
    dep_error = depolarizing_error(error_rate, 1)
    noise_model.add_all_qubit_quantum_error(dep_error, ['h', 'cx'])
    
    # Create simulator with density matrix output
    simulator = AerSimulator(noise_model=noise_model, method='density_matrix')
    qc.save_density_matrix()
    
    # Run the circuit
    result = simulator.run(qc).result()
    observed_state = result.data()['density_matrix']
    
    # Estimate hardware gate errors for the survival calculation
    # In a real scenario, this comes from Randomized Benchmarking
    estimated_gate_errors = [error_rate, error_rate]
    # Evaluate using HDMF
    metrics = observer.evaluate_state(observed_state, estimated_gate_errors)
    
    print(f"State Fidelity (F):                  {metrics['fidelity']:.4f}")
    print(f"Fidelity-Residual Purity (Gamma_P):  {metrics['gamma_perp']:.4f}")
    print(f"Hardware Survival (S):               {metrics['survival']:.4f}")
    print(f"---")
    print(f"HDM Operational Trust Score:         {metrics['R_HDM']:.4f}")
    
    if metrics['fidelity'] > 0.90 and metrics['R_HDM'] < 0.60:
        print("\nWARNING: State is inside the Hidden Reliability Region!")

if __name__ == "__main__":
    run_bell_benchmark()

