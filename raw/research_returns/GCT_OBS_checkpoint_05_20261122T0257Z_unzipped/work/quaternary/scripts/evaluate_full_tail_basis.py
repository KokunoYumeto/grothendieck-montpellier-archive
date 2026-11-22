#!/usr/bin/env python3
"""Exact standard-library evaluation of full-monomial centered tail bases.

Unlike verify_centered_evaluations.py, these coefficient files contain full
monomials, with no S3 orbit compression. This script supports weights such
as (9,6,6) and (9,7,4), and centered tensors through order9. Completed
profile blocks are cached with source/sample hashes, so later invocations
only evaluate newly available profiles.
"""
import argparse
from collections import defaultdict
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import time
import zipfile
from verify_centered_evaluations import PackedSamples, read_array, check_arithmetic


def evaluate_profile(profile,path,dimension,packed,coordinates,cache_size):
    degrees=[j for j,k in enumerate(profile,2) for _ in range(k)]
    triples={j:[(a,b,j-a-b) for a in range(j+1) for b in range(j-a+1)]
             for j in range(2,10)}
    lookup={tuple(a):i for i,a in enumerate(coordinates)}
    maps={j:[lookup[(j,)+alpha] for alpha in alphas] for j,alphas in triples.items()}
    terms=defaultdict(list)
    with zipfile.ZipFile(path) as archive:
        for row in range(dimension):
            keys=read_array(archive,'keys'+str(row));coeff=read_array(archive,'coeff'+str(row))
            assert len(keys)==len(coeff) and len(set(keys))==len(keys)
            # Each product is reduced to <=100 and each coefficient to <=100.
            assert 100*100*len(keys)<2**32
            for key,c in zip(keys,coeff):
                if c%101:terms[key].append((row,c%101))

    @lru_cache(maxsize=cache_size)
    def monomial(variables):
        if not variables:return packed.one
        if len(variables)==1:return packed.values[variables[0]]
        return packed.multiply_coordinate(monomial(variables[:-1]),variables[-1])

    accumulators=[0]*dimension
    for key,uses in terms.items():
        local=(key[0].to_bytes(8,'big')+key[1].to_bytes(8,'big'))[:len(degrees)]
        variables=tuple(maps[j][i] for j,i in zip(degrees,local))
        assert variables==tuple(sorted(variables))
        value=monomial(variables)
        for row,c in uses:accumulators[row]+=c*value
    raw=b''.join(bytes(packed.unpack(v)) for v in accumulators)
    return raw,dict(profile=profile,rows=dimension,samples=packed.samples,
                    entries=dimension*packed.samples,monomials=len(terms),
                    monomial_cache=monomial.cache_info()._asdict())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--basis',type=Path,required=True)
    parser.add_argument('--samples',type=Path,default=Path('work/quaternary/results/centered_dense_2060_j9.json'))
    parser.add_argument('--output-dir',type=Path,required=True)
    parser.add_argument('--cache-size',type=int,default=8192)
    parser.add_argument('--limit-profiles',type=int)
    args=parser.parse_args();started=time.monotonic();args.output_dir.mkdir(parents=True,exist_ok=True)
    arithmetic=check_arithmetic()
    samples=json.loads(args.samples.read_text())
    assert samples['prime']==101
    sample_hash=hashlib.sha256(args.samples.read_bytes()).hexdigest()
    inventory=json.loads((args.basis/'profiles.json').read_text())
    packed=PackedSamples(samples['normalized_tensors']);completed=0
    for entry in inventory['profiles']:
        profile=entry['profile'];tag='_'.join(map(str,profile))
        source=args.basis/(tag+'.npz');meta_path=args.basis/(tag+'.json')
        target=args.output_dir/(tag+'.bin');target_meta=args.output_dir/(tag+'.json')
        if not meta_path.exists():continue
        meta=json.loads(meta_path.read_text())
        if meta['rank']!=entry['dimension']:continue
        source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
        if target.exists() and target_meta.exists():
            cached=json.loads(target_meta.read_text())
            if cached['source_sha256']==source_hash and cached['sample_sha256']==sample_hash:continue
        before=time.monotonic()
        raw,record=evaluate_profile(profile,source,meta['rank'],packed,samples['coordinates'],args.cache_size)
        record.update(source_sha256=source_hash,sample_sha256=sample_hash,
                      matrix_sha256=hashlib.sha256(raw).hexdigest(),seconds=round(time.monotonic()-before,3))
        target.write_bytes(raw);target_meta.write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps(record),flush=True);completed+=1
        if args.limit_profiles and completed>=args.limit_profiles:break
    records=[];blocks=[]
    for entry in inventory['profiles']:
        tag='_'.join(map(str,entry['profile']));path=args.output_dir/(tag+'.bin')
        meta_path=args.output_dir/(tag+'.json')
        if path.exists() and meta_path.exists():
            meta=json.loads(meta_path.read_text())
            assert meta['sample_sha256']==sample_hash
            raw=path.read_bytes()
            assert len(raw)==meta['rows']*packed.samples
            assert hashlib.sha256(raw).hexdigest()==meta['matrix_sha256']
            blocks.append(raw);records.append(dict(profile=entry['profile'],rows=meta['rows']))
    raw=b''.join(blocks);rows=sum(r['rows'] for r in records)
    metadata=dict(prime=101,weight=inventory['weight'],samples=str(args.samples),
                  shape=[rows,packed.samples],profiles=records,
                  complete=rows==inventory['total_dimension'],
                  target_dimension=inventory['total_dimension'],
                  matrix_sha256=hashlib.sha256(raw).hexdigest(),
                  arithmetic_checks=arithmetic,seconds=round(time.monotonic()-started,3))
    (args.output_dir/'matrix.bin').write_bytes(raw)
    (args.output_dir/'matrix.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps({k:v for k,v in metadata.items() if k!='profiles'}),flush=True)


if __name__=='__main__':main()
