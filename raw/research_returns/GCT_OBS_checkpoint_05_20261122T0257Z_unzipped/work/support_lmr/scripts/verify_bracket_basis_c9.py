#!/usr/bin/env python3
"""Reconstruct the C2=I nine-bracket polynomials using only stdlib.

Each graph itself defines a genuine det^9 relative invariant. The checker
enumerates its epsilon colorings with exact quadratic equality constraints,
collects integral coefficients, and compares them to the saved restricted
tables. Nonzero coefficient minors prove independence on C2=I, hence on the
full tensor space. Together with the exact character dimension2386 this
certifies completeness when all profiles have been supplied.
"""
import argparse
import hashlib
import os
import tempfile
from collections import defaultdict
from itertools import permutations
import json
from pathlib import Path
import time
import zipfile

from verify_bracket_basis import minor,read_npy

PERMS=list(permutations(range(3)))
SIGNS=[(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) for p in PERMS]


class Profile:
    def __init__(self,profile):
        self.profile=profile
        self.degrees=[j for j,k in enumerate(profile,2) for _ in range(k)]
        self.higher=[(v,j) for v,j in enumerate(self.degrees) if j>2]
        self.k=len(self.higher)
        self.groups=[];offset=0
        for j,k in enumerate(profile[1:],3):
            if k:self.groups.append((j,offset,offset+k))
            offset+=k
        self.alpha={j:[(a,b,j-a-b) for a in range(j+1) for b in range(j-a+1)]
                    for j in range(3,10)}
        self.maps={}
        for j,alphas in self.alpha.items():
            lookup={alpha:i for i,alpha in enumerate(alphas)}
            self.maps[j]=[[lookup[tuple(alpha[p] for p in perm)] for alpha in alphas]
                          for perm in PERMS]
        self.canonical_cache={}

    def canonical(self,monomial):
        if monomial in self.canonical_cache:return self.canonical_cache[monomial]
        images=[]
        for p in range(6):
            transformed=[]
            for j,lo,hi in self.groups:
                transformed.extend(sorted(self.maps[j][p][i] for i in monomial[lo:hi]))
            images.append(bytes(transformed))
        representative=min(images)
        signs={SIGNS[p] for p,image in enumerate(images) if image==representative}
        result=None if len(signs)>1 else (representative,next(iter(signs)))
        self.canonical_cache[monomial]=result
        return result

    def validate_key(self,key):
        monomial=(key[0].to_bytes(8,'big')+key[1].to_bytes(8,'big'))[:self.k]
        assert self.canonical(monomial)==(monomial,1)
        weight=[0,0,0]
        for (_,j),index in zip(self.higher,monomial):
            for c,value in enumerate(self.alpha[j][index]):weight[c]+=value
        assert all(0<=w<=9 and w%2==1 for w in weight)
        assert sum((9-w)//2 for w in weight)==self.profile[0]
        return monomial

    def reconstruct(self,graph):
        slots=defaultdict(list)
        for e,vertices in enumerate(graph):
            assert len(vertices)==3 and len(set(vertices))==3
            for s,v in enumerate(vertices):slots[v].append((e,s))
        assert [len(slots[v]) for v in range(len(self.degrees))]==self.degrees
        links={}
        for v,j in enumerate(self.degrees):
            if j==2:
                a,b=slots[v];links[a]=b;links[b]=a
        # Reordering epsilon factors introduces no sign. Fix the first one in
        # this order, then restore all six global colors by anti-symmetrization.
        order=[];unused=set(range(9))
        while unused:
            e=max(unused,key=lambda e:(sum(links.get((e,s),(-1,0))[0] in order for s in range(3)),
                                       sum((e,s) in links for s in range(3)),-e))
            order.append(e);unused.remove(e)
        prior=[]
        for level,e in enumerate(order):
            prior.append([(s,*links[e,s]) for s in range(3)
                          if (e,s) in links and links[e,s][0] in order[:level]])
        assigned=[None]*9;counts=[[0,0,0] for _ in self.degrees]
        higher_slots=[[(v,s) for s,v in enumerate(graph[e]) if self.degrees[v]>2] for e in range(9)]
        raw=defaultdict(int);colorings=0
        permitted={}
        for pattern in __import__('itertools').product(range(-1,3),repeat=3):
            permitted[pattern]=[(p,SIGNS[i]) for i,p in enumerate(PERMS)
                                if all(a<0 or a==b for a,b in zip(pattern,p))]

        def visit(level,sign):
            nonlocal colorings
            if level==9:
                mon=[]
                for v,j in self.higher:
                    a,b,_=counts[v];mon.append(a*(2*j+3-a)//2+b)
                for _,lo,hi in self.groups:mon[lo:hi]=sorted(mon[lo:hi])
                raw[bytes(mon)]+=sign;colorings+=1
                return
            e=order[level]
            if level==0:choices=[(PERMS[0],1)]
            else:
                pattern=[-1,-1,-1]
                for s,f,t in prior[level]:pattern[s]=assigned[f][t]
                choices=permitted[tuple(pattern)]
            for colors,psign in choices:
                assigned[e]=colors
                for v,s in higher_slots[e]:counts[v][colors[s]]+=1
                visit(level+1,sign*psign)
                for v,s in higher_slots[e]:counts[v][colors[s]]-=1
            assigned[e]=None

        visit(0,1)
        compressed=defaultdict(int)
        for monomial,value in raw.items():
            if value:
                canonical=self.canonical(monomial)
                if canonical is not None:
                    representative,sign=canonical;compressed[representative]+=value*sign
        return {key:value for key,value in compressed.items() if value},colorings


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir',type=Path,default=Path('work/support_lmr/results/bracket_basis_c9'))
    parser.add_argument('--profile',type=int,nargs=8)
    parser.add_argument('--limit-profiles',type=int)
    parser.add_argument('--limit-graphs',type=int)
    parser.add_argument('--skip-reconstruction',action='store_true')
    parser.add_argument('--resume',action='store_true',help='reuse complete checks with identical source SHA256')
    parser.add_argument('--output',type=Path,default=Path('work/support_lmr/results/bracket_basis_c9_verification.json'))
    args=parser.parse_args();start=time.monotonic()
    entries=json.loads(Path('work/support_lmr/results/invariant_profiles_c9.json').read_text())['profiles']
    if args.profile is not None:entries=[e for e in entries if e['profile']==args.profile]
    prior={}
    if args.resume and args.output.exists():
        prior={tuple(r['profile']):r for r in json.loads(args.output.read_text())['profiles']}
    rows=[]
    for entry in entries:
        profile=entry['profile'];tag='_'.join(map(str,profile));path=args.data_dir/(tag+'.json')
        if not path.exists():continue
        meta=json.loads(path.read_text())
        if meta['rank']!=entry['invariant_dimension']:continue
        source_hash=hashlib.sha256(path.read_bytes()+path.with_suffix('.npz').read_bytes()).hexdigest()
        old=prior.get(tuple(profile))
        if old and old.get('source_sha256')==source_hash and old['graphs_reconstructed']==meta['rank']:
            rows.append(old)
            continue
        decoder=Profile(profile);pivots=[tuple(v) for v in meta['pivot_monomials']]
        matrix=[];terms=0;graphs=0;colorings=0;before=time.monotonic()
        with zipfile.ZipFile(path.with_suffix('.npz')) as archive:
            for i,graph in enumerate(meta['graphs']):
                keys=read_npy(archive,'keys'+str(i));coeff=read_npy(archive,'coeff'+str(i))
                assert len(keys)==len(coeff);lookup=dict(zip(keys,coeff));assert len(lookup)==len(keys)
                matrix.append([lookup.get(key,0)%101 for key in pivots]);terms+=len(keys)
                expected={decoder.validate_key(key):value for key,value in zip(keys,coeff)}
                if not args.skip_reconstruction and (not args.limit_graphs or graphs<args.limit_graphs):
                    actual,count=decoder.reconstruct(graph)
                    assert actual==expected,(profile,i,len(actual),len(expected),
                        next(((list(k),v,actual.get(k)) for k,v in expected.items() if actual.get(k)!=v),None))
                    graphs+=1;colorings+=count
        determinant=minor(matrix,101);assert determinant
        row=dict(profile=profile,dimension=meta['rank'],minor_mod101=determinant,terms=terms,
                 graphs_reconstructed=graphs,colorings=colorings,seconds=time.monotonic()-before,
                 source_sha256=source_hash)
        rows.append(row);print(json.dumps(row),flush=True)
        result=dict(profiles=rows,dimension=sum(r['dimension'] for r in rows),
                    graphs_reconstructed=sum(r['graphs_reconstructed'] for r in rows),
                    elapsed_seconds=time.monotonic()-start)
        with tempfile.NamedTemporaryFile(mode='w',dir=args.output.parent,prefix=args.output.name+'.',suffix='.tmp',delete=False) as handle:
            json.dump(result,handle,indent=2);handle.write('\n');temporary=handle.name
        os.replace(temporary,args.output)
        if args.limit_profiles and len(rows)>=args.limit_profiles:break
    result=dict(profiles=rows,dimension=sum(r['dimension'] for r in rows),
                graphs_reconstructed=sum(r['graphs_reconstructed'] for r in rows),
                elapsed_seconds=time.monotonic()-start)
    with tempfile.NamedTemporaryFile(mode='w',dir=args.output.parent,prefix=args.output.name+'.',suffix='.tmp',delete=False) as handle:
        json.dump(result,handle,indent=2);handle.write('\n');temporary=handle.name
    os.replace(temporary,args.output)
    print(json.dumps({k:v for k,v in result.items() if k!='profiles'}),flush=True)


if __name__=='__main__':main()
