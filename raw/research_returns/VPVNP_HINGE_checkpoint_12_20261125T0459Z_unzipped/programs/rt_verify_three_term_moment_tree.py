#!/usr/bin/env python3
"""Independent semantic replay of the D4 three-term moment proof tree.

No generator, propagation engine, optimizer or solver is imported. Every
deduction is reconstructed from the proved rank and geometric inequalities;
all roots, omitted patterns, child boxes and reachable nodes are checked.
"""
from pathlib import Path
from itertools import permutations
from collections import Counter
import sys,json,hashlib,math

w=Path(__file__).resolve().parents[1]
cfg=json.loads(Path(sys.argv[1]).read_text())
p=w/cfg['certificate']
raw=p.read_bytes();data=json.loads(raw)
assert data['complete'] is True and not data['survivors']
assert data['model']['dimension']==4 and data['model']['width']==6 and data['model']['terms']==3
assert data['model']['linear_budget']==141 and data['model']['quadratic_budget']==2496
assert (2809*4**2*8-1)//144==2496 and (53*4*8-1)//12==141
nodes=data['nodes'];counts=Counter();updates=0;visited=set();active=set()

# Independent finite verification of the global-minimum reduction. Under
# minimum14, every row has weight at most10, whereas eight cuts require32.
states={0:0}
for _ in range(8):
    nxt={}
    for total,weight in states.items():
        for k in range(14,25):
            t=total+k
            if t<=141:
                v=weight+({22:1,23:2,24:4}.get(k,0))
                nxt[t]=max(nxt.get(t,-1),v)
    states=nxt
maxweight=max(states.values())
assert maxweight==10 and 3*maxweight<8*4

def ceil_log(v):
    if v<=1:return 0
    r=0
    while (1<<r)<v:r+=1
    return r

def dist(s,t):
    assert 0<=s<8 and 0<=t<8 and s!=t
    h=sum(((s>>i)&1)!=((t>>i)&1) for i in range(3))
    return min(h,4-h)

def valid_weight(s,t,weight,target):
    h=dist(s,t);P=1<<(6*(4-h));Q=1<<(6*h)
    if weight==1:
        assert target==(67*P+48)//49
    elif weight==3:
        assert target==2*P
    else:
        z=math.isqrt(weight)
        assert z*z==weight and 1<=z<=Q and target==z*P

def patterns(t):
    return sorted(set(permutations((24,t,t)))|set(permutations((23,23,t)))|set(permutations((23,22,22))))

def visit(i,t,lo0,hi0):
    global updates
    assert isinstance(i,int) and 0<=i<len(nodes)
    node=nodes[i]
    assert node['minimum']==t and node['initial_lower']==lo0 and node['initial_upper']==hi0
    assert i not in active,'Cycle in proof graph'
    if i in visited:return
    active.add(i)
    lo=[r[:] for r in lo0];hi=[r[:] for r in hi0]
    assert len(lo)==len(hi)==3 and all(len(r)==8 for r in lo+hi)
    assert all(isinstance(v,int) and 0<=v<=24 for r in lo+hi for v in r)
    for entry in node.get('trace',[]):
        kind,a,c,value,why,*tail=entry
        assert kind in ('lower','upper') and 0<=a<3 and 0<=c<8 and isinstance(value,int)
        if why=='budget':
            assert kind=='upper' and not tail
            bound=141-sum(lo[a][j] for j in range(8) if j!=c)
        elif why=='quadratic_budget':
            assert kind=='upper' and not tail
            remainder=2496-sum(lo[a][j]**2 for j in range(8) if j!=c)
            assert remainder>=0
            bound=math.isqrt(remainder)
        elif why=='lipschitz':
            u,h=tail;assert h==dist(c,u)
            bound=lo[a][u]-12*h if kind=='lower' else hi[a][u]+12*h
        elif why=='single_cut':
            assert kind=='lower' and not tail
            bound=ceil_log((1<<24)-sum(1<<hi[j][c] for j in range(3) if j!=a))
        else:
            assert why=='weighted' and kind=='lower'
            s,u,weight,target,side=tail
            assert side in (0,1) and c==(s,u)[side]
            valid_weight(s,u,weight,target)
            residual=target-sum(min(1<<hi[j][s],weight*(1<<hi[j][u])) for j in range(3) if j!=a)
            assert residual>0
            bound=ceil_log(residual if side==0 else (residual+weight-1)//weight)
        assert bound==value,(i,entry,bound)
        table=lo if kind=='lower' else hi
        assert (value>table[a][c]) if kind=='lower' else (value<table[a][c])
        table[a][c]=value;updates+=1
    status=node['status'];counts[status]+=1
    if status=='excluded':
        why,*tail=node['contradiction']
        if why=='bounds':
            a,c=tail;assert lo[a][c]>hi[a][c]
        elif why=='budget':
            a,=tail;assert sum(lo[a])>141
        elif why=='quadratic_budget':
            a,=tail;assert sum(v*v for v in lo[a])>2496
        elif why=='single_cut':
            c,=tail;assert sum(1<<hi[a][c] for a in range(3))<(1<<24)
        else:
            assert why=='weighted'
            s,u,weight,target=tail;valid_weight(s,u,weight,target)
            assert sum(min(1<<hi[a][s],weight*(1<<hi[a][u])) for a in range(3))<target
        counts['contradiction:'+why]+=1
    else:
        assert status=='split'
        assert node['lower']==lo and node['upper']==hi
        s=node['cut'];assert 0<=s<8
        assert sum(1<<lo[a][s] for a in range(3))<(1<<24)
        pats=patterns(t);assert len(pats)==9
        admissible={j for j,pat in enumerate(pats) if all(pat[a]<=hi[a][s] for a in range(3))}
        omitted=set(node['omitted'])
        assert len(omitted)==len(node['omitted']) and omitted==set(range(9))-admissible
        child_patterns=[j for j,_ in node['children']]
        assert len(child_patterns)==len(set(child_patterns)) and set(child_patterns)==admissible
        for j,child in node['children']:
            clo=[r[:] for r in lo]
            for a in range(3):clo[a][s]=max(clo[a][s],pats[j][a])
            assert clo!=lo
            visit(child,t,clo,[r[:] for r in hi])
    active.remove(i);visited.add(i)

expected={(t,b) for t in range(14) for b in range(2)};seen=set()
for root in data['roots']:
    t,b=root['minimum'],root['base'];assert (t,b) in expected and (t,b) not in seen
    seen.add((t,b))
    lo=[[t]*8 for _ in range(3)];hi=[[24]*8 for _ in range(3)];hi[0][0]=t
    lo[1][0]=24 if b==0 else 23
    if b:lo[2][0]=23
    visit(root['node'],t,lo,hi)
assert seen==expected and len(visited)==len(nodes) and not active
out={'status':'PASS','certificate':cfg['certificate'],'certificate_sha256':hashlib.sha256(raw).hexdigest(),
     'roots':len(seen),'nodes':len(nodes),'reachable_nodes':len(visited),'replayed_updates':updates,
     'counts':dict(counts),'global_minimum_upper_bound':13,'baseline14_maximum_row_weight':maxweight,
     'generator_imported':False,'solver_used':False,'all_arithmetic':'integers',
     'coverage':'All minima0..13 and both normalized base patterns; each split covers all nine minimal rank patterns compatible with its exact upper box. Every retained node is reachable and excluded or completely split.',
     'source_rows':'SH55 geometric moments; SH39 rectangular weighted ranks; SH44 rectangular Singh bound; SH48 minimum reduction.'}
Path(sys.argv[2]).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
