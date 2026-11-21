#!/usr/bin/env python3
"""Independent exact Jacobian certificate: nine labelled squares fill 3xSym^2(6)."""
from itertools import combinations_with_replacement
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def determinant(M):
    M=[r[:] for r in M];n=len(M);previous=1;sign=1
    for k in range(n-1):
        if not M[k][k]:
            j=next((j for j in range(k+1,n) if M[j][k]),None)
            if j is None:return 0
            M[k],M[j]=M[j],M[k];sign=-sign
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=M[i][j]*pivot-M[i][k]*M[k][j]
                assert value%previous==0
                M[i][j]=value//previous
            M[i][k]=0
        previous=pivot
    return sign*M[-1][-1]

def main():
    data=json.loads((HERE/'nine_square_jacobian_certificate.json').read_text())
    A=data['A'];V=data['V']
    expected_A=[[int(i==h//3) for i in range(3)] for h in range(9)]
    expected_V=[[int(i==h) for i in range(6)] for h in range(6)]
    expected_V += [[1,1,0,1,1,0],[1,0,1,2,0,1],[0,1,1,0,2,2]]
    assert A==expected_A and V==expected_V
    mons=list(combinations_with_replacement(range(6),2))
    rows,cols=data['rows'],data['cols']
    assert rows==list(range(63)) and len(cols)==len(set(cols))==63
    assert all(0<=c<81 for c in cols)
    def entry(row,col):
        a,m=divmod(row,21);i,j=mons[m]
        point,variable=divmod(col,9)
        if variable<3:return int(a==variable)*V[point][i]*V[point][j]
        h=variable-3
        return A[point][a]*(int(i==h)*V[point][j]+int(j==h)*V[point][i])
    value=determinant([[entry(r,c) for c in cols] for r in rows])
    assert value==data['determinant_Z']==-16
    result={'status':'PASS','jacobian_shape':[63,81],'minor_order':63,
            'determinant_Z':value,'field_scope':'every characteristic other than two',
            'conclusion':'the nine-labelled-squares parameter map is dominant'}
    (HERE/'nine_square_jacobian_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
