"""Exploratory exact Mumford coordinates of the Q8 norm-seven theta map.

This script makes no geometric conclusion. All output, including any
coefficient-domain failure, is retained separately from the certificate.
"""
from pathlib import Path
import datetime
import json
import time
import traceback
from sympy import Poly, symbols
from sympy.polys.domains import GF
from sympy.polys.agca.extensions import MonogenicFiniteExtension
from sympy.polys.rings import ring

start = time.perf_counter()
root = Path(__file__).resolve().parent.parent
result = {"status": "RUNNING"}
try:
    rr, tt, bb, ww = symbols("r t beta w")
    base = GF(2).frac_field(rr)
    Kt = MonogenicFiniteExtension(Poly(tt**2+tt+rr**2, tt, domain=base))
    zexpr = (rr**2+1)/rr**3
    Kb = MonogenicFiniteExtension(Poly(bb**2+bb+zexpr+1, bb, domain=Kt))
    ftexpr = (rr**4+rr**3+rr+1)/rr**3*tt+(rr**3+rr**2+1)/rr
    K = MonogenicFiniteExtension(Poly(ww**2+ww+ftexpr, ww, domain=Kb))
    # Each triangular extension is used as a field; SymPy leaves its generic
    # Domain.gcd unimplemented. The field gcd is one for nonzero input.
    for domain in (Kt, Kb, K):
        domain.gcd = lambda x,y,domain=domain: domain.one if x or y else domain.zero
    Rp, pp = ring("p", K)
    FF = Rp.to_field()
    p = FF.gens[0]
    const = lambda expr: FF(K.from_sympy(expr))
    r,t,beta,w = map(const, (rr,tt,bb,ww))
    z = (r**2+1)/r**3
    a,b,D = z**2,z**2+z+1,r**2
    u,v = z*(t+r),z*t**2+t+1/D
    gp = z*p**2+(z+1)*p+beta
    hp = u*p**2+v*p+w
    d1 = a*p**4+b*p**2
    cg = z*D+t
    Z = hp+t**2*gp+D*d1+t*cg
    c = D*cg
    E = t*gp+hp+(t+1)*cg
    A3 = (Z*E+c*cg)/D
    A2 = (Z+c)*gp+c*d1+A3
    ell = p+A3**2/(a*Z**2)
    kappa = (b+a*(D+1))/a
    tau = c/Z
    cx = kappa+tau**2
    dd = p*ell+p**2+cx
    n1 = tau*d1+(A2/Z)*ell+(A3/Z)*(ell**2+cx)
    n0 = cx*((A2/Z)+(A3/Z)*ell)
    nu = (n0+tau*n1)/(cx+tau*ell+tau**2)
    eta_minus_y = n1+nu*(ell+tau)+nu*p
    Z0 = w+t**2*beta+t*cg
    E0 = w+t*beta+(t+1)*cg
    q0 = (E0**2+Z0)/D**2
    assert ell == Z/(a*D**2)+q0/a+cg**4/(a*Z**2)
    result = {
        "status": "PASS_EXPLORATORY",
        "ell": str(ell),
        "constant": str(dd),
        "nu": str(nu),
        "eta_minus_y": str(eta_minus_y),
        "q0": str(q0),
        "degrees": {
            "ell": [ell.numer.degree(),ell.denom.degree()],
            "constant": [dd.numer.degree(),dd.denom.degree()],
            "nu": [nu.numer.degree(),nu.denom.degree()],
            "eta_minus_y": [eta_minus_y.numer.degree(),eta_minus_y.denom.degree()],
        },
        "scope": "Rational Mumford coordinates only; no fibre-size or nodality conclusion.",
    }
except Exception:
    result = {"status": "EXPLORATORY_SETUP_OR_CALCULATION_FAILURE", "traceback": traceback.format_exc()}
finally:
    result["actual_timestamp_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result["runtime_seconds"] = time.perf_counter()-start
    out = root / "outputs/explore_seven_residual_coordinates.json"
    out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
