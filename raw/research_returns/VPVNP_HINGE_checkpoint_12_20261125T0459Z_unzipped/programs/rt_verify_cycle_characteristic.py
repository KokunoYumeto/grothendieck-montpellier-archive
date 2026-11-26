"""Reconstruct the four-cycle characteristic-two certificate independently."""
from itertools import product
from pathlib import Path
import hashlib
import json
import sympy as sp

W = Path(__file__).resolve().parents[1]
source = W / 'outputs/ex_cycle_sextic_results.json'
data = json.loads(source.read_text())
cfg = data['parameters']
t = sp.symbols('t0:16')
x0,x1,z0,z1,u = sp.symbols('x0 x1 z0 z1 u')

def index(a,b,c,d):
    return 8*a+4*b+2*c+d

def coefficient_matrix(values):
    mat = sp.Matrix(2,2,lambda b,d: sum(values[index(a,b,c,d)]*
                    (x0,x1)[a]*(z0,z1)[c] for a,c in product(range(2),repeat=2)))
    poly = sp.Poly(sp.expand(mat.det()),x0,x1,z0,z1)
    return sp.Matrix(3,3,lambda i,j: poly.coeff_monomial(
        x0**(2-i)*x1**i*z0**(2-j)*z1**j))

K = coefficient_matrix(t)
sextic = sp.Poly(sp.expand(K.det()),*t)
observed = {tuple(exps):int(c) for exps,c in sextic.terms()}
saved = {tuple(row['exponents']):row['coefficient'] for row in data['invariant_monomials']}
assert observed == saved
assert len(observed)==144 and set(observed.values())=={-1,1}
bell = [int(a==c and b==d) for a,b,c,d in product(range(2),repeat=4)]
assert coefficient_matrix(bell)==sp.diag(1,2,1)
witness=cfg['h_zero_sextic_nonzero_point']
H=sum(witness[i]*witness[15-i] for i in range(8))
assert H%2==0 and int(coefficient_matrix(witness).det())%2==1

# Rebuild all upper-unipotent coefficient constraints on an arbitrary
# torus-weight-zero quadratic, rather than reuse the saved matrix.
cc=sp.symbols('c0:8')
quadratic=sum(cc[i]*t[i]*t[15-i] for i in range(8))
rows=[]
for party in range(4):
    bit=1<<(3-party)
    transformed=[t[i]+u*t[i|bit] if not i&bit else t[i] for i in range(16)]
    diff=sp.Poly(sp.expand(sum(cc[i]*transformed[i]*transformed[15-i]
                            for i in range(8))-quadratic),u,*t)
    for coeff in diff.coeffs():
        row=[int(sp.expand(coeff).coeff(c))%2 for c in cc]
        if any(row): rows.append(row)

def rank2(matrix):
    a=[list(map(lambda x:int(x)%2,row)) for row in matrix]
    r=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        for i in range(len(a)):
            if i!=r and a[i][j]:a[i]=[x^y for x,y in zip(a[i],a[r])]
        r+=1
    return r

assert rank2(rows)==7 and all(sum(row)%2==0 for row in rows)

point=[[[sp.Matrix(matrix) for matrix in party][i] for i in range(2)]
       for party in cfg['jacobian_point']]
J=[]
for physical in product(range(2),repeat=4):
    row=[]
    for party in range(4):
        for p,i,j in product(range(2),repeat=3):
            if p!=physical[party]:row.append(0);continue
            mats=[point[v][physical[v]] for v in range(4)]
            E=sp.zeros(2);E[i,j]=1;mats[party]=E
            row.append(int(sp.trace(mats[0]*mats[1]*mats[2]*mats[3])))
    J.append(row)
assert J==data['jacobian']
minor=sp.Matrix(J).extract(cfg['jacobian_minor_rows'],cfg['jacobian_minor_columns'])
assert minor.tolist()==data['jacobian_minor'] and minor.det()==-1

s=sp.symbols('s')
I=sp.eye(2);E=sp.diag(0,1);X=sp.Matrix([[0,1],[1,0]])
maps=[[I,s*E],[I,X],[s*E,I],[I,X]]
entries=[]
for a,b,c,d in product(range(2),repeat=4):
    value=sp.expand(sp.trace(maps[0][a]*maps[1][b]*maps[2][c]*maps[3][d]))
    expected=2*int(a==0 and c==1 and b==d)+s*int(a==c and b==d)+s*s*int((a,b,c,d)==(1,0,0,0))
    assert sp.expand(value-expected)==0
    entries.append(str(value))

result={'status':'PASS','source_certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'sextic_monomials':144,'coefficient_values':[-1,1],
        'unipotent_constraint_rank_mod2':rank2(rows),'jacobian_minor_determinant':-1,
        'witness_H_mod2':H%2,'witness_I6_mod2':1,'integer_family_entries':entries,
        'scope':'All polynomial and integer certificates reconstructed. Structural exact-obstruction and irreducibility arguments are separately proof-checked.'}
(W/'outputs/rt_cycle_characteristic_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
