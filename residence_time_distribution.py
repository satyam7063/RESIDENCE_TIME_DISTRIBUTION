import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz, trapz
from scipy.special import factorial

# Time range
t = np.linspace(0.001, 10, 1000)
tau = 2.0  # Mean residence time

# 1. Ideal CSTR RTD
E_cstr = (1 / tau) * np.exp(-t / tau)
F_cstr = cumtrapz(E_cstr, t, initial=0)

# 2. Tanks-in-Series (n CSTRs in series)
n = 3
E_series = (n**n * t**(n - 1) * np.exp(-n * t / tau)) / (factorial(n - 1) * tau**n)
F_series = cumtrapz(E_series, t, initial=0)

# 3. PFR RTD (approximated by a narrow Gaussian spike)
E_pfr = (1 / (0.05 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((t - tau) / 0.05)**2)
F_pfr = cumtrapz(E_pfr, t, initial=0)

# Calculate mean residence time and variance for tanks-in-series
tau_series = trapz(t * E_series, t)
var_series = trapz(((t - tau_series)**2) * E_series, t)

# Plotting E(t)
plt.figure(figsize=(10, 6))
plt.plot(t, E_cstr, label='CSTR', color='red')
plt.plot(t, E_series, label=f'{n} CSTRs in Series', color='blue')
plt.plot(t, E_pfr, label='PFR (Gaussian approx)', color='green')
plt.title('RTD Function E(t)')
plt.xlabel('Time (t)')
plt.ylabel('E(t)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting F(t)
plt.figure(figsize=(10, 6))
plt.plot(t, F_cstr, label='CSTR', color='red')
plt.plot(t, F_series, label=f'{n} CSTRs in Series', color='blue')
plt.plot(t, F_pfr, label='PFR (Gaussian approx)', color='green')
plt.title('Cumulative RTD Function F(t)')
plt.xlabel('Time (t)')
plt.ylabel('F(t)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Display numerical results
print(f"Mean Residence Time (τ) for tanks-in-series (n={n}): {tau_series:.2f}")
print(f"Variance (σ²) for tanks-in-series (n={n}): {var_series:.4f}")
