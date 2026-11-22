#!/usr/bin/env python3
"""Exact circle-lift and three-point-fibre checks for the Hardt diagnostic.

AI-produced by GPT-6 Astra, OpenAI, 20 November 2026.
The code does not replace the properness or non-bundle proof.
"""
import json
import time
import sympy as sp

started = time.perf_counter()
s, lam = sp.symbols("s lam", real=True)
q = sp.Rational
cp = [(1,4*s), (2-4*s,1), (0,3-4*s), (4*s-3,0)]
bp = [3*s,2-3*s,3*s-2]
ap = [(1-lam)*s+lam*v for v in bp]
checks=[]

def exact(name, residual):
    r=sp.simplify(residual)
    checks.append({"name":name,"pass":r==0,"exact_residual":str(r)})

def point(piece,t):
    return tuple(sp.sympify(v).subs(s,t) for v in piece)

for i,t in enumerate([q(1,4),q(1,2),q(3,4)]):
    a,b=point(cp[i],t),point(cp[i+1],t)
    for j in [0,1]:
        exact(f"square_circle_join_{i+1}_coordinate_{j+1}",a[j]-b[j])
for j in [0,1]:
    exact(f"square_circle_identified_endpoints_coordinate_{j+1}",
          point(cp[0],0)[j]-point(cp[-1],1)[j])
exact("fold_left_endpoint",bp[0].subs(s,0))
exact("fold_right_endpoint",bp[-1].subs(s,1)-1)
exact("fold_first_join",bp[0].subs(s,q(1,3))-bp[1].subs(s,q(1,3)))
exact("fold_second_join",bp[1].subs(s,q(2,3))-bp[2].subs(s,q(2,3)))
exact("homotopy_left_endpoint",ap[0].subs(s,0))
exact("homotopy_right_endpoint",ap[-1].subs(s,1)-1)
for i,v in enumerate(ap):
    exact(f"homotopy_identity_slice_{i+1}",v.subs(lam,0)-s)
    exact(f"homotopy_terminal_slice_{i+1}",v.subs(lam,1)-bp[i])
    exact(f"homotopy_slope_{i+1}",sp.diff(v,s)-([1+2*lam,1-4*lam,1+2*lam][i]))
roots=[q(1,24),q(5,8),q(17,24)]
intervals=[(0,q(1,3)),(q(1,3),q(2,3)),(q(2,3),1)]
for i,(v,r,(lo,hi)) in enumerate(zip(bp,roots,intervals)):
    exact(f"inverse_fibre_value_{i+1}",v.subs(s,r)-q(1,8))
    checks.append({"name":f"inverse_fibre_unique_in_piece_{i+1}",
                   "pass":sp.solve(v-q(1,8),s)==[r] and bool(lo<r<hi),
                   "exact_root":str(r),"piece_open_interval":[str(lo),str(hi)]})
def cvalue(t):
    return point(cp[min(int(4*t),3)],t)
pts=[cvalue(r) for r in roots]
checks.append({"name":"three_inverse_circle_points_distinct",
               "pass":len(set(pts))==3,
               "exact_points":[[str(v) for v in p] for p in pts]})
checks.append({"name":"target_point_in_open_first_edge",
               "pass":cvalue(q(1,8))==(1,q(1,2)),
               "exact_point":[str(v) for v in cvalue(q(1,8))]})
report={"result":"A5.METHOD.HARDT_STRATUM", "status":"PASS" if all(c["pass"] for c in checks) else "FAIL",
        "exact_checks":len(checks),"runtime_seconds":time.perf_counter()-started,
        "scope":"Exact endpoints, slopes and complete three-point inverse-fibre calculation only; topology is proved in the note.",
        "checks":checks}
print(json.dumps(report,indent=2))
if report["status"]!="PASS":
    raise SystemExit(1)
