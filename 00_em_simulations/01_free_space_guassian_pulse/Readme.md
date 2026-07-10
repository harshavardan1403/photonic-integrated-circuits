
# Session 1: Gaussian Pulse in Free Space  
**Folder:** `00_em_simulations/01_free_space_gaussian_pulse/`  
**Simulator:** MEEP FDTD

---
## What This Simulation is About
A Gaussian pulse of light is sent through a 1D vacuum domain and recorded at a detector point inside the domain. This is a beginner friendly MEEP EM simulation to understand the structure of a MEEP script.

#### Why a Gaussian Pulse?
A gaussian pulse has a defined center frequency and a finite bandwidth. It helps in analyzing the response of a system to given spectrum.  

--- 
## Output
![Output Image](outputs/session01_output.png)

The plot shows Ez field as a function of simulation time. The bell shaped envelope is the gaussian pulse measured at a detector position (x=+5). The oscillations within the envelope represent the electric field cycles at 300 THz.

---
## MEEP Script Structure  
Any MEEP script follows the same structure.
1. Define your `simulation parameters`
2. Define your `Source`
3. Define `Boundary Conditions`
4. Build the `simulation Object`
5. Define your `detector` and `detection function`
6. Run the simulation

---
## Script Explanation
### Import necessary libraries
```
import meep as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
```

Configuring matplotlib with non-interactive backend to work efficiently with WSL.


### Defining Simulation Parameters

For any MEEP simulation, two parameters are of utmost importance.
1. Resolution: Number of pixels per unit length
2. Cell Size: The size of our simulation domain 
```
resolution=16
cell_size=mp.Vector3(16,0,0)
```
The unit length is arbitrary in MEEP, i.e, we define what 1 unit is. By default it is in **micro meters**. The MEEP method Vector3(x,y,z) takes three parameters for each of the principle axises. Since we are performing 1D simulation, only x has a non-zero value.  We defined the 1D cell with length along x=16. Hence, the cell spans from (-8,0,0) to (8,0,0).

Resolution controls the fitness of spatial grid. The rule of thumb is:
```
resolution >= 8 x center_frequency      (minimum)
resolution = 16 x center_frequency      (standard)
``` 
`Note:` Below 8 pixel per wavelength, the program itself distorts the wave which does not hold any physical meaning.

### Defining the Source

Defining a gaussian source involves defining its center frequency and bandwidth.  

```
fc = 1.0
fwidth = 0.5

sources=[
    mp.Source(                  # Creating Source Object
        mp.GaussianSource(      # Defining the Source Type
            frequency = fc,     
            fwidth = fwidth     
        ),
    
    component = mp.Ez,          # Defining the field component ot be excited

    center = mp.Vector3(-5,0,0) # Defining the position of the source
    )
]
```

Multiple sources can be used for a single simulation. Hence, MEEP's inbuilt simulation method takes a *list of sources*.  

To define a source, the `Source` method in MEEP is used.  
The `mp.Source` method takes three parameters:
- *source_type*: The function that defines the behavior of the source pulse.
- *field_component*: The field component of the E or F field to be excited as per source_type.
- *source_position*: Position of source inside the simulation cell.

`Note:` Frequency in MEEP is expressed as `c/distance_unit`. With 1 unit = 1 µm,  frequency 1.0 = c/1µm = 300 THz. In this case, we are operating in *infra red* region. 

### Defining Boundary Condition

Define the Characteristics of the boundaries of the defined cell.  
PML (Perfectly Matched Layer) is an absorbing boundary, meaning, No reflection or refraction. Without PML, the electromagnetic waves will be reflected by the boundaries causing interference and other higher order effects. 

```
pml_layers=[mp.PML(thickness=1.0)]
```

### Building the Simulation Object

```
sim = mp.Simulation(
    cell_size=cell_size,
    boundary_layers=pml_layers,
    sources=sources,
    resolution=resolution
)
```
No `geometry` argument is passed here. An empty simulation domain defaults to vacuum.

### Setting up the detector and detection function

Detectors are places to monitor a certain field component through the simulation time.  
Defining detector's position
```
detector_position = mp.Vector3(5,0,0)
```

Defining an array to store monitored value

```
time_series = []
```

Function to store data inside the array
```
def record_field_component(sim):
    ez_value = sim.get_field_point(mp.Ez, detector_position)
    time_series.append((sim.meep_time(),ez_value))
```
For a 1D cell with x dimension, Ez is the naturally existing field component. 

 ###   Running the Simulation

To run the simulation, we use the `run()` method and call the `at_every()` method to record the field component as per our detector function.

```
print("\nStarting Simulation")

sim.run(
    mp.at_every(0.1, record_field_component),
    until=40
)

print("Simulation Completed")
```

### Visualizing the result


Unpacking field component and time stamp
```
times=np.array([t for t,_ in time_series])
ez_values=np.array([ez for _,ez in time_series])
```
Plot electric field component Ez
```
plt.figure(figsize=(10,5))
plt.plot(times,
         ez_values.real,
         color='steelblue',
         linewidth=1.5
         )
```
Plot formatting
```
plt.xlabel("Time (MEEP units)", fontsize=13)
plt.ylabel("Ez field amplitude", fontsize=13)
plt.title("Session 1: Gaussian Pulse in Free Space\nEz field recorded at x = +5", fontsize=14)
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')  # Zero reference line
plt.grid(True, alpha=0.3)
plt.tight_layout()
```
Save to file (since we're on WSL, saving is more reliable than plt.show())
```
plt.savefig("session01_output_r2.png", dpi=300)
print("Plot saved as session1_output.png")
print("Open it in VS Code's file explorer or use: explorer.exe session1_output.png")
```

---
## Observations
#### Bandwidth
The time response for increase or decrease in `fwidth` is governed by the *Time-Bandwidth Product*.  
- When the bandwidth is increased, the time response narrowed. This can be seen in [session01_output_n.png](outputs/session01_output_n.png). This output was observed for a `fwidth = 1.0`.
- When the bandwidth is decreased, the time response widens. This can be seen in [session01_output_w.png](outputs/session01_output_w.png) and [session01_output_w1.png](outputs/session01_output_w1.png). This output was observed for `fwidth = 0.1`.

#### Source/Detector Position
When the position of source/detector is moved closer or away from the detector/source, the pulse advances or delays respectively. This can be seen in [session01_output_d1.png](outputs/session01_output_d1.png). This output was observed for detector position (2,0,0).

#### Sampling Time
When the sampling time in `mp.at_every()` method in reduced, the output becomes smoother in time. This can be seen in [session01_output_s.png](outputs/session01_output_s.png)

#### Resolution
At `resolution = 2`, the pulse arrives late and appears distorted. This is **Numerical dispersion** and does not hold any physical meaning.

---
## Key Parameters
| Parameter | Value | Physical Meaning |
| ------- | ------- | ------- |
| `resolution` | 16 | 16 grid points per µm |
| `cell_size` | (16,0,0) | 16 µm x 1D domain |
| `fc` | 1.0 | 300 THz, near-infrared |
| `fwidth` | 0.5 | Pulse bandwidth |
| Source position | (-5,0,0) | 3 µm from left PML |
| Detector position | (+5,0,0) | 3 µm from right PML|
| PML thickness | 1.0 | 1 µm absorbing boundary|