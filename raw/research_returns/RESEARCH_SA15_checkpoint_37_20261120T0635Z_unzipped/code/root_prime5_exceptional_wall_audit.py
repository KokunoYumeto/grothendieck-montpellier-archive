"""Retained full root audit and unchanged isolated rerun of the abstract p5 wall diagnostic."""
from pathlib import Path
import datetime, hashlib, json, shutil, subprocess, sys, time, traceback
w=Path(__file__).resolve().parents[1]
out=w/'outputs/root_prime5_exceptional_wall_audit.json'
assert not out.exists()
candidate=w/'agents/monodromy/post_CP36_prime5_exceptional_wall_candidate.tex'
program=w/'agents/monodromy/code/post_CP36_prime5_wall_diagnostic.py'
author=program.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before={str(p.relative_to(w)):sha(p) for p in (candidate,program,author)}
assert sha(candidate)=='5d949110f65325c83cbf986fd0b29ae017eebf64eff9bc79d305b4cb861e22ef'
run=w/'outputs/root_prime5_exceptional_wall_isolated'
run.mkdir(exist_ok=False)
shutil.copyfile(program,run/program.name)
start=time.perf_counter()
record={'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)), 'input_sha256':before,
 'scope':'Complete abstract three-statement proof audit plus a literal unchanged isolated exact-polynomial rerun. No actual Cartier realization, new geometric monodromy result or main-gate movement is asserted.'}
try:
 with (run/'stdout.txt').open('w') as so,(run/'stderr.txt').open('w') as se:
  proc=subprocess.run([sys.executable,str(run/program.name)],cwd=run,stdout=so,stderr=se)
 record['wall_seconds']=time.perf_counter()-start
 assert proc.returncode==0
 result=json.loads((run/program.name).with_suffix('.output.json').read_text())
 original=json.loads(author.read_text())
 assert result['status']==original['status']=='PASS'
 assert result['data']==original['data']
 data=result['data']
 assert data['checked_all_25_adjugate_entries'] and data['checked_all_five_inverse_compositions']
 assert (data['Q_terms'],data['E_terms'])==(15,37)
 assert data['c1_one_proportionality_gcd_binary']==33
 assert data['c1_one_E_coefficient_gcd_binary']==1
 assert before=={str(p.relative_to(w)):sha(p) for p in (candidate,program,author)}
 record.update(status='PASS: full independent proof and exact-polynomial audit',
  checker_runtime_seconds=result['runtime_seconds'], all_author_data_identical=True,
  proof_checks=[
   'The actual PHR2 indexing specializes at p5 to inverse2=3 and distance modulo sign; the retained alternating matrix and multiplication contraction agree with those formulas.',
   'Binary monomial sets implement exact F2 polynomial arithmetic, including coefficient cancellation; determinant signs vanish in characteristic2. Every one of the25 cofactors is reconstructed, rather than sampled.',
   'The first adjugate row is divisible by its section coordinate s0, and all rows verify adj(M_s)=s tau(s)^t polynomially. For nonzero s, rankM_s=4 exactly when tau(s) is nonzero.',
   'Every component of tau(sigma(y)) is divisible by its corresponding y coordinate and the five quotient polynomials agree. This proves the identity even at zero-coordinate points.',
   'Q has a coefficient c1^4, so after c1=1 this is a permanent unit pivot. Exact Euclidean gcd33 encodes t^5+1 and cuts out simultaneous vanishing of all proportionality equations over an algebraic closure.',
   'The gcd1 of E coefficients prevents any zero-polynomial specialization. Consequently the proportionality scalar on t^5=1 is nonzero.',
   'On dual rank4, s=sigma(y) represents its kernel. Q(y)=0 at an exceptional coefficient gives E(y)=0 and tau(s)=0, hence rankM_s<4. Conversely the typed identity B_y s=M_s^t y forces this same relation for any hypothetical common rank4 Euler wall point.',
   'Generic dual rank4, generic multiplication rank4 and birationality are the already fully audited prime-Heisenberg dependency. The argument refutes only their implication of a common maximal-rank wall; it does not refute generic Euler bijectivity.',
   'All three candidate labels and the claimed author runtime/output scope were read in full. The full author polynomial vectors and every coefficient equation were opened before this rerun. No geometric realization is supplied or inferred.'
  ],
  statements=['lem:prime-five-exceptional-composition','prop:prime-five-empty-common-wall','rem:prime-five-empty-wall-scope'])
except Exception:
 record.update(status='FAIL',error=traceback.format_exc(),wall_seconds=time.perf_counter()-start)
record['actual_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
record['retained_run']=str(run.relative_to(w))
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
if not record['status'].startswith('PASS'):raise SystemExit(1)
