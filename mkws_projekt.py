# -*- coding: utf-8 -*-
import cantera as ct
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# INITIAL CONDITIONS
# =====================================================
T0 = 300.0
P0 = ct.one_atm
gas = ct.Solution("gri30.yaml")


REFINE = True


REFINE_CRITERIA = {
    "ratio": 3,
    "slope": 0.05,
    "curve": 0.1
}

# =====================================================
# STORAGE
# =====================================================
H2_fractions = np.linspace(0, 0.5, 11)

flame_speed = []
NO_ppm = []
NO2_ppm = []
N2O_ppm = []
Tad = []

# =====================================================
# EFFECT OF HYDROGEN CONTENT
# =====================================================
for x_H2 in H2_fractions:

    fuel = {"CH4": 1 - x_H2, "H2": x_H2}
    oxidizer = {"O2": 1, "N2": 3.76}

    # ---------------- adiabatic temperature ----------------
    gas.set_equivalence_ratio(1.0, fuel, oxidizer)
    gas.TP = T0, P0

    gas.equilibrate("HP")
    Tad.append(gas.T)

    # ---------------- flame ----------------
    gas.set_equivalence_ratio(1.0, fuel, oxidizer)
    gas.TP = T0, P0

    flame = ct.FreeFlame(gas, width=0.03)
    flame.set_refine_criteria(**REFINE_CRITERIA)

    flame.solve(loglevel=0, auto=True, refine_grid=REFINE)

    flame_speed.append(flame.velocity[0] * 100)

    gas.X = flame.X[:, -1]

    NO_ppm.append(gas["NO"].X[0] * 1e6)
    NO2_ppm.append(gas["NO2"].X[0] * 1e6)
    N2O_ppm.append(gas["N2O"].X[0] * 1e6)

# =====================================================
# SAVE RESULTS
# =====================================================
results = pd.DataFrame({
    "H2_fraction": H2_fractions,
    "Flame_speed_cm_s": flame_speed,
    "NO_ppm": NO_ppm,
    "NO2_ppm": NO2_ppm,
    "N2O_ppm": N2O_ppm,
    "Adiabatic_temperature_K": Tad
})

results.to_csv("results.csv", index=False)

# =====================================================
# PLOT FUNCTION
# =====================================================
def plot(x, y, xlabel, ylabel, filename, style='o-'):
    plt.figure(figsize=(7,5))
    plt.plot(x, y, style)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.tight_layout()
    plt.savefig(filename, dpi=300)

# =====================================================
# MAIN PLOTS
# =====================================================
plot(H2_fractions*100, flame_speed,
     "Hydrogen fraction (%)",
     "Laminar flame speed (cm/s)",
     "flame_speed.png")

plot(H2_fractions*100, NO_ppm,
     "Hydrogen fraction (%)",
     "NO (ppm)",
     "NO_emissions.png", 'o-r')

plot(H2_fractions*100, NO2_ppm,
     "Hydrogen fraction (%)",
     "NO2 (ppm)",
     "NO2_emissions.png", 'o-g')

plot(H2_fractions*100, N2O_ppm,
     "Hydrogen fraction (%)",
     "N2O (ppm)",
     "N2O_emissions.png", 'o-m')

plot(H2_fractions*100, Tad,
     "Hydrogen fraction (%)",
     "Adiabatic temperature (K)",
     "adiabatic_temperature.png", 'o-k')



plt.show()