"""Exact lower-weight GL2 and proved adjoint-factor consistency check.

The classical matrices are freshly computed with the audited uniform GL2
program. Polynomial operations do not use archived factor lists. The compact
stable polynomial is the independently checked quotient saved in this audit.
"""
from pathlib import Path
from math import gcd
from fractions import Fraction
import hashlib,importlib.util,json,sys
from flint import fmpz_mat
import sympy as sp

from check_spectral_split import divide_monic,monic_square_root,evaluate

sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
GL2_PATH=ROOT/'KTOWER_work/evidence/gl2_uniform.py'
spec=importlib.util.spec_from_file_location('ktower_classical_uniform',GL2_PATH)
gl2=importlib.util.module_from_spec(spec);spec.loader.exec_module(gl2)


def square_image_polynomial(h,constant):
    n=len(h)-1
    if not n:return [1]
    C=[[0]*n for _ in range(n)]
    for j in range(n-1):C[j+1][j]=1
    for i in range(n):C[i][-1]=-h[n-i]
    C=fmpz_mat(C)
    A=C*C
    for i in range(n):A[i,i]-=constant
    return list(reversed(list(map(int,A.charpoly()))))


def main():
    split_path=HERE/'spectral_split_check.json'
    split=json.loads(split_path.read_text())
    stable={(x['e'],x['p']):x for x in split['results']}
    old_gl2=json.loads((ROOT/'KTOWER_work/evidence/gl2_uniform.json').read_text())
    old={(x['e'],p['p']):p['charpoly_coefficients'] for x in old_gl2['degrees'] for p in x['results']}
    classical=[];results=[];summaries=[]
    for e in range(2,32,2):
        n=e//2
        lower=gl2.compute(n,[7,13]);classical.append(lower)
        expected=(e-2)//6
        remainder_values=[]
        for row in lower['results']:
            p=row['p'];q=row['charpoly_coefficients']
            if (n,p) in old:assert old[n,p]==q
            if row['cm_eigenvalue'] is not None:
                q=divide_monic(q,[1,-row['cm_eigenvalue']])
            h=monic_square_root(q)
            assert len(h)-1==expected
            symmetric=square_image_polynomial(h,p**e)
            assert len(symmetric)-1==expected
            s=stable[e,p]
            remainder=divide_monic(s['stable_coefficients'],symmetric)
            t=s['stable_comparison_point']
            sv=evaluate(symmetric,t);rv=evaluate(remainder,t)
            assert sv*rv==s['stable_comparison_value']
            remainder_values.append(abs(rv))
            results.append({'e':e,'lower_parameter':n,'lower_weight':e+1,'p':p,
                            'lower_dimension':lower['dimension'],
                            'lower_cm_dimension':lower['cm_dimension'],
                            'symmetric_square_dimension':expected,
                            'remaining_stable_dimension':len(remainder)-1,
                            'lower_noncm_twist_orbit_polynomial':h,
                            'symmetric_square_coefficients':symmetric,
                            'remaining_stable_coefficients':remainder,
                            'comparison_point':t,'symmetric_square_comparison':sv,
                            'remaining_stable_comparison':rv,
                            'exact_stable_divisibility':True})
            print(f'e={e:2} p={p:2} Sym2={expected:2} remaining={len(remainder)-1:3}: PASS',flush=True)
        summaries.append({'e':e,'symmetric_square_dimension':expected,
                          'remaining_stable_dimension':len(remainder)-1,
                          'remaining_stable_gcd_7_13':gcd(*remainder_values)})
    lookup={(r['e'],r['p']):r for r in results}
    residual=[]
    for e in (26,28,30):
        support_path=ROOT/f'KTOWER_work/evidence/higher4/hecke_general/higher4/residual_support_e{e}.json'
        support=json.loads(support_path.read_text())['degrees'][0]['residual_support_moduli']
        n=e+1
        bern=sp.cancel(2*3**(n-1)*sp.bernoulli(n,sp.Rational(1,3))/n)
        for m in support:
            entry={'e':e,'modulus':m,
                   'gcd_with_symmetric_square_7':gcd(m,lookup[e,7]['symmetric_square_comparison']),
                   'gcd_with_symmetric_square_13':gcd(m,lookup[e,13]['symmetric_square_comparison']),
                   'gcd_with_remaining_stable_7':gcd(m,lookup[e,7]['remaining_stable_comparison']),
                   'gcd_with_remaining_stable_13':gcd(m,lookup[e,13]['remaining_stable_comparison']),
                   'bernoulli_index':n,'bernoulli_divided_by_index_numerator':int(sp.numer(bern)),
                   'bernoulli_divided_by_index_denominator':int(sp.denom(bern)),
                   'gcd_with_bernoulli_numerator':gcd(m,int(sp.numer(bern))),
                   'gcd_with_inert_CM_test_1_minus_2power_e':gcd(m,1-2**e),
                   'gcd_with_6':gcd(m,6),
                   'gcd_with_bernoulli_denominator':gcd(m,int(sp.denom(bern))),
                   'gcd_with_all_FR_and_CM_exceptions':gcd(m,6*int(sp.denom(bern))*(1-2**e))}
            if m==support[0]:
                assert int(sp.numer(bern))%m==0
                assert entry['gcd_with_all_FR_and_CM_exceptions']==1
            residual.append(entry)
    out={'status':'PASS exact Sym2 divisibility in all30 compact stable polynomials',
         'scope':'Polynomial consistency; global lift and source obligations stated separately',
         'gl2_program':str(GL2_PATH.relative_to(ROOT)),
         'gl2_program_sha256':hashlib.sha256(GL2_PATH.read_bytes()).hexdigest(),
         'stable_input_sha256':hashlib.sha256(split_path.read_bytes()).hexdigest(),
         'lower_classical_models':classical,'results':results,'degree_summary':summaries,
         'residual_moduli':residual}
    HERE.joinpath('symmetric_square_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS all30; residual support:')
    for x in residual:
        print(x['e'],x['modulus'],'Sym2 gcds',x['gcd_with_symmetric_square_7'],x['gcd_with_symmetric_square_13'],
              'remaining gcds',x['gcd_with_remaining_stable_7'],x['gcd_with_remaining_stable_13'],flush=True)


if __name__=='__main__':main()
