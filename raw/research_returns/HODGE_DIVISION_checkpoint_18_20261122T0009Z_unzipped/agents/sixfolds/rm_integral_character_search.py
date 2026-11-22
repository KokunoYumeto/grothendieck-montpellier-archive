#!/usr/bin/env python3
"""Search necessary integral full characters on one explicit even RM lattice.

Exact arithmetic only.  No bundle, perfect object, finite action, or
semiregularity is constructed.  Hensel branches are bounded explicitly;
an incomplete run is never reported as a nonexistence theorem.
"""
from fractions import Fraction as F
from itertools import combinations
from math import prod
from pathlib import Path
import argparse,json,time

I2=list(combinations(range(8),2)); I4=list(combinations(range(8),4))
I6=list(combinations(range(8),6)); mask=lambda t:sum(1<<x for x in t)
M4=[mask(t) for t in I4]

def pf(A, inds):
    if not inds:return 1
    a=inds[0]; total=0
    for j in range(1,len(inds)):
        total+=(-1)**(j+1)*A[a][inds[j]]*pf(A,inds[1:j]+inds[j+1:])
    return total

def divpow(A,k):
    return {mask(t):pf(A,t) for t in combinations(range(8),2*k)}

def wedge(a,b):
    c={}
    for x,v in a.items():
        if not v:continue
        for y,w in b.items():
            if not w or x&y:continue
            inv=sum((y&((1<<i)-1)).bit_count() for i in range(8) if x>>i&1)
            z=x|y;c[z]=c.get(z,0)+(-1)**inv*v*w
    return c

def add(A,B):return [[A[i][j]+B[i][j] for j in range(8)]for i in range(8)]
def scale(A,n):return [[n*x for x in row]for row in A]
def form(entries):
    A=[[0]*8 for _ in range(8)]
    for i,j,v in entries:
        A[i][j]+=v;A[j][i]-=v
    return A

basis=[];names=[]
for i in range(4):
    basis.append(form([(2*i,2*i+1,1)]));names.append('diag'+str(i))
for i,j in combinations(range(4),2):
    basis.append(form([(2*i,2*j+1,1),(2*j,2*i+1,1)]));names.append('real'+str(i)+str(j))
    basis.append(form([(2*i,2*j,1),(2*i+1,2*j+1,1)]));names.append('imag'+str(i)+str(j))

def from_coeff(c):
    A=[[0]*8 for _ in range(8)]
    for n,B in zip(c,basis):
        if n:A=add(A,scale(B,n))
    return A

def hermitian_real(H):
    entries=[]
    for i in range(4):
        entries.append((2*i,2*i+1,H[i][i]))
        for j in range(i+1,4):
            entries.extend([(2*i,2*j+1,H[i][j]),(2*j,2*i+1,H[i][j])])
    return form(entries)

def bits(v):return sum((int(v.get(m,0))&1)<<i for i,m in enumerate(M4))
bp=[divpow(B,2) for B in basis]
bpb=[bits(v) for v in bp]
cross=[[0]*16 for _ in range(16)]
for i in range(16):
    for j in range(i):
        C=divpow(add(basis[i],basis[j]),2)
        cross[i][j]=cross[j][i]=bits({m:C[m]-bp[i][m]-bp[j][m] for m in M4})

def solve(columns,target):
    piv={};null=[]
    for j,col in enumerate(columns):
        v=col;word=1<<j
        while v:
            p=v.bit_length()-1
            if p not in piv:piv[p]=(v,word);break
            vv,ww=piv[p];v^=vv;word^=ww
        if not v:null.append(word)
    word=0;v=target
    while v:
        p=v.bit_length()-1
        if p not in piv:return None
        vv,ww=piv[p];v^=vv;word^=ww
    return word,null

def solutions(particular,null):
    yield particular
    v=particular;old=0
    for n in range(1,1<<len(null)):
        gray=n^(n>>1);j=(gray^old).bit_length()-1
        v^=null[j];old=gray;yield v

def candidate(r,c,t,self_euler):
    A=from_coeff(c);p2=divpow(A,2);p3=divpow(A,3)
    ch2={m:F(p2[m],r)-t[m] for m in M4}
    at=wedge(divpow(A,1),t)
    ch3={mask(ix):F(p3[mask(ix)],r*r)-F(at.get(mask(ix),0),r) for ix in I6}
    pt=wedge(p2,t).get(255,0)
    ch4=F(pf(A,tuple(range(8))),r**3)-pt/(r*r)+F(self_euler,4*r)
    if any(v.denominator!=1 for v in ch2.values()):return None
    if any(v.denominator!=1 for v in ch3.values()) or ch4.denominator!=1:return None
    return {'rank':r,'c1_coefficients':dict(zip(names,c)),
            'c1_matrix':A,'ch2':{str(m):int(v) for m,v in ch2.items() if v},
            'ch3':{str(m):int(v) for m,v in ch3.items() if v},
            'ch4_integral':int(ch4),'self_Euler':self_euler,
            'algebraic_K0_realization_proved':False,'actual_bundle_constructed':False,
            'finite_action_constructed':False,'semiregularity_checked':False}

def run(r,t,self_euler,limit):
    rhs=[r*t[m] for m in M4]
    if any(x.denominator!=1 for x in rhs):
        return {'rank':r,'status':'rank does not clear necessary ch2 denominators'}
    rhs=list(map(int,rhs));target=sum((v&1)<<i for i,v in enumerate(rhs))
    residues=[];active=0;value=0;old=0
    for n in range(65536):
        gray=n^(n>>1)
        if n:
            j=(gray^old).bit_length()-1
            value^=bpb[j]
            for k in range(16):
                if active>>k&1:value^=cross[j][k]
            active^=1<<j
        if value==target:residues.append(active)
        old=gray
    stats={'rank':r,'mod2_residues_checked':65536,'mod2_passes':len(residues),
           'full_ch2_lifts_checked':0,'lift_nodes_checked':0,'branch_limit':limit,
           'exhaustive':True,'integral_full_characters':[]}
    stages=r.bit_length()-1
    assert r==1<<stages
    def lift(c,level,columns):
        if stats['lift_nodes_checked']>=limit:
            stats['exhaustive']=False;return
        stats['lift_nodes_checked']+=1
        if level==stages:
            stats['full_ch2_lifts_checked']+=1
            out=candidate(r,c,t,self_euler)
            if out:stats['integral_full_characters'].append(out)
            return
        pp=divpow(from_coeff(c),2)
        vals=[rhs[i]-pp[m] for i,m in enumerate(M4)]
        assert all(v%(1<<level)==0 for v in vals)
        tar=sum(((v>>level)&1)<<i for i,v in enumerate(vals))
        sol=solve(columns,tar)
        if sol is None:return
        for z in solutions(*sol):
            lift([a+((1<<level) if z>>i&1 else 0) for i,a in enumerate(c)],level+1,columns)
            if not stats['exhaustive']:return
    for active in residues:
        c=[(active>>i)&1 for i in range(16)]
        columns=[]
        for j in range(16):
            col=0
            for k in range(16):
                if active>>k&1:col^=cross[j][k]
            columns.append(col)
        lift(c,1,columns)
        if not stats['exhaustive']:break
    return stats

def main():
    p=argparse.ArgumentParser();p.add_argument('--ranks',default='4,8')
    p.add_argument('--limit',type=int,default=100000)
    p.add_argument('--pull',default='',help='even number of elliptic positions multiplied by1+i')
    p.add_argument('--output',default='rm_integral_character_search_output.json')
    args=p.parse_args();start=time.monotonic()
    U=[[1,1,0,0],[1,-1,0,0],[0,0,1,1],[0,0,1,-1]]
    H=[[3,1,0,0],[1,1,0,0],[0,0,1,0],[0,0,0,1]]
    HU=[[sum(H[i][k]*U[k][j] for k in range(4)) for j in range(4)]for i in range(4)]
    assert HU==[list(x) for x in zip(*HU)]
    theta=hermitian_real(H);eta=hermitian_real(HU)
    assert pf(theta,tuple(range(8)))==2
    positions=[] if not args.pull else [int(x) for x in args.pull.split(',')]
    assert len(set(positions))==len(positions) and len(positions)%2==0
    R=[[int(i==j) for j in range(8)]for i in range(8)]
    for j in positions:
        assert 0<=j<4
        R[2*j][2*j]=1;R[2*j][2*j+1]=-1
        R[2*j+1][2*j]=1;R[2*j+1][2*j+1]=1
    def pull(A):
        return [[sum(R[k][i]*A[k][ell]*R[ell][j]
                     for k in range(8) for ell in range(8))
                 for j in range(8)]for i in range(8)]
    theta=pull(theta);eta=pull(eta)
    degree=1<<len(positions);root_degree=1<<(len(positions)//2)
    assert pf(theta,tuple(range(8)))==2*degree
    ptheta=divpow(theta,2);peta=divpow(eta,2)
    t={m:F(ptheta[m],4*root_degree)+F(peta[m],8*root_degree) for m in M4}
    assert wedge(t,t).get(255)==1
    results=[]
    for r in map(int,args.ranks.split(',')):
        result=run(r,t,2,args.limit);results.append(result)
        print(json.dumps({k:v for k,v in result.items() if k!='integral_full_characters'}),flush=True)
        if result.get('integral_full_characters'):
            print('INTEGRAL_CHARACTER_CANDIDATES',len(result['integral_full_characters']),flush=True)
    out={'status':'EXACT NECESSARY CHARACTER SEARCH ONLY','H':H,'U':U,
         'polarization_product':2*degree,'pull_positions':positions,'pull_degree':degree,
         'pull_real_matrix':R,'r_times_q':str(F(1,2*root_degree)),'self_Euler':2,
         't_square_integral':1,'elapsed_seconds':time.monotonic()-start,'results':results}
    Path(__file__).with_name(args.output).write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
