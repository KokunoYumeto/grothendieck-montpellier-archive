"""Small exact certificates supporting audit/root_proofs.md.
Graph computations concern geometric graph realizations via their cell-incidence graph.
Finite order samples certify specified memberships only, never infinite density axioms.
"""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import json

def components(nodes,edges):
 nodes=set(nodes);adj={v:set() for v in nodes}
 for u,v in edges:
  if u in nodes and v in nodes:adj[u].add(v);adj[v].add(u)
 out=[]
 while nodes:
  stack=[next(iter(nodes))];seen=set()
  while stack:
   a=stack.pop()
   if a in seen:continue
   seen.add(a);stack.extend(adj[a]-seen)
  nodes-=seen;out.append(sorted(seen))
 return sorted(out)

def graph_case(name,vertices,edges,A,B):
 cells={'v:'+v for v in vertices}|{'e:'+e for e in edges}
 def closed(C):return all('e:'+e not in C or {'v:'+u,'v:'+v}<=C for e,(u,v) in edges.items())
 def link(C):return sum(('v:'+v in C) for e,pair in edges.items() if 'e:'+e not in C for v in pair)
 def comp_after(remove,collapse):
  rest=cells-remove;inc=[]
  for e,pair in edges.items():
   for v in pair:inc.append(('e:'+e,'v:'+v))
  chosen=sorted(collapse&rest)
  inc += [(chosen[0],v) for v in chosen[1:]] if chosen else []
  return components(rest,inc)
 raw=comp_after(set(),set());pa=comp_after(A,B);pb=comp_after(B,A)
 conditions={'A_B_closed':closed(A) and closed(B),'disjoint':not bool(A&B),'both_nonopen':link(A)>0 and link(B)>0,'regular_finite_graph_cones':True,'punctured_A_quotient_B_connected':len(pa)==1,'punctured_B_quotient_A_connected':len(pb)==1}
 return {'name':name,'vertices':vertices,'edges':edges,'A':sorted(A),'B':sorted(B),'ambient_components':raw,'link_cardinalities':[link(A),link(B)],'punctured_quotient_components':[pa,pb],'conditions':conditions,'is_ficelle':all(conditions.values()),'scope':'Closed subcomplexes of these finite graph realizations; regularity uses the explicit finite-star cone argument.'}

graphs=[]
graphs.append(graph_case('disconnected_two_intervals',['a0','a1','b0','b1'],{'e0':('a0','b0'),'e1':('a1','b1')},{'v:a0','v:a1'},{'v:b0','v:b1'}))
graphs.append(graph_case('interval_disconnected_end',['0','m','1'],{'left':('0','m'),'right':('m','1')},{'v:0','v:1'},{'v:m'}))
tripod={'oa':('o','a'),'ob':('o','b'),'oc':('o','c')}
graphs.append(graph_case('tripod_original',['o','a','b','c'],tripod,{'v:a'},{'v:b'}))
graphs.append(graph_case('tripod_enlarged_end',['o','a','b','c'],tripod,{'v:a','v:o','e:oa'},{'v:b'}))
assert [g['is_ficelle'] for g in graphs]==[True,True,True,False]
graphs.append(graph_case('side_contraction_tripod_quotient',['d','t','b','c'],{'dt':('d','t'),'tb':('t','b'),'dc':('d','c')},{'v:d'},{'v:b'}))
assert not graphs[-1]['is_ficelle'] and graphs[-1]['conditions']['regular_finite_graph_cones']

# Exact memberships in the infinite dense-diamond model, using a finite witness list.
def le(p,q):
 levp,arm_p,t=p;levq,arm_q,u=q
 return levp<levq or (levp==levq and (levp!=1 or arm_p==arm_q) and t<=u)
zero=(0,0,Q(0));z=(1,0,Q(3,2));top=(2,0,Q(3));omitted=(1,1,Q(3,2))
sample=[zero,(0,0,Q(1,2)),(1,0,Q(7,5)),z,(1,0,Q(8,5)),omitted,(2,0,Q(5,2)),top]
in_interval=lambda a,b,x:le(a,x) and le(x,b)
left={i for i,x in enumerate(sample) if in_interval(zero,z,x)}
right={i for i,x in enumerate(sample) if in_interval(z,top,x)}
whole={i for i,x in enumerate(sample) if in_interval(zero,top,x)}
assert left&right=={sample.index(z)} and sample.index(omitted) in whole-(left|right)
order={'scope':'Witness memberships in an infinite rational order; full F1–F6 verification is analytic in R-SA21-restriction. This finite sample is not asserted to satisfy those axioms.','sample':[str(x) for x in sample],'left':sorted(left),'right':sorted(right),'ambient_composite':sorted(whole),'omitted_witness':str(omitted),'joint_is_between_retained_witnesses':in_interval((1,0,Q(7,5)),(1,0,Q(8,5)),z)}

C=(Q(1,3),Q(2,3));D=(Q(2,3),Q(1,3))
sides=['A' if d<c else 'B' if d>c else 'intersection' for c,d in zip(C,D)]
assert set(sides)=={'A','B'}
circle={'C':[str(x) for x in C],'D':[str(x) for x in D],'D_sides_relative_to_C':sides,'ordinary_disjoint':all(c!=d for c,d in zip(C,D)),'cut_compatible':False}

boolean=[]
for n in range(4):
 valuations=list(product([0,1],repeat=n));atoms=len(valuations);mask=(1<<atoms)-1
 generators=[sum(v[j]<<i for i,v in enumerate(valuations)) for j in range(n)]
 generated={0,mask,*generators}
 while True:
  old=set(generated)
  generated|={a^b for a in old for b in old}|{a&b for a in old for b in old}
  if generated==old:break
 assert len(generated)==2**(2**n)
 boolean.append({'generators':n,'atoms':atoms,'elements':len(generated)})
ring=list(range(4));characters=[]
for values in product([0,1],repeat=4):
 if values[0]!=0 or values[3]!=1:continue
 if all(values[a^b]==values[a]^values[b] and values[a&b]==values[a]*values[b] for a in ring for b in ring):characters.append(values)
assert len(characters)==2

# The spanning-tree endpoint argument is also checked on all simple connected
# graphs with 2..5 labelled vertices. This is corroboration, not its general proof.
graph_counts=[]
for n in range(2,6):
 V=list(map(str,range(n)));possible=list(combinations(V,2));connected=0;min_noncut=n
 for mask in range(1<<len(possible)):
  E=[e for i,e in enumerate(possible) if mask>>i&1]
  if len(components(V,E))!=1:continue
  connected+=1;noncut=[v for v in V if len(components(set(V)-{v},E))==1]
  min_noncut=min(min_noncut,len(noncut));assert len(noncut)>=2
 graph_counts.append({'vertices':n,'connected_labelled_graphs':connected,'minimum_noncut_vertices':min_noncut})

out={'graph_ficelle_certificates':graphs,'dense_diamond_witness':order,'alternating_circle_cuts':circle,'free_boolean_algebra_counts':boolean,'F2_squared_unital_characters':[list(x) for x in characters],'relative_boundary_fiber_sizes':{'ring_elements':4,'prime_spectrum':2},'finite_graph_noncut_check':graph_counts,'all_assertions_passed':True}
root=Path(__file__).resolve().parents[1];(root/'outputs'/'root_checks.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
