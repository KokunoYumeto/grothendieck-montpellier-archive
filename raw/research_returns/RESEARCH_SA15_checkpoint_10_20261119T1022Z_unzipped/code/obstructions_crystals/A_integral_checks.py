"""Exact arithmetic checks; geometric claims are proved in the accompanying TeX."""
from time import perf_counter
import json
from pathlib import Path
started=perf_counter()
rows=[]
for p in (2,3,5,7,11,13,17,19):
    ell=p+1
    q=ell**2
    n=2 if p==2 else p*(p-2)
    assert p*ell*n%2==0
    g=1+p*ell*n//2
    B=g+p+2+p**3*(p+1)*n//2
    direct_B=g+2+sum(p*p*i*n+1 for i in range(1,p+1))
    assert B==direct_B
    r=0
    direct_r=0
    for i in range(p+1):
        a=p*ell-i
        assert ell*n*a*(a+1)%2==0
        r+=(a+1)*((q+p*i)*n+1-g)+ell*n*a*(a+1)//2
        for j in range(a+1):
            degree=(q+p*i+ell*j)*n
            assert degree>2*g-2
            direct_r+=degree+1-g
    assert r==direct_r and r>0 and q%p==1
    rows.append(dict(p=p,ell=ell,q=q,n=n,g=g,B_p=B,r=r,
                     h0_differentials_bound=f'{q}^{r}*{B+r}',
                     chosen_m=f'{q}^{r}*{B+r}+2',strict_margin=1))
assert rows[0]['B_p']==35 and rows[0]['r']==556
assert rows[0]['h0_differentials_bound']=='9^556*591'
# The p-torsion generator-number inequality has strict margin one even when a=1.
for qx in range(12):
    for b1 in range(12):
        for h10 in range(12):
            m=h10+2
            assert (qx+m-1-b1)-(qx+h10-b1)==1
out=dict(status='PASS',scope='Exact integer identities and dimension-bound margin; no numerical approximation to crystalline cohomology is claimed.',
         primes_checked=rows,elapsed_seconds=perf_counter()-started)
target=Path(__file__).with_name('A_integral_checks_output.json')
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
