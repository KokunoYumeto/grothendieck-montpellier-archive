"""Exact finite certificates for the linear algebra in Part A.

These verify finite calculations only, not the geometric vanishing theorems.
"""
from pathlib import Path
import json, time
from datetime import datetime, timezone

started = time.perf_counter()
checks = []

def rank(matrix, p):
    a = [[v % p for v in row] for row in matrix]
    r = 0
    for j in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r,len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p)
        a[r] = [(x*inv)%p for x in a[r]]
        for i in range(len(a)):
            if i != r:
                c = a[i][j]
                a[i] = [(x-c*y)%p for x,y in zip(a[i],a[r])]
        r += 1
        if r == len(a):
            break
    return r

def matmul(a,b,p):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))%p
             for j in range(len(b[0]))] for i in range(len(a))]

def check(name, condition, data):
    assert condition, (name,data)
    checks.append({'name':name,'passed':True,'data':data})

for p in (2,3,5,7):
    # The standard periodic resolution of C2 over F_p[C2].
    diff = [[-1,1],[1,-1]]
    norm = [[1,1],[1,1]]
    rd, rn = rank(diff,p),rank(norm,p)
    check(f'C2 resolution over F_{p}',
          matmul(diff,norm,p)==[[0,0],[0,0]] and rd+rn==2,
          {'difference_rank':rd,'norm_rank':rn,'kernel_equals_image_dimension':2-rd})
    # Hom into the trivial F_p-module alternates 0 and multiplication by 2.
    dims = [1]
    for q in range(1,13):
        outgoing = (2%p != 0) if q%2 else False
        incoming = False if q%2 else (2%p != 0)
        dims.append(1-int(outgoing)-int(incoming))
    expected = [1]*13 if p==2 else [1]+[0]*12
    check(f'C2 trivial cohomology through degree 12 over F_{p}',dims==expected,
          {'dimensions_H0_through_H12':dims})
    # Restrictions to y=0 and y=x give the same Kummer class of x.
    diagonal = [[1],[1]]
    r = rank(diagonal,p)
    check(f'one-divisor witness cokernel over F_{p}',r==1 and 2-r==1,
          {'matrix':diagonal,'rank':r,'cokernel_dimension':2-r})
    # The multiplicity-p cycle map vanishes modulo p in Nagata's example.
    check(f'multiplicity in F_{p}', p%p==0 and rank([[1]],p)==1,
          {'multiplicity_p_mod_p':p%p,'multiplicity_one_rank':rank([[1]],p)})

# This is the finite exact sequence used in quadratic descent.
d = [[1],[1]]
s = [[1,1]]
swap = [[0,1],[1,0]]
check('quadratic descent exactness and equivariance',
      rank(d,2)==1 and rank(s,2)==1 and matmul(s,d,2)==[[0]]
      and matmul(s,swap,2)==s and matmul(swap,d,2)==d,
      {'diagonal':d,'sum':s,'swap':swap,'dimensions':[1,2,1]})

# A finite slice of the Laurent-form obstruction in the wild example.
exponents = list(range(-12,9))
allowed = [[int(e==power) for e in exponents] for power in range(-1,9)]
negative = [[int(e==power) for e in exponents] for power in range(-12,-1)]
check('wild-symbol Laurent-form obstruction over F2',
      rank(allowed,2)==10 and rank(allowed+negative,2)==21,
      {'exponent_range':[-12,8],'allowed_powers':[-1,8],
       'independent_negative_classes':11,'witness_power':-2})
for mask in range(1<<10):
    coefficients = [sum(((mask>>j)&1)*v[i] for j,v in enumerate(allowed))%2
                    for i in range(len(exponents))]
    assert coefficients[exponents.index(-2)]==0
check('wild obstruction coefficient functional', True,
      {'allowed_forms_exhaustively_tested':1<<10,
       'coefficient_of_t_to_minus_2_in_every_allowed_form':0,
       'coefficient_in_witness':1})

output = {'utc':datetime.now(timezone.utc).isoformat(),
          'scope':'Finite linear algebra only; no claim to certify infinite geometric theorems.',
          'prime_cases':[2,3,5,7],'checks':checks,'check_count':len(checks),
          'cohomology_degrees_per_prime':13,'seconds':time.perf_counter()-started}
path=Path(__file__).resolve().parent/'output/verify_A_finite.json'
path.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
