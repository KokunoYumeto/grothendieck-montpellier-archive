"""Exact GF(2)[c] Cartier-minor search for ordinary-times-supersingular (6,3).

This is a candidate certificate, not a geometric smoothness or norm proof.
All attempted coefficient vectors, ranks, minors, failures and elapsed time
are retained.  Polynomial integers encode coefficients in GF(2)[c].
"""
from pathlib import Path
import json, random, time, traceback

started = time.perf_counter()
root = Path(__file__).resolve().parents[1]
output = root / 'outputs' / 'mixed_6_3_cartier_search.json'
assert not output.exists()
record = {'status': 'RUNNING', 'field': 'GF(2)[c]',
          'ordinary_curve': 'y^2+xy=x^3+c; c!=0',
          'ordinary_basis': ['1','x','y','x^2','xy','x^3'],
          'supersingular_curve': 'w^2+w=z^3',
          'supersingular_basis': ['1','z','w'],
          'trials': [], 'seed': 202611191343}

def pmul(a,b):
    ans=0
    while b:
        if b&1:ans^=a
        b>>=1;a<<=1
    return ans

def pdiv(a,b):
    assert b
    q=0
    while a and a.bit_length()>=b.bit_length():
        d=a.bit_length()-b.bit_length();q^=1<<d;a^=b<<d
    return q,a

def pexact(a,b):
    q,r=pdiv(a,b)
    assert r==0, (a,b,r)
    return q

def pgcd(a,b):
    while b:a,b=b,pdiv(a,b)[1]
    return a

def psquare(a):
    ans=0;i=0
    while a:
        if a&1:ans|=1<<(2*i)
        a>>=1;i+=1
    return ans

def mmul(A,B):
    n=len(A)
    ans=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    if B[k][j]:ans[i][j]^=pmul(A[i][k],B[k][j])
    return ans

def det(A):
    A=[r[:] for r in A];n=len(A);prev=1
    for k in range(n-1):
        pivot=next(((i,j) for i in range(k,n) for j in range(k,n) if A[i][j]),None)
        if pivot is None:return 0
        i,j=pivot;A[k],A[i]=A[i],A[k]
        if j!=k:
            for row in A:row[k],row[j]=row[j],row[k]
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=pexact(pmul(p,A[i][j])^pmul(A[i][k],A[k][j]),prev)
        for i in range(k+1,n):A[i][k]=0
        prev=p
    return A[-1][-1]

def pivots_at_one(A):
    # Track both row and column choices so the extracted original minor is nonzero.
    B=[[x.bit_count()%2 for x in row] for row in A]
    rowids=list(range(len(B)));columns=[];rank=0
    for c in range(len(B[0])):
        pivot=next((i for i in range(rank,len(B)) if B[i][c]),None)
        if pivot is None:continue
        B[rank],B[pivot]=B[pivot],B[rank]
        rowids[rank],rowids[pivot]=rowids[pivot],rowids[rank]
        for i in range(rank+1,len(B)):
            if B[i][c]:B[i]=[a^b for a,b in zip(B[i],B[rank])]
        columns.append(c);rank+=1
    return rank,rowids[:rank],columns

try:
    # Each entry records an ordinary output basis coefficient, plus c^1/2.
    # squaring the Cartier matrix replaces c^1/2 by c, encoded by integer2.
    # Ordinary multiplication-Cartier pairing C(f_i f_j dx/x)/(dx/x).
    E = [
      [{0:1},{},{1:1},{1:1},{2:1,0:2},{}],
      [{},{1:1},{2:1,0:2},{},{3:1},{3:1}],
      [{1:1},{2:1,0:2},{2:1},{3:1},{},{4:1,1:2}],
      [{1:1},{},{3:1},{3:1},{4:1,1:2},{}],
      [{2:1,0:2},{3:1},{},{4:1,1:2},{4:1},{5:1}],
      [{},{3:1},{4:1,1:2},{},{5:1},{5:1}],
    ]
    S = [[None,0,1],[0,None,2],[1,2,None]]
    assert all(E[i][j]==E[j][i] for i in range(6) for j in range(6))
    record['squared_ordinary_pairing']=E
    record['supersingular_pairing_output_indices']=S
    rng=random.Random(record['seed']);common=0
    for trial in range(512):
        coeff=[rng.randrange(2) for _ in range(18)]
        T=[[0]*18 for _ in range(18)]
        for i in range(6):
            for j in range(3):
                if not coeff[3*i+j]:continue
                for a in range(6):
                    for b in range(3):
                        z=S[j][b]
                        if z is not None:
                            for x,v in E[i][a].items():T[3*x+z][3*a+b]^=v
        M=[list(row) for row in zip(*T)]
        MM=mmul(M,[[psquare(v) for v in row] for row in M])
        rank,rows,cols=pivots_at_one(MM)
        rec={'trial':trial,'coefficients':coeff,'rank_at_c_one':rank}
        if rank>=16:
            assert rank==16, 'Unexpected rank above the candidate geometric upper bound'
            minor=det([[MM[i][j] for j in cols] for i in rows])
            assert minor and minor.bit_count()%2==1
            common=pgcd(common,minor)
            rec.update({'minor_rows':rows,'minor_columns':cols,
                        'minor_polynomial_bits':minor,
                        'minor_nonzero_exponents':[i for i in range(minor.bit_length()) if minor>>i&1],
                        'gcd_polynomial_bits':common,
                        'squared_cartier_matrix':M,
                        'two_iterate_matrix':MM})
        record['trials'].append(rec)
        if common and common&(common-1)==0:
            record['status']='PASS'
            record['common_minor_gcd_bits']=common
            record['common_minor_gcd_degree']=common.bit_length()-1
            record['scope']='For every c!=0 at least one retained F2 section has its two-iterate Frobenius matrix of rank at least16. Smoothness, rank upper bound, stable-rank deduction and norm transfer require separate proofs.'
            break
    else:
        record['status']='SEARCH_INCOMPLETE'
        record['common_minor_gcd_bits']=common
except Exception:
    record['status']='FAIL'
    record['traceback']=traceback.format_exc()
finally:
    record['elapsed_seconds']=time.perf_counter()-started
    output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k not in ('trials','squared_ordinary_pairing')},indent=2))
    print('Trial count:',len(record['trials']))
    print('Rank16 witnesses:',sum(t['rank_at_c_one']==16 for t in record['trials']))
