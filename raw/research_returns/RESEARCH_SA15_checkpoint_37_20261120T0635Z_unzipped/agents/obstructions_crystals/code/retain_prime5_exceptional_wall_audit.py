"""Retain a full, author-preserving independent audit of the p5 wall diagnostic."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'RESEARCH_SA15_paper.tex').exists())
OWN = ROOT / 'agents/obstructions_crystals'
AUTHOR = ROOT / 'agents/monodromy'
CANDIDATE = AUTHOR / 'post_CP36_prime5_exceptional_wall_candidate.tex'
PROGRAM = AUTHOR / 'code/post_CP36_prime5_wall_diagnostic.py'
OUTPUT = PROGRAM.with_suffix('.output.json')
RUN = OWN / 'outputs/prime5_exceptional_wall_independent_run'
RECORD = OWN / 'prime5_exceptional_wall_independent_audit.json'
assert not RUN.exists() and not RECORD.exists()
RUN.mkdir(parents=True)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

before = {str(p.relative_to(ROOT)): sha(p) for p in (CANDIDATE, PROGRAM, OUTPUT)}
copy = RUN / PROGRAM.name
shutil.copyfile(PROGRAM, copy)
assert sha(copy) == sha(PROGRAM)
start = time.perf_counter()
proc = subprocess.run([sys.executable, str(copy)], cwd=RUN, text=True, capture_output=True)
elapsed = time.perf_counter() - start
(RUN / 'stdout.txt').write_text(proc.stdout)
(RUN / 'stderr.txt').write_text(proc.stderr)
assert proc.returncode == 0, proc.stderr
author_data = json.loads(OUTPUT.read_text())
rerun_data = json.loads(copy.with_suffix('.output.json').read_text())
assert author_data['status'] == rerun_data['status'] == 'PASS'
omit = {'actual_utc', 'runtime_seconds'}
assert {k:v for k,v in author_data.items() if k not in omit} == {k:v for k,v in rerun_data.items() if k not in omit}
d = rerun_data['data']
assert d['checked_all_25_adjugate_entries'] and d['checked_all_five_inverse_compositions']
assert (d['Q_terms'], d['E_terms']) == (15, 37)
assert d['c1_one_proportionality_gcd_binary'] == 33
assert d['c1_one_E_coefficient_gcd_binary'] == 1
after = {str(p.relative_to(ROOT)): sha(p) for p in (CANDIDATE, PROGRAM, OUTPUT)}
assert before == after
now = datetime.now(timezone.utc).isoformat()
checks = {
    'lem:prime-five-exceptional-composition': 'All five Pfaffians and 25 cofactors reconstructed in the exact GF(2) coefficient ring. Adjugate row/column orientation is correct: adj(M)[i,j] is cofactor(j,i), and division of row zero by s0 gives tau_j. All five compositions have the common polynomial quotient E after division by y_j. Every zero-coordinate specialization is covered by the polynomial identities. The coefficient pivot is exactly c1^4, hence becomes 1; coefficient gcd(E)=1 ensures E never vanishes identically and the proportionality gcd t^5+1 gives precisely the claimed exceptional ratios over an algebraically closed field.',
    'prop:prime-five-empty-common-wall': 'The previously fully audited prime-five theorem supplies generic dual/multiplication rank four and a birational radical. If Q(y)=0 at a dual-maximal point, the exact composition identity with E proportional to Q gives tau(sigma(y))=0, so every cofactor of M vanishes. Conversely, simultaneous maximal ranks identify s projectively with sigma(y_s); the Euler incidence condition is then exactly Q(y_s)=0. Thus the proposed common maximal-rank wall is empty. No specialization of a full local-system fibre across a rank drop is used.',
    'rem:prime-five-empty-wall-scope': 'This is an abstract Heisenberg tensor counterexample to a common-wall inference. It preserves generic Euler bijectivity and does not assert actual Cartier realizability, a monodromy counterexample, an abelian-surface embedding, or a classification of the contracted image.'
}
record = {
    'status': 'FULL PROOF AND CODE PASS', 'actual_utc': now,
    'candidate': str(CANDIDATE.relative_to(ROOT)), 'candidate_sha256': sha(CANDIDATE),
    'labels': checks, 'author_hashes_before': before, 'author_hashes_after': after,
    'program_run': {'isolated_exact_copy': str(copy.relative_to(ROOT)),
                    'internal_runtime_seconds': rerun_data['runtime_seconds'],
                    'wall_runtime_seconds': elapsed, 'exit_code': proc.returncode,
                    'mathematical_output_identical': True, 'excluded_fields': sorted(omit),
                    'output': str(copy.with_suffix('.output.json').relative_to(ROOT))},
    'read_scope': 'Entire written three-label candidate, entire standalone binary-polynomial program and every coefficient/exponent of the full author output read. All written and exact reconstruction steps independently rederived.',
    'dependencies': ['agents/obstructions_crystals/prime_Heisenberg_independent_audit.json',
                     'agents/obstructions_crystals/prime_Heisenberg_cocycle_delta_audit.json'],
    'new_external_source_import': None,
    'scope': 'Full abstract polynomial and consequence audit only. No new actual-Cartier realization or geometric classification is inferred.'
}
RECORD.write_text(json.dumps(record, indent=2) + '\n')
with (OWN / 'CHECK_EVENTS.tsv').open('a') as stream:
    for label, detail in checks.items():
        stream.write('\t'.join([now, label, 'independent-full-proof-code-audit',
                                 str(CANDIDATE.relative_to(ROOT)),
                                 'Entire proof/program read and exact author-preserving isolated rerun',
                                 'PASS: ' + detail, str(RECORD.relative_to(ROOT))]) + '\n')
print(json.dumps({'status': record['status'], 'actual_utc': now,
                  'record': str(RECORD.relative_to(ROOT)), 'candidate_sha256': sha(CANDIDATE),
                  'runtime_seconds': rerun_data['runtime_seconds']}))
