#!/usr/bin/env python3
"""Exact checks of D-DET-01 on genuinely unpaired genus-zero tuples.

Reuses only the field/matrix/group builders from the G24/GF4 certificates.
The parabolic quotient, ambient Seifert form, and determinant identity are
rebuilt here.  This is a finite consistency certificate, not the proof that
all Nielsen components have the same discriminant (D-DET-01 supplies that).
"""
import importlib.util
import json
import random
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, HERE.parent / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def certify(M, tt, H):
    m = len(H)
    eye = M.eye(m)
    blocks, selectors, dims, prefixes = [], [], [], []
    p = eye
    local_product = M.ONE
    local_dets = []
    for t in tt:
        assert M.mul(t, t) == eye
        assert M.mul(M.star(t), M.mul(H, t)) == H
        a = M.sub(eye, t)
        cols = M.rref(a)[1]
        u = M.tr([M.tr(a)[j] for j in cols])
        rows = M.rref(M.tr(u))[1]
        left = M.inv([u[i] for i in rows])
        gram = M.mul(M.star(u), M.mul(H, u))
        dl = M.det(gram)
        assert dl and not dl.b
        local_product *= dl
        local_dets.append(dl.pair())
        blocks.append(M.mul(p, u))
        selectors.append((rows, left))
        dims.append(len(cols))
        prefixes.append(p)
        p = M.mul(p, t)
    assert p == eye
    D = sum(dims)
    assert D - 2*m == 6
    R = [sum((block[i] for block in blocks), []) for i in range(m)]
    cob = []
    for t, (rows, left) in zip(tt, selectors):
        cob.extend(M.mul(left, [M.sub(eye, t)[i] for i in rows]))
    assert M.rank(R) == M.rank(cob) == m
    assert M.iszero(M.mul(R, cob))
    offsets = [0]
    for d in dims:
        offsets.append(offsets[-1] + d)
    S = M.zero(D, D)
    for j, left in enumerate(blocks):
        for i in range(j, len(tt)):
            block = M.mul(M.star(left), M.mul(H, blocks[i]))
            if i == j:
                block = M.scale(block, M.F(1)/2)
            for a in range(dims[j]):
                for b in range(dims[i]):
                    S[offsets[j]+a][offsets[i]+b] = block[a][b]
    assert M.add(S, M.star(S)) == M.mul(M.star(R), M.mul(H, R))
    assert M.mul(M.star(cob), S) == M.mul(H, R)
    # Extend the coboundaries to the full relation kernel.
    T = [row[:] for row in cob]
    pcols = []
    for v in M.tr(M.nullspace(R)):
        candidate = [row+[x] for row,x in zip(T,v)]
        if M.rank(candidate) > M.rank(T):
            T = candidate
            pcols.append(v)
    assert len(pcols) == 6
    P = M.tr(pcols)
    SP = M.mul(M.star(P), M.mul(S, P))
    assert M.add(SP, M.star(SP)) == M.zero(6,6)
    assert M.rank(SP) == 6
    # Complete the quotient basis to all of the ambient cocycle-value space.
    ccols = []
    for v in M.eye(D):
        candidate = [row+[x] for row,x in zip(T,v)]
        if M.rank(candidate) > M.rank(T):
            T = candidate
            ccols.append(v)
    assert len(ccols) == m
    C = M.tr(ccols)
    B = M.mul(H, M.mul(R,C))
    detT, detB, detSP, detS = M.det(T), M.det(B), M.det(SP), M.det(S)
    norm = lambda a: a*a.conj()
    assert norm(detT)*detS == norm(detB)*detSP
    assert detS == local_product/M.F(2**D)
    witness = detT/(detB*M.F(2**(D//2)))
    assert detSP/local_product == norm(witness)
    assert not detSP.b and detSP.a > 0
    local_norm_witness = M.ONE
    q = local_product.a
    while q > 1 and q.denominator == 1 and q.numerator % 2 == 0:
        q /= 2
        local_norm_witness *= M.w
    assert q == 1 and norm(local_norm_witness) == local_product
    full_norm_witness = witness*local_norm_witness
    assert norm(full_norm_witness) == detSP
    return {
        'tuple': [M.serialize(t) for t in tt],
        'moving_dimensions': dims,
        'adjacent_equal_pairs': sum(tt[i] == tt[i+1] for i in range(0,len(tt),2)),
        'relation_rank': M.rank(R), 'coboundary_rank': M.rank(cob),
        'quotient_dimension': 6, 'local_gram_determinants': local_dets,
        'local_product': local_product.pair(), 'parabolic_determinant': detSP.pair(),
        'determinant_ratio_norm_witness': witness.pair(),
        'determinant_ratio': norm(witness).pair(),
        'local_product_norm_witness': local_norm_witness.pair(),
        'parabolic_determinant_norm_witness': full_norm_witness.pair(),
        'quotient_gram': M.serialize(SP),
        'all_exact_identities_pass': True,
    }


def hurwitz_mix(M, tt, rng):
    tt = list(tt)
    for _ in range(37):
        i = rng.randrange(len(tt)-1)
        a,b = tt[i:i+2]
        # Product ab is preserved; all entries here are involutions.
        tt[i:i+2] = [b, M.mul(b, M.mul(a,b))]
    return tt


def samples(M, refl, initial, extra, H, rng):
    out = []
    for _ in range(3):
        for attempt in range(10000):
            ts = list(initial) + [rng.choice(refl) for _ in range(extra)]
            prod = M.eye(len(H))
            for t in ts:
                prod = M.mul(prod,t)
            last = M.inv(prod)
            if any(last == t for t in refl):
                ts.append(last)
                break
        else:
            raise RuntimeError('fixed-seed unpaired word search exhausted')
        if len(H) == 4:
            ts.extend([M.ZZ,M.ZZ])
        ts = hurwitz_mix(M, ts, rng)
        result = certify(M,ts,H)
        result['last_reflection_search_attempts'] = attempt+1
        assert result['adjacent_equal_pairs'] < len(ts)//2
        out.append(result)
    return out


def all_gf4_involutions(M, gg, ww):
    table = Counter()
    outside = Counter()
    norm_witnesses = {}
    for key in gg:
        g = [list(row) for row in key]
        if M.mul(g,g) != M.eye(4) or g == M.eye(4):
            continue
        a = M.sub(M.eye(4),g)
        cols = M.rref(a)[1]
        u = M.tr([M.tr(a)[j] for j in cols])
        d = M.det(M.mul(M.star(u),u))
        assert not d.b and d.a > 0
        # Exact powers of two are norms because N(t)=2.
        power, q = 0, d.a
        while q > 1 and q.denominator == 1 and q.numerator % 2 == 0:
            q /= 2
            power += 1
        assert q == 1
        witness = M.ONE
        for _ in range(power):
            witness *= M.w
        assert witness*witness.conj() == d
        norm_witnesses[str(d.a)] = witness.pair()
        label = (len(cols),str(d.a))
        table[label] += 1
        if key not in ww:
            assert len(cols) == 2
            outside[label] += 1
    return {
        'nonidentity_involutions': sum(table.values()),
        'all_involution_moving_gram_determinants': [
            {'moving_rank':k[0], 'determinant':k[1], 'count':v}
            for k,v in sorted(table.items())],
        'outside_involutions': [
            {'moving_rank':k[0], 'determinant':k[1], 'count':v}
            for k,v in sorted(outside.items())],
        'determinant_norm_witnesses':norm_witnesses,
    }


def main():
    start=time.time()
    rng=random.Random(20261121)
    A=load('g24_builder','g24/g24_reconstruct.py')
    roots,gg=A.group()
    refs=[A.reflection(v) for v in roots]
    basic=[A.reflection(v) for v in A.eye(3)]
    res={'seed':20261121, 'G24_order':len(gg),
         'G24_unpaired_samples':samples(A,refs,basic,8,A.H,rng)}
    print('G24: three unpaired sixfold tuples passed exact determinant identities',flush=True)
    B=load('gf4_builder','gf4/gf4_reconstruct.py')
    roots,gg,ww=B.group()
    refs=[B.reflection(v) for v in roots]
    simple=B.mat([[0,1,-1,0],[0,0,1,-1],[0,0,0,1],
                  [B.Q(1,2),B.Q(-1,2),B.Q(-1,2),B.Q(-1,2)]])
    basic=[B.reflection(v) for v in simple]
    res.update({'GF4_order':len(gg), 'W_F4_order':len(ww),
                'GF4_unpaired_samples':samples(B,refs,basic,5,B.eye(4),rng),
                'GF4_involution_audit':all_gf4_involutions(B,gg,ww)})
    res['elapsed_seconds']=time.time()-start
    (HERE/'unpaired_determinants.json').write_text(json.dumps(res,indent=2)+'\n')
    print('GF4: three unpaired sixfold tuples and all involution moving forms passed',flush=True)
    print('All exact determinant identities PASS',flush=True)


if __name__ == '__main__':
    main()
