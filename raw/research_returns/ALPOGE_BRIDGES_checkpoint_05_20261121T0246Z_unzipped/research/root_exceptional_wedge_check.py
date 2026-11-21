"""Exact finite root-data certificates for the F4/E8 wedge obstruction.

No floating point arithmetic or external algebra package is used. A[i][j]
means <alpha_i, alpha_j^vee>. Words list reflections in application order.
The mathematical implication from this certificate is proved in
root_exceptional_opposition.tex; an exhaustive numerical search is not that proof.
"""
from collections import deque
from fractions import Fraction
import json

DATA = {
    'F4': dict(A=[[2,-1,0,0],[-1,2,-2,0],[0,-1,2,-1],[0,0,-1,2]],
               lengths=[2,2,1,1], h=12, theta=(2,3,4,2), j=0),
    'E8': dict(A=[[2,0,-1,0,0,0,0,0],[0,2,0,-1,0,0,0,0],
                 [-1,0,2,-1,0,0,0,0],[0,-1,-1,2,-1,0,0,0],
                 [0,0,0,-1,2,-1,0,0],[0,0,0,0,-1,2,-1,0],
                 [0,0,0,0,0,-1,2,-1],[0,0,0,0,0,0,-1,2]],
               lengths=[2]*8, h=30, theta=(2,3,4,6,5,4,3,2), j=7),
}

def calculate(name, data):
    A=data['A']; lengths=data['lengths']; r=len(A); h=data['h']
    G=[[Fraction(A[i][j]*lengths[j],2) for j in range(r)] for i in range(r)]
    assert all(G[i][j]==G[j][i] for i in range(r) for j in range(r))
    simple=[tuple(int(i==j) for i in range(r)) for j in range(r)]
    def reflect(v,j):
        multiple=sum(v[i]*A[i][j] for i in range(r))
        w=list(v); w[j]-=multiple
        return tuple(w)
    def dot(v,w):
        return sum(v[i]*G[i][j]*w[j] for i in range(r) for j in range(r))
    def c(v):
        for j in reversed(range(r)):v=reflect(v,j)
        return v
    def cpow(v,n):
        for _ in range(n):v=c(v)
        return v
    def add(v,w):return tuple(a+b for a,b in zip(v,w))
    def canonical(a,b):return tuple(sorted((a,b)))
    roots=set(simple); queue=list(simple)
    for v in queue:
        for j in range(r):
            w=reflect(v,j)
            if w not in roots:roots.add(w);queue.append(w)
    assert len(roots)=={'F4':48,'E8':240}[name]
    assert all(all(x>=0 for x in v) or all(x<=0 for x in v) for v in roots)
    theta=data['theta']; j=data['j']
    other=list(theta);other[j]-=1;other=tuple(other)
    assert theta in roots and other in roots
    assert all(add(theta,alpha) not in roots for alpha in simple)
    assert all(add(other,alpha) not in roots for i,alpha in enumerate(simple) if i!=j)
    assert add(other,simple[j])==theta
    assert dot(theta,theta)==dot(other,other)==2 and dot(theta,other)==1
    assert all(cpow(v,h)==v and cpow(v,h//2)==tuple(-x for x in v) for v in simple)
    # This orbit proves that both chosen root pairs are Weyl translates of
    # the same actual highest wedge; no dimension table is required.
    origin=canonical(theta,other); words={origin:[]}; queue=deque([origin])
    while queue:
        pair=queue.popleft()
        for i in range(r):
            target=canonical(*(reflect(v,i) for v in pair))
            if target not in words:
                words[target]=words[pair]+[i+1];queue.append(target)
    # Select short certificates, rather than lexicographically negative roots.
    candidates=[]
    for d in range(1,h):
        mu_pairs=[]
        for mu in roots:
            target=canonical(mu,cpow(mu,d))
            if target in words:mu_pairs.append((len(words[target]),mu,target))
        if not mu_pairs:continue
        mu_info=min(mu_pairs)
        for pair,word in words.items():
            if d*(sum(pair[0])-sum(pair[1])) % h == 0:
                candidates.append((len(word)+mu_info[0],d,pair,mu_info[1],mu_info[2]))
    assert candidates
    _,d,pair,mu,mupair=min(candidates)
    def check_word(word,target):
        current=origin
        for i in word:current=canonical(*(reflect(v,i-1) for v in current))
        assert current==target
    check_word(words[pair],pair);check_word(words[mupair],mupair)
    output=dict(type=name,root_count=len(roots),highest_root=theta,
                other_highest_wedge_root=other,highest_simple_index=j+1,
                highest_wedge_orbit_size=len(words),coxeter_order=h,
                coxeter_half_power_minus_identity=True,power=d,
                alpha=pair[0],beta=pair[1],heights=[sum(v) for v in pair],
                coordinate_pair_word=words[pair],mu=mu,c_power_mu=cpow(mu,d),
                coxeter_pair_word=words[mupair],
                divisibility_integer=d*(sum(pair[0])-sum(pair[1]))//h,
                raising_tests_pass=True)
    return output

if __name__=='__main__':
    for name,data in DATA.items():
        print(json.dumps(calculate(name,data),sort_keys=True))
