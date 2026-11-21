"""Exact ordinary/symmetric Kronecker coefficients of the n=m=3 Hessian shape."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import json
source=Path(__file__).with_name('check_hessian_bracket_plethysm.py')
ns={'__file__':str(source)};exec(source.read_text().split('start=time.time()')[0],ns)
parts=ns['partitions'];chi=ns['character'];z_type=ns['z_type']
lam=(13,3)+(2,)*7;mu=(10,10,10)
g=Fraction(0);twist=Fraction(0);nonzero=0
for cyc in parts(30):
 a=chi(lam,cyc);b=chi(mu,cyc)
 g+=Fraction(a*b*b,z_type(cyc))
 square=tuple(sorted([j for k in cyc for j in ([k//2,k//2] if k%2==0 else [k])],reverse=True))
 twist+=Fraction(a*chi(mu,square),z_type(cyc))
 nonzero+=bool(a*b)
sk=(g+twist)/2
assert g==sk==0
result={'date_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed','run':'GCT_KRON_20261120','method':'Exact Murnaghan-Nakayama character sums over all partitions of30. Symmetric coefficient uses chi_Sym2(mu)(sigma)=(chi_mu(sigma)^2+chi_mu(sigma^2))/2. Engine independently crosschecked in companion plethysm certificate.','partition_lambda':lam,'rectangle_mu':mu,'cycle_types':len(parts(30)),'nonzero_product_cycle_types':nonzero,'ordinary_g':int(g),'squared_cycle_character_inner_product':int(twist),'symmetric_sk':int(sk),'status':'PASS'}
p=Path(__file__).with_name('hessian_rectangular_kronecker_certificate.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
