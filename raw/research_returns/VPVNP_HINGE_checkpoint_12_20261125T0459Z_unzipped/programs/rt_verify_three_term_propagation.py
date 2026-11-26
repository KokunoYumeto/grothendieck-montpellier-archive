"""Independent semantic replay of the complete width-six, D=3, A=3 proof.

No propagation, optimizer, or certificate-generator code is imported.
Each retained update is reconstructed from the necessary integer inequality.
"""
from pathlib import Path
from itertools import permutations,combinations_with_replacement,product
from collections import Counter
import json,hashlib

W=Path(__file__).resolve().parents[1]
P=W/'outputs/sh_three_term_pattern_all.json'
data=json.loads(P.read_text())

def ceiling(v):
    if v<=1:return 0
    k=0
    while 2**k<v:k+=1
    return k

def valid_weight(w,target):
    if w==1:assert target==(67*4096+48)//49
    elif w==3:assert target==8192
    else:
        roots=[z for z in range(2,65)if z*z==w]
        assert len(roots)==1 and target==4096*roots[0]

expected={(t,b,pat)for t in range(9)for b in range(2)
          for pat in combinations_with_replacement(range(9),3)}
seen=set();counts=Counter();survivors=[];updates=0
for case in data['cases']:
    t,b,pat=case['minimum'],case['base'],tuple(case['patterns'])
    key=t,b,pat;assert key in expected and key not in seen;seen.add(key)
    patterns=sorted(set(permutations((18,t,t)))|set(permutations((17,17,t)))|
                    set(permutations((17,16,16))))
    columns=[(t,18,t)if b==0 else(t,17,17)]+[patterns[i]for i in pat]
    lo=[[columns[c][a]for c in range(4)]for a in range(3)]
    hi=[[18]*4 for _ in range(3)];hi[0][0]=t
    for entry in case['trace']:
        kind,a,c,value,why,*tail=entry
        assert kind in('lower','upper')and 0<=a<3 and 0<=c<4
        if why=='budget':
            assert kind=='upper' and not tail
            bound=52-sum(lo[a][j]for j in range(4)if j!=c)
        elif why=='lipschitz':
            u,=tail;assert 0<=u<4 and u!=c
            bound=lo[a][u]-12 if kind=='lower'else hi[a][u]+12
        elif why=='single_cut':
            assert kind=='lower'and not tail
            bound=ceiling(2**18-sum(2**hi[j][c]for j in range(3)if j!=a))
        else:
            assert why=='weighted'and kind=='lower'
            s,u,weight,target,side=tail
            assert 0<=s<4 and 0<=u<4 and s!=u and side in(0,1)
            assert c==(s,u)[side];valid_weight(weight,target)
            residual=target-sum(min(2**hi[j][s],weight*2**hi[j][u])
                                for j in range(3)if j!=a)
            assert residual>0
            bound=ceiling(residual if side==0 else(residual+weight-1)//weight)
        assert bound==value,(key,entry,bound)
        table=lo if kind=='lower'else hi
        assert value>table[a][c]if kind=='lower'else value<table[a][c]
        table[a][c]=value;updates+=1
    if case['excluded']:
        why,*tail=case['contradiction']
        if why=='bounds':
            a,c=tail;assert lo[a][c]>hi[a][c]
        elif why=='budget':
            a,=tail;assert sum(lo[a])>52
        elif why=='single_cut':
            c,=tail;assert sum(2**hi[a][c]for a in range(3))<2**18
        else:
            assert why=='weighted';s,u,weight,target=tail
            valid_weight(weight,target)
            assert sum(min(2**hi[a][s],weight*2**hi[a][u])for a in range(3))<target
        counts[t]+=1
    else:
        assert lo==case['lower']and hi==case['upper']
        survivors.append((t,b,list(pat),lo,hi))
assert seen==expected
assert [(t,b,p)for t,b,p,_,_ in survivors]==[(t,0,[0,8,8])for t in(6,7,8)]
analytic=[]
for t,b,pat,lo,hi in survivors:
    assert lo==[[t,t,18,18],[18,t,t,t],[t,18,t,t]]
    assert hi==[[t,16-t,18,18],[18,18,18,18],[18,18,18,18]]
    B,C=5601-2**t,5601-2**(16-t)
    assert B>4096 and C>4096
    # If u or v<=11, the other row's three unknown ceilings are>=12.
    assert B-2048>2048 and C-2048>2048 and 3*12>34
    z=2**(11-t);assert 1<=z<=64
    assert z*4096-z*z*2**t==2**(22-t)
    pairs=[(a,b)for a in range(t,19)for b in range(t,19)if 2**a+2**b>=2**(22-t)]
    assert min(a+b for a,b in pairs)==22
    assert {(a,b)for a,b in pairs if a+b==22}=={(t,22-t),(22-t,t)}
    assert 4096+2**(t+1)<5601
    assert 4096+2**t+2**(16-t)<5601
    analytic.append({'minimum':t,'B':B,'C':C,'parameter':z,'status':'PASS'})
out={'status':'PASS','input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
     'branches':len(seen),'propagation_exclusions':sum(counts.values()),
     'replayed_updates':updates,'excluded_by_minimum':dict(counts),
     'analytic_survivor_checks':analytic,'solver_used':False,'generator_imported':False,
     'coverage_justification':'Globalminimum<=8 is a separate hand proof. Fix its summand and cut; other cuts are symmetric. Each cut dominates a permutation of(18,t,t),(17,17,t),(17,16,16). At base cut only(t,18,t)or(t,17,17)are needed after swapping the other summands.'}
(W/'outputs/rt_three_term_propagation_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
