'''
Session 02: Implementation of gaussian pulse in a dielectric slab
Simulation: Gaussian pulse incident on a dielectric slab (n=1.5) in 1D
Author: K. S. Harshavardan
'''

import meep as mp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#------------------------------------
#  Defining Simulation Parameters
#------------------------------------

resolution=32
cell_size=mp.Vector3(20,0,0)

#----------------------
#   Defining Geometry
#----------------------

slab_thickness = 4.0
slab_epsilon = 2.25

geometry = [
    mp.Block(
        size=mp.Vector3(slab_thickness,mp.inf,mp.inf),
        center=mp.Vector3(0,0,0),
        material=mp.Medium(epsilon=slab_epsilon)
    )
]

#-------------------
# Defining Source
#-------------------

fc = 1.0
fwidth = 0.5

sources = [
    mp.Source(
        src=mp.GaussianSource(frequency=fc, fwidth=fwidth),
        component=mp.Ez,
        center=mp.Vector3(-7, 0, 0)
    )
]

# ─────────────────────────────────────────────
# SECTION 4: BOUNDARY CONDITIONS
# ─────────────────────────────────────────────

pml_layers = [mp.PML(thickness=1.0)]    # Absorbing boundaries on both ends

# ─────────────────────────────────────────────
# SECTION 5: BUILD SIMULATION OBJECT
# ─────────────────────────────────────────────

sim = mp.Simulation(
    cell_size=cell_size,
    boundary_layers=pml_layers,
    sources=sources,
    geometry=geometry,          # This is new compared to Session 1
    resolution=resolution
)

# ─────────────────────────────────────────────
# SECTION 6: DETECTORS
# ─────────────────────────────────────────────

# Two detectors this time:
# 1. Reflection detector — placed BETWEEN source and slab
#    It will record both the incident pulse (going right) AND
#    the reflected pulse (coming back left) superimposed.
#    The reflected pulse arrives AFTER the incident pulse,
#    so they are separated in time and clearly distinguishable.

# 2. Transmission detector — placed AFTER the slab
#    Records only the transmitted pulse.
#    Compare its arrival time to Session 1 to see the slab-induced delay.

reflection_detector = mp.Vector3(-6, 0, 0)     # x = -6, left of slab
transmission_detector = mp.Vector3(6, 0, 0)    # x = +6, right of slab

reflection_data = []
transmission_data = []

def record_reflection(sim):
    ez = sim.get_field_point(mp.Ez, reflection_detector)
    reflection_data.append((sim.meep_time(), ez))

def record_transmission(sim):
    ez = sim.get_field_point(mp.Ez, transmission_detector)
    transmission_data.append((sim.meep_time(), ez))

# ─────────────────────────────────────────────
# SECTION 7: RUN THE SIMULATION
# ─────────────────────────────────────────────

print("\nStarting Simulation...")

sim.run(
    mp.at_every(0.1, record_reflection),
    mp.at_every(0.1, record_transmission),
    until=60
)

print("Simulation Complete.")

# ─────────────────────────────────────────────
# SECTION 8: EXTRACT DATA
# ─────────────────────────────────────────────

refl_times = np.array([t for t, _ in reflection_data])
refl_ez    = np.real(np.array([e for _, e in reflection_data]))

tran_times = np.array([t for t, _ in transmission_data])
tran_ez    = np.real(np.array([e for _, e in transmission_data]))

# ─────────────────────────────────────────────
# SECTION 9: PLOT RESULTS
# ─────────────────────────────────────────────

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# --- Top plot: Reflection detector ---
ax1.plot(refl_times, refl_ez, color='steelblue', linewidth=1.2)
ax1.axhline(0, color='gray', linewidth=0.8, linestyle='--')
ax1.set_xlabel("Time (MEEP units)", fontsize=12)
ax1.set_ylabel("Ez amplitude", fontsize=12)
ax1.set_title("Reflection Detector (x = −6)\nIncident pulse + reflected pulse", fontsize=13)
ax1.grid(True, alpha=0.3)

# --- Bottom plot: Transmission detector ---
ax2.plot(tran_times, tran_ez, color='darkorange', linewidth=1.2)
ax2.axhline(0, color='gray', linewidth=0.8, linestyle='--')
ax2.set_xlabel("Time (MEEP units)", fontsize=12)
ax2.set_ylabel("Ez amplitude", fontsize=12)
ax2.set_title("Transmission Detector (x = +6)\nTransmitted pulse — delayed by optical path through slab", fontsize=13)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/session02_output.png", dpi=300)
print("Plot saved as outputs/session02_output.png")