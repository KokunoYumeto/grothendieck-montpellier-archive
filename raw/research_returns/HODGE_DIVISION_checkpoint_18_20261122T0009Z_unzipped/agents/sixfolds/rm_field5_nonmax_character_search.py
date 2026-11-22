#!/usr/bin/env python3
"""Exact rank25 character test after a nonmaximal-at5 isogeny.

Only necessary integral characters are tested; there is no object or action
construction.  The mod5 candidates have the prescribed rank2 row/column
spaces, and all their first lifts are checked by exact linear algebra.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,time
import rm_integral_character_search as ex

start=time.monotonic();p=5;r=25
U=[[1,2,0,0],[2,-1,0,0],[0,0,1,2],[0,0,2,-1]]
theta=ex.hermitian_real([[int(i==j)for j in range(4)]for i in range(4)])
eta=ex.hermitian_real(U)
R=[[int(i==j)for j in range(8)]for i in range(8)]
for j in (0,2):
    R[2*j][2*j]=2;R[2*j][2*j+1]=-1
    R[2*j+1][2*j]=1;R[2*j+1][2*j+1]=2
def pull(A):
    return [[sum(R[k][i]*A[k][ell]*R[ell][j]for k in range(8)for ell in range(8))
             for j in range(8)]for i in range(8)]
theta=pull(theta);eta=pull(eta)
assert ex.pf(theta,tuple(range(8)))==25
pt=ex.divpow(theta,2);pe=ex.divpow(eta,2)
t={m:F(pt[m],10)+F(pe[m],50)for m in ex.M4}
assert ex.wedge(t,t).get(255)==2
rhs=[r*t[m]for m in ex.M4];assert all(x.denominator==1 for x in rhs)
rhs=list(map(int,rhs))
P=[[0,0],[1,0],[0,0],[0,1]]
Q=[[3,0],[4,0],[0,3],[0,4]]
inconsistency_witnesses=[]

def solve(columns,target):
    piv={};null=[]
    for j,col in enumerate(columns):
        v=[x%p for x in col];word=[int(j==i)for i in range(16)]
        for row in sorted(piv):
            if v[row]:
                c=v[row];vv,ww=piv[row]
                v=[(a-c*b)%p for a,b in zip(v,vv)]
                word=[(a-c*b)%p for a,b in zip(word,ww)]
        row=next((i for i,x in enumerate(v)if x),None)
        if row is None:null.append(word);continue
        inv=pow(v[row],-1,p)
        piv[row]=([x*inv%p for x in v],[x*inv%p for x in word])
    v=[x%p for x in target];word=[0]*16
    for row in sorted(piv):
        if v[row]:
            c=v[row];vv,ww=piv[row]
            v=[(a-c*b)%p for a,b in zip(v,vv)]
            word=[(a+c*b)%p for a,b in zip(word,ww)]
    if any(v):
        row=next(i for i,x in enumerate(v)if x)
        lam=[int(i==row)for i in range(len(v))]
        for pivot in reversed(sorted(piv)):
            vv,_=piv[pivot]
            dot=sum(a*b for a,b in zip(lam,vv))%p
            lam[pivot]=(lam[pivot]-dot)%p
        assert all(sum(a*b for a,b in zip(lam,col))%p==0 for col in columns)
        pairing=sum(a*b for a,b in zip(lam,target))%p
        assert pairing!=0
        inconsistency_witnesses.append({'annihilator':lam,'target_pairing':pairing})
        return None
    return word,null

tested=0;base_pass=0;liftable=0;lift_count=0;found=[];den_stats={};kernel_stats={}
for a,b,c,d in product(range(5),repeat=4):
    if (a*d-b*c)%5!=3:continue
    tested+=1;K=[[a,b],[c,d]]
    M=[[sum(P[i][s]*K[s][u]*Q[j][u]for s in range(2)for u in range(2))%5
        for j in range(4)]for i in range(4)]
    coeff=[M[i][i]for i in range(4)]
    for i,j in ex.combinations(range(4),2):
        coeff.extend([3*(M[i][j]+M[j][i])%5,4*(M[i][j]-M[j][i])%5])
    A=ex.from_coeff(coeff);pa=ex.divpow(A,2)
    diff=[rhs[i]-pa[m]for i,m in enumerate(ex.M4)]
    if any(x%5 for x in diff):continue
    base_pass+=1
    columns=[]
    for basis in ex.basis:
        w=ex.wedge(ex.divpow(A,1),ex.divpow(basis,1))
        columns.append([int(w.get(m,0))%5 for m in ex.M4])
    sol=solve(columns,[x//5 for x in diff])
    if sol is None:continue
    liftable+=1;z0,null=sol;kernel_stats[len(null)]=kernel_stats.get(len(null),0)+1
    for lambdas in product(range(5),repeat=len(null)):
        z=[(z0[i]+sum(lam*v[i]for lam,v in zip(lambdas,null)))%5 for i in range(16)]
        cc=[x+5*y for x,y in zip(coeff,z)];AA=ex.from_coeff(cc);pp=ex.divpow(AA,2)
        assert all((F(pp[m],25)-t[m]).denominator==1 for m in ex.M4)
        lift_count+=1
        p3=ex.divpow(AA,3);at=ex.wedge(ex.divpow(AA,1),t)
        den=sorted({(F(p3[ex.mask(ix)],625)-F(at.get(ex.mask(ix),0),25)).denominator for ix in ex.I6})
        key=','.join(map(str,den));den_stats[key]=den_stats.get(key,0)+1
        if den!=[1]:continue
        result=ex.candidate(25,cc,t,4)
        if result:
            found.append(result)
            print('FOUND_NECESSARY_INTEGRAL_CHARACTER',json.dumps(result),flush=True)
out={'status':'EXACT FIXED-RANK NECESSARY CHARACTER TEST','field_radicand':5,
     'rank':25,'polarization_product':25,'r_times_q':'1/5','self_Euler':4,
     'pull_real_matrix':R,'mod5_candidates':tested,'mod5_passes':base_pass,
     'liftable_mod5_candidates':liftable,'kernel_dimensions':kernel_stats,
     'exact_inconsistency_witnesses':inconsistency_witnesses,
     'ch2_integral_lifts':lift_count,'ch3_denominator_distributions':den_stats,
     'integral_full_characters':found,'elapsed_seconds':time.monotonic()-start,
     'actual_object_constructed':False,'all_rank_obstruction_claimed':False}
Path(__file__).with_name('rm_field5_nonmax_character_search_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in ('integral_full_characters','exact_inconsistency_witnesses','pull_real_matrix')},indent=2))
