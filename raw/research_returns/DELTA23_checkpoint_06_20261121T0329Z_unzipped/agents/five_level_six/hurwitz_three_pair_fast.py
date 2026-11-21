#!/usr/bin/env python3
"""Exact triple same-word membership; abelianization criterion avoids derivedclosure."""
from pathlib import Path
import json,pickle,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).parent;ROOT=HERE.parents[1];PENT=HERE.parent/'pentagon'
def pp(g):return Permutation(np.asarray(g).tolist())
def main():
 start=time.monotonic();q=np.load(ROOT/'records/hurwitz_first_solvable_joint.npz')['generators'];A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'];s=A[B[A]];z=s[s];t=C[B[C]];zp=t[t];mixed=[C[C],z];last=[z,zp];gs=np.array([np.r_[a,472+b,1816+c] for a,b,c in zip(q,mixed,last)])
 G=PermutationGroup([pp(g) for g in gs]);go=int(G.order());print('jointGorder',go,'gensorders',[int(g.order()) for g in G.generators],flush=True)
 assert go==10866225302113486007489789952 and all(g.order()==12 for g in G.generators)
 with (HERE/'hurwitz_three_pair_group_state.pkl').open('wb') as f:pickle.dump((list(G.args),G.__dict__),f)
 np.savez_compressed(HERE/'hurwitz_three_pair_group.npz',generators=gs,strong_generators=np.array([g.array_form for g in G.strong_gens],dtype=np.int16),base=np.array(G.base))
 # Independent literal checks of the abelianization criterion.
 args,st=pickle.load(open(HERE/'hurwitz_full_mixed_groups_state.pkl','rb'))[1];D34=PermutationGroup(args);D34.__dict__.update(st)
 state45=pickle.load(open(ROOT/'private/hurwitz_mixed45_state.pkl','rb'))[1];D45=PermutationGroup(state45[0]);D45.__dict__.update(state45[1]);I=np.arange(1344)
 powers=[]
 for g in mixed:
  ps=[I]
  for _ in range(1,12):ps.append(g[ps[-1]])
  powers.append(ps)
 relation34=[(i,j) for i in range(12) for j in range(12) if D34.contains(pp(powers[0][i][powers[1][j]]))]
 assert relation34==[(0,0),(6,0)]
 ps=I.copy();o=None
 for k in range(1,13):
  ps=z[ps]
  if D45.contains(pp(ps)):o=k;break
 assert o==12
 data=np.load(ROOT/'records/hurwitz_pentagon45_fibers.npz');f=np.load(PENT/'hurwitz_first_four_block_lifts.npz')['first_f_1'];ftarget=np.r_[f,448+np.arange(24)];rows=[];kept=[]
 for i in data['base_indices']:
  i=int(i)
  for j,(R,H) in enumerate(zip(data[f'R_{i}'],data[f'H_{i}'])):
   assert D34.contains(pp(R)) and D45.contains(pp(H))
   target=np.r_[ftarget,472+R,1816+H];yes=G.contains(pp(target))
   row={'candidate':i,'R_fiber_index':j,'centralizer_index':int(data[f'centralizer_indices_{i}'][j]),'triple_group_membership':bool(yes),'triple_derived_membership':bool(yes)};rows.append(row)
   if yes:kept.append((i,j))
   print(row,flush=True)
 out={'joint_order':go,'joint_abelianization_order':144,'joint_derived_order':go//144,'generator_orders':[12,12],'M34_abelian_rectangle_relations':relation34,'first_M45_generator_abelian_order':o,'tested_pairs':len(rows),'surviving_pairs':len(kept),'cases':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Exact commonwordcommutator necessary test; noactualgentlelift asserted. Jmembership equalsJprime membership for these componentderived tuples by the explicit abelianization proof.','result':'PASS'}
 (HERE/'hurwitz_three_pair_fast.json').write_text(json.dumps(out,indent=2)+'\n')
 np.savez_compressed(HERE/'hurwitz_three_pair_fast.npz',surviving_labels=np.array(kept,dtype=int))
 print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2),flush=True)
if __name__=='__main__':main()
