"""Verify every recorded GT-Hermite product directly in all nine matrix blocks.

No polynomial triangular division or multiplication-table construction
code is imported.  The known faithful GT coordinate map is the input.
Each stored linear combination is multiplied by one common denominator
and compared with ordinary dense matrix multiplication over Q[D].
"""
from pathlib import Path
import gzip,json,time
from flint import fmpq,fmpq_poly

HERE=Path(__file__).resolve().parent
ZERO=fmpq_poly([]);ONE=fmpq_poly([1]);D=fmpq_poly([0,1])


def parse(p):return fmpq_poly([fmpq(p.get(str(i),'0')) for i in range(max(map(int,p),default=-1)+1)])
def exact(p,q):
    a,r=divmod(p,q);assert not r
    return a


def main():
    started=time.time()
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','rt') as f:data=json.load(f)
    with gzip.open(HERE/'gt_hermite_multiplication_table.json.gz','rt') as f:table=json.load(f)
    assert table['basis_labels']==data['coordinate_labels']
    den=[parse(p) for p in data['coordinate_denominators']];Delta=ONE
    for p in den:Delta=exact(Delta*p,Delta.gcd(p))
    Delta/=Delta.leading_coefficient()
    labels=data['coordinate_labels'];modules=[];coordinates={};sizes={}
    for z,label in enumerate(labels):
        name=label['module']
        if name not in sizes:modules.append(name);sizes[name]=0
        i,j=label['matrix_row'],label['matrix_column']
        sizes[name]=max(sizes[name],i+1,j+1);coordinates[name,i,j]=z
    rows=[];matrices=[]
    for row in data['rows']:
        v={int(z):parse(p)*exact(Delta,den[int(z)]) for z,p in row['gt_numerators'].items()}
        rows.append(v)
        matrices.append({name:[[v.get(coordinates[name,i,j],ZERO) for j in range(sizes[name])]
                               for i in range(sizes[name])] for name in modules})
    assert len(rows)==114 and sum(n*n for n in sizes.values())==114
    total=0;nonzero=0;maximum_degree=-1
    for i in range(114):
        for j in range(114):
            coeffs={int(k):parse(p) for k,p in table['multiplication'][i][j].items()}
            if i==0:assert coeffs=={j:ONE}
            if j==0:assert coeffs=={i:ONE}
            nonzero+=len(coeffs)
            for p in coeffs.values():maximum_degree=max(maximum_degree,p.degree())
            expected={}
            for k,p in coeffs.items():
                for z,c in rows[k].items():
                    value=expected.get(z,ZERO)+p*c
                    if value:expected[z]=value
                    else:expected.pop(z,None)
            actual={}
            for name in modules:
                n=sizes[name];A=matrices[i][name];B=matrices[j][name]
                for r in range(n):
                    for c in range(n):
                        value=sum((A[r][k]*B[k][c] for k in range(n)),ZERO)
                        if value:actual[coordinates[name,r,c]]=value
            assert actual=={z:p*Delta for z,p in expected.items()},(i,j)
            total+=1
        if (i+1)%20==0:print(json.dumps({'rows_checked':i+1,'products_checked':total,'seconds':time.time()-started}),flush=True)
    witness=parse(table['multiplication'][1][10]['92'])
    assert witness==D-fmpq(9,2) and not witness(fmpq(9,2))
    result={'status':'PASS','scope':'Separate full-table matrix replay using the independently verified faithful GT map; same author.',
            'basis_size':114,'products_verified':total,'nonzero_constants':nonzero,
            'maximum_D_degree':maximum_degree,'identity_basis_index':0,
            'signed_positivity_counterexample':{'left':1,'right':10,'output':92,'coefficient':'D-9/2','zero_at_v':'sqrt(2)'},
            'seconds':time.time()-started}
    (HERE/'gt_hermite_multiplication_independent_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
