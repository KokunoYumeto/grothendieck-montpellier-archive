"""Standalone universal characteristic-two Moore/Fermat certificate.

Reconstructs the literal determinant and its monic remainder; no external data
or author output is imported.  All support/phase exclusions are universal
coefficient identities, not tests at finitely many parameter values.
"""
from pathlib import Path
from itertools import product, permutations
from collections import defaultdict, Counter
from functools import lru_cache
from datetime import datetime, timezone
import hashlib, json, time

start=time.perf_counter()
pts=list(product(range(3),repeat=2));idx={p:i for i,p in enumerate(pts)}
plus=[[idx[((a[0]+b[0])%3,(a[1]+b[1])%3)]for b in pts]for a in pts]
minus=[[idx[((a[0]-b[0])%3,(a[1]-b[1])%3)]for b in pts]for a in pts]
enc=lambda es:sum(e<<(4*i)for i,e in enumerate(es))
dec=lambda n:tuple((n>>(4*i))&15 for i in range(9))
def mul(a,b):
    out=set()
    for x in a:
        for y in b:
            z=x+y
            if z in out:out.remove(z)
            else:out.add(z)
    return out
def cube(a):return mul(mul(a,a),a)
def xor(*polys):
    out=set()
    for p in polys:out.symmetric_difference_update(p)
    return out
def mon(*indices):
    return sum(1<<(4*i)for i in indices)

entries=[[(1<<(36+4*minus[i][j]))+(1<<(4*plus[i][j]))for j in range(9)]for i in range(9)]
det=set()
for p in permutations(range(9)):
    m=sum(entries[i][j]for i,j in enumerate(p))
    if m in det:det.remove(m)
    else:det.add(m)
coeff=defaultdict(set)
for m in det:coeff[m&((1<<36)-1)].add(m>>36)
assert len(det)==55296 and len(coeff)==2080
S={3<<(4*i)for i in range(1,9)}
powers=[{0}]
for j in range(3):powers.append(mul(powers[-1],S))
@lru_cache(None)
def rem_x(x):
    q,r=divmod(x&15,3)
    base=x-(x&15)+r
    return {base+t for t in powers[q]}
rem=defaultdict(set)
for x,cs in coeff.items():
    for xr in rem_x(x):rem[xr].symmetric_difference_update(cs)
rem={x:cs for x,cs in rem.items()if cs}
assert len(rem)==1085 and sum(map(len,rem.values()))==47349
assert all((x&15)<3 for x in rem)

squarefree=enc([1]*9)
assert coeff[squarefree]==rem[squarefree]==cube({3<<(4*i)for i in range(9)})
assert len(rem[squarefree])==81
normals=[(1,0),(0,1),(1,1),(1,2)]
lines=[[frozenset(i for i,g in enumerate(pts)if(n[0]*g[0]+n[1]*g[1])%3==j)
        for j in range(3)]for n in normals]
product_factors=[]
for n,parallel in zip(normals,lines):
    P={mon(*line)for line in parallel}
    target=cube(P)
    locators=[dec(x)for x,cs in rem.items()if cs==target]
    assert locators
    product_factors.append({'normal':n,'cubic_terms':[dec(m)for m in sorted(P)],
                            'cube_coefficient_locators':locators})

def support(m):return sum(1<<i for i,e in enumerate(dec(m))if e)
support_table=sorted([(x,[(m,support(m))for m in cs])for x,cs in rem.items()],key=lambda a:len(a[1]))
excluded=[];survivors=[]
for s in range(1,512):
    witness=None
    for x,ms in support_table:
        kept=[m for m,supp in ms if supp&~s==0]
        if len(kept)==1:
            witness={'x_exponents':dec(x),'c_exponents':dec(kept[0])};break
    if witness:excluded.append({'support':s,'witness':witness})
    else:survivors.append(s)
assert len(excluded)==399 and len(survivors)==112
assert dict(Counter(s.bit_count()for s in survivors))=={2:36,4:54,6:12,8:9,9:1}

linear=[m for m in product(range(3),repeat=4)if(m[0]*m[3]-m[1]*m[2])%3]
def transform(i,m,t):
    x,y=pts[i]
    return idx[((m[0]*x+m[1]*y+t[0])%3,(m[2]*x+m[3]*y+t[1])%3)]
transforms=[tuple(transform(i,m,t)for i in range(9))for m in linear for t in pts]
assert len(set(transforms))==432
representatives=[(1,2),(1,2,3,6),tuple(range(3,9)),tuple(range(1,9)),tuple(range(9))]
affine_orbits=[]
for rep in representatives:
    maps={sum(1<<tr[i]for i in rep):tr for tr in transforms}
    affine_orbits.append({'representative':rep,'size':len(maps),'maps':maps})
assert [r['size']for r in affine_orbits]==[36,54,12,9,1]
assert set(survivors)==set().union(*(set(r['maps'])for r in affine_orbits))

def restricted(supp):
    mask=sum(1<<i for i in supp)
    return {x:kept for x,cs in rem.items()if(kept:={m for m in cs if support(m)&~mask==0})}
def factor_record(name,supp,target):
    locators=[dec(x)for x,cs in restricted(supp).items()if cs==target]
    assert locators,name
    return {'name':name,'support':supp,'c_terms':[dec(m)for m in sorted(target)],'locators':locators}
factors=[]
factors.append(factor_record('two',(1,2),cube({3<<(4*1),3<<(4*2)})))
factors.append(factor_record('four_first',(1,2,3,6),mul({3<<(4*1),3<<(4*2)},{mon(3,3,3,6,6,6)})))
factors.append(factor_record('four_second',(1,2,3,6),mul({3<<(4*3),3<<(4*6)},{mon(1,1,1,2,2,2)})))
six=tuple(range(3,9))
factors.append(factor_record('six_product',six,cube({mon(3,4,5),mon(6,7,8)})))
factors.append(factor_record('six_cube_sum',six,cube({3<<(4*i)for i in six})))
for r in range(3):
    P={0}
    for i in range(3):P=mul(P,{3<<(4*(3+i)),3<<(4*(6+(i+r)%3))})
    factors.append(factor_record('six_matching_'+str(r),six,P))
assert len(factors)==8

# All line choices and the stabilizer orbits needed for the repaired
# eight-coordinate argument. These are independent of the old, absent
# opposite-pair binomials in the remainder.
choices={c:frozenset(lines[i][c[i]]for i in range(4))for c in product(range(3),repeat=4)}
def orbit(choice):
    return {frozenset(frozenset(tr[i]for i in line)for line in choice)for tr in transforms}
conc=orbit(choices[(0,0,0,0)]);nonconc=orbit(choices[(0,0,0,1)])
assert len(conc)==9 and len(nonconc)==72 and conc.isdisjoint(nonconc)
assert conc|nonconc==set(choices.values())
base=choices[(0,0,0,1)]
stabilizer=[tr for tr in transforms if frozenset(frozenset(tr[i]for i in line)for line in base)==base]
assert len(stabilizer)==6
zero_orbits={frozenset(tr[i]for tr in stabilizer)for i in range(9)}
assert zero_orbits=={frozenset((0,)),frozenset((2,3,7)),frozenset((1,5,6)),frozenset((4,8))}
line_records=[]
for c,choice in choices.items():
    mult=[sum(i in line for line in choice)for i in range(9)]
    assert max(mult)in(3,4)and mult.count(max(mult))==1
    line_records.append({'constants':c,'type':'concurrent'if max(mult)==4 else'triple-plus-one','centre':mult.index(max(mult))})

# Normal-form cube identities, represented by coefficient masks in five
# independent symbols E,A,B,D,Z.  This also checks the unique-zero cases.
def variable(i):return {1<<(4*i)}
E,A,B,D,Z=[variable(i)for i in range(5)]
U=xor(E,A);W=xor(E,B);V=xor(A,B);T=xor(E,A,B)
assert xor(mul(B,V),mul(W,T))==mul(E,U)
assert xor(mul(A,T),mul(U,V))==mul(E,B)
assert xor(mul(A,B),mul(U,W))==mul(E,T)
assert xor(mul(xor(D,A),U),mul(xor(D,W),B))==mul(xor(D,V),T)
# E=1, a=0 => BV+WT=1; u=0 => A=1, T=B, W=V=1+B.
one={0}
assert xor(mul(B,B),mul(xor(one,B),xor(one,B)))==one
assert xor(one,one,B)==B
assert xor(one,B)==xor(one,B)
# Opposite pairs about the representative double point index2.
cube_forms=[one,one,set(),B,xor(one,B),xor(one,B),xor(one,B),B,xor(one,B)]
h=2
for i in range(9):
    j=idx[((2*pts[h][0]-pts[i][0])%3,(2*pts[h][1]-pts[i][1])%3)]
    assert cube_forms[i]==cube_forms[j]

# Explicit full-torus ideal identity. Variables a,b,d,u,v,w,t use indices0..6.
a,b,d,u,v,w,t=[variable(i)for i in range(7)]
rhs=[xor(one,cube(a)),xor(cube(a),cube(b)),xor(one,cube(b)),xor(one,cube(a),cube(b))]
rp=[]
for p in rhs:
    seq=[one]
    for j in range(3):seq.append(mul(seq[-1],p))
    rp.append(seq)
def reduce_cubes(P):
    result=set()
    for m in P:
        es=list(dec(m));part=one
        for j in range(4):
            q,r=divmod(es[j+3],3);es[j+3]=r
            part=mul(part,rp[j][q])
        result.symmetric_difference_update({enc(es)+x for x in part})
    return result
I1=xor(mul(a,u),mul(d,xor(mul(b,v),mul(w,t))))
I2=xor(mul(b,w),mul(d,xor(mul(a,t),mul(u,v))))
I3=xor(mul(v,t),mul(d,xor(mul(a,b),mul(u,w))))
d2=mul(d,d)
R1=xor(mul(b,v),mul(w,t));R2=xor(mul(a,t),mul(u,v));R3=xor(mul(a,b),mul(u,w))
J1=xor(mul(d2,mul(mul(b,v),mul(w,t))),mul(mul(a,u),mul(d,R1)))
J2=xor(mul(d2,mul(mul(a,u),mul(v,t))),mul(mul(b,w),mul(d,R2)))
J3=xor(mul(d2,mul(mul(a,b),mul(u,w))),mul(mul(v,t),mul(d,R3)))
identity=xor(cube(I1),cube(I2),cube(I3),mul(J1,I1),mul(J2,I2),mul(J3,I3))
K=mul(d2,mul(mul(mul(a,b),mul(u,v)),mul(w,t)))
assert reduce_cubes(identity)==K

# Eight-support cube equalities now follow from the written zero-orbit proof.
# Retain independent-variable phase substitutions and a monomial witness for
# every noncharacter pattern. No finite parameter sampling is used.
r8=restricted(range(1,9));pairs=[(1,2),(3,6),(4,8),(5,7)]
characters={tuple((ell[0]*pts[a][0]+ell[1]*pts[a][1])%3 for a,b in pairs)for ell in pts}
roots=[1,2,3];phase_records=[]
for phase in product(range(3),repeat=4):
    nonzero=0;witness=None
    for x,cs in r8.items():
        values={}
        for m in cs:
            es=dec(m);ds=tuple(es[a]+es[b]for a,b in pairs)
            exponent=sum(phase[j]*es[a]for j,(a,b)in enumerate(pairs))%3
            value=values.get(ds,0)^roots[exponent]
            if value:values[ds]=value
            elif ds in values:del values[ds]
        if values:
            nonzero+=1
            if len(values)==1 and witness is None:
                ds,value=next(iter(values.items()))
                witness={'x_exponents':dec(x),'d_exponents':ds,'F4_scalar':value}
    assert (nonzero==0)==(phase in characters)
    assert phase in characters or witness is not None
    phase_records.append({'phase':phase,'character':phase in characters,'nonzero_coefficients':nonzero,'monomial_witness':witness})

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,
     'counts':{'permutations':362880,'universal_monomials':len(det),'universal_coefficients':len(coeff),
               'remainder_coefficients':len(rem),'remainder_monomials':sum(map(len,rem.values())),
               'single_monomial_exclusions':399,'surviving_supports':112,'old_factors_reverified':8,
               'line_product_cube_coefficients':4,'line_choices':81,'concurrent_choices':9,
               'nonconcurrent_choices':72,'nonconcurrent_stabilizer':6,'zero_position_orbits':4,
               'phase_patterns':81,'character_phases':9,'phase_exclusions':72,'full_torus_ideal_identities':1},
     'point_order':pts,'support_exclusions':excluded,'support_orbits':affine_orbits,
     'lower_support_factors':factors,'central_squarefree_coefficient':[dec(m)for m in sorted(rem[squarefree])],
     'line_product_cube_coefficients':product_factors,'line_choices':line_records,
     'zero_position_orbits':[sorted(s)for s in sorted(zero_orbits,key=lambda x:(len(x),sorted(x)))],
     'full_torus_identity':{'variables':['a','b','d','u','v','w','t'],
         'relations':['u^3=1+a^3','v^3=a^3+b^3','w^3=1+b^3','t^3=1+a^3+b^3'],
         'I1':'a*u+d*(b*v+w*t)','I2':'b*w+d*(a*t+u*v)','I3':'v*t+d*(a*b+u*w)',
         'identity':'Sum_j (I_j^3+J_j*I_j)=d^2*a*b*u*v*w*t modulo the four cube relations', 'J1':'d^2*b*v*w*t+a*u*d*(b*v+w*t)', 'J2':'d^2*a*u*v*t+b*w*d*(a*t+u*v)', 'J3':'d^2*a*b*u*w+v*t*d*(a*b+u*w)'},
     'eight_support_phase_records':phase_records,
     'remainder_sha256':hashlib.sha256(json.dumps({hex(x):sorted(map(hex,cs))for x,cs in sorted(rem.items())},sort_keys=True).encode()).hexdigest(),
     'scope':'Universal algebraic certificate for Fermat divisibility iff identically zero determinant, with the written affine-line/zero-orbit proof. No actual geometric gauge, Cartier wall or full monodromy consequence is asserted by this program alone.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in('status','actual_utc','runtime_seconds','counts','remainder_sha256')},indent=2))
