"""Exact edge-coefficient explanation for inherited F57, INT-NSRH-4, F67.

The inherited obstructions are inputs, not newly claimed discoveries.
The new output records their common binomial coefficient transfer and the
three complete D-polynomials behind the INT-NSRH-4 coordinates.
"""
from pathlib import Path
import json
import sys
import sympy as s

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/"dependencies"))
import e4lib as h

D,t = s.symbols("D t")


def from_laurent(p):
    top = max(p)
    eps = top%2
    rem = dict(p)
    f = 0
    for n in range(top,eps-1,-2):
        c = rem.get(n,0)
        if c:
            f += c*D**((n-eps)//2)
            term = {2*j-n:int(s.binomial(n,j)) for j in range(n+1)}
            rem = h.padd(rem,term,-c)
    assert not rem
    return eps,s.expand(f)


def expand(eps,f):
    out = {}
    for (j,),a in s.Poly(f,D).terms():
        n = 2*j+eps
        out = h.padd(out,{n-2*k:int(a*s.binomial(n,k)) for k in range(n+1)})
    return out


def inspect(name,eps,f,expected=None):
    P = s.Poly(f,D)
    m = P.degree()
    L = 2*m+eps
    p = expand(eps,f)
    if expected is not None:
        assert p == expected
    # Check the coefficient-transfer identity at every exponent.
    for r in range(L+1):
        c = sum(P.nth(m-k)*s.binomial(L-2*k,r-k)
                for k in range(min(r,m)+1)
                if 0 <= r-k <= L-2*k)
        assert c == p.get(L-2*r,0)
    assert all(p.get(-e,0) == c for e,c in p.items())
    return {"name":name,"epsilon":eps,"D_polynomial":str(f),
            "top_exponent":L,"leading_D_coefficients":[int(P.nth(m)),int(P.nth(m-1))],
            "outer_Laurent_coefficients":[p.get(L,0),p.get(L-2,0)],
            "negative_exponents":sorted(e for e,c in p.items() if c<0),
            "Laurent_coefficients":{str(e):c for e,c in sorted(p.items())}}


def whole_output(m,a,n,b):
    N1=s.Matrix([[m,a],[0,0]])
    N2=s.Matrix([[0,0],[a,m]])
    L1=s.Matrix([[n,b],[0,0]])
    L2=s.Matrix([[0,0],[b,n]])
    Rs=[s.kronecker_product(N,L)+s.kronecker_product(m*s.eye(2)-N,n*s.eye(2)-L)
        for N,L in [(N1,L1),(N2,L2)]]
    trace=s.Poly(s.expand(s.trace(Rs[0]*Rs[1])),t)
    assert all(j%2==0 for (j,),c in trace.terms())
    return s.expand(sum(c*D**(j//2) for (j,),c in trace.terms()))


def main():
    omega=(2,3,2,3,2,3,1,2,1,2,1)
    co=h.dualcoords(h.word_elt(omega))
    pairs=[("2013","3201"),("2013","3021"),("2103","3021")]
    bad={k for k,p in co.items() if any(c<0 for c in p.values())}
    intended=set()
    out=[]
    for a,b in pairs:
        aa,bb=tuple(map(int,a)),tuple(map(int,b))
        intended.update([(aa,bb),(bb,aa)])
        p=co[(aa,bb)]
        assert p==co[(bb,aa)]
        eps,f=from_laurent(p)
        out.append(inspect("INT-NSRH-4 "+a+","+b,eps,f,p))
    assert bad==intended
    f57=-D**9+20*D**8-163*D**7+734*D**6-2048*D**5+3712*D**4-4352*D**3+3072*D**2-1024*D
    out.append(inspect("GCT_NSRH F57",0,f57))
    f67=whole_output(t**3,3*t**2-4,t**3,3*t**2-4)
    assert s.expand(f67-(D**6+(-D**3+18*D**2-48*D+32)**2))==0
    out.append(inspect("GCT_NSRH F67 three-plus-three",0,f67))
    f13=whole_output(t,1,t**3,3*t**2-4)
    assert f13==2*D**4-20*D**3+84*D**2-128*D+64
    out.append(inspect("GCT_NSRH F67 one-plus-three",0,f13))
    result={"status":"PASS","coordinate_convention":"zero-based one-line permutations for INT-NSRH-4", "cases":out}
    (HERE/"edge_coefficients_verified.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","edges":{r["name"]:r["outer_Laurent_coefficients"] for r in out}},indent=2))


if __name__=="__main__":
    main()
