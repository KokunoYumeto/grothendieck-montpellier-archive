from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess,time,sys
own=Path(__file__).resolve().parents[1]
other=own.parent/'obstructions_crystals'
program=other/'code/verify_Moore_Fermat_nondivisibility.py'
output=program.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before={'program':sha(program),'output':sha(output)}
run=own/'outputs/independent_Moore_Fermat_run'
run.mkdir(exist_ok=False)
copy=run/'verify_Moore_Fermat_nondivisibility.py'
copy.write_bytes(program.read_bytes())
start=time.perf_counter()
r=subprocess.run([sys.executable,str(copy)],cwd=run,text=True,capture_output=True)
wall=time.perf_counter()-start
(run/'stdout.txt').write_text(r.stdout)
(run/'stderr.txt').write_text(r.stderr)
assert r.returncode==0, r.stderr
after={'program':sha(program),'output':sha(output)}
assert before==after
author=json.loads(output.read_text())
independent=json.loads(copy.with_suffix('.output.json').read_text())
mathematical=lambda d:{k:v for k,v in d.items() if k not in ('runtime_seconds','actual_utc')}
assert mathematical(author)==mathematical(independent)
record={'status':'EXACT_CODE_PASS_FULL_PROOF_AUDIT_PENDING',
        'actual_utc':datetime.now(timezone.utc).isoformat(),
        'author_program':str(program),'author_output':str(output),
        'author_hashes':before,'author_hashes_unchanged':before==after,
        'independent_program':str(copy),'independent_output':str(copy.with_suffix('.output.json')),
        'independent_runtime_seconds':independent['runtime_seconds'],
        'subprocess_wall_seconds':wall,'counts':independent['counts'],
        'remainder_sha256':independent['remainder_sha256'],
        'all_mathematical_output_identical':True,
        'code_read_scope':'Entire literal determinant, monic remainder, support/affine orbit witnesses, repaired line-choice and zero-orbit checks, torus ideal identity, and independent-variable F4 phase exclusions read before execution.',
        'proof_scope':'Written full candidate not yet available at execution; this record alone does not pass the theorem.',
        'new_external_sources':[]}
(own/'outputs/independent_Moore_Fermat_code_audit.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
