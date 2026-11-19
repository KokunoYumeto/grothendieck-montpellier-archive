#!/usr/bin/env python3
"""Bounded exact GF64 search for a degree-three norm contact witness.

The output is a candidate until global smoothness and every unwanted kernel
collision are excluded.  No geometric claim is inferred from rational-point
sampling.  Coefficients use the monomial basis (1,x,y) tensor (1,x,y).
"""
from pathlib import Path
import itertools,json,random,time,sys

MOD=0x43
def mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&64:a^=MOD
    return z
def power(a,n):
    z=1
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n>>=1
    return z
def inv(a):
    assert a
    return power(a,62)
def div(a,b):return mul(a,inv(b))
def dot(a,b):
    z=0
    for x,y in zip(a,b):z^=mul(x,y)
    return z
def neg(P):return None if P is None else (P[0],P[1]^1)
def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u:
        if y!=v:return None
        lam=mul(x,x)
    else:lam=div(y^v,x^u)
    nu=y^mul(lam,x);r=mul(lam,lam)^x^u
    return r,mul(lam,r)^nu^1
def scalar(n,P):
    out=None
    while n:
        if n&1:out=add(out,P)
        P=add(P,P);n>>=1
    return out
def rows_reduce(rows,cols):
    rows=[list(r) for r in rows];piv=[]
    for j in range(cols):
        a=next((a for a in range(len(piv),len(rows)) if rows[a][j]),None)
        if a is None:continue
        i=len(piv);rows[a],rows[i]=rows[i],rows[a]
        z=inv(rows[i][j]);rows[i]=[mul(z,v) for v in rows[i]]
        for a in range(len(rows)):
            if a!=i and rows[a][j]:
                z=rows[a][j];rows[a]=[x^mul(z,y) for x,y in zip(rows[a],rows[i])]
        piv.append(j)
    return rows,piv
def nullspace(rows,n):
    R,piv=rows_reduce(rows,n);free=[j for j in range(n) if j not in piv]
    out=[]
    for j in free:
        v=[0]*n;v[j]=1
        for i,p in enumerate(piv):v[p]=R[i][j]
        out.append(v)
    return out
def solve(A,b):
    R,piv=rows_reduce([r+[v] for r,v in zip(A,b)],len(A[0]))
    if any(not any(r[:-1]) and r[-1] for r in R):return None,piv
    x=[0]*len(A[0])
    for i,p in enumerate(piv):x[p]=R[i][-1]
    return x,piv
def point_values(P):return [1,P[0],P[1]]
def point_derivative(P):return [0,1,mul(P[0],P[0])]
def tensor(a,b):return [mul(x,y) for x in a for y in b]
def evaluate(s,P):return dot(s,tensor(point_values(P[0]),point_values(P[1])))
def gradient(s,P):return [dot(s,tensor(point_derivative(P[0]),point_values(P[1]))),dot(s,tensor(point_values(P[0]),point_derivative(P[1])))]
def cartier(s):
    # C(1*x)=1, C(1*y)=x, C(x*y)=y; every diagonal product is killed.
    table={(0,1):0,(1,0):0,(0,2):1,(2,0):1,(1,2):2,(2,1):2}
    A=[[0]*9 for _ in range(9)]
    for a,b,u,v in itertools.product(range(3),repeat=4):
        if (a,u) in table and (b,v) in table:
            i=3*table[a,u]+table[b,v];j=3*u+v
            A[i][j]^=s[3*a+b]
    return A
def determinant3(s):
    z=0
    for p in itertools.permutations(range(3)):
        z^=mul(mul(s[p[0]],s[3+p[1]]),s[6+p[2]])
    return z
def hasse_cubic(s):return dot([mul(x,x) for x in s],list(reversed(s)))
def second_coefficient(s,P,velocity):
    jets=[]
    for (x,y),v in zip(P,velocity):
        v2=mul(v,v);x2=mul(x,x);a2=x^mul(x2,x2)
        jets.append([[1,0,0],[x,v,0],[y,mul(x2,v),mul(a2,v2)]])
    answer=0
    for i,j in itertools.product(range(3),repeat=2):
        a,b=jets[0][i],jets[1][j]
        term=mul(a[0],b[2])^mul(a[1],b[1])^mul(a[2],b[0])
        answer^=mul(s[3*i+j],term)
    return answer
def translation_second(P,g):
    if g is None:return 0
    x,y=P;u,v=g;den=x^u
    assert den
    slope1=div(mul(mul(x,x),den)^y^v,mul(den,den))
    return mul(slope1,slope1)

def main():
    run_index=int(sys.argv[1]) if len(sys.argv)>1 else 3
    seed=202611191117+run_index-1
    started=time.perf_counter();rng=random.Random(seed)
    assert all(mul(a,inv(a))==1 for a in range(1,64))
    omega=next(a for a in range(2,64) if mul(a,a)^a^1==0)
    points=[(x,y) for x,y in itertools.product(range(64),repeat=2) if mul(y,y)^y==mul(mul(x,x),x)]+[None]
    assert len(points)==81
    def automorphism(P):return None if P is None else (P[0]^1,P[1]^P[0]^omega)
    def bmap(P):return add(P,automorphism(P))
    torsion=[P for P in points if scalar(3,P) is None]
    assert len(torsion)==9
    kernel=[(neg(bmap(P)),P) for P in torsion]
    P0=(0,0);P1=(1,omega)
    G=(neg(bmap(P0)),P0);H=(neg(bmap(P1)),P1)
    assert G==((omega,mul(omega,omega)),(0,0))
    assert H==((mul(omega,omega),mul(omega,omega)),(1,omega))
    multiplication=[[mul(a,b) for b in range(64)] for a in range(64)]
    def projective_values(P):return [0,0,1] if P is None else point_values(P)
    remaining=set(itertools.product(points,repeat=2));orbits=[]
    while remaining:
        base=min(remaining,key=lambda P:tuple((-1,-1) if x is None else x for x in P))
        orbit=[tuple(add(base[i],g[i]) for i in range(2)) for g in kernel]
        assert len(set(orbit))==9
        remaining.difference_update(orbit)
        orbits.append([(P,tensor(*map(projective_values,P))) for P in orbit])
    assert len(orbits)==729
    def rational_triple(s):
        for orbit in orbits:
            zeros=[]
            for P,vals in orbit:
                z=0
                for a,b in zip(s,vals):z^=multiplication[a][b]
                if z==0:zeros.append(P)
                if len(zeros)==3:return zeros
        return None
    choices=[P for P in points if P is not None and scalar(3,P) is not None]
    trials=[];found=None
    for base_attempt in range(1,21):
        P=(rng.choice(choices),rng.choice(choices));Q=tuple(add(P[i],G[i]) for i in range(2))
        if any(Q[i] is None or P[i][0]==G[i][0] for i in range(2)):continue
        valsP=tensor(*map(point_values,P));valsQ=tensor(*map(point_values,Q))
        dp=[tensor(point_derivative(P[0]),point_values(P[1])),tensor(point_values(P[0]),point_derivative(P[1]))]
        dq=[tensor(point_derivative(Q[0]),point_values(Q[1])),tensor(point_values(Q[0]),point_derivative(Q[1]))]
        equations=[valsP,valsQ]+[[a^b for a,b in zip(x,y)] for x,y in zip(dp,dq)]
        N=nullspace(equations,9)
        for attempt in range(1,10001):
            c=[rng.randrange(64) for _ in N]
            s=[dot(c,[row[j] for row in N]) for j in range(9)]
            q=hasse_cubic(s);det=determinant3(s)
            if q or not det:continue
            u,piv=solve(cartier(s),[mul(x,x) for x in s])
            assert u is not None and len(piv)==8
            grad=gradient(s,P);gradQ=gradient(s,Q)
            assert evaluate(s,P)==evaluate(s,Q)==0 and grad==gradQ
            if not any(grad):continue
            eta=evaluate(u,P)^evaluate(u,Q)
            velocity=[grad[1],grad[0]]
            second=second_coefficient(s,Q,velocity)^second_coefficient(s,P,velocity)
            second^=dot(gradQ,[mul(translation_second(P[i],G[i]),mul(velocity[i],velocity[i])) for i in range(2)])
            rec=dict(base_attempt=base_attempt,attempt=attempt,P=P,Q=Q,coefficients=s,
                     determinant=det,Cartier_rank=8,Cartier_kernel_lift=u,
                     gradient=grad,eta_difference=eta,tacnode_second_difference=second)
            trials.append(rec)
            if eta and second:
                triple=rational_triple(s)
                rec['rational_triple_screen']=triple
                if triple is not None:continue
                found=rec;break
        if found:break
    result=dict(status='CANDIDATE_FOUND' if found else 'NO_CANDIDATE_WITHIN_BUDGET',
       field_modulus_binary=MOD,omega=omega,curve_point_count=len(points),
       tensor_basis='(1,x,y) tensor (1,x,y); index3*i+j',
       Hasse_cubic='sum_i s_i^2 s_(8-i), not sum_i s_i^3 in this basis',
       G=G,H=H,kernel=kernel,seed=seed,run_index=run_index,
       budget='20 base pairs,10000 sections per base pair; exact GF64 triple orbit screening is rejection only',
       all_Hasse_contact_candidates=trials,candidate=found,
       rational_triple_orbit_count=729,
       global_smoothness_checked=False,unwanted_kernel_collisions_checked=False,
       elapsed_seconds=time.perf_counter()-started)
    path=Path(__file__).resolve().parents[1]/f'outputs/ss_contact_witness_{run_index:02d}.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
