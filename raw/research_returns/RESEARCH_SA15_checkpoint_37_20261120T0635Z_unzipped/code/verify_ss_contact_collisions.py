#!/usr/bin/env python3
"""Exclude every other nonnodal collision over the algebraic closure.

Projective translation matrices are certified by exact rational group-law
identities, not by their values at finitely many points alone. All four
charts and all28 nonzero translation pairs are checked by Groebner bases.
"""
from pathlib import Path
import itertools,json,time,sys,sympy as sp
from sympy.polys.agca.extensions import FiniteExtension
import ss_contact_witness as ff

started=time.perf_counter();w=Path(__file__).resolve().parents[1]
sourcepath=Path(sys.argv[1]) if len(sys.argv)>1 else w/'outputs/ss_contact_witness.json'
source=json.loads(sourcepath.read_text())
candidate=source['candidate'];s=candidate['coefficients']
z,x,y,u,v=sp.symbols('z x y u v')
mod=sp.Poly(z**6+z+1,z,modulus=2);assert mod.is_irreducible
K=FiniteExtension(mod);K.has_assoc_Field=True;K.get_field=lambda:K
K.exquo=lambda a,b:a/b;K.quo=lambda a,b:a/b
def coeff(a):return sum(z**i for i in range(6) if a>>i&1)
def projective(P):return [0,0,1] if P is None else [1,P[0],P[1]]
def tuple_point(P):return None if P is None else tuple(P)
kernel=[tuple(tuple_point(P) for P in g) for g in source['kernel']]
kernel=[g for g in kernel if g!=(None,None)]
G=tuple(map(tuple_point,source['G']));minusG=tuple(ff.neg(P) for P in G)
curve_reduce=sp.groebner([y*y+y+x**3],y,x,domain=K)
torsion=[]
for a,b in itertools.product(range(64),repeat=2):
    P=(a,b)
    if ff.mul(b,b)^b==ff.power(a,3) and ff.scalar(3,P) is None:torsion.append(P)
torsion.append(None);assert len(torsion)==9
translation_records=[]
def translation(g):
    if g is None:return [[1,0,0],[0,1,0],[0,0,1]]
    equations=[]
    for P in torsion:
        b=projective(P);c=projective(ff.add(P,g))
        for a,i in itertools.combinations(range(3),2):
            row=[0]*9
            for j in range(3):
                row[3*a+j]^=ff.mul(c[i],b[j]);row[3*i+j]^=ff.mul(c[a],b[j])
            equations.append(row)
    N=ff.nullspace(equations,9);assert len(N)==1
    T=[N[0][3*i:3*i+3] for i in range(3)];assert ff.determinant3(N[0])
    L=[sum(coeff(a)*b for a,b in zip(row,[1,x,y])) for row in T]
    gx,gy=map(coeff,g);den=x+gx;num=y+gy
    rx=num**2+den**3
    ry=num*rx+(y+1)*den**3+num*x*den**2
    identities=[sp.expand(L[1]*den**2+L[0]*rx),sp.expand(L[2]*den**3+L[0]*ry)]
    assert all(curve_reduce.reduce(e)[1]==0 for e in identities)
    translation_records.append(dict(point=g,matrix=T,group_law_identities='Both reduce to zero modulo y^2+y+x^3'))
    return T
translations={g:translation(g) for g in torsion}
def linear(T,B):return [sum(coeff(a)*b for a,b in zip(row,B)) for row in T]
def section(chart,g=(None,None)):
    B=[1,x,y] if chart[0]==0 else [y,x,1]
    D=[1,u,v] if chart[1]==0 else [v,u,1]
    B=linear(translations[g[0]],B);D=linear(translations[g[1]],D)
    return sp.expand(sum(coeff(s[3*i+j])*B[i]*D[j] for i in range(3) for j in range(3)))
def derivative(f):return sp.diff(f,x)+x*x*sp.diff(f,y),sp.diff(f,u)+u*u*sp.diff(f,v)
def chart_coordinates(P,chart):
    out=[]
    for point,c in zip(P,chart):
        if c==0:
            if point is None:return None
            out.extend(point)
        elif point is None:out.extend([0,0])
        else:
            a,b=point
            if not b:return None
            out.extend([ff.div(a,b),ff.inv(b)])
    return out
records=[];outpath=w/'outputs'/f'verify_{sourcepath.stem}_collisions.json'
def save(status):
    result=dict(status=status,source=str(sourcepath),
       coefficient_field=str(K),sympy_version=sp.__version__,translation_certificates=translation_records,
       checks=records,elapsed_seconds=time.perf_counter()-started)
    outpath.write_text(json.dumps(result,indent=2)+'\n');return result
for chart in itertools.product(range(2),repeat=2):
    f=section(chart);a,b=derivative(f)
    base=[y*y+y+x**3,v*v+v+u**3,f]
    sections={g:section(chart,g) for g in kernel}
    for g in kernel:
        fg=sections[g];c,d=derivative(fg);equations=base+[fg,sp.expand(a*d+b*c)]
        tick=time.perf_counter();gb=sp.groebner(equations,x,y,u,v,domain=K,order='grevlex')
        known=candidate['P'] if g==G else (candidate['Q'] if g==minusG else None)
        coords=None if known is None else chart_coordinates(known,chart)
        if coords is None:passed=list(gb)==[1];remainders=[]
        else:
            assert list(gb)!=[1]
            remainders=[gb.reduce(var**32+coeff(ff.power(a,32)))[1] for var,a in zip((x,y,u,v),coords)]
            passed=all(r==0 for r in remainders)
        rec=dict(kind='pair_tangency',chart=chart,translation=g,
            expected_support='empty' if coords is None else coords,
            verified=passed,groebner_basis=[str(p.as_expr()) for p in gb.polys],
            coordinate_power32_remainders=[str(r) for r in remainders],seconds=time.perf_counter()-tick)
        records.append(rec);save('IN_PROGRESS')
        print(json.dumps({k:v for k,v in rec.items() if k not in ('groebner_basis','coordinate_power32_remainders')}),flush=True)
        if not passed:save('FAILED: unexpected nonnodal pair collision over algebraic closure')
        assert passed,'Unexpected nonnodal pair collision over algebraic closure'
    for g,h in itertools.combinations(kernel,2):
        tick=time.perf_counter();gb=sp.groebner(base+[sections[g],sections[h]],x,y,u,v,domain=K,order='grevlex')
        rec=dict(kind='triple_collision',chart=chart,translations=[g,h],unit_ideal=list(gb)==[1],
                 groebner_basis=[str(p.as_expr()) for p in gb.polys],seconds=time.perf_counter()-tick)
        records.append(rec);save('IN_PROGRESS')
        print(json.dumps({k:v for k,v in rec.items() if k!='groebner_basis'}),flush=True)
        if not rec['unit_ideal']:save('FAILED: unexpected triple collision over algebraic closure')
        assert rec['unit_ideal'],'Unexpected triple collision over algebraic closure'
out=save('PASS: exactly the certified simple tacnode and otherwise ordinary nodes')
print(json.dumps({k:v for k,v in out.items() if k not in ('checks','translation_certificates')},indent=2))
