import numpy as np

def simulate_tunneling(barrier_height, barrier_width, particle_energy):
    h_bar = 1.0545718e-34  # Planck constant
    m = 9.10938356e-31  # Mass of electron
    k = np.sqrt(2 * m * (barrier_height - particle_energy)) / h_bar
    transmission_coefficient = np.exp(-2 * k * barrier_width)
    return transmission_coefficient
