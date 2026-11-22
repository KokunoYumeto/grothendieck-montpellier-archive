#!/usr/bin/env python3
"""Independent checks of the retained degree-three group certificates."""
import json,time
from pathlib import Path
import sympy as sp
started=time.perf_counter();root=Path(__file__).resolve().parents[1]
src=Path(__file__).with_name('product_higher_degree_certificates.py')
ctx={'__file__':str(src)}
exec(compile(src.read_text().split("print('degree',d")[0],str(src),'exec'),ctx)
assert ctx['d']==3
record=json.loads((root/'outputs/product_degree3_certificates.json').read_text())
ell=record['irreducible_frobenius']['primitive_prime_dividing_order']
assert ell==4278255361
divisors=list(range(3,sp.integer_nthroot(ell,2)[0]+1,2))
assert ell%2 and all(ell%d for d in divisors)
assert pow(2,80,ell)==1 and pow(2,40,ell)!=1 and pow(2,16,ell)!=1
T=sp.Symbol('T');checks=[]
for key in ['irreducible_frobenius','different_frobenius']:
 r=record[key];C=ctx['matrix'](r['section_bits']);assert C==r['columns']
 assert ctx['rank'](C)==81
 P=sp.Matrix(81,81,lambda i,j:(C[j]>>i)&1).charpoly(T).as_poly()
 bits=sum((int(c)%2)<<int(m[0]) for m,c in P.terms())
 f,rem=ctx['pdiv'](bits,3);assert rem==0
 assert f==r.get('factor_bits',r.get('relative_factor_bits'))
 checks.append({'record':key,'coefficient_reconstruction':True,
                'Cartier_rank':81,'independent_integer_charpoly_mod2':True})
assert record['irreducible_frobenius']['factor_bits']!=record['different_frobenius']['relative_factor_bits']
f=record['irreducible_frobenius']['factor_bits']
assert ctx['irreducible'](f) and ctx['reciprocal'](f)!=f
assert ctx['poly_power'](2,(2**80-1)//ell,f)!=1
L=record['line_certificate']
A=ctx['matrix'](L['section_a_bits']);B=ctx['matrix'](L['section_b_bits'])
assert A==L['A_columns'] and B==L['B_columns']
yes,out=ctx['line_certificate'](A,B);assert yes
assert out['determinant_bits']==L['determinant_bits'] and out['factors']==L['factors']
result={'degree':3,'primitive_prime':ell,'primality':'trial division through floor sqrt',
 'trial_divisors_tested':len(divisors),'multiplicative_order_of_2':80,
 'frobenius_checks':checks,'line_reconstructed_and_all_finite_field_ranks_rechecked':True,
 'runtime_seconds':time.perf_counter()-started}
(root/'outputs/verify_product_degree3.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
