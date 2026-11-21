#!/usr/bin/env python3
"""Independent rebuild of sibling nodal multiplication minors with Sympy Poly.
Does not import the sibling's polynomial or elimination implementation.
"""
from pathlib import Path
import json
import sympy as s

x=s.Symbol('x')
root=Path(__file__).resolve().parent.parent/'imprimitive'
cases=json.loads((root/'nodal_rank_certificate.json').read_text())+json.loads((root/'additional_rank_certificates.json').read_text())
results=[]
for c in cases:
    p=c['prime'];d=c['d'];z=c['zeta_mod_prime'];g=c['g']
    assert pow(z,d,p)==1 and all(pow(z,k,p)!=1 for k in range(1,d))
    pairs=c.get('node_pairs_integer',c.get('node_pairs'))
    pairs=[(a%p,b%p)for a,b in pairs]
    points=[a for pair in pairs for a in pair]
    assert len(set(points))==2*g
    D=s.Poly(s.prod(x-a for a in points),x,modulus=p)
    partial={a:D.exquo(s.Poly(x-a,x,modulus=p))for a in points}
    if c.get('construction')=='two_branch_points':
        e=c['e'];f=[];h=[]
        for j,(a,b) in enumerate(pairs,1):
            q=z*pow(2*j+1,-e,p)%p
            q2=b*pow(a,-1,p)*pow(q,-1,p)%p
            assert pow(q,d,p)==pow(b*pow(a,-1,p),e,p)
            f.append(partial[a]-partial[b].mul_ground(q))
            h.append(partial[a]-partial[b].mul_ground(q2))
    else:
        exponents=c.get('gluing_exponents',[1]*g)
        def forms(zz):
            ff=[partial[a]-partial[b].mul_ground(pow(zz,e,p))for(a,b),e in zip(pairs,exponents)]
            if exponents[0]==0:return [ff[0]]+[ff[j]-ff[-1]for j in range(1,g-1)]
            return [ff[j]-ff[-1]for j in range(g-1)]
        f=forms(z);h=forms(pow(z,-1,p))
    products=[a*b for a in f for b in h]
    minor=[[int(products[j].nth(i))%p for j in c['column_ids_zero_based']]for i in c['row_ids_zero_based']]
    assert minor==c['minor']
    residue=int(s.Matrix(minor).det())%p
    assert residue==c['minor_determinant_mod_prime']and residue!=0
    results.append({'d':d,'e':c.get('e'),'g':g,'construction':c.get('construction','unramified'),'minor_size':len(minor),'determinant_mod_1009':residue,'matrix_match':True})
out=Path(__file__).with_name('imprimitive_peer_audit_result.json')
out.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
