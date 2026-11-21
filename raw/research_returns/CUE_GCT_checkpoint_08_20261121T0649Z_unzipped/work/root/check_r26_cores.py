#!/usr/bin/env python3
"""Independently reconstruct R26 core matrices by enumerating path matchings.

This checks the 17 finite cores and their recorded minors. The all-size
insertion argument is a separate whole-proof check, not a computational claim.
"""
from pathlib import Path
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json

base = Path(__file__).resolve().parents[2]
source = base/'work/rectangular/border_ternary/jacobi_uniform_cores.json'
records = json.loads(source.read_text())
checks = []

def determinant_mod(rows, p):
    a = [row[:] for row in rows]
    n = len(a)
    previous = 1
    sign = 1
    for k in range(n-1):
        if not a[k][k]:
            j = next(i for i in range(k+1, n) if a[i][k])
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        inverse = pow(previous, -1, p)
        for i in range(k+1, n):
            for j in range(k+1, n):
                a[i][j] = (pivot*a[i][j]-a[i][k]*a[k][j])*inverse % p
        for i in range(k+1, n):
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1] % p

for record in records:
    r, j, p = record['r'], record['j'], record['prime']
    m = r+j
    d = record['d']
    K = record['K']
    assert d == [0 if i in record['cuts'] else ((7*i*i+13*i+36)%p or 1)
                 for i in range(m-1)]

    @lru_cache(None)
    def matching_polynomial(a, b):
        # Direct enumeration of independent edge subsets, not the author's
        # continuant recurrence. An edge contributes d_e*tau.
        result = [0]*((b-a+1)//2+1)
        if b < a:
            return (1,)
        def visit(start, count, weight):
            result[count] = (result[count]+weight) % p
            for e in range(start, b):
                visit(e+2, count+1, weight*d[e] % p)
        visit(a, 0, 1)
        return tuple(result)

    positive_count = (j+1)//2+1
    negative_count = (r+1)//2+1
    matrix = [[0]*8 for _ in range(positive_count+negative_count)]
    # (interval start, interval end, tau shift, scalar): derived directly
    # from x a_r, y a_(r-1), z a_(r+1), x b_j, y b_(j+1),
    # z b_(j-1), t_r, t'_j after dividing by y^r and D_r*z^j.
    positive = [(r+1,m-1,0,1),(r,m-1,0,1),(r+2,m-1,1,1),
                (0,j-1,0,1),(0,j,0,1),(0,j-2,1,1),
                (r+1,m-2,1,2),(1,j-1,0,2)]
    negative = [(0,r-1,0,1),(0,r-2,1,d[r-1]),
                (0,r,0,pow(d[r],-1,p)),(j+1,m-1,0,K),
                (j+2,m-1,1,K*d[j]),(j,m-1,0,K*pow(d[j-1],-1,p)),
                (1,r-1,0,2),(j+1,m-2,1,2*K)]
    for offset, components in [(0, positive),(positive_count, negative)]:
        for column, (a,b,shift,scale) in enumerate(components):
            for degree, coefficient in enumerate(matching_polynomial(a,b)):
                matrix[offset+shift+degree][column] = coefficient*scale % p
    assert matrix == record['matrix'], (r,j,'matrix mismatch')
    selected = [matrix[i] for i in record['selected_rows_in_order']]
    residue = determinant_mod(selected,p)
    assert residue == record['selected_minor'] != 0, (r,j,residue)
    if min(r,j) <= 5:
        numerator = denominator = 1
        for e in range(min(r,j)):
            numerator = numerator*d[e] % p
        for e in range(max(r,j),m-1):
            denominator = denominator*d[e] % p
        assert K == numerator*pow(denominator,-1,p) % p
    checks.append({'r':r,'j':j,'all_entries_matched':True,
                   'entry_count':len(matrix)*8,'minor':residue})

assert len(checks) == 17
result = {'checked_utc':datetime.now(timezone.utc).isoformat(),
          'who':'GPT-6 Astra Pro; root; effort not exposed; CUE_GCT_20261121_R1',
          'status':'PASS','certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
          'entry_method':'Independent enumeration of all matchings of each interval path',
          'minor_method':'Fraction-free Bareiss recurrence modulo 101 with swap signs',
          'cores':checks,'scope':'Finite core certificates only; uniform extension requires the separate insertion proof.'}
(base/'work/root/r26_core_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
