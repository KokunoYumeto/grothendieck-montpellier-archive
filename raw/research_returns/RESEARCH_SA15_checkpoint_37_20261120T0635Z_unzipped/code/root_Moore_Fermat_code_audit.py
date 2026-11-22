"""Independently read/rerun the standalone exact Moore/Fermat certificate."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
source=w/'agents/obstructions_crystals/code/verify_Moore_Fermat_nondivisibility.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source_before=sha(source);author_before=sha(author)
dest=w/'code/audit_snapshots/Moore_Fermat_root_independent_certificate.py'
out=w/'outputs/root_Moore_Fermat_code_audit.json'
assert not dest.exists() and not out.exists()
shutil.copy2(source,dest)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_Moore_Fermat_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_Moore_Fermat_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text());independent=json.loads(dest.with_suffix('.output.json').read_text())
mathpart=lambda v:{k:x for k,x in v.items() if k not in ('actual_utc','runtime_seconds')}
assert mathpart(original)==mathpart(independent)
assert sha(source)==source_before==sha(dest) and sha(author)==author_before
prior=json.loads((w/'code/root_Moore_Fermat_divisibility_probe.output.json').read_text())
assert independent['remainder_sha256']==prior['remainder_table_sha256']
r={'status':'PASS: complete exact-code audit; written theorem audit pending',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'source':str(source.relative_to(w)),'source_sha256':source_before,
 'author_output':str(author.relative_to(w)),'author_output_sha256':author_before,
 'author_bytes_unchanged':True,
 'independent_program':str(dest.relative_to(w)),
 'independent_output':str(dest.with_suffix('.output.json').relative_to(w)),
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'independent_runtime_seconds':independent['runtime_seconds'],
 'author_runtime_seconds':original['runtime_seconds'],
 'subprocess_wall_seconds':wall,
 'all_mathematical_output_identical':True,
 'same_remainder_as_root_prior_independent_construction':True,
 'counts':independent['counts'],
 'code_checks':[
  'Read every line of the standalone program. Literal9! expansion uses characteristic-two parity and packed exponents bounded by9, so no four-bit exponent carry occurs. Monic elimination of x0^3 by the other eight cubes reconstructs the same1085 coefficients and47349 monomials as the earlier root construction.',
  'The squarefree x coefficient is exactly the cube of the total parameter-cube sum. Four parallel-line product-sum cubes have literal remainder coefficient locators. All511 nonzero supports are enumerated;399 have an actual single nonzero monomial witness. The other112 form the five recorded affine support orbits.',
  'All eight lower-support proof factors are reverified as literal restricted remainder coefficients. All432 affine transformations are distinct. The81 affine-line choices split9/72, and the six-element nonconcurrent stabilizer has zero-position orbits{0},{2,3,7},{1,5,6},{4,8}.',
  'Read the normal-form and explicit full-torus ideal identity, including the corrected cross-term multiples J1,J2,J3. Reduction modulo the four cube relations leaves precisely d^2*a*b*u*v*w*t. The independent-variable phase check represents cube roots in F4 exactly and supplies a nonzero single-monomial witness for all72 noncharacter patterns, not finite-field sampling of free parameters.',
  'The unique-zero argument itself requires the written orbit-case proof; the program does not replace that geometric-free algebraic deduction. The complete theorem will receive a separate proof audit.'
 ],
 'root_executed_failures':[],
 'retained_author_failure':'Initial full-torus ideal expression omitted a cubed-sum cross term; the author preserved exact failed version and streams before correction. This record concerns the corrected stable source only.',
 'scope':'Exact universal algebra code audit only. No Cartier coordinate identification, Hasse wall, full group or promoted theorem is inferred here.'}
out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ('status','actual_utc','source_sha256','independent_runtime_seconds','all_mathematical_output_identical','counts')},indent=2))
