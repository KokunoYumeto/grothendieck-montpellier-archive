#!/usr/bin/env python3
"""Check the rank-five contact-plus-third-value incidence at exact witnesses."""
from pathlib import Path
from time import perf_counter
import json
started=perf_counter()
MOD=0x43
def mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&64:a^=MOD
    return z
def power(a,n):
    r=1
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n>>=1
    return r
def rows_at(P):
    A=[1,*P[0]];B=[1,*P[1]]
    DA=[0,1,mul(P[0][0],P[0][0])]
    DB=[0,1,mul(P[1][0],P[1][0])]
    return [[mul(a,b) for a in AA for b in BB] for AA,BB in ((A,B),(DA,B),(A,DB))]
def dot(A,B):
    z=0
    for a,b in zip(A,B):z^=mul(a,b)
    return z
def reduce(M):
    A=[list(row) for row in M];pivots=[];r=0
    for c in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r];iv=power(A[r][c],62)
        A[r]=[mul(iv,x) for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                f=A[i][c];A[i]=[x^mul(f,y) for x,y in zip(A[i],A[r])]
        pivots.append(c);r+=1
        if r==len(A):break
    return r,pivots,A
root=Path(__file__).resolve().parent.parent
checks=[]
for name in ('collinear','noncollinear'):
    source=json.loads((root/'outputs'/('ss_tangent_triple_'+name+'.json')).read_text())
    w=source['candidate'];s=w['coefficients']
    jp,jq,jr=(rows_at(w[z]) for z in ('P','Q','R'))
    gp=[dot(jp[i],s) for i in (1,2)]
    gq=[dot(jq[i],s) for i in (1,2)]
    gr=[dot(jr[i],s) for i in (1,2)]
    tau=[gp[1],gp[0]]
    tangent=lambda J:[mul(tau[0],x)^mul(tau[1],y) for x,y in zip(J[1],J[2])]
    rows=[jp[0],jq[0],tangent(jp),tangent(jq),jr[0]]
    assert all(dot(row,s)==0 for row in rows)
    rank,pivots,reduced=reduce(rows)
    assert rank==5
    assert mul(gp[0],gq[1])^mul(gp[1],gq[0])==0
    cross=mul(gp[0],gr[1])^mul(gp[1],gr[0])
    assert cross!=0
    checks.append({'type':name,'points':[w['P'],w['Q'],w['R']],
       'source_coefficients':s,'gradients':[gp,gq,gr],
       'common_tangent_vector':tau,'five_contact_value_rows':rows,
       'rank':rank,'pivot_columns':pivots,'reduced_rows':reduced,
       'transverse_third_determinant':cross})
out={'status':'PASS','scope':'Both already globally audited witnesses belong to the main rank-five triple-contact incidence; no new global existence claim.',
     'field_modulus':MOD,'checks':checks,'elapsed_seconds':perf_counter()-started}
(root/'outputs'/'verify_ss_tangent_incidence_rank.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
