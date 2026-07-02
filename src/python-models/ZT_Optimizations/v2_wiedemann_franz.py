import numpy as np
import matplotlib.pyplot as plt

# Auri Labs - FlexTEG ZT Optimization Model V2
# Material: Ag2Se Nanowires + PEDOT:PSS Matris


T = 300  # (Kelvin)

# Thermal conductivity (k) [W/mK]
k_polymer = 0.25
k_ag2se = 0.60

# Electrical Conductivity (sigma) [S/m]
sigma_polymer = 1000
sigma_ag2se = 1.5e5

# Seebeck Coefficient (S) [V/K]
S_polymer = 20e-6
S_ag2se = 150e-6

# Percolation Parameters
phi = np.linspace(0.01, 0.40, 500)
phi_c = 0.06
t_exponent = 2.0

L_lorenz = 2.44e-8  # W*Ohm/K^2 (Standart Lorenz Value)

sigma_total = np.zeros_like(phi)
k_total = np.zeros_like(phi)
S_total = np.zeros_like(phi)


for i, p in enumerate(phi):
    

    if p <= phi_c:
        sigma_total[i] = sigma_polymer * (1 + 3 * p) 
    else:
        sigma_total[i] = sigma_polymer + (sigma_ag2se - sigma_polymer) * ((p - phi_c) / (1 - phi_c))**t_exponent
        

    # New Thermal Conductivity Calculations via Wiedemann-Franz Equations

    k_lattice = k_polymer * (1 - p) + k_ag2se * p
    
    k_electronic = L_lorenz * sigma_total[i] * T
    
    k_total[i] = k_lattice + k_electronic
    

    S_total[i] = (S_polymer * sigma_polymer * (1 - p) + S_ag2se * sigma_total[i] * p) / (sigma_polymer * (1 - p) + sigma_total[i] * p)

# lastly ZT - Figure of Merit Calc.
ZT = (S_total**2 * sigma_total * T) / k_total


max_ZT = np.max(ZT)
optimal_phi = phi[np.argmax(ZT)]

print(f"--- Auri Labs Simulation Results ---")
print(f"Max ZT: {max_ZT:.3f}")
print(f"Optimum Ag2Se Volume Fraction: %{optimal_phi*100:.1f}")



fig, ax1 = plt.subplots(figsize=(10, 6))

color1 = 'tab:blue'
ax1.set_xlabel('Ag2Se Volume Fraction ($\Phi$)')
ax1.set_ylabel('Electrical Conductivity ($\sigma$) [S/m]', color=color1)
line1 = ax1.plot(phi, sigma_total, color=color1, label='Electrical Conductivity', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()  
color2 = 'tab:red'
ax2.set_ylabel('ZT', color=color2)
line2 = ax2.plot(phi, ZT, color=color2, label='ZT Value', linewidth=2, linestyle='--')
ax2.tick_params(axis='y', labelcolor=color2)


ax2.plot(optimal_phi, max_ZT, marker='o', markersize=8, color='gold', markeredgecolor='black')
ax2.annotate(f'Optimum Point\n% {optimal_phi*100:.1f} Ag2Se\nZT: {max_ZT:.2f}',
             xy=(optimal_phi, max_ZT), xytext=(optimal_phi + 0.05, max_ZT - 0.2),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')

plt.axvline(x=phi_c, color='gray', linestyle=':', label='Percolation threshold ($\Phi_c$)')

plt.title('Auri Labs: Flexible Ag2Se/PEDOT:PSS Thermoelectric Band Optimization', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
fig.tight_layout()
plt.show()