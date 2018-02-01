"""
Compare minimum fluidization velocities.
"""

import chemics as cm

# Parameters
# -----------------------------------------------------------------------------

# particle properties
dp = 0.0005   # diameter of bed particle, m
rhop = 1580   # density of bed particle, kg/m^3

# air properties at T=300K and P=1atm -> rho=1.17 kg/m^3, ug=1.85e-5 kg/ms
# N2 properties at T=773K and P=1atm -> rho=0.44 kg/m^3, ug=3.6e-5 kg/ms
ug = 3.6e-5     # dynamic viscosity of gas, kg/ms
rhog = 0.44     # density of gas, kg/m^3

# void fraction and sphericity for the Ergun equation
ep = 0.46    # void fraction, (-)
phi = 0.86   # sphericity, (-)

# Umf Calculations
# -----------------------------------------------------------------------------

# Wen and Yu correlation
umf_WenYu = cm.umfWenYu(dp, rhog, rhop, ug)

# Richardson correlation
umf_Rich = cm.umfRich(dp, rhog, rhop, ug)

# Saxena and Vogel correlation
umf_SaxVogel = cm.umfSaxVog(dp, rhog, rhop, ug)

# Babu correlatio
umf_Babu = cm.umfBabu(dp, rhog, rhop, ug)

# Grace correlation
umf_Grace = cm.umfGrace(dp, rhog, rhop, ug)

# Chitester correlation
umf_Chit = cm.umfChit(dp, rhog, rhop, ug)

# Ergun function
umf_Ergun = cm.umfErgun(dp, ep, phi, rhog, rhop, ug)

# Small particles, Re < 20
umf_SmallRe = cm.umfSmallRe(dp, ep, phi, rhog, rhop, ug)

# Large particles, Re > 1000
umf_LargeRe = cm.umfLargeRe(dp, ep, phi, rhog, rhop)

# Print Results
# -----------------------------------------------------------------------------

print('Umf = {:.4f} m/s Wen and Yu'.format(umf_WenYu))
print('Umf = {:.4f} m/s Richardson'.format(umf_Rich))
print('Umf = {:.4f} m/s Saxena and Vogel'.format(umf_SaxVogel))
print('Umf = {:.4f} m/s Babu'.format(umf_Babu))
print('Umf = {:.4f} m/s Grace'.format(umf_Grace))
print('Umf = {:.4f} m/s Chitester'.format(umf_Chit))
print('Umf = {:.4f} m/s Ergun'.format(umf_Ergun))
print('Umf = {:.4f} m/s Small Re'.format(umf_SmallRe))
print('Umf = {:.4f} m/s Large Re'.format(umf_LargeRe))

