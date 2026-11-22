#!/usr/bin/env python3
"""Independent coefficient checks for the centered determinant tensor sampler.

The Newton interpolation procedure is compared against a direct six-term
Leibniz expansion for 3x3 pencils, and against multiplication of three
independently expanded 3x3 block determinants for 9x9 pencils. Every
coefficient, including degree9, is compared; direct values also are checked.
"""
import argparse
import json
from time import monotonic
from centered_det9_sampler import (Generator, CenteredDeterminantSampler,
                                  cubic_coefficients, dense_coefficients,
                                  exponents)


def check():
    started=monotonic()
    generator=Generator(202611220017,101)
    small=[]
    for i in range(24):
        matrices=[generator.traceless(3) for _ in range(3)]
        interpolation=dense_coefficients(matrices,101)
        leibniz=cubic_coefficients(matrices,101)
        assert all(interpolation.get(a,0)==leibniz.get(a,0)
                   for j in range(4) for a in exponents(j))
        small.append(dict(index=i,coefficients_checked=20))
    sampler=CenteredDeterminantSampler(202611220018,101)
    blocks=[]
    for i in range(12):
        tensors,certificate=sampler.sample('block',sanity_points=5)
        interpolation=dense_coefficients(certificate['matrices'],101)
        direct={tuple(a):v for a,v in certificate['coefficients']}
        assert all(interpolation[a]==direct[a] for a in interpolation)
        blocks.append(dict(index=i,coefficients_checked=220,
                           sanity=certificate['sanity']))
    return dict(prime=101,three_by_three=small,nine_by_nine_blocks=blocks,
                total_coefficients_checked=24*20+12*220,
                seconds=round(monotonic()-started,3),all_checks_passed=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result=check()
    with open(args.output,'w') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items()
                      if k not in ('three_by_three','nine_by_nine_blocks')}))
