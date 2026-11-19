#!/usr/bin/env python3
"""Modular discovery comparison with explicit degree-six Johnson brackets."""
from pathlib import Path
import pickle
import random
source=Path(__file__).with_name('calc_genus_three_partial_trace.py').read_text()
exec(compile(source.split('Ds=[];Dlabels=[]')[0],str(Path(__file__)), 'exec'))

deltas=[];names=[]
for triple in combinations(alphabet,3):
    a,b,c=triple
    delta={x:add(add(scale(bracket(v[b],v[c]),pair(x,a)),
                       scale(bracket(v[c],v[a]),pair(x,b))),
                       scale(bracket(v[a],v[b]),pair(x,c))) for x in alphabet}
    names.append(''.join(triple));deltas.append(delta)
opposite=[]
for name in names:
    other=''.join(sorted(alphabet[alphabet.index(x)^1] for x in name))
    opposite.append(names.index(other))
random.seed(20261119)
vectors=[];programs=[];rank=0
for trial in range(120):
    selected=[random.randrange(20) for _ in range(3)]
    selected+= [opposite[i] for i in selected]
    random.shuffle(selected)
    D=deltas[selected[-1]]
    for i in reversed(selected[:-1]):D=derbracket(deltas[i],D)
    value=contractions(D)
    if not any(value):continue
    test=np.array(vectors+[value],dtype=np.int16).T
    _,newrank=nullspace(test)
    if newrank>rank:
        vectors.append(value);programs.append([names[i] for i in selected]);rank=newrank
        print('NEW_J6_CONTRACTION_RANK_MOD101',rank,'BRACKET',programs[-1],flush=True)
    if trial%10==0:print('TRIAL',trial,'RANK',rank,flush=True)

for n in (1,2):
    path=Path(__file__).with_name('partial_trace_pairs'+str(n)+'.pickle')
    if path.exists():
        with path.open('rb') as f:data=pickle.load(f)
        A=np.array(vectors,dtype=np.int16).T
        combined=np.hstack((A,data['onker']))
        _,joined_rank=nullspace(combined)
        _,own_rank=nullspace(data['onker'])
        print('PAIRS',n,'PARTIAL_KERNEL_CONTRACTION_RANK',own_rank,
              'JOHNSON_RANK',rank,'JOINED_RANK',joined_rank)
with Path(__file__).with_name('partial_J6_contractions.pickle').open('wb') as f:
    pickle.dump(dict(vectors=vectors,programs=programs,rank=rank,prime=prime),f)
print('WORK ONLY: modular comparison; no rational or arithmetic conclusion yet.')
print('ACTUAL_WALL_SECONDS',perf_counter()-started)
