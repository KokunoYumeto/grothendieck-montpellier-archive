#!/usr/bin/env python3
"""Complete finite gentle core of the smallest raw colored C-covariance detector."""
from pathlib import Path
import sys,json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;CHAR=HERE.parent/'characters';sys.path.insert(0,str(CHAR/'code'))
from hurwitz_mixed72_s3_core import induced,power
start=time.monotonic();parts=np.load(HERE/'hurwitz_colored_raw_mixed_projection.npz');x,y=parts['raw_generators_9'];sub=parts['raw_subset_9'];n=len(x)
s,r,X,Y=induced(x,y);G=PermutationGroup([Permutation(X.tolist()),Permutation(Y.tolist())]);D=G.derived_subgroup();order,do=int(G.order()),int(D.order());print('core',order,'derived',do,flush=True)
(HERE/'hurwitz_colored_raw48_gentle_state.pkl').write_bytes(pickle.dumps([(G.args,G.__dict__),(D.args,D.__dict__)]))
raw=np.load(HERE/'hurwitz_colored_raw_cover.npz');A,B,C=raw['generators'];N=len(C);I=np.arange(N);V=np.load(HERE/'hurwitz_colored_raw_last_pair.npz')['base_V'];pot=np.load(HERE/'hurwitz_colored_last_gentle.npz')['potential_0'];W=6*V[I//6]+(I%6+pot[I//6])%6
loc=np.full(N,-1,dtype=int);loc[sub]=np.arange(n);c=loc[C[sub]];newc=loc[W[C[np.argsort(W)]][sub]];assert min(c)>=0 and min(newc)>=0
one=np.arange(6*n);z=np.argsort(X[Y]);ri=np.argsort(r)
if np.array_equal(r[X[ri]],Y)and np.array_equal(r[Y[ri]],z):cyc=r
elif np.array_equal(ri[X[r]],Y)and np.array_equal(ri[Y[r]],z):cyc=ri
else:raise AssertionError('cyclic marking')
ci=np.argsort(cyc);c2=cyc[cyc];c2i=np.argsort(c2)
assert do<=2000000,('enumeration size',do)
counts={'derived':do,'two_cycle':0,'three_cycle':0,'both':0,'negative':0,'raw_C_covariance':0};passing=[];allnorm=[]
for gg in D.generate_schreier_sims():
 f=np.array(gg.array_form);fi=np.argsort(f);n2=np.array_equal(power(s[f],2),one);n3=np.array_equal(power(fi[r],3),one)
 counts['two_cycle']+=int(n2);counts['three_cycle']+=int(n3)
 if not(n2 and n3):continue
 counts['both']+=1;fyz=cyc[f[ci]];fzx=c2[f[c2i]]
 negative=np.array_equal(fzx[np.argsort(z)[fyz[np.argsort(Y)[f[np.argsort(X)]]]]],one)
 if not negative:continue
 counts['negative']+=1;allnorm.append(f);R=f[:n]
 if np.array_equal(R[c[np.argsort(R)]],newc):counts['raw_C_covariance']+=1;passing.append(f)
np.savez_compressed(HERE/'hurwitz_colored_raw48_gentle.npz',s=s,r=r,x=X,y=Y,all_gentle=np.array(allnorm),passing=np.array(passing),raw_C=c,new_C=newc,raw_subset=sub)
out={'core_order':order,'core_derived_order':do,'counts':counts,'distinct_gentle_R_values':len({f[:n].tobytes()for f in allnorm}),'distinct_passing_R_values':len({f[:n].tobytes()for f in passing}),
 'elapsed_seconds':time.monotonic()-start,'scope':'Complete common F-prime finite S3 core with two/three/m=-1 norms and exact half-twist C covariance on raw48; no profinite lift assertion.'}
(HERE/'hurwitz_colored_raw48_gentle.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
