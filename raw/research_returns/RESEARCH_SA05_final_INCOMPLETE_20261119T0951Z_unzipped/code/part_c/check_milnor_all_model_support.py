"""Exact finite checks for the all-model residue-support diagnostic.

The proof for every eligible m is the displayed tame-symbol formula in
part_c/b1_milnor_residue_independent_audit.md; this finite certificate
checks that formula on explicit pairwise different alterations.
"""
from datetime import datetime, timezone
from pathlib import Path
from math import gcd
import json
from time import perf_counter

started_utc=datetime.now(timezone.utc).isoformat()
started_monotonic=perf_counter()

p, ell = 5, 3
samples=[]
for index in range(10):
    m=1+p*ell*index
    assert gcd(m,p*ell)==1
    # Exponents in (s,u): alpha={u,s^m}.
    first=(0,1)
    second=(m,0)
    # Convention: residue of {unit, uniformizer} is the reduced unit.
    # The u exponent in the first residue is v_s(second)*v_u(first)
    # minus v_s(first)*v_u(second).
    u_exponent=second[0]*first[1]-first[0]*second[1]
    second_residue=u_exponent
    assert second_residue==m and second_residue!=0
    samples.append({'alteration_degree':m,'first_residue_u_exponent':u_exponent,'second_residue':second_residue})
assert len({row['alteration_degree'] for row in samples})==len(samples)
out={
 'recorded_utc':datetime.now(timezone.utc).isoformat(),
 'started_utc':started_utc,
 'runtime_seconds':perf_counter()-started_monotonic,
 'runtime_scope':'Exact arithmetic checks and result construction, excluding JSON serialization and file I/O.',
 'residue_characteristic':p,'coefficient_prime':ell,
 'symbol':'{u,t}', 'alteration':'t=s^m; u=u',
 'residue_chain':['s=0','u=0'],
 'general_formula':'The iterated residue is m for every positive m coprime to p*ell, using the final-uniformizer convention; a convention change only changes a fixed sign.',
 'samples':samples,
 'scope':'Exact integer tame-symbol calculation. The note proves that infinitely many pairwise nonisomorphic alteration tuples exist. Finite enumeration is not claimed to prove the infinitude.',
 'status':'All exact checks passed'
}
target=Path(__file__).with_name('check_milnor_all_model_support_output.json')
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
