#!/usr/bin/env python3
"""Exact local homotopy for the unequal-slope unit extension.

Only a first-order local deformation is certified.  No global HH
vanishing, finite action, or semiregularity is asserted.
"""
from pathlib import Path
import json
import sympy as s

z=s.symbols('z0:4')
f=s.Function('f')(*z)
g=s.Function('g')(*z)
p=s.symbols('p01 p02 p03 p12 p13 p23')
pairs=[(i,j) for i in range(4) for j in range(i+1,4)]

def bracket(a,b):
    return sum(c*(s.diff(a,z[i])*s.diff(b,z[j])
                  -s.diff(a,z[j])*s.diff(b,z[i]))
               for c,(i,j) in zip(p,pairs))

P=bracket(f,g)
d1=s.Matrix([[-g,0,0],[f,0,0],[-1,f,g]])
d2=s.Matrix([0,-g,f])
h1=s.Matrix([[0,P,0],[0,0,P],[0,0,0]])
h2=s.Matrix([-P,0,0])
star=s.Matrix([sum(bracket(d1[i,j],d2[j,0])/2 for j in range(3))
               for i in range(3)])
assert d1*d2==s.zeros(3,1)
assert s.simplify(star-s.Matrix([0,0,-P]))==s.zeros(3,1)
assert s.simplify(d1*h2+h1*d2-s.Matrix([0,0,P]))==s.zeros(3,1)
assert s.simplify(star+d1*h2+h1*d2)==s.zeros(3,1)
minimal=s.Matrix([[-f*g,-g*g],[f*f,f*g]])
minimal_syzygy=s.Matrix([-g,f])
assert minimal*minimal_syzygy==s.zeros(2,1)
t=s.symbols('t')
character=s.series(2*s.exp(-t)-2*s.exp(-3*t)+s.exp(-4*t),t,0,5).removeO()
assert s.expand(character-(1-2*t**3+4*t**4))==0
out={
 'result':'PASS',
 'scope':'Generic f,g in four formal coordinates; all six constant bivector coefficients; first-order local homotopy only.',
 'star_square':'(0,0,-P)^t',
 'h2':'(-P,0,0)^t',
 'h1':'[[0,P,0],[0,0,P],[0,0,0]]',
 'corrected_square_zero':True,
 'minimal_resolution_square_zero':True,
 'complete_character_through_dimension_four':str(character),
 'limits':'Global gluing, global HH evaluation, finite action and semiregularity are not computed or asserted.'
}
Path(__file__).with_name('rm_unequal_slope_local_homotopy_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
