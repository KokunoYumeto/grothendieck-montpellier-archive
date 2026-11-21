#!/usr/bin/env python3
"""G-023: exact coefficient, literal positive polytopes, and lazy witnesses.

Only Python's standard library is needed.  No input-dependent character
calculation or precomputed external table is used.
"""
from functools import lru_cache
from math import comb
import argparse
import json

LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
SIZES=(1,10,15,20,20,30,24)
CHARS=((1,1,1,1,1,1,1),(4,2,0,1,-1,0,-1),
       (5,1,1,-1,1,-1,0),(6,0,-2,0,0,0,1),
       (5,-1,1,-1,-1,1,0),(4,-2,0,1,1,0,-1),
       (1,-1,1,1,-1,-1,1))
IDENTITY_NEWTON=(1,23,172,550,850,630,180)

def transpose(lam):
    return tuple(sum(v>=j for v in lam) for j in range(1,max(lam,default=0)+1))

def validate(r,d,outer):
    if any(type(v) is not int or v<0 for v in (r,d)):
        raise ValueError('r and d must be nonnegative integers')
    outer=tuple(outer)
    if any(type(v) is not int for v in outer) or outer not in LABELS:
        raise ValueError('outer must be a partition of five')
    return LABELS.index(transpose(outer) if d%2 else outer)

def trace(g,r):
    if g==0:return sum(v*comb(r,j) for j,v in enumerate(IDENTITY_NEWTON))
    if g==1:
        h,s=divmod(r,2)
        return 0 if s else (h+1)**3+h**3
    if g==2:
        h,s=divmod(r,2)
        return 0 if s else 3*h*h+3*h+1
    if g==3:
        h,s=divmod(r,3)
        return h+1 if s==0 else (-h if s==1 else 0)
    if g==4:return (1,0,0,0,-1,0)[r%6]
    if g==5:return (1,0,-1,0)[r%4]
    if g==6:return (1,-1,-1,1,0)[r%5]
    raise ValueError('class index must lie between zero and six')

@lru_cache(None)
def constants(label,residue):
    values=[]
    for q in range(7):
        value=sum(SIZES[g]*CHARS[label][g]*trace(g,residue+60*q) for g in range(7))
        if value%120:raise ArithmeticError('nonintegral fixed constant')
        values.append(value//120)
    answer=[]
    while values:
        answer.append(values[0])
        values=[b-a for a,b in zip(values,values[1:])]
    if any(v<0 for v in answer):raise ArithmeticError('negative fixed constant')
    return tuple(answer)

def coefficient(r,d=0,outer=(5,)):
    label=validate(r,d,outer)
    q,residue=divmod(r,60)
    return sum(c*comb(q,j) for j,c in enumerate(constants(label,residue)))

def polytopes(r,d=0,outer=(5,),all_residues=False):
    label=validate(r,d,outer)
    answer=[]
    for residue in range(60) if all_residues else (r%60,):
        for j,c in enumerate(constants(label,residue)):
            if not c:continue
            names=['q','y']+[f'z{i+1}' for i in range(j)]
            size=len(names);ineq=[]
            for index in (0,1):
                row=[0]*size;row[index]=-1;ineq.append([row,0])
            row=[0]*size;row[1]=1;ineq.append([row,c-1])
            if j:
                row=[0]*size;row[2]=-1;ineq.append([row,0])
                for index in range(2,size-1):
                    row=[0]*size;row[index]=1;row[index+1]=-1;ineq.append([row,-1])
                row=[0]*size;row[-1]=1;row[0]=-1;ineq.append([row,-1])
            equality=[0]*size;equality[0]=60
            answer.append({'residue':residue,'order':j,'constant':c,
                           'variables':names,'equalities':[[equality,r-residue]],
                           'inequalities':ineq})
    return answer

def increasing_subsets(q,j):
    """Lexicographic subsets without materializing range(q), even for huge q."""
    if q<j:return
    if j==0:
        yield ();return
    values=list(range(j))
    while True:
        yield tuple(values)
        index=j-1
        while index>=0 and values[index]==q-j+index:index-=1
        if index<0:return
        values[index]+=1
        for i in range(index+1,j):values[i]=values[i-1]+1

def witnesses(r,d=0,outer=(5,),limit=10):
    label=validate(r,d,outer)
    if type(limit) is not int or limit<0:raise ValueError('limit must be a nonnegative integer')
    q,residue=divmod(r,60);produced=0
    if not limit:return
    for j,c in enumerate(constants(label,residue)):
        if not c:continue
        for subset in increasing_subsets(q,j):
            y=0
            while y<c:
                yield {'residue':residue,'order':j,'coordinates':(q,y)+subset}
                produced+=1
                if produced>=limit:return
                y+=1

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--r',type=int,required=True)
    parser.add_argument('--d',type=int,default=0)
    parser.add_argument('--outer',default='5')
    parser.add_argument('--polytopes',action='store_true')
    parser.add_argument('--all-residues',action='store_true')
    parser.add_argument('--witness-limit',type=int,default=0)
    args=parser.parse_args();outer=tuple(map(int,args.outer.split(',')))
    result={'r':args.r,'d':args.d,'outer':outer,'inner':args.d+2*args.r,
            'output':[args.d+(4-i)*args.r for i in range(5)],
            'coefficient':coefficient(args.r,args.d,outer)}
    if args.polytopes:result['polytopes']=polytopes(args.r,args.d,outer,args.all_residues)
    if args.witness_limit:result['witnesses']=list(witnesses(args.r,args.d,outer,args.witness_limit))
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
