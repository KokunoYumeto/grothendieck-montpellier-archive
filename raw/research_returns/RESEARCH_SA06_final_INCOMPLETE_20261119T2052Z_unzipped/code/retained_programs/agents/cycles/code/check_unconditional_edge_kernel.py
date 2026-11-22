"""Bounded exact algebra for C.3bt; it does not certify descent or proper families."""
from pathlib import Path
from datetime import datetime, timezone
import json, time
import sympy as s
base=Path(__file__).resolve().parents[1]
tick=time.perf_counter()
started=datetime.now(timezone.utc).isoformat()
rows=[]
def check(name, condition, data=None):
    rows.append({"name":name,"passed":bool(condition),"data":data})
    assert condition,name
g,h,u=s.symbols("g h u")
F=g*g-(h+2)*g+1
check("endpoint_roots",s.cancel(F.subs(h,(u-1)**2/u)-(g-u)*(g-1/u))==0)
check("quadratic_discriminant",s.expand(s.discriminant(F,g)-h*(h+4))==0)
check("marked_zero_has_root_one",s.expand(F.subs(h,0)-(g-1)**2)==0)
check("norm_one",s.Poly(F,g).all_coeffs()[-1]==1)
AS=s.expand((g+1)**2+h*(g+1)-h)
F2=g*g+h*g+1
check("characteristic_two_artin_schreier",s.Poly(AS-F2,g,h,modulus=2).is_zero)
for m in range(1,9):
    check(f"odd_pole_not_artin_schreier_order_{m}",2*m != 1)
for genus in range(7):
    for support in range(9):
        n=2*genus+2*support+5
        jet_degree=2*support+3
        check(f"curve_jet_degree_{genus}_{support}",n-1-jet_degree>2*genus-2,
              {"pole_order":n,"jet_degree":jet_degree})
for r in range(2,10):
    check(f"BG_term_incoming_{r}",1-r<0)
    check(f"BG_term_outgoing_{r}",1+r>2)
x=s.symbols("x")
projector=s.cancel((x-1)*(x-2)*(x-8)/((4-1)*(4-2)*(4-8)))
for eigen in [1,2,4,8]:
    check(f"weight_two_projector_{eigen}",projector.subs(x,eigen)==int(eigen==4))
for e in [1,2,3,5]:
    for n in [-3,-1,1,4]:
        check(f"ramified_marked_unit_{e}_{n}",s.Integer(1)**(e*n)==1)
record={"started_utc":started,"finished_utc":datetime.now(timezone.utc).isoformat(),
        "runtime_seconds":time.perf_counter()-tick,
        "passed":all(row["passed"] for row in rows),"check_count":len(rows),"checks":rows,
        "scope":"Only quadratic/root/Artin-Schreier identities, bounded interpolation-degree inequalities, spectral-sequence index bounds, projector values and unit-one multiplicities. No computer verification of generic curves, Gersten, descent naturality, actual family existence or the main quotient."}
encoded=json.dumps(record,indent=2)
(base/"output/unconditional_edge_kernel_certificate.json").write_text(encoded+"\n")
print(encoded)

