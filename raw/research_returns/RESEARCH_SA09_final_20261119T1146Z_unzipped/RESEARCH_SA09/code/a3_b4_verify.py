"""Finite certificates supporting A3 and B4; not an all-level proof.
The all-level statements are proved in the paper. This program checks
finite-difference ranks, the explicit finite obstruction, and all projected
Kummer subgroup counts through level 128, with closure at selected levels.
"""
from math import comb, gcd, lcm
from time import perf_counter
from pathlib import Path
import json
start=perf_counter()
rank_checks=0
for n in range(9):
    seq=[comb(m+n+1,n+1) for m in range(20)]
    for i in range(15):
        expected=comb(n+1,i) if i<=n+1 else 0
        assert seq[0]==expected,(n,i,seq[0],expected)
        rank_checks+=1
        seq=[seq[j+1]-seq[j] for j in range(len(seq)-1)]
units5=[u for u in range(5) if gcd(u,5)==1]
lens_rows=[{'unit':u,'sign':eps,'signed_square_mod5':(eps*u*u)%5}
           for u in units5 for eps in (1,-1)]
assert all(row['signed_square_mod5']!=2 for row in lens_rows)
# The polynomial (t^2-t)/2 has a coefficient with denominator 2.
from fractions import Fraction
assert Fraction(1,2).denominator==2
assert 0%2==2%2 and comb(0,2)%2!=comb(2,2)%2

def chi2(a):return 1 if a%8 in (1,7) else -1

def compose(g,h,n):
    return ((g[0]*h[0])%n,)+tuple((g[i]+g[0]*h[i])%n for i in range(1,len(g)))

rows=[];closure_pairs=0
for n in range(1,129):
    mod_a=lcm(8,2*n);mod_b=lcm(2,n)
    H2=set();Hm=set();HE=set()
    for a in range(mod_a):
        if gcd(a,mod_a)!=1:continue
        for b in range(mod_b):
            if (-1)**b!=chi2(a):continue
            c=((a-1)//2-b)%n
            H2.add((a%n,b%n));Hm.add((a%n,c))
            HE.add((a%n,(c-a+1)%n,c))
    phi=sum(gcd(a,n)==1 for a in range(n)) if n>1 else 1
    defect=2 if n%8==0 else 1
    assert len(H2)==n*phi//defect
    assert len(Hm)==n*phi//defect
    assert len(HE)==n*phi//defect
    assert all((g[2]-g[1]-g[0]+1)%n==0 for g in HE)
    if n%8==0:
        assert all((-1)**b==chi2(a) for a,b in H2)
        assert all((-1)**c==((-1)**((a-1)//2))*chi2(a) for a,c in Hm)
    if n in (1,2,4,8,12,16):
        for H in (H2,Hm,HE):
            for g in H:
                for h in H:
                    assert compose(g,h,n) in H
                    closure_pairs+=1
    rows.append({'n':n,'phi_n':phi,'K2_image_order':len(H2),
                 'Kminus_half_image_order':len(Hm),'Fermat_image_order':len(HE),
                 'K2_affine_index':n*phi//len(H2),
                 'Fermat_scalar_affine_index':n*n*phi//len(HE)})
output={'scope':'n=1,...,128; subgroup closure n=1,2,4,8,12,16; R_n ranks n=0,...,8',
        'rank_checks':rank_checks,'lens_signed_squares':lens_rows,
        'lens_nonisometry_verified':True,'closure_pairs_checked':closure_pairs,
        'levels':rows,'elapsed_seconds':perf_counter()-start}
root=Path(__file__).resolve().parents[1]
(root/'logs/a3_b4_verify.json').write_text(json.dumps(output,indent=2))
print('Rank finite-difference checks:',rank_checks)
print('Signed squares of units modulo 5:',sorted({r['signed_square_mod5'] for r in lens_rows}))
print('No signed unit square equals 2: verified')
print('Binomial naturality obstruction mod2: inputs 0 and2 agree, outputs0 and1 differ')
print('Subgroup composition pairs checked:',closure_pairs)
print('All 128 levels satisfy the proved image/order formulas')
for n in (1,2,4,8,16,24,64,128):print(rows[n-1])
print('Elapsed seconds:',output['elapsed_seconds'])
