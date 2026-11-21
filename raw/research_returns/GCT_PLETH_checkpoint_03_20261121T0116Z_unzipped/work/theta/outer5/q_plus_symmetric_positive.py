#!/usr/bin/env python3
"""T042: fixed positive polytopes for all Sym^a Q on the odd five-point ray."""
from pathlib import Path
from math import comb
import argparse,json
HERE=Path(__file__).resolve().parent
TABLE=json.loads((HERE/'Q_PLUS_SYMMETRIC_TABLE.json').read_text())['labels']

def transpose(lam):
    return tuple(sum(x>=j for x in lam) for j in range(1,max(lam,default=0)+1))

def label(a,k,d,mu):
    if any(type(v) is not int or v<0 for v in (a,k,d)):
        raise ValueError('a,k,d must be nonnegative integers')
    mu=tuple(mu)
    if any(type(v) is not int for v in mu) or ','.join(map(str,mu)) not in TABLE:
        raise ValueError('outer must be a partition of five')
    nu=transpose(mu) if (a+d)%2 else mu
    return ','.join(map(str,nu))

def coefficient(a,k,d,mu):
    nu=label(a,k,d,mu);qa,ra=divmod(a,60);qk,rk=divmod(k,60)
    constants=TABLE[nu][ra][rk]
    return sum(constants[4*i+j]*comb(qa,i)*comb(qk,j)
               for i in range(4) for j in range(4)
               if i<=qa and j<=qk and constants[4*i+j])

def polytopes(a,k,d,mu,all_residues=False):
    nu=label(a,k,d,mu)
    residues=((ra,rk) for ra in range(60) for rk in range(60)) if all_residues else ((a%60,k%60),)
    answer=[]
    for ra,rk in residues:
        constants=TABLE[nu][ra][rk]
        for i in range(4):
            for j in range(4):
                c=constants[4*i+j]
                if not c:continue
                variables=['qa','qk','z']+[f'x{h}' for h in range(1,i+1)]+[f'y{h}' for h in range(1,j+1)]
                size=len(variables);assert size<=8
                inequalities=[]
                for index in (0,1,2):
                    row=[0]*size;row[index]=-1;inequalities.append((row,0))
                row=[0]*size;row[2]=1;inequalities.append((row,c-1))
                for start,length,upper in ((3,i,0),(3+i,j,1)):
                    if not length:continue
                    row=[0]*size;row[start]=-1;inequalities.append((row,-1))
                    for h in range(length-1):
                        row=[0]*size;row[start+h]=1;row[start+h+1]=-1;inequalities.append((row,-1))
                    row=[0]*size;row[start+length-1]=1;row[upper]=-1;inequalities.append((row,0))
                ea=[0]*size;ea[0]=60;ek=[0]*size;ek[1]=60
                answer.append(dict(residues=[ra,rk],orders=[i,j],constant=c,
                                   variables=variables,equalities=[(ea,a-ra),(ek,k-rk)],inequalities=inequalities))
    assert len(answer)<=54000
    return answer

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('a','k','d'):parser.add_argument('--'+name,required=True,type=int)
    parser.add_argument('--outer',default='5')
    parser.add_argument('--polytopes',action='store_true')
    parser.add_argument('--all-residues',action='store_true')
    args=parser.parse_args();a,k,d=args.a,args.k,args.d
    mu=tuple(map(int,args.outer.split(',')))
    result=dict(a=a,k=k,d=d,outer=list(mu),inner=d+a+k+1,
                output=[d+2*a+3*k+4,d+a+2*k+1,d+a,d+a,d],
                coefficient=coefficient(a,k,d,mu))
    if args.polytopes:result['polytopes']=polytopes(a,k,d,mu,args.all_residues)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
