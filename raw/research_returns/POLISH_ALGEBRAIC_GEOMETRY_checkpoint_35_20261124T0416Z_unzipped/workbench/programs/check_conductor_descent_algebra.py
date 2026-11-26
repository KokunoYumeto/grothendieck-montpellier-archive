#!/usr/bin/env python3
"""Finite algebra checks supplementing the formal-depth/descent proofs.

Run: python3 workbench/programs/check_conductor_descent_algebra.py
No finite test certifies a Picard, descent, or geometric assertion.
"""
from pathlib import Path
from datetime import datetime, timezone
import json

def sparse_rank(columns, p):
    pivots = {}
    for col in columns:
        v = {i: x % p for i, x in col.items() if x % p}
        while v:
            lead = min(v)
            if lead not in pivots:
                scale = pow(v[lead], -1, p)
                pivots[lead] = {i: x * scale % p for i, x in v.items()}
                break
            scale = v[lead]
            for i, x in pivots[lead].items():
                value = (v.get(i, 0) - scale * x) % p
                if value: v[i] = value
                else: v.pop(i, None)
    return len(pivots)

def mul(a, b, length, p):
    c = [0] * length
    for i, x in enumerate(a):
        for j, y in enumerate(b[:length-i]): c[i+j] = (c[i+j] + x*y) % p
    return c

def main():
    assertions = 0; differential_cases = []; leading_cases = 0; degree_cases = 0
    for p in [2, 3, 5, 7, 11]:
        for a in range(1, 6):
            cut = p*a; N = p*(a+1); block = cut*p
            cols = []
            for i in range(N):
                for j in range(p):
                    col = {}
                    if i and i-1 < cut: col[(i-1)*p+j] = i
                    if j and i < cut: col[block+i*p+j-1] = j
                    cols.append(col)
            rank = sparse_rank(cols, p)
            # Kernel of d modulo t^(pa): pth powers plus the t^(pa) ideal.
            expected_dimension = a + p*p
            assert N*p-rank == expected_dimension; assertions += 1
            differential_cases.append(dict(p=p,a=a,matrix_columns=N*p,
                matrix_rows=2*block,rank=rank,kernel_dimension=expected_dimension))
        for a in range(1, 31):
            for c in range(1, p):
                length = a+4; g = [0]*length; g[0]=1
                g[a]=c; g[a+1]=(c+1)%p; g[a+2]=(2*c+1)%p
                inv=[0]*length;inv[0]=1
                for n in range(1,length):
                    inv[n]=-sum(g[i]*inv[n-i] for i in range(1,n+1))%p
                assert mul(g,inv,length,p)==[1]+[0]*(length-1);assertions+=1
                logarithmic=mul([i*x%p for i,x in enumerate(g)],inv,length,p)
                assert all(x==0 for x in logarithmic[:a]);assertions+=1
                assert logarithmic[a]==a*c%p;assertions+=1
                leading_cases+=1
        for a in range(1, 101):
            for d in range(1, 21):
                if a%p:continue
                assert p*a*d==p*(a//p)*(p*d);assertions+=1
                if p==2:assert (p*d)%2==0;assertions+=1
                degree_cases+=1
    out={'recorded_utc':datetime.now(timezone.utc).isoformat(),
        'status':'PASS','assertions':assertions,
        'differential_matrix_cases':differential_cases,
        'formal_leading_coefficient_cases':leading_cases,
        'quotient_degree_cases':degree_cases,
        'scope':'Sparse Gaussian elimination for the local pth-power approximation; truncated inverse multiplication for the radial logarithmic cocycle; exact quotient-degree identities. These checks do not certify global cohomology, linearization or geometry.'}
    target=Path(__file__).resolve().parents[1]/'records/CONDUCTOR_DESCENT_ALGEBRA.json'
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='differential_matrix_cases'}))

if __name__=='__main__':main()
