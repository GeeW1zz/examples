"""
Convert proximate analysis from as-received basis to dry basis and dry
ash-free basis.
"""

import chemics as cm

# proximate analysis as-received basis (% ar)
# given as [FC, VM, ash, moisture]
prox_ar = [16.92, 76.40, 0.64, 6.04]

# convert to other bases
prox = cm.proximate_bases(*prox_ar)

# dry basis (% dry) as [FC, VM, ash]
print(f"""
FC {prox['dry'][0]:.2f}
VM {prox['dry'][1]:.2f}
ash {prox['dry'][2]:.2f}
""")

# dry ash-free basis (% daf) as [FC, VM]
print(f"""
FC {prox['daf'][0]:.2f}
VM {prox['daf'][1]:.2f}
""")

# display all bases to console
prox2 = cm.proximate_bases(*prox_ar, disp=True)
