#!/usr/bin/env python3
"""Full covariance fiber with fixed448+24 quotient, then both gentlecycles."""
from pathlib import Path
import numpy as np,pickle,json,time
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).parent;PENT=HERE.parent/'pentagon'
def pp(g):return Permutation(np.asarray(g).tolist())
def main():
 start=time.monotonic();args,st=pickle.load(open(HERE/'hurwitz_first_perfect_state.pkl','rb'));N=PermutationGroup(args);N.__dict__.update(st);assert N.order()==16796160000
 A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'];n=len(A);I=np.arange(n);r=A[B];s=r[A];ri=np.argsort(r);r2=r[r];r2i=np.argsort(r2);si=np.argsort(s)
 Z=N.centralizer(pp(B));zo=Z.order();print('C_N(B) order',zo,'generators',len(Z.generators),flush=True)
 with (HERE/'hurwitz_first_fiber_centralizer_state.pkl').open('wb') as f:pickle.dump((list(Z.args),Z.__dict__),f)
 np.savez_compressed(HERE/'hurwitz_first_fiber_centralizer.npz',generators=np.array([g.array_form for g in Z.generators],dtype=np.int16))
 fs=np.load(HERE/'hurwitz_first_pair_covariance.npz');vs=np.load(PENT/'hurwitz_global_conjugators.npz');rows=[];saved={};central=[]
 if zo>1000000:raise RuntimeError('Fullcentralizertoolargefornaiveenumeration; preserveexactgroupandrefine')
 for g in Z.generate_schreier_sims():central.append(np.array(g.array_form,dtype=np.int16))
 for bit in [0,1]:
  ids=sorted(int(k.split('_')[-1]) for k in fs.files if k.startswith(f'F_{bit}_'))
  for j in ids:
   f0=fs[f'F_{bit}_{j}'];V=vs[f'mixed72_V_{bit}'][j];Bi=V[B[np.argsort(V)]];passed=[];two=0
   for k,c in enumerate(central):
    f=c[f0]
    if not np.array_equal(s[f[si]],np.argsort(f)):continue
    two+=1
    if not np.array_equal(r2[f[r2i]][r[f[ri]][f]],I):continue
    assert np.array_equal(f[Bi[np.argsort(f)]],B)
    passed.append(k)
   rows.append({'a3':bit,'candidate':j,'two_cycle_count':two,'both_cycle_count':len(passed),'centralizer_indices':passed})
   saved[f'F_{bit}_{j}']=np.array([central[k][f0] for k in passed],dtype=np.int16)
   print('bit,index,cycles',bit,j,two,len(passed),flush=True)
 np.savez_compressed(HERE/'hurwitz_first_full_fiber.npz',centralizer_elements=np.array(central),**saved)
 out={'centralizer_order':int(zo),'rows':rows,'elapsed_seconds':time.monotonic()-start,'scope':'COMPLETE finite firstpairfiber with fixedP/P∞ value and covariance, filteredbyliteral two/threecycles. No fullGTlift claimed.'}
 (HERE/'hurwitz_first_full_fiber.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
