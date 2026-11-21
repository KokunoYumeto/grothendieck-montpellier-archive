"""Exact bounded-length arithmetic certificate for O018, not an enumeration of all cuts."""
import json
from datetime import datetime, timezone
from math import comb, factorial
from pathlib import Path

m=2**200
r=m*m
n=m**25
d=3*n
last_variables=r-51
G=sum(comb(last_variables+t-1,t)*sum(comb(48+j,j)*(m-j-t+1)
                                   for j in range(27-t)) for t in range(3))
support_upper=(m+1)*comb(75,26)*comb(r-49,2)
assert G<=support_upper<=comb(75,26)*m**5<n
dimension_bound=(r-2)*n*n+2
cut_bounds={
    'k2_or_k_greater_than_r_over_2':comb(r//2-2,27),
    'k3_through_51':(m-25)*comb(r-50,26),
    'k52_through_r_over_2':comb(m+48,50)*comb(r//2+1,2),
}
assert dimension_bound<m**52
assert all(value>m**52 for value in cut_bounds.values())
assert 2**54*factorial(27)<m*m
assert 2**27*factorial(26)<m
assert 2**53*factorial(50)<m*m
assert comb(187,49)<=190**20<comb(188,49)
assert m>5001
assert comb(r//2,27)>n
tail=2*n+2*r+1172
first=3*n*n-tail
assert first>=2*n>=26>=2
assert tail<=m*d
assert n-r-586>=0 and n-16>=0
factor_degree=2*(n-16)+51*12+r+(n-r-586)
assert factor_degree==d-6
assert 6+2*(n-16)+2*12+2==2*n
assert comb(d,2)>n
record={
    'finding':'O-018',
    'date_utc':datetime.now(timezone.utc).isoformat(),
    'model':'GPT-6 Astra Pro','effort':'not exposed','run':'GCT_KRON_20261120',
    'parameters':{'m_power_of_two':200,'r_power_of_two':400,'n_power_of_two':5000,'d':'3*n'},
    'exact_support_count':str(G),'support_upper':str(support_upper),
    'determinant_pencil_dimension_bound':str(dimension_bound),
    'one_cut_lower_bounds':{key:str(value) for key,value in cut_bounds.items()},
    'joint_row_constant':{'binom187_49':str(comb(187,49)),
                          '190_to_20':str(190**20),'binom188_49':str(comb(188,49))},
    'all_range_lower_bounds_exceed_m52':True,
    'support_fits_n':True,'all_positive_factor_exponents':True,
    'Hessian_factor_degree':'d-6','second_row_after_seed':'2*n',
    'Grenet_comparison':'2^m-1 > n follows from m>5001; gigantic power not constructed',
    'scope':'Finite exact integer formula checks. Every-cut coverage is proved by three ranges in the text; no exponential enumeration or multiplicity computation is claimed.',
    'status':'PASS'
}
path=Path(__file__).with_name('full_profile_certificate.json')
path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','range_checks':len(cut_bounds),
                  'support_count_digits':len(str(G)),
                  'certificate':str(path)}))
