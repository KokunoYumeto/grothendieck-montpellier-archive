#!/usr/bin/env python3
"""Recompute every stored centered-invariant evaluation using only stdlib.

The input polynomials have canonical S3 monomial-orbit coefficients. We
restore their exact six-color sum and evaluate on the deterministic centered
determinant tensors. All sample values are packed into independent 32-bit
integer lanes. Pointwise multiplication uses seven coordinate-bit masks,
then exact reciprocal reduction modulo 101. No machine integer overflows,
floating arithmetic, NumPy, or source evaluation code is used.
"""
import argparse
import ast
from collections import defaultdict, Counter
from functools import lru_cache
import hashlib
from itertools import permutations
import json
from pathlib import Path
import struct
import time
import zipfile


def read_array(archive,name):
    data=archive.read(name+'.npy')
    assert data[:6]==b'\x93NUMPY'
    assert data[6:8] in (b'\x01\x00',b'\x02\x00')
    size=2 if data[6]==1 else 4
    header=int.from_bytes(data[8:8+size],'little')
    start=8+size+header
    meta=ast.literal_eval(data[8+size:start].decode('latin1').strip())
    assert not meta['fortran_order']
    assert meta['descr'] in ('<u8','<i8')
    scalar='<Q' if meta['descr']=='<u8' else '<q'
    values=[x[0] for x in struct.iter_unpack(scalar,data[start:])]
    shape=meta['shape']
    if len(shape)==1:
        assert len(values)==shape[0]
        return values
    assert len(shape)==2 and shape[1]==2 and len(values)==2*shape[0]
    return list(zip(values[::2],values[1::2]))


class PackedSamples:
    prime=101
    bits=7
    lane_bits=32
    lane_bytes=4

    def __init__(self,rows):
        self.samples=len(rows)
        assert self.samples and all(len(row)==len(rows[0]) for row in rows)
        assert all(0<=v<101 for row in rows for v in row)
        self.one=((1<<(32*self.samples))-1)//((1<<32)-1)
        self.low=127*self.one
        self.reciprocal=(1<<14)//101
        self.correction=(256-101)*self.one
        self.values=[];self.masks=[]
        for column in zip(*rows):
            self.values.append(self.pack(column))
            self.masks.append(tuple(self.pack(127 if (v>>bit)&1 else 0 for v in column)
                                    for bit in range(7)))

    def pack(self,values):
        return int.from_bytes(b''.join(int(v).to_bytes(4,'little') for v in values),'little')

    def unpack(self,value):
        raw=value.to_bytes(4*self.samples,'little')
        return [v[0] % 101 for v in struct.iter_unpack('<I',raw)]

    def reduce(self,value):
        # Requires each lane z < 101^2. The reciprocal quotient is exact
        # or one too small; the residual is <202 and one correction suffices.
        quotient=((value*self.reciprocal)>>14)&self.low
        residue=value-101*quotient
        return residue-101*(((residue+self.correction)>>8)&self.one)

    def multiply_coordinate(self,value,coordinate):
        # Each selected lane contributes value_lane*2^bit exactly when
        # that bit occurs in the coordinate. The sum is <101^2<2^14.
        product=sum((value&mask)<<bit for bit,mask in enumerate(self.masks[coordinate]))
        return self.reduce(product)


def check_arithmetic():
    rows=[(a,b) for a in range(101) for b in range(101)]
    packed=PackedSamples(rows)
    actual=packed.unpack(packed.multiply_coordinate(packed.values[0],1))
    assert actual==[a*b%101 for a,b in rows]
    values=list(range(101**2))
    assert packed.unpack(packed.reduce(packed.pack(values)))==[v%101 for v in values]
    return dict(pointwise_products=101**2,reduction_inputs=101**2,all_checks_passed=True)


def verify_profile(profile,archive_path,packed,coordinates,expected,cache_size):
    degrees=[j for j,k in enumerate(profile,2) for _ in range(k)]
    assert sum(degrees)==24 and len(degrees)<=12
    triples={j:[(a,b,j-a-b) for a in range(j+1) for b in range(j-a+1)]
             for j in range(2,9)}
    lookup={tuple(x):i for i,x in enumerate(coordinates)}
    color_maps={j:[[lookup[(j,)+tuple(alpha[p] for p in pi)] for alpha in triples[j]]
                  for pi in permutations(range(3))] for j in range(2,9)}
    terms=defaultdict(list)
    with zipfile.ZipFile(archive_path) as archive:
        for row in range(len(expected)):
            keys=read_array(archive,'keys'+str(row))
            coefficients=read_array(archive,'coeff'+str(row))
            assert len(keys)==len(coefficients) and len(set(keys))==len(keys)
            # Every orbit value is a sum of six residues <=100. After
            # coefficients are reduced modulo101, each term is <=60000.
            # The bound prevents every carry between the 32-bit lanes.
            assert 6*100*100*len(keys)<2**32
            for key,c in zip(keys,coefficients):
                if c%101:terms[key].append((row,c%101))

    @lru_cache(maxsize=cache_size)
    def monomial(variables):
        if not variables:return packed.one
        if len(variables)==1:return packed.values[variables[0]]
        return packed.multiply_coordinate(monomial(variables[:-1]),variables[-1])

    accumulators=[0]*len(expected)
    for key,uses in terms.items():
        local=(key[0].to_bytes(8,'big')+key[1].to_bytes(8,'big'))[:len(degrees)]
        orbit=Counter(tuple(sorted(color_maps[j][pi][index]
                                   for j,index in zip(degrees,local)))
                      for pi in range(6))
        # Repeated monomials are deliberately counted: their multiplicity
        # is the required stabilizer size6/|orbit|.
        orbit_value=sum(count*monomial(variables) for variables,count in orbit.items())
        for row,c in uses:accumulators[row]+=c*orbit_value
    actual=[bytes(packed.unpack(value)) for value in accumulators]
    for row,(a,e) in enumerate(zip(actual,expected)):
        assert a==e,dict(profile=profile,row=row,
                         mismatches=[i for i,(x,y) in enumerate(zip(a,e)) if x!=y][:8])
    return actual,dict(profile=profile,rows=len(actual),samples=packed.samples,
                       entries=len(actual)*packed.samples,orbit_monomials=len(terms),
                       monomial_cache=monomial.cache_info()._asdict())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--samples',type=Path,default=Path('work/quaternary/results/centered_dense_830.json'))
    parser.add_argument('--basis',type=Path,default=Path('work/support_lmr/results/bracket_basis'))
    parser.add_argument('--evaluation',type=Path,default=Path('work/support_lmr/results/bracket_evaluation'))
    parser.add_argument('--cache-size',type=int,default=8192)
    parser.add_argument('--limit-profiles',type=int)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();started=time.monotonic()
    arithmetic=check_arithmetic()
    samples=json.loads(args.samples.read_text())
    metadata=json.loads((args.evaluation/'matrix.json').read_text())
    expected=(args.evaluation/'matrix.bin').read_bytes()
    shape=metadata['shape']
    assert samples['prime']==metadata['prime']==101
    assert shape[1]==len(samples['normalized_tensors'])
    assert len(expected)==shape[0]*shape[1]
    packed=PackedSamples(samples['normalized_tensors'])
    offset=0;records=[];recomputed=[]
    for entry in metadata['profiles']:
        profile=entry['profile'];count=entry['rows'];tag='_'.join(map(str,profile))
        block=[expected[(offset+i)*shape[1]:(offset+i+1)*shape[1]] for i in range(count)]
        before=time.monotonic()
        actual,record=verify_profile(profile,args.basis/(tag+'.npz'),packed,
                                     samples['coordinates'],block,args.cache_size)
        record['seconds']=round(time.monotonic()-before,3)
        records.append(record);recomputed.extend(actual);offset+=count
        print(json.dumps(record),flush=True)
        if args.limit_profiles and len(records)>=args.limit_profiles:break
    raw=b''.join(recomputed)
    result=dict(prime=101,profiles=records,rows=len(recomputed),samples=shape[1],
                entries=len(raw),complete=len(recomputed)==804,
                arithmetic_checks=arithmetic,
                agrees_with_entire_available_matrix=len(recomputed)==shape[0],
                matrix_sha256=hashlib.sha256(raw).hexdigest(),
                seconds=round(time.monotonic()-started,3),all_checks_passed=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='profiles'}),flush=True)


if __name__=='__main__':main()
