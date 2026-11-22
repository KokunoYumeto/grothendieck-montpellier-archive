"""Exhaust a precisely bounded integral-ratio dimension-ring subclass.

Class: common monic quadratic delta in Z[D], W of degree <=2,
G1=k1*W*delta, G2=k2*W*delta, S=k1*k2*W*delta^2,
k1 positive even and k2 positive odd integers. Require W>=D,
delta>=|delta_true|, Lambda_i>=lambda_i_true coefficientwise,
with required parity. Lambda is selected coefficientwise minimally
from the congruence needed for V_i. This is NOT global optimality.
"""
from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path('sources/OURS_counting_scripts').resolve()))
import consult_a157422a_dimension_ring_search as S
import dimension_ring_minimal_pairs as M

ROOT=Path('work/gct')
LIMIT=7276
CAP=4424+2*LIMIT
start=time.monotonic()

def qdict(p):
    a=S.to_q(p); m=len(a)//2
    return {j-m:v for j,v in enumerate(a) if v}

def sym_q_to_D(a):
    # q^j+q^-j satisfies C_j=(D-2)C_(j-1)-C_(j-2).
    cs=[[2],[-2,1]]
    for j in range(2,len(a)):
        cs.append(S.sub(S.mul([-2,1],cs[-1]),cs[-2]))
    out=[a[0]]
    for j in range(1,len(a)):
        out=S.add(out,[a[j]*v for v in cs[j]])
    return S.trim(out)

def min_lam(ki,kj,W,lamtrue,K):
    upper=S.sub([ki*v for v in S.mul(S.D,W)],[kj*v for v in K])
    uq,tq=qdict(upper),qdict(lamtrue)
    deg=max([0]+list(uq)+list(tq))
    vals=[]
    for j in range(deg+1):
        x=tq.get(j,0); u=uq.get(j,0)
        if (u-x)%2:return None
        v=x+(u-x)%(2*kj)
        if v>u:return None
        vals.append(v)
    lam=sym_q_to_D(vals)
    V=S.divexact(S.sub([ki*v for v in S.mul(S.D,W)],lam),[kj])
    assert V is not None and S.ge_abs(lam,lamtrue) and S.ge_abs(V,K)
    return lam,V

# Positivity and the score cap imply w<=36 and delta(4)<=26.
Ws=[]
for c2 in range(0,18,2):
 for c1 in range(1,18,2):
  for c0 in range(2,37,2):
   w=c0+2*c1+2*c2
   if w<=36:Ws.append((w,sym_q_to_D([c0,c1,c2])))
deltas=[]
for a in range(7):
 for b in range(14):
  d=4+4*a+2*b
  if d<=26:deltas.append((d,[2*b-4*a,-3+2*a,1]))

best=[]; tested=0; structural=0
for k1 in range(2,54,2):
 for k2 in range(1,54,2):
  for d,delta in deltas:
   for w,W in Ws:
    lower=k1*k2*w*d*d+20*w*d*(k1+k2)+200*w+800+164*d
    if lower>CAP:continue
    tested+=1
    U1=S.divexact(S.sub([k1*v for v in W],S.D),[k2])
    U2=S.divexact(S.sub([k2*v for v in W],S.D),[k1])
    if U1 is None or U2 is None or not S.ge_abs(U1,S.D) or not S.ge_abs(U2,S.D):continue
    WD=S.mul(W,delta)
    G1=[k1*v for v in WD];G2=[k2*v for v in WD]
    Sc=[k1*k2*v for v in S.mul(W,S.mul(delta,delta))]
    if not S.ge_abs(G1,S.g1) or not S.ge_abs(G2,S.g2) or not S.ge_abs(Sc,S.s0):continue
    L1=min_lam(k1,k2,W,S.l1true,S.K1)
    L2=min_lam(k2,k1,W,S.l2true,S.K2)
    if L1 is None or L2 is None:continue
    structural+=1
    la1,v1=L1;la2,v2=L2
    par={'S':Sc,'G':{1:G1,2:G2},'W':W,'delta':{1:delta,2:delta},'Lam':{1:la1,2:la2}}
    score=M.score(par)
    assert score is not None
    if score[0]<=LIMIT:
      result={'score':score,'k1':k1,'k2':k2,'W':W,'delta':delta,'Lambda1':la1,'Lambda2':la2,'G1':G1,'G2':G2,'S':Sc,'U1':U1,'U2':U2,'V1':v1,'V2':v2}
      best.append(result)
      print('CANDIDATE',json.dumps(result),flush=True)
      if score[0]<LIMIT:
        LIMIT=score[0];CAP=4424+2*LIMIT
        (ROOT/'dimension_ratio_best.json').write_text(json.dumps(result,indent=2))
result={'seconds':time.monotonic()-start,'tested_after_eval_bound':tested,'structurally_valid':structural,'minimum':LIMIT,'candidates':best,'scope':'fixed integral-ratio class only; see script docstring'}
(ROOT/'dimension_ratio_results.json').write_text(json.dumps(result,indent=2))
print('DONE',json.dumps({k:v for k,v in result.items() if k!='candidates'}),flush=True)
