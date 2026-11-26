"""Exact finite certificate for ALP-LIFT-18.
Checks the actual G halves, residue norms, source congruence and HC numbers.
The global character proof is in the accompanying Markdown.
"""
from fractions import Fraction
from math import gcd
import json

def prime(q):
    return q>=2 and all(q%d for d in range(2,int(q**0.5)+1))
def factors(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out
def primitive(q):
    return next(a for a in range(2,q)
                if all(pow(a,(q-1)//p,q)!=1 for p in factors(q-1)))

phi=[1,3,9,15,17,23]
psi=[1,9,11,15,23,25]
assert sum(phi)==68 and sum(psi)==84
assert sorted(a for a in range(1,28) if gcd(a,28)==1 and a%7 in (1,2,4))==psi
prime_data={}
for q,a,b in ((113,1,4),(281,13,4)):
    assert prime(q) and (q-1)%28==0 and q-1>72
    assert a*a+7*b*b==q and gcd(q,2*a)==1
    g=primitive(q)
    z=pow(g,(q-1)//28,q)
    selected=[]
    for power in range(1,28):
        if gcd(power,28)!=1:continue
        zz=pow(z,power,q)
        s=(sum(pow(zz,4*i,q) for i in (1,2,4))-
           sum(pow(zz,4*i,q) for i in (3,5,6)))%q
        if (a-b*s)%q==0:selected.append(zz)
    assert len(selected)==6
    norm=1
    for x in selected:norm=norm*x%q
    assert norm==1
    prime_data[q]={"primitive_generator":g,
                   "selected_zeta28_residues":selected,
                   "relative_norm_mod_q":norm,
                   "chi_orders":[(q-1)//gcd(q-1,2*(i+1)) for i in range(2)]}

k,m,t=6,2,1795
r=k+m-1
threshold=(r+m*t)**3
C=46539458987
assert C%7==0 and C>threshold+k+t+10
u=[Fraction((2*(k-i)+1)*C)+Fraction(1,2) for i in range(k)]
v=[Fraction(2*(k-i)*C) for i in range(k-1)]
b=[Fraction((4*j-2)*C) for j in range(m)]
e=[Fraction(4*j*C) for j in range(m)]
eta=Fraction(-1,2)
assert all(u[i]>v[i]>u[i+1] for i in range(k-1))
assert u[-1]>-b[0]
assert b[0]<e[0]<b[1]<e[1]
bound=Fraction(t+3,2)
block=lambda center:[center+Fraction(t-1,2)-i for i in range(t)]
for j in range(m):
    assert all(abs(x+e[j])>=bound for x in u+v)
    assert all(abs(e[j]-x)>=bound for x in b)
    for jp in range(m):
        if jp!=j:
            assert all(abs(x+e[j])>=bound for x in block(-e[jp]))
gap_data={}
for j in range(m+1):
    data={(x,True) for x in v}
    data.update((-b[i],i<=j or (i-j)%2==0) for i in range(m))
    for i in range(m):
        if i<j:data.update((x,True) for x in block(-e[i]))
    shift=eta if j%2 else 0
    pos=[x+shift for x,sg in data if sg]
    neg=[x+shift for x,sg in data if not sg]
    distances=[abs(x-y) for x in pos for y in neg]
    assert all(d>threshold for d in distances)
    gap_data[j]=None if not distances else str(min(distances))
assert all((sum(phi)*int(ej))%28==0 for ej in e)
rho=[Fraction(k-1,2)-i for i in range(k)]
nu=[u[i]-rho[i]+e[0]-Fraction(k+t+1,2) for i in range(k)]
assert all(x.denominator==1 and x>=0 for x in nu)
assert nu[-1]==3*C-898
assert 1801<=r+t and m+3<=k and r+5<=t and 3*m<t and m*m<=k+m*(t+1)
assert 113*281==31753

print(json.dumps({"status":"PASS","G_primes":prime_data,
                  "C":C,"e":[int(x) for x in e],
                  "NCGaps_threshold":threshold,
                  "NCGaps_minima":gap_data,
                  "selected_nu_min":int(nu[-1]),
                  "scope":"Exact finite residue and numerical-source checks; not a formal global-character proof."},indent=2))

