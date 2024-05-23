import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from superposition import simulate_superposition
from entanglement import simulate_entanglement
from tunneling import simulate_tunneling

st.title("Quantum Mechanics Simulator")

# Superposition
st.header("Superposition")
alpha = st.slider("Alpha", 0.0, 1.0, 0.5)
alpha, beta = simulate_superposition(alpha)
st.write(f"State: |Ψ⟩ = {alpha:.2f}|0⟩ + {beta:.2f}|1⟩")

# Entanglement
st.header("Entanglement")
entangled_state = simulate_entanglement()
st.write("Entangled State:")
st.write(entangled_state)

# Quantum Tunneling
st.header("Quantum Tunneling")
barrier_height = st.slider("Barrier Height (eV)", 0.0, 10.0, 5.0)
barrier_width = st.slider("Barrier Width (nm)", 0.1, 2.0, 1.0)
particle_energy = st.slider("Particle Energy (eV)", 0.0, 10.0, 1.0)
transmission_coefficient = simulate_tunneling(barrier_height, barrier_width * 1e-9, particle_energy)
st.write(f"Transmission Coefficient: {transmission_coefficient:.2e}")

# Visualization
st.header("Visualization")

# Superposition Visualization
fig, ax = plt.subplots()
states = ['|0⟩', '|1⟩']
probabilities = [alpha**2, beta**2]
ax.bar(states, probabilities, color=['blue', 'orange'])
ax.set_ylabel('Probability')
ax.set_title('Superposition State Probabilities')
st.pyplot(fig)

# Quantum Tunneling Visualization
x = np.linspace(0, barrier_width * 1e-9, 500)
potential = np.where((x > 0) & (x < barrier_width * 1e-9), barrier_height, 0)
fig, ax = plt.subplots()
ax.plot(x * 1e9, potential, label='Potential Barrier')
ax.axhline(particle_energy, color='red', linestyle='--', label='Particle Energy')
ax.set_xlabel('Position (nm)')
ax.set_ylabel('Potential Energy (eV)')
ax.legend()
st.pyplot(fig)
