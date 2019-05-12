"""
Plot the Geldart particle classification based on gas density, solid density,
and mean particle diameter. Update by G.W. on 5/11/2019.
"""

import chemics as cm

dp = 300
rhog = 0.0012
rhos = 2.5

cm.plot_geldart(dp, rhog, rhos)
