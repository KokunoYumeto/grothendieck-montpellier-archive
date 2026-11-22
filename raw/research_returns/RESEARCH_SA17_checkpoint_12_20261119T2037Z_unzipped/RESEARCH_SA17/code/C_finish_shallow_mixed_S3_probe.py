"""Focused exact curvature test for L012,+ + L012,- and Q,+ + Q,-.

Exhaust all opposite-arrow parameters, then a bounded deterministic sample
including the two other tangent blocks.  No additivity or class-vanishing
conclusion is inferred from a zero detector output.
"""
from pathlib import Path
from itertools import product
from time import perf_counter
import random
import json
import numpy as np
exec(Path('code/C_finish_shallow_curvature_probe.py').read_text().split('\nroots=[')[0])
start=perf_counter()

def tensorI2(A):
    return [[A[i//2][j//2] if i%2==j%2 else zero for j in range(6)] for i in range(6)]
D=mat([[1,0,0],[0,zeta,0],[0,0,power(zeta,2)]])
BF=mat([[0,1,pi],[pi,1,0],[neg(pi),1,0]])
BQ=mat([[0,0,1],[pi,1,F(-1,2)],[pi,-1,F(-1,2)]])
I=ident(6);In=np.eye(6,dtype=np.int64)
N=np.zeros((6,6),dtype=np.int64);N[:2,2:4]=np.eye(2,dtype=np.int64)
rng=random.Random(202611191846)
arrows=[(0,0,a,b,c,d,0,0) for a,b,c,d in product(range(3),repeat=4)]
extra={tuple(rng.randrange(3) for _ in range(8)) for _ in range(500)}-set(arrows)
runs=[];detected=[];total=primary_cases=0
for name,B,signs in [('L012_plus_minus',BF,[-1,1,1,-1,1,-1]),
                      ('Q_plus_minus',BQ,[1,-1,-1,1,1,-1])]:
    T0=tensorI2(conjugate(D,B));sg=np.diag(signs);S=mat(sg.tolist())
    assert mm(mm(T0,T0),T0)==I and mm(mm(S,T0),S)==mm(T0,T0)
    assert np.array_equal(np.array([[residue(x) for x in row] for row in T0]),In+N)
    def invol(U):return -sg@(In-N)@U@(In-N)@sg%3
    count=nz=0
    for scope,pars,ms in [('all_opposite_arrow_classes',arrows,(3,4,5)),
                         ('deterministic_full_tangent_sample',sorted(extra),(3,5))]:
        subtotal=snz=0
        for par in pars:
            W=np.zeros((6,6),dtype=np.int64)
            W[2,3],W[3,2]=par[:2]
            if name.startswith('L012'):
                W[2,5],W[3,4]=par[2:4];W[4,0],W[5,1]=par[4:6]
            else:
                W[2,4],W[3,5]=par[2:4];W[4,1],W[5,0]=par[4:6]
            W[4,5],W[5,4]=par[6:]
            U=(2*(W+invol(W)))%3
            assert np.array_equal(invol(U),U) and not np.any(N@U@N%3)
            for m in ms:
                T=ma(T0,scale(mat(U.tolist()),power(pi,m-1)))
                cube=ma(mm(mm(T,T),T),mn(I))
                conjugacy=ma(mm(mm(S,T),S),mn(mm(T,T)))
                assert all(valuation(x)>=m for row in cube for x in row)
                assert all(valuation(x)>=m for row in conjugacy for x in row)
                C=scale(cube,power(pi,-m));d=ma(T,mn(I))
                assert mm(C,d)==mm(d,C)
                vals,lengths=smith_curvature(d,C,m)
                relevant={str(q):v for q,v in lengths.items() if q!=(1,0)}
                if relevant:snz+=1
                bad={q:v%m for q,v in relevant.items() if v%m}
                if bad:detected.append({'baseline':name,'parameters':par,'m':m,'smith_exponents':vals,
                                       'primary_lengths':relevant,'nonzero_residues':bad})
                subtotal+=1
        count+=subtotal;nz+=snz
        runs.append({'baseline':name,'scope':scope,'gauge_parameters':len(pars),'truncations':list(ms),
                     'actual_S3_actions':subtotal,'nonzero_primary_cases':snz})
        print(name,scope,'completed',subtotal,'actions; detections',len(detected),flush=True)
    total+=count;primary_cases+=nz
report={'status':'BOUNDED SEARCH COMPLETE',
 'scope':'The two minimal opposite-signed rank6 constant baselines. All81 pure opposite-arrow tangent classes at m3,4,5, plus a fixed-seed full-tangent sample at m3,5. Actual cubic and transposition identities modulo pi^m, exact Q(zeta3) Smith transformations and every curvature-primary composition length. Zero output is not a Swan-class vanishing theorem or a solution of the shallow residue-torsion case.',
 'runs':runs,'actual_S3_actions':total,'nonzero_primary_cases':primary_cases,
 'detections':detected,'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_shallow_mixed_S3_probe.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
