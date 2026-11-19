#!/usr/bin/env python3
"""Independent check of the displayed reduced identity in F.3.32.

The seven scalar rows and five detector rows are retained inputs already
independently checked by literal word realization. This certificate types
the displayed N0 independently and checks all 36 polynomial identities.
It does not substitute for the standalone diagram recomputation.
"""
from pathlib import Path
import pickle
import sympy as sp

data = pickle.loads(Path('work/calc_levi_selected_identity.pickle').read_bytes())
s = data['s']
M, K = data['M'], data['K']
L = sp.Matrix([[-1,4,0,0,0],[1,0,1,0,0],[0,0,0,1,1]])
J = sp.Matrix([[-104,-288],[-26,-72],[104,288],[32,192],[-32,-192]])
N = sp.Matrix([
[-2*s*(2*s+3)*(128*s**4+528*s**3+776*s**2+465*s+101),
 -4*s*(2*s+3)*(16*s**4-48*s**3-305*s**2-402*s-152),
 2*s*(s-1)*(2*s+3)*(128*s**3+464*s**2+550*s+199),
 -3*s*(576*s**4+2720*s**3+4684*s**2+3546*s+1029),
 -6*s*(s+2)*(4*s+3)*(4*s+5)*(8*s+7),
 3*s*(2*s+1)*(2*s+3)*(80*s**2+240*s+187),
 24*s*(s-1)*(2*s+3)*(4*s**2+6*s-1)],
[2*s*(2*s+1)**2*(2*s+3)*(8*s**2+25*s+20),
 2*s*(2*s+1)*(2*s+3)*(4*s**3-14*s**2-70*s-61),
 -4*s*(s-1)*(2*s+1)*(2*s+3)*(8*s**2+25*s+20),
 3*s*(2*s+3)*(72*s**3+232*s**2+224*s+69),
 6*s*(s+2)*(2*s+1)*(2*s+3)*(8*s+7),
 -3*s*(2*s+3)*(40*s**3+140*s**2+146*s+37),
 -6*s*(s-1)*(2*s+3)*(4*s**2+6*s-1)],
[-6*s*(2*s+3)*(16*s**3+66*s**2+80*s+27),
 -6*s*(2*s+3)*(4*s**3-12*s**2-82*s-81),
 6*s*(s-1)*(2*s+3)*(16*s**2+60*s+53),
 -18*s*(s+2)*(36*s**2+102*s+67),
 -36*s*(s+2)**2*(8*s+7),
 18*s*(s+2)*(2*s+3)*(10*s+13),0]])
d = 9*(2*s+3)*(4*s**2+6*s-1)
assert M.shape == (7,12) and K.shape == (5,12)
defects = (N*M-d*L*K).applyfunc(sp.expand)
assert all(sp.Poly(x,s,domain=sp.QQ).is_zero for x in defects)
assert L*J == sp.zeros(3,2) and L.rank() == 3 and J.rank() == 2
t = sp.symbols('t', nonnegative=True)
assert sp.expand(d.subs(s,3+t)-9*(9+2*t)*(53+30*t+4*t**2)) == 0
assert all(c>0 for c in sp.Poly(d.subs(s,3+t),t).all_coeffs())
assert L == data['L'] and L*K == data['LK']
print('DISPLAYED_REDUCED_N0_ENTRIES_CHECKED',len(N))
print('EXACT_QQ_s_IDENTITY_DEFECTS_ZERO',len(defects))
print('KERNEL_L_EQUALS_IMAGE_J: ranks3+2 and LJ=0')
print('DENOMINATOR',sp.factor(d))
print('NONVANISHING_ALL_s_GE_3: d(3+t)=9(9+2t)(53+30t+4t^2)')
print('SCOPE: displayed reduced identity and quotient-coordinate typing; retained previously verified scalar inputs.')
