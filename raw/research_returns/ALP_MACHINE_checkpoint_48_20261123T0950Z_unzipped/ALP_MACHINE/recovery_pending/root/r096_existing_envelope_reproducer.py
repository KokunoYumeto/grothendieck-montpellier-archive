#!/usr/bin/env python3
"""Reproduce the failed support27 sufficient envelope; no theorem or charge."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from datetime import datetime, timezone
import hashlib
import json

B = Path(__file__).resolve().parents[2]
source = B / 'agents/unitary_transverse_compression_support_twenty_six.md'
source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
assert source_hash == 'f6a9266690c8e96397b41db9b5a5c90dde329582045fd2f2551507d8d91a9a62'
hostpath = B / 'agents/definite_oscillator_large_t_certificate.json'
host = next(r for r in json.loads(hostpath.read_text())['rows'] if r['host'] == 'J56')
g0,g1,T = (int(host[k]) for k in ('g0','g1','T'))
Q = g0*g1
U = 77*Q*Q-14
f,m,s,H = 168,164,27,133
D0 = 7**140*29**144*5**84*13**84
LT,LQ,LU,LH = F(1019333,1024),F(287843,4096),F(601356,4096),F(28900,4096)
assert Q == 1427908193729121522601
assert T**1024 < 2**1019333
assert Q**4096 > 2**287843 and U**4096 > 2**601356
assert H**4096 < 2**28900
assert 2*(T-1)**2 < 2**997*(T-2)
cap = 90
assert Q**167 * 2**(cap*f) < T**s
assert H**2 * 2**132 < U
assert 2250**2*164 < 4117**2*49
radius_numerator = 2**(cap-67)+4117
assert radius_numerator == 8392725
num = (528*radius_numerator**2)**(m*f)
den = factorial(m*f)*D0**m*2**(2*cap*m*f)
def strict_below_power(n,d,e):
    return n < d*2**e if e >= 0 else n*2**(-e) < d
rowceil = num.bit_length()-den.bit_length()
while not strict_below_power(num,den,rowceil):
    rowceil += 1
while strict_below_power(num,den,rowceil-1):
    rowceil -= 1
assert strict_below_power(num,den,rowceil)
assert not strict_below_power(num,den,rowceil-1)
assert rowceil == -4071532
zpower = 334*f-328*f-F(f,8)-f
assert zpower == 819
fixed = 1+668+168+8+107+5757+249
assert fixed == 6958
E = (fixed-F(929*f,2)+41*167*f+F(f,8)*(LH-1)-F(f,2)*LU
     -501*167*LQ+(344*LT+997)*s+rowceil-zpower*cap)
assert E == F(1289132235,4096) and E > 0
oldpath = B / 'recovery_pending/root/r096_existing_envelope_probe.json'
old = json.loads(oldpath.read_text())
for key,value in dict(support=s,z_cap_exponent=-cap,row_radius_numerator=radius_numerator,
                     row_radius_binary_denominator=cap,strict_row_volume_ceiling=rowceil,
                     complete_existing_envelope=str(E),source_sha256=source_hash).items():
    assert old[key] == value, key
result = dict(finding='AM-R-096-EXPLORATORY',completed_utc=datetime.now(timezone.utc).isoformat(),
              status='PASS_REPRODUCED_FAILED_SUFFICIENT_ENVELOPE_ONLY',
              source=str(source.relative_to(B)),source_sha256=source_hash,
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              host_sha256=hashlib.sha256(hostpath.read_bytes()).hexdigest(),
              historical_probe_sha256=hashlib.sha256(oldpath.read_bytes()).hexdigest(),
              historical_probe_utc=old['time_utc'],support=s,z_cap_exponent=-cap,
              row_radius_numerator=radius_numerator,row_radius_binary_denominator=cap,
              strict_row_volume_ceiling=rowceil,z_power=str(zpower),
              complete_existing_envelope=str(E),new_charge=None,
              scope='The unchanged complete DO111 VC12–22 upper envelope at support27 is positive. This gives no sufficient smallness estimate, contribution lower bound, existence, sign or impossibility of a sharper argument. Full source column, source fibre and paired finite weights remain. This execution is new; it is not backdated to the earlier inline probe.',
              canonical_mutations=False)
out = B / 'recovery_pending/root/r096_existing_envelope_replay.json'
assert not out.exists()
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
