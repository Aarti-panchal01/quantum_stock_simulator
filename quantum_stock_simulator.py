
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.title("📈 Quantum-Inspired Stock Market Simulator (Classic Version)")

# Simulation parameters
num_days = st.slider("Number of Days to Simulate", 10, 200, 100)
initial_price = st.number_input("Initial Stock Price", value=100.0)
volatility = st.slider("Market Volatility", 0.0, 1.0, 0.2)

# Run simulation
prices = [initial_price]
for _ in range(num_days):
    change_percent = random.uniform(-volatility, volatility)
    new_price = prices[-1] * (1 + change_percent)
    prices.append(new_price)

# Display results
st.subheader("📊 Simulated Stock Price Over Time")
fig, ax = plt.subplots()
ax.plot(prices, label="Stock Price")
ax.set_xlabel("Day")
ax.set_ylabel("Price")
ax.grid(True)
st.pyplot(fig)

