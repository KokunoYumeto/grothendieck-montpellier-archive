"""Exact certificate for the characteristic-two very ample H1 example.

The script constructs an ordered GF(2) basis of H0(S,Q^9) in the explicit
Raynaud affine chart y^2+y=x^15, z^3=w^2+x.  The section polynomial is
sum f_ij(x,y) w^j z^i.  Pole/transition constraints at the missing base
point and section at infinity are exact finite linear equations, not
sampled point tests. Generic branch coefficients remain independent
indeterminates; their smooth SNC locus is proved by Bertini in the paper.
"""
from pathlib import Path
from math import comb
from collections import Counter
import json,time,hashlib
from search_raynaud_cech import power
root=Path(__file__).resolve().parents[1]

def nullspace_gf2(rows,n):
    basis={}
    for row in rows:
        while row:
            p=(row&-row).bit_length()-1
            if p in basis:row^=basis[p]
            else:basis[p]=row;break
    pivots=sorted(basis)
    free=[j for j in range(n) if j not in basis]
    kernels=[]
    for f in free:
        vec=1<<f
        for p in reversed(pivots):
            if ((basis[p]&vec).bit_count()&1):vec|=1<<p
        assert all((row&vec).bit_count()%2==0 for row in rows)
        kernels.append(vec)
    return len(pivots),kernels

def section_basis(i):
    a=6-i;b=9+2*i
    # w_U=t^6*w_V+t^-1, z_U=t^4*z_V, Q^9 base frame t^-18.
    # Downward substitution gives pole(f_j)<=2*b+7*a-j.
    variables=[(j,r,s) for j in range(a+1) for s in [0,1]
               for r in range(max(-1,(2*b+7*a-j-15*s)//2)+1)]
    precision=(7*a)//15+2
    unit=[1]+[0]*precision
    for _ in range(precision+1):unit=[1]+power(unit,-7,2,precision)[:precision]
    assert unit==[1]+power(unit,-7,2,precision)[:precision]
    powers={r+8*s:power(unit,r+8*s,2,precision) for j,r,s in variables}
    equations={}
    for col,(j,r,s) in enumerate(variables):
        pole=2*r+15*s
        for h in range(j+1):
            if comb(j,h)%2==0:continue
            for k,value in enumerate(powers[r+8*s]):
                exponent=2*b+7*h-j-pole+15*k
                if value and exponent<0:equations[(h,exponent)]=equations.get((h,exponent),0)^(1<<col)
    rank,kernels=nullspace_gf2(list(equations.values()),len(variables))
    sections=[]
    for vec in kernels:
        sections.append([dict(x=r,y=s,w=j,z=i) for col,(j,r,s) in enumerate(variables) if (vec>>col)&1])
    # Independent dimension from the filtration by N^(b+3j), degree2.
    expected=sum(2*(b+3*j)+1-7 for j in range(a+1))
    assert len(sections)==expected
    return dict(i=i,a=a,b=b,variables=len(variables),equations=len(equations),rank=rank,
                dimension=len(sections),riemann_roch_dimension=expected,
                series_precision_in_t15=precision,sections=sections)

if __name__=='__main__':
    start=time.monotonic();parts=[section_basis(i) for i in range(3)]
    sections=[s for part in parts for s in part['sections']]
    assert len(sections)==556
    basis_file=root/'code/A3_Q9_basis.json'
    basis_file.write_text(json.dumps(dict(field='GF(2)',chart_relations=['y^2+y=x^15','z^3=w^2+x'],section_format='Each section is the sum of the listed monomials x^a y^b w^c z^d, with coefficient1.',sections=sections),separators=(',',':'))+'\n')
    p=2;ell=3;r=8;D=6;Ndegree=2;g=7
    assert (p-1)*(p*r-2)//2==g and p*D==2*g-2
    assert p*(D+1)+1-p==13>p*D
    positive=[dict(i=i,projective_power=(2+i)//ell-i,base_N_power=2*i+1) for i in range(ell)]
    negative=[]
    for i in range(ell):
        projective_power=-i-(1 if i<2 else 0)
        if projective_power<=-2:
            negative.append(dict(i=i,symmetric_dual_power=-projective_power-2,base_N_power=2*i-1-3))
    assert negative==[{'i':1,'symmetric_dual_power':0,'base_N_power':-2},{'i':2,'symmetric_dual_power':0,'base_N_power':0}]
    degree=9**556
    out=dict(scope=__doc__,seconds=round(time.monotonic()-start,6),curve=dict(p=p,equation='y^2+y=x^15',genus=g,pole_orders={'x':2,'y':15},t='y/x^8',degD=D,degN=Ndegree,ord_dx=12,ord_x_minus_t_minus2=13),
             positive_pushforward=positive,negative_R1_summands=negative,
             H0_Q=6,H1_Q_inverse=1,Q_square=16,K_dot_Q=20,chi_O=-2,H1_O=9,
             Q9_basis_parts=[{k:v for k,v in a.items() if k!='sections'} for a in parts],
             Q9_basis_file=str(basis_file.relative_to(root)),Q9_basis_sha256=hashlib.sha256(basis_file.read_bytes()).hexdigest(),
             root_count=556,root_order=9,cover_degree=str(degree),cover_degree_mod2=degree%2,
             H0_new_L=562,H1_new_L_inverse=1,H1_new_O=565,
             exact_scope='All finite coefficients and transition equations verified over GF(2). Smoothness, connectedness, generic branch transversality and very ampleness follow from the full arguments in the paper, not enumeration of the enormous cover.')
    (root/'code/certify_A3_output.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
