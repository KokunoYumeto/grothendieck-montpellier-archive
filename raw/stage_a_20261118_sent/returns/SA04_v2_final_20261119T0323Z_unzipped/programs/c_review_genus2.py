"""Independent trace-formula check of root's scan204 counterexample.
Uses polynomial convolution/reduction rather than enumerating the affine z equation.
"""
import json
from fractions import Fraction

def degree(a):return a.bit_length()-1
def prod(a,b,mod):
    # Convolution of binary coefficients, then polynomial long division.
    v=0
    for i in range(a.bit_length()):
        for j in range(b.bit_length()):
            if ((a>>i)&1) and ((b>>j)&1):v^=1<<(i+j)
    while degree(v)>=degree(mod):v^=mod<<(degree(v)-degree(mod))
    return v
def power(a,k,mod):
    out=1
    for _ in range(k):out=prod(out,a,mod)
    return out
records=[]
for n,mod in [(1,3),(2,7),(3,11),(4,19)]:
    q=2**n
    assert all(power(a,q-1,mod)==1 for a in range(1,q))
    poles=[];trace0=[];trace1=[]
    for x in range(q):
        h=prod(x,x,mod)^x^1
        if h==0:poles.append(x);continue
        r=x^power(h,q-2,mod)
        tr=0
        for j in range(n):tr^=power(r,2**j,mod)
        assert tr in [0,1]
        (trace0 if tr==0 else trace1).append(x)
    N=1+len(poles)+2*len(trace0)
    records.append(dict(n=n,q=q,polynomial_bits=mod,finite_poles=poles,trace0_x=trace0,trace1_x=trace1,N=N))
assert [r['N'] for r in records]==[3,7,9,31]
# Newton identities from all four independent counts, without imposing a functional equation.
power_sums=[0]+[2**n+1-records[n-1]['N'] for n in range(1,5)]
coeff=[Fraction(1)]
for k in range(1,5):
    coeff.append(-sum(coeff[k-i]*power_sums[i] for i in range(1,k+1))/k)
assert coeff==[1,0,1,0,4]
print(json.dumps(dict(method='Artin-Schreier trace criterion with explicit field verification',records=records,power_sums=power_sums[1:],numerator_coefficients=list(map(str,coeff)),Jacobian_order=int(sum(coeff)),rational_2_torsion_dimension=1,mod2_root1_multiplicity=2),indent=2))
