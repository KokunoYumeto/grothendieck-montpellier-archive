"""Finite symbolic checks supplementing C_Witt_localization_source_correction.md.
The infinite localization claims are proved in the note, not certified by sampling.
"""
from pathlib import Path
from time import perf_counter
import json, hashlib
import sympy as s
start=perf_counter();checks=0
f=s.Symbol('f');a=s.symbols('a0:5');polynomial_checks=0
for p in (2,3,5):
 for N in (1,2,3):
  for n in range(5):
   ghost_a=sum(p**i*a[i]**(p**(n-i)) for i in range(n+1))
   ghost_b=sum(p**i*(f**(N*p**i)*a[i])**(p**(n-i)) for i in range(n+1))
   assert s.expand(ghost_b-f**(N*p**n)*ghost_a)==0
   checks+=1;polynomial_checks+=1
printed_witness_checks=0;corrected_witness_checks=0
for p in (2,3,5):
 for i in range(17):
  assert p**i-i>=0
  checks+=1;printed_witness_checks+=1
 for N in range(17):
  i=N+1
  assert N*p**i-i*p**i<0
  checks+=1;corrected_witness_checks+=1
out={'status':'PASS','checks_count':checks,'ghost_polynomial_identities':polynomial_checks,'printed_witness_exponent_checks':printed_witness_checks,'corrected_witness_exponent_checks':corrected_witness_checks,'primes':[2,3,5],'elapsed_seconds':perf_counter()-start,'scope':'45 exact universal-polynomial ghost identities,51 printed-witness nonnegative exponents,51 corrected-witness negative exponents. The arbitrary-length and arbitrary-prime statements are proved analytically in the note.','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path('RESEARCH_SA22/logs/C_Witt_localization_certificate.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
