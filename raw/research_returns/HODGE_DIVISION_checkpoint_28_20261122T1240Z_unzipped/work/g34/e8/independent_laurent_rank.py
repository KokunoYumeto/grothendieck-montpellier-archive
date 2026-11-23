#!/usr/bin/env python3
"""Independent reconstruction of the E8 candidate multiplication map.

GPT-6 Astra Pro, inherited effort, /root/g34, 2026-11-21.
Only numerical residue-centre data and its candidate radius are read.
No supplied period matrices, Frobenius coefficients, pivots, or outputs
are imported. Exact existence in this box is a separate cert_M gate.

The original s-coordinate makes both pulled-back local gauges series
in s^5 (respectively t^5). Every required jet has width at most four,
so the holomorphic differential spaces are given by two flag problems.
"""
from pathlib import Path
from fractions import Fraction as F
import json, hashlib, time
import numpy as np
from flint import acb, arb, acb_mat, ctx

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / 'l_check'
ctx.prec = 256
N = 8

def exact(q):
    if isinstance(q, F):
        return acb(q.numerator) / q.denominator
    return acb(q)

def eye(n):
    return acb_mat([[int(i == j) for j in range(n)] for i in range(n)])

def midpoint(M):
    return np.array([[complex(float(M[i,j].real.mid()),
                              float(M[i,j].imag.mid()))
                      for j in range(M.ncols())] for i in range(M.nrows())])

def choose_minor(M, rank):
    """Fresh complete-pivot Gaussian elimination on complex midpoints.

    This selects indices only. Every assertion of invertibility below
    is subsequently made in Arb, not inferred from floating point.
    """
    A = midpoint(M).copy()
    rows, cols = list(range(A.shape[0])), list(range(A.shape[1]))
    for k in range(rank):
        a, b = np.unravel_index(np.abs(A[k:,k:]).argmax(), A[k:,k:].shape)
        a += k; b += k
        assert abs(A[a,b]) > 1e-14
        A[[k,a],:] = A[[a,k],:]; rows[k], rows[a] = rows[a], rows[k]
        A[:,[k,b]] = A[:,[b,k]]; cols[k], cols[b] = cols[b], cols[k]
        for i in range(k+1, A.shape[0]):
            v = A[i,k] / A[k,k]
            A[i,k:] -= v * A[k,k:]
    return rows[:rank], cols[:rank]

def norm_upper(M):
    return max(sum((abs(M[i,j]) for j in range(M.ncols())), arb(0)).upper()
               for i in range(M.nrows()))

def null_basis(M, dimension, label):
    rank = M.ncols() - dimension
    rows, dep = choose_minor(M, rank)
    free = [j for j in range(M.ncols()) if j not in dep]
    S = acb_mat([[M[i,j] for j in dep] for i in rows])
    assert not S.det().contains(0), label + ' pivot determinant'
    Si = S.inv()
    R = acb_mat([[Si[i,j].mid() for j in range(rank)] for i in range(rank)])
    neumann = norm_upper(eye(rank) - R*S)
    assert neumann < 1, label + ' Neumann test'
    result = []
    for f in free:
        v = [acb(0) for _ in range(M.ncols())]
        v[f] = acb(1)
        sol = Si * acb_mat([[-M[i,f]] for i in rows])
        for k,j in enumerate(dep):
            v[j] = sol[k,0]
        result.append(v)
    residual = arb(0)
    for v in result:
        w = M * acb_mat([[x] for x in v])
        for i in range(w.nrows()):
            assert w[i,0].contains(0), label + ' unused row'
            residual = max(residual, abs(w[i,0]).upper())
    record = dict(shape=[M.nrows(),M.ncols()], nullity=dimension,
                  rows=rows, dependent=dep, free=free,
                  neumann=str(neumann), residual=str(residual))
    print(label, record['shape'], 'Neumann', neumann, flush=True)
    return result, record

def main():
    start = time.time()
    xt = json.loads((INPUT/'xtilde_g_0.json').read_text())
    meta = json.loads((INPUT/'meta_g_0.json').read_text())
    cert = json.loads((INPUT/'certM_g_0.json').read_text())
    rho = cert['rho']
    w = [acb(arb(x,rho),arb(y,rho)) for x,y in xt]
    u1 = [acb(x,y) for x,y in meta['u1f']]
    v1, v2 = w[:8], w[15:23]
    u2 = [None]*8
    u2[meta['j0']] = acb(*meta['u2j0'])
    for k,j in enumerate(meta['others']):
        u2[j] = w[8+k]
    mvals = [1,3,7,9,11,13,17,19]
    B0 = acb_mat([[exact(F(mvals[i],20)) if i==j else 0
                  for j in range(N)] for i in range(N)])
    B1 = acb_mat([[u1[i]*v1[j] for j in range(N)] for i in range(N)])
    Bc = acb_mat([[u2[i]*v2[j] for j in range(N)] for i in range(N)])
    Binf = -(B0+B1+Bc)
    beta = [F(-1),F(-1),F(-11,12),F(-2,3),F(-7,12),
            F(-5,12),F(-1,3),F(-1,12)]

    # Fresh eigenbases from exact candidate eigenvalues. Their exact
    # multiplicities follow from the separately certified monodromy.
    columns, labels, eigen_records = [], [], []
    for value in sorted(set(beta)):
        mult = beta.count(value)
        eig, rec = null_basis(Binf-eye(N)*exact(value), mult,
                             'infinity eigenspace '+str(value))
        columns.extend(eig); labels.extend([value]*mult)
        eigen_records.append(rec)
    P = acb_mat([[columns[j][i] for j in range(N)] for i in range(N)])
    assert not P.det().contains(0)
    Pi = P.inv()
    spectral = Pi*Binf*P
    for i,e in enumerate(labels):
        rad = sum((abs(spectral[i,j]) for j in range(N) if i != j),arb(0))
        assert abs(spectral[i,i]-exact(e))+rad < arb(1)/10**10

    lam0 = [F(m+1,4)-3 for m in mvals]
    laminf = [5*e+F(11,4) for e in labels]
    floor = lambda x: x.numerator//x.denominator
    f0a, fia = list(map(floor,lam0)), list(map(floor,laminf))
    f0b, fib = [floor(-e) for e in lam0], [floor(-e) for e in laminf]
    assert f0a == [-3,-2,-1,-1,0,0,1,2]
    assert min(fia)==-3 and max(fia)==2
    assert min(f0b)==-2 and max(f0b)==2
    assert min(fib)==-3 and max(fib)==2

    # R(s)=sum_{k=-3}^1 r_k s^k. At zero the frame is the
    # coordinate frame; at infinity it is P. Local coefficients
    # t^{-2-k} of the one-form have an immaterial common minus sign.
    aidx = {(k,j):(k+3)*N+j for k in range(-3,2) for j in range(N)}
    Arows = []
    for j in range(N):
        for k in range(-3,min(2,f0a[j])):
            row=[acb(0)]*40; row[aidx[k,j]]=acb(1); Arows.append(row)
    for j in range(N):
        for k in range(-3,2):
            if -2-k < fia[j]:
                row=[acb(0)]*40
                for i in range(N): row[aidx[k,i]]=Pi[j,i]
                Arows.append(row)
    assert len(Arows)==37
    avec, arec = null_basis(acb_mat(Arows),3,'A Laurent constraints')

    # Q(s)=sum_{k=-2}^1 q_k s^k + v1 P1(s)/(s^5-1)
    #                           + v2 Pc(s)/(s^5-c), deg P1,Pc<=4.
    # Residues at the ten reflection points then have exactly the
    # required one-dimensional directions, without root extraction.
    c = acb(2,1)
    bidx = {(k,j):(k+2)*N+j for k in range(-2,2) for j in range(N)}
    pidx = lambda a,j: 32+5*a+j
    Brows=[]
    for i in range(N):
        for k in range(-2,min(2,f0b[i])):
            row=[acb(0)]*42; row[bidx[k,i]]=acb(1)
            if k>=0:
                row[pidx(0,k)] = -v1[i]
                row[pidx(1,k)] = -v2[i]/c
            Brows.append(row)
    for j in range(N):
        for ell in range(-3,min(2,fib[j])):
            row=[acb(0)]*42
            k=-ell-2
            if -2<=k<=1:
                for i in range(N): row[bidx[k,i]]=P[i,j]
            degree=3-ell
            if 0<=degree<=4:
                row[pidx(0,degree)] = sum((P[i,j]*v1[i] for i in range(N)),acb(0))
                row[pidx(1,degree)] = sum((P[i,j]*v2[i] for i in range(N)),acb(0))
            Brows.append(row)
    assert len(Brows)==39
    bvec,brec=null_basis(acb_mat(Brows),3,'B Laurent constraints')

    # Coefficients of s(s^5-1)(s^5-c) R(s)^T Q(s).
    # The actual holomorphic contraction proves that only powers0..8
    # survive. Outside coefficients are also checked for consistency.
    products=[]; outside=arb(0)
    for ar in avec:
        for bq in bvec:
            coeff={k:acb(0) for k in range(-4,14)}
            for k in range(-3,2):
                for ell in range(-2,2):
                    dot=sum((ar[aidx[k,i]]*bq[bidx[ell,i]] for i in range(N)),acb(0))
                    for shift,mult in [(1,c),(6,-1-c),(11,acb(1))]:
                        coeff[k+ell+shift]+=mult*dot
                for which,direction,constant in [(0,v1,-c),(1,v2,acb(-1))]:
                    dot=sum((ar[aidx[k,i]]*direction[i] for i in range(N)),acb(0))
                    for degree in range(5):
                        v=dot*bq[pidx(which,degree)]
                        coeff[k+degree+1]+=constant*v
                        coeff[k+degree+6]+=v
            for k,v in coeff.items():
                if not 0<=k<=8:
                    assert v.contains(0),('outside',k,str(v))
                    outside=max(outside,abs(v).upper())
            products.append([coeff[k] for k in range(9)])
    product=acb_mat(products)
    determinant=product.det()
    assert not determinant.contains(0)
    print('INDEPENDENT polynomial coefficient determinant',determinant,flush=True)
    print('absolute determinant lower',abs(determinant).lower(),flush=True)
    print('PASS: rank9 from independent Laurent-coordinate computation',flush=True)
    report=dict(statement='E8 candidate smooth multiplication rank from residue box',
       date='2026-11-21',model='GPT-6 Astra Pro; inherited effort',
       algorithm='Independent s-Laurent flag calculation, no Frobenius jets or supplied L matrices',
       source='Candidate residue seeds from Severn Zenodo23549514; existence separately checked',
       flint_precision_bits=ctx.prec,rho=str(rho),
       infinity_exponents=list(map(str,labels)),pulled_zero_exponents=list(map(str,lam0)),
       pulled_infinity_exponents=list(map(str,laminf)),
       infinity_eigenbasis_records=eigen_records,A=arec,B=brec,
       polynomial_coefficient_matrix=[[str(v) for v in row] for row in products],
       determinant=str(determinant),abs_determinant_lower=str(abs(determinant).lower()),
       outside_residual=str(outside),rank=9,
       inputs={n:hashlib.sha256((INPUT/n).read_bytes()).hexdigest()
               for n in ['xtilde_g_0.json','meta_g_0.json','certM_g_0.json']},
       elapsed_seconds=time.time()-start)
    Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':main()
