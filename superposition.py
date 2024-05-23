import numpy as np

def simulate_superposition(alpha):
    beta = np.sqrt(1 - alpha**2)
    return alpha, beta
