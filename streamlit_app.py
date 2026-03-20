import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(page_title="Electrical Virtual Lab", layout="centered")

# Title
st.title("⚡ Electrical Engineering Virtual Lab")
st.subheader("Induction Motor: Torque–Slip Characteristics")

# Description
st.write("Change parameters and observe how torque varies with slip.")

# Sidebar inputs
st.sidebar.header("Input Parameters")

V = st.sidebar.slider("Supply Voltage (V)", 100, 500, 230)
R2 = st.sidebar.slider("Rotor Resistance R2 (Ohm)", 0.1, 2.0, 0.5)
X2 = st.sidebar.slider("Rotor Reactance X2 (Ohm)", 0.1, 5.0, 1.5)

# Slip range
s = np.linspace(0.01, 1, 200)

# Torque calculation
T = (s * V**2 * R2) / ((R2/s)**2 + X2**2)

# Plot
fig, ax = plt.subplots()
ax.plot(s, T)
ax.set_xlabel("Slip")
ax.set_ylabel("Torque")
ax.set_title("Torque vs Slip Curve")
ax.grid()

st.pyplot(fig)

# Results
st.write("### 📊 Observations")
st.write("- Torque increases with slip initially.")
st.write("- Maximum torque occurs at a particular slip.")
st.write("- Increasing rotor resistance shifts peak torque.")

# Viva Section
st.write("### ❓ Viva Questions")
st.write("1. What is slip?")
st.write("2. Condition for maximum torque?")
st.write("3. Effect of rotor resistance?")

# Download option (basic)
if st.button("Download Data"):
    data = np.column_stack((s, T))
    np.savetxt("torque_slip.csv", data, delimiter=",", header="Slip,Torque", comments='')
    st.success("Data saved as torque_slip.csv")
