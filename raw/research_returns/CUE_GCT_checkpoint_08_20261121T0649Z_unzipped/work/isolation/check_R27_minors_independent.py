"""Independent selected-minor check for R27's stored boundary jet arrays.

Does not import the author's checkers.  The full coefficient reconstruction
was performed independently by root; this script checks only the three
specified selected minors, with fresh exact modular elimination.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import numpy as np

ROOT=Path('/workspace/scratch/64674c0aa6e9')
BASE=ROOT/'work/rectangular/border_ternary'
arrays_path=BASE/'jacobi_boundary_repair_m17.npz'
certificate_path=BASE/'boundary_toeplitz_certificates.json'


def determinant(values,p):
    a=[list(map(int,row)) for row in values]
    n=len(a); value=1
    assert all(len(row)==n for row in a)
    for k in range(n):
        pivot=next((r for r in range(k,n) if a[r][k]%p),None)
        assert pivot is not None
        if pivot!=k:
            a[k],a[pivot]=a[pivot],a[k]
            value=-value
        diagonal=a[k][k]%p
        value=value*diagonal%p
        inverse=pow(diagonal,-1,p)
        for r in range(k+1,n):
            factor=a[r][k]*inverse%p
            if factor:
                a[r][k]=0
                for c in range(k+1,n):
                    a[r][c]=(a[r][c]-factor*a[k][c])%p
    return value%p


def main():
    archive=np.load(arrays_path)
    coefficients=[archive['C0'],archive['C1'],archive['C2']]
    assert all(c.shape==(124,91) for c in coefficients)
    certificates=json.loads(certificate_path.read_text())
    results=[]
    for certificate in certificates:
        order=certificate['jet_order']
        rows=certificate['ordered_selected_rows']
        cols=certificate['selected_columns']
        assert len(rows)==len(set(rows))==len(cols)==len(set(cols))==certificate['rank']
        # Directly generate each selected coefficient from its block indices,
        # rather than building/importing the author's Toeplitz matrix.
        values=[]
        for row in rows:
            block_row,local_row=divmod(row,124)
            current=[]
            for col in cols:
                block_col,local_col=divmod(col,91)
                shift=block_row-block_col
                current.append(int(coefficients[shift][local_row,local_col])
                               if 0<=shift<=order else 0)
            values.append(current)
        computed=determinant(values,101)
        assert computed==certificate['selected_minor_mod101'] and computed
        results.append({'order':order,'minor_size':len(rows),'determinant_mod101':computed})
    delta=[34,1,37,24,47,1,59,41,0,92,38,56,75,6,44,14]
    product=1
    for i,d in enumerate(delta):
        if i!=8: product=product*d%101
    assert product==1
    result={'time_utc':datetime.now(timezone.utc).isoformat(),
            'checker':'GPT-6 Astra Pro; effort not exposed; agent=/root/isolation',
            'method':'Fresh exact pure-Python modular elimination of the three selected minors; direct block-index coefficient extraction; no author-code imports.',
            'arrays_sha256':sha256(arrays_path.read_bytes()).hexdigest(),
            'certificate_sha256':sha256(certificate_path.read_bytes()).hexdigest(),
            'results':results,'noncut_edge_product_mod101':product,
            'scope':'Selected-minor verification only. Root independently reconstructed all33852 stored coefficient entries; this reviewer did not repeat that reconstruction.'}
    output=ROOT/'work/isolation/R27_minors_independent_checks.json'
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
