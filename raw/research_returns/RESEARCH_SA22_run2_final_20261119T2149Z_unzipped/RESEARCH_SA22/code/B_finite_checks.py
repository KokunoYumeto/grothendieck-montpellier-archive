#!/usr/bin/env python3
"""Exact finite symbolic checks; these do not certify the Hodge-theoretic inputs."""
import json
import time
from pathlib import Path
import sympy as sp
from itertools import combinations
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

start = time.perf_counter()
Q = sp.diag(1, 0)
assert Q.rank() == 1
assert Q.nullspace() == [sp.Matrix([0, 1])]
assert (sp.Matrix([[1, 0]]) * Q * sp.Matrix([1, 0]))[0] == 1

# Chow-ring calculation in Z[a,b]/(a^2,b^2).
a, b = sp.symbols("a b")
gb = sp.groebner([a*a, b*b], a, b)
remainder = gb.reduce((a+b)**2)[1]
assert remainder == 2*a*b

# The Jacobian discriminant of E: y^2=x^3-x is 64, so nonsingular.
discriminant = -16*(4*(-1)**3+27*0**2)
assert discriminant == 64

# Albanese image of the exterior product, as a symbolic group sum.
P, Qpoint = sp.symbols("P Q")
alb1 = P-P-0+0
alb2 = Qpoint-0-Qpoint+0
assert alb1 == alb2 == 0

n = 2
exponents_mod_n = sorted({j % n for j in range(-8, 9)})
assert exponents_mod_n == [0,1]
assert (1 % n) != 0

x, t = sp.symbols("x t")
hasse_coefficient = sp.Poly((x**3+t*x+1)**2, x).coeff_monomial(x**4)
family_discriminant = sp.expand(-16*(4*t**3+27))
assert hasse_coefficient == 2*t
assert int(family_discriminant.subs(t,0)) % 5 == 3

def elliptic_point_count(p, aa, bb):
    assert (-16*(4*aa**3+27*bb**2)) % p != 0
    points = [(xx,yy) for xx in range(p) for yy in range(p)
              if (yy*yy-xx**3-aa*xx-bb) % p == 0]
    return {"p": p, "a": aa, "b": bb, "affine_points": points,
            "count_including_infinity": len(points)+1,
            "Frobenius_trace": p-len(points)}

ordinary = elliptic_point_count(5,-1,0)
supersingular = elliptic_point_count(5,0,1)
assert ordinary["count_including_infinity"] == 8
assert supersingular["count_including_infinity"] == 6

# The odd one-dimensional object's Koszul switch is -1, whereas the
# switch on a one-dimensional ordinary vector space is +1 in characteristic 0.
assert sp.Matrix([[-1]]) != sp.Matrix([[1]])

# Finite Galois descent datum on the doubled affine line.  The action on
# coefficients in basis (1,i) is diag(1,-1); t is fixed and the charts swap.
conj = sp.diag(1, -1)
chart_perm = lambda g, u: (u+g) % 2
cocycle_checks = []
for g in range(2):
    for h in range(2):
        product = (g+h) % 2
        assert conj**g * conj**h == conj**product
        assert all(chart_perm(g,chart_perm(h,u)) == chart_perm(product,u)
                   for u in range(2))
        assert (-1)**g * (-1)**h == (-1)**product
        cocycle_checks.append({"g": g, "h": h, "product": product,
                               "coefficient_action": "passed",
                               "chart_action": "passed", "t_fixed": True})
assert conj * conj == sp.eye(2)

# Translation by the rational 2-torsion point T=(0,0) on E:y^2=x^3-x.
# The displayed chart excludes x=0; the missing points O and T are exchanged.
yvar, svar0 = sp.symbols("y s0")
elliptic_equation = yvar**2-x**3+x
translated_equation = elliptic_equation.subs(
    {x:-1/x, yvar:yvar/x**2}, simultaneous=True)
assert sp.cancel(translated_equation-elliptic_equation/x**4) == 0
assert sp.cancel(-1/(-1/x)-x) == 0
assert sp.cancel((yvar/x**2)/(-1/x)**2-yvar) == 0
fixed_ideal = sp.groebner(
    [elliptic_equation, x*x+1, yvar*(x*x-1)], x,yvar, domain=sp.QQ)
assert list(fixed_ideal) == [1]
assert (-svar0)**2 == svar0**2
elliptic_double_fibre_checks = {
    "translation": ["-1/x", "y/x^2"],
    "equation_transforms_by": "1/x^4", "involution": True,
    "fixed_locus_on_x_nonzero_groebner_basis": [str(f) for f in fixed_ideal],
    "omitted_points": "O and T=(0,0) are exchanged by group translation",
    "base_invariant": "t=s0^2", "special_fibre_multiplicity": 2,
}

# Explicit non-torsion henselian-rigidity obstruction.  These are exact
# polynomial identities used in the full Cech/valuation proof, not a numerical
# claim to compute the infinite-dimensional cohomology group.
w_h, alpha_h, r_h, s_h = sp.symbols('w_h alpha_h r_h s_h')
assert sp.expand((1+2*w_h)**2-1-4*(w_h*w_h+w_h)) == 0
assert list(sp.groebner([x,x-1],x,domain=sp.QQ)) == [1]
q_h = x*(x-1)+4*t
assert sp.expand(q_h.subs(t,alpha_h*(1-alpha_h)/4)
                 -(x-alpha_h)*(x-(1-alpha_h))) == 0
assert sp.expand(alpha_h*(alpha_h-1)+4*(alpha_h*(1-alpha_h)/4)) == 0
nilp_h = sp.Matrix([[0,-2],[0,0]])
assert nilp_h**2 == sp.zeros(2)
assert (sp.eye(2)+r_h*nilp_h)*(sp.eye(2)+s_h*nilp_h) == sp.eye(2)+(r_h+s_h)*nilp_h
henselian_nontorsion_checks = {
    'cover_ideal': '1=(x)-(x-1)',
    'quadratic_identity': '(1+2w)^2=1+4(w^2+w)',
    'branch_factorization': 'x(x-1)+4t=(x-alpha)(x-(1-alpha)), alpha(1-alpha)=4t',
    'branch_denominator': 'alpha(alpha-1)=-4t != 0',
    'involution_product': [[1,-2],[0,1]],
    'additive_power_identity': '(I+rN)(I+sN)=I+(r+s)N, N^2=0',
}

# Rond's explicit approximate zeros.  These check the finite instances only;
# the square-distance obstruction and all-m proof are in the paper.
svar, tvar = sp.symbols("s t")
rond_checks = []
for mm in range(5, 13):
    pp = mm-2
    uu = sum(sp.binomial(sp.Rational(1,2), jj) * svar**(2*mm-2-2*jj)
             * tvar**(pp*jj) for jj in range(mm))
    vv, ww = svar**(2*mm-3), svar**2+tvar**pp
    error_poly = sp.Poly(sp.expand(uu**2-vv**2*ww), svar,tvar)
    order = min(sum(monom) for monom,coeff in error_poly.terms() if coeff)
    assert order == mm*mm-4
    assert min(sum(monom) for monom,coeff in sp.Poly(uu,svar,tvar).terms()) == 2*mm-2
    rond_checks.append({"m":mm, "error_order":order,
                        "excluded_exact_congruence_exponent":2*mm-2,
                        "nonzero_error_terms":len(error_poly.terms())})

# A completely specified finite-polyhedral link for the local-Hurewicz
# counterexample. The five edges incident with vertex 1 form a spanning tree.
# Chord coordinates therefore identify the integral cycle lattice with Z^10.
moore_faces = [(1,2,3),(1,2,4),(1,3,5),(1,4,6),(1,5,6),
               (2,3,6),(2,4,5),(2,5,6),(3,4,5),(3,4,6)]
moore_edges = sorted({e for face in moore_faces for e in combinations(face,2)})
moore_d1 = sp.zeros(6,len(moore_edges))
for j,(a0,b0) in enumerate(moore_edges):
    moore_d1[a0-1,j],moore_d1[b0-1,j] = -1,1
moore_d2 = sp.zeros(len(moore_edges),len(moore_faces))
for j,face in enumerate(moore_faces):
    for k in range(3):
        edge = tuple(v0 for l,v0 in enumerate(face) if l != k)
        moore_d2[moore_edges.index(edge),j] = (-1)**k
assert moore_d1*moore_d2 == sp.zeros(6,10)
moore_chords = [e for e in moore_edges if e[0] != 1]
moore_M = moore_d2[[moore_edges.index(e) for e in moore_chords],:]
moore_smith = smith_normal_form(moore_M,domain=ZZ)
assert moore_d1.rank() == 5 and moore_d2.rank() == 10
assert moore_M.det() == -2
assert [abs(moore_smith[i,i]) for i in range(10)] == [1]*9+[2]
moore_link_checks = {
    'base_complex_facets':moore_faces, 'vertices':list(range(1,7)),
    'edges':moore_edges, 'd1':[[int(v) for v in row] for row in moore_d1.tolist()], 'd2':[[int(v) for v in row] for row in moore_d2.tolist()],
    'spanning_tree':[[1,i] for i in range(2,7)],
    'cycle_lattice_chords':moore_chords,
    'boundary_in_cycle_coordinates':[[int(v) for v in row] for row in moore_M.tolist()],
    'determinant':int(moore_M.det()),
    'smith_diagonal':[int(moore_smith[i,i]) for i in range(10)],
    'base_reduced_homology':{'H1':'Z/2','other':'0'},
    'suspension_vertices':[7,8],
    'suspension_facets':[list(f)+( [v0] ) for f in moore_faces for v0 in [7,8]],
    'suspension_reduced_homology':{'H2':'Z/2','other':'0'},
    'local_cone_cohomology':{'H0_H1_H2_H3':'0','H4':'Z/2'},
    'topological_proof_inputs':'van Kampen, suspension Mayer-Vietoris, integral UCT, Hurewicz; checked in the text, not inferred from finite algebra',
}

result = {
    "checks": 14,
    "local_Hurewicz_finite_polyhedron":moore_link_checks,
    "henselian_nontorsion_Cech_obstruction": henselian_nontorsion_checks,
    "elliptic_quotient_double_fibre": elliptic_double_fibre_checks,
    "Rond_nonlinear_Artin_approximate_family": rond_checks,
    "Galois_doubled_origin_C2_cocycle": cocycle_checks,
    "elliptic_family_characteristic5": {
        "Hasse_coefficient": str(hasse_coefficient),
        "discriminant": str(family_discriminant),
        "special_discriminant_mod5": 3,
        "ordinary_example": ordinary,
        "supersingular_example": supersingular,
    },
    "super_symmetry_vs_ordinary_symmetry": [-1,1],
    "Kummer_units_exponent_quotient_n2": exponents_mod_n,
    "quadratic_form": {"matrix": [[1,0],[0,0]], "rank": 1,
                       "radical_basis": [[0,1]], "quotient_matrix": [[1]]},
    "square_mod_a2_b2": str(remainder),
    "elliptic_discriminant": discriminant,
    "albanese_image": [0,0],
    "scope": "Exact rational/integer finite algebra; Mumford nonvanishing is proved in the paper, not computed.",
    "seconds": round(time.perf_counter()-start, 6),
}
output = json.dumps(result, indent=2)
root = Path(__file__).resolve().parents[1]
(root / "logs" / "B_finite_checks.json").write_text(output + "\n")
print(output)
