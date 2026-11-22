from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work')
OWN = ROOT / 'agents/reduction_descent'
AUTHOR = ROOT / 'agents/monodromy'
source = AUTHOR / 'post_CP32_birational_Pfaffian_height_two_counterexample_candidate.tex'
program = AUTHOR / 'code/verify_birational_Pfaffian_height_two.py'
author_output = AUTHOR / 'outputs/birational_Pfaffian_height_two_checks.json'
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
before = {str(p): sha(p) for p in (source, program, author_output)}
run = OWN / 'outputs/independent_Pfaffian_height_two_run'
assert not run.exists()
(run / 'code').mkdir(parents=True)
copy = run / 'code' / program.name
shutil.copyfile(program, copy)
assert sha(copy) == sha(program)
result = subprocess.run([sys.executable, str(copy)], cwd=run, capture_output=True, text=True)
(run / 'stdout.txt').write_text(result.stdout)
(run / 'stderr.txt').write_text(result.stderr)
assert result.returncode == 0, result.stderr
actual = json.loads((run / 'outputs/birational_Pfaffian_height_two_checks.json').read_text())
expected = json.loads(author_output.read_text())
ignore = {'actual_utc', 'runtime_seconds'}
assert {k:v for k,v in actual.items() if k not in ignore} == {k:v for k,v in expected.items() if k not in ignore}
assert before == {str(p):sha(p) for p in (source, program, author_output)}
record = {
    'status': 'PASS',
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'candidate': str(source),
    'candidate_sha256': sha(source),
    'program_sha256': sha(program),
    'author_output_sha256': sha(author_output),
    'author_bytes_preserved': True,
    'unchanged_isolated_program': str(copy),
    'runtime_seconds': actual['runtime_seconds'],
    'all_mathematical_output_identical': True,
    'labels': ['prop:abstract-birational-Pfaffian-height-two', 'cor:abstract-Pfaffian-common-incidence', 'rem:abstract-Pfaffian-height-two-scope'],
    'full_proof_scope': [
        'Read the complete three-assertion candidate and rederived the unique nonzero perfect matching for every deleted vertex in arbitrary odd size N=2m+1, m>=2.',
        'Checked the exact raw Pfaffian common factor x0^(m-2), coprimality after removal, and both explicit rational inverse polynomial identities for arbitrary m.',
        'Recomputed the radical of the reduced homogeneous base ideal as the intersection of the displayed codimension-two and codimension-three monomial primes; neither component contains the other.',
        'Reconstructed the alternating bilinear tensor, the reciprocal section contraction, both ranks at the displayed common pair, and the inverse left-kernel map on the dense common-rank locus.',
        'Read the entire dependency-free checker, including sparse F2 arithmetic, matching recursion, support hitting-set enumeration, tensor reconstruction, inverse identities and independent binary rank computations at N=5,7,9,11,13.',
        'The uniform mathematical proof is independent of the five finite sizes. No actual Cartier tensor, Lang reducibility, monodromy failure or global image conclusion is inferred.'
    ],
    'primary_source_scope': 'No new original-source reading is claimed by this record. The mathematical counterexample is self-contained; the final comparative bibliography paragraph is not used as a theorem input.',
    'executed_failures': [],
    'output': str(run / 'outputs/birational_Pfaffian_height_two_checks.json')
}
out = OWN / 'outputs/independent_Pfaffian_height_two_audit.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status':record['status'], 'actual_utc':record['actual_utc'], 'candidate_sha256':record['candidate_sha256'], 'runtime_seconds':record['runtime_seconds'], 'record':str(out), 'author_bytes_preserved':True}))
