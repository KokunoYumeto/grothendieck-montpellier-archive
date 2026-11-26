#!/usr/bin/env python3
"""Bounded exact branch exploration for the D4 three-term rank relaxation.

All arithmetic deductions are integer statements. An unfinished tree or
a surviving interval box is explicitly not an exclusion.
"""
import itertools
import json
import sys
import time
from pathlib import Path


class Contradiction(Exception):
    def __init__(self,reason):self.reason=reason


def clog(value):
    return max(0,(value-1).bit_length()) if value>0 else 0


def propagate(lower,upper):
    trace=[]
    def update(kind,a,s,value,reason):
        table=lower if kind=='lower' else upper
        if (kind=='lower' and value<=table[a][s]) or (kind=='upper' and value>=table[a][s]):return False
        table[a][s]=value;trace.append([kind,a,s,value]+reason)
        if lower[a][s]>upper[a][s]:raise Contradiction(['bounds',a,s])
        return True
    try:
        for a in range(3):
            for s in range(8):
                if lower[a][s]>upper[a][s]:raise Contradiction(['bounds',a,s])
        while True:
            changed=False
            for a in range(3):
                total=sum(lower[a])
                if total>141:raise Contradiction(['budget',a])
                for s in range(8):changed|=update('upper',a,s,141-total+lower[a][s],['budget'])
                for s in range(8):
                    for u in range(8):
                        raw=(s^u).bit_count();h=min(raw,4-raw)
                        if h:
                            changed|=update('lower',a,s,lower[a][u]-12*h,['lipschitz',u,h])
                            changed|=update('upper',a,s,upper[a][u]+12*h,['lipschitz',u,h])
            for s in range(8):
                caps=[2**upper[a][s] for a in range(3)]
                if sum(caps)<2**24:raise Contradiction(['single_cut',s])
                for a in range(3):
                    residual=2**24-sum(caps[b] for b in range(3) if b!=a)
                    changed|=update('lower',a,s,clog(residual),['single_cut'])
            for s in range(8):
                for u in range(8):
                    raw=(s^u).bit_count();h=min(raw,4-raw)
                    if not h:continue
                    p,q=2**(6*(4-h)),2**(6*h)
                    specs=[(1,(67*p+48)//49),(3,2*p)]
                    specs += [(z*z,z*p) for z in (2**e for e in range(1,6*h+1))]
                    for weight,target in specs:
                        caps=[min(2**upper[a][s],weight*2**upper[a][u]) for a in range(3)]
                        if sum(caps)<target:raise Contradiction(['weighted',s,u,weight,target])
                        for a in range(3):
                            residual=target-sum(caps[b] for b in range(3) if b!=a)
                            if residual>0:
                                changed|=update('lower',a,s,clog(residual),['weighted',s,u,weight,target,0])
                                changed|=update('lower',a,u,clog((residual+weight-1)//weight),['weighted',s,u,weight,target,1])
            if not changed:return trace,None
    except Contradiction as error:return trace,error.reason


def main():
    config=json.loads(Path(sys.argv[1]).read_text())
    started=time.monotonic();nodes=[];roots=[];survivors=[];stopped=False
    for t in config['minima']:
        patterns=sorted(set(itertools.permutations((24,t,t)))|
                        set(itertools.permutations((23,23,t)))|
                        set(itertools.permutations((23,22,22))))
        cache={}
        def visit(lower,upper):
            nonlocal stopped
            key=tuple(sum(lower,[])+sum(upper,[]))
            if key in cache:return cache[key]
            index=len(nodes);cache[key]=index
            node=dict(minimum=t,initial_lower=[r[:] for r in lower],initial_upper=[r[:] for r in upper])
            nodes.append(node)
            if len(nodes)>=config.get('max_nodes',20000) or time.monotonic()-started>config.get('seconds',90):
                node['status']='interrupted';stopped=True;return index
            trace,contradiction=propagate(lower,upper);node['trace']=trace
            if contradiction:
                node.update(status='excluded',contradiction=contradiction);return index
            choices=[]
            for s in range(8):
                if sum(2**lower[a][s] for a in range(3))>=2**24:continue
                allowed=[j for j,p in enumerate(patterns) if all(p[a]<=upper[a][s] for a in range(3))]
                choices.append((len(allowed),min((s^0).bit_count(),4-(s^0).bit_count()),s,allowed))
            if not choices:
                node.update(status='survivor',lower=lower,upper=upper);survivors.append(index);return index
            _,_,s,allowed=min(choices)
            assert allowed
            node.update(status='split',cut=s,children=[],omitted=[j for j in range(9) if j not in allowed],
                        lower=lower,upper=upper)
            for j in allowed:
                lb=[r[:] for r in lower];ub=[r[:] for r in upper]
                for a in range(3):lb[a][s]=max(lb[a][s],patterns[j][a])
                child=visit(lb,ub);node['children'].append([j,child])
                if stopped:break
            if len(node['children'])<len(allowed):node['status']='interrupted_split'
            return index
        for base in range(2):
            lower=[[t]*8 for _ in range(3)];upper=[[24]*8 for _ in range(3)]
            upper[0][0]=t
            lower[1][0]=24 if base==0 else 23
            if base:lower[2][0]=23
            roots.append(dict(minimum=t,base=base,node=visit(lower,upper)))
            if stopped:break
        print(json.dumps(dict(minimum=t,nodes=len(nodes),survivors=len(survivors),stopped=stopped)),flush=True)
        if stopped:break
    out=dict(config=config,roots=roots,nodes=nodes,survivors=survivors,complete=not stopped,
             seconds=time.monotonic()-started,
             claim='Only a complete independently replayed tree with no surviving boxes would prove an exclusion.')
    path=Path(sys.argv[2]);temporary=path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(out,separators=(',',':')));temporary.replace(path)


if __name__=='__main__':main()
