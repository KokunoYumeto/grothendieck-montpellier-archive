#!/usr/bin/env python3
"""Literal isolated companion rerun; never writes to the author directory."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
OWN = ROOT / 'agents/monodromy'
AUTHOR = ROOT / 'agents/reduction_descent'
CANDIDATE = AUTHOR / 'B_uniform_wild_trace_arcs_candidate.tex'
PROGRAM = AUTHOR / 'code/verify_uniform_wild_trace_arcs.py'
OUTPUT = PROGRAM.with_suffix('.output.json')
EXPECTED = '7b3d5176da21e3d81c76e9fea88742dd9459f08112afbd3925d1d71ea688b7c2'
DEST = OWN / 'notes/B101_independent_audit_20261120'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(CANDIDATE) == EXPECTED
assert not DEST.exists(), 'Preserve any prior audit environment rather than replacing it'
DEST.mkdir(parents=True)
before = {str(p.relative_to(ROOT)): sha(p) for p in (CANDIDATE, PROGRAM, OUTPUT)}
shutil.copyfile(CANDIDATE, DEST / CANDIDATE.name)
shutil.copyfile(PROGRAM, DEST / PROGRAM.name)
shutil.copyfile(OUTPUT, DEST / 'author_output.json')
start = time.perf_counter()
proc = subprocess.run([sys.executable, str(DEST / PROGRAM.name)], cwd=DEST,
                      text=True, capture_output=True, timeout=60)
external_elapsed = time.perf_counter() - start
(DEST / 'stdout.txt').write_text(proc.stdout)
(DEST / 'stderr.txt').write_text(proc.stderr)
assert proc.returncode == 0, proc.stderr
actual = json.loads((DEST / PROGRAM.with_suffix('.output.json').name).read_text())
expected = json.loads(OUTPUT.read_text())
math = lambda d: {k:v for k,v in d.items() if k not in ('runtime_seconds', 'actual_utc')}
assert actual['status'] == 'PASS'
assert math(actual) == math(expected), 'Mathematical output differs'
after = {str(p.relative_to(ROOT)): sha(p) for p in (CANDIDATE, PROGRAM, OUTPUT)}
assert before == after, 'Author bytes changed'
record = {
    'status':'PASS', 'actual_utc':datetime.now(timezone.utc).isoformat(),
    'candidate_sha256':EXPECTED, 'author_hashes_before':before,
    'author_hashes_after':after, 'author_bytes_unchanged':True,
    'literal_program_copy_sha256':sha(DEST / PROGRAM.name),
    'runtime_seconds':actual['runtime_seconds'],
    'external_runtime_seconds':external_elapsed,
    'mathematical_fields_equal':True, 'counts':actual['counts'],
    'environment':str(DEST),
    'scope':'Unchanged finite symbolic/arithmetic certificate only; all infinite geometric and effectivity assertions are audited from the complete written proofs separately.'
}
target = OWN / 'outputs/independent_B101_exact_rerun.json'
assert not target.exists(), 'Preserve earlier audit output'
target.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
