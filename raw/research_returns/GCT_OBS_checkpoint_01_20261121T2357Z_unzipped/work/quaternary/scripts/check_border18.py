#!/usr/bin/env python3
"""Rebuild the CUE_GCT R-25 certificate implying c_18=1262; stdlib only.

Differentiate the permanent at A+tuv^T modulo t^2. Coefficients G_0,G_1
of its matrix-entry gradient give a=G_0v, b=G_0^Tu, t=G_1v, t'=G_1^Tu.
This computes all polynomial columns directly, not from archived matrices.
"""
import argparse
import hashlib
import json
import multiprocessing as mp
import time
from check_projection import compositions, packed_eliminate

N, P = 17, 1021


def coefficients():
    state, out = 20330804, []
    for _ in range(3*N*N+6*N):
        state = (1664525*state+1013904223) % 2**32
        out.append((state >> 8) % P)
    return out


def evaluate(point):
    coeff = coefficients()
    values = [sum(coeff[k+i]*point[i] for i in range(3)) % P
              for k in range(0,len(coeff),3)]
    A = [values[N*i:N*(i+1)] for i in range(N)]
    u, v = values[N*N:N*N+N], values[N*N+N:]
    H = [[ui*vj % P for vj in v] for ui in u]
    size = 1 << N
    f0, f1 = [1]+[0]*(size-1), [0]*size
    for S in range(1,size):
        i, bits, z0, z1 = S.bit_count()-1, S, 0, 0
        while bits:
            bit = bits & -bits
            j, T = bit.bit_length()-1, S ^ bit
            z0 += A[i][j]*f0[T]
            z1 += A[i][j]*f1[T]+H[i][j]*f0[T]
            bits ^= bit
        f0[S],f1[S] = z0 % P,z1 % P
    b0, b1 = [0]*size, [0]*size
    b0[-1] = 1
    g0, g1 = [[0]*N for _ in range(N)], [[0]*N for _ in range(N)]
    for S in range(size-1,0,-1):
        z0,z1 = b0[S] % P,b1[S] % P
        i,bits = S.bit_count()-1,S
        while bits:
            bit = bits & -bits
            j,T = bit.bit_length()-1,S ^ bit
            b0[T] += z0*A[i][j]
            b1[T] += z1*A[i][j]+z0*H[i][j]
            g0[i][j] += z0*f0[T]
            g1[i][j] += z0*f1[T]+z1*f0[T]
            bits ^= bit
    a = [sum(g0[i][j]*v[j] for j in range(N)) % P for i in range(N)]
    b = [sum(g0[i][j]*u[i] for i in range(N)) % P for j in range(N)]
    t = [sum(g1[i][j]*v[j] for j in range(N)) % P for i in range(N)]
    tp = [sum(g1[i][j]*u[i] for i in range(N)) % P for j in range(N)]
    return ([x*f0[-1] % P for x in point]
            + [x*y % P for y in a for x in point]
            + [x*y % P for y in b for x in point] + t + tp)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workers', type=int, default=1)
    parser.add_argument('--output')
    args = parser.parse_args()
    started = time.monotonic()
    points = list(compositions(18,3))
    if args.workers==1:
        matrix = list(map(evaluate,points))
    else:
        with mp.Pool(args.workers) as pool:
            matrix = list(pool.imap(evaluate,points,chunksize=1))
    minor = [[value for j,value in enumerate(row) if j!=104] for row in matrix[:138]]
    rank,columns,det = packed_eliminate(minor,P)
    assert (rank,det)==(138,501),(rank,det)
    digest = hashlib.sha256(b''.join(x.to_bytes(2,'little') for row in matrix for x in row)).hexdigest()
    result = dict(matrix_size=17,prime=P,rows=len(points),columns=139,minor_rank=rank,
                  determinant_mod_prime=det,omitted_column=104,
                  row_major_uint16le_sha256=digest,seconds=round(time.monotonic()-started,3),
                  implication='R-24 plus the proved bordered induction gives c18=1262')
    print(json.dumps(result,indent=2))
    if args.output:
        with open(args.output,'w') as stream:
            json.dump(result,stream,indent=2)
            stream.write('\n')


if __name__=='__main__':
    main()
