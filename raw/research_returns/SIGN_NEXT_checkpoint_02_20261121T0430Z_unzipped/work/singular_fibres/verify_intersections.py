#!/usr/bin/env python3
"""Exact arithmetic certificate for SN-44-02 and SN-44-04/05.

This checks algebraic identities, not the geometric hypotheses of the proof.
No floating point arithmetic or heuristic numerical test is used.
"""
import json
import sympy as s

a, b, t, h = s.symbols("a b t h")
u, v, up, vp = s.symbols("u v up vp")


def reduce_ambient(expr):
    """CH*(P^2 x P^2 x P^1)=Z[a,b,t]/(a^3,b^3,t^2)."""
    p = s.Poly(s.expand(expr), a, b, t)
    return s.expand(sum(c*a**i*b**j*t**k for (i, j, k), c in p.terms()
                        if i <= 2 and j <= 2 and k <= 1))


def degree_M(expr):
    """[M]=a+b+t in the five-dimensional ambient product."""
    return int(s.Poly(reduce_ambient(expr*(a+b+t)), a, b, t)
               .coeff_monomial(a**2*b**2*t))


Z = a*a-a*b+b*b
F_c2 = b*b-(a+t)*b+(a+t)**2
regular_section_identity = s.expand(F_c2-(Z+t*(2*a-b)))
assert reduce_ambient(regular_section_identity) == 0
assert degree_M(Z**2) == 3
assert degree_M((t*(b-2*a))**2) == 0
assert reduce_ambient((a+b)*Z) == 0

# Normal bundle N_{D_i/M}=Omega^1_{P^2}(1) has c(N)=1/(1+b).
c2_normal = s.series(1/(1+h), h, 0, 3).removeO().coeff(h, 2)
assert c2_normal == 1

# For D_i, a=t=0, and b is its plane hyperplane class.
restriction_Z_D = s.expand(Z.subs({a: 0, t: 0})).coeff(b, 2)
assert restriction_Z_D == 1
G = s.eye(3)
avector = s.Matrix([restriction_Z_D]*3)
node_terms = [int(avector[i]**2/G[i, i]) for i in range(3)]
assert node_terms == [1, 1, 1]
assert int((avector.T*G.inv()*avector)[0]) == degree_M(Z**2)

# Independently check parity and exceptional-divisor signs for arbitrary m.
node_form_checks = []
for m in range(1, 10):
    self_ruling = (1+(-1)**(m-1))//2
    cross_ruling = (1-(-1)**(m-1))//2
    Q_pairing = self_ruling*(u*up+v*vp)+cross_ruling*(u*vp+v*up)
    computed = s.expand((u+v)*(up+vp)-2*Q_pairing)
    target = (-1)**m*(u-v)*(up-vp)
    assert s.expand(computed-target) == 0
    # p^*D = Dbar + c E^m; E^(2m)=-1; Dbar E^m=(-1)^(m-1)(u+v).
    coeff = (-1)**(m+1)
    exceptional_total = 2*coeff*(-1)**(m-1)-coeff**2
    assert exceptional_total == 1
    node_form_checks.append({"m": m, "ruling_self": self_ruling,
                             "ruling_cross": cross_ruling,
                             "norm_of_normalized_defect": (-1)**m,
                             "exceptional_correction": exceptional_total})

# Check the three ordinary quadratic singularities independently.
x1, x2, y1, y2 = s.symbols("x1 x2 y1 y2")
hessians = []
for i in range(3):
    others = [j for j in range(3) if j != i]
    c, d = (j-i for j in others)
    Q = c*x1*y1+d*x2*y2
    determinant = int(s.det(s.hessian(Q, (x1, x2, y1, y2))))
    assert determinant == c*c*d*d and determinant != 0
    hessians.append({"parameter": [-i, 1], "coefficients": [c, d],
                     "Hessian_determinant": determinant})

# Full middle intersection matrix in a convenient seven-element basis.
# D_2 is reconstructed using D_0+D_1+D_2=Z+t(2a-b).
ambient_basis = [a*a, a*b, b*b, a*t, b*t]
G7 = s.zeros(7)
for i, x in enumerate(ambient_basis):
    for j, y in enumerate(ambient_basis):
        G7[i,j] = degree_M(x*y)
    d_pair = s.expand(x.subs({a:0,t:0})).coeff(b,2)
    G7[i,5] = G7[5,i] = d_pair
    G7[i,6] = G7[6,i] = d_pair
G7[5,5] = G7[6,6] = 1
assert G7.det() != 0
zvec = s.Matrix([1,-1,1,0,0,0,0])
d0 = s.Matrix([0,0,0,0,0,1,0])
d1 = s.Matrix([0,0,0,0,0,0,1])
d2 = s.Matrix([1,-1,1,2,-1,-1,-1])
Ds = s.Matrix.hstack(d0,d1,d2)
assert Ds.T*G7*Ds == G
assert Ds.T*G7*zvec == avector
residual = zvec-Ds*avector
assert residual == s.Matrix([0,0,0,-2,1,0,0])
assert (residual.T*G7*residual)[0] == 0
assert Ds.T*G7*residual == s.zeros(3,1)

print(json.dumps({
    "status":"all exact identities passed",
    "scope":"arithmetic certificate, not a formalization of geometric proofs",
    "Z_square":degree_M(Z**2),
    "normal_bundle_c2":int(c2_normal),
    "node_correction_terms":node_terms,
    "corrected_square":degree_M(Z**2)-sum(node_terms),
    "quadric_parity_checks":node_form_checks,
    "nodal_hessians":hessians,
    "middle_Gram_basis":["a^2","ab","b^2","at","bt","D_0","D_1"],
    "middle_Gram_matrix":[[int(x) for x in G7.row(i)] for i in range(7)],
    "middle_Gram_determinant":int(G7.det()),
    "D_2_coordinates":[int(x) for x in d2],
    "corrected_extension_coordinates":[int(x) for x in residual]
}, indent=2))
