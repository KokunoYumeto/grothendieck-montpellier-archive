"""Exact algebra supporting the characteristic-two Galois-closure proof.

This checks the displayed polynomial and matrix identities. The geometric
Galois-closure and ramification arguments are proved in the accompanying TeX;
they are not inferred from a finite sample.
"""
from pathlib import Path
import datetime
import json
import time
import sympy as sp

started = time.perf_counter()
A, B, C, z, a, b, c = sp.symbols('A B C z a b c')

def red(expr, variables=(A, B, C, z)):
    return sp.Poly(sp.expand(expr), *variables, modulus=2).as_expr()

def matrix_zero(mat):
    return all(red(v) == 0 for v in mat)

# Basis order: omega_0, omega_1, omega'_0, omega'_1.
sigma = sp.Matrix([[0, 0, 1, 1], [0, 0, 0, 1],
                   [1, 1, 0, 0], [0, 1, 0, 0]])
cartier = sp.Matrix([[0, 0, B+1, C+A+B+1],
                     [0, 0, 1, A+1],
                     [B, C, 0, 0], [1, A, 0, 0]])
invariants = sp.Matrix([[1, 0], [0, 1], [1, 1], [0, 1]])
H = sp.Matrix([[B+1, A+C], [1, A]])
assert matrix_zero(sigma*sigma-sp.eye(4))
assert matrix_zero(sigma*invariants-invariants)
assert matrix_zero(sigma*cartier-cartier*sigma)
assert matrix_zero(cartier*invariants-invariants*H)
assert red(H.det()**2-(A*A*B*B+C*C)) == 0

F = z**3+a*z**2+b*z+c
shifted = z**3+(a+1)*z**2+(b+1)*z+(c+a+b+1)
assert red(F.subs(z,z+1)-shifted,(a,b,c,z)) == 0
resultant = red(sp.resultant(F, sp.diff(F,z), z),(a,b,c))
assert resultant == red((a*b+c)**2,(a,b,c))
assert red(F.subs({a:A*A,b:B*B,c:C*C,z:B})-(A*A*B*B+C*C)) == 0

# Reconstruct each Cartier column from the odd coefficients of F and F(z+1).
Fs = red(F.subs({a:A*A,b:B*B,c:C*C}))
Gs = red(Fs.subs(z,z+1))
def polynomial_cartier(poly):
    ans = 0
    for mon, coefficient in sp.Poly(poly,z,A,B,C,modulus=2).terms():
        iz, ia, ib, ic = mon
        if iz % 2:
            assert ia % 2 == ib % 2 == ic % 2 == 0
            ans += coefficient*z**((iz-1)//2)*A**(ia//2)*B**(ib//2)*C**(ic//2)
    return red(ans)

computed = [polynomial_cartier(Fs), polynomial_cartier(z*Fs),
            polynomial_cartier(Gs), polynomial_cartier(z*Gs)]
expected = [B+z, C+A*z, B+1+z, C+A+B+1+(A+1)*z]
assert all(red(x-y)==0 for x,y in zip(computed,expected))

# Different degree eight with at least three tame index-three points.
possibilities=[]
for tame3 in range(3,5):
    for wild_points in range(0,5):
        if 2*tame3+2*wild_points==8:
            possibilities.append([tame3,wild_points])
assert possibilities == [[3,1],[4,0]]

result={
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-started,
 'status':'PASS',
 'scope':'Universal polynomial and matrix identities over F2; no geometric inference from finite tests.',
 'checks':[
  'Involution squares to one and fixes the two displayed invariant forms',
  'Cartier commutes with the involution and restricts to the displayed two-by-two H',
  'All four Cartier columns independently rebuilt from odd polynomial coefficients',
  'Squared determinant equals ab+c',
  'Cubic separability resultant equals (ab+c)^2',
  'Shift F(z+1) and critical-value evaluation agree',
  'Different-budget possibilities are (three tame, one wild) and (four tame, zero wild)'
 ],
 'root_removed_matrix':[['b+1','a+c'],['1','a']],
 'determinant_square':'ab+c',
 'separability_resultant':str(resultant),
 'different_cases':possibilities
}
out=Path(__file__).resolve().parents[1]/'outputs/genus_two_three_total_ramification_checks.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
