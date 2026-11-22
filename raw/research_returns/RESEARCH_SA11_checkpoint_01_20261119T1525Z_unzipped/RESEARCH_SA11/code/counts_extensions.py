#!/usr/bin/env python3
"""Enumerate rank-three one-element extensions for simple rank-three bases.
The support of the new zero triples is restricted to a matching; supercritical
(parallel-element) extensions are counted separately. All compatible sign
vectors are retained modulo simultaneous sign reversal on the new element.
A compiled C++ inner loop checks every 3-term Grassmann-Pluecker relation.
"""
from pathlib import Path
from itertools import combinations, permutations, product
from math import comb
import json, subprocess, time
ROOT=Path(__file__).resolve().parents[1]

def det(a,b,c):
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def sgn(a): return (a>0)-(a<0)
def matching_sets(n):
 def rec(rem,pairs):
  if not rem:
   yield tuple(pairs);return
  i,*rest=rem
  yield from rec(rest,pairs)
  for j in rest:
   yield from rec([x for x in rest if x!=j],pairs+[(i,j)])
 yield from rec(list(range(n)),[])

def main():
 results=[]
 # Dual vectors: each pair lies on a line through the common point p=(0,0,1).
 # The first member's affine parameters t are used only for exact rational construction.
 cases={
  'n3':[(1,0,1),(0,1,1),(1,2,1)],
  'n4':[(0,0,1),(1,1,1),(2,4,1),(3,9,1)],
  'n5':[(0,0,1),(1,1,1),(2,4,1),(3,9,1),(4,16,1)],
  'n6_convex':[(0,0,1),(1,1,1),(2,4,1),(3,9,1),(4,16,1),(5,25,1)],
  'n6_three_pair':[(1,0,1),(2,0,1),(0,1,1),(0,3,1),(1,1,1),(4,4,1)]}
 for name,base in cases.items():
  t=time.perf_counter(); n=len(base); p=n; pairs=list(combinations(range(n),2)); m=len(pairs)
  basechi={tup:sgn(det(*(base[i] for i in tup))) for tup in combinations(range(n),3)}
  assert all(basechi.values()),(name,'base not simple',basechi)
  def term(tup):
   parity=1
   for i in range(3):
    for j in range(i+1,3):
     if tup[i]>tup[j]:parity*=-1
   key=tuple(sorted(tup))
   if p in key: return pairs.index(key[:2]),parity
   return -1,parity*basechi[key]
  relations=[]
  for a in range(n+1):
   for b,c,d,e in combinations([i for i in range(n+1) if i!=a],4):
    ts=[(term((a,b,c)),term((a,d,e)),1),(term((a,b,d)),term((a,c,e)),-1),(term((a,b,e)),term((a,c,d)),1)]
    if any(u[0]>=0 or v[0]>=0 for u,v,s in ts): relations.append(ts)
  zsets=[[pairs.index(t) for t in mm] for mm in matching_sets(n)]
  inp={'case':name,'n':n,'base_vectors':base,'pairs':pairs,'base_chirotope':[[*k,v] for k,v in basechi.items()],'relations':relations,'zero_matchings':zsets}
  (ROOT/f'audit/counts_{name}_input.json').write_text(json.dumps(inp,indent=2)+'\n')
  # Encode every relation as its three (index1,sign1,index2,sign2,coefficient) terms.
  data=[f'{m} {len(relations)} {len(zsets)}']
  for rr in relations:data.append(' '.join(str(x) for u,v,c in rr for x in (*u,*v,c)))
  for z in zsets:data.append(' '.join(map(str,[len(z),*z])))
  run=subprocess.run([str(ROOT/'code/counts_extensions_bin')],input='\n'.join(data)+'\n',text=True,capture_output=True,check=True)
  pos=[tuple(map(int,x.split())) for x in run.stdout.splitlines()]
  (ROOT/f'audit/counts_{name}_positions.txt').write_text(run.stdout)
  counts={k:sum(s.count(0)==k for s in pos) for k in range(n//2+1)}
  assert len(pos)==len(set(pos))
  # Canonicalize unoriented position by its first nonzero sign.
  def canon(s):
   first=next(v for v in s if v)
   return tuple(first*v for v in s)
  lookup=set(pos)
  ordinary_edges=0
  generization_failure=[]
  for s in pos:
   for k,val in enumerate(s):
    if val==0:
     for eps in [-1,1]:
      ss=list(s);ss[k]=eps;ss=canon(ss)
      if ss not in lookup:generization_failure.append([s,k,eps])
      else: ordinary_edges+=1
  assert not generization_failure
  # Simple arrangement exceptional sweeps: two per original edge.
  exceptional_edges=2*n*(n-1)
  total_edges=ordinary_edges+exceptional_edges
  assert total_edges%2==0
  summary={
   'case':name,'n':n,'base_vectors':base,'zero_count_distribution':counts,
   'non_supercritical_positions_s2':len(pos),'ordinary_transition_edges':ordinary_edges,
   'exceptional_sweep_edges':exceptional_edges,'total_transition_edges_s1':total_edges,
   's0_if_all_vertex_links_four_cycles':total_edges//2,
   'chi_if_all_vertex_links_four_cycles':len(pos)-total_edges//2,
   'candidate_count':sum(2**(m-len(z)-1) for z in zsets),
   'tested_GP_relations_per_candidate':len(relations),'elapsed_seconds':time.perf_counter()-t}
  results.append(summary)
  print(json.dumps(summary),flush=True)
 (ROOT/'audit/counts_extension_summary.json').write_text(json.dumps(results,indent=2)+'\n')

if __name__=='__main__':main()
