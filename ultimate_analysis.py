"""
Convert ultimate analysis from as-received basis to dry basis and dry ash-free
basis.
"""

import chemics as cm

# ultimate analysis as-received basis (% ar)
# given as [C, H, O, N, S, ash, moisture]
ult_ar = [49.52, 5.28, 38.35, 0.15, 0.02, 0.64, 6.04]

# convert to other bases
ult = cm.ultimate_bases(*ult_ar)

# dry basis (% dry) as [C, H, O, N, S, ash]
print(f"""
C {ult['dry'][0]:.2f}
H {ult['dry'][1]:.2f}
O {ult['dry'][2]:.2f}
N {ult['dry'][3]:.2f}
S {ult['dry'][4]:.2f}
ash {ult['dry'][5]:.2f}
""")

# dry ash-free basis (% daf) as [[C, H, O, N, S]
print(f"""
C {ult['daf'][0]:.2f}
H {ult['daf'][1]:.2f}
O {ult['daf'][2]:.2f}
N {ult['daf'][3]:.2f}
S {ult['daf'][4]:.2f}
""")

# display all bases to console
ult2 = cm.ultimate_bases(*ult_ar, disp=True)
