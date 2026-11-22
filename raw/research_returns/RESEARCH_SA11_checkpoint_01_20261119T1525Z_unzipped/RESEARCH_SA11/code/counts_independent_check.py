#!/usr/bin/env python3
"""Independently verify full chirotope basis exchange and count disk G-G arcs.
Input: complete position lists from counts_extensions.py.
No numerical geometry is used in this checker.
"""
from pathlib import Path
from itertools import combinations, permutations
from functools import cmp_to_key
import json,time
ROOT=Path(__file__).resolve().parents[1]

def sgn(x):return (x>0)-(x<0)
def canonical(s):
 a=next(x for x in s if x)
 return tuple(a*x for x in s)

def main():
 results=[]
 for f in sorted((ROOT/'audit').glob('counts_n*_input.json')):
  tic=time.perf_counter(); data=json.loads(f.read_text());n=data['n'];name=data['case'];pairs=[tuple(p) for p in data['pairs']]
  base={tuple(r[:3]):r[3] for r in data['base_chirotope']}
  positions=[tuple(map(int,l.split())) for l in (ROOT/f'audit/counts_{name}_positions.txt').read_text().splitlines()]
  lookup=set(positions); details=[];exchange_checks=0
  for sid,s in enumerate(positions):
   def chi(a,b,c):
    if len({a,b,c})<3:return 0
    arr=(a,b,c);parity=(-1)**sum(arr[i]>arr[j] for i in range(3) for j in range(i+1,3));key=tuple(sorted(arr))
    if key[2]==n:return parity*s[pairs.index(key[:2])]
    return parity*base[key]
   def q(i,j):return chi(i,j,n)
   # Full chirotope signed basis exchange. Any ordering of y multiplies
   # both sides uniformly; only choice of first x matters.
   bases=[t for t in combinations(range(n+1),3) if chi(*t)]
   for x0 in bases:
    for first in x0:
     x=(first,*(v for v in x0 if v!=first))
     for y in bases:
      target=chi(*x)*chi(*y)
      vals=[chi(y[i],x[1],x[2])*chi(*(y[:i]+(x[0],)+y[i+1:])) for i in range(3)]
      assert target in vals,(name,s,x,y,vals)
      exchange_checks+=1
   pivot=0;k0=next(k for k in range(n) if q(pivot,k))
   def half(t):
    eps,i=t;v=eps*q(pivot,i)
    if v:return 0 if v>0 else 1
    direction=eps*(1 if i==pivot else q(i,k0)*q(pivot,k0))
    return 0 if direction>0 else 1
   def cmp(a,b):
    if a==b:return 0
    ha,hb=half(a),half(b)
    if ha!=hb:return -1 if ha<hb else 1
    eps,i=a;eta,j=b;c=eps*eta*q(i,j)
    if c:return -1 if c>0 else 1
    # Same direction: resolve parallel endpoint packet by the affine offsets.
    assert i!=j
    k=next(k for k in range(n) if q(i,k))
    before=-eta*chi(i,j,k)*q(i,k)
    assert before
    return -1 if before>0 else 1
   order=sorted([(eps,i) for i in range(n) for eps in [1,-1]],key=cmp_to_key(cmp))
   assert len(set(order))==2*n
   # All adjacent pairs crossing the artificial 0-angle cut are harmless;
   # the cyclic order is what matters.
   transitions=[];gpositions=[];spositions=[]
   for j in range(2*n):
    eps,i=order[j];eta,k=order[(j+1)%(2*n)]
    if i==k:continue
    if q(i,k)==0:
     # same-direction signed pair, not opposite parallel directions.
     t=next(t for t in range(n) if q(i,t))
     if eps*q(i,t)==eta*q(k,t):
      transitions.append((j,'G'));gpositions.append(j)
     continue
    # Ordinary specialization iff this boundary wedge is a triangle.
    # Endpoints belonging to an existing G packet are excluded.
    if any(q(i,t)==0 for t in range(n) if t!=i):continue
    if any(q(k,t)==0 for t in range(n) if t!=k):continue
    okay=True
    for t in range(n):
     if t in [i,k]:continue
     v=chi(i,k,t)*q(i,k)
     if q(i,t) and v!=eps*q(i,t):okay=False;break
     if q(k,t) and v!=eta*q(k,t):okay=False;break
    if okay:transitions.append((j,'S'));spositions.append(j)
   nu=s.count(0)
   assert len(gpositions)==2*nu,(name,s,order,transitions)
   # Compare independent specialization description with full extension list.
   expected_special=[]
   for jj,v in enumerate(s):
    if not v:continue
    ss=list(s);ss[jj]=0
    if any(ss) and canonical(ss) in lookup:expected_special.append(pairs[jj])
   observed_special=[tuple(sorted((order[j][1],order[(j+1)%(2*n)][1]))) for j in spositions]
   assert sorted(observed_special)==sorted(expected_special),(name,s,order,transitions,observed_special,expected_special)
   # For nu=1, exceptional corridor arcs interrupt each remaining G-G gap.
   # Count them by the test of specializing to a parallel base element,
   # and insert in the unique interval not containing the paired line.
   exc=[]
   if nu==1:
    iz=s.index(0);u,v=pairs[iz]
    for i,other in [(u,v),(v,u)]:
     ratios={q(a,b)*chi(a,b,i) for a,b in pairs if i not in [a,b]}
     if len(ratios)!=1:continue
     # Two endpoints of i; select boundary interval excluding both endpoints
     # of the other member of its parallel class.
     ii=[j for j,t in enumerate(order) if t[1]==i]
     def interior(a,b):
      res=[];j=(a+1)%(2*n)
      while j!=b:res.append(j);j=(j+1)%(2*n)
      return res
     possible=[(a,b) for a,b in [ii,ii[::-1]] if not any(order[j][1]==other for j in interior(a,b))]
     assert len(possible)==1
     a,b=possible[0]
     # Exceptional arc may span several ordinary endpoint gaps; no ordinary
     # transition may occur in its interior.
     interior_gaps=[a,*interior(a,b)]
     assert not any(j in interior_gaps for j in spositions),(name,s,order,transitions,i,other,possible,ratios)
     # Shrink the exceptional arc away from its ends and use a midpoint.
     length=(b-a)%(2*n);mid=(a+length/2)%(2*n)
     transitions.append((mid,'E'));exc.append({'line':i,'start':a,'end':b})
   transitions.sort()
   gg=0
   for a,b in zip(transitions,transitions[1:]+transitions[:1]):
    if a[1]==b[1]=='G':gg+=1
   if nu<=1:assert gg==0,(name,s,order,transitions,exc)
   details.append({'position_id':sid,'signs':s,'nu':nu,'boundary_order':order,'ordinary_transitions':transitions,'exceptional_corridors':exc,'gen_gen_arcs':gg})
  ggs=sum(x['gen_gen_arcs'] for x in details)
  flags=2*n*(n-1)
  summary={'case':name,'full_signed_basis_exchange_checks':exchange_checks,'positions':len(positions),'literal_gen_gen_arcs':ggs,'original_vertex_edge_flags':flags,'literal_s0':ggs+flags,'literal_s2_minus_s0':len(positions)-ggs-flags,'gen_gen_arcs_by_nu':{k:sum(x['gen_gen_arcs'] for x in details if x['nu']==k) for k in range(n//2+1)},'elapsed_seconds':time.perf_counter()-tic}
  results.append(summary)
  (ROOT/f'audit/counts_{name}_boundary_certificate.json').write_text(json.dumps(details,indent=2)+'\n')
  print(json.dumps(summary),flush=True)
 (ROOT/'audit/counts_independent_summary.json').write_text(json.dumps(results,indent=2)+'\n')
if __name__=='__main__':main()
