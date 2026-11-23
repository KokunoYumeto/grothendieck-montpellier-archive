"""Finite arithmetic checks for ALP-LIFT-17.
Checks actual flag-permutation character sums in rank3.
This is a finite check, not a formal proof of the general local theorem.
"""
from itertools import product
import json

def canon(v, q):
    inv=pow(next(x for x in v if x % q), -1, q)
    return tuple((x*inv)%q for x in v)

def flags3(q):
    lines=sorted({canon(v,q) for v in product(range(q),repeat=3) if any(v)})
    return [(v,n) for v in lines for n in lines if sum(a*b for a,b in zip(v,n))%q==0]

def fixed_count(h, flags, q):
    total=0
    for v,n in flags:
        hv=tuple(sum(h[i][j]*v[j] for j in range(3))%q for i in range(3))
        if canon(hv,q)!=v:
            continue
        nh=tuple(sum(n[i]*h[i][j] for i in range(3))%q for j in range(3))
        if canon(nh,q)==n:
            total+=1
    return total

# r=2,n1=1 over F3, H0=U2 with both choices of additive character,
# and the nontrivial determinant character on GL1.
q=3
fl=flags3(q)
assert len(fl)==52
sums=[[0,0,0] for _ in range(3)]
for u,x,y in product(range(q),repeat=3):
    for t in (1,2):
        h=((1,u,x),(0,1,y),(0,0,t))
        f=fixed_count(h,fl,q)
        sign=1 if t==1 else -1
        for additive in range(3):
            sums[additive][(-additive*u)%3]+=sign*f
# A0+A1*zeta3+A2*zeta3^2=0 iff all three coefficients are equal.
for row in sums:
    assert row[0]==row[1]==row[2],row

# r=1,n1=n2=1 over F5 with distinct nontrivial determinant
# characters omega and omega^2; check every tame scalar twist omega^e.
q=5
fl5=flags3(q)
assert len(fl5)==186
log={pow(2,a,q):a for a in range(4)}
gaussian_sums=[[0,0] for _ in range(4)]
powers=((1,0),(0,1),(-1,0),(0,-1))
for x,y,z in product(range(q),repeat=3):
    for t1,t2 in product(range(1,q),repeat=2):
        h=((1,x,y),(0,t1,z),(0,0,t2))
        f=fixed_count(h,fl5,q)
        for e in range(4):
            exponent=-((1-e)*log[t1]+(2-e)*log[t2])%4
            re,im=powers[exponent]
            gaussian_sums[e][0]+=f*re
            gaussian_sums[e][1]+=f*im
assert gaussian_sums==[[0,0] for _ in range(4)],gaussian_sums

print(json.dumps({
    "status":"PASS",
    "F3_flag_count":52,
    "F3_generic_first_block_character_sums":sums,
    "F5_flag_count":186,
    "F5_two_distinct_blocks_all_four_tame_twists":gaussian_sums,
    "scope":"Finite character-projector traces only; general theorem is proved in Markdown."
},indent=2))

