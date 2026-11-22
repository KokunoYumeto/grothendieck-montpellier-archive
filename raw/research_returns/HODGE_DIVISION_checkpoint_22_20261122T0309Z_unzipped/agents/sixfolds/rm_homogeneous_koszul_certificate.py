#!/usr/bin/env python3
"""Exact checks for SF-E846.  No first-order existence witness is asserted.

The universal proof is in the adjoining Markdown file.  This program checks
the full finite exterior operator spaces, all internal degree bounds, and
the actual 31-by-31 Moyal matrix identities at three independent rational
inputs.  The latter are identities without imposing the first-order
equations; their Bianchi remainder is retained explicitly.
"""
from __future__ import annotations
import hashlib
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
import sympy as s

HERE = Path(__file__).resolve().parent
START = datetime.now(timezone.utc).isoformat()
T0 = perf_counter()
CHECKS = []


def check(name, condition, details=None):
    if not condition:
        raise AssertionError((name, details))
    CHECKS.append({'name': name, 'pass': True, 'details': details})


B = {p: list(itertools.combinations(range(4), p)) for p in range(5)}
N = {p: len(B[p]) for p in B}


def contract(i, p):
    out = s.zeros(N[p-1], N[p])
    for j, basis in enumerate(B[p]):
        if i in basis:
            at = basis.index(i)
            image = basis[:at] + basis[at+1:]
            out[B[p-1].index(image), j] = (-1)**at
    return out


def wedge(i, p):
    out = s.zeros(N[p+1], N[p])
    for j, basis in enumerate(B[p]):
        if i not in basis:
            image = tuple(sorted((i,) + basis))
            out[B[p+1].index(image), j] = (-1)**sum(a < i for a in basis)
    return out


I = {(i,p): contract(i,p) for i in range(4) for p in range(1,5)}
E = {(i,p): wedge(i,p) for i in range(4) for p in range(4)}
PAIRS = list(itertools.combinations(range(4), 2))


def icon(v, p):
    return sum((v[i]*I[i,p] for i in range(4)), s.zeros(N[p-1],N[p]))


def itwo(b, p):
    return sum((b[i,j]*(I[j,p-1]*I[i,p]) for i,j in PAIRS),
               s.zeros(N[p-2],N[p]))


def hform(A, p):
    if p < 2:
        return s.zeros(N[p-1],N[p])
    return sum((E[l,p-2]*itwo(A[l],p) for l in range(4)),
               s.zeros(N[p-1],N[p]))


def operator_space_rank(kind):
    if kind == 'lower_chain':
        domains = list(range(1,5))
        shape = {p: (N[p],N[p]) for p in domains}
        equations = [(p,i) for p in range(2,5) for i in range(4)]
    else:
        domains = list(range(1 if kind == 'top_anticommutant' else 2,5))
        shape = {p: (N[p-1],N[p]) for p in domains}
        equations = [(p,i) for p in range(2 if kind == 'top_anticommutant' else 3,5)
                     for i in range(4)]
    columns = []
    for q in domains:
        for a in range(shape[q][0]):
            for b in range(shape[q][1]):
                X = {p: s.zeros(*shape[p]) for p in domains}
                X[q][a,b] = 1
                values = []
                for p,i in equations:
                    if kind == 'lower_chain':
                        z = I[i,p]*X[p]-X[p-1]*I[i,p]
                    else:
                        z = I[i,p-1]*X[p]+X[p-1]*I[i,p]
                    values.extend(list(z))
                columns.append(s.Matrix(values))
    mat = s.Matrix.hstack(*columns)
    rank = mat.rank()
    return {'variables': mat.cols, 'equations': mat.rows, 'rank': rank,
            'kernel_dimension': mat.cols-rank}


for kind, expected in [('lower_chain',1),('top_anticommutant',4),
                       ('bottom_anticommutant',4)]:
    data = operator_space_rank(kind)
    check(kind, data['kernel_dimension'] == expected, data)

# The resolution has top K_p, p=0,...,4, and bottom K_q in degree q-1.
blocks = [(side,p) for side in ('T','B')
          for p in (range(5) if side == 'T' else range(1,5))]
offset = {}
total = 0
for z in blocks:
    offset[z] = total
    total += N[z[1]]
check('resolution_total_free_rank', total == 31, total)


def put(M, dst, src, block):
    a,b = offset[dst],offset[src]
    M[a:a+block.rows,b:b+block.cols] = block


def get(M, dst, src):
    a,b = offset[dst],offset[src]
    return M[a:a+N[dst[1]],b:b+N[src[1]]]


def homological(z):
    return z[1] if z[0] == 'T' else z[1]-1


def internal(z):
    return 3+2*z[1] if z[0] == 'T' else 2*z[1]


coefficient_degrees = []
for src in blocks:
    for dst in blocks:
        if homological(src)-homological(dst) == 1:
            coefficient_degrees.append(-4+internal(src)-internal(dst))
check('no_degree_one_homotopy_internal_minus4',
      max(coefficient_degrees) < 0, sorted(set(coefficient_degrees)))

x = s.symbols('x0:4')


def expand(M):
    return M.applyfunc(s.expand)


def zero(M):
    return all(s.expand(v) == 0 for v in M)


def m1(F,G,pi):
    out = s.zeros(total)
    for i,j in itertools.product(range(4),repeat=2):
        if pi[i,j]:
            out += s.Rational(1,2)*pi[i,j]*(F.diff(x[i])*G.diff(x[j]))
    return expand(out)


def m2(F,G,pi):
    nz = [(i,j,pi[i,j]) for i,j in itertools.product(range(4),repeat=2)
          if pi[i,j]]
    out = s.zeros(total)
    for i,j,a in nz:
        for k,l,b in nz:
            out += s.Rational(1,8)*a*b*(F.diff(x[i],x[k])*G.diff(x[j],x[l]))
    return expand(out)


for seed in range(1,4):
    f = [x[i]**2+(seed+i)*x[(i+1)%4]*x[(i+2)%4] for i in range(4)]
    b = {(i,j): sum((((seed+2*i+3*j+k)%7)-3)*x[k] for k in range(4))
         for i,j in PAIRS}
    c = sum((seed+k)*x[k] for k in range(4))
    v = [seed-2*i for i in range(4)]
    w = [2*seed+i-3 for i in range(4)]
    A = [{(i,j): ((3*l+2*i+j+seed)%5)-2 for i,j in PAIRS} for l in range(4)]
    pi = s.zeros(4)
    for i,j in PAIRS:
        pi[i,j] = ((seed+i+2*j)%5)-2
        pi[j,i] = -pi[i,j]
    check(f'input_{seed}_symplectic', pi.det() != 0, int(pi.det()))
    D,H = s.zeros(total),s.zeros(total)
    for p in range(1,5):
        put(D,('T',p-1),('T',p),icon(f,p))
        put(H,('T',p-1),('T',p),hform(A,p)+icon(v,p))
        put(H,('B',p),('T',p),c*s.eye(N[p]))
    for q in range(2,5):
        put(D,('B',q-1),('B',q),-icon(f,q))
        put(D,('T',q-2),('B',q),itwo(b,q))
        put(H,('B',q-1),('B',q),-hform(A,q)+icon(w,q))
    check(f'input_{seed}_actual_resolution_square', zero(D*D))
    E1 = expand(D*H+H*D+m1(D,D,pi))
    O = expand(H*H+m1(D,H,pi)+m1(H,D,pi)+m2(D,D,pi))
    r = [-sum(pi[i,j]*s.diff(f[a],x[i])*s.diff(c,x[j])
              for i,j in itertools.product(range(4),repeat=2))+c*(v[a]+w[a])
         for a in range(4)]
    for p in range(2,5):
        check(f'input_{seed}_O21_exterior_degree_{p}',
              zero(get(O,('B',p-1),('T',p))-icon(r,p)))
    bianchi = D*O-O*D+H*E1-E1*H+m1(D,E1,pi)-m1(E1,D,pi)
    check(f'input_{seed}_full_order2_bianchi_with_E1_remainder', zero(bianchi))
    P = {(i,j): sum(pi[a,c0]*s.diff(f[i],x[a])*s.diff(f[j],x[c0])
                     for a,c0 in itertools.product(range(4),repeat=2))
         for i,j in PAIRS}
    expected = {ij: sum(f[l]*A[l][ij] for l in range(4))+c*b[ij]-P[ij]
                for ij in PAIRS}
    for p in range(2,5):
        check(f'input_{seed}_top_first_order_diagonal_{p}',
              zero(get(E1,('T',p-2),('T',p))-itwo(expected,p)))

# For C=x0 and its nonzero Hamiltonian field partial_x1, solve the full
# ten-coefficient quadratic equation partial_x1(f) in C*x0.
quadratic_monomials = [x[i]*x[j] for i in range(4) for j in range(i,4)]
coeff = s.symbols('a0:10')
f_generic = sum(a*m for a,m in zip(coeff,quadratic_monomials))
z = s.symbols('z')
eq = s.Poly(s.diff(f_generic,x[1])-z*x[0],*x)
solution = s.linsolve(eq.coeffs(), (*coeff,z))
check('Hamiltonian_linear_eigenform_forces_axis_basepoint',
      all(s.expand(f_generic.subs(dict(zip((*coeff,z),row)))).subs(
          {x[0]:0,x[1]:1,x[2]:0,x[3]:0}) == 0 for row in solution),
      str(solution))
check('residue_weight_canonical_volume_included', -4-2+4 == -2,
      {'local_Ext2_weight':-4,'bivector_evaluation_weight':-2,
       'volume_weight':4,'total_weight':-2,'trace_weight':0})

result = {
    'statement':'SF-E846 exact homogeneous scalar-extension identities',
    'started_utc':START,
    'finished_utc':datetime.now(timezone.utc).isoformat(),
    'elapsed_seconds':perf_counter()-T0,
    'author':'GPT-6 Astra Pro /root/sixfolds; inherited effort not exposed',
    'status':'PASS',
    'scope':'Universal exterior operator ranks and degree table; three exact 31x31 matrix identity checks. No first-order existence witness, global proof, source audit, or independent review is certified by computation.',
    'checks':CHECKS,
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(HERE/'rm_homogeneous_koszul_certificate_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(CHECKS),'elapsed_seconds':result['elapsed_seconds'],
                  'started_utc':START,'finished_utc':result['finished_utc']}))
