from datetime import datetime, timezone
from pathlib import Path
import json
import time
import sympy as s

started = datetime.now(timezone.utc).isoformat()
tick = time.perf_counter()
names = ['u1', 'u2', 'v1', 'v2', 'w1', 'w2', 'e']
q = s.zeros(7)
for i in (0, 2, 4):
    q[i, i+1] = q[i+1, i] = 1
q[6, 6] = -6
mons = [(i, j) for i in range(7) for j in range(i, 7)]
index = {m: i for i, m in enumerate(mons)}
gram = s.Matrix(28, 28, lambda a, b: 3*(q[mons[a][0], mons[a][1]]*q[mons[b][0], mons[b][1]] + q[mons[a][0], mons[b][0]]*q[mons[a][1], mons[b][1]] + q[mons[a][0], mons[b][1]]*q[mons[a][1], mons[b][0]]))

def mon(i,j):
    r = s.zeros(28,1)
    r[index[tuple(sorted((i,j)))]] = 1
    return r

columns=[]
column_names=[]
for i,j in mons:
    if (i == j and i < 6) or (i,j) == (0,1):
        continue
    columns.append(mon(i,j))
    column_names.append(names[i]+'*'+names[j])
for i in range(6):
    columns.append(mon(i,i)/2-mon(i,6)/6)
    column_names.append('B_'+names[i])
Q=mon(0,1)+mon(2,3)+mon(4,5)
columns.append(Q/2)
column_names.append('Q/2')
change=s.Matrix.hstack(*columns)
new_gram=change.T*gram*change
assert all(x.q == 1 for x in new_gram)
assert gram.det() == 2**14*3**38
assert abs(change.det()) == s.Rational(1,2**7)
assert new_gram.det() == 3**38

a,b,c,d=s.symbols('a b c d')
ell2=mon(0,0)+4*mon(0,1)+4*mon(1,1)
elle=mon(0,6)+2*mon(1,6)
hodge=a*ell2+b*elle+c*mon(6,6)+d*Q
coords=change.inv()*hodge
coordinate_data={column_names[i]:str(s.expand(x)) for i,x in enumerate(coords) if x != 0}
assert coords[column_names.index('B_u1')] == 2*a
assert coords[column_names.index('e*e')] == c
assert coords[column_names.index('Q/2')] == 8*a+2*d
scalar=s.expand((mon(2,3).T*gram*hodge)[0])
assert scalar == 12*a-18*c+12*d
assert s.expand((mon(4,5).T*gram*hodge)[0]-scalar) == 0
assert (mon(2,3).T*gram*(Q/6))[0] == 2
output={
 'started_utc': started,
 'finished_utc': datetime.now(timezone.utc).isoformat(),
 'seconds': time.perf_counter()-tick,
 'q_determinant':int(q.det()),
 'symmetric_square_rank':28,
 'symmetric_square_gram_determinant':str(gram.det()),
 'symmetric_square_gram_factorization':{'2':14,'3':38},
 'change_determinant':str(change.det()),
 'enlarged_gram_integral':True,
 'enlarged_gram_determinant':str(new_gram.det()),
 'enlarged_gram_factorization':{'3':38},
 'hodge_coordinates_in_enlarged_basis':coordinate_data,
 'transcendental_scalar':str(scalar),
 'even_expression':'6*(2*a) - 18*c + 6*(2*d)',
 'Yp_scalar':2,
 'scope':'Exact rational lattice and symbolic coefficient certificate. Published integrality of B_y and Q/6 is an external geometric input; this program does not prove it. No general Chow group or main-gate computation.'
}
target=Path(__file__).resolve().parents[1]/'output/kummer_incidence_parity.json'
target.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
