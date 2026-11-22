#!/usr/bin/env python3
r"""Exact finite PL counterexample to 121/049.

X = { -2<=x,y<=2, 0<=z<=2, x<=0 or y>=z or y<=-z }.
T = X intersect {z=0}; A=X\T; S=T intersect {y=0};
R=S intersect {x>=0}.
P=(A,T_plus,T_minus,S), Q=(A,T\R,R).

Use a common staircase triangulation of six triangular prisms.
Check connectedness, global frontiers, local closedness, and frontier
conditions after splitting into connected components in EVERY simplex
open star. Such stars have arbitrarily small combinatorially identical
PL neighbourhoods at points of their carrier simplices. Thus these
finite checks certify strictness for arbitrary open subsets, by the
local-to-global frontier lemma proved in part_A5.tex.
"""
from itertools import combinations
from pathlib import Path
import json
from fractions import Fraction

outdir=Path(__file__).resolve().parents[1]/'logs'
outdir.mkdir(exist_ok=True)
section=[(-2,0),(0,0),(2,0),(-2,2),(0,2),(2,2)]
triangles=[(0,1,3),(1,3,4),(1,4,5),(1,2,5)]
wing_triangles=[triangles[0],triangles[3]]
coord={6*i+j:(x,y,z) for i,x in enumerate((-2,0,2))
       for j,(y,z) in enumerate(section)}
tetra=[]
for slab,ts in [(0,triangles),(1,wing_triangles)]:
    for tri in ts:
        a,b,c=sorted(tri)
        lo=lambda v:6*slab+v
        hi=lambda v:6*(slab+1)+v
        tetra.extend([tuple(sorted(t)) for t in [
            (lo(a),hi(a),hi(b),hi(c)),
            (lo(a),lo(b),hi(b),hi(c)),
            (lo(a),lo(b),lo(c),hi(c))]])
cells=sorted({tuple(s) for t in tetra for r in range(1,5)
              for s in combinations(t,r)}, key=lambda s:(len(s),s))
sets={s:frozenset(s) for s in cells}
face={s:{t for t in cells if sets[t]<=sets[s]} for s in cells}

def labels(s):
    bary=[sum(Fraction(coord[v][j]) for v in s)/len(s) for j in range(3)]
    x,y,z=bary
    if z>0:
        return ('A','A','A')
    p='T_plus' if y>0 else 'T_minus' if y<0 else 'S'
    q='R' if y==0 and x>=0 else 'B'
    return (p,q,'T')
lab={s:labels(s) for s in cells}

def components(domain):
    todo=set(domain); result=[]
    while todo:
        seed=min(todo,key=lambda s:(len(s),s)); todo.remove(seed)
        done={seed}; frontier=[seed]
        while frontier:
            s=frontier.pop()
            new={t for t in todo if sets[t]<=sets[s] or sets[s]<=sets[t]}
            todo-=new; done|=new; frontier.extend(new)
        result.append(done)
    return result

def partition_components(domain,k):
    ans=[]
    for label in sorted({lab[s][k] for s in domain}):
        for c in components({s for s in domain if lab[s][k]==label}):
            ans.append((label,c))
    return ans

def frontier_check(domain,k):
    pcs=partition_components(domain,k)
    for label,c in pcs:
        closure=set().union(*(face[s] for s in c)) & domain
        for other,d in pcs:
            if closure & d and not d<=closure:
                return {'source_label':label,'target_label':other,
                        'source_cells':[list(s) for s in sorted(c)],
                        'target_hit':list(min(closure&d,key=lambda s:(len(s),s))),
                        'target_missed':list(min(d-closure,key=lambda s:(len(s),s)))}
    return None

def locally_closed(k):
    # A union of open simplices is locally closed iff its carrier set
    # is order-convex in the face poset.
    for label in sorted({lab[s][k] for s in cells}):
        chosen={s for s in cells if lab[s][k]==label}
        for top in chosen:
            for bot in chosen & face[top]:
                for mid in face[top]:
                    if sets[bot]<=sets[mid] and mid not in chosen:
                        return False
    return True

summary={}
for k,name in enumerate(('P','Q','join')):
    connected={label:len(components({s for s in cells if lab[s][k]==label}))
               for label in sorted({lab[s][k] for s in cells})}
    failures=[]
    for carrier in cells:
        domain={s for s in cells if sets[carrier]<=sets[s]}
        fail=frontier_check(domain,k)
        if fail is not None:
            failures.append({'carrier':list(carrier),
                             'carrier_coordinates':[coord[v] for v in carrier],**fail})
    summary[name]={'leaf_component_counts':connected,
                   'locally_closed':locally_closed(k),
                   'global_frontier':frontier_check(set(cells),k) is None,
                   'star_checks':len(cells),
                   'failed_stars':len(failures),
                   'first_failure':failures[0] if failures else None}
    if name in ('P','Q'):
        assert all(n==1 for n in connected.values())
        assert summary[name]['locally_closed'] and summary[name]['global_frontier']
        assert not failures
    else:
        assert failures
# Force the transparent failure at the interior of the positive x-axis edge.
axis_edge=tuple(sorted((7,13)))
assert axis_edge in cells
axis_domain={s for s in cells if sets[axis_edge]<=sets[s]}
axis_fail=frontier_check(axis_domain,2)
assert axis_fail is not None
# Connected join of the P and Q labels within T.
join_edges={(lab[s][0],lab[s][1]) for s in cells if lab[s][2]=='T'}
assert ('S','B') in join_edges and ('S','R') in join_edges
assert ('T_plus','B') in join_edges and ('T_minus','B') in join_edges
# Independent exact volume calculation checks that the 18 tetrahedra
# fill the intended prism volume: 2*8 + 2*(2+2) = 24.
def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))
volume=Fraction(0)
for t in tetra:
    p=coord[t[0]]
    vectors=[tuple(coord[v][j]-p[j] for j in range(3)) for v in t[1:]]
    d=abs(det3(*vectors)); assert d>0
    volume+=Fraction(d,6)
assert volume==24
payload={'vertices':{str(v):coord[v] for v in sorted(set().union(*sets.values()))},
         'tetrahedra':[list(t) for t in tetra],
         'cells':[{'vertices':list(s),'P':lab[s][0],'Q':lab[s][1],'join':lab[s][2]}
                  for s in cells],
         'f_vector':[sum(len(s)==d+1 for s in cells) for d in range(4)],
         'exact_volume':str(volume),'summary':summary,
         'positive_axis_failure':axis_fail,
         'join_edges':[list(e) for e in sorted(join_edges)]}
(outdir/'A5_strict_no_coarsest.json').write_text(json.dumps(payload,indent=2)+'\n')
lines=[f"f-vector = {payload['f_vector']}", f'exact volume = {volume}']
for name,s in summary.items():
    lines += [f"{name}: leaf component counts = {s['leaf_component_counts']}",
              f"{name}: locally closed = {s['locally_closed']}; global frontier = {s['global_frontier']}",
              f"{name}: {s['star_checks']} simplex-star checks; failures = {s['failed_stars']}"]
lines += ['positive-axis carrier = '+str([coord[v] for v in axis_edge]),
          'positive-axis failure = '+json.dumps(axis_fail,sort_keys=True),
          'common-coarsening incidence = '+str(sorted(join_edges)),
          'PASS: P and Q are strict; their only T-adapted common coarsening is not strict.']
text='\n'.join(lines)+'\n'
(outdir/'A5_strict_no_coarsest.txt').write_text(text)
print(text,end='')
