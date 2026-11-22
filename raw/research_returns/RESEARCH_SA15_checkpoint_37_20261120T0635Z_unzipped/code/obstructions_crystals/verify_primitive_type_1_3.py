"""Exact characteristic-two Euler and Lang identities for primitive type(1,3).

Standalone: no source files or author outputs are read.  All polynomial
identities are universal; Kummer/Artin--Schreier irreducibility, stability,
the geometry of divisors and nodal smoothing are proved in the written file.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as sp

started = time.perf_counter()
s0, s1, s2, t, u, a, b, w, c, omega = sp.symbols('s0 s1 s2 t u a b w c omega')
variables = (s0, s1, s2, t, u, a, b, w, c, omega)
checks = []


def check(name, expression):
    numerator, denominator = sp.together(expression).as_numer_denom()
    assert denominator != 0
    assert sp.Poly(numerator, *variables, modulus=2).is_zero, (name, expression)
    checks.append(name)


def matrix_check(name, expression):
    for i in range(expression.rows):
        for j in range(expression.cols):
            check(f'{name}[{i},{j}]', expression[i, j])


M = sp.Matrix([[0, s2, s1], [s2, 0, s0], [s1, s0, 0]])
matrix_check('alternating right kernel', M * sp.Matrix([s0, s1, s2]))
chart_M = M.subs({s0: 1, s1: t, s2: u})
source_frame = sp.Matrix([[t**2, u**2], [1, 0], [0, 1]])
target_frame = sp.Matrix([[t, u], [1, 0], [0, 1]])
Phi = sp.Matrix([[u*t**2, 1+u**3], [1+t**3, t*u**2]])
matrix_check('actual Euler frame multiplication', chart_M.T * source_frame - target_frame * Phi)
F = 1+t**3+u**3
check('Euler determinant equals Fermat', Phi.det()-F)
column = sp.Matrix([t**2, u**2])
row = sp.Matrix([[u, t]])
J = sp.Matrix([[0, 1], [1, 0]])
matrix_check('wall rank-one factorization with exact remainder', Phi-column*row-F*J)
rho = (row * column.applyfunc(lambda x: x**2))[0]
check('stable rank-one scalar', rho-t*u*(F+1))
fermat_ideal = sp.groebner([F], t, u, modulus=2)
iterate_difference = Phi * Phi.applyfunc(lambda x: x**2) - t*u*column*row.applyfunc(lambda x: x**2)
for i in range(2):
    for j in range(2):
        remainder = fermat_ideal.reduce(sp.expand(iterate_difference[i, j]))[1]
        check(f'actual second iterate on Fermat[{i},{j}]', remainder)

# Constant fibre scaling x=c^-1*xnew removes the nonzero scalar c.
new_vector = sp.Matrix([a, b])
old_vector = new_vector / c
old_equation = old_vector + c * Phi * old_vector.applyfunc(lambda x: x**2)
normalized_equation = new_vector + Phi * new_vector.applyfunc(lambda x: x**2)
matrix_check('constant scalar normalization', c*old_equation-normalized_equation)

Phi_three = sp.Matrix([[0, 1+u**3], [1, 0]])
matrix_check('Kummer slice matrix', Phi.subs(t, 0)-Phi_three)
check('Kummer elimination', a+(1+u**3)*(a**2)**2-a*(1+(1+u**3)*a**3))
g = 1+u**3
check('simple Kummer zeros identity', g+u*sp.diff(g, u)-1)

Phi_two = sp.Matrix([[t**2, 0], [1+t**3, t]])
matrix_check('Artin--Schreier slice matrix', Phi.subs(u, 1)-Phi_two)
regular = sp.Matrix([0, 1/t])
matrix_check('rational nonzero fixed vector', regular+Phi_two*regular.applyfunc(lambda x: x**2))
pair = sp.Matrix([1/t**2, w/t])
pair_equations = pair+Phi_two*pair.applyfunc(lambda x: x**2)
check('other two first coordinate fixed', pair_equations[0])
check('other two AS equation', t*pair_equations[1]-(w**2+w+t**(-3)+1))

# The same actual level-three clock gives the target Frobenius weights.
omega_ideal = sp.groebner([omega**2+omega+1], omega, modulus=2)
for i in range(3):
    for j in range(i+1, 3):
        k = 3-i-j
        remainder = omega_ideal.reduce(omega**(i+j)+omega**(2*k))[1]
        check(f'level-three Cartier clock weight[{i},{j}]', remainder)

record = {
    'status': 'PASS',
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'runtime_seconds': time.perf_counter()-started,
    'check_count': len(checks),
    'checks': checks,
    'Euler_matrix_without_nonzero_scalar': [['u*t^2', '1+u^3'], ['1+t^3', 't*u^2']],
    'determinant': '1+t^3+u^3',
    'wall_factorization': '(t^2,u^2)^transpose * (u,t)',
    'wall_second_iterate_scalar': 't*u',
    'Kummer_equation': 'a^3=(1+u^3)^(-1)',
    'Artin_Schreier_equation': 'w^2+w=t^(-3)+1',
    'scope': 'Universal matrix, relative Euler-frame, scalar-normalization and Lang-slice identities in characteristic two. No numerical sampling or proof of geometric stability/smoothness is substituted for the complete written argument.'
}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
