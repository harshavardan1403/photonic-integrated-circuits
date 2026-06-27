'''
Session 01: Implementation of guassian pulse in free space
SImulation: Guassian Pulse propagation in a 1D free space
Author: K. S. Harshavardan
'''
#importing neccessary libraries
import meep as mp
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# configuring libraries
matplotlib.use('Agg') #Non-interactive backend - required for WSL

'''
Any MEEP script follows the same structure.
1. Define your simulation parameters
2. Define your Source
3. Define Boundary Conditions
4. Build the simulation Object
5. Define your detector
6. Run the simulation
'''

#-------------------------------------
#   1. Defining Simulation Parameters
#-------------------------------------
'''
For any MEEP simulation, two parameters are of utmost importance.
1. Resolution: Number of pixels per unit length
2. Cell Size: The size of our simulation domain 
'''

# Defining resolution
'''
The unit length is arbitrary in MEEP, i.e, we define what 1 unit is.
By default it is in micro meters.
Higher the resolution, clearer the output, but slower the process.
'''
resolution=2

# Defining Cell Size
'''
The MEEP method Vector3(x,y,z) takes three parameters for each of the principle axices.
Since we are performing 1D simulation, only x exists.
'''
cell_size=mp.Vector3(16,0,0)    # 16 units long in x direction, 0 in y and z directions

#---------------------------
#  2.  Defining the Source
#---------------------------
'''
Defining a guassian source involves definiting its center frequency and bandwidth.
Frequency in MEEP is a distance dependant quantity.
1 unit of frequency = c/distance_unit
In this case,
    frequency,1 = c/1um = 300 THz

We are operating in infrared region.
'''
fc = 1.0
fwidth = 0.5

sources=[
    mp.Source(                  # creating source object
        mp.GaussianSource(      # A Guassian Pulse Source
            frequency = fc,     # Center Frequency
            fwidth = fwidth     # Bandwidth of the pulse
        ),
    
    component = mp.Ez,          # Exciting the Ez component

    center = mp.Vector3(-5,0,0) # Placing the source at (-5, 0, 0)
    )
]

#-----------------------------------
#   3. Defining Boundary Condition
#-----------------------------------
'''
Define the Characteristics of the boundaries of the defined cell.
PML = Perfectly Matched Layer
PML is an absorbing boundary, meaning, No reflection or reraction. 
'''
pml_layers=[mp.PML(thickness=1.0)]

#---------------------------------------
#   4. Building the Simulation Object
#---------------------------------------

sim = mp.Simulation(
    cell_size=cell_size,
    boundary_layers=pml_layers,
    sources=sources,
    resolution=resolution
)

#--------------------------------
#   5. Setting up the detector
#--------------------------------
'''
Detectors are places to monitor a certain field component through the simulation time.
'''
#   Defining detector'sposition
detector_position = mp.Vector3(5,0,0)

# Defining an array to store monitored value
time_series = []

# Function to store data inside the array
def record_field_component(sim):
    ez_value = sim.get_field_point(mp.Ez, detector_position)
    time_series.append((sim.meep_time(),ez_value))

#-------------------------------
#   6. Running the Simulation
#-------------------------------

print("\nStarting Simulation")

sim.run(
    mp.at_every(0.1, record_field_component),
    until=40
)

print("Simulation Completed")

#-------------------------------
#   7. Visualising the result
#-------------------------------

# Unpacking field component and time
times=np.array([t for t,_ in time_series])
ez_values=np.array([ez for _,ez in time_series])

# Plot electric field component Ez
plt.figure(figsize=(10,5))
plt.plot(times,
         ez_values.real,
         color='steelblue',
         linewidth=1.5
         )

# Plot formatting
plt.xlabel("Time (MEEP units)", fontsize=13)
plt.ylabel("Ez field amplitude", fontsize=13)
plt.title("Session 1: Gaussian Pulse in Free Space\nEz field recorded at x = +5", fontsize=14)
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')  # Zero reference line
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save to file (since we're on WSL, saving is more reliable than plt.show())
plt.savefig("session01_output_r2.png", dpi=300)
print("Plot saved as session1_output.png")
print("Open it in VS Code's file explorer or use: explorer.exe session1_output.png")