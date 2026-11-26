#!/usr/bin/env python3
"""Exact ranks of the middle type in the binary pentagon cover squared.

This tests compression into one restriction of precisely K_{3,2}(4),
with unchanged party dimensions and no selector or extra resource.
It does not test the profile construction with added selector wires.
"""
from fractions import Fraction
from pathlib import Path
import json
import sys
import numpy as np
import sympy as sp


def party_product(a, b):
    n = a.ndim
    tensor = np.tensordot(a, b, axes=0)
    tensor = tensor.transpose([j for i in range(n) for j in (i, i+n)])
    return tensor.reshape(tuple(x*y for x,y in zip(a.shape,b.shape)))


def exact_ranks(mat):
    if mat.shape[1] > mat.shape[0]:
        mat = mat.T
    basis = {}; selected_rows = []; pivots = []
    gf2 = {}
    for index, raw in enumerate(mat):
        if not np.any(raw):
            continue
        row = [Fraction(int(v)) for v in raw]
        for pivot in sorted(basis):
            if row[pivot]:
                scalar = row[pivot]
                row = [a-scalar*b for a,b in zip(row,basis[pivot])]
        try:
            pivot = next(j for j,v in enumerate(row) if v)
        except StopIteration:
            pass
        else:
            scalar = row[pivot]
            basis[pivot] = [v/scalar for v in row]
            selected_rows.append(index); pivots.append(pivot)
        bits = sum((int(v)&1)<<j for j,v in enumerate(raw))
        while bits:
            lead = bits.bit_length()-1
            if lead in gf2:
                bits ^= gf2[lead]
            else:
                gf2[lead] = bits
                break
    minor = sp.Matrix(mat[np.ix_(selected_rows,pivots)].tolist())
    det = int(minor.det())
    assert det != 0
    return dict(transposed_matrix_shape=list(mat.shape),
                rank_over_Q=len(basis),rank_over_F2=len(gf2),
                rational_pivot_rows=selected_rows,
                rational_pivot_columns=pivots,
                nonzero_minor_determinant=det,
                every_row_reduced_exactly=True)


def main():
    cfg = json.loads(Path(sys.argv[1]).read_text())
    data = np.load(cfg['binary_tables'])
    s,u = data['term_0'],data['term_1']
    middle = party_product(s,u)+party_product(u,s)
    records = {}
    n = middle.ndim
    for name,axes in [('left_right',[0,1,2])]+[(f'singleton_{i}',[i]) for i in range(n)]:
        other = [i for i in range(n) if i not in axes]
        arr = middle.transpose(axes+other)
        arr = arr.reshape(int(np.prod([middle.shape[i] for i in axes])), -1)
        records[name] = exact_ranks(arr)
    assert [records[f'singleton_{i}']['rank_over_Q'] for i in range(5)] == [16,16,16,4,4]
    assert [records[f'singleton_{i}']['rank_over_F2'] for i in range(5)] == [16,16,16,4,4]
    assert records['left_right']['rank_over_Q'] == 10
    assert records['left_right']['rank_over_F2'] == 6
    # Remove the two shared EPR paths.  The grouped local bases interleave
    # the two binary copies; this extraction accounts for that permutation.
    core = np.zeros((4,)*4,dtype=np.int64)
    for a in range(4):
        for b in range(4):
            core[a,b] = middle[4*(a//2)+a%2,0,8*(b//2)+2*(b%2)]
    core_minors = []
    for k in range(4):
        mat = np.moveaxis(core,k,0).reshape(4,-1)
        binary_basis = {}; columns = []
        for j,col in enumerate(mat.T):
            bits = sum((int(x)&1)<<i for i,x in enumerate(col))
            while bits:
                p = bits.bit_length()-1
                if p in binary_basis:
                    bits ^= binary_basis[p]
                else:
                    binary_basis[p] = bits; columns.append(j); break
            if len(columns)==4:
                break
        minor = mat[:,columns]
        determinant = int(sp.Matrix(minor.tolist()).det())
        assert abs(determinant)==1
        core_minors.append(dict(axis=k,columns=columns,matrix=minor.tolist(),
                                determinant=determinant))
    result = dict(input=cfg,profile='S tensor U + U tensor S, grouped at each party',
                  shape=list(middle.shape),entries=int(middle.size),
                  nonzero_entries=int(np.count_nonzero(middle)),
                  coefficients=sorted({int(x) for x in middle.ravel()}),
                  ranks=records,
                  core_singleton_unit_minors=core_minors,
                  exact_K32_q4_restriction_impossible_over_Q_C_F2=True,
                  reason='Full left singleton ranks force invertible maps; full right ranks force global left:right rank16, contradicting10 or6.',
                  scope='One exact restriction of unchanged K32(4); no obstruction to border covers, selector-augmented profiles or asymptotic covers is asserted.')
    out = Path(sys.argv[2]);out.write_text(json.dumps(result,indent=2))
    np.savez_compressed(out.with_suffix('.npz'),middle=middle)
    print(json.dumps(result),flush=True)


if __name__=='__main__':
    main()
