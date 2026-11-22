#!/usr/bin/env python3
"""Exact finite RP3 base certificate for the pending concordance obstruction.

Take the barycentric subdivision of the boundary of the four-dimensional
cross-polytope and quotient its flag complex by the antipodal involution.
The output includes every quotient facet and a Tietze reduction of its
edge-path fundamental-group presentation. No TOP homeomorphism-space
class is constructed or tested by this finite program.
"""
from itertools import combinations, permutations, product
from time import perf_counter
import json

started=perf_counter()
checks=[]
def check(name, condition):
    assert condition,name
    checks.append(name)
def face_sets(facets):
    return [sorted({tuple(t) for s in facets for t in combinations(s,d+1)})
            for d in range(max(map(len,facets)))]
def boundaries(faces):
    result=[[]]
    for d in range(1,len(faces)):
        rows={s:i for i,s in enumerate(faces[d-1])}
        result.append([sum(1<<rows[t] for t in combinations(s,d)) for s in faces[d]])
    return result
def binary_rank(columns):
    pivots={}
    for value in columns:
        while value:
            i=value.bit_length()-1
            if i in pivots:value^=pivots[i]
            else:
                pivots[i]=value
                break
    return len(pivots)
def betti(faces):
    ranks=[0]+[binary_rank(c) for c in boundaries(faces)[1:]]+[0]
    return [len(faces[d])-ranks[d]-ranks[d+1] for d in range(len(faces))]
def antipode(face):return tuple(sorted(-x for x in face))

cross_facets=sorted(tuple(sorted(s*(i+1) for i,s in enumerate(signs)))
                    for signs in product((-1,1),repeat=4))
cross_faces=face_sets(cross_facets)
check('cross-polytope boundary f-vector',list(map(len,cross_faces))==[8,24,32,16])
check('cross-polytope boundary mod2 Betti',betti(cross_faces)==[1,0,0,1])
all_faces=sorted({f for level in cross_faces for f in level},key=lambda f:(len(f),f))
cover_id={f:i for i,f in enumerate(all_faces)}
orbit_reps=sorted({min(f,antipode(f)) for f in all_faces},key=lambda f:(len(f),f))
orbit_id={f:i for i,f in enumerate(orbit_reps)}
vertex_map={cover_id[f]:orbit_id[min(f,antipode(f))] for f in all_faces}
for f in all_faces:
    check('antipodal face disjoint '+str(f),not set(f)&set(antipode(f)))
    check('antipodal face present '+str(f),antipode(f) in cover_id)

cover_facets=set()
for facet in cross_facets:
    for order in permutations(facet):
        flag=[tuple(sorted(order[:k])) for k in range(1,5)]
        cover_facets.add(tuple(sorted(cover_id[f] for f in flag)))
cover_facets=sorted(cover_facets)
quotient_facets=sorted({tuple(sorted(vertex_map[v] for v in s)) for s in cover_facets})
for s in cover_facets:
    check('flag quotient no vertex collision '+str(s),len({vertex_map[v] for v in s})==4)
for s in quotient_facets:
    check('two maximal lifts '+str(s),sum(tuple(sorted(vertex_map[v] for v in t))==s
                                          for t in cover_facets)==2)
faces=face_sets(quotient_facets)
cover_faces=face_sets(cover_facets)
fvector=list(map(len,faces))
check('quotient f-vector',fvector==[40,232,384,192])
check('cover f-vector',list(map(len,cover_faces))==[80,464,768,384])
check('quotient Euler zero',sum((-1)**d*n for d,n in enumerate(fvector))==0)
check('quotient mod2 Betti',betti(faces)==[1,1,1,1])
check('subdivided sphere mod2 Betti',betti(cover_faces)==[1,0,0,1])

qsets=[frozenset(s) for s in quotient_facets]
csets=[frozenset(s) for s in cover_facets]
for f in all_faces:
    v=cover_id[f]
    qv=vertex_map[v]
    cover_star={s for s in cover_facets if v in s}
    image={tuple(sorted(vertex_map[w] for w in s)) for s in cover_star}
    quotient_star={s for s in quotient_facets if qv in s}
    check('star maps bijectively '+str(v),len(image)==len(cover_star) and image==quotient_star)

for d in range(3):
    for s in faces[d]:
        sigma=frozenset(s)
        link=face_sets(sorted({tuple(sorted(f-sigma)) for f in qsets if sigma<=f}))
        expected=[0]*(3-d)
        expected[0]=1
        expected[-1]+=1
        check('quotient sphere link '+str(s),betti(link)==expected)
for s in faces[2]:
    check('two tetrahedra on triangle '+str(s),sum(set(s)<=f for f in qsets)==2)
cols=boundaries(faces)
for d in (2,3):
    for k,c in enumerate(cols[d]):
        result=0
        while c:
            low=c&-c
            result^=cols[d-1][low.bit_length()-1]
            c^=low
        check(f'boundary square d{d} column{k}',result==0)

# Edge-path presentation after collapsing one deterministic spanning tree.
parent=list(range(40))
def find(v):
    while parent[v]!=v:
        parent[v]=parent[parent[v]]
        v=parent[v]
    return v
tree=[]
non_tree=[]
for e in faces[1]:
    u,v=e
    if find(u)!=find(v):
        parent[find(u)]=find(v)
        tree.append(e)
    else:non_tree.append(e)
check('spanning tree has39 edges',len(tree)==39 and len({find(v) for v in range(40)})==1)
edge_gen={e:i+1 for i,e in enumerate(non_tree)}
def edge_word(u,v):
    g=edge_gen.get(tuple(sorted((u,v))),0)
    return [] if not g else [g if u<v else -g]
def reduce_word(word,cyclic=False):
    out=[]
    for x in word:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    if cyclic:
        while len(out)>1 and out[0]==-out[-1]:out=out[1:-1]
    return out
def inverse(word):return [-x for x in word[::-1]]
original_relations=[reduce_word(edge_word(u,v)+edge_word(v,w)+edge_word(w,u),True)
                    for u,v,w in faces[2]]
relations=[r for r in original_relations if r]
active=set(range(1,len(non_tree)+1))
steps=[]
while True:
    pivot=None
    for ri,r in enumerate(relations):
        for g in sorted({abs(x) for x in r}):
            if sum(abs(x)==g for x in r)==1:
                pivot=(ri,g)
                break
        if pivot:break
    if not pivot:break
    ri,g=pivot
    r=relations[ri]
    k=next(i for i,x in enumerate(r) if abs(x)==g)
    tail=r[k+1:]+r[:k]
    replacement=inverse(tail) if r[k]>0 else tail
    check('Tietze replacement excludes pivot '+str(g),all(abs(x)!=g for x in replacement))
    updated=[]
    for j,old in enumerate(relations):
        if j==ri:continue
        new=[]
        for x in old:
            new.extend(replacement if x==g else inverse(replacement) if x==-g else [x])
        new=reduce_word(new,True)
        if new:updated.append(new)
    steps.append({'eliminated_generator':g,'pivot_relation':r,'replacement_word':replacement})
    relations=updated
    active.remove(g)
check('one fundamental-group generator remains',len(active)==1)
last=next(iter(active))
check('remaining relations all square of generator',bool(relations) and
      all(len(r)==2 and r[0]==r[1] and abs(r[0])==last for r in relations))

print(json.dumps({
    'status':'PASS','checks':len(checks),'failures':0,'elapsed_seconds':perf_counter()-started,
    'construction':'Antipodal quotient of barycentric boundary of the4-cross-polytope',
    'vertex_orbit_representatives':orbit_reps,'all_quotient_facets':quotient_facets,
    'face_vector':fvector,'cover_face_vector':list(map(len,cover_faces)),
    'betti_mod2':betti(faces),'cover_betti_mod2':betti(cover_faces),
    'spanning_tree':tree,'non_tree_edges_in_generator_order':non_tree,
    'original_triangle_relations':original_relations,'tietze_steps':steps,
    'remaining_generator':last,'remaining_relations':relations,
    'fundamental_group':'C2 by exact elementary Tietze eliminations',
    'mathematical_scope':'Finite base only. The free antipodal sphere quotient proves PL RP3; local star bijections check the2-sheeted covering; this program does not construct or test a TOP concordance class.'
},indent=2))
