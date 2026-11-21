#!/usr/bin/env python3
"""D23.F27: exact non-Ferrari affine orbital calculation, retaining F9 tau."""
from pathlib import Path
import types,json,itertools

HERE=Path(__file__).resolve().parent;PENT=HERE.parent/'pentagon'
af=types.ModuleType('af')
exec((PENT/'affine_cubic_detector.py').read_text().split('S=(0,1,2,0)')[0],af.__dict__)
data=json.loads((PENT/'affine_cubic_detector.json').read_text())
s=tuple(data['s']);r=tuple(data['r']);x=tuple(data['x']);tau=af.am(s,r)
S=(0,1,2,0);R=(0,2,1,2);U=(1,1,0,1);L=(1,0,2,1)
shift=(0,2);H=(0,0,2,0,1,2);Hi=af.ai(H)
delta=(0,0)+af.mm(U,L);K=(2,0)+af.mm(U,U)
def project(a):
    assert all(j<3 for j in a[2:])
    M=a[2:];d=(a[0]%3,a[1]%3);m=af.mv(M,shift)
    return ((d[0]-shift[0]+m[0])%3,(d[1]-shift[1]+m[1])%3)+M

v=af.am(af.am(s,r),s)
assert project(r)==(2,2,0,2,1,2)
assert project(v)==(1,1,2,2,1,0)
assert project(x)==(0,0,2,1,0,2)
assert af.am(af.am(H,project(x)),Hi)==delta
assert af.am(af.am(H,project(v)),Hi)==K
assert af.am(af.am(tau,x),af.ai(tau))==x
assert af.am(af.am(tau,r),af.ai(tau))==v

linear_values=[af.I,S,(1,1,1,2)]
records=[];total=0
for rho,b in itertools.product(range(3),range(2)):
    fE=tuple(next(row['f'] for row in data['gentle_f_images']
                  if row['rho']==rho and row['a3']==b))
    Mrho=(1,rho,rho,(1+rho*rho)%3)
    CE=af.mm(af.mm(af.ap((0,0)+U,2)[2:],Mrho),af.ap((0,0)+U,-2)[2:])
    A0=tuple(af.mul(1 if b==0 else 2,z) for z in af.mi(CE))
    frames=[]
    for t0,t1 in itertools.product(range(9),repeat=2):
        AE=(t0,t1)+A0
        if af.am(af.am(AE,r),af.ai(AE))==af.am(af.ai(fE),r):frames.append(AE)
    assert len(frames)==9
    values=set()
    for AE in frames:
        Cf=af.am(af.ai(AE),af.ap(x,-3*b))
        rawg=af.am(af.am(tau,Cf),af.ai(tau))
        g=af.am(af.am(H,project(rawg)),Hi);values.add(g)
        for e in range(2):
            D=(0,0)+(af.I if e==0 else (2,0,0,2))
            q=delta
            for z0 in [D,af.ai(g),K,g,af.ai(D)]:q=af.am(q,z0)
            assert af.ap(q,3)==af.ID
            total+=1
    assert values=={(u,0)+linear_values[rho] for u in range(3)}
    records.append({'rho':rho,'b':b,'frame_count':9,
                    'g_values':sorted(values),'both_defect_signs_pass':True})

periodic=[]
for rho,M in enumerate(linear_values):
    g=(0,0)+M;Q=delta
    for z0 in [af.ai(g),K,g]:Q=af.am(Q,z0)
    N=Q[2:]
    assert N!=af.I and af.ap((0,0)+N,3)==af.ID
    NN=af.mm(N,N)
    assert all((af.I[j]+N[j]+NN[j])%3==0 for j in range(4))
    ell=next((u,v) for u,v in itertools.product(range(3),repeat=2)
             if (u or v) and
             ((u*N[0]+v*N[2]-u)%3,(u*N[1]+v*N[3]-v)%3)==(0,0)
             and (u*Q[0]+v*Q[1])%3==1)
    periodic.append({'rho':rho,'linear':list(N),'translation_for_positive_sign':list(Q[:2]),
                     'coinvariant_row':list(ell),'coinvariant':1})

out={'statement':'D23.F27','eta3_delta':delta,'eta3_K':K,
     'C14_conjugator':H,'tau_F9':tau,'frame_cases':records,
     'periodic_cases':periodic,'total_signed_frame_tests':total,
     'result':'PASS; both defect signs satisfy every tested periodic cube; no comparison conclusion.'}
(HERE/'orbital_affine216.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'total_signed_frame_tests':total,'frame_cases':len(records),
                  'g_values_per_case':3,'both_defect_signs_pass':True},indent=2))
