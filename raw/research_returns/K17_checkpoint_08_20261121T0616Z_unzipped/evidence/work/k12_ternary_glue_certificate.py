"""Exact finite classification and all 26 minimum certificates for proper index3 glue.

Run this script beside k12_ternary_glue_form_data.json. Standard library only.
The published complete five-class Delta1 rank3 polytope list is an explicit
external coverage input; its points, all color cases, all symmetry tests,
all orbit reductions and all 26 complete minimum sets are checked here.
No nonboundary or whole-homology claim is made.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd, isqrt, lcm
from pathlib import Path
import json


def canon(z):
    z=tuple(z)
    if not any(z): return z
    return z if next(x for x in z if x)>0 else tuple(-x for x in z)


def quad(v):
    return [[F(x*y) for y in v] for x in v]


def gram_value(q,v):
    return sum(q[i][j]*v[i]*v[j] for i in range(len(v)) for j in range(len(v)))


def matrix_rank(rows):
    a=[[F(x) for x in row] for row in rows]
    k=0
    for j in range(len(a[0])):
        i=next((i for i in range(k,len(a)) if a[i][j]),None)
        if i is None:continue
        a[i],a[k]=a[k],a[i]
        p=a[k][j];a[k]=[x/p for x in a[k]]
        for i in range(k+1,len(a)):
            p=a[i][j]
            if p:a[i]=[x-p*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k


def det3(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-b[0]*(a[1]*c[2]-a[2]*c[1])+c[0]*(a[1]*b[2]-a[2]*b[1])


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def reconstruct_dual(rays):
    pivot=next(j for j in combinations(range(len(rays)),3) if abs(det3(*(rays[i] for i in j)))==1)
    a,b,c=(rays[j] for j in pivot);det=det3(a,b,c)
    inverse=[[F(x,det) for x in row] for row in (cross(b,c),cross(c,a),cross(a,b))]
    others=[j for j in range(len(rays)) if j not in pivot]
    order=others+list(pivot)
    bnorm=[[sum(row[k]*rays[j][k] for k in range(3)) for j in order] for row in inverse]
    assert all(x.denominator==1 for row in bnorm for x in row)
    n=len(rays)-3
    vectors=[tuple(int(i==j) for i in range(n)) for j in range(n)]+[tuple(-int(bnorm[j][i]) for i in range(n)) for j in range(3)]
    assert all(sum(bnorm[i][j]*vectors[j][k] for j in range(len(rays)))==0 for i in range(3) for k in range(n))
    return vectors,[[int(x) for x in row] for row in bnorm],order


def ldl(q):
    n=len(q);lower=[[F(i==j) for j in range(n)] for i in range(n)];diagonal=[]
    for i in range(n):
        d=q[i][i]-sum(lower[i][k]**2*diagonal[k] for k in range(i))
        assert d>0
        diagonal.append(d)
        for j in range(i+1,n):
            lower[j][i]=(q[j][i]-sum(lower[j][k]*lower[i][k]*diagonal[k] for k in range(i)))/d
    assert all(q[i][j]==sum(lower[i][k]*diagonal[k]*lower[j][k] for k in range(n)) for i in range(n) for j in range(n))
    return lower,diagonal


def exact_short_vectors(q,bound):
    lower,diagonal=ldl(q)
    n=len(q);z=[0]*n;found=[];nodes=0
    def visit(i,partial):
        nonlocal nodes
        nodes+=1
        if i<0:
            if any(z):
                assert gram_value(q,z)==partial
                found.append(tuple(z))
            return
        remaining=bound-partial
        if remaining<0:return
        shift=sum(lower[j][i]*z[j] for j in range(i+1,n))
        a,b=shift.numerator,shift.denominator
        squared_radius=(remaining/diagonal[i])*b*b
        radius=isqrt(squared_radius.numerator//squared_radius.denominator)
        low=-((radius+a)//b)
        high=(radius-a)//b
        # low=ceil((-radius-a)/b), high=floor((radius-a)/b).
        for value in range(low,high+1):
            z[i]=value
            term=diagonal[i]*(F(value)+shift)**2
            assert term<=remaining
            visit(i-1,partial+term)
    visit(n-1,F(0))
    return sorted(found),nodes,diagonal



from itertools import product, combinations, permutations
from pathlib import Path
import ast,json,time

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def canon(v):
 v=tuple(v)
 return v if next(x for x in v if x)>0 else tuple(-x for x in v)
def mv(A,v):return tuple(dot(r,v)for r in A)
def parity(p):return sum(p[i]>p[j]for i in range(len(p))for j in range(i+1,len(p)))%2

MASKS=tuple(range(1,8));COLORS={m:tuple(c for c in range(3)if m>>c&1)for m in MASKS}
SHIFT={(m,t):sum(1<<((c+t)%3)for c in COLORS[m])for m in MASKS for t in range(3)}
SIGN={(m,e):sum(1<<((e*c)%3)for c in COLORS[m])for m in MASKS for e in [-1,1]}

def autos(B):
 pivot=next(p for p in combinations(range(len(B)),3)if abs(det(*(B[i]for i in p)))==1)
 a,b,c=(B[i]for i in pivot);D=det(a,b,c)
 inv=tuple(tuple(x//D for x in r)for r in (cross(b,c),cross(c,a),cross(a,b)))
 signed=B+[tuple(-x for x in b)for b in B];lookup={b:i for i,b in enumerate(B)}
 found={}
 for im in permutations(signed,3):
  if abs(det(*im))!=1:continue
  A=tuple(tuple(sum(im[k][i]*inv[k][j]for k in range(3))for j in range(3))for i in range(3))
  images=[mv(A,b)for b in B]
  if not all(canon(v)in lookup for v in images):continue
  perm=tuple(lookup[canon(v)]for v in images)
  signs=tuple(1 if v==canon(v)else -1 for v in images)
  found[A]=(perm,signs)
 return [(A,*v)for A,v in found.items()]

def odd_witness(state,B,group,shifts):
 sizes=[m.bit_count()for m in state];offset=[0]
 for n in sizes:offset.append(offset[-1]+n)
 for A,perm,signs in group:
  if any(sizes[j]!=sizes[perm[j]]for j in range(len(B))):continue
  signed=tuple(SIGN[state[j],signs[j]]for j in range(len(B)))
  for lam,values in shifts:
   if any(signed[j]!=SHIFT[state[perm[j]],values[perm[j]]]for j in range(len(B))):continue
   p=[]
   for j,m in enumerate(state):
    dest=perm[j];values_dest=COLORS[state[dest]]
    p.extend(offset[dest]+values_dest.index((signs[j]*c-values[dest])%3)for c in COLORS[m])
   if parity(p):return {'matrix':A,'lambda':lam,'permutation':p}
 return None

def support_witness(state,zweight,shifts):
 n=sum(m.bit_count()for m in state)
 for lam,values in shifts:
  w=n-sum(bool(SHIFT[m,t]&1)for m,t in zip(state,values))+zweight
  if w<=6:return {'lambda':lam,'support':w}
 return None

def facets(vertices):
    out = set()
    from math import gcd
    from functools import reduce
    for a, b, c in combinations(vertices, 3):
        n = cross(tuple(y-x for x,y in zip(a,b)), tuple(y-x for x,y in zip(a,c)))
        if n == (0,0,0):
            continue
        rhs = dot(n, a)
        vals = [dot(n,v)-rhs for v in vertices]
        if all(x <= 0 for x in vals):
            pass
        elif all(x >= 0 for x in vals):
            n = tuple(-x for x in n)
            rhs = -rhs
        else:
            continue
        g = reduce(gcd, (abs(x) for x in (*n, rhs)))
        out.add(tuple(x//g for x in (*n, rhs)))
    return sorted(out)


SOURCE_RECORDS = [[(-1, -1, 0), (-1, -1, 1), (-1, 0, 0), (-1, 0, 1), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, 0, -1), (1, 0, 0), (1, 1, -1), (1, 1, 0)], [(-1, 0, -1), (-1, 0, 0), (0, -1, -1), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1)], [(-1, 0, 0), (0, -1, -1), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0)], [(-1, 0, 0), (-1, 1, 1), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, -1, -1), (1, 0, 0)], [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, 0, 0)]]
EXPECTED_ORBITS = [{'record': 1, 'B': [[0, 0, 1], [0, 1, 0], [1, 0, -1], [1, 0, 0], [1, 1, -1], [1, 1, 0]], 'orbits': [{'state': [1, 1, 3, 7, 7, 7], 'zero_count': 0, 'zero_weight': 0, 'orbit_size': 324}, {'state': [1, 3, 1, 3, 7, 7], 'zero_count': 1, 'zero_weight': 1, 'orbit_size': 1296}, {'state': [1, 3, 1, 6, 3, 7], 'zero_count': 2, 'zero_weight': 1, 'orbit_size': 648}, {'state': [1, 3, 1, 6, 5, 7], 'zero_count': 2, 'zero_weight': 1, 'orbit_size': 1296}, {'state': [1, 3, 1, 6, 7, 3], 'zero_count': 2, 'zero_weight': 1, 'orbit_size': 324}, {'state': [1, 3, 1, 6, 7, 5], 'zero_count': 2, 'zero_weight': 1, 'orbit_size': 648}, {'state': [1, 3, 1, 6, 7, 7], 'zero_count': 1, 'zero_weight': 0, 'orbit_size': 648}, {'state': [1, 3, 1, 6, 7, 7], 'zero_count': 1, 'zero_weight': 1, 'orbit_size': 648}, {'state': [1, 3, 1, 7, 3, 7], 'zero_count': 1, 'zero_weight': 1, 'orbit_size': 648}, {'state': [1, 3, 1, 7, 5, 6], 'zero_count': 2, 'zero_weight': 1, 'orbit_size': 648}, {'state': [1, 3, 1, 7, 5, 7], 'zero_count': 1, 'zero_weight': 1, 'orbit_size': 1296}, {'state': [1, 3, 1, 7, 7, 3], 'zero_count': 1, 'zero_weight': 1, 'orbit_size': 324}, {'state': [1, 3, 1, 7, 7, 5], 'zero_count': 1, 'zero_weight': 1, 'orbit_size': 648}, {'state': [1, 3, 1, 7, 7, 7], 'zero_count': 0, 'zero_weight': 0, 'orbit_size': 648}, {'state': [1, 3, 3, 3, 3, 7], 'zero_count': 1, 'zero_weight': 1, 'orbit_size': 1296}, {'state': [1, 3, 3, 5, 3, 7], 'zero_count': 1, 'zero_weight': 1, 'orbit_size': 1296}, {'state': [1, 3, 3, 5, 5, 7], 'zero_count': 1, 'zero_weight': 1, 'orbit_size': 1296}, {'state': [1, 3, 3, 5, 6, 7], 'zero_count': 1, 'zero_weight': 1, 'orbit_size': 1296}, {'state': [1, 3, 3, 5, 7, 7], 'zero_count': 0, 'zero_weight': 0, 'orbit_size': 648}, {'state': [1, 7, 3, 5, 3, 7], 'zero_count': 0, 'zero_weight': 0, 'orbit_size': 1296}]}, {'record': 2, 'B': [[0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1]], 'orbits': [{'state': [3, 1, 7, 3, 7], 'zero_count': 2, 'zero_weight': 1, 'orbit_size': 216}, {'state': [3, 3, 3, 3, 7], 'zero_count': 2, 'zero_weight': 1, 'orbit_size': 216}, {'state': [7, 1, 3, 3, 7], 'zero_count': 2, 'zero_weight': 1, 'orbit_size': 216}, {'state': [7, 1, 7, 3, 3], 'zero_count': 2, 'zero_weight': 1, 'orbit_size': 108}, {'state': [7, 1, 7, 3, 7], 'zero_count': 1, 'zero_weight': 0, 'orbit_size': 72}, {'state': [7, 1, 7, 3, 7], 'zero_count': 1, 'zero_weight': 1, 'orbit_size': 72}]}, {'record': 3, 'B': [[0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0]], 'orbits': []}, {'record': 4, 'B': [[0, 0, 1], [0, 1, 0], [1, -1, -1], [1, 0, 0]], 'orbits': []}, {'record': 5, 'B': [[0, 0, 1], [0, 1, 0], [1, 0, 0]], 'orbits': []}]

expected_counts=[(63450,21978,24300,17172),(2310,1410,0,900),(14,14,0,0),(14,14,0,0),(0,0,0,0)]
reports=[];retained={}
for idx,vertices0 in enumerate(SOURCE_RECORDS):
 vertices=[tuple(v)for v in vertices0];B=sorted(set(canon(v)for v in vertices));ineq=facets(vertices)
 box=[range(min(v[i]for v in vertices),max(v[i]for v in vertices)+1)for i in range(3)]
 points={v for v in product(*box)if all(dot(f[:3],v)<=f[3]for f in ineq)}
 assert points=={(0,0,0)}|set(vertices)
 assert all(abs(det(*a))<=1 for a in combinations(B,3))
 group=autos(B);shifts=[(lam,tuple(dot(lam,b)%3 for b in B))for lam in product(range(3),repeat=3)]
 counts=[0,0,0,0];survivors=set()
 for state in product(MASKS,repeat=len(B)):
  n=sum(m.bit_count()for m in state);z=13-n
  if z not in (0,1,2):continue
  zero_weights=(0,)if z==0 else(0,1)if z==1 else(1,)
  odd=odd_witness(state,B,group,shifts)
  for zw in zero_weights:
   counts[0]+=1
   if odd:counts[1]+=1;continue
   if support_witness(state,zw,shifts):counts[2]+=1;continue
   counts[3]+=1;survivors.add((state,z,zw))
 assert tuple(counts)==expected_counts[idx]
 left=set(survivors);actual=[]
 while left:
  state,z,zw=min(left);orbit=set()
  for A,perm,signs in group:
   signed=[None]*len(B)
   for j,m in enumerate(state):signed[perm[j]]=SIGN[m,signs[j]]
   for lam,values in shifts:orbit.add((tuple(SHIFT[m,t]for m,t in zip(signed,values)),z,zw))
  assert orbit<=left
  left-=orbit;actual.append({'state':list(state),'zero_count':z,'zero_weight':zw,'orbit_size':len(orbit)})
 assert actual==EXPECTED_ORBITS[idx]['orbits']
 retained[idx+1]=(B,actual,group,shifts)
 reports.append({'record':idx+1,'signed_classes':len(B),'automorphisms':len(group),'states':counts[0],'odd':counts[1],'Watson_impossible':counts[2],'retained_states':counts[3],'orbits':len(actual)})
 print(json.dumps(reports[-1]),flush=True)

forms=json.loads(Path(__file__).with_name('k12_ternary_glue_form_data.json').read_text())
assert len(forms)==26
form_reports=[];seen=set()
for f in forms:
 rid,oid=f['record'],f['orbit'];assert (rid,oid)not in seen;seen.add((rid,oid))
 B,orbs,group,shifts=retained[rid];orb=orbs[oid-1];assert f['state']==orb
 BB=[tuple(v)for v in f['gale_columns']];V=f['Lmin_vectors'];c=f['colors'];AB=f['ambient_basis_numerator'];W=f['minimum_vectors']
 expected=[]
 for b,mask in zip(B,orb['state']):expected.extend((b,color)for color in COLORS[mask])
 z,zw=orb['zero_count'],orb['zero_weight']
 expected.extend(((0,0,0),color)for color in ([]if z==0 else[zw]if z==1 else[0,1]))
 assert sorted(zip(BB,c))==sorted(expected)
 assert V[:10]==[[int(i==j)for i in range(10)]for j in range(10)]
 assert all(sum(BB[j][i]*V[j][k]for j in range(13))==0 for i in range(3)for k in range(10))
 assert max(abs(det(*a))for a in combinations(BB,3))==1
 w=[(sum(c[j]*V[j][i]for j in range(13))+1)%3-1 for i in range(10)]
 j0=next(i for i,t in enumerate(w)if t)
 if w[j0]<0:w=[-x for x in w]
 expectedAB=[[3*int(i==j)for j in range(10)]for i in range(10)]
 for i in range(10):expectedAB[i][j0]=w[i]
 assert AB==expectedAB and w[j0]==1
 assert all(sum(AB[i][k]*W[j][k]for k in range(10))==3*V[j][i]for j in range(13)for i in range(10))
 H=f['integer_gram'];d=f['gram_denominator'];q=[[F(t,d)for t in row]for row in H]
 assert all(H[i][j]==H[j][i]for i in range(10)for j in range(10))
 sv,nodes,diag=exact_short_vectors(q,F(1));target={tuple(v)for v in W}|{tuple(-x for x in v)for v in W}
 assert len(target)==26 and set(sv)==target and all(gram_value(q,v)==1 for v in W)
 assert matrix_rank([[v[i]*v[j]for i in range(10)for j in range(i,10)]for v in W])==13
 assert odd_witness(tuple(orb['state']),B,group,shifts)is None
 form_reports.append({'record':rid,'orbit':oid,'positive_definite':True,'minimum_pairs':13,'nodes':nodes,'quadratic_rank':13,'maximal_basis_index':3,'minimum_lattice_index':3,'orientation_reversing_stabilizer':False})
assert seen=={(rid,i+1)for rid,(B,orbs,group,shifts)in retained.items()for i in range(len(orbs))}
output={'coverage_input':'Published complete five-class Delta1 rank3 polytope list, Averkov-Schymura2024 section5.2 Table2 p85; not independently reclassified here.','classification':reports,'retained_cells':26,'all_retained_cells_exactly_realized':True,'forms':form_reports,'all_full_rank_facets_orientation_zero':'Proved by the rank-two Gale/color pigeonhole lemma in the accompanying mathematical proof.','nonboundary_claim':False,'whole_homology_claim':False}
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'states':sum(x['states']for x in reports),'odd':sum(x['odd']for x in reports),'Watson_impossible':sum(x['Watson_impossible']for x in reports),'retained_cells':26,'exact_complete_minimum_certificates':len(form_reports),'nonboundary_claim':False}),flush=True)
