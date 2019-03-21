"""
Calculate tranport velocity for particles in a riser.
"""

import chemics as cm

dp = 0.0005     # paricle diameter [m]
mu = 3.6e-5     # viscosity of nitrogen gas at 773 K and 1 atm [kg/(m s)]
rhog = 0.44     # density of nitrogen gas at 773 K and 1 atm [kg/m^3]
rhos = 1630     # particle density [kg/m^3]

utr = cm.utr(dp, mu, rhog, rhos)

print(f'utr = {utr:.4f} m/s')
