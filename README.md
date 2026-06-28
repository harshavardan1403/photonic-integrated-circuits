# Photonic Integrated Circuits — FDTD Simulation Portfolio

**MIT MEEP simulations of photonic integrated circuit components, built ground-up from electromagnetic fundamentals to WDM signal processing devices.**

[![MEEP](https://img.shields.io/badge/Simulator-MIT%20MEEP-blue)](https://meep.readthedocs.io/)
[![Python](https://img.shields.io/badge/Python-3.9-green)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-WSL2%20Ubuntu-orange)](https://ubuntu.com/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

---

## What This Repository Is

This is a structured, documented portfolio of photonic integrated circuit (PIC) simulations using the MIT MEEP finite-difference time-domain (FDTD) solver. Every simulation is self-contained — a runnable Python script, output visualizations, and a README that explains the physics, the parameters, and what the result means in real-world photonic engineering terms.

The curriculum runs from absolute fundamentals (electromagnetic wave propagation, dielectric interfaces, PML boundary conditions) through to practical PIC components (waveguides, directional couplers, ring resonators, MZI switches) and eventually photonic signal processing architectures relevant to WDM optical communications and neuromorphic photonics.

This repository is designed to be useful to:
- Engineers and students learning photonic simulation from scratch
- Researchers wanting documented MEEP examples with physical interpretation
- Anyone exploring the MIT MEEP Python API for PIC design workflows

---

## Repository Structure

```
photonic-integrated-circuits/
│
├── 00_em_fundamentals/          # FDTD theory · field behavior · wave propagation
├── 01_guided_wave_optics/       # Waveguide modes · dispersion · bend loss
├── 02_passive_devices/          # Couplers · ring resonators · MZI · Bragg gratings
├── 03_active_devices/           # Modulator geometry · photodetector overlap · SOA
├── 04_circuits/                 # Multi-component PIC assemblies · WDM circuits
├── 05_systems/                  # Link budgets · neuromorphic photonics · reservoir computing
├── 06_pdk/                      # Reusable material definitions · geometry primitives
└── 07_utils/                    # Shared plotting · convergence testing · environment check
```

Each numbered folder builds on the one before it. The progression mirrors how photonic integrated circuit design is taught and practiced — you cannot design a ring resonator without understanding guided modes, and you cannot engineer a WDM system without understanding resonator Q-factors and coupling conditions.

---

## Simulations Index

### `00_em_fundamentals` — Electromagnetic Foundations and FDTD Basics

Core electromagnetic wave behavior simulated in MIT MEEP before any photonic structure is introduced. Establishes FDTD intuition, numerical stability, and field monitoring techniques that every later simulation depends on.

| # | Simulation | Physics Demonstrated | Status |
|---|-----------|---------------------|--------|
| 01 | [Free Space Gaussian Pulse](./00_em_fundamentals/01_free_space_gaussian_pulse/) | Time-bandwidth product · PML boundaries · field monitoring · FDTD timestep stability | ✅ Complete |
| 02 | [Dielectric Slab — Transmission and Reflection](./00_em_fundamentals/02_dielectric_slab/) | Fresnel equations · partial reflection · phase velocity · refractive index | 🔄 In Progress |
| 03 | Standing Wave in a 1D Cavity | Resonance condition · nodes and antinodes · boundary-driven interference | ⬜ Planned |
| 04 | Pulse Propagation in a Dispersive Medium | Group velocity vs phase velocity · pulse broadening · material dispersion | ⬜ Planned |
| 05 | Flux Spectrum Analysis | Fourier decomposition in MEEP · transmission spectra · flux monitor workflow | ⬜ Planned |

---

### `01_guided_wave_optics` — Waveguide Theory and Mode Propagation

Light confinement via total internal reflection. Simulated using both MIT MEEP (time-domain field propagation) and MIT MPB (direct mode solving). Understanding mode profiles and cutoff conditions is prerequisite for every device simulation.

| # | Simulation | Physics Demonstrated | Status |
|---|-----------|---------------------|--------|
| 01 | 2D Slab Waveguide — TE Mode (MPB) | Total internal reflection · guided vs radiation modes · transverse mode profile | ⬜ Planned |
| 02 | 2D Slab Waveguide — TM Mode (MPB) | Polarization dependence · cutoff condition · field asymmetry | ⬜ Planned |
| 03 | Single-Mode vs Multimode Waveguide | V-number · mode cutoff · single-mode design criteria for PICs | ⬜ Planned |
| 04 | Silicon-on-Insulator Strip Waveguide | SOI platform · effective index method · high-index contrast confinement | ⬜ Planned |
| 05 | Waveguide Bend Loss | Radiation loss at bends · minimum bend radius · mode mismatch at transitions | ⬜ Planned |
| 06 | Waveguide Group Velocity Dispersion | GVD coefficient · anomalous vs normal dispersion · dispersion engineering | ⬜ Planned |

---

### `02_passive_devices` — Core PIC Building Blocks

The foundation of any photonic integrated circuit. These are the structures that appear in every WDM transceiver, optical sensor, and photonic signal processor. Ring resonator simulations (04–06) are the portfolio centerpiece.

| # | Simulation | Physics Demonstrated | Status |
|---|-----------|---------------------|--------|
| 01 | Y-Junction Power Splitter | Power splitting · mode symmetry · fabrication tolerance analysis | ⬜ Planned |
| 02 | Directional Coupler | Evanescent coupling · coupling length · 3 dB coupler design | ⬜ Planned |
| 03 | Multimode Interference (MMI) Coupler | Self-imaging principle · broadband operation · insertion loss | ⬜ Planned |
| 04 | Ring Resonator — Through-Port Transmission | Resonance condition · free spectral range · extinction ratio | ⬜ Planned |
| 05 | Ring Resonator — Q-Factor Analysis | Loaded Q · intrinsic Q · coupling gap sweep | ⬜ Planned |
| 06 | Add-Drop Ring Resonator | WDM channel dropping · through vs drop port · crosstalk | ⬜ Planned |
| 07 | Mach-Zehnder Interferometer | Optical interference · phase-to-intensity conversion · null depth | ⬜ Planned |
| 08 | Bragg Grating Filter | Periodic dielectric structure · photonic stopband · reflection spectrum | ⬜ Planned |

---

### `03_active_devices` — Electromagnetic Modeling of Active PIC Components

Active devices involve carrier dynamics beyond MEEP's native scope. These simulations model the electromagnetic aspects — field overlap with active regions, modulation geometry, absorption profiles — and document explicitly what MEEP captures and what requires additional solvers.

| # | Simulation | Physics Demonstrated | Status |
|---|-----------|---------------------|--------|
| 01 | PIN Junction Waveguide Model | Confinement factor · overlap integral · mode-active region interaction | ⬜ Planned |
| 02 | Electro-Optic Modulator Geometry | Phase modulation · Pockels effect field geometry · modulation efficiency | ⬜ Planned |
| 03 | Photodetector Absorption Region | Mode overlap with absorbing material · responsivity geometry · bandwidth estimate | ⬜ Planned |
| 04 | Semiconductor Optical Amplifier | Gain medium in MEEP · field amplification · saturation geometry | ⬜ Planned |

---

### `04_circuits` — Multi-Component PIC Assemblies

Individual components assembled into functional integrated circuits. Simulations here combine multiple MEEP structures and introduce inter-component coupling, crosstalk, and cascaded response analysis.

| # | Simulation | Physics Demonstrated | Status |
|---|-----------|---------------------|--------|
| 01 | 2-Channel WDM Multiplexer | Ring-based wavelength routing · channel isolation · insertion loss | ⬜ Planned |
| 02 | 4-Channel WDM Demultiplexer | Filter bank design · channel spacing · adjacent channel crosstalk | ⬜ Planned |
| 03 | MZI-Based Optical Switch | Switching condition · extinction ratio · thermo-optic tuning geometry | ⬜ Planned |
| 04 | Reconfigurable Add-Drop Array | Cascaded ring resonators · multi-channel WDM routing | ⬜ Planned |
| 05 | Photonic Delay Line | Time delay · dispersion-managed propagation · buffer architecture | ⬜ Planned |

---

### `05_systems` — Architecture-Level Photonic Signal Processing

System-level analysis combining MEEP simulation results with Python post-processing. Includes link budget modeling and neuromorphic photonics architectures — directly relevant to photonic computing research.

| # | Simulation | Physics Demonstrated | Status |
|---|-----------|---------------------|--------|
| 01 | WDM Link Budget Analysis | Insertion loss · power penalty · channel count scaling | ⬜ Planned |
| 02 | Optical SNR Estimation | Noise sources in PICs · OSNR vs channel spacing | ⬜ Planned |
| 03 | Neuromorphic Photonic Weight Bank | Ring resonator arrays as synaptic weights · optical matrix-vector multiply | ⬜ Planned |
| 04 | Photonic Reservoir Computing Model | Nonlinear dynamics · temporal information processing with light | ⬜ Planned |

---

## Quickstart

### Prerequisites

- Linux or WSL2 (Ubuntu 20.04+)
- Miniconda or Anaconda
- Git

### Install MEEP via Conda

```bash
conda create -n photonics -c conda-forge pymeep python=3.9
conda activate photonics
pip install matplotlib numpy
```

### Run Any Simulation

```bash
git clone https://github.com/YOUR_USERNAME/photonic-integrated-circuits.git
cd photonic-integrated-circuits/00_em_fundamentals/01_free_space_gaussian_pulse
python 01_free_space_gaussian_pulse.py
```

Output plots are saved as `.png` in the simulation directory. No GUI or notebook required.

---

## Tools and Environment

| Tool | Role in This Workflow |
|------|-----------------------|
| [MIT MEEP](https://meep.readthedocs.io/) | Primary FDTD electromagnetic solver |
| [MIT MPB](https://mpb.readthedocs.io/) | Photonic band structure and mode profile solver |
| Python 3.9 | Simulation scripting, post-processing, visualization |
| NumPy | Numerical array operations, Fourier analysis |
| Matplotlib | Field plots, transmission spectra, mode profiles |
| Conda (Miniconda) | Reproducible environment management |
| WSL2 + Ubuntu | Linux simulation environment on Windows hardware |
| VS Code | Script editing and WSL terminal integration |

---

## Key Photonic Concepts Covered

`FDTD simulation` · `finite-difference time-domain` · `MIT MEEP` · `MIT MPB` · `photonic integrated circuits` · `PIC design` · `silicon photonics` · `silicon-on-insulator` · `SOI waveguide` · `optical waveguide modes` · `TE mode` · `TM mode` · `total internal reflection` · `evanescent coupling` · `directional coupler` · `ring resonator` · `Q-factor` · `free spectral range` · `WDM` · `wavelength division multiplexing` · `add-drop multiplexer` · `Mach-Zehnder interferometer` · `Bragg grating` · `perfectly matched layer` · `PML` · `Gaussian pulse` · `Fresnel equations` · `group velocity dispersion` · `neuromorphic photonics` · `photonic signal processing`

---

## About

**K. S. Harshavardan** — RF and Signal Processing Engineer, Bharat Electronics Limited, India.

Transitioning into photonic integrated circuit design and photonic signal processing for European research and industry. NPTEL Photonic Integrated Circuits certification, top 5 percentile. Currently enrolled in NPTEL Introduction to Photonics and Applied Electromagnetics.

Long-term direction: photonic neuromorphic computing.

[LinkedIn](https://linkedin.com/in/YOUR_PROFILE) · [GitHub](https://github.com/YOUR_USERNAME)

---

## License

MIT License. All simulation scripts are free to use, adapt, and redistribute with attribution.  
See [LICENSE](./LICENSE) for full terms.