#!/usr/bin/env python3
"""Complete binary trace-code enumeration for a partial-packet operator test.

This is finite module arithmetic only. It constructs no curve or cover.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json


def mul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        b >>= 1
        a <<= 1
        if a & 32:
            a ^= 0b100101
    return c


def trace(a):
    t = 0
    for _ in range(5):
        t ^= a
        a = mul(a, a)
    assert t in (0, 1)
    return t


def cyclic_mul(a, b, modulus):
    out = [0] * 31
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[(i+j) % 31] = (out[(i+j) % 31] + x*y) % modulus
    return out


def newton_idempotent(a):
    a2 = cyclic_mul(a, a, 8)
    a3 = cyclic_mul(a2, a, 8)
    return [(3*x-2*y) % 8 for x, y in zip(a2, a3)]


def main():
    zeta = [1]
    for _ in range(30):
        zeta.append(mul(zeta[-1], 2))
    # These are all nonzero elements, each a power of zeta with inverse.
    # Thus the specified quotient ring is a field and zeta has order31.
    assert len(set(zeta)) == 31 and set(zeta) == set(range(1, 32))
    assert mul(zeta[-1], 2) == 1
    omega = sorted({pow(2, j, 31) for j in range(5)} |
                   {(-pow(2, j, 31)) % 31 for j in range(5)})
    assert len(omega) == 10 and 0 not in omega

    rows, words, hist = [], set(), Counter()
    for a in range(32):
        for b in range(32):
            bits = [trace(mul(a,zeta[i]) ^ mul(b,zeta[-i % 31])) for i in range(31)]
            word = sum(c << i for i,c in enumerate(bits))
            assert word not in words
            words.add(word)
            weight = sum(bits)
            hist[weight] += 1
            rows.append({'a':a, 'b':b, 'word_integer':word, 'weight':weight})
    expected = {0:1, 10:31, 12:155, 14:310, 16:217, 18:155, 20:155}
    assert dict(hist) == expected
    assert min(w for w in hist if w) == 10

    def dft(bits):
        out = []
        for k in range(31):
            v = 0
            for i,c in enumerate(bits):
                if c:
                    v ^= zeta[k*i % 31]
            out.append(v)
        return out

    generators = []
    for a,b in [(1<<j,0) for j in range(5)] + [(0,1<<j) for j in range(5)]:
        bits = [trace(mul(a,zeta[i]) ^ mul(b,zeta[-i % 31])) for i in range(31)]
        values = dft(bits)
        assert all(v == 0 for k,v in enumerate(values) if k not in omega)
        generators.append({'a':a,'b':b,'dft':values})

    e0 = [trace(zeta[i]) ^ trace(zeta[-i % 31]) for i in range(31)]
    assert sum(e0) == 10
    assert dft(e0) == [int(k in omega) for k in range(31)]
    assert cyclic_mul(e0,e0,2) == e0
    e8 = newton_idempotent(newton_idempotent(e0))
    assert cyclic_mul(e8,e8,8) == e8
    assert [x % 2 for x in e8] == e0
    assert sum(e8) % 8 == 0
    complement = [(-x) % 8 for x in e8]
    complement[0] = (complement[0]+1) % 8
    assert cyclic_mul(e8,complement,8) == [0]*31
    assert cyclic_mul(complement,complement,8) == complement
    assert any(x % 2 for x in complement)

    data = {
      'status':'PASS',
      'scope':'Complete finite trace-code and idempotent arithmetic; no geometric realization.',
      'field_modulus_binary':0b100101,
      'zeta_powers':zeta,
      'spectral_support_omega':omega,
      'dimension':10,
      'number_of_distinct_words':len(words),
      'weight_distribution':dict(sorted(hist.items())),
      'minimum_nonzero_weight':10,
      'all_words':rows,
      'ten_generators_dft':generators,
      'binary_idempotent_coefficients':e0,
      'lifted_idempotent_mod8_coefficients':e8,
      'complement_idempotent_mod8_coefficients':complement,
      'bad_module_rank_over_Z8':21,
      'annihilator_minimum_from_written_proof_not_operator_enumeration':8,
      'largest_integer_d_with_31_greater_than_d_minus_1_squared':6,
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    out=Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','dimension':10,'words':1024,'minimum_weight':10,
                      'weight_distribution':dict(sorted(hist.items())), 'output':str(out)}))


if __name__=='__main__':
    main()
