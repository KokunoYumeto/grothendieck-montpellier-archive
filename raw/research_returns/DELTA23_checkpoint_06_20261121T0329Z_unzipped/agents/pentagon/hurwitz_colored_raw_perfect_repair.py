#!/usr/bin/env python3
"""Construct perfect-residual source-kernel commutator corrections for the remaining binary raw C defect.

A successful result is a word witness. A failed bounded search is not
an exclusion and is never represented as kernel completeness.
"""
from pathlib import Path
from collections import deque
import json,random,time,pickle,sys
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;FIVE=HERE.parent/'five_level_six';start=time.monotonic()
raw=np.load(HERE/'hurwitz_colored_raw_cover.npz');A,B,C=raw['generators'];N=len(A);n=N//6;M=2*n;I=np.arange(N);s=A[B[A]]
rawgens=np.array([np.r_[A[A],N+C[C]],np.r_[B[B],N+s[s]]],dtype=np.int32)
orig=np.load(HERE/'hurwitz_cubic216_four_13.npz')['generators'];a,b,c=orig
oldgens=np.load(FIVE/'hurwitz_colored_full_commonword_group.npz')['generators']
sourcegens=np.array([np.r_[oldgens[0],2290+a[a]],np.r_[oldgens[1],2290+b[b]]],dtype=np.int32)
rawis=[np.argsort(g).astype(np.int32)for g in rawgens];srcis=[np.argsort(g).astype(np.int32)for g in sourcegens]
basegens=rawgens[:,::6]//6;baseis=[np.argsort(g)for g in basegens]
witness=np.load(HERE/'hurwitz_colored_raw_restored_witness.npz');F0,R0,W=[witness[k]for k in['raw_F','raw_R','raw_V']];Wi=np.argsort(W)
fp,rp=F0[::6]//6,R0[::6]//6;ef,er=F0[::6]%6,R0[::6]%6
Bnew=W[B[Wi]];Cnew=W[C[Wi]];bp=Bnew[::6]//6;cp=C[::6]//6;eb=B[::6]%6;ebn=Bnew[::6]%6;ecn=Cnew[::6]%6;ec=C[::6]%6
rb=(eb[fp]-ebn-ef[bp]+ef)%6;rc=(ecn[rp]-ec-er[cp]+er)%6
assert np.all(rb==0)and set(map(int,rc))<={0,3}
target=np.r_[rb//3,rc//3].astype(np.uint8)
def bits(v):return int.from_bytes(np.packbits(np.asarray(v,dtype=np.uint8),bitorder='little').tobytes(),'little')
def vector(v):return np.unpackbits(np.frombuffer(v.to_bytes((M+7)//8,'little'),dtype=np.uint8),bitorder='little')[:M]
def linear(v):
 k=vector(v);df=k[:n][fp];dr=k[n:][rp]
 return bits(np.r_[df[bp]^df,dr[cp]^dr])
def power(p,e):
 out=np.arange(len(p),dtype=np.int32);q=p.copy()
 while e:
  if e&1:out=out[q]
  q=q[q];e//=2
 return out
def word(ws,gs,invs):
 out=np.arange(len(gs[0]),dtype=np.int32)
 for token in ws:out=out[gs[token-1]if token>0 else invs[-token-1]]
 return out
def comm(a,b):return a[b[np.argsort(a)[np.argsort(b)]]]
Krows={};Lrows={};kbasis=[];nodes=[];queue=deque();targetbits=bits(target)
def solve_target():
 q=targetbits;combo=0
 while q:
  piv=q.bit_length()-1
  if piv not in Lrows:return None
  row,cc=Lrows[piv];q^=row;combo^=cc
 return combo
solution=None
def add(k,node):
 global solution
 q=k
 while q:
  piv=q.bit_length()-1
  if piv not in Krows:break
  q^=Krows[piv]
 if not q:return False
 Krows[q.bit_length()-1]=q;i=len(kbasis);kbasis.append(k);nodes.append(node);queue.append(i)
 v=linear(k);combo=1<<i
 while v:
  piv=v.bit_length()-1
  if piv not in Lrows:break
  row,cc=Lrows[piv];v^=row;combo^=cc
 if v:Lrows[v.bit_length()-1]=(v,combo)
 solution=solve_target();return True
sys.path.insert(0,str(FIVE))
from hurwitz_colored_word_evaluator import colored_evaluator,WordEvaluator
args,state=pickle.loads((HERE/'hurwitz_colored_full_first_join_state.pkl').read_bytes());source=PermutationGroup(args);source.__dict__.update(state)
join=np.load(HERE/'hurwitz_colored_full_first_join.npz')
xab=np.array([12*((i//12+1)%12)+i%12 for i in range(144)]);yab=np.array([12*(i//12)+(i%12+1)%12 for i in range(144)])
first=colored_evaluator(np.r_[rawgens[0],2*N+xab],np.r_[rawgens[1],2*N+yab])
ev=WordEvaluator(source,[first.evaluate(p)for p in join['seed_old']])
perfect=[(i,p)for i,p in enumerate(source.strong_gens)if np.array_equal(p.array_form[:2290],np.arange(2290))]
seeds=[]
for attempt,(strong_index,p)in enumerate(perfect):
 order=int(p.order());allraw=ev.evaluate(p);assert np.array_equal(allraw[2*N:]-2*N,np.arange(144))
 rr=allraw[:2*N];ker=power(rr,3*order)
 assert np.array_equal(ker//6,np.arange(2*N)//6)
 phase=ker[::6]%6;assert set(map(int,phase))<={0,3};k=bits(phase//3)
 added=add(k,{'type':'source_strong_power','strong_index':strong_index,'source_order':order,'power':3*order,'word_exponents_mod12_zero':True})if k else False
 while queue and solution is None:
  parent=queue.popleft();v=vector(kbasis[parent])
  for gen in range(2):
   kk=bits(v[baseis[gen]])
   add(kk,{'type':'conjugate','parent':parent,'generator':gen+1})
   if solution is not None:break
 seeds.append({'attempt':attempt,'source_element_order':order,'raw_kernel_nontrivial':bool(k),'new_seed_independent':bool(added),'kernel_rank':len(Krows),'constraint_rank':len(Lrows)})
 print(seeds[-1],flush=True)
 if solution is not None:break
info={'found':solution is not None,'attempts':seeds,'kernel_span_dimension':len(Krows),'constraint_span_dimension':len(Lrows),'nodes':nodes,
 'elapsed_seconds':time.monotonic()-start,'scope':'Constructed source-kernel commutator subgroup only. A found correction is exact; no completeness or exclusion is claimed if search fails.'}
saved={'source_generators':sourcegens,'raw_generators':rawgens,'target_constraint':target,'basis_vectors':np.array([vector(k)for k in kbasis],dtype=np.uint8)}
if solution is not None:
 selected=[i for i in range(len(kbasis))if(solution>>i)&1];k=0
 for i in selected:k^=kbasis[i]
 assert linear(k)==targetbits
 v=vector(k);KF=6*(I//6)+(I%6+3*v[:n][I//6])%6;KR=6*(I//6)+(I%6+3*v[n:][I//6])%6
 F=KF[F0];R=KR[R0]
 assert np.array_equal(W[B[Wi]],np.argsort(F)[B[F]])
 assert np.array_equal(W[C[Wi]],R[C[np.argsort(R)]])
 saved.update(raw_F=F,raw_R=R,raw_V=W,correction_phase=v,selected_basis=np.array(selected))
 info.update(selected_basis=selected,raw_B_covariance=True,raw_C_covariance=True)
np.savez_compressed(HERE/'hurwitz_colored_raw_perfect_repair.npz',**saved)
(HERE/'hurwitz_colored_raw_perfect_repair.json').write_text(json.dumps(info,indent=2)+'\n');print({k:v for k,v in info.items()if k not in['nodes','attempts']},flush=True)
