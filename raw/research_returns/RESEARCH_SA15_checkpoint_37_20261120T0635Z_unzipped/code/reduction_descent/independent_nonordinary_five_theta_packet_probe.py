"""Exact fifth-torsion theta-packet census on y^2+y=x^5 over F16.

The group coordinates are reconstructed from the explicit Weil-function
pairings. All finite assertions are checked; geometric interpretation is
separate in the accompanying proof note.
"""
from pathlib import Path
from itertools import combinations,product
import json,time,datetime
start=time.perf_counter()
modulus=0b10011

def mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&16:a^=modulus
    return z

def power(a,n):
    z=1
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n>>=1
    return z

def inv(a):
    assert a
    return power(a,14)
points=[None]+[(a,b) for a in range(16) for b in range(16) if power(b,2)^b==power(a,5)]
assert len(points)==33
zeta=power(2,3)
assert power(zeta,5)==1 and zeta!=1
log={power(zeta,i):i for i in range(5)}

def weil_function(P,Q):
    a,b=P;c,d=Q
    return d^mul(power(a,8),power(c,2))^mul(power(a,4),c)^power(b,4)

def pairing(P,Q):
    if P is None or Q is None or P==Q:return 0
    x=weil_function(P,Q);y=weil_function(Q,P)
    assert x and y and x==power(y,4)
    e=mul(x,inv(y));assert e in log
    return log[e]
B=[[pairing(P,Q) for Q in points] for P in points]
assert all((B[i][j]+B[j][i])%5==0 for i in range(33) for j in range(33))

def echelon(rows):
    a=[[x%5 for x in row] for row in rows];piv=[];r=0
    if not a:return a,piv
    for j in range(len(a[0])):
        s=next((s for s in range(r,len(a)) if a[s][j]),None)
        if s is None:continue
        a[r],a[s]=a[s],a[r];u=pow(a[r][j],-1,5);a[r]=[(x*u)%5 for x in a[r]]
        for k in range(len(a)):
            if k!=r and a[k][j]:
                u=a[k][j];a[k]=[(x-u*y)%5 for x,y in zip(a[k],a[r])]
        piv.append(j);r+=1
        if r==len(a):break
    return a,piv
assert len(echelon(B)[1])==4
chosen=next(I for I in combinations(range(1,33),4) if len(echelon([[B[i][j] for j in I] for i in I])[1])==4)
J=[[B[i][j] for j in chosen] for i in chosen]

def solve4(A,b):
    q,p=echelon([row+[v] for row,v in zip(A,b)])
    assert p[:4]==list(range(4))
    return tuple(row[4] for row in q)
vec=[solve4(J,[B[i][j] for i in chosen]) for j in range(33)]
assert len(set(vec))==33 and vec[0]==(0,0,0,0)
def symp(u,v):return sum(u[i]*J[i][j]*v[j] for i in range(4) for j in range(4))%5
assert all(symp(vec[i],vec[j])==B[i][j] for i in range(33) for j in range(33))
for i,P in enumerate(points[1:],1):
    q=points.index((P[0],P[1]^1))
    assert all((x+y)%5==0 for x,y in zip(vec[i],vec[q]))

def add(u,v):return tuple((x+y)%5 for x,y in zip(u,v))
def scale(c,v):return tuple(c*x%5 for x in v)
def sub(u,v):return tuple((x-y)%5 for x,y in zip(u,v))
def encode(v):return sum(x*5**i for i,x in enumerate(v))
def decode(n):return tuple(n//5**i%5 for i in range(4))
zero=(0,0,0,0)
lines={}
for v in product(range(5),repeat=4):
    if v==zero:continue
    c=next(x for x in v if x);u=scale(pow(c,-1,5),v);lines[u]=u
assert len(lines)==156
planes={}
for u,v in combinations(lines,2):
    if symp(u,v):continue
    K=frozenset(encode(add(scale(a,u),scale(b,v))) for a,b in product(range(5),repeat=2))
    assert len(K)==25
    planes.setdefault(tuple(sorted(K)),(u,v))
assert len(planes)==156
census=[];bad_lines=[]
for u in lines:
    H=[scale(c,u) for c in range(5)]
    packets={}
    for i,v in enumerate(vec):
        rep=min(encode(sub(v,h)) for h in H);packets.setdefault(rep,[]).append(i)
    if max(map(len,packets.values()))>=3:bad_lines.append({'basis':u,'packets':[x for x in packets.values() if len(x)>=3]})
for Kencoded,(u,v) in sorted(planes.items()):
    K=[decode(x) for x in Kencoded];packets={}
    for i,x in enumerate(vec):
        rep=min(encode(sub(x,h)) for h in K);packets.setdefault(rep,[]).append(i)
    sizes={n:sum(len(z)==n for z in packets.values()) for n in sorted({len(z) for z in packets.values()})}
    maximum=max(sizes)
    tangencies=[i for i,x in enumerate(vec) if i and encode(x) in Kencoded]
    good=maximum<=2 and not tangencies
    census.append({'basis':[u,v],'packet_size_counts':sizes,'max_packet':maximum,'theta_points_in_kernel':tangencies,'good_nodal':good,'multiple_packets':[z for z in packets.values() if len(z)>=3]})
counts={n:sum(c['max_packet']==n for c in census) for n in sorted({c['max_packet'] for c in census})}
differences={encode(sub(x,y)) for i,x in enumerate(vec) for j,y in enumerate(vec) if i!=j}
assert len(differences)==544
result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'field_modulus':modulus,'zeta5':zeta,'curve_points':points,'chosen_basis_indices':chosen,'symplectic_matrix':J,'curve_torsion_vectors':vec,'pairing_matrix_rank':4,'lagrangian_count':156,'good_nodal_count':sum(c['good_nodal'] for c in census),'max_packet_census':counts,'bad_cyclic_line_count':len(bad_lines),'bad_cyclic_lines':bad_lines,'rational_difference_count':len(differences),'lagrangians':census,'scope':'Exact F16 coordinates, explicit function-pairing reconstruction and finite packet enumeration; universal/fixed-target geometric conclusions are not inferred by this program.'}
out=Path(__file__).resolve().parent.parent/'outputs/nonordinary_five_theta_packet_probe.json';out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('curve_points','curve_torsion_vectors','bad_cyclic_lines','lagrangians')},indent=2))
