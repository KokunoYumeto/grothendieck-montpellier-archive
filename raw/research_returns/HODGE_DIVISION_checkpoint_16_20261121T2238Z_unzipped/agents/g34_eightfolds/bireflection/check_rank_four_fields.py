#!/usr/bin/env python3
"""Exact small cyclotomic calculation in D-BI11, independent of group enumeration."""
from pathlib import Path
import sympy as S,json,hashlib
from sympy.polys.numberfields import to_number_field
from sympy.polys.polyerrors import IsomorphismFailed
x=S.symbols('x')
orders=[1,2,3,4,5,6,8,10,12]
expect={0:[1,2,3,4,6],2:[1,2,3,4,6,8],5:[1,2,3,4,5,6,10],
        -1:[1,2,3,4,6,8,12],-3:[1,2,3,4,6,12]}
radicands=[-1,-2,-3,-5,-6,-7,-10,-11,-15,-19,-30,-43,-67,-163]
expected_union={0:{-1,-3},2:{-1,-2,-3,-6},5:{-1,-3,-5,-15},
                -1:{-1,-2,-3},-3:{-1,-3}}

def main():
    records=[]
    for d,allowed in expect.items():
        root=S.sqrt(d) if d else None
        got=[]; union=set(); fields=[]
        for n in orders:
            poly=S.cyclotomic_poly(n,x)
            factors=S.factor_list(poly,extension=root)[1] if d else S.factor_list(poly)[1]
            degrees=[S.degree(f,x) for f,e in factors]
            if max(degrees)>2:continue
            got.append(n)
            zeta=S.expand_complex(S.exp(2*S.pi*S.I/n))
            generators=[zeta]+([root] if d else [])
            theta=to_number_field(generators)
            quadratic=[]
            for q in radicands:
                try:
                    a=to_number_field(S.sqrt(q),theta)
                    witness=S.Poly.from_list(a.coeffs(),x,domain=S.QQ)
                    modulus=S.Poly.from_list(theta.minpoly.all_coeffs(),x,domain=S.QQ)
                    assert (witness*witness-S.Poly(q,x)).rem(modulus).is_zero
                    quadratic.append(q)
                except IsomorphismFailed:pass
            union.update(quadratic)
            fields.append({'order':n,'cyclotomic_factor_degrees':list(map(int,degrees)),
                           'ambient_degree':int(theta.minpoly.degree()),
                           'imaginary_quadratic_radicands':quadratic})
        assert got==allowed,(d,got,allowed)
        assert union==expected_union[d],(d,union)
        records.append({'model_field_radicand':d,'allowed_orders':got,
                        'imaginary_quadratic_union':sorted(union),'fields':fields})
    out={'status':'PASS','records':records,
         'classification_or_group_claim_checked':False,
         'proof_explains_exhaustive_order_list':True,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','field_rows':len(records),'field_cases':sum(len(r['fields']) for r in records)}))
if __name__=='__main__':main()
