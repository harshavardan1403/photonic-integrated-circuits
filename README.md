# Photonic Integrated Circuits — MEEP FDTD Simulation Portfolio

> FDTD electromagnetic simulations of photonic integrated circuit components using MIT MEEP.  
> Structured from first principles — free space propagation through to waveguides, resonators, and signal processing devices.

---

## About

This repository documents a structured, ground-up study of photonic integrated circuit simulation using the open-source FDTD solver [MEEP (MIT Electromagnetic Equation Propagation)](https://meep.readthedocs.io/en/latest/).

Each simulation is self-contained: runnable Python script, output plots, and a documented README explaining the physics, the parameters, and what the result means physically. The goal is rigorous simulation practice that builds toward photonic signal processing components relevant to WDM systems, neuromorphic photonics, and photonic integrated circuit design.

**Simulation environment:** MIT MEEP · Python 3.9 · NumPy · Matplotlib · WSL2 (Ubuntu) · VS Code  
**Background:** RF and Signal Processing Engineer · NPTEL Photonic Integrated Circuits (Top 5%) · NPTEL Introduction to Photonics (ongoing)

---

## Simulations Index

### Phase 1 — Foundations

| # | Simulation | Key Concept | Status |
|---|-----------|-------------|--------|
| 01 | [Free Space Gaussian Pulse](./01_free_space_gaussian_pulse/) | FDTD basics · Time-bandwidth product · PML boundaries | ✅ Complete |
| 02 | Dielectric Slab — Transmission and Reflection | Fresnel equations · Refractive index · Phase velocity | 🔄 In progress |
| 03 | 2D Waveguide Mode Propagation | Total internal reflection · Guided modes · Field confinement | ⬜ Planned |
| 04 | Field Visualization — TE and TM Modes | Polarization · Mode profiles · Spatial field distribution | ⬜ Planned |

### Phase 2 — Core Photonic Components

| # | Simulation | Key Concept | Status |
|---|-----------|-------------|--------|
| 05 | Strip Waveguide Design | Effective index · Bend loss · Single-mode condition | ⬜ Planned |
| 06 | Evanescent Coupling — Directional Coupler | Coupling length · Power splitting ratio | ⬜ Planned |
| 07 | Ring Resonator — Transmission Spectrum | Resonance condition · FSR · Finesse | ⬜ Planned |
| 08 | Ring Resonator — Q-Factor Analysis | Loaded vs intrinsic Q · Loss mechanisms | ⬜ Planned |

### Phase 3 — Photonic Signal Processing (Ongoing)

Planning ongoing

---

## Repository Structure

```
photonic-integrated-circuits/
├── 01_free_space_gaussian_pulse/
│   ├── 01_free_space_gaussian_pulse.py   # Runnable simulation script
│   ├── session1_output.png               # Output plot
│   └── README.md                         # Physics explanation + results
├── 02_dielectric_slab/
│   └── ...
└── README.md                             # This file
```

Each simulation folder is independently runnable. Clone the repo, activate a MEEP environment, and run any script directly:

```bash
git clone https://github.com/harshavardan/photonic-integrated-circuits
cd 01_free_space_gaussian_pulse
python 01_free_space_gaussian_pulse.py
```

---

## Tools and Environment

| Tool | Purpose |
|------|---------|
| [MIT MEEP](https://meep.readthedocs.io/) | FDTD electromagnetic simulation |
| [MIT MPB](https://mpb.readthedocs.io/) | Photonic band structure and mode solving |
| Python 3.9 + NumPy | Simulation scripting and numerical processing |
| Matplotlib | Field visualization and spectral plots |
| Conda (Miniconda) | Environment management |
| WSL2 + Ubuntu | Linux simulation environment on Windows |
| VS Code | Development and script execution |

---

## About the Author

**K. S. Harshavardan** — RF and Signal Processing Engineer at Bharat Electronics Limited, India.  
Transitioning into photonic integrated circuit design and photonic signal processing.  
NPTEL Photonic Integrated Circuits certification · Top 5 percentile.

[LinkedIn](https://linkedin.com/in/harshavardan1403) · [GitHub](https://github.com/harshavardan1403)

---

## License

MIT License. Scripts are free to use, modify, and distribute with attribution.