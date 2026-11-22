#!/usr/bin/env python3
"""Independent E821 arithmetic, using an eight-generator exterior algebra.

No author code or character-polynomial implementation is imported. Parameters
k are recovered by cohomological homogeneity; all divisor classes scale by k.
This certificate does not replace the local deformation or support proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial
from pathlib import Path
import hashlib
import json


def clean(a):
    return {m:F(c) for m,c in a.items() if c}


def add(*xs):
    z={}
    for x in xs:
        for m,c in x.items():
            z[m]=z.get(m,F(0))+c
    return clean(z)


def scale(a,c):
    return clean({m:c*x for m,x in a.items()})


def wedge(a,b):
    z={}
    for m,c in a.items():
        for n,d in b.items():
            if m&n:
                continue
            inversions=sum((n&((1<<i)-1)).bit_count()
                           for i in range(8) if (m>>i)&1)
            sign=(-1)**inversions
            z[m|n]=z.get(m|n,F(0))+sign*c*d
    return clean(z)


def power(a,j):
    z={0:F(1)}
    for _ in range(j):
        z=wedge(z,a)
    return z


def exp(a):
    return add(*(scale(power(a,j),F(1,factorial(j))) for j in range(5)))


def contract(a,i):
    z={}
    for m,c in a.items():
        if (m>>i)&1:
            z[m^(1<<i)]=c*(-1)**((m&((1<<i)-1)).bit_count())
    return clean(z)


def hermitian_form(M):
    z={}
    for i in range(4):
        for j in range(4):
            z=add(z,scale(wedge({1<<(2*i):F(1)},
                                {1<<(2*j+1):F(1)}),M[i][j]))
    return z


U=[[1,1,0,0],[1,-1,0,0],[0,0,1,1],[0,0,1,-1]]
I=[[int(i==j) for j in range(4)] for i in range(4)]
assert [[sum(U[i][a]*U[a][j] for a in range(4)) for j in range(4)]
        for i in range(4)] == [[2*x for x in row] for row in I]
theta=hermitian_form(I)
eta=hermitian_form(U)
one={0:F(1)}
char=add(scale(one,18),exp(eta),exp(scale(eta,-1)),
         *(scale(exp(add(scale(theta,s),scale(eta,t))),-1)
           for s,t in product((1,-1),repeat=2)))
# theta_+^2+theta_-^2 = theta^2/2+eta^2/4;
# theta_+^2 theta_-^2=(theta^2/4-eta^2/8)^2.
mixed=add(scale(power(theta,2),F(1,4)),scale(power(eta,2),F(-1,8)))
top=power(mixed,2)
target=add(scale(one,16),scale(power(theta,2),-2),
           scale(power(eta,2),-1),top)
assert char==target
assert top=={255:F(4)}
surface=[]
for s in (1,-1):
    surface.append(wedge(exp(scale(eta,s)),
                   add(exp(theta),scale(one,-2),exp(scale(theta,-1)))))
B=add(exp(eta),exp(scale(eta,-1)),*surface)
assert char==add(scale(one,18),scale(B,-1))
assert wedge(char,char).get(255)==256
assert [x.get(255,F(0)) for x in surface]==[-6,-6]
assert exp(eta).get(255)==4
assert exp(scale(eta,-1)).get(255)==4

# Check both balanced cap-kernel vectors directly, in split complex coordinates.
theta_plus={3:F(1),12:F(1)}
theta_minus={48:F(1),192:F(1)}
cap_checks=0
for q in (F(1,2),F(1),F(3)):
    v=wedge(add(one,scale(power(theta_plus,2),-q/2)),
            add(one,scale(power(theta_minus,2),-q/2)))
    for th,i,j in ((theta_plus,0,2),(theta_minus,4,6)):
        anti=contract(contract(scale(power(th,2),F(1,2)),i),j)
        assert add(contract(contract(v,i),j),scale(wedge(anti,v),q))=={}
        cap_checks+=1

restrictions=[]
for s in (1,-1):
    H=[[I[i][j]+s*U[i][j] for j in range(4)] for i in range(4)]
    for ij in combinations(range(4),2):
        a,b=ij
        d=H[a][a]*H[b][b]-H[a][b]*H[b][a]
        tr=H[a][a]+H[b][b]
        typ='index1' if d<0 else 'positive' if d>0 and tr>0 else 'flat_factor'
        restrictions.append({'sign':s,'free':[i+1 for i in ij],
                             'det':d,'trace':tr,'type':typ})
    positives=[x['free'] for x in restrictions if x['sign']==s and x['type']=='positive']
    assert positives==([[1,3]] if s==1 else [[2,4]])

# Exhaust all combinatorial face types used to force vanishing on the only
# positive components. Point indices within each torsion set have no effect.
face_checks=0
for s,free in ((1,(0,2)),(-1,(1,3))):
    fixed=tuple(i for i in range(4) if i not in free)
    for sides in ((0,1),(1,0)):
        constraints=dict(zip(fixed,sides))
        for f in free:
            for side in (0,1):
                face=dict(constraints);face[f]=side
                found=False
                for a,b in combinations(face,2):
                    if face[a]==face[b]:
                        continue
                    other_free=[i+1 for i in range(4) if i not in (a,b)]
                    row=next(x for x in restrictions if x['sign']==s and x['free']==other_free)
                    if row['type']!='positive':
                        found=True
                assert found
                face_checks+=1

p=Path(__file__).resolve().parent
author=p.parent.parent/'sixfolds'
inputs=['rm_surface_cone_obstruction_draft.md',
        'rm_surface_cone_torsionfree_addendum_draft.md',
        'rm_surface_cone_certificate.py']
out={'result':'PASS','method':'Independent Fraction exterior algebra on eight generators; no author arithmetic imported',
     'proof_hashes':{f:hashlib.sha256((author/f).read_bytes()).hexdigest() for f in inputs},
     'full_character_rank':16,'q':'k^2/2',
     'top_character_integral':'4*k^4','self_Euler':'256*k^4',
     'individual_surface_Euler':'-6*k^4','line_bundle_h2':'4*k^4 each',
     'restriction_matrices':restrictions,'balanced_cap_checks':cap_checks,
     'positive_component_face_types':face_checks,
     'scope':'Character, intersection, cap identities and restriction combinatorics only; support/deformation/addendum proofs reviewed separately.'}
(p/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
