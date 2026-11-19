#!/usr/bin/env python3
"""Exact arithmetic checks of the Kodaira table and local volume formulas.

The correspondence of a geometric fiber to its root lattice is a cited theorem,
not an output of this script. Given that correspondence, Smith normal forms
independently check the component-group invariants of every displayed family.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def chain(n):
    A=2*s.eye(n)
    for i in range(n-1): A[i,i+1]=A[i+1,i]=-1
    return A

def star(arms):
    A=2*s.eye(1+sum(arms)); k=1
    for length in arms:
        prev=0
        for _ in range(length):
            A[prev,k]=A[k,prev]=-1; prev=k; k+=1
    return A

def group(A):
    if A.rows==0: return []
    D=smith_normal_form(A,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(A.rows) if abs(D[i,i])!=1]

rows=[]
def record(kind,m,delta,A,expected):
    g=group(A); assert g==expected,(kind,g,expected)
    rows.append(dict(type=kind,geometric_components=m,tame_v_delta=delta,
                     conductor_by_Ogg=delta+1-m,root_lattice_rank=A.rows,
                     component_group_cyclic_factors=g))
record('I0',1,0,s.zeros(0),[])
for n in range(1,21): record(f'I{n}',n,n,chain(n-1),[] if n==1 else [n])
record('II',1,2,s.zeros(0),[])
record('III',2,3,chain(1),[2])
record('IV',3,4,chain(2),[3])
for n in range(0,21):
    record(f'I{n}*',n+5,n+6,star([n+1,1,1]),[4] if n%2 else [2,2])
for kind,arms,delta,expected in [('IV*',[2,2,1],8,[3]),('III*',[3,2,1],9,[2]),('II*',[4,2,1],10,[])]:
    record(kind,2+sum(arms),delta,star(arms),expected)
assert all(r['conductor_by_Ogg']==(0 if r['type']=='I0' else 1 if '*' not in r['type'] and r['type'][1:].isdigit() else 2) for r in rows)
q,a,c,T=s.symbols('q a c T',nonzero=True)
vol=[]
for kind,count,poly in [('good',q+1-a,1-a*T+q*T*T),('split multiplicative',q-1,1-T),('nonsplit multiplicative',q+1,1+T),('additive',q,s.Integer(1))]:
    residual=s.factor(count/q-poly.subs(T,1/q)); assert residual==0
    vol.append(dict(type=kind,nonsingular_residue_points=str(count),
                    inverse_local_L_at_1=str(poly.subs(T,1/q)),
                    total_volume=str(c*count/q),identity_residual=str(residual)))
out={'scope':'Root-lattice and tame numerical table checks; no claim to prove Kodaira classification or wild conductor formula.',
     'rows':rows,'haar_volume_identities':vol,
     'all_pass':True}
p=Path(__file__).resolve().parents[1]/'outputs/c63_kodaira.json'
p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
