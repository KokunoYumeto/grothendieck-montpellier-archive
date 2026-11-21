#!/usr/bin/env python3
"""T047: twelve fixed positive polytopes for the exact H1 correction."""
from itertools import combinations,product
from functools import lru_cache
import argparse,json
from five_point_positive import LABELS,transpose

THREE=((3,),(2,1),(1,1,1))
SHIFTS={(3,):(0,),(2,1):(1,2),(1,1,1):(3,)}
CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))

def strip(nu,rho,vertical):
    if any((rho[i] if i<len(rho) else 0)>(nu[i] if i<len(nu) else 0) for i in range(max(len(nu),len(rho)))):return False
    boxes=[(i,j) for i,a in enumerate(nu) for j in range((rho[i] if i<len(rho) else 0),a)]
    return len(boxes)==2 and len({v[0 if vertical else 1] for v in boxes})==2

def tags(label):
    label=tuple(label)
    if label not in LABELS:raise ValueError('label must be a partition of five')
    return [dict(sigma=sigma,tau=tau,rho=rho,shift=shift)
            for sigma,tau,rho in product((0,1),(0,1),THREE)
            if strip(label,rho,bool(sigma))
            for shift in SHIFTS[transpose(rho) if tau else rho]]

def coin23(R):
    if R<0:return 0
    last=R//3;first=R%2
    return max(0,(last-first)//2+1)

def coefficient(x,b,s,label):
    if any(type(v) is not int or v<0 for v in (x,b,s)) or s<2:
        raise ValueError('x,b>=0 ands>=2 are required')
    answer=0
    for tag in tags(label):
        sigma,tau,e=tag['sigma'],tag['tau'],tag['shift']
        for j in range(s-1):
            for u in range(min(x,s-2-j)+1):
                for v in range(min(b,s-2-j-u)+1):
                    last=s-j-u-v-2;first=(sigma-u-v-1)%2
                    pcount=max(0,(last-first)//2+1)
                    if not pcount:continue
                    for h in range(min(j,x-u+v)+1):
                        if (b-v+h)%2!=tau:continue
                        answer+=pcount*coin23(j+x-u+v-2*h-e)
    return answer

def constraints(x,b,s,tag):
    names=['j','u','v','h','p','A','B','z2','z3'];n=9
    A=[[-int(i==j) for j in range(n)] for i in range(n)];rhs=[0]*n
    def add(terms,value):
        row=[0]*n
        for i,c in terms.items():row[i]=c
        A.append(row);rhs.append(value)
    add({1:1},x);add({2:1},b);add({0:1,1:1,2:1,4:1},s-2)
    add({3:1,0:-1},0);add({3:1,1:1,2:-1},x)
    return dict(variables=names,A_ub=A,b_ub=rhs,
                A_eq=[[0,-1,-1,0,-1,2,0,0,0],[0,0,1,-1,0,0,2,0,0],[-1,1,-1,2,0,0,0,2,3]],
                b_eq=[1-tag['sigma'],b-tag['tau'],x-tag['shift']])

def witnesses(x,b,s,label):
    for tag in tags(label):
        for j in range(s-1):
            for u in range(min(x,s-2-j)+1):
                for v in range(min(b,s-2-j-u)+1):
                    for h in range(min(j,x-u+v)+1):
                        if (b-v+h)%2!=tag['tau']:continue
                        for p in range((tag['sigma']-u-v-1)%2,s-j-u-v-1,2):
                            A=(u+v+1+p-tag['sigma'])//2;B=(b-v+h-tag['tau'])//2
                            R=j+x-u+v-2*h-tag['shift']
                            for z3 in range(R%2,R//3+1,2) if R>=0 else ():
                                z2=(R-3*z3)//2
                                yield tag,(j,u,v,h,p,A,B,z2,z3)

def representative(cyc):
    perm=list(range(5));start=0
    for size in cyc:
        for j in range(size):perm[start+j]=start+(j+1)%size
        start+=size
    return tuple(perm)

def cycle_type(perm,letters):
    remaining=set(letters);lengths=[]
    while remaining:
        v=min(remaining);length=0
        while v in remaining:remaining.remove(v);length+=1;v=perm[v]
        lengths.append(length)
    return tuple(sorted(lengths,reverse=True))

def h3(cyc,n):
    if n<0:return 0
    if cyc==(1,1,1):return n+1
    if cyc==(2,1):return int(n%2==0)
    return (1,-1,0)[n%3]

@lru_cache(None)
def trace_from_fixed_pairs(x,b,s,g):
    """Independent literal induction of D.2, without its CG/Pieri count."""
    perm=representative(CLASSES[g]);answer=0
    for pair in combinations(range(5),2):
        if {perm[i] for i in pair}!=set(pair):continue
        pair_sign=1 if perm[pair[0]]==pair[0] else -1
        cyc=cycle_type(perm,set(range(5))-set(pair));complement_sign=(-1)**(3-len(cyc))
        for j in range(s-1):
            for u in range(min(x,s-2-j)+1):
                for v in range(min(b,s-2-j-u)+1):
                    R=s-j-u-v-2
                    symP=R+1 if pair_sign==1 else int(R%2==0)
                    answer+=pair_sign**(u+v+1)*symP*h3(cyc,j)*complement_sign**(b-v)*h3(cyc,x-u+v)
    return answer

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('x','b','s'):parser.add_argument('--'+name,type=int,required=True)
    parser.add_argument('--label',default='5');parser.add_argument('--polytopes',action='store_true')
    args=parser.parse_args();label=tuple(map(int,args.label.split(',')))
    answer=dict(statement='T-047 correction',x=args.x,b=args.b,s=args.s,label=label,
                coefficient=coefficient(args.x,args.b,args.s,label),tags=len(tags(label)))
    if args.polytopes:answer['polytopes']=[dict(tag,constraints=constraints(args.x,args.b,args.s,tag)) for tag in tags(label)]
    print(json.dumps(answer,indent=2))

if __name__=='__main__':main()
