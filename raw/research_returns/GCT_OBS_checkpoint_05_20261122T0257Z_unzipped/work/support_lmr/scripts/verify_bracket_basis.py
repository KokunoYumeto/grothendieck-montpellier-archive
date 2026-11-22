#!/usr/bin/env python3
"""Standard-library verification of the centered-jet invariant basis.

The build data contain integral coefficients of S3 monomial orbits, together
with eight-epsilon graphs. This verifier does not trust the graph expansion:
it restores the full integral polynomial and checks its Lie raising identity
exactly. All polynomials have torus weight (8,8,8) and are S3-invariant, so
one raising operator suffices for both simple roots. Nonzero modular minors
in all 154 multidegrees, whose independently counted dimensions sum to 804,
certify a complete rational invariant basis.

The NumPy .npz storage format is read directly with zipfile/struct/ast; NumPy
is not required. Use --skip-raising only for a quick partial verification.
"""
import argparse
import ast
from collections import defaultdict
from itertools import permutations
import json
from pathlib import Path
import struct
import time
import zipfile


def read_npy(archive,name):
    data=archive.read(name+'.npy')
    assert data[:6]==b'\x93NUMPY' and data[6:8] in (b'\x01\x00',b'\x02\x00')
    size=2 if data[6]==1 else 4
    length=int.from_bytes(data[8:8+size],'little');start=8+size+length
    meta=ast.literal_eval(data[8+size:start].decode('latin1').strip())
    assert not meta['fortran_order'] and meta['descr'] in ('<u8','<i8')
    fmt='<Q' if meta['descr']=='<u8' else '<q'
    values=[v[0] for v in struct.iter_unpack(fmt,data[start:])]
    shape=meta['shape']
    assert len(values)==__import__('math').prod(shape)
    if len(shape)==2:
        assert shape[1]==2
        return list(zip(values[::2],values[1::2]))
    assert len(shape)==1
    return values


def minor(matrix,p):
    a=[list(row) for row in matrix];d=1
    for k in range(len(a)):
        pivot=next((i for i in range(k,len(a)) if a[i][k]%p),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];d=-d
        value=a[k][k]%p;d=d*value%p;inv=pow(value,-1,p)
        for i in range(k+1,len(a)):
            factor=a[i][k]*inv%p
            if factor:
                for j in range(k+1,len(a)):a[i][j]=(a[i][j]-factor*a[k][j])%p
    return d%p


class Profile:
    def __init__(self,profile):
        self.degrees=[j for j,k in enumerate(profile,2) for _ in range(k)]
        self.k=len(self.degrees)
        self.groups=[]
        offset=0
        for j,k in enumerate(profile,2):
            if k:self.groups.append((j,offset,offset+k))
            offset+=k
        self.alpha={j:[(a,b,j-a-b) for a in range(j+1)
                       for b in range(j-a+1)] for j in range(2,9)}
        self.maps={}
        self.raise_maps={}
        for j,alphas in self.alpha.items():
            lookup={alpha:i for i,alpha in enumerate(alphas)}
            self.maps[j]=[[lookup[tuple(alpha[p] for p in perm)] for alpha in alphas]
                          for perm in permutations(range(3))]
            self.raise_maps[j]=[(lookup[(a+1,b-1,c)],b) if b else (0,0)
                                for a,b,c in alphas]
        self.cache={}

    def orbit(self,key):
        if key in self.cache:return self.cache[key]
        monomial=(key[0].to_bytes(8,'big')+key[1].to_bytes(8,'big'))[:self.k]
        weight=[0,0,0]
        for j,index in zip(self.degrees,monomial):
            for c,value in enumerate(self.alpha[j][index]):weight[c]+=value
        assert weight==[8,8,8]
        orbit=set()
        for p in range(6):
            transformed=[]
            for j,lo,hi in self.groups:
                transformed.extend(sorted(self.maps[j][p][i] for i in monomial[lo:hi]))
            orbit.add(bytes(transformed))
        result=sorted(orbit)
        assert result[0]==monomial and 6%len(result)==0
        self.cache[key]=result
        return result

    def raising(self,keys,coeff):
        result=defaultdict(int)
        for key,value in zip(keys,coeff):
            orbit=self.orbit(key);value*=6//len(orbit)
            for monomial in orbit:
                for j,lo,hi in self.groups:
                    i=lo
                    while i<hi:
                        index=monomial[i];end=i+1
                        while end<hi and monomial[end]==index:end+=1
                        target,scale=self.raise_maps[j][index]
                        if scale:
                            changed=list(monomial[lo:hi]);changed[i-lo]=target;changed.sort()
                            keyout=monomial[:lo]+bytes(changed)+monomial[hi:]
                            result[keyout]+=value*scale*(end-i)
                        i=end
        failures=[(list(k),v) for k,v in result.items() if v]
        assert not failures,failures[:3]
        return len(result)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir',type=Path,default=Path('work/support_lmr/results/bracket_basis'))
    parser.add_argument('--profiles',type=Path,default=Path('work/support_lmr/results/invariant_profiles.json'))
    parser.add_argument('--skip-raising',action='store_true')
    parser.add_argument('--limit',type=int)
    parser.add_argument('--output',type=Path,default=Path('work/support_lmr/results/bracket_basis_verification.json'))
    args=parser.parse_args();start=time.monotonic()
    expected=json.loads(args.profiles.read_text())['profiles'];rows=[]
    for entry in expected:
        profile=entry['profile'];tag='_'.join(map(str,profile));path=args.data_dir/(tag+'.json')
        if not path.exists():continue
        meta=json.loads(path.read_text())
        if meta['rank']!=entry['invariant_dimension']:continue
        decoder=Profile(profile);pivots=[tuple(v) for v in meta['pivot_monomials']]
        matrix=[];terms=0;raised_terms=0
        with zipfile.ZipFile(args.data_dir/(tag+'.npz')) as archive:
            for i in range(meta['rank']):
                keys=read_npy(archive,'keys'+str(i));coeff=read_npy(archive,'coeff'+str(i))
                assert len(keys)==len(coeff)
                lookup=dict(zip(keys,coeff));assert len(lookup)==len(keys)
                matrix.append([lookup.get(key,0)%meta['prime'] for key in pivots])
                terms+=len(keys)
                if not args.skip_raising:raised_terms+=decoder.raising(keys,coeff)
                else:
                    for key in keys:decoder.orbit(key)
        determinant=minor(matrix,meta['prime']);assert determinant
        row=dict(profile=profile,dimension=meta['rank'],minor_mod_p=determinant,
                 terms=terms,raised_terms=raised_terms,exact_raising_checked=not args.skip_raising)
        rows.append(row);print(json.dumps(row),flush=True)
        if args.limit and len(rows)>=args.limit:break
    total=sum(row['dimension'] for row in rows)
    result=dict(profiles=rows,dimension=total,complete=total==804,
                exact_raising_checked=not args.skip_raising,elapsed_seconds=time.monotonic()-start)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='profiles'}),flush=True)


if __name__=='__main__':main()
