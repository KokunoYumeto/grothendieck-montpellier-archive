"""Finite certificates supporting the analytic arguments in proof_checks.md.

No finite truncation is offered as a proof of an infinite-product assertion.
The root run separately computes the finite nerves and the W0 bifibration.
"""
from itertools import permutations, product
from collections import deque
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]

def involutions(n):
    return [p for p in permutations(range(n)) if all(p[p[i]]==i for i in range(n))]

def homlabels(action,s,t):
    return {g for g in (0,1) if (s if g==0 else action[s])==t}

def equivariant(a,b,f):
    return all(f[a[i]]==b[f[i]] for i in range(len(a)))

def action_equivalence(a,b,f):
    ff=all(homlabels(a,s,t)==homlabels(b,f[s],f[t])
           for s in range(len(a)) for t in range(len(a)))
    ess=all(any(t==f[s] or t==b[f[s]] for s in range(len(a)))
            for t in range(len(b)))
    return ff and ess

def components(action):
    todo=set(range(len(action))); out=[]
    while todo:
        x=min(todo); orbit={x,action[x]};todo-=orbit;out.append(sorted(orbit))
    return out

checked=0; equivs=0; mismatches=[]
for n in range(4):
    for m in range(4):
        for a in involutions(n):
            for b in involutions(m):
                for f in product(range(m),repeat=n):
                    if not equivariant(a,b,f): continue
                    checked+=1
                    eq=action_equivalence(a,b,f)
                    bijective=(len(set(f))==n==m)
                    equivs+=eq
                    if eq!=bijective:mismatches.append([a,b,f,eq,bijective])
assert not mismatches

regular=(1,0)
pairs=list(product(range(2),repeat=2))
diagonal_action=tuple(pairs.index((regular[x],regular[y])) for x,y in pairs)
fence=[]
for n in range(1,21):
    adjacency={i:set() for i in range(n+1)}
    for i in range(n):
        adjacency[i].add(i+1);adjacency[i+1].add(i)
    d={0:0};q=deque([0])
    while q:
        i=q.popleft()
        for j in adjacency[i]:
            if j not in d:d[j]=d[i]+1;q.append(j)
    assert d[n]==n
    fence.append({'n':n,'vertices':n+1,'nonidentity_arrows':n,'nondegenerate_higher_simplices':0,'endpoint_distance':d[n]})

out={
 'date':'2026-11-19',
 'action_groupoid_equivalence':{'claim':'SA27-C407','all_involution_actions_on_sizes':list(range(4)),
    'equivariant_maps_checked':checked,'equivalences':equivs,'mismatches_with_underlying_bijection':mismatches},
 'regular_C2':{'action':regular,'components':components(regular),
    'diagonal_product_action':diagonal_action,'diagonal_product_components':components(diagonal_action),
    'product_of_action_groupoids_component_count':1},
 'fence_diagnostics':{'claims':['SA27-C409','SA27-C427'],'rows':fence,
    'limitation':'Finite distances only. The infinite conclusion is the uniform-coordinate bound proved in proof_checks.md §7.'},
 'other_certificates':[
    '../../code/finite_categories.py','../../outputs/finite_categories.json',
    '../../code/groupoid_pi0.py','../../outputs/groupoid_pi0.json',
    '../../code/reused_sheet_arithmetic.py','../../outputs/reused_sheet_arithmetic.json']}
(ROOT/'outputs/check_examples.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
