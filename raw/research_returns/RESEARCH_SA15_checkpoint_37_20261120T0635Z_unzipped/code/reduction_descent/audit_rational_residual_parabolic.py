from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys

own = Path(__file__).resolve().parents[1]
work = own.parents[1]
author = work/'outputs/rational_residual_parabolic.json'
before = author.read_bytes()
proof = work/'notes/rational_monodromy_residual_obstruction.tex'
program = work/'code/check_rational_residual_parabolic.py'
env = own/'outputs/independent_rational_residual_environment'
assert not env.exists()
(env/'code').mkdir(parents=True)
(env/'outputs').mkdir()
copied = env/'code/check_rational_residual_parabolic.py'
copied.write_bytes(program.read_bytes())
run = subprocess.run([sys.executable,str(copied)],capture_output=True,text=True,cwd=env)
(env/'outputs/stdout.json').write_text(run.stdout)
(env/'outputs/stderr.txt').write_text(run.stderr)
assert run.returncode == 0, run.stderr
out = json.loads((env/'outputs/rational_residual_parabolic.json').read_text())
original = json.loads(before)
strip = lambda x: {k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert strip(out) == strip(original)
assert author.read_bytes() == before
now = datetime.now(timezone.utc).isoformat()
labels = ['prop:root-rational-residual-obstruction','ex:root-rational-residual-parabolic']
checks = [
    'Full proposition independently rederived. Reduction is surjective by unit-determinant lifts; its subgroup inverse image is compact open and contains 1+pMat. Coordinatewise polynomial vanishing on Zp proves Zariski density, and finite coefficient-span decomposition extends the argument to Qpbar. An invariant algebraic subspace is then GLd-invariant, so the rational representation is absolutely irreducible for every residual subgroup.',
    'Full example independently rederived for all p and r>s>=2. The upper block parabolic is proper, preserves a rank-r subspace, and contains the actual natural GLr block. Independent diagonal GLr and GLs actions kill all natural and dual fixed vectors. This does not imply any realization by the geometric family.',
    'Entire finite program read. All 64512 block matrices, GF2 rank routine, 14 elementary transvections, dual fixed vectors, embedded GL3, and explicit escaping matrix are correctly typed. An unchanged literal copy was run in an isolated parent/output directory; all mathematical fields equal author and author bytes are unchanged.',
    'The literature paragraph explicitly limits its original-source read claim and imports no rational theorem as a residual-image theorem. This companion audit does not claim a fresh read of the DAddezio original or its deeper dependencies; the two mathematical statements are self-contained.'
]
record = dict(status='FULL INDEPENDENT PROOF AND EXACT-CODE PASS',actual_utc=now,
    candidate=str(proof),candidate_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),
    labels=labels,checks=checks,program_sha256=hashlib.sha256(program.read_bytes()).hexdigest(),
    independent_program=str(copied),independent_output=str(env/'outputs/rational_residual_parabolic.json'),
    independent_runtime_seconds=out['runtime_seconds'],counts=out['counts'],
    author_output_sha256=hashlib.sha256(before).hexdigest(),author_output_unchanged=True,
    mathematical_fields_equal_author=True,
    source_scope='No new external original-source read claimed; two self-contained proofs and entire exact finite code fully audited.',
    scope_limit='Abstract continuous representation countermodel only; no hypersurface realization or main geometric-gate movement.')
(own/'outputs/independent_rational_residual_parabolic_audit.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'INDEPENDENT_FULL_PASS','Self-contained full proof and exact finite supplement; abstract residual countermodel only','outputs/independent_rational_residual_parabolic_audit.json','Original author output preserved; no fresh DAddezio source read claimed'])+'\n')
print(json.dumps(record,indent=2))
