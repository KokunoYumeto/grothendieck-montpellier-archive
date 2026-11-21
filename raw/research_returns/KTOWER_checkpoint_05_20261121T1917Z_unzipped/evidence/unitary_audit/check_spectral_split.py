"""Exact independent polynomial check of the proved spectral split.

Uses classical and compact characteristic-polynomial inputs, but no archived
factorization routines or factors. Polynomial square roots, shifts and
division are implemented directly with Python integers. This is a consistency
check, not a replacement for the global packet proof.
"""
from pathlib import Path
from math import gcd
import hashlib
import json
import sys
from datetime import datetime, timezone

from character_trace import I, mul, conj, add

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARCHIVE = ROOT/'input/RETURN_K17_checkpoint_08_20261121T0616Z/evidence/work/hecke_general'


def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def divide_monic(a,b):
    assert b and b[0]==1
    assert len(a)>=len(b)
    work=a[:]
    q=[]
    for i in range(len(a)-len(b)+1):
        lead=work[i];q.append(lead)
        for j,coefficient in enumerate(b):work[i+j]-=lead*coefficient
    assert all(x==0 for x in work), 'nonzero exact-division remainder'
    assert multiply(q,b)==a
    return q


def monic_square_root(a):
    assert a[0]==1 and (len(a)-1)%2==0
    m=(len(a)-1)//2
    root=[1]
    for i in range(1,m+1):
        remainder=a[i]-sum(root[j]*root[i-j] for j in range(1,i))
        assert remainder%2==0
        root.append(remainder//2)
    assert multiply(root,root)==a, 'not a polynomial square'
    return root


def shift(a,n):
    out=[a[0]]
    for coefficient in a[1:]:
        out=multiply(out,[1,n]);out[-1]+=coefficient
    return out


def evaluate(a,x):
    out=0
    for c in a:out=out*x+c
    return out


def cm_value(e,p):
    pi={7:(3,1),13:(4,1)}[p]
    power=I
    for _ in range(2*e):power=mul(power,pi)
    value=add(power,conj(power))
    assert value[1]==0
    return value[0]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    sources=[
        ARCHIVE/'harmonic_hecke_exact_data.json',
        ARCHIVE/'higher2/harmonic_hecke_exact_data.json',
        ARCHIVE/'higher3/harmonic_hecke_exact_data.json',
        ROOT/'KTOWER_work/evidence/higher4/hecke_general/higher4/harmonic_hecke_exact_data.json',
    ]
    full={}
    input_metadata=[]
    for path in sources:
        data=json.loads(path.read_text())
        input_metadata.append({'path':str(path.relative_to(ROOT)),'sha256':digest(path)})
        for degree in data['degrees']:
            e=degree['e']
            for row in degree['results']:
                p=row['p']
                if p in (7,13):
                    assert (e,p) not in full
                    full[e,p]=(row['charpoly_coefficients'],str(path.relative_to(ROOT)))
    traces={}
    dimensions=None
    for p,name in [(7,'character_trace.json'),(13,'character_trace13.json')]:
        path=HERE/name;d=json.loads(path.read_text())
        input_metadata.append({'path':str(path.relative_to(ROOT)),'sha256':digest(path)})
        traces[p]=d[f'scaled_T{p}_traces']
        if dimensions is None:dimensions=d['dimensions']
        assert dimensions==d['dimensions']
        for e in (2,4):
            assert dimensions[e-1] in (0,1)
            coefficients=[1] if dimensions[e-1]==0 else [1,-traces[p][e-1]]
            full[e,p]=(coefficients,str(path.relative_to(ROOT)))
    classical_path=ROOT/'KTOWER_work/evidence/gl2_uniform.json'
    classical=json.loads(classical_path.read_text())
    input_metadata.append({'path':str(classical_path.relative_to(ROOT)),
                           'sha256':digest(classical_path)})
    results=[];summaries=[]
    for degree in classical['degrees']:
        e=degree['e'];d=e-1
        assert degree['dimension']==(2*e-2)//3
        assert degree['cm_dimension']==int(e%3==0)
        endodim=(e-1)//3
        full_dim=dimensions[d]
        stable_dim=full_dim-endodim
        stable_values=[]
        for row in degree['results']:
            p=row['p']
            q=row['charpoly_coefficients']
            if e%3==0:
                cm=cm_value(e,p)
                assert cm==row['cm_eigenvalue']
                noncm=divide_monic(q,[1,-cm])
            else:
                cm=None;noncm=q[:]
                assert row['cm_eigenvalue'] is None
            root=monic_square_root(noncm)
            endo=shift(root,-p**e)
            assert len(endo)-1==endodim
            compact,source=full[e,p]
            assert len(compact)-1==full_dim
            trace=-compact[1] if len(compact)>1 else 0
            assert trace==traces[p][d], 'independent character trace disagreement'
            stable=divide_monic(compact,endo)
            assert len(stable)-1==stable_dim
            target=p**(2*e)+p**e+1
            value=evaluate(stable,target)
            assert value!=0
            stable_values.append(abs(value))
            results.append({'e':e,'p':p,'coefficient_degree':d,
                'classical_dimension':degree['dimension'],
                'cm_dimension':degree['cm_dimension'],
                'full_dimension':full_dim,'endoscopic_dimension':endodim,
                'stable_dimension':stable_dim,'cm_eigenvalue':cm,
                'classical_noncm_square_root_coefficients':root,
                'endoscopic_coefficients':endo,'stable_coefficients':stable,
                'stable_comparison_point':target,'stable_comparison_value':value,
                'compact_input':source,'full_trace':trace,
                'exact_noncm_square':True,'exact_compact_quotient':True,
                'all_coefficients_reconstructed':True,
                'independent_character_trace_matches':True})
            print(f'e={e:2} p={p:2} full={full_dim:3} endo={endodim:2} stable={stable_dim:3}: PASS',flush=True)
        common=gcd(*stable_values)
        summaries.append({'e':e,'full_dimension':full_dim,
                          'endoscopic_dimension':endodim,'stable_dimension':stable_dim,
                          'stable_comparison_gcd_7_13':common})
    assert len(results)==30
    out={'status':'PASS all30 degree-prime pairs, exact square roots and divisibility',
         'checked_utc':datetime.now(timezone.utc).isoformat(),
         'method':'independent integer polynomial arithmetic and character traces',
         'scope':'Numerical consistency; global exhaustion proved separately',
         'inputs':input_metadata,'results':results,'degree_summary':summaries}
    HERE.joinpath('spectral_split_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS:',len(results),'pairs; 30 independent trace checks; no mismatches')


if __name__=='__main__':main()
