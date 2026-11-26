#!/usr/bin/env python3
"""Exact integer-bound propagation on the D3 three-term high-rank patterns.

Each branch is a necessary lower-bound pattern, not a proposed tensor.
Every exclusion carries a replayable integer deduction trace. Survivors
are only intervals in a relaxation and are explicitly retained.
"""
import itertools
import json
import sys
from pathlib import Path


class Contradiction(Exception):
    def __init__(self, reason):
        self.reason=reason


def ceil_log2(value):
    return max(0,(value-1).bit_length()) if value>0 else 0


def propagate(t, base, pattern_indices, patterns, full_parameters=False):
    columns=[(t,18,t) if base==0 else (t,17,17)]
    columns += [patterns[i] for i in pattern_indices]
    lower=[[columns[s][a] for s in range(4)] for a in range(3)]
    upper=[[18]*4 for _ in range(3)]
    upper[0][0]=t
    trace=[]
    params=range(2,65) if full_parameters else (2,4,8,16,32,64)
    specifications=[(1,(67*4096+48)//49),(3,8192)]
    specifications += [(z*z,z*4096) for z in params]

    def update(kind,a,s,value,reason):
        table=lower if kind=='lower' else upper
        if (kind=='lower' and value<=table[a][s]) or (kind=='upper' and value>=table[a][s]):
            return False
        table[a][s]=value
        trace.append([kind,a,s,value]+reason)
        if lower[a][s]>upper[a][s]:
            raise Contradiction(['bounds',a,s])
        return True

    try:
        while True:
            changed=False
            for a in range(3):
                total=sum(lower[a])
                if total>52:
                    raise Contradiction(['budget',a])
                for s in range(4):
                    changed |= update('upper',a,s,52-total+lower[a][s],['budget'])
                for s in range(4):
                    for u in range(4):
                        if s!=u:
                            changed |= update('lower',a,s,lower[a][u]-12,['lipschitz',u])
                            changed |= update('upper',a,s,upper[a][u]+12,['lipschitz',u])
            for s in range(4):
                caps=[2**upper[a][s] for a in range(3)]
                if sum(caps)<2**18:
                    raise Contradiction(['single_cut',s])
                for a in range(3):
                    residual=2**18-sum(caps[b] for b in range(3) if b!=a)
                    changed |= update('lower',a,s,ceil_log2(residual),['single_cut'])
            for s in range(4):
                for u in range(4):
                    if s==u:
                        continue
                    for weight,target in specifications:
                        caps=[min(2**upper[a][s],weight*2**upper[a][u]) for a in range(3)]
                        if sum(caps)<target:
                            raise Contradiction(['weighted',s,u,weight,target])
                        for a in range(3):
                            residual=target-sum(caps[b] for b in range(3) if b!=a)
                            if residual>0:
                                changed |= update('lower',a,s,ceil_log2(residual),
                                                  ['weighted',s,u,weight,target,0])
                                changed |= update('lower',a,u,ceil_log2((residual+weight-1)//weight),
                                                  ['weighted',s,u,weight,target,1])
            if not changed:
                return dict(excluded=False,lower=lower,upper=upper,trace=trace)
    except Contradiction as error:
        return dict(excluded=True,contradiction=error.reason,trace=trace)


def main():
    config=json.loads(Path(sys.argv[1]).read_text())
    cases=[]
    counts=[]
    for t in config['minima']:
        patterns=sorted(set(itertools.permutations((18,t,t))) |
                        set(itertools.permutations((17,17,t))) |
                        set(itertools.permutations((17,16,16))))
        assert len(patterns)==9
        excluded=0
        start=len(cases)
        for base in range(2):
            for indices in itertools.combinations_with_replacement(range(9),3):
                result=propagate(t,base,indices,patterns,config.get('full_parameters',False))
                excluded+=result['excluded']
                cases.append(dict(minimum=t,base=base,patterns=list(indices),**result))
        counts.append(dict(minimum=t,branches=len(cases)-start,excluded=excluded))
        print(json.dumps(counts[-1]),flush=True)
    out=dict(config=config,counts=counts,cases=cases,
             claim='Only branches with exact replayed contradictions are exclusions; survivors are not tensor constructions.')
    path=Path(sys.argv[2]);temporary=path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(out,separators=(',',':')));temporary.replace(path)


if __name__=='__main__':
    main()
