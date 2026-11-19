#!/usr/bin/env python3
"""Exact genus-polynomial scalar contractions on the12-vector Levi input.

Work only: each selected scalar row is necessary for the actual mixed
normalizer equation. Completeness of selected rows is not asserted.
"""
from pathlib import Path
from itertools import permutations,product
from functools import lru_cache
from time import perf_counter
import pickle
import sympy as sp

started=perf_counter();s=sp.Symbol('s')
data=pickle.loads(Path(__file__).with_name('calc_levi_single_line_input.pickle').read_bytes())
inputs=data['inputs'];labels=data['labels']

def pairings(items):
    if not items:yield ();return
    a=items[0]
    for j in range(1,len(items)):
        for rest in pairings(items[1:j]+items[j+1:]):yield ((a,items[j]),)+rest

def pair(x,y):
    return (1 if x%2==0 else -1) if x//2==y//2 and x!=y else 0

@lru_cache(maxsize=300000)
def scalar_diagram(key,caps):
    n=len(key);assert sorted(x for cap in caps for x in cap)==list(range(n))
    edge_labels=sorted({x for x in key if x>=0})
    edges={label:tuple(i for i,x in enumerate(key) if x==label) for label in edge_labels}
    adjacency=[[] for _ in range(n)]
    for i,j in caps:
        adjacency[i].append(j);adjacency[j].append(i)
    for i,j in edges.values():
        adjacency[i].append(j);adjacency[j].append(i)
    seen=set();assigned={};loops=0
    for vertex in range(n):
        if vertex in seen:continue
        component=set();todo=[vertex]
        while todo:
            x=todo.pop()
            if x in component:continue
            component.add(x);todo.extend(adjacency[x])
        seen|=component
        omega={key[i] for i in component if key[i]>=0}
        constants=[-key[i]-1 for i in component if key[i]<0]
        if not omega:continue
        if not constants:loops+=1;handle=1
        else:
            assert len(constants)==2
            if any(x//2==0 for x in constants):return 0,0
            if constants[0]//2!=constants[1]//2:return 0,0
            handle=constants[0]//2
        for label in omega:assigned[label]=handle
    coefficient=0
    for bits in product((0,1),repeat=len(edge_labels)):
        values=[-x-1 if x<0 else None for x in key];sign=1
        for label,bit in zip(edge_labels,bits):
            i,j=edges[label];h=assigned[label]
            values[i]=2*h+bit;values[j]=2*h+1-bit
            if bit:sign=-sign
        for i,j in caps:
            sign*=pair(values[i],values[j])
            if not sign:break
        coefficient+=sign
    return coefficient,loops

def canonical_caps(caps):
    sign=1;out=[]
    for i,j in caps:
        if i>j:i,j=j,i;sign=-sign
        out.append((i,j))
    return tuple(sorted(out)),sign

def parity(order):return (-1)**sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))

def bracket_plans():
    # T_delta is minus the alternating tensor for our delta convention.
    for perm in permutations(range(3)):
        E=tuple(8+i for i in perm);wedge_sign=-parity(perm)
        for j in (1,2):
            output=(E[0],)+tuple(x for k in (1,2) for x in (tuple(range(1,8)) if k==j else (E[k],)))
            yield output,(0,E[j]),wedge_sign
        for j in range(1,8):
            output=(0,)+tuple(x for k in range(1,8) for x in (E[1:] if k==j else (k,)))
            yield output,(E[0],j),-wedge_sign

rterms=[(-2,((0,1),(2,4),(3,6),(5,7))),
        (2,((0,1),(2,5),(3,6),(4,7))),
        (2,((0,1),(2,5),(3,7),(4,6))),
        (2,((0,1),(2,6),(3,5),(4,7))),
        (1,((0,2),(1,5),(3,6),(4,7)))]

def plans_R():
    plans={}
    for output,glue,sign in bracket_plans():
        for coefficient,pairs in rterms:
            caps,orientation=canonical_caps((glue,)+tuple((output[i],output[j]) for i,j in pairs)+((output[8],11),))
            plans[caps]=plans.get(caps,0)+sign*coefficient*orientation
    return {caps:c for caps,c in plans.items() if c}

def plans_ES(chord):
    plans={}
    for output,glue,sign in bracket_plans():
        tail=output[2:]
        for rotation in range(7):
            word=tail[rotation:]+tail[:rotation]
            caps,orientation=canonical_caps((glue,(output[0],output[1]))+
               tuple((word[i],word[j]) for i,j in chord)+((word[6],11),))
            plans[caps]=plans.get(caps,0)+sign*orientation
    return {caps:c for caps,c in plans.items() if c}

def evaluate(poly,constants,plans):
    coefficients=[0]*5
    for key,c in poly.items():
        extended=key+constants
        for caps,d in plans.items():
            value,loops=scalar_diagram(extended,caps)
            coefficients[loops]+=c*d*value
    return sum(c*s**i for i,c in enumerate(coefficients))

chords=list(pairings(tuple(range(8))))
detector=[chords[i] for i in (0,1,2,7,13)]
K=sp.Matrix([[evaluate(T,(),{chord:1}) for T in inputs] for chord in detector])
print('INPUT_LABELS',labels,flush=True)
print('FIVE_DETECTOR_MATRIX',K.tolist(),flush=True)
pure=[i for i,label in enumerate(labels) if label[0]=='pure']
pure_det=sp.factor(K[:,pure].det())
print('PURE_DETECTOR_DETERMINANT',pure_det,flush=True)
assert pure_det.subs(s,3)!=0

J=sp.Matrix([[-104,-288],[-26,-72],[104,288],[32,192],[-32,-192]])
L=sp.Matrix.hstack(*J.T.nullspace()).T
assert L.shape==(3,5) and L*J==sp.zeros(3,2)
LK=L*K
print('OUTPUT_QUOTIENT_MATRIX',LK.tolist(),flush=True)

R=plans_R();print('R_PLAN_COUNT',len(R),flush=True)
tests=[('abx',(-1,-2,-3,-4)),('axy',(-1,-3,-4,-2)),('xyu',(-3,-4,-5,-6))]
rows=[];names=[]
for name,constants in tests:
    row=[sp.factor(evaluate(T,constants,R)) for T in inputs]
    rows.append(row);names.append('R_'+name)
    print('ROW',names[-1],row,flush=True)
M=sp.Matrix(rows)
for genus_parameter in (3,4,5):
    A=M.subs(s,genus_parameter);B=LK.subs(s,genus_parameter)
    print('AT_s',genus_parameter,'RANK',A.rank(),'JOINED_OUTPUT_RANK',A.col_join(B).rank(),flush=True)
with Path(__file__).with_suffix('.pickle').open('wb') as file:
    pickle.dump(dict(input_labels=labels,K=K,L=L,LK=LK,rows=rows,names=names,s=s),file)
print('SCOPE: selected exact scalar rows only; no all-genus kernel inclusion claimed.')
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
