"""Retain the full root B85 proof audit and unchanged isolated exact rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_first_wild_diagonal_projection_candidate.tex'
source=w/'agents/reduction_descent/code/verify_first_wild_diagonal_projection.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='7ae032b8394c8209094c53cdbf26d13d23868fd3c39ab026841527f9dd65cb18'
assert sha(candidate)==expected
assert sha(source)=='6e7307002a4682c7121a7aec0a6ae02d3273c1cd57114ad07e3989e1e73bcbb5'
before=sha(author)
dest=w/'code/audit_snapshots/B85_root_independent_certificate.py'
snapshot=w/'notes/root_B85_audited_candidate.tex';out=w/'outputs/root_B85_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_B85_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_B85_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text());independent=json.loads(dest.with_suffix('.output.json').read_text())
mathematical=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathematical(original)==mathematical(independent)
assert sha(author)==before and sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,
 'labels':['lem:B-RD85-diagonal','cor:B-RD85-tame','rem:B-RD85-scope'],
 'proof_scope':'Entire three-label candidate and exact checker read. Entire B60 lower-break proof, B69 comparison and actual quotient proofs, and B83 tame point-field, opposite quotient and Lie-layer proofs freshly reread. Root independently rederived both inverse slopes and the incompatible equal-break identities.',
 'proof_checks':[
  'The B83 actual quotient lattice formula detects both off-diagonal projections of the original actual first matrix layer. This implication needs no congruence restriction on p and no independent realizability of abstract matrices.',
  'If A11 vanishes, evaluation W1 e1 is the entire line Fp e2 because its21 projection is nonzero. A primitive second-level point above e1 therefore has exactlyp conjugates. All first-level translations are L-rational, so its point field is Galois; the actual torsion isomorphism identifies the two point fields and their automorphisms.',
  'The high inverse target has valuation p(N-pk1). Its degree-p vertex lies strictly above the degree-q chord because p²k1>N-pk1; the linear and intermediate vertices satisfy the universal coefficient bounds. This is a direct use of the coefficient proof at the new index, not an invocation of B69 conclusions beyond their prime-to-p scope.',
  'The two coordinate valuations in the degree-p field are N-pk1 and k2, positive and prime top for1<=ki<=p-2. The low/high translation by e2 has respective displacement valuations qk1 and q(N-pk2). Formal addition changes the coordinate by the translating parameter times a unit.',
  'The exact same lower break must equal p(p+1)k1-N and qN-(p³+1)k2. Equality forces p(p+1)k1+(p³+1)k2=p4-1. Maximizing both parameters leaves the strictly positive gap(p+1)(p²+1), a contradiction. Swapping models and basis vectors excludes vanishing22.',
  'Forp=1mod4, the nonsquare residual ratio has three distinct conjugation weights1,ratio,ratio-inverse. The tame projectors isolate both off-diagonals and a nonzero diagonal part, giving dimensionW1>=3. Actual pth powers embed W1 inW2, giving dimensionW2>=3 and exact group order at leastp6.',
  'The p5 order15625 bound and the necessary{25,75} A/B pattern apply only to the tame reducible sector. No existence, exclusion of larger groups, other-residual p6 bound, or unrestricted least-index improvement is claimed. Zero terminal trace alone is explicitly not used to annihilate the full determinant.'
 ],
 'dependencies_read_scope':'Full freshly reread lem:B-RD60-break; lem:B-RD69-rules and lem:B-RD69-quotients; lem:B-RD83-tame, lem:B-RD83-quotients and prop:B-RD83-Lie. B84 and its finite-pattern application were fully audited separately in the retained root B84 record.',
 'primary_source_scope':'No new original-source reading is claimed for B85. The original universal coefficient source retains its earlier recorded scope; the new point-field and lower-break comparison is direct.',
 'program':str(source.relative_to(w)),'program_sha256':sha(source),'isolated_program':str(dest.relative_to(w)),
 'author_output_sha256_before_and_after':before,'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'independent_runtime_seconds':independent['runtime_seconds'],'wall_seconds':wall,
 'author_runtime_seconds':original['runtime_seconds'],'all_mathematical_fields_equal':True,
 'counts':independent['counts'],'small_prime_rows':independent['small_prime_rows'],
 'executed_failures':[],'checkpoint_scope':'Post-CP30-build candidate; no edit to the frozen CP30 canonical paper.'}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in record['labels']:
  writer.writerow([label,now,record['reviewer'],'targeted proof check / unchanged independent exact-program rerun','PASS: full candidate and checker read; actual degree-p point field, both prime-valued coordinates and incompatible break identities independently rederived. All mathematical output fields agree; author bytes unchanged. See outputs/root_B85_audit.json.'])
 for label in ['lem:B-RD60-break','lem:B-RD69-rules','lem:B-RD69-quotients','lem:B-RD83-tame','lem:B-RD83-quotients','prop:B-RD83-Lie']:
  writer.writerow([label,now,record['reviewer'],'used and rechecked in this run','Entire invoked proof freshly reread for B85; exact scope retained in outputs/root_B85_audit.json.'])
print(json.dumps(record,indent=2))
