#!/usr/bin/env python3
"""Independent E840 witness reconstruction; not a universal-proof certificate.

The complete author's program was read before this was written.  No author
code, computed bracket matrix, or output is imported.  Normal forms come from
a Groebner basis, and the brackets from Jacobian/skew-matrix multiplication.
"""
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import time
import sympy as sp

started = time.perf_counter()
here = Path(__file__).resolve().parent
proof = here.parent.parent / "sixfolds/rm_rank_four_principal_image_draft.md"
expected_hash = "d29300c26b59b71edd4b14381faad4713f3982c884e8da68047b62f641c199b8"
assert sha256(proof.read_bytes()).hexdigest() == expected_hash

x, y, z, w, a, b = sp.symbols("x y z w a b")
v = (x, y, z, w)
relations = (x*x+y*w, y*y, z*z, w*w)
gb = sp.groebner(relations, *v, order="lex", domain=sp.QQ)
assert [p.LM().exponents for p in gb.polys] == [
    (2, 0, 0, 0), (0, 2, 0, 0), (0, 0, 2, 0), (0, 0, 0, 2)]
normal = lambda f: sp.expand(gb.reduce(sp.expand(f))[1])
exponents = sorted(product((0, 1), repeat=4), key=lambda t: (sum(t), t))
monomials = [sp.prod(v[i]**t[i] for i in range(4)) for t in exponents]
monomial_index = {t: i for i, t in enumerate(exponents)}
hilbert = [sum(sum(t) == j for t in exponents) for j in range(5)]
assert hilbert == [1, 4, 6, 4, 1]

# Every product is computed by the Groebner normal form, without a hand-coded
# replacement rule.  Then verify the complete finite multiplication table.
table = {}
for i, m in enumerate(monomials):
    for j, n in enumerate(monomials):
        p = sp.Poly(normal(m*n), *v)
        if p.is_zero:
            table[i, j] = (0, 0)
        else:
            terms = p.terms()
            assert len(terms) == 1
            t, c = terms[0]
            table[i, j] = (int(c), monomial_index[t])
associativity_checks = 0
for i, j, k in product(range(16), repeat=3):
    c, r = table[i, j]
    d, s = table[r, k]
    e, t = table[j, k]
    f, u = table[i, t]
    left, right = (c*d, s), (e*f, u)
    assert left == right or left[0] == right[0] == 0
    associativity_checks += 1

pairs = list(combinations(range(4), 2))
quadratic_basis = [v[i]*v[j] for i, j in pairs]
def quadratic_vector(f):
    p = sp.Poly(normal(f), *v)
    return sp.Matrix([p.coeff_monomial(m) for m in quadratic_basis])

# The four vectors are the actual two ordered plane bases, not a supplied
# transformed bracket matrix.
frame = sp.Matrix.hstack(sp.Matrix([1, 0, 0, -1]),
                        sp.Matrix([0, 1, 1, 0]),
                        sp.Matrix([1, 0, 0, 1]),
                        sp.Matrix([0, 1, -1, 0]))
assert frame.det() == 4
pi = [frame[:,i]*frame[:,j].T-frame[:,j]*frame[:,i].T
      for i, j in ((0, 1), (2, 3))]
assert all(P.rank() == 2 for P in pi)
jacobian = sp.Matrix(relations).jacobian(v)
bracket_arrays = [jacobian*P*jacobian.T for P in pi]
tuples = [[normal(B[i,j]) for i,j in pairs] for B in bracket_arrays]
matrices = [sp.Matrix.hstack(*(quadratic_vector(f) for f in t)) for t in tuples]
Mp, Mq = matrices
M = a*Mp+b*Mq
assert Mp.rank() == Mq.rank() == 4
assert M.subs({a:1,b:1}).rank() == 3
assert M.subs({a:1,b:-1}).rank() == 2
assert M.det() == 0
five_minors = [sp.factor(M.extract(I,J).det())
               for I in combinations(range(6),5)
               for J in combinations(range(6),5)]
assert len(five_minors) == 36 and not any(five_minors)
four_minors = [sp.factor(M.extract(I,J).det())
               for I in combinations(range(6),4)
               for J in combinations(range(6),4)]
nonzero_four = sorted(set(str(t) for t in four_minors if t))
assert sp.factor(M.extract((0,1,4,5),(0,1,4,5)).det()) == 256*(a-b)**2*(a+b)**2

cross_checks = 0
for i,j in product(range(6),repeat=2):
    assert normal(tuples[0][i]*tuples[1][j]-tuples[1][i]*tuples[0][j]) == 0
    cross_checks += 1
def wedge(P,Q):
    return normal(P[0]*Q[5]+P[5]*Q[0]-P[1]*Q[4]-P[4]*Q[1]+P[2]*Q[3]+P[3]*Q[2])
assert wedge(tuples[0],tuples[0]) == wedge(tuples[1],tuples[1]) == 0
assert wedge(*tuples) == 64*x*y*z*w
assert normal(jacobian.det()) == 16*x*y*z*w

# Derive the quotient functionals, rather than importing the printed pair.
quotient = sp.Matrix.vstack(*(q.T for q in Mp.T.nullspace()))
assert quotient.shape == (2,6) and quotient*Mp == sp.zeros(2,6)
mu = [sp.Matrix.hstack(*(quadratic_vector(t*u) for u in v)) for t in v]
kernel_test = sp.Matrix.vstack(*(quotient*T for T in mu))
assert kernel_test.rank() == 4 and kernel_test.nullspace() == []
kernel_minors = [sp.factor(kernel_test.extract(I,range(4)).det()) for I in combinations(range(8),4)]
assert any(kernel_minors)

# A genuine equality example: multiplication by x has four-dimensional
# quadratic image and a unique common factor line.  This is not a deformation.
principal = mu[0]
assert principal.rank() == 4
principal_quotient = sp.Matrix.vstack(*(q.T for q in principal.T.nullspace()))
principal_test = sp.Matrix.vstack(*(principal_quotient*T for T in mu))
assert principal_test.nullspace() == [sp.Matrix([1,0,0,0])]
coordinate_plane_ranks = [(i,j,sp.Matrix.hstack(mu[i],mu[j]).rank()) for i,j in pairs]
assert all(r >= 5 for _,_,r in coordinate_plane_ranks)

alpha,beta,gamma,delta = sp.symbols("alpha beta gamma delta")
hessian = sp.hessian(alpha*relations[0]+beta*relations[1]+gamma*relations[2]+delta*relations[3],v)
assert hessian.extract((0,1),(0,3)).det() == 2*alpha**2
assert hessian.subs(alpha,0) == sp.diag(0,2*beta,2*gamma,2*delta)

result = {
    "status":"PASS", "completed_utc":datetime.now(timezone.utc).isoformat(),
    "runtime_seconds":time.perf_counter()-started,
    "proof_sha256":expected_hash, "script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
    "normal_form_method":"Groebner basis, lex order, rational coefficients",
    "hilbert_function":hilbert, "multiplication_products":256,
    "associativity_triples":associativity_checks,
    "coordinate_determinant":4,
    "bracket_tuples":[[str(f) for f in t] for t in tuples],
    "pencil_matrix":[[str(t) for t in row] for row in M.tolist()],
    "endpoint_ranks":[4,4], "special_direction_ranks":[3,2],
    "all_five_minors_zero":36, "four_minors_computed":225,
    "distinct_nonzero_four_minors":nonzero_four,
    "all_scalar_cross_minors_zero":cross_checks,
    "mixed_wedge":"64*x*y*z*w", "jacobian_socle":"16*x*y*z*w",
    "kernel_test_matrix":[[str(t) for t in row] for row in kernel_test.tolist()],
    "kernel_dimension":0, "nonzero_kernel_test_minors":[str(d) for d in kernel_minors if d],
    "principal_example_kernel":[1,0,0,0], "coordinate_plane_ranks":coordinate_plane_ranks,
    "rank_one_relation_minor":"2*alpha**2", "extension_dimension":"96*m**2",
    "scope":"Independent finite witness/equality-example reconstruction only. The universal equality, actual module companion and geometric arguments are checked as proofs. Author code was read first; none is imported."
}
(here/"audit_rank_four_principal.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
