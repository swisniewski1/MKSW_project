# The Impact of Hydrogen Addition on Methane-Air Combustion

Numerical investigation of hydrogen-enriched methane flames using **Python**, **Cantera**, and the **GRI-Mech 3.0** mechanism.

## 📌 Project Overview
This study evaluates how adding hydrogen ($H_2$, 0% to 50%) to methane-air mixtures affects laminar flame characteristics and pollutant emissions ($NO_x$) across variations in equivalence ratio ($\phi$), pressure ($P$), and initial temperature ($T_0$).

---

## 📈 Key Findings

* **Laminar Flame Speed ($s_u$):** Increases monotonically from **$\approx 38\text{ cm/s}$** (0% $H_2$) to **$> 60\text{ cm/s}$** (50% $H_2$) due to enhanced mass diffusivity and kinetic rates of hydrogen.
* **Adiabatic Flame Temperature ($T_{ad}$):** Rises systematically from **$2225\text{ K}$** to over **$2258\text{ K}$**[cite: 1].
* **Nitric Oxide ($NO$) Emissions:** Contrary to the thermal Zeldovich mechanism, $NO$ steadily **decreases** from **$\approx 169.8\text{ ppm}$** to **$\approx 164.1\text{ ppm}$**[cite: 1]. This indicates that chemical dilution and shorter residence times outweighed the thermal effect[cite: 1].
* **$NO_2$ & $N_2O$ Profiles:** $NO_2$ remains extremely low and slightly decreases ($0.033\text{ ppm}$)[cite: 1], while $N_2O$ displays a linear increase from **$0.099\text{ ppm}$** to **$0.110\text{ ppm}$**[cite: 1].

---

## 🚀 Quick Start

1. **Install dependencies:**
```bash
   conda create --name cantera_env -c cantera cantera numpy matplotlib
   conda activate cantera_env
