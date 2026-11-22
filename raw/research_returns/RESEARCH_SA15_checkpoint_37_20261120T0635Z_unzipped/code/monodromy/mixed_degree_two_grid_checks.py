#!/usr/bin/env python3
"""Exact F2 graph data for the candidate mixed degree-two comparison.
This verifies finite linear algebra, not geometric specialization or monodromy.
"""
from pathlib import Path
import json,time
start=time.perf_counter()
def rank(vectors):
 piv={}
 for v in vectors:
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i]
   else:piv[i]=v;break
 return len(piv)
def edge(i,j):return 1<<(6*i+j)
cuts=[sum(edge(i,j) for j in range(6)) for i in range(6)]
cuts += [sum(edge(i,j) for i in range(6)) for j in range(6)]
assert rank(cuts)==11
assert 36-rank(cuts)==25
def crossing(I,J):return [(i,j) for i in range(6) for j in range(6) if ((i in I) != (j in J))]
partitions=[({0,1,2},{0,1,2}),({0,1,3},{0,1,3})]
checks=[]
for I,J in partitions:
 E=crossing(I,J);assert len(E)==18
 ev=[edge(*ij) for ij in E]
 heart=[v^ev[0] for v in ev[1:]]
 assert rank(heart)==17
 assert rank(cuts+heart)-rank(cuts)==16
 assert rank(cuts+[sum(ev)])==rank(cuts)
 checks.append(dict(rows=sorted(I),columns=sorted(J),cross_edges=18,heart_dimension=16))
vC=edge(0,2)^edge(1,2)
vD=edge(3,4)^edge(3,5)
E2=set(crossing(*partitions[1]))
assert {(0,2),(1,2),(3,4),(3,5)}<=E2
cycleC=edge(0,1)^edge(0,2)^edge(2,1)^edge(2,2)
cycleD=edge(3,3)^edge(3,4)^edge(4,3)^edge(4,4)
assert (vC&cycleC).bit_count()%2==1
assert (vD&cycleD).bit_count()%2==1
def internal_projection(v,I,J):
 I=sorted(I);J=sorted(J)
 return sum(((v>>(6*i+j))&1)<<(3*a+b) for a,i in enumerate(I) for b,j in enumerate(J))
smallcuts=[sum(1<<(3*i+j) for j in range(3)) for i in range(3)]
smallcuts += [sum(1<<(3*i+j) for i in range(3)) for j in range(3)]
assert rank(smallcuts)==5 and 9-rank(smallcuts)==4
pC=internal_projection(vC,{0,1,2},{0,1,2})
pD=internal_projection(vD,{3,4,5},{3,4,5})
assert rank(smallcuts+[pC])==6
assert rank(smallcuts+[pD])==6
assert internal_projection(vC,{3,4,5},{3,4,5})==0
assert internal_projection(vD,{0,1,2},{0,1,2})==0
assert 9+9+(18-1)-1==34
assert 25+6-1==30
assert 16+8+8==32
out=dict(status='PASS',scope='Only exact graph quotients/projections and rank arithmetic; no geometric inference from the finite check.',
         global_coboundary_rank=11,global_graph_rank=25,partitions=checks,
         comparison_vectors=[['e02','e12'],['e34','e35']],
         four_cycle_evaluations=[1,1],internal_graph_ranks=[4,4],
         nonzero_internal_projection_checks=[True,True],
         generic_relative_rank=34,grid_relative_stable_rank=30,common_covector_kernel_rank=32,
         runtime_seconds=time.perf_counter()-start)
dest=Path(__file__).resolve().parents[1]/'outputs/mixed_degree_two_grid_checks.json'
assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
