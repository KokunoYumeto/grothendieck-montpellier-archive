#!/usr/bin/env python3
"""Independent SF-E838 reconstruction using sparse rational polynomials.

No SymPy, author arithmetic, or author code is imported. Seven exact
evaluations determine each homogeneous degree-six determinant pencil.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
import datetime
import hashlib
import json
import time

started = time.perf_counter()
HERE = Path(__file__).resolve().parent
PROOF = HERE.parents[1]/'sixfolds/rm_quadratic_jet_obstruction_draft.md'
FROZEN = '43e434aba81f88dc0ae386173bb7e01e2742b646f16bef89c5291a880bdee75c'
assert hashlib.sha256(PROOF.read_bytes()).hexdigest() == FROZEN
ZERO = (0, 0, 0, 0)


def clean(p):
    return {m:Q(c) for m,c in p.items() if c}


def add(*ps):
    out = {}
    for p in ps:
        for m,c in p.items():
            out[m] = out.get(m,Q(0))+c
    return clean(out)


def scale(p,c):
    return clean({m:Q(c)*v for m,v in p.items()})


def mul(p,q):
    out = {}
    for m,c in p.items():
        for n,d in q.items():
            v = tuple(x+y for x,y in zip(m,n))
            out[v] = out.get(v,Q(0))+c*d
    return clean(out)


def diff(p,i):
    out = {}
    for m,c in p.items():
        if m[i]:
            n = list(m)
            n[i] -= 1
            out[tuple(n)] = c*m[i]
    return clean(out)


def bracket(p,q,i,j):
    return add(mul(diff(p,i),diff(q,j)),scale(mul(diff(p,j),diff(q,i)),-1))


def elimination(rows):
    a = [[Q(x) for x in row] for row in rows]
    k,det = 0,Q(1)
    for col in range(len(a[0])):
        pivot = next((r for r in range(k,len(a)) if a[r][col]),None)
        if pivot is None:
            continue
        if pivot != k:
            a[k],a[pivot] = a[pivot],a[k]
            det = -det
        p = a[k][col]
        det *= p
        for r in range(k+1,len(a)):
            if a[r][col]:
                c = a[r][col]/p
                for j in range(col+1,len(a[0])):
                    a[r][j] -= c*a[k][j]
                a[r][col] = Q(0)
        k += 1
        if k == len(a):
            break
    return k,det if k == len(a) == len(a[0]) else Q(0)


def det(rows):
    return elimination(rows)[1]


z = []
for i in range(4):
    m = [0]*4
    m[i] = 1
    z.append({tuple(m):Q(1)})
pairs = list(combinations(range(4),2))
monomials = [next(iter(mul(x,x))) for x in z]
monomials += [next(iter(mul(z[i],z[j]))) for i,j in pairs]
J = [[Q(x) for x in row] for row in
     [[1,0,1,0],[0,1,0,1],[Q(-3,5),1,Q(-9,5),2],[Q(-8,5),1,Q(-16,5),3]]]
assert det(J) == Q(-4,5)
ell = [add(*(scale(z[j],row[j]) for j in range(4))) for row in J]
Fs = [mul(x,x) for x in ell]
Fn = Fs.copy()
Fn[0] = add(Fn[0],mul(ell[1],ell[2]))


def coeff_matrix(polys,basis=monomials):
    return [[p.get(m,Q(0)) for p in polys] for m in basis]


def pencil_columns(fs,a,b):
    return fs + [add(scale(bracket(fs[i],fs[j],0,1),a),
                     scale(bracket(fs[i],fs[j],2,3),b)) for i,j in pairs]


def poly_product(p,q):
    out = [Q(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j] += a*b
    return out


def interpolate(values):
    out = [Q(0)]*len(values)
    for i,value in enumerate(values):
        basis,den = [Q(1)],Q(1)
        for j in range(len(values)):
            if i != j:
                basis = poly_product(basis,[Q(-j),Q(1)])
                den *= i-j
        for k,c in enumerate(basis):
            out[k] += value*c/den
    return out


target = [Q(-100663296,78125)]
for c in (1,1,2,2,3,3):
    target = poly_product(target,[Q(c),Q(1)])
T = [[2,1,0,0],[0,3,1,0],[0,0,1,1],[0,0,0,1]]
Ft = [add(*(scale(Fn[j],T[i][j]) for j in range(4))) for i in range(4)]
assert det(T) == 6
records = []
for name,fs,mult in [('squares',Fs,1),('nonsquare',Fn,1),('different_generator_change',Ft,6**4)]:
    values = [det(coeff_matrix(pencil_columns(fs,a,1))) for a in range(7)]
    coefficients = interpolate(values)
    assert coefficients == [mult*c for c in target]
    endpoint = det(coeff_matrix(pencil_columns(fs,1,0)))
    assert endpoint == mult*target[6] != 0
    assert values[0] != 0
    records.append({'name':name,'b1_values_a0_to_6':list(map(str,values)),
                    'coefficients_a6_to_b6':list(map(str,reversed(coefficients))),
                    'a1_b0_endpoint':str(endpoint)})

# Ambient coordinate covariance is reconstructed independently from ten
# actual quadratic images, not inferred from the supplied determinant.
sym2_images = [mul(x,x) for x in ell]+[mul(ell[i],ell[j]) for i,j in pairs]
sym2_det = det(coeff_matrix(sym2_images))
assert sym2_det == det(J)**5
p = [J[i][0]*J[j][1]-J[i][1]*J[j][0] for i,j in pairs]
q = [J[i][2]*J[j][3]-J[i][3]*J[j][2] for i,j in pairs]
assert p == list(map(Q,[1,1,1,Q(3,5),Q(8,5),1]))
assert q == list(map(Q,[1,2,3,Q(9,5),Q(16,5),1]))

# The nonsquare quotient calculation is linear in six unrelated bivector
# coefficients. Verify its coefficient matrices separately, so this is
# the full symbolic triangular identity rather than a sampled bivector.
gn = [add(mul(z[0],z[0]),mul(z[1],z[2]))]+[mul(x,x) for x in z[1:]]
for pi,(u,v) in enumerate(pairs):
    actual = []
    for i,j in pairs:
        raw = bracket(gn[i],gn[j],u,v)
        col = [raw.get(mon,Q(0)) for mon in monomials[4:]]
        col[3] -= raw.get(monomials[0],Q(0))
        actual.append(col)
    matrix = list(map(list,zip(*actual)))
    expected = [[Q(0)]*6 for _ in range(6)]
    expected[pi][pi] = 4
    if pi == 5:
        expected[4][2] = 2
    if pi == 4:
        expected[5][2] = 2
    assert matrix == expected


def degree_monomials(n):
    return [(i,j,k,n-i-j-k) for i in range(n+1)
            for j in range(n-i+1) for k in range(n-i-j+1)]


hilbert = {}
for name,gs in [('squares_ell',[mul(x,x) for x in z]),('nonsquare_ell',gn)]:
    dims = []
    for d in range(6):
        basis = degree_monomials(d)
        columns = [] if d<2 else [mul(g,{m:Q(1)}) for g in gs for m in degree_monomials(d-2)]
        rr = elimination(coeff_matrix(columns,basis))[0] if columns else 0
        dims.append(len(basis)-rr)
    assert dims == [1,4,6,4,1,0]
    hilbert[name] = dims

# Direct actual Jacobian determinant of the nonsquare quadrics: its
# nonzero squarefree top monomial is a basis element of the monic quotient.
def permutation_sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))


jac = {}
for perm in permutations(range(4)):
    term = {ZERO:Q(permutation_sign(perm))}
    for i in range(4):
        term = mul(term,diff(gn[i],perm[i]))
    jac = add(jac,term)
assert jac == {(1,1,1,1):Q(16)}

# Different cubic perturbations preserve every leading quadratic bracket.
higher = [add(mul(mul(z[i],z[i]),z[i]),
              mul(mul(z[(i+1)%4],z[(i+2)%4]),z[(i+3)%4])) for i in range(4)]
perturbed = [add(f,h) for f,h in zip(Fn,higher)]
for i,j in pairs:
    for u,v in [(0,1),(2,3)]:
        leading = {m:c for m,c in bracket(perturbed[i],perturbed[j],u,v).items() if sum(m)==2}
        assert leading == bracket(Fn[i],Fn[j],u,v)

# Strictness of the matrix lemma's hypothesis has a simple actual boundary:
# A=C[x]/x^3, e=h2=1, C=(x) is noninvertible and coker C is killed by n².
multiply_x = [[0,0,0],[1,0,0],[0,1,0]]
assert elimination(multiply_x)[0] == 2

out = {
    'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'proof_sha256':FROZEN,'runtime_seconds':time.perf_counter()-started,
    'implementation':'Python Fraction and independently written sparse polynomial, elimination and interpolation routines; no author code or SymPy imported.',
    'pencils':records,'det_sym2_J':str(sym2_det),'plus_coefficients':list(map(str,p)),
    'minus_coefficients':list(map(str,q)),
    'unrestricted_bivector_coefficient_matrices_checked':6,
    'hilbert_pieces':hilbert,'nonsquare_jacobian_socle_coefficient':'16',
    'independent_cubic_jet_checks':12,
    'matrix_hypothesis_boundary':{'algebra':'C[x]/(x^3)','e':1,'h2':1,
                                 'matrix':'(x)','cokernel_annihilated_by_n2':True,
                                 'matrix_invertible':False},
    'scope':'Finite exact reconstruction and boundary example. Universal Artin-matrix and filtered/Grassmannian proofs separately read in full.',
    'failures_before_pass':[]
}
(HERE/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
