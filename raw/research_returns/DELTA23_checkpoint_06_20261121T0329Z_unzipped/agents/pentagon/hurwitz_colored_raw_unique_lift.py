#!/usr/bin/env python3
"""Minimal216-point certificate excluding the two nonzero P32 raw phases."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;start=time.monotonic()
raw=np.load(HERE/'hurwitz_colored_raw_cover.npz');A,B,C=raw['generators'];s=A[B[A]];x=C[C];y=s[s];N=len(x);I=np.arange(N)
baseparts=np.load(HERE/'hurwitz_colored_inverse_12_mixed.npz');base=baseparts['orbit_32'];bgens=baseparts['pair_32'];assert len(base)==36
sub=np.array([6*int(i)+k for i in base for k in range(6)]);loc=np.full(N,-1,dtype=int);loc[sub]=np.arange(216)
gens=np.array([loc[g[sub]]for g in[x,y]]);assert min(gens.flat)>=0
assert all(np.array_equal(g//6,b[np.arange(216)//6])for g,b in zip(gens,bgens))
G=PermutationGroup([Permutation(g.tolist())for g in gens]);BG=PermutationGroup([Permutation(g.tolist())for g in bgens])
go,bo=int(G.order()),int(BG.order());assert(go,bo)==(15116544,3779136)and go//bo==4
lifts=np.load(HERE/'hurwitz_colored_last_gentle.npz');V=np.load(HERE/'hurwitz_colored_raw_last_pair.npz')['base_V']
targets=[];rows=[]
for aid in[0,86,172]:
 W=6*V[I//6]+(I%6+lifts[f'potential_{aid}'][I//6])%6
 xx=W[x[np.argsort(W)]];t=loc[xx[sub]];assert min(t)>=0
 targets.append(t);rows.append({'assembly':aid,'new_x_in_raw_group':bool(G.contains(Permutation(t.tolist())))})
t0=targets[0];assert rows[0]['new_x_in_raw_group']
for row,t in zip(rows[1:],targets[1:]):
 delta=t[np.argsort(t0)]
 assert np.array_equal(delta//6,np.arange(216)//6)
 assert not np.array_equal(delta,np.arange(216))and np.array_equal(delta[delta[delta]],np.arange(216))
 assert not row['new_x_in_raw_group'];row['difference_order']=3;row['difference_projects_to_identity']=True
assert G.contains(Permutation(gens[0].tolist()))
# Literal witnesses that the surviving phase can meet this local covariance.
old=np.load(HERE/'hurwitz_colored_raw_mixed_local.npz');witnesses=old['R_0_32'];assert len(witnesses)==2
for r in witnesses:
 assert G.contains(Permutation(r.tolist()))
 assert np.array_equal(r[gens[0][np.argsort(r)]],t0)
np.savez_compressed(HERE/'hurwitz_colored_raw_unique_lift.npz',raw_subset=sub,base_subset=base,generators=gens,base_generators=bgens,targets=targets,surviving_R_witnesses=witnesses)
out={'statement':'D23.P33','raw_degree':216,'base_degree':36,'raw_group_order':go,'base_group_order':bo,'projection_kernel_order':4,
 'cases':rows,'identity_control':True,'surviving_local_R_witness_count':2,'elapsed_seconds':time.monotonic()-start,
 'scope':'Necessary exclusion of P32 colored raw phases86/172 via a nontrivial order3 kernel discrepancy in a quotient with kernel order4. Baseform(1,0) remains with rawphase0.'}
(HERE/'hurwitz_colored_raw_unique_lift.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
