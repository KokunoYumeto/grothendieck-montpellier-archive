#!/usr/bin/env python3
"""T043: fixed positive formula for all hook quotient powers at twist2k."""
from pathlib import Path
from math import comb
import argparse,json
HERE=Path(__file__).resolve().parent
TABLE=json.loads((HERE/'HOOK_ALL_POWERS_TABLE.json').read_text())['labels']

def transpose(lam):return tuple(sum(x>=j for x in lam) for j in range(1,max(lam,default=0)+1))

def label(a,k,d,mu):
    if any(type(v) is not int for v in (a,k,d)) or a<1 or min(k,d)<0:
        raise ValueError('a must be positive; k,d must be nonnegative')
    mu=tuple(mu)
    if any(type(v) is not int for v in mu) or ','.join(map(str,mu)) not in TABLE:
        raise ValueError('outer must be a partition of five')
    nu=transpose(mu) if (a+d)%2 else mu
    return ','.join(map(str,nu))

def coefficient(a,k,d,mu):
    nu=label(a,k,d,mu);q,r=divmod(a-1,60);p,s=divmod(k,60)
    constants=TABLE[nu][r][s]
    return sum(constants[4*i+j]*comb(q,i)*comb(p,j) for i in range(4) for j in range(4)
               if i<=q and j<=p and constants[4*i+j])

def polytopes(a,k,d,mu,all_residues=False):
    nu=label(a,k,d,mu)
    residues=((r,s) for r in range(60) for s in range(60)) if all_residues else (((a-1)%60,k%60),)
    answer=[]
    for r,s in residues:
        for i in range(4):
            for j in range(4):
                c=TABLE[nu][r][s][4*i+j]
                if not c:continue
                variables=['q','p','z']+[f'x{h}' for h in range(1,i+1)]+[f'y{h}' for h in range(1,j+1)]
                size=len(variables);assert size<=8
                inequalities=[]
                for h in (0,1,2):
                    row=[0]*size;row[h]=-1;inequalities.append((row,0))
                row=[0]*size;row[2]=1;inequalities.append((row,c-1))
                for start,length,upper in ((3,i,0),(3+i,j,1)):
                    if not length:continue
                    row=[0]*size;row[start]=-1;inequalities.append((row,-1))
                    for h in range(length-1):
                        row=[0]*size;row[start+h]=1;row[start+h+1]=-1;inequalities.append((row,-1))
                    row=[0]*size;row[start+length-1]=1;row[upper]=-1;inequalities.append((row,0))
                eq1=[0]*size;eq1[0]=60;eq2=[0]*size;eq2[1]=60
                answer.append(dict(residues=[r,s],orders=[i,j],constant=c,variables=variables,
                                   equalities=[(eq1,a-1-r),(eq2,k-s)],inequalities=inequalities))
    assert len(answer)<=54000
    return answer

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('a','k','d'):parser.add_argument('--'+name,required=True,type=int)
    parser.add_argument('--outer',default='5')
    parser.add_argument('--polytopes',action='store_true')
    args=parser.parse_args();a,k,d=args.a,args.k,args.d;mu=tuple(map(int,args.outer.split(',')))
    result=dict(a=a,k=k,d=d,outer=list(mu),inner=d+a+k,
                output=[d+2*a+3*k+1,d+a+2*k,d+a,d+a-1,d],coefficient=coefficient(a,k,d,mu))
    if args.polytopes:result['polytopes']=polytopes(a,k,d,mu)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
