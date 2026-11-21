#!/usr/bin/env python3
"""T040: positive fixed-polytope formula for the Q(2k+1) family."""
from pathlib import Path
from math import comb
import argparse,json

HERE=Path(__file__).resolve().parent
TABLE=json.loads((HERE/'Q_PLUS_NEWTON_TABLE.json').read_text())['labels']

def transpose(lam):
    return tuple(sum(x>=j for x in lam) for j in range(1,max(lam,default=0)+1))

def validate(k,d,mu):
    if type(k) is not int or type(d) is not int or min(k,d)<0:
        raise ValueError('k and d must be nonnegative integers')
    mu=tuple(mu)
    if any(type(x) is not int for x in mu) or ','.join(map(str,mu)) not in TABLE:
        raise ValueError('outer must be a partition of five')
    return mu

def coefficient(k,d,mu):
    mu=validate(k,d,mu)
    nu=transpose(mu) if (d+1)%2 else mu
    q,r=divmod(k,60)
    coefficients=TABLE[','.join(map(str,nu))][r]
    return sum(c*comb(q,j) for j,c in enumerate(coefficients) if j<=q)

def polytopes(k,d,mu,all_residues=False):
    mu=validate(k,d,mu)
    nu=transpose(mu) if (d+1)%2 else mu
    rows=TABLE[','.join(map(str,nu))]
    residues=range(60) if all_residues else (k%60,)
    result=[]
    for r in residues:
        for j,c in enumerate(rows[r]):
            if not c:continue
            variables=['q','z']+[f'x{i}' for i in range(1,j+1)]
            size=2+j
            inequalities=[]
            row=[0]*size;row[0]=-1;inequalities.append((row,0))
            row=[0]*size;row[1]=-1;inequalities.append((row,0))
            row=[0]*size;row[1]=1;inequalities.append((row,c-1))
            if j:
                row=[0]*size;row[2]=-1;inequalities.append((row,-1))
                for i in range(j-1):
                    row=[0]*size;row[2+i]=1;row[3+i]=-1
                    inequalities.append((row,-1))
                row=[0]*size;row[-1]=1;row[0]=-1;inequalities.append((row,0))
            equality=[0]*size;equality[0]=60
            result.append(dict(residue=r,newton_order=j,constant=c,
                               variables=variables,equality=(equality,k-r),
                               inequalities=inequalities))
    assert len(result)<=240 and all(len(p['variables'])<=5 for p in result)
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--k',type=int,required=True)
    parser.add_argument('--d',type=int,required=True)
    parser.add_argument('--outer',default='5')
    parser.add_argument('--polytopes',action='store_true')
    parser.add_argument('--all-residues',action='store_true')
    args=parser.parse_args()
    mu=tuple(map(int,args.outer.split(',')))
    k,d=args.k,args.d
    result=dict(k=k,d=d,outer=list(mu),inner=d+k+2,
                output=[d+3*k+6,d+2*k+2,d+1,d+1,d],
                coefficient=coefficient(k,d,mu))
    if args.polytopes:result['polytopes']=polytopes(k,d,mu,args.all_residues)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
