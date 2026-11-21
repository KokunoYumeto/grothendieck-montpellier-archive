"""Exact standard-monomial/polytope and Koszul dimension checks for T053."""
from pathlib import Path
from itertools import product
import hashlib
import json
import sympy as sp
from charged_incidence_polytopes import polytopes,standard_monomials,compositions
from oscillator_charge_checks import basis,lowering

HERE=Path(__file__).resolve().parent


def tail_count(m,eta,k):
    if min(eta)<0:return 0
    return sum(all(sum(row[i] for row in rows)>=k for i in range(m))
               for rows in product(*(compositions(a,m) for a in eta)))


def satisfies(poly,w):
    return (all(lo<=x<=hi for lo,x,hi in zip(poly['lower_bounds'],w,poly['upper_bounds']))
            and all(sum(a*x for a,x in zip(row,w))==rhs for row,rhs in zip(poly['A_eq'],poly['b_eq']))
            and all(sum(a*x for a,x in zip(row,w))>=rhs for row,rhs in zip(poly['A_ge'],poly['b_ge'])))


def main():
    rows=[];witnesses=0;nullspaces=0;groebner_cases=0
    for m,r in ((3,1),(4,2),(5,3)):
        X=sp.symbols('x:'+str(r*m));Y=sp.symbols('y:'+str(m));s=sp.Symbol('s')
        diagonal=[X[a*m+a] for a in range(r)]
        variables=diagonal+[v for v in X if v not in diagonal]+list(Y)
        rel=[sum(X[a*m+i]*Y[i] for i in range(m)) for a in range(r)]
        gb=sp.groebner(rel,*variables,order='lex')
        assert len(gb.polys)==r
        assert {sp.expand(f.as_expr()) for f in gb.polys}==set(rel)
        family=[X[a*m+a]*Y[a]+s*sum(X[a*m+i]*Y[i] for i in range(m) if i!=a) for a in range(r)]
        gs=sp.groebner(family,*variables,order='lex',domain=sp.QQ.poly_ring(s))
        assert len(gs.polys)==r
        assert {sp.expand(f.as_expr()) for f in gs.polys}==set(map(sp.expand,family))
        groebner_cases+=2
        cap={1:10,2:4,3:2}[r]
        for eta in product(range(cap+1),repeat=r):
            if r==2 and sum(eta)>6:continue
            for k in range(sum(eta)//m+2):
                standard=standard_monomials(m,eta,k);polys=polytopes(m,eta,k)
                expected=sum((-1)**sum(mask)*tail_count(m,tuple(a-b for a,b in zip(eta,mask)),k)
                             for mask in product((0,1),repeat=r))
                assert len(standard)==expected,(m,eta,k,len(standard),expected)
                for mask,w in standard:
                    assert [i for i,p in enumerate(polys) if satisfies(p,w)]==[mask]
                    witnesses+=1
                # Check all ambient monomials, including every forbidden one.
                for rr in product(*(compositions(a,m) for a in eta)):
                    v=tuple(sum(row[i] for row in rr)-k for i in range(m))
                    w=sum(rr,())+v
                    memberships=sum(satisfies(p,w) for p in polys)
                    expected_membership=int(min(v)>=0 and not any(rr[a][a] and v[a] for a in range(r)))
                    assert memberships==expected_membership
                if len(basis(eta,m,k))<=125 and sum(eta)<=5:
                    C=sp.Matrix.vstack(*(lowering(eta,m,k,a) for a in range(r)))
                    assert len(standard)==len(basis(eta,m,k))-C.rank()
                    nullspaces+=1
                rows.append((m,r,eta,k,len(standard)))
    receipt={'statement':'T-053','status':'PASS','row_weight_cases':len(rows),
             'literal_standard_witnesses':witnesses,'literal_lowering_nullity_checks':nullspaces,
             'exact_quadratic_Groebner_checks':groebner_cases,
             'method':'literal standard monomials and complete tagged-polytope membership; independent alternating Koszul counts and direct lowering ranks; exact symbolic initial and parameter families',
             'sha256':hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()}
    (HERE/'CHARGED_INCIDENCE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
