"""Exact certificates for HD-G01--G06 and HD-WQ.

HODGE_DIVISION, 2026-11-21; GPT-6 Astra Pro, inherited session effort.
These computations verify the displayed algebra and constants, not the
geometric source, dominance, or cycle-class arguments.
Run with Python 3 and SymPy; prints JSON using decimal integer strings.
"""
import json
from math import factorial
import sympy as sp

i = sp.I
eigenvalues = []
for j in range(5):
    r = i**j * (-i)**(4-j)
    s = sp.expand((1+i)**j * (1-i)**(4-j))
    val = sp.simplify((1+r)*(4-s))
    assert val == (16 if j in (0,4) else 0)
    eigenvalues.append({'j':j, 'I':str(r), 'S':str(s), 'P':str(val)})

M = sp.Matrix([[1,-7],[-7,625]])
assert M.det() == 576
v1, v2 = sp.Matrix([625,7]), sp.Matrix([7,1])
assert (v1.T*M*v1)[0] == 600**2
assert (v2.T*M*v2)[0] == 24**2
assert sp.expand((2+i)**4) == -7+24*i

q, s, d = sp.symbols('q s d', real=True)
general = sp.Matrix([[1,s/2],[s/2,q*q]])
H = 4*q*q-s*s
adj4 = sp.Matrix([[4*q*q,-2*s],[-2*s,4]])
assert sp.simplify(adj4*general-H*sp.eye(2)) == sp.zeros(2)
assert sp.simplify((sp.Matrix([4*q*q,-2*s]).T*general*
                    sp.Matrix([4*q*q,-2*s]))[0]-4*q*q*H) == 0
assert sp.simplify((sp.Matrix([-2*s,4]).T*general*
                    sp.Matrix([-2*s,4]))[0]-4*H) == 0

U = sp.Matrix([[0,1],[1,0]])
I11 = sp.diag(1,-1)
S = sp.Matrix([[1,1],[1,-1]])
assert S.T*I11*S == 2*U
assert S.T*U*S == 2*I11

deg_w = 3**4*factorial(9)//factorial(5)
deg_t = 3**6*factorial(6)*4**2
assert (4*deg_w*deg_t) % 9 == 0
D = 4*deg_w*deg_t//9
D_all = 4*D
assert D == 914248581120
assert D_all == 3656994324480
data = {
    'normalization':'principal Prym xi; Theta_C|B = 2 xi; unnormalized intersection degrees',
    'projector_eigenvalue_check':eigenvalues,
    'gram_shape':[[1,-7],[-7,625]],
    'gram_shape_determinant':576,
    'dual_norm_squares_over_d':[600**2,24**2],
    'deg_W4_3Theta':deg_w,
    'deg_T0_3Theta':deg_t,
    'D_prym':D,
    'D_all_principal_gaussian_lattices':D_all,
    'N_coefficient':576*64,
    'degree_coefficient':8*(600+25*24)*8,
    'C4_prym_multiplier_coefficient':36864*D**2,
    'C4_prym_degree_coefficient':76800*D**2,
    'C4_all_principal_multiplier_coefficient':36864*D_all**2,
    'C4_all_principal_degree_coefficient':76800*D_all**2,
    'general_quadratic_gram_identity':'PASS',
    'even_odd_two_similitude':'PASS',
    'all_assertions':'PASS'
}
print(json.dumps(data,indent=2))
