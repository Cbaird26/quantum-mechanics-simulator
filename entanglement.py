import numpy as np
from qutip import basis, tensor

def simulate_entanglement():
    psi1 = basis(2, 0)  # |0>
    psi2 = basis(2, 1)  # |1>
    entangled_state = (tensor(psi1, psi1) + tensor(psi2, psi2)).unit()
    return entangled_state
