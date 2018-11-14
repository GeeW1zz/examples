"""
Determine viscosity of a gas at temperature or for a range of temperatures.
Updated by G.W. on 11/14/2018.
"""

import chemics as cm
import matplotlib.pyplot as plt
import numpy as np

# Determine viscosity of nitrogen gas at temperature [K]
# ----------------------------------------------------------------------------

mu_n2 = cm.mu_gas_inorganic('N2', 773.15)

# Use coefficients to plot viscosity for range of temperatures [K]
# ----------------------------------------------------------------------------

results = cm.mu_gas_organic('CH4', 833, full=True)

mu_ch4 = results[0]
tmin = results[2]
tmax = results[3]
a, b, c, d = results[4:]

tk = np.arange(tmin, tmax+1)
mu_ch4_tk = a + b*tk + c*(tk**2) + d*(tk**3)

# Print results
# ----------------------------------------------------------------------------

print(f'mu_n2 = {mu_n2:.2f} micropoise')
print(f'mu_n2 = {mu_n2/1e7:.5g} kg/(m s)')

# Plot results
# ----------------------------------------------------------------------------

plt.close('all')

plt.figure()
plt.plot(tk, mu_ch4_tk)
plt.xlabel('Temperature [K]')
plt.ylabel(r'Viscosity of gas [$\mu$ P]')
plt.title(r'Plot of CH$_4$ viscosity vs temperature')

plt.show()
