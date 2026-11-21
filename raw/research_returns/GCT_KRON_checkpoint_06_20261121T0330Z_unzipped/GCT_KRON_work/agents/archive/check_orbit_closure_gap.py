from pathlib import Path
import sys,json,datetime
from fractions import Fraction
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"computations"))
from independent_characters import character,partitions,z_type,kronecker

def square_cycle(c):
    return tuple(sorted([x//2 if x%2==0 else x for x in c for _ in range(2 if x%2==0 else 1)],reverse=True))

def symmetric_coefficient(lam,mu):
    v=sum((Fraction(character(lam,c)*(character(mu,c)**2+character(mu,square_cycle(c))),2*z_type(c)) for c in partitions(sum(lam))),Fraction(0))
    assert v.denominator==1
    return v.numerator

out=[]
for h in range(2,8):
    lam=(h,h,h);mu=(3,)*h
    count=sum(1 for a in range(h//2+1) for b in range(h//3+1) for c in range(h//4+1) if 2*a+3*b+4*c==h)
    g=kronecker(lam,mu,mu);sk=symmetric_coefficient(lam,mu)
    assert g==count
    assert sk==(count if h%2==0 else 0)
    out.append({"h":h,"g":g,"sk":sk,"positive_count":count})
r={"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"engine":"Exact Murnaghan-Nakayama; symmetric-square character (chi(s)^2+chi(s^2))/2","status":"PASS","rows":out}
Path(__file__).with_name("ORBIT_CLOSURE_GAP_CERTIFICATE.json").write_text(json.dumps(r,indent=2)+"\n")
print(json.dumps(r))
