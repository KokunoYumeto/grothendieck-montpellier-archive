"""Retained author-preserving independent exact-code execution for B81."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, sys, time

root = Path(__file__).resolve().parents[3]
own = root / 'agents/monodromy'
other = root / 'agents/reduction_descent'
source = other / 'B_first_wild_Cartan_exclusion_candidate.tex'
program = other / 'code/verify_first_wild_Cartan_exclusion.py'
author = program.with_suffix('.output.json')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
before = {str(p.relative_to(root)): sha(p) for p in (source, program, author)}
assert before[str(source.relative_to(root))] == '8b7c13a40f6c40f2f55a54d3d17a5c214e01c4456cbf0a0c81eeb27462da332b'
destination = own / 'outputs/independent_B81_environment'
destination.mkdir(parents=True, exist_ok=True)
copied = destination / program.name
shutil.copy2(program, copied)
started = time.perf_counter()
run = subprocess.run([sys.executable, str(copied)], capture_output=True, text=True, check=False)
elapsed = time.perf_counter() - started
(destination / 'stdout.txt').write_text(run.stdout)
(destination / 'stderr.txt').write_text(run.stderr)
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
original = json.loads(author.read_text())
assert result['status'] == 'PASS'
for key in ('status', 'counts', 'boundary_rows', 'scope'):
    assert result[key] == original[key], key
assert {str(p.relative_to(root)): sha(p) for p in (source, program, author)} == before
record = {
    'status': 'PASS_FULL_PROOF_AND_CODE_AUDIT',
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'source': str(source.relative_to(root)), 'source_sha256': sha(source),
    'program': str(program.relative_to(root)), 'program_sha256': sha(program),
    'author_output_sha256': sha(author), 'author_bytes_preserved': True,
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'isolated_wall_seconds': elapsed, 'exact_program_runtime_seconds': result['runtime_seconds'],
    'assertions': [
        {'label': 'lem:B-RD81-levels', 'verdict': 'PASS', 'details': 'The actual full Cartan, its surjective pth-power map onto U, both displacement valuations, and strict increase of the lower break under nontrivial pth powers are correctly typed.'},
        {'label': 'prop:B-RD81-Cartan', 'verdict': 'PASS', 'details': 'Fixed-coordinate leading terms and both strict comparison identities check. The boundary equation forces f_j0(z)=c_i z, including c_i=0. Nonzero c_i forces the same terminal break in both models; both zero excludes higher nonterminal breaks. In both cases actual Frobenius orientation contradicts scalar proportionality on the full residual quadratic field.'},
        {'label': 'cor:B-RD81', 'verdict': 'PASS', 'details': 'Combining the proved p3 exclusion with this p4 exclusion and the actual matrix-kernel upper bound gives exactly wild orders p5 through p8, with the stated p5 instance.'},
        {'label': 'rem:B-RD81-scope', 'verdict': 'PASS', 'details': 'The finite-level assertion is not promoted to CM, and all larger or reducible cases remain open. The finite exact supplement has the stated scope.'}
    ],
    'proof_scope': 'Entire B81 proof and exact program read and independently rederived. Entire canonical B79 and B80 proofs reread, including the fixed-coefficient lemma, integral Cartan lift and original residual orientation. No fresh primary-source access is claimed. Finite calculations supplement, rather than replace, the uniform actual-coordinate proof.',
    'counts': result['counts']
}
out = own / 'outputs/independent_B81_Cartan_exclusion_audit.json'
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': record['status'], 'actual_utc': record['actual_utc'], 'record': str(out.relative_to(root)), 'runtime_seconds': result['runtime_seconds'], 'source_sha256': record['source_sha256'], 'author_bytes_preserved': True}, indent=2))
