#!/usr/bin/env python3
"""Run the exact certificates supplied with BR_PENCIL.

Dependencies are Python, NumPy and SymPy. Integer and rational arithmetic
are used throughout; modular arithmetic selects or certifies minors with
the stated field scope. Run from any working directory. Logs are preserved.
"""
from pathlib import Path
import json, subprocess, sys, datetime
here=Path(__file__).resolve().parent
jobs=[
 ('P-03--P-06',['check_pencils.py']),
 ('P-08',['check_finite_differences.py']),
 ('R-04',['check_permanent_apolar_certificate.py']),
 ('R-02,R-03,R-05',['verify_global_bounds.py']),
 ('R-06',['verify_five_by_two.py','five_by_two_extra.json']),
 ('P-09',['verify_det7_certificate.py']),
 ('P-12',['verify_det7_certificate.py','--certificate','det7_extra_m12_certificate.json']),
 ('P-10,P-11',['verify_adjacent_cubic.py']),
 ('P-13',['verify_seven_plane_certificate.py']),
 ('P-14',['verify_det7_certificate.py','--certificate','det7_extra_m11_certificate.json']),
 ('P-15',['check_support9_sevenplanes.py']),
 ('R-08',['verify_det7_global.py']),
 ('P-16',['verify_seven_plane_certificate.py','--certificate','per7_m11_certificate.json']),
 ('P-18-upper',['verify_polynomial_cubic_upper.py']),
 ('P-18-lower',['verify_polynomial_cubic_lower.py']),
 ('P-19',['check_per7_last_certificate.py']),
 ('R-10',['verify_per7_global.py']),
 ('R-11',['verify_uniform7.py']),
 ('P-18-Jacobian',['verify_nine_square_jacobian.py']),
 ('P-20',['check_per10_upper18.py']),
 ('P-17',['verify_det10_borel.py']),
 ('S-01',['check_certificates.py'])]
logdir=here/'verification_logs';logdir.mkdir(exist_ok=True)
records=[]
for finding,args in jobs:
 result=subprocess.run([sys.executable,*args],cwd=here,text=True,capture_output=True)
 suffix='__'+Path(args[-1]).stem if len(args)>1 else ''
 log=logdir/(Path(args[0]).stem+suffix+'.txt')
 log.write_text(result.stdout+result.stderr)
 item={'finding':finding,'checker':args[0],'exit_code':result.returncode,'status':'PASS' if result.returncode==0 else 'FAIL','log':str(log.relative_to(here))}
 records.append(item);print(json.dumps(item),flush=True)
 if result.returncode:print(result.stdout+result.stderr);break
out={'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'verification_type':'exact computation, not formal theorem proving','checks':records}
(here/'verification_summary.json').write_text(json.dumps(out,indent=2)+'\n')
if len(records)!=len(jobs) or any(x['exit_code'] for x in records):raise SystemExit(1)
print('All packaged certificate checks passed.')
