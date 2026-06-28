# Purpose: Check that MEEP and all required libraries are correctly installed
# This is NOT a simulation yet — just a health check

# Try importing MEEP — if this fails, installation has an issue
import meep as mp

# Try importing numpy — used for numerical arrays in all our simulations
import numpy as np

# Try importing matplotlib — used to visualize our simulation results
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend — important for WSL
import matplotlib.pyplot as plt

# If we reach this line, all imports succeeded
print("MEEP version:", mp.__version__)
print("NumPy version:", np.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("\nAll imports successful. Your environment is ready.")