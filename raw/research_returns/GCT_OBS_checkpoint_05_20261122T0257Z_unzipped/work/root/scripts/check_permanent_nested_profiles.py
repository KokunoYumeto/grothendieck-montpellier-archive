#!/usr/bin/env python3
"""Coefficient-level nested projection certificates for quaternary per_17.

Reuses the included, independently reconstructed permanent differential
engine in work/quaternary/scripts/check_projection.py. No inherited
matrix is read. Interpolation and all subsequent ranks are exact mod101.
"""
import argparse
import hashlib
import json
import math
import multiprocessing as mp
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'quaternary'/'scripts'))
from check_projection import compositions, pencil, evaluate, packed_eliminate

P = 101


class Packed:
    """Independent32-bit lanes, all stored entries in0,...,100."""
    def __init__(self, width):
        self.width = width
        self.one = ((1 << (32*width))-1)//((1 << 32)-1)
        self.mask = 255*self.one
        self.offset = P*(P-1)*self.one

    def pack(self, row):
        return int.from_bytes(b''.join(int(v).to_bytes(4,'little') for v in row),'little')

    def unpack(self, row):
        raw = row.to_bytes(4*self.width,'little')
        assert all(raw[i] == 0 for i in range(len(raw)) if i%4)
        return bytes(raw[::4])

    def reduce(self, value):
        q = ((value*((1 << 16)//P)) >> 16) & self.mask
        r = value-P*q
        return r-P*(((r+(512-P)*self.one) >> 9) & self.one)

    def subtract(self, a, b):
        return self.reduce(a+self.offset-b)

    def add_multiple(self, a, b, scalar):
        return self.reduce(a+(scalar%P)*b)


def interpolate(n, points, rows):
    """Recover monomial coefficients from F(n-|t|,t) on |t|<=n.

    1. Axiswise forward differences give the Newton coefficients.
    2. Expand each product of binomial polynomials in monomials.
    3. Homogenize and substitute s=(x0+x1+x2+x3)/n.
    """
    ring = Packed(len(rows[0]))
    data = {tuple(point[1:]):ring.pack(row) for point,row in zip(points,rows)}
    labels = list(data)
    # Descending order ensures that each difference uses the previous stage.
    for axis in range(3):
        ordered = sorted(labels,key=lambda a:a[axis],reverse=True)
        for step in range(1,n+1):
            for alpha in ordered:
                if alpha[axis] >= step:
                    previous = list(alpha)
                    previous[axis] -= 1
                    data[alpha] = ring.subtract(data[alpha],data[tuple(previous)])
    # B[b][a] is the coefficient of t^a in binomial(t,b).
    B = [[1]]
    for b in range(1,n+1):
        current = [0]*(b+1)
        for a,value in enumerate(B[-1]):
            current[a] = (current[a]-(b-1)*value) % P
            current[a+1] = (current[a+1]+value) % P
        B.append([v*pow(b,-1,P)%P for v in current])
    for axis in range(3):
        for alpha in sorted(labels,key=lambda a:a[axis]):
            total = 0
            for b in range(alpha[axis],n-sum(alpha)+alpha[axis]+1):
                source = list(alpha)
                source[axis] = b
                total = ring.add_multiple(total,data[tuple(source)],B[b][alpha[axis]])
            data[alpha] = total
    inverse_n = pow(n,-1,P)
    for alpha in labels:
        data[alpha] = ring.reduce(data[alpha]*pow(inverse_n,n-sum(alpha),P))
    # Translate the homogenizing coordinate by each tail variable in turn.
    for axis in range(3):
        for alpha in sorted(labels,key=lambda a:a[axis],reverse=True):
            b = alpha[axis]
            remaining = n-sum(alpha)+b
            total = 0
            for a in range(b+1):
                source = list(alpha)
                source[axis] = a
                total = ring.add_multiple(total,data[tuple(source)],math.comb(remaining-a,b-a))
            data[alpha] = total
    return ring, data


def count(profile):
    b,c,e = profile
    return sum(b-u+1 for z in range(e+1) for u in range(z,c+1))


def frontier(n, dimension):
    valid = {(b,c,e) for b in range(n+1) for c in range(b+1) for e in range(c+1)
             if count((b,c,e)) <= dimension}
    return sorted(a for a in valid if not any(
        tuple(v+int(i==j) for i,v in enumerate(a)) in valid for j in range(3)))


def check(n=17, workers=4):
    start = time.monotonic()
    points = list(compositions(n,4))
    coeff = pencil(n)
    tasks = [(n,coeff,point) for point in points]
    if workers == 1:
        values = list(map(evaluate,tasks))
    else:
        with mp.Pool(workers) as pool:
            values = list(pool.imap(evaluate,tasks,chunksize=1))
    built = time.monotonic()
    ring, data = interpolate(n,points,values)
    # Exact inverse checks on complete differential rows at six grid points.
    checked_indices = sorted({0,1,len(points)//5,len(points)//2,len(points)-2,len(points)-1})
    for index in checked_indices:
        point = points[index]
        reconstructed = 0
        for alpha,row in data.items():
            exponent = (n-sum(alpha),)+alpha
            scalar = math.prod(pow(x,a,P) for x,a in zip(point,exponent)) % P
            reconstructed = ring.add_multiple(reconstructed,row,scalar)
        assert ring.unpack(reconstructed) == values[index], index
    dimension = min(math.comb(n+3,3),4*n*n-2*n+2)
    results = []
    for profile in frontier(n,dimension):
        b,c,e = profile
        labels = [a for a in data if sum(a)<=b and a[1]+a[2]<=c and a[2]<=e]
        matrix = [ring.unpack(data[a]) for a in labels]
        rank,columns,det = packed_eliminate(matrix)
        result = dict(profile=profile,coordinates=len(matrix),rank=rank,
                      full_row_rank=rank==len(matrix),minor_mod_101=det if rank==len(matrix) else None,
                      row_labels=[(n-sum(a),)+a for a in labels],selected_columns=columns,
                      coefficient_matrix_sha256=hashlib.sha256(b''.join(matrix)).hexdigest())
        results.append(result)
        print(json.dumps({k:v for k,v in result.items() if k not in ('row_labels','selected_columns')}),flush=True)
    return dict(n=n,prime=P,seed=20261121+1009*n,dimension=dimension,
                build_seconds=round(built-start,3),elapsed_seconds=round(time.monotonic()-start,3),
                evaluation_matrix_sha256=hashlib.sha256(b''.join(values)).hexdigest(),
                interpolation_grid_checks=checked_indices,results=results)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workers',type=int,default=4)
    parser.add_argument('--output',required=True)
    args = parser.parse_args()
    result = check(workers=args.workers)
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='results'}))


if __name__=='__main__':
    main()
