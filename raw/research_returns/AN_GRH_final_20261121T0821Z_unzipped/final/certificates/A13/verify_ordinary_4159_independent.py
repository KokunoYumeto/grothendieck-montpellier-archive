"""Independent exact checks for the ordinary genus-two Lang-cover example.

No producer imports. Compute the Jacobian order as a Sylvester determinant,
not using the producer's Frobenius power-sum recurrence. Standard library only.
"""
from math import isqrt
from pathlib import Path
import json

def mul4(x,y):
    z=0
    while y:
        if y&1:z^=x
        y>>=1;x<<=1
        if x&4:x^=7
    return z

def trace4(x):return x^mul4(x,x)
def inv4(x):
    assert x
    return next(y for y in range(1,4) if mul4(x,y)==1)

counts={2:3}
# The three simple poles (0,1,infinity) each give one ramified rational point.
counts[4]=3+sum(2 for x in (2,3) if trace4(x^inv4(x)^inv4(x^1))==0)
assert counts=={2:3,4:3}
# N1=3,N2=3 imply s1=0,s2=2, hence P(T)=T^4-T^2+4.
f=[1,0,-1,0,4]
g=[1,0,0,0,0,0,0,-1] # T^7-1
m,n=len(f)-1,len(g)-1
matrix=[]
for i in range(n):matrix.append([0]*i+f+[0]*(n-1-i))
for i in range(m):matrix.append([0]*i+g+[0]*(m-1-i))

def det_bareiss(a):
    a=[r[:] for r in a];sign=1;previous=1;n=len(a)
    for k in range(n-1):
        if a[k][k]==0:
            j=next(j for j in range(k+1,n) if a[j][k])
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=pivot*a[i][j]-a[i][k]*a[k][j]
                assert num%previous==0
                a[i][j]=num//previous
        for i in range(k+1,n):a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]

order=det_bareiss(matrix)
assert order==16636==4*4159
ell=4159
assert all(ell%d for d in range(2,isqrt(ell)+1))
assert 2*3**3*7*11==ell-1
o=2079
assert pow(2,o,ell)==1
quotient_powers={str(q):pow(2,o//q,ell) for q in (3,7,11)}
assert all(x!=1 for x in quotient_powers.values())
assert o%2==1 and 2*o==ell-1
# N_theta >= (129-10*sqrt(128))/4 > 3; square positive sides exactly.
assert 129-4*3>0 and (129-4*3)**2>100*128
assert 128>(2*4+3)**2
result=dict(status='PASS',counts=counts,frobenius_polynomial_descending=f,
            jacobian_order_over_F128=order,resultant_method='11x11 Sylvester determinant, fraction-free Bareiss',
            factorization={'2':2,'4159':1},prime_trial_division_max=isqrt(ell),
            order_of_2_mod_4159=o,proper_quotient_powers=quotient_powers,
            generates_with_minus_one=True,Lang_index=4,
            integer_theta_lower_bound=4,formal_verification=False)
out=Path(__file__).with_name('ordinary_4159_independent_check.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
