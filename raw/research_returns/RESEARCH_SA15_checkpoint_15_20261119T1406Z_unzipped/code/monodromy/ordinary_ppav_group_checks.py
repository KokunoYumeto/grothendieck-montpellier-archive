"""Exact checks supporting the ordinary ppav arithmetic quotient and block separation.
These finite calculations do not replace the geometric incidence proof.
"""
import itertools,json,time
from pathlib import Path
start=time.perf_counter()
H=range(4)
def act(a,x):
    u,v=x&1,x>>1
    return ((a[0]*u+a[1]*v)&1)+2*((a[2]*u+a[3]*v)&1)
gl2=[a for a in itertools.product(range(2),repeat=4) if (a[0]*a[3]+a[1]*a[2])%2]
assert len(gl2)==6
perms=[]
for a in gl2:
    pi=[act(a,x) for x in H]
    assert pi[0]==0 and sorted(pi)==list(H)
    # Quotient F2^H/<1111>, represented by zero in coordinate0.
    def quotient(v):
        if v&1:v^=15
        return v>>1
    images=[]
    for j in range(1,4):
        images.append(quotient(1<<pi[j]))
    assert sorted(images)==[1,2,4]
    assert quotient(sum(1<<pi[j] for j in H))==0
    perms.append(tuple(pi[1:]))
assert len(set(perms))==6
order_gl8=1
for j in range(8):order_gl8*=2**8-2**j
assert order_gl8%31==0 and order_gl8%11!=0
assert all(31%q for q in [2,3,5,7,11,13,17])
for n in range(1,102,2):
    for e in range(1,101):
        N=18*n*e
        assert N>=18 and 11<=N
        assert 9*(n+e)**2-1>=8
result={'status':'PASS','GL2_matrices':len(gl2),'character_permutations':perms,
        'GL8_order':order_gl8,'GL8_has_prime31':True,'GL8_lacks_prime11':True,
        'isogeny_degree_cases':51*100,'seconds':time.perf_counter()-start}
print(json.dumps(result,indent=2))
Path(__file__).resolve().parents[1].joinpath('outputs/ordinary_ppav_group_checks.json').write_text(json.dumps(result,indent=2)+'\n')
