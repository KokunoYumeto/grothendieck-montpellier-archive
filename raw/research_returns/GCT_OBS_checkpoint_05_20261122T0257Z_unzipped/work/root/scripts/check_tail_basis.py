#!/usr/bin/env python3
"""Verify integral highest-weight tail polynomials with the stdlib only.

No graph expansion or floating-point rank is trusted. Every monomial's
weight is checked, both simple Lie raising operators are applied over Z,
and a nonzero coefficient minor proves independence in each multidegree.
The total number of independent polynomials is compared with the separate
exact centered-jet character count1250 or2030.
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import sys
import time
import zipfile

sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'support_lmr'/'scripts'))
from verify_bracket_basis import read_npy, minor


class Profile:
    def __init__(self,profile,weight):
        self.degrees=[j for j,k in enumerate(profile,2) for _ in range(k)]
        self.k=len(self.degrees);self.weight=weight;self.groups=[]
        offset=0
        for j,k in enumerate(profile,2):
            if k:self.groups.append((j,offset,offset+k))
            offset+=k
        self.alpha={j:[(a,b,j-a-b) for a in range(j+1) for b in range(j-a+1)]
                    for j in range(2,len(profile)+2)}
        self.raise_maps={}
        for root in (0,1):
            self.raise_maps[root]={}
            for j,alphas in self.alpha.items():
                lookup={alpha:i for i,alpha in enumerate(alphas)};moves=[]
                for alpha in alphas:
                    if alpha[root+1]:
                        target=list(alpha);target[root]+=1;target[root+1]-=1
                        moves.append((lookup[tuple(target)],alpha[root+1]))
                    else:moves.append((0,0))
                self.raise_maps[root][j]=moves

    def decode(self,key):
        raw=key[0].to_bytes(8,'big')+key[1].to_bytes(8,'big')
        assert not any(raw[self.k:])
        monomial=raw[:self.k];weight=[0,0,0]
        for j,index in zip(self.degrees,monomial):
            for i,value in enumerate(self.alpha[j][index]):weight[i]+=value
        assert weight==self.weight,(weight,self.weight)
        for j,lo,hi in self.groups:assert list(monomial[lo:hi])==sorted(monomial[lo:hi])
        return monomial

    def check(self,keys,coefficients):
        monomials=[self.decode(key) for key in keys];counts=[]
        for root in (0,1):
            result=defaultdict(int)
            for monomial,value in zip(monomials,coefficients):
                assert isinstance(value,int)
                for j,lo,hi in self.groups:
                    i=lo
                    while i<hi:
                        index=monomial[i];end=i+1
                        while end<hi and monomial[end]==index:end+=1
                        target,scale=self.raise_maps[root][j][index]
                        if scale:
                            changed=list(monomial[lo:hi]);changed[i-lo]=target;changed.sort()
                            keyout=monomial[:lo]+bytes(changed)+monomial[hi:]
                            result[keyout]+=value*scale*(end-i)
                        i=end
            failures=[(list(key),value) for key,value in result.items() if value]
            assert not failures,(root,failures[:3])
            counts.append(len(result))
        return counts


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--limit',type=int)
    args=parser.parse_args();start=time.monotonic()
    inventory=json.loads((args.data_dir/'profiles.json').read_text());weight=inventory['weight']
    expected={(9,6,6):1250,(9,7,4):2030}[tuple(weight)]
    assert inventory['total_dimension']==expected
    rows=[]
    for entry in inventory['profiles']:
        profile=entry['profile'];tag='_'.join(map(str,profile));meta_path=args.data_dir/(tag+'.json')
        if not meta_path.exists():continue
        meta=json.loads(meta_path.read_text());decoder=Profile(profile,weight)
        pivots=[tuple(key) for key in meta['pivot_monomials']];matrix=[];terms=0;raised=[0,0]
        with zipfile.ZipFile(args.data_dir/(tag+'.npz')) as archive:
            for i in range(meta['rank']):
                keys=read_npy(archive,'keys'+str(i));coefficients=read_npy(archive,'coeff'+str(i))
                assert len(keys)==len(coefficients)
                lookup=dict(zip(keys,coefficients));assert len(lookup)==len(keys)
                matrix.append([lookup.get(key,0)%101 for key in pivots])
                terms+=len(keys)
                counts=decoder.check(keys,coefficients)
                raised=[a+b for a,b in zip(raised,counts)]
        determinant=minor(matrix,101);assert determinant
        result=dict(profile=profile,rank=meta['rank'],expected=entry['dimension'],
                    minor_mod_101=determinant,terms=terms,raised_terms=raised)
        rows.append(result);print(json.dumps(result),flush=True)
        if args.limit and len(rows)>=args.limit:break
    total=sum(row['rank'] for row in rows)
    output=dict(weight=weight,dimension=total,expected=expected,complete=total==expected,
                exact_both_raising_checked=True,profiles=rows,seconds=time.monotonic()-start)
    args.output.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='profiles'}),flush=True)


if __name__=='__main__':main()
