"""
Example of estimating biomass composition from ultimate analysis values.
"""

import matplotlib.pyplot as plt
import chemics as cm

# Parameters
# ----------------------------------------------------------------------------

yc = 0.534
yh = 0.06

# Biomass composition
# ----------------------------------------------------------------------------

bc = cm.biocomp(yc, yh, printcomp=True)

# Plot results
# ----------------------------------------------------------------------------

fig, ax = plt.subplots(tight_layout=True)
cm.plot_biocomp(ax, yc, yh, bc['y_rm1'], bc['y_rm2'], bc['y_rm3'])

plt.show()
