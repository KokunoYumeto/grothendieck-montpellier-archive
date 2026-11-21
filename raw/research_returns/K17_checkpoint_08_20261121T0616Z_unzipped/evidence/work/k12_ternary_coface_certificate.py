"""Exact 26-coface certificate. Standard library; no optimization or network.
Run beside k12_ternary_coface_data.json and k12_ternary_glue_form_data.json.
The old-cell orientation classification is a separately replayable input.
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




base=Path(__file__).parent
forms=json.loads((base/'k12_ternary_glue_form_data.json').read_text())
cofaces=json.loads((base/'k12_ternary_coface_data.json').read_text())
old={(r['record'],r['orbit']):r for r in forms}
assert len(old)==26 and len(cofaces)==26
seen=set();reports=[]
for f in cofaces:
 key=(f['record'],f['orbit']);assert key in old and key not in seen;seen.add(key)
 V=old[key]['minimum_vectors'];w=f['new_vector'];target=f['minimum_vectors']
 assert target==V+[w] and len(target)==14
 H=f['integer_gram'];d=f['gram_denominator'];assert d>0
 assert all(H[i][j]==H[j][i]for i in range(10)for j in range(10))
 q=[[F(t,d)for t in row]for row in H]
 sv,nodes,diag=exact_short_vectors(q,F(1))
 signed={tuple(v)for v in target}|{tuple(-x for x in v)for v in target}
 assert len(signed)==28 and set(sv)==signed and all(gram_value(q,v)==1 for v in target)
 assert matrix_rank([[v[i]*v[j]for i in range(10)for j in range(i,10)]for v in target])==14
 relative=set(f['relative_facets']);assert relative=={i for i,b in enumerate(old[key]['gale_columns'])if not any(b)}
 treated=set()
 for wit in f['facet_reflections']:
  i,a,b,e=(wit[k]for k in ('deleted','a','b','sign'))
  assert i not in relative and i not in treated and len({i,a,b})==3 and e in(-1,1)
  treated.add(i);num=wit['phi_ambient_numerator'];assert len(num)==10 and all(x%3==0 for x in num)
  phi=[x//3 for x in num];diff=[e*V[b][j]-V[a][j]for j in range(10)]
  assert sum(phi[j]*diff[j]for j in range(10))==-2
  G=[[int(j==k)+diff[j]*phi[k]for k in range(10)]for j in range(10)]
  assert all(sum(G[j][l]*G[l][k]for l in range(10))==int(j==k)for j in range(10)for k in range(10))
  def action(v):return [sum(G[j][k]*v[k]for k in range(10))for j in range(10)]
  for j,v in enumerate(V):
   if j==i:continue
   expect=[e*x for x in V[b]]if j==a else[e*x for x in V[a]]if j==b else v
   assert action(v)==expect
  assert action(w)==w
  assert matrix_rank([v for j,v in enumerate(target)if j!=i])==10
 for i in relative:
  assert matrix_rank([v for j,v in enumerate(target)if j!=i])==9
 assert treated|relative==set(range(13)) and not treated&relative
 # The new-ray deletion is the previous orientable cell; every other facet
 # is explicitly odd or relative-zero. The accompanying proof supplies the
 # unique-facet orientation and incidence-one conclusion.
 reports.append({'record':key[0],'orbit':key[1],'minimum_pairs':14,'quadratic_rank':14,'exact_enumeration_nodes':nodes,'integral_odd_other_facets':len(treated),'relative_other_facets':len(relative),'all_reflections_fix_new_ray':True,'boundary_coefficient':1})
assert seen==set(old)
out={'scope':'All26 explicit coefficient-one fillings, using the prior exact orientation classification and the unique-facet incidence proof. No whole rank10 homology or K12 vanishing claim.','all_26_fillings_verified':True,'reports':reports,'remaining_target_support':'maximal minimum-basis index at least4','whole_homology_claim':False}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'all_26_fillings_verified':True,'node_range':[min(r['exact_enumeration_nodes']for r in reports),max(r['exact_enumeration_nodes']for r in reports)],'whole_homology_claim':False},indent=2))
