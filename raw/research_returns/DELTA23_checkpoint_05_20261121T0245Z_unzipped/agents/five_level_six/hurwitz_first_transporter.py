#!/usr/bin/env python3
from pathlib import Path
import numpy as np,json,pickle,time
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).parent;PENT=HERE.parent/'pentagon'
def perm(a):return Permutation(np.asarray(a).tolist())
def powp(a,k):
 r=np.arange(len(a))
 for _ in range(k):r=a[r]
 return r

def main():
 start=time.monotonic()
 A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators']; n=len(A);I=np.arange(n)
 with (HERE/'hurwitz_first_P.pkl').open('rb') as f:P=PermutationGroup(list(pickle.load(f).args))
 P.order()
 with (HERE/'hurwitz_first_Pderived.pkl').open('rb') as f:PD=PermutationGroup(list(pickle.load(f).args))
 PD.order()
 with (HERE/'hurwitz_first_groups_state.pkl').open('wb') as f:pickle.dump([(list(G.args),G.__dict__) for G in [P,PD]],f)
 zz=np.load(PENT/'hurwitz_first_four_block_lifts.npz');sub=zz['subset'];rev=np.full(n,-1);rev[sub]=np.arange(len(sub))
 ca=np.load(PENT/'hurwitz_global_conjugators.npz');sj=json.load(open(HERE/'hurwitz_global_firstpair.json'))
 bp=[powp(B,2*k) for k in range(7)]
 order_b=next(k for k in range(1,7) if PD.contains(perm(bp[k])))
 print('B2 image order in Pab',order_b,flush=True)
 rows=[];save={};surv={}
 D=A[B]
 for bit in [0,1]:
  expect=zz[f'first_f_{bit}'];vs=ca[f'mixed72_V_{bit}'];keep=[]
  for j in sj['survivors'][str(bit)]:
   V=vs[j];Bi=V[B[np.argsort(V)]];Di=A[Bi];F0=D[np.argsort(Di)]
   assert np.array_equal(F0[Bi[np.argsort(F0)]],B)
   inp=P.contains(perm(F0));ks=[];ks448=[];rr=[]
   for k in range(6):
    F=bp[k][F0];yes=PD.contains(perm(F))
    got=rev[F[sub]];eq=np.array_equal(got,expect)
    if yes:ks.append(k)
    if yes and eq:ks448.append(k)
    rr.append({'k':k,'in_Pderived':bool(yes),'correct448':bool(eq)})
   if ks448:
    keep.append(j);save[f'F_{bit}_{j}']=bp[ks448[0]][F0]
   rows.append({'a3':bit,'candidate':j,'F0_in_P':bool(inp),'Pderived_k':ks,'Pderived_correct448_k':ks448,'tests':rr})
  surv[str(bit)]=keep
  print('a3',bit,'correctderived448',len(keep),'of',len(sj['survivors'][str(bit)]),flush=True)
 out={'B2_order_in_Pabelianization':order_b,'rows':rows,'survivors':surv,'elapsed_seconds':time.monotonic()-start,
 'scope':'Explicit B2-power corrections certify existence only; failures may admit other centralizer corrections.'}
 (HERE/'hurwitz_first_transporter.json').write_text(json.dumps(out,indent=2)+'\n')
 np.savez_compressed(HERE/'hurwitz_first_transporter.npz',**save)
 print('done',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
