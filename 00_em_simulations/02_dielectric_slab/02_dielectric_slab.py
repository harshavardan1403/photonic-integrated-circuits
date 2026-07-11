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
        mp.GaussianSource(
            frequency = fc,
            fwidth = fwidth
        ),
        component = mp.Ez,
        center = mp.Vector3(-7, 0, 0)
    )
]

#--------------------------------
#   Defining Boundary Condition
#--------------------------------
pml_layers=[mp.PML(thickness = 1.0)]

#-------------------------------
#   Defining Simulation Object
#-------------------------------

sim = mp.Simulation(
    cell_size = cell_size,
    boundary_layers = pml_layers,
    sources = sources,
    geometry = geometry,
    resolution = resolution
)

#------------------------
#   Defining Detectors
#------------------------

reflection_detector = mp.Vector3(-6,0,0)
transmission_detector = mp.Vector3(6,0,0)

reflection_data = []
transmission_data = []

def record_reflection(sim):
    ez = sim.get_field_point(mp.Ez, reflection_detector)
    reflection_data.append( (sim.meep_time(),ez) )

def record_transmission(sim):
    ez=sim.get_field_point(mp.Ez,transmission_detector)
    transmission_data.append( (sim.meep_time(), ez) )

#------------------------
#   Run the Simulation
#------------------------

print("\n Starting the Simulation")

sim.run(
    mp.at_every(0.1,record_reflection),
    mp.at_every(0.1,record_transmission),
    until = 60
)

print("\nSimulation Completed")

#---------------------
#   Extracting Data
#---------------------

refl_time = np.array([t for t,_ in reflection_data])
refl_ez = np.real(np.array([ez for _,ez in reflection_data]))

trans_time = np.array([t for t,_ in transmission_data])
trans_ez = np.real(np.array([ez for _,ez in transmission_data]))

#----------------------
#   Plotting Results
#----------------------

fig, (ax1,ax2) = plt.subplots(2,1,figsize=(12,8))

#--------------Reflection Plot------------------#
ax1.plot(refl_time, refl_ez, color="steelblue", linewidth=1.2)
ax1.axhline(0, color="gray", linewidth=0.8, linestyle='--')
ax1.set_xlabel('Time (MEEP units)', fontsize=12)
ax1.set_ylabel('Ez Amplitude', fontsize=12)
ax1.set_title('Reflection Detector',fontsize=13)
ax1.grid(True, alpha=0.3)

#--------------Transmission Plot------------------#
ax2.plot(trans_time, trans_ez, color="darkorange", linewidth=1.2)
ax2.axhline(0, color="gray", linewidth=0.8, linestyle='--')
ax2.set_xlabel('Time (MEEP units)', fontsize=12)
ax2.set_ylabel('Ez Amplitude', fontsize=12)
ax2.set_title('Transmission Detector', fontsize=13)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("s02_op_Si.png", dpi=300)
print("\nOutput Plot Saved to Outputs directory")