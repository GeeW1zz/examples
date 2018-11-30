"""
Determine molecular weight of an element, compound, or gas mixture. Updated by
G.W. on 11/30/2018.
"""

import chemics as cm

formula = 'C'
mw = cm.molecular_weight(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = 'Co'
mw = cm.molecular_weight(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = 'CH4'
mw = cm.molecular_weight(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = '(CO2)2'
mw = cm.molecular_weight(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = 'Ca(C2H3O2)2'
mw = cm.molecular_weight(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = '(NH4)2SO4'
mw = cm.molecular_weight(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = '(NH4)(NO3)'
mw = cm.molecular_weight(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = '((NH4)3)'
mw = cm.molecular_weight(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

formula = '(((H2O)4)3)8'
mw = cm.molecular_weight(formula)
print(f'Molecular weight of {formula} = {mw:.2f} g/mol')

mix = ['H2', 'N2']
mw_mix = cm.mw_mix(mix, [0.8, 0.2])
print(f'Molecular weight of mixture {mix} = {mw_mix:.2f} g/mol')

mix = ['H2', 'N2']
mw_mix = cm.mw_mix(mix, [0.8, 0.2])
print(f'Molecular weight of mixture {mix} = {mw_mix:.2f} g/mol')
