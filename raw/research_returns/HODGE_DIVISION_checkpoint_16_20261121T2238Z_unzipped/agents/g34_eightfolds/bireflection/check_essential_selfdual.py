#!/usr/bin/env python3
"""Exact arithmetic certificate for D-BI09; the universal proof is in the TeX."""
from pathlib import Path
import hashlib,json

def main():
    rows=[]
    for k in range(9,24):
        p=(k+1)//2
        low=2*p+30
        assert low>2*k+6
        factors=[]
        for a in range(2,k+1):
            if k%a: continue
            b=k//a
            if a>b: continue
            lower=2*p+b+9*a
            assert lower>2*k+6
            factors.append({'a':a,'b':b,'moving_lower_bound':lower,
                            'budget':2*k+6,'excess':lower-(2*k+6)})
        rows.append({'k':k,'tensor_indecomposable_lower_bound':low,
                     'budget':2*k+6,'tensor_factorizations':factors})
    assert 2*5+10*2==30>26
    assert 2*((24+1)//2)+30==2*24+6
    tensor_first=[]
    for a in range(2,10):
        b=a
        while (a-1)*b<9*a-6+(a*b%2): b+=1
        tensor_first.append({'a':a,'first_permitted_b':b,'degree':a*b})
    assert tensor_first[0]=={'a':2,'first_permitted_b':12,'degree':24}
    out={'status':'PASS','statement':'D-BI09 arithmetic certificate',
         'universal_group_and_geometric_proof':'essential_selfdual_section.tex',
         'degree_range_checked':[9,23],'all_factorizations':rows,
         'symplectic_exception_lower_bound':30,'symplectic_exception_budget':26,
         'first_not_numerically_excluded_independent_degree':24,
         'first_tensor_degrees':tensor_first,
         'warning':'Passing a numerical budget is not a construction or a dominance claim.',
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','excluded_degrees':[9,23],
                      'first_tensor_degrees':tensor_first}))
if __name__=='__main__': main()
