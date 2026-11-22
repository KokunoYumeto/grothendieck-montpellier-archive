"""Retain monodromy's complete independent B90 proof/code audit and literal rerun."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, time
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[3]
own = root / 'agents/monodromy'
source = root / 'agents/reduction_descent/B_p5_third_point_ramification_candidate.tex'
program = root / 'agents/reduction_descent/code/verify_p5_third_point_ramification.py'
author = program.with_suffix('.output.json')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(source) == '915d0471127a83c19d45fdefcd7696c92fedc5571e5785d3734e85fafaa732bd'
before = {str(p.relative_to(root)): sha(p) for p in (source,program,author)}
env = own / 'outputs/independent_B90_environment'
env.mkdir(exist_ok=False)
shutil.copy2(source, env/source.name)
shutil.copy2(program, env/program.name)
start = time.perf_counter()
run = subprocess.run([sys.executable,str(env/program.name)],cwd=env,text=True,capture_output=True)
wall = time.perf_counter()-start
(env/'stdout.txt').write_text(run.stdout)
(env/'stderr.txt').write_text(run.stderr)
assert run.returncode == 0, run.stderr
out = env/program.with_suffix('.output.json').name
actual = json.loads(out.read_text())
expected = json.loads(author.read_text())
omit = {'actual_utc','runtime_seconds'}
assert {k:v for k,v in actual.items() if k not in omit} == {k:v for k,v in expected.items() if k not in omit}
assert before == {str(p.relative_to(root)):sha(p) for p in (source,program,author)}
now = datetime.now(timezone.utc).isoformat()
assertions = [
 {'label':'lem:B-RD90-point-towers','verdict':'PASS','details':'Actual integral tame eigenbasis, stabilizers H_i/S_i, order-25 Galois point towers, two uniform inverse-Newton steps, all four displacement rows, tame congruences and fixed-coordinate first-prime-exponent exclusions were independently rederived. The two forced lower pairs are (606,6936) and (624,6834); no assertion that E_i^+/L is Galois is used.'},
 {'label':'prop:B-RD90-terminal','verdict':'PASS','details':'The equalities US_i=H_i and F_2 intersection E_i^+=E_i identify actual fields. Commutator and fifth-power identities make the indicated degree-625 composita elementary abelian. Distinct character conductors, lower subgroup restriction and exact Herbrand integration give terminal breaks 7896,11646,769146,937896. The quotient coset-average argument correctly identifies every break outside U.'},
 {'label':'thm:B-RD90-tame-exclusion','verdict':'PASS','details':'The actual cyclotomic determinant quotient has kernel order 15625. All nonidentity order-five determinant cosets include the trace carry and det(A) term. The stated counts give weighted sum 5925000, hence the actual normalized lower break 1896/5, contradicting integrality. This uses the exact quotient formula, not Hasse-Arf or an abstract realizability assumption.'},
 {'label':'rem:B-RD90-scope','verdict':'PASS','details':'Only the tame reducible residual branch is excluded. The unrestricted least-index interval and remaining wild/irreducible sectors are not closed. Finite arithmetic supplements the actual-field proof and is not asserted to realize a profile.'}
]
record = {'status':'PASS_FULL_PROOF_AND_CODE_AUDIT','actual_utc':now,
 'source':str(source.relative_to(root)),'source_sha256':sha(source),
 'program':str(program.relative_to(root)),'program_sha256':sha(program),
 'author_output_sha256':sha(author),'author_bytes_preserved':True,
 'independent_output':str(out.relative_to(root)), 'isolated_wall_seconds':wall,
 'exact_program_runtime_seconds':actual['runtime_seconds'],
 'all_mathematical_output_identical':True,'counts':actual['counts'],'assertions':assertions,
 'proof_scope':'Entire B90 candidate and entire unchanged exact verifier read and independently rederived. Complete B87 fixed-coordinate coefficient lemma and full-image proof, B88 point-field and full-filtration proofs, and B76 inverse-Newton setup and recurrence were freshly reread. Their already audited primary-source inputs are reused; no new primary-source opening or image view is claimed. Four exact determinant fibers and every listed finite arithmetic check were independently rerun with author bytes preserved.'}
dest = own/'outputs/independent_B90_third_point_ramification_audit.json'
assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for a in assertions:
  f.write('\t'.join([a['label'],now,'GPT-6 Astra Pro /root/monodromy; inherited effort','independent-proof-code','PASS: '+a['details']+' Record: '+str(dest.relative_to(root))])+ '\n')
print(json.dumps({k:record[k] for k in ('status','actual_utc','source_sha256','exact_program_runtime_seconds','author_bytes_preserved','counts')},indent=2))
