"""Test both split minuscule directions at carried residual moduli.

No modulus is assumed prime. Elimination only divides units. A full-rank
result is therefore valid at every prime divisor of the modulus; a returned
primitive kernel is checked directly in all four matrices.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd
import json,sys,hashlib

sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE=ROOT/'KTOWER_work/evidence/higher4/hecke_general/higher4'


def modular_matrix(row,signs,m):
    raw=row['rational_real_form_operator']
    matrix=[]
    denominator_gcds=set()
    for i,line in enumerate(raw):
        out=[]
        for j,entry in enumerate(line):
            r=Fraction(entry)
            a=Fraction(row['operator_0'][i][j])
            b=Fraction(row['operator_omega'][i][j])
            if signs[i]==signs[j]:
                assert b==0 and r==a
            else:
                assert b==2*a
                assert r==(-3*a if signs[i]==1 else a)
            g=gcd(r.denominator,m)
            denominator_gcds.add(g)
            assert g==1, ('nonunit denominator',g)
            out.append(r.numerator*pow(r.denominator,-1,m)%m)
        matrix.append(out)
    return matrix,sorted(denominator_gcds)


def unit_rref(matrix,m):
    a=[row[:] for row in matrix]
    height=len(a);width=len(a[0]) if a else 0
    pivots=[];pivot_units=[];rank=0
    for col in range(width):
        found=next((r for r in range(rank,height) if gcd(a[r][col],m)==1),None)
        if found is None:continue
        a[rank],a[found]=a[found],a[rank]
        pivot_units.append(a[rank][col])
        inv=pow(a[rank][col],-1,m)
        a[rank]=[x*inv%m for x in a[rank]]
        for r in range(height):
            if r!=rank and a[r][col]:
                v=a[r][col]
                a[r]=[(x-v*y)%m for x,y in zip(a[r],a[rank])]
        pivots.append(col);rank+=1
        if rank==width:break
    tail_nonzero=[gcd(x,m) for row in a[rank:] for x in row if x]
    kernel=[]
    if not tail_nonzero:
        for col in range(width):
            if col in pivots:continue
            v=[0]*width;v[col]=1
            for r,pivot in enumerate(pivots):v[pivot]=-a[r][col]%m
            assert all(sum(x*y for x,y in zip(row,v))%m==0 for row in matrix)
            kernel.append(v)
    return {'unit_rank':rank,'columns':width,'pivot_columns':pivots,
            'pivot_units':pivot_units,'unresolved_nonunit_gcds':sorted(set(tail_nonzero)),
            'kernel_basis':kernel,
            'status':'full_column_rank' if rank==width else
                     ('primitive_kernel' if not tail_nonzero else 'inconclusive_nonunit_pivots')}


def difference(R,t,m):
    return [[(x-(t if i==j else 0))%m for j,x in enumerate(row)]
            for i,row in enumerate(R)]


def dual(R,signs,m):
    return [[(signs[i]*x*signs[j])%m for j,x in enumerate(row)]
            for i,row in enumerate(R)]


def commutes(A,B,m):
    n=len(A)
    for i in range(n):
        for j in range(n):
            if sum(A[i][k]*B[k][j]-B[i][k]*A[k][j] for k in range(n))%m:return False
    return True


def main():
    source=BASE/'harmonic_hecke_exact_data.json'
    models=json.loads(source.read_text())['degrees']
    reports=[]
    for model in models:
        e=model['e'];signs=model['swap_signs'];n=len(signs)
        residual_path=BASE/f'residual_support_e{e}.json'
        support=json.loads(residual_path.read_text())['degrees'][0]['residual_support_moduli']
        m=support[0]
        assert gcd(m,6)==1
        matrices={};denominator_checks={};commuting_checks={}
        for row in model['results']:
            p=row['p']
            if p not in (7,13):continue
            R,ds=modular_matrix(row,signs,m)
            Rp=dual(R,signs,m)
            commuting_checks[str(p)]=commutes(R,Rp,m)
            assert commuting_checks[str(p)]
            t=(pow(p,2*e,m)+pow(p,e,m)+1)%m
            matrices[p]=(difference(R,t,m),difference(Rp,t,m))
            denominator_checks[str(p)]=ds
        checks=[]
        for primes in [(7,),(13,),(7,13)]:
            pieces=[];full_kernel=[]
            for parity in (1,-1):
                columns=[i for i,s in enumerate(signs) if s==parity]
                selected=[[row[j] for j in columns]
                          for p in primes for row in matrices[p][0]]
                result=unit_rref(selected,m)
                result['parity']=parity
                for v in result['kernel_basis']:
                    full=[0]*n
                    for j,x in zip(columns,v):full[j]=x
                    for p in primes:
                        for A in matrices[p]:
                            assert all(sum(x*y for x,y in zip(row,full))%m==0 for row in A)
                    full_kernel.append(full)
                pieces.append(result)
            check={'primes':primes,'parity_checks':pieces,
                   'both_directions_excluded':all(x['status']=='full_column_rank' for x in pieces),
                   'verified_full_kernel_vectors':full_kernel}
            checks.append(check)
            print('e',e,'modulus',m,'primes',primes,
                  [(x['parity'],x['unit_rank'],x['columns'],x['status']) for x in pieces],flush=True)
        reports.append({'e':e,'modulus':m,'dimension':n,
                        'coefficient_basis':'delta=1+2omega on negative-swap columns; dual=C R C',
                        'denominator_gcds':denominator_checks,
                        'dual_commutation_checks':commuting_checks,'checks':checks})
    out={'status':'exact unit-pivot elimination, no primality assumption',
         'source':str(source.relative_to(ROOT)),
         'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'reports':reports}
    HERE.joinpath('dual_hecke_check.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
