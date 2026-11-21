"""Independent finite checks of the proposed SL2 determinant-jet calculation.

Construct actual tridiagonal pencil cofactors by continuants, expand in
(t,h,e,f), multiply by all four variables and rank the truncated coefficient
matrix modulo a prime. This does not assume the harmonic/Jacobi proof.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json
import numpy as np

def add(p, q, scale=1):
    out = dict(p)
    for a, c in q.items():
        out[a] = out.get(a, 0) + scale*c
        if not out[a]: del out[a]
    return out

def mul(p, q, truncate=3):
    out = {}
    for a, x in p.items():
        for b, y in q.items():
            c = tuple(i+j for i,j in zip(a,b))
            if c[0] <= truncate: out[c] = out.get(c, 0) + x*y
    return {a:c for a,c in out.items() if c}

ONE={(0,0,0,0):1}
EF={(0,0,1,1):1}

def cofactors(m):
    d=[{(1,0,0,0):1, (0,1,0,0):m-1-2*i} for i in range(m)]
    lead=[ONE, d[0]]
    for k in range(2,m+1):
        lead.append(add(mul(d[k-1],lead[-1]),mul(EF,lead[-2]),-(k-1)*(m-k+1)))
    trail=[None]*(m+1); trail[m]=ONE; trail[m-1]=d[-1]
    for i in range(m-2,-1,-1):
        trail[i]=add(mul(d[i],trail[i+1]),mul(EF,trail[i+2]),-(i+1)*(m-1-i))
    out=[]
    for i in range(m):
        for j in range(m):
            lo=min(i,j); hi=max(i,j)
            scale=(-1)**(i+j)
            if i<j:
                for z in range(i,j):scale*=z+1
                factor={(0,0,j-i,0):scale}
            elif i>j:
                for z in range(j,i):scale*=m-1-z
                factor={(0,0,0,i-j):scale}
            else:factor=ONE
            out.append(mul(mul(lead[lo],trail[hi+1]),factor))
    return out

def rank_mod(A,p):
    A=A.copy();r=0
    for c in range(A.shape[1]):
        nz=np.flatnonzero(A[r:,c])
        if not len(nz):continue
        k=r+int(nz[0]);A[[r,k]]=A[[k,r]]
        A[r,c:]=(A[r,c:]*pow(int(A[r,c]),-1,p))%p
        for start in range(r+1,A.shape[0],128):
            end=min(A.shape[0],start+128)
            A[start:end,c:]=(A[start:end,c:]-A[start:end,c,None]*A[r,c:])%p
        r+=1
        if r==A.shape[0]:break
    return r

def run(m,p):
    mons=[(t,h,e,m-t-h-e) for t in range(min(3,m)+1) for h in range(m-t+1) for e in range(m-t-h+1)]
    idx={a:i for i,a in enumerate(mons)}
    A=np.zeros((len(mons),4*m*m),dtype=np.int64)
    for j,C in enumerate(cofactors(m)):
        for variable in range(4):
            for a,c in C.items():
                b=list(a);b[variable]+=1;b=tuple(b)
                if b in idx:A[idx[b],4*j+variable]=c%p
    rk=rank_mod(A,p)
    return {'m':m,'prime':p,'rows':len(mons),'columns':4*m*m,'rank':rk,'full_jet_rank':rk==len(mons),'matrix_sha256':hashlib.sha256(A.tobytes()).hexdigest()}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--max-m',type=int,default=16);ap.add_argument('--prime',type=int,default=1000003);args=ap.parse_args()
    rows=[]
    for m in range(2,args.max_m+1):
        row=run(m,args.prime);rows.append(row);print(json.dumps(row),flush=True)
        Path(__file__).with_name('sl2_jet_checks.json').write_text(json.dumps({'checked_utc':datetime.now(timezone.utc).isoformat(),'method':'exact modular rank of actual expanded tridiagonal cofactors, finite corroboration only','rows':rows},indent=2)+'\n')
        if not row['full_jet_rank']:raise SystemExit('FAILED')
