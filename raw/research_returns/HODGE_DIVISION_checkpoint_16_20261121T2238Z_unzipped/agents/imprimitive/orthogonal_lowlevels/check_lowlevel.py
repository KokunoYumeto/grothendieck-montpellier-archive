#!/usr/bin/env python3
"""Exact author checks for D-OL04--05. Universal argument is in the TeX."""
from pathlib import Path
from fractions import Fraction as F
from collections import deque,Counter
import hashlib,json,time
start=time.perf_counter(); out={'status':'PASS'}
J=10**30; d0=4*J-2
assert 4*(J-1)+2==d0 and 4*(J-1)+1==d0-1
assert d0>2*J and F(1,3)<F(9,16)
c=F(9,16); delta=(1-c)/4
assert delta==F(7,64)
coefficient=1+10*delta-2
assert coefficient==F(3,32) and 6/coefficient==64
assert 16**6*15>64
powers=[]
for q in range(2,16):
 for p in (2,3,5,7,11,13):
  x=p
  while x<q:x*=p
  if x==q:
   powers.append(q);break
assert powers==[2,3,4,5,7,8,9,11,13]
# Direct finite verification of every odd-prime binary form in the displayed
# fields; the universal proof instead uses the two-set intersection argument.
forms=0
for q in (3,5,7,11,13,17,19,23,29,31):
 squares={x*x%q for x in range(q)}
 assert len(squares)==(q+1)//2
 for a in range(1,q):
  for b in range(1,q):
   values={(a*x+b*y)%q for x in squares for y in squares}
   assert values==set(range(q))
   forms+=1
out['constants']={'level_bound':str(J),'stable_dimension_threshold':str(d0),
 'support':str(delta),'inducing_degree_ceiling':64,'remaining_prime_powers':powers,
 'binary_forms_checked':forms}

# Entire O_6^+(2) generated from the rank-one symmetries of Q=x1y1+x2y2+x3y3.
# No GAP, group table, or external matrix input is used.
def Q(v):return ((v&7)&(v>>3)).bit_count()%2
def B(v,w):return (((v&7)&(w>>3))^((w&7)&(v>>3))).bit_count()%2
def sym(v,x):return x^(v if B(v,x) else 0)
def act(M,x):
 a=0
 while x:
  bit=x&-x;a^=M[bit.bit_length()-1];x^=bit
 return a
def comp(A,B0):return tuple(act(A,b) for b in B0)
I=tuple(1<<i for i in range(6))
roots=[v for v in range(1,64) if Q(v)]
assert len(roots)==28
Gens=[tuple(sym(v,1<<i) for i in range(6)) for v in roots]
for g in Gens:
 assert comp(g,g)==I
 assert all(Q(act(g,x))==Q(x) for x in range(64))
anchor=Gens[0]
Comms=list(set(comp(comp(anchor,g),comp(anchor,g)) for g in Gens)-{I})
def closure(gens):
 # Table each fixed left factor's action on all64 vectors, so composition
 # needs just six exact integer lookups.
 tabs=[[act(g,x) for x in range(64)] for g in gens]
 found={I}; queue=deque([I])
 while queue:
  m=queue.popleft()
  for tab in tabs:
   n=tuple(tab[x] for x in m)
   if n not in found:found.add(n);queue.append(n)
 return found
whole=closure(Gens);derived=closure(Comms)
assert len(whole)==40320 and len(derived)==20160 and derived<=whole
assert all(g not in derived for g in Gens)
# The commutator-generated subgroup already has index2, proving that it is
# the entire derived subgroup in this exact finite witness.
def pair_orbits(gens):
 tabs=[[act(g,x) for x in range(64)] for g in gens]
 unseen=set(range(4096)); result=[]
 while unseen:
  seed=min(unseen);unseen.remove(seed); orbit=[seed];queue=deque([seed])
  while queue:
   x=queue.popleft(); a=x&63;b=x>>6
   for tab in tabs:
    y=tab[a]+64*tab[b]
    if y in unseen:unseen.remove(y);orbit.append(y);queue.append(y)
  result.append(tuple(sorted(orbit)))
 return sorted(result)
Oorbits=pair_orbits(Gens); Sorbits=pair_orbits(Comms)
assert Oorbits==Sorbits
out['full_finite_orbit_witness']={'field':2,'natural_dimension':6,'level':1,
 'symmetries':len(Gens),'commutator_generators':len(Comms),
 'full_group_order':len(whole),'derived_group_order':len(derived),
 'ordered_pairs':4096,'equal_pair_orbits':len(Oorbits),
 'orbit_sizes':sorted(len(a) for a in Oorbits)}
# Check the chosen nondegenerate complement for every subspace R generated
# by two vectors, using a direct enumeration of R^perp and its radical.
seen=set(); complement_cases=0
for x in range(64):
 for y in range(64):
  R=frozenset((0,x,y,x^y))
  if R in seen:continue
  seen.add(R)
  perp=[v for v in range(64) if all(B(v,r)==0 for r in R)]
  radical=[v for v in perp if all(B(v,w)==0 for w in perp)]
  assert len(perp)//len(radical)>=4
  # A nondegenerate2-plane is certified by a single polar pairing1.
  assert any(B(v,w)==1 for v in perp for w in perp)
  complement_cases+=1
out['all_two_vector_spans']={'distinct_spans':complement_cases,
 'nondegenerate_binary_complement_exists':True}
proof=Path(__file__).with_name('orthogonal_lowlevel_section.tex')
out['proof_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
out['seconds']=time.perf_counter()-start
Path(__file__).with_name('lowlevel_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
