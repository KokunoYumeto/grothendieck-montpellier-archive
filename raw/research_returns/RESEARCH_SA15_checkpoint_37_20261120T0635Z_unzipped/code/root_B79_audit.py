"""Record the completed root B79 proof audit and an isolated literal rerun."""
from pathlib import Path
import csv, datetime, hashlib, json, shutil, subprocess, sys, time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_first_wild_irreducible_image_candidate.tex'
source=w/'agents/reduction_descent/code/verify_first_wild_irreducible_image.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='89fe8a1c7e95c145738418c7f9d852a4cfb4a032506887d1a41266e72b697870'
assert sha(candidate)==expected
before=sha(author)
assert sha(source)=='fbd336f0d87b85da07d8ed37dc6927ebdc87fc034332c22e41e3c07b27d1c5fc'
dest=w/'code/audit_snapshots/B79_root_independent_certificate.py'
out=w/'outputs/root_B79_audit.json'
assert not dest.exists() and not out.exists()
shutil.copy2(source,dest)
proof_snapshot=w/'notes/root_B79_audited_candidate.tex'
assert not proof_snapshot.exists()
shutil.copy2(candidate,proof_snapshot)
started=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],capture_output=True,text=True,cwd=w)
wall=time.perf_counter()-started
stdout=w/'outputs/root_B79_independent_stdout.json'
stderr=w/'outputs/root_B79_independent_stderr.txt'
stdout.write_text(run.stdout);stderr.write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=json.loads(dest.with_suffix('.output.json').read_text())
original=json.loads(author.read_text())
def mathematical(x):return {k:v for k,v in x.items() if k not in ('runtime_seconds','actual_utc')}
assert mathematical(independent)==mathematical(original)
assert sha(author)==before
assert sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={
 'status':'PASS', 'actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)), 'candidate_sha256':expected,
 'labels':['lem:B-RD79-layers','prop:B-RD79-minimal','cor:B-RD79','rem:B-RD79-scope'],
 'proof_scope':'All four assertions and every paragraph of their proofs/scope were read in full. The exact actual torsion and common division-field hypotheses are retained.',
 'proof_checks':[
  'Residual irreducibility kills wild first-level action and forces one valuation. The good extension of degree N is legitimate at arbitrary absolute ramification by the full B49 inertia proof.',
  'The entire inverse Newton polygon gives e/q^(j-1) for exact order p^j. The primitive p^3 denominator forces wild order at least p^3, with the actual reduction-kernel upper order p^8.',
  'The literal pth-power identity gives W1 subset W2. If W1=0, a primitive point has at most p^2 conjugates; this exact special case suffices. Sum of layer dimensions three forces dimensions (1,2). No broader evaluation-rank orbit estimate is used.',
  'At the minimal full division-field degree, every primitive third-level coordinate has integral valuation A=p-1. The complete fixed-coefficient uniformizer expansion has its nonzero first change at A+b; all higher-degree terms change later.',
  'Every nonidentity element of the actual dimension-two terminal kernel therefore moves every primitive point, has break (q^2-1)A, and acts by field multiplication on the normalized leading Fq plane.',
  'Multiplication by p^2 transports leading coordinates through q^2 power, which fixes Fq. The common tame residual action is rederived as c+e, without importing the e=p-1 restriction of B53.',
  'Different special characters require Frobenius orientation. Its conjugation rule on the full terminal Cartan plane contradicts the scalar ratio of the two common-field leading coefficients.',
  'The conclusion excludes only minimal wild order p^3 with irreducible residual inertia; larger orders and reducible residual modules remain open. No actual model existence is inferred from finite image sizes.'
 ],
 'dependencies_freshly_read':[
  'B_tame_minimal_wild_layer.tex: complete B55 valuation lemma and minimal-image proposition, including fixed-coefficient proof and leading-coordinate transport.',
  'B_tame_residual_cycle.tex: complete B53 leading-coordinate lemma and adjacent-type proposition; only the direct leading-action argument is reused at the new index.',
  'B_tame_reducible_newton.tex: complete B60 lower-break lemma and proof.',
  'B_tame_minimal_height_two.tex: complete B49 good tame inertia lemma and proof.'
 ],
 'primary_source_scope':'The original Stacks032A proof was freshly read earlier for B78; its exact read scope is reused. Earlier original Tate/Honda/descent audits remain at their recorded scope. No additional fresh external theorem read is asserted for B79.',
 'program':str(source.relative_to(w)), 'program_sha256':sha(source),
 'isolated_program':str(dest.relative_to(w)),
 'author_output_sha256_before_and_after':before,
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'independent_runtime_seconds':independent['runtime_seconds'],
 'wall_seconds':wall, 'author_runtime_seconds':original['runtime_seconds'],
 'all_mathematical_output_fields_equal':True,
 'counts':independent['counts'],
 'executed_failures':[],
 'checkpoint_scope':'Post-CP28 root audit. CP28 remains immutable. Promotion and CP29 integration are separate actions.'}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in record['labels']:
  writer.writerow([label,now,record['reviewer'],'targeted proof check / unchanged independent exact-program rerun',
   'PASS: complete proof and dependencies read; literal copied checker passed; every mathematical output field matches; original output unchanged. Exact scope outputs/root_B79_audit.json.'])
 for label in ['lem:B-RD55-valuations','prop:B-RD55-minimal-wild','lem:B-RD53-leading','lem:B-RD60-break','lem:B-RD49-inertia']:
  writer.writerow([label,now,record['reviewer'],'used and rechecked in this run',
   'Complete stated dependency proof freshly reread for B79; arbitrary-index leading orientation rederived, not assumed from a restricted theorem. See outputs/root_B79_audit.json.'])
print(json.dumps(record,indent=2))
