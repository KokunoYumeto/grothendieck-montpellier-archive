"""New b=-1 projector checks on previously certified actual units."""
from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
P=269
def add(a,b):return [(x+y)%P for x,y in zip(a,b)]
def scale(a,c):return [x*c%P for x in a]
def fmul(a,b):
    z=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%P
    for i in range(6,3,-1):
        z[i-4]=(z[i-4]-2*z[i])%P
        z[i-2]=(z[i-2]-4*z[i])%P
    return z[:4]
def fpow(a,n):
    z=[1,0,0,0]
    while n:
        if n&1:z=fmul(z,a)
        a=fmul(a,a);n//=2
    return z
def fcompose(a,b):
    z=[0]*4
    for x in reversed(a):
        z=fmul(z,b);z[0]=(z[0]+x)%P
    return z
A=[26,0,232,0];B=[143,123,169,39]
R=scale(fmul(B,fpow(A,P**4-2)),3)
assert fmul(A,fpow(A,P**4-2))==[1,0,0,0]
assert R==[263,135,266,252]
bw=[0,-3%P,0,-1%P]
orbit=[R]
for _ in range(3):orbit.append(fcompose(orbit[-1],bw))
proj=[0]*4
for j,v in enumerate(orbit):proj=add(proj,scale(v,(-1)**j))
assert proj==[245,0,257,0]
assert fcompose(proj,bw)==scale(proj,-1)

N=12
def tmul(a,b):
    z=[0]*N
    for i,x in enumerate(a):
        for j in range(N-i):z[i+j]=(z[i+j]+x*b[j])%P
    return z
def tcompose(a,b):
    z=[0]*N
    for x in reversed(a):
        z=tmul(z,b);z[0]=(z[0]+x)%P
    return z
unit=[268,129,65,73,150,86,265,238,76,236,114,116]
q=scale(unit,pow(unit[0],-1,P));q[0]=0
log=[0]*N;power=[1]+[0]*(N-1)
for n in range(1,N):
    power=tmul(power,q)
    log=add(log,scale(power,(-1)**(n+1)*pow(n,-1,P)))
assert log==[0,140,88,127,0,231,12,233,60,227,192,211]
nlog=[0 if n%3==0 else 3*log[n]%P for n in range(N)]
bu=[0,187,0,0,0,0,0,262,0,0,0,0]
orbit2=[nlog]
for _ in range(3):orbit2.append(tcompose(orbit2[-1],bu))
proj2=[0]*N
for j,v in enumerate(orbit2):proj2=add(proj2,scale(v,(-1)**j))
assert proj2==[0,0,249,0,0,0,0,0,182,0,152,0]
assert tcompose(proj2,bu)==scale(proj2,-1)
paths=[
Path("/tmp/alp_recovery_trace/research/conductor16_review/independent_raw_units_local_saturation.json"),
Path("/tmp/alp_recovery_trace/research/conductor16_quartic_strict/quartic_residue_local_certificate.json"),
Path("/tmp/alp_recovery_trace/research/conductor16_quartic_strict/selected_units_exact.json")]
out={"utc":datetime.now(timezone.utc).isoformat(),
     "status":"PASS_EXACT_NEW_QUADRATIC_PROJECTORS",
     "scope":"New b=-1 computations only; actual unit relations and full rational-denominator conversion retained from named already reviewed certificates.",
     "first_residue":{"A":A,"B":B,"three_B_over_A":R,
                      "global_b_orbit":orbit,"projector":proj,
                      "target":"Fp[w]/(w4+4w2+2), multiplied by uniformizer t; all two completions retained"},
     "second_residue":{"unit_mod_u12":unit,"normalized_log":log,
                       "cubic_corrected_log":nlog,"global_b_orbit":orbit2,
                       "projector":proj2,"target":"Fp[u]/u12 inside the unique e12f2 larger-cover completion"},
     "sources":[{"path":str(p),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths],
     "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
p=Path(__file__).with_suffix(".json");p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":out["status"],"first":proj,"second":proj2,
                  "sha256":hashlib.sha256(p.read_bytes()).hexdigest()},indent=2))
