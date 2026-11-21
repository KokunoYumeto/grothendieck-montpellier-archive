"""Exact finite construction checks for G-09. Not a proof for all parameters."""
from collections import defaultdict, deque
from itertools import product
from math import comb, ceil, isqrt
from fractions import Fraction
import sympy as sp
from pathlib import Path
from datetime import datetime, timezone

def monomials(v, degree):
    return [a for a in product(range(degree+1), repeat=v) if sum(a)<=degree]

def parent(a):
    a=list(a)
    i=max(i for i,x in enumerate(a) if x)
    a[i]-=1
    return tuple(a),i

def graph(m,r,h):
    Q=m//h; s0=min(h-1,m); zero=(0,)*r
    left={}; right={}; nodes=[]; edges=[]
    def add(v):
        if v not in nodes:nodes.append(v)
        return v
    for j in range(Q*h+1):add(('LZ',j))
    for j in range(Q*h):edges.append((('LZ',j),('LZ',j+1),('var',2*r)))
    for q in range(Q+1):
        for a in monomials(r,m-q*h):
            v=('LZ',q*h) if a==zero else add(('LX',q,a))
            left[q,a]=v
        for a in monomials(r,m-q*h):
            if a!=zero:
                pa,i=parent(a);edges.append((left[q,pa],left[q,a],('var',i)))
    for j in range(s0+1):add(('RZ',j))
    for j in range(1,s0+1):edges.append((('RZ',j),('RZ',j-1),('var',2*r)))
    for s in range(s0+1):
        for b in monomials(r,m-s):
            v=('RZ',s) if b==zero else add(('RY',s,b))
            right[s,b]=v
        for b in monomials(r,m-s):
            if b!=zero:
                pb,i=parent(b);edges.append((right[s,b],right[s,pb],('var',r+i)))
    for (q,a),v in left.items():
        for (s,b),w in right.items():
            e=q*h+s
            if sum(a)+sum(b)+e<=m:edges.append((v,w,('coeff',a+b+(e,))))
    indeg=dict.fromkeys(nodes,0);out=defaultdict(list)
    for u,v,label in edges:out[u].append((v,label));indeg[v]+=1
    queue=deque(v for v in nodes if indeg[v]==0);order=[]
    while queue:
        u=queue.popleft();order.append(u)
        for v,label in out[u]:
            indeg[v]-=1
            if indeg[v]==0:queue.append(v)
    assert len(order)==len(nodes)
    assert order[0]==('LZ',0) and order[-1]==('RZ',0)
    expected=sum(comb(m-q*h+r,r) for q in range(Q+1))+Q*(h-1)+sum(comb(m-s+r,r) for s in range(s0+1))
    assert len(nodes)==expected
    return order,edges

def path_check(m,r,h):
    order,edges=graph(m,r,h);out=defaultdict(list)
    for u,v,label in edges:out[u].append((v,label))
    paths=defaultdict(lambda:defaultdict(int));paths[order[0]][(None,(0,)*(2*r+1))]=1
    for u in order:
        for v,label in out[u]:
            for (c,a),mult in paths[u].items():
                if label[0]=='var':
                    b=list(a);b[label[1]]+=1;key=(c,tuple(b))
                else:
                    assert c is None
                    key=(label[1],a)
                paths[v][key]+=mult
    expected={(a,a):1 for a in monomials(2*r+1,m)}
    assert dict(paths[order[-1]])==expected
    return len(order)-1,len(expected)

def determinant_check(m,r,h,values,L):
    order,edges=graph(m,r,h);pos={v:i for i,v in enumerate(order)};size=len(order)
    A=sp.zeros(size)
    coefficients={a:(sum((i+1)*(e+1) for i,e in enumerate(a))%7)-3 for a in monomials(2*r+1,m)}
    for u,v,label in edges:
        value=values[label[1]] if label[0]=='var' else coefficients[label[1]]*L
        A[pos[u],pos[v]]+=value
    # Homogenize I-A: constants (diagonal 1 and coefficient edges) gain L.
    M=L*sp.eye(size)-A
    minor=M.minor_submatrix(size-1,0)
    got=(-1)**(size+1)*minor.det(method='domain-ge')
    q=sum(c*L**(m-sum(a))*sp.prod(values[i]**e for i,e in enumerate(a)) for a,c in coefficients.items())
    B=size-1
    expected=L**(B-m)*q
    assert got==expected
    return B,int(got)

results=[]
for r in [1,2]:
    for m in range(1,6):
        for h in range(1,m+2):
            B,count=path_check(m,r,h)
            results.append(f'PASS unique coefficient paths r={r}, m={m}, h={h}, B={B}, coefficients={count}')
for args in [(1,1,1,(1,2,3),2),(2,1,2,(-1,2,3),2),(3,1,2,(2,-1,1),0),(2,2,2,(1,2,-1,3,2),-1)]:
    B,value=determinant_check(*args)
    results.append(f'PASS exact homogenized determinant m={args[0]}, r={args[1]}, h={args[2]}, L={args[4]}, B={B}, value={value}')
text='Run timestamp: '+datetime.now(timezone.utc).isoformat()+'\n'+'\n'.join(results)+'\n'
Path('work/root/G09_purity_computation_results.txt').write_text(text)
print(text)
