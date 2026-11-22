#!/usr/bin/env python3
"""Exact algebraic-closure smoothness checks for the retained GF64 candidate.

The two projective charts on each E are Z=1 and Y=1 in
Y^2 Z+Y Z^2=X^3.  On the second chart, the local basis of O(3O)
is (y,x,1), and the equation is again y^2+y=x^3.
"""
from pathlib import Path
import json,time,sys,sympy as sp
from sympy.polys.agca.extensions import FiniteExtension
import ss_contact_witness as ff

started=time.perf_counter();w=Path(__file__).resolve().parents[1]
sourcepath=Path(sys.argv[1]) if len(sys.argv)>1 else w/'outputs/ss_contact_witness.json'
source=json.loads(sourcepath.read_text())
candidate=source['candidate'];s=candidate['coefficients']
z,x,y,u,v=sp.symbols('z x y u v')
mod=sp.Poly(z**6+z+1,z,modulus=2)
assert mod.is_irreducible
# SymPy's generic extension domain omits the associated-field flag and
# uses polynomial exact division in its domain-level exquo. Irreducibility
# is certified above; use the element's modular inverse for field division.
# Preserve the original domain class name for SymPy's conversion dispatch.
K=FiniteExtension(mod)
K.has_assoc_Field=True
K.get_field=lambda:K
K.exquo=lambda a,b:a/b
K.quo=lambda a,b:a/b
def coeff(a):return sum(z**i for i in range(6) if a>>i&1)
for a in range(64):
 for b in range(64):
    assert K(coeff(a))*K(coeff(b))==K(coeff(ff.mul(a,b)))
    if b:assert K.exquo(K(coeff(a)),K(coeff(b)))==K(coeff(ff.div(a,b)))
def section(chart):
    B=[1,x,y] if chart[0]==0 else [y,x,1]
    D=[1,u,v] if chart[1]==0 else [v,u,1]
    return sp.expand(sum(coeff(s[3*i+j])*B[i]*D[j] for i in range(3) for j in range(3)))
records=[]
outpath=w/'outputs'/f'verify_{sourcepath.stem}_geometry.json'
def save(status):
    result=dict(status=status,source=str(sourcepath),
                coefficient_field=str(K),sympy_version=sp.__version__,
                checks=records,elapsed_seconds=time.perf_counter()-started,
                unwanted_kernel_collisions_checked=False)
    outpath.write_text(json.dumps(result,indent=2)+'\n')
    return result
for i in range(2):
 for j in range(2):
    f=section((i,j));dx=sp.diff(f,x)+x*x*sp.diff(f,y);du=sp.diff(f,u)+u*u*sp.diff(f,v)
    equations=[y*y+y+x**3,v*v+v+u**3,f,dx,du]
    tick=time.perf_counter()
    basis=sp.groebner(equations,x,y,u,v,domain=K,order='grevlex')
    rec=dict(kind='source_smoothness',charts=[i,j],
             equations=[str(e) for e in equations],
             groebner_basis=[str(p.as_expr()) for p in basis.polys],
             unit_ideal=list(basis)==[1],seconds=time.perf_counter()-tick)
    records.append(rec);save('IN_PROGRESS')
    print(json.dumps({k:v for k,v in rec.items() if k not in ('equations','groebner_basis')}),flush=True)
    assert rec['unit_ideal'],'Candidate source is singular over the algebraic closure'
result=save('SMOOTH_SOURCE_PROVED; COLLISION_CHECKS_PENDING')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
