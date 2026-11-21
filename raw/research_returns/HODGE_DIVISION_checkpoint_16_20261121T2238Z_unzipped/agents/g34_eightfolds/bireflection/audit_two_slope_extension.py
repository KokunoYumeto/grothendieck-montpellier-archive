#!/usr/bin/env python3
"""Independent exact arithmetic audit of SF-E826.

Imports no author's arithmetic or selected capacities/tree output.  Reads the
eight rational orbit weights, and the actual tree printed in the proof.
The all-size brick and categorical arguments remain written proof checks.
"""
from pathlib import Path
from fractions import Fraction as F
from math import lcm
from functools import reduce
from collections import Counter
import re, json, hashlib, time

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent.parent / 'sixfolds'
INPUT = AUTHOR / 'rm_two_slope_exact_input.json'
PROOF = AUTHOR / 'rm_two_slope_extension_obstruction_draft.md'

# Q(sqrt(2)), independently represented by pairs of rational coefficients.
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,t): return (x[0]*t,x[1]*t)
def eig(v):
    a,b,c,d=v
    return [(F(a+c),F(b+d)),(F(a-c),F(b-d)),
            (F(a+c),F(-b-d)),(F(a-c),F(-b+d))]
def full_char(v):
    out=[]; z=eig(v)
    for mask in range(16):
        p=(F(1),F(0))
        for k in range(4):
            if mask & (1<<k):p=mul(p,z[k])
        out.append(p)
    return out
def inertia(v):
    # Exact inertia of the two real symmetric Gaussian blocks, by determinant
    # and trace; no rounded roots or the author's index routine.
    a,b,c,d=v; neg=0; det=1
    for x,y in ((a+c,b+d),(a-c,b-d)):
        dd=x*x-2*y*y
        if dd==0:return None,0
        det *= dd
        if dd<0:neg+=1
        elif x<0:neg+=2
        else:assert x>0
    return neg,abs(det)
def ceil_rat(q):return -((-q.numerator)//q.denominator)

def rank_mod(A, p=1009):
    A=[[v%p for v in row] for row in A]
    if not A:return 0
    row=0
    for col in range(len(A[0])):
        pivot=next((i for i in range(row,len(A)) if A[i][col]),None)
        if pivot is None:continue
        A[row],A[pivot]=A[pivot],A[row]
        inv=pow(A[row][col],-1,p)
        A[row]=[(x*inv)%p for x in A[row]]
        for i in range(row+1,len(A)):
            t=A[i][col]
            if t:A[i]=[(x-t*y)%p for x,y in zip(A[i],A[row])]
        row+=1
        if row==len(A):break
    return row

def product(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def brick(n,m):
    # Independently construct a cover by full coordinate windows, then add
    # the two endpoint-window Jordan products as in the universal proof.
    if n<m:return [list(map(list,zip(*A))) for A in brick(m,n)]
    k=(n+m-1)//m
    starts=[min(j*m,n-m) for j in range(k)]
    windows=[[[int(i==s+j) for j in range(m)] for i in range(n)] for s in starts]
    J=[[int(j==i+1) for j in range(m)] for i in range(m)]
    JT=list(map(list,zip(*J)))
    return windows+[product(windows[0],J),product(windows[0],JT)]

def wedge(x,y):
    z={}
    for I,a in x.items():
        for J,b in y.items():
            if I&J:continue
            inversions=sum(1 for i in range(8) for j in range(8)
                           if I>>i&1 and J>>j&1 and i>j)
            z[I|J]=z.get(I|J,0)+(-1)**inversions*a*b
    return {I:a for I,a in z.items() if a}
def wedge_rank(omega):
    source=[(1<<i)|(1<<j) for i in range(8) for j in range(i+1,8)]
    images=[wedge({I:1},omega) for I in source]
    target=sorted(set().union(*(set(im) for im in images)))
    return rank_mod([[im.get(J,0) for im in images] for J in target])

def main():
    started=time.perf_counter(); data=json.loads(INPUT.read_text()); proof=PROOF.read_text()
    weights={}; printed_multiplicities=[]
    for item in data['exact_support']:
        a,b,c,d=item['rep']; w=F(item['orbit_total_weight'])
        orbit={(a,b,c,d),(a,-b,c,-d),(a,b,-c,-d),(a,-b,-c,d)}
        assert len(orbit)==4 and w>0
        for v in orbit:
            assert v not in weights
            weights[v]=w/4
    assert len(weights)==32
    r=reduce(lcm,(w.denominator for w in weights.values()),1)
    assert r==341355757056
    for row in re.findall(r'^\|\(([-0-9, ]+)\)\|([^|]+)\|([0-9]+)\|$',proof,re.M):
        v=tuple(map(int,row[0].split(',')))
        assert F(row[1].strip())==4*weights[v]
        assert int(row[2])==r*weights[v]
        printed_multiplicities.append(int(row[2]))
    # Whitespace after each Markdown table separator is allowed.
    if not printed_multiplicities:
        for line in proof.splitlines():
            if not line.startswith('|('):continue
            cells=[x.strip() for x in line.strip('|').split('|')]
            v=tuple(map(int,cells[0].strip('()').split(',')))
            assert F(cells[1])==4*weights[v]
            assert int(cells[2])==r*weights[v]
            printed_multiplicities.append(int(cells[2]))
    assert len(printed_multiplicities)==8
    free=[(F(0),F(0)) for _ in range(16)]
    for v,w in weights.items():free=[add(x,scale(y,w)) for x,y in zip(free,full_char(v))]
    unit=[add(add(scale(x,2),scale(y,-2)),z) for x,y,z in
          zip(full_char((10,0,0,0)),full_char((2,0,0,0)),full_char((-2,0,0,0)))]
    target=[F(0)]*16;target[0]=32;target[3]=target[12]=-16;target[15]=8
    assert [add(x,y) for x,y in zip(free,unit)]==[(v,F(0)) for v in target]
    assert [free[k][0] for k in (0,1,3,5,9,7,15)]==list(map(F,(31,-14,-212,-196,-196,-1976,-19976)))
    A=[None]+sorted(v for v in weights if v[0]==14)
    B=sorted(v for v in weights if v[0]==-14)
    aw=[F(1)]+[weights[v] for v in A[1:]]; bw=[weights[v] for v in B]
    assert sum(aw)==sum(bw)==16
    hist=Counter();caps={};unit_data=[]
    for i,a in enumerate(A):
        for j,b in enumerate(B):
            if a is not None:
                idx,dim=inertia(tuple(x-y for x,y in zip(a,b)))
                assert idx is not None and idx<=2
                hist[idx]+=1;cap=dim if idx==1 else 0
            else:
                terms=[]
                for twist in (10,2,-2):
                    terms.append(inertia((twist-b[0],-b[1],-b[2],-b[3])))
                assert terms[0][0] is not None and terms[0][0]<=2 and 2-b[0]>0
                cap=max(0,2*(terms[0][1]-terms[1][1])) if all(t[0]==1 for t in terms) else 0
                unit_data.append({'B':j,'indices':[t[0] for t in terms],
                                  'line_dimensions':[t[1] for t in terms],'Ext1_lower_bound':cap})
            need=ceil_rat(max(aw[i]/bw[j],bw[j]/aw[i]))+2
            if cap>=need:caps[i,j]=(need,cap)
    assert hist=={0:36,1:144,2:60}
    assert len(caps)==148
    unit_positive=[x for x in unit_data if x['Ext1_lower_bound']]
    assert [x['B'] for x in unit_positive]==[0,3,16,19]
    assert all(x['line_dimensions']==[4718592,3174400,2467584] and
               x['Ext1_lower_bound']==3088384 for x in unit_positive)
    # Validate exactly the tree printed in the proof, not a separately generated
    # graph or the author's saved spanning-tree output.
    tree=[]
    for line in proof.splitlines():
        if re.fullmatch(r'\|[0-9]+\|[0-9]+\|[0-9]+\|[0-9]+\|',line):
            i,j,need,cap=map(int,line.strip('|').split('|'))
            assert caps[i,j]==(need,cap)
            tree.append((i,13+j))
    assert len(tree)==32
    parent=list(range(33))
    def find(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]];v=parent[v]
        return v
    for v,w in tree:
        v,w=find(v),find(w);assert v!=w;parent[v]=w
    assert len({find(v) for v in range(33)})==1
    matrix_cases=[]
    for n in range(1,7):
        for m in range(1,7):
            arrows=brick(n,m); cols=n*n+m*m; equations=[]
            assert len(arrows)==ceil_rat(max(F(n,m),F(m,n)))+2
            for C in arrows:
                for i in range(n):
                    for j in range(m):
                        row=[0]*cols
                        for k in range(n):row[i*n+k]+=C[k][j]
                        for k in range(m):row[n*n+k*m+j]-=C[i][k]
                        equations.append(row)
            rank=rank_mod(equations)
            assert rank==cols-1
            matrix_cases.append({'n':n,'m':m,'rank':rank})
    op={3:1,12:1}; om={48:1,192:1}
    assert wedge_rank(wedge(op,om))==18
    assert wedge_rank({15:1})==6
    out={'result':'PASS','proof_sha256':hashlib.sha256(PROOF.read_bytes()).hexdigest(),
         'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
         'orbit_count':8,'line_classes':32,'full_character_coordinates':16,
         'defect_rank':r,'total_rank':32*r,'line_index_histogram':dict(hist),
         'unit_resolution_checks':unit_data,'qualified_edges':len(caps),
         'printed_tree_vertices':33,'printed_tree_edges':len(tree),
         'brick_cases':matrix_cases,'balanced_cap_rank':18,'line_cap_rank':6,
         'runtime_seconds':time.perf_counter()-started,
         'scope':'Independent exact reconstruction; no author code or saved capacities/tree imported. The universal LES, invariant categorical bridge, actual gluing, all-size brick construction and indecomposability are separate whole-proof checks.'}
    HERE.joinpath('audit_two_slope_extension.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('unit_resolution_checks','brick_cases')},indent=2))

if __name__=='__main__':main()
