import streamlit as st
import numpy as np
from unified_interactions import visualize_interactions

st.title("Unified Particle Interactions Simulator")

# Particle properties
particle1 = {'position': np.array([0, 0, 0]), 'mass': st.slider('Particle 1 Mass', 0.1, 10.0, 1.0),
             'charge': st.slider('Particle 1 Charge', -1.0, 1.0, 0.0)}
particle2 = {'position': np.array([1, 0, 0]), 'mass': st.slider('Particle 2 Mass', 0.1, 10.0, 1.0),
             'charge': st.slider('Particle 2 Charge', -1.0, 1.0, 0.0)}

# Force constants
force_constants = {
    'gravitational': st.slider('Gravitational Constant', 1e-10, 1e-8, 6.67430e-11),
    'electromagnetic': st.slider('Electromagnetic Constant', 1e-2, 1e0, 8.9875517923e9),
    'strong': st.slider('Strong Force Constant', 1e-1, 1e1, 1.0),
    'weak': st.slider('Weak Force Constant', 1e-5, 1e-3, 1.0)
}

# Visualize
fig = visualize_interactions(particle1, particle2, force_constants)
st.pyplot(fig)
