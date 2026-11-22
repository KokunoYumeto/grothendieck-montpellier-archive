#!/usr/bin/env python3
"""Cache exact normalized centered tensors and verification data for 830 pencils."""
import argparse
import hashlib
import json
from time import monotonic
from centered_det9_sampler import CenteredDeterminantSampler


def generate(samples,seed,output,max_jet=8):
    started=monotonic()
    coordinates=[(j,a,b,j-a-b) for j in range(2,max_jet+1)
                 for a in range(j+1) for b in range(j-a+1)]
    sampler=CenteredDeterminantSampler(seed=seed,prime=101)
    rows=[];sanity=[];states=[];source_hash=hashlib.sha256()
    initial_pencil=None
    for i in range(samples):
        tensors,certificate=sampler.sample('dense',sanity_points=3,max_jet=max_jet)
        rows.append([tensors[j][(a,b,c)] for j,a,b,c in coordinates])
        states.append(certificate['generator_state_before'])
        sanity.append([check['point']+[check['determinant']]
                       if isinstance(check['point'],list)
                       else list(check['point'])+[check['determinant']]
                       for check in certificate['sanity']])
        source_hash.update((json.dumps(certificate['matrices'],separators=(',',':'))+'\n').encode())
        if i==0:initial_pencil=certificate['matrices']
    tensor_hash=hashlib.sha256(bytes(v for row in rows for v in row)).hexdigest()
    data=dict(prime=101,seed=seed,kind='dense',samples=samples,
              pencil='x0 I9 + x1 A1 + x2 A2 + x3 A3; each Ai has integer trace zero',
              generator='s <- 1664525 s + 1013904223 mod 2^32; value=(s>>16) mod101',
              matrix_generation='Three 9x9 matrices per sample, row major; replace last diagonal by minus sum of previous diagonal entries',
              coordinates=coordinates,
              tensor_normalization='coefficient * (9-j)! a! b! c! / 9! mod101',
              normalized_tensors=rows,generator_states_before=states,
              sanity_point_format='[x1,x2,x3,determinant]; all equal reconstructed polynomial values',
              sanity=sanity,initial_pencil=initial_pencil,
              source_matrices_sha256=source_hash.hexdigest(),
              source_hash_encoding='compact JSON for each matrices array, followed by newline, in sample order',
              normalized_tensors_sha256=tensor_hash,
              tensor_hash_encoding='one byte per residue in row-major sample/coordinate order')
    encoded=(json.dumps(data,separators=(',',':'))+'\n').encode()
    with open(output,'wb') as f:f.write(encoded)
    manifest=dict(file=output,file_sha256=hashlib.sha256(encoded).hexdigest(),
                  samples=samples,coordinates=len(coordinates),
                  direct_determinant_checks=3*samples,
                  normalized_tensors_sha256=tensor_hash,
                  source_matrices_sha256=source_hash.hexdigest(),
                  seconds=round(monotonic()-started,3))
    with open(output+'.manifest.json','w') as f:json.dump(manifest,f,indent=2);f.write('\n')
    return manifest


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--samples',type=int,default=830)
    parser.add_argument('--seed',type=int,default=20261122)
    parser.add_argument('--max-jet',type=int,choices=(8,9),default=8)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    print(json.dumps(generate(args.samples,args.seed,args.output,args.max_jet)),flush=True)
