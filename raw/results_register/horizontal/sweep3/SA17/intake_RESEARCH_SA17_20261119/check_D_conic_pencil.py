"""Intake check (Claude Opus 5.5 at effort max, 19 Nov 2026) of RESEARCH_SA17 D:reducible-counterexample, conic case.
Pencil t*x(y-z) + y(x-z) of conics through [1,0,0],[0,1,0],[0,0,1],[1,1,1]: the singular members are the
zeros of det of the symmetric matrix (homogeneous in (t:1)); with degree 2 in t, t = infinity is also singular."""
from fractions import Fraction as Fr
def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1]) - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
def mat(t):
    # q = t*(xy - xz) + (xy - yz); symmetric matrix with off-diagonals = half coefficients
    xy = Fr(t + 1, 2); xz = Fr(-t, 2); yz = Fr(-1, 2)
    return [[0, xy, xz], [xy, 0, yz], [xz, yz, 0]]
vals = {t: det3(mat(t)) for t in range(-3, 5)}
print(vals)
print('equals t(t+1)/4 at all sample points:', all(v == Fr(t*(t+1), 4) for t, v in vals.items()),
      '(the run writes t(t-1)/4: same pencil up to the sign of one generator; roots 0, -1 here)')
print('singular members: t=0, t=-1, t=infinity (degree 2 < 3) -> 3 reducible conics;',
      'rho(Bl_4 P^2)=5, uncorrected rho(X)+n-2 = 1+4-2 = 3, corrected 3-3 = 0 = MW rank of a genus-0 fibration')
