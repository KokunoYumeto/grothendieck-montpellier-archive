"""Record the completed root B80 proof audit and isolated literal rerun."""
from pathlib import Path
import csv, datetime, hashlib, json, shutil, subprocess, sys, time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_first_wild_fourth_layer_candidate.tex'
source=w/'agents/reduction_descent/code/verify_first_wild_fourth_layer.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='fc7d5bf4a947feb60de702f1d16c7432a8fddd6480f6f42f9dff7317f21f386e'
assert sha(candidate)==expected
before=sha(author); source_before=sha(source)
dest=w/'code/audit_snapshots/B80_root_independent_certificate.py'
out=w/'outputs/root_B80_audit.json'
snapshot=w/'notes/root_B80_audited_candidate.tex'
assert not dest.exists() and not out.exists() and not snapshot.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
started=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],capture_output=True,text=True,cwd=w)
wall=time.perf_counter()-started
(w/'outputs/root_B80_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_B80_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=json.loads(dest.with_suffix('.output.json').read_text())
original=json.loads(author.read_text())
def mathematical(x):return {k:v for k,v in x.items() if k not in ('runtime_seconds','actual_utc')}
assert mathematical(independent)==mathematical(original)
assert sha(author)==before and sha(source)==source_before and sha(dest)==source_before
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={
 'status':'PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,
 'labels':['lem:B-RD80-first','prop:B-RD80-three-terminal','lem:B-RD80-plane',
           'lem:B-RD80-orientation','thm:B-RD80','rem:B-RD80-scope'],
 'proof_scope':'All 348 lines of the final candidate and all 135 lines of its checker were read. Every argument was checked at the stated first-wild absolute ramification and actual third torsion level.',
 'proof_checks':[
  'The actual common-field valuations give A=p(p-1) and v_F(p)>q^2 A. Fixed representatives are invariant under the group; the truncated calculation is characteristic p. At either D=qA or D=q^2 A the leading p-divisible degree and first prime degree exhaust the earliest binomial changes.',
  'For a low break, cancellation forces j=A+(p-1)b, its nonzero coefficient C z d_g^(p-1), and p not dividing b. For a high break, the unique first prime degree is D-b. The same chosen point expansions are used for every element.',
  'All tame-invariant three-dimensional terminal planes are treated: an irreducible full anti-Cartan for h>2, a full anti-Cartan with one or two breaks when h=2, and Z plus an anti line. The full-plane leading coefficient map is injective; scalar proportionality contradicts Frobenius orientation. The anti conjugacy factor a^(1-p) is included.',
  'The equal two-dimensional layers form a Lie algebra. A nonabelian derived line is nilpotent by traces of E and E^2, so it has a tame-invariant rational kernel. The dual-number plane has the same obstruction.',
  'The split-Cartan exclusion constructs an actual matrix lift with B11=0 and a primitive v=e1+p w, w2=-B21. Its order-p^2 stabilizer forces an orbit of order at most p^2, contrary to the exact p^3 valuation denominator. No invalid residual-rank orbit shortcut is used.',
  'For the nonsplit plane the exact commutator is trivial, and the pth-power image has rank two, giving W=(Z/p^2)^2. An outside-normalizer tame element has exact plus/minus projectors on W; its anti generator and its pth power contradict the unique fixed first prime coefficient at the two displacement levels.',
  'The aligned original Cartan makes the prime-to-p tame action on W trivial. The actual tame matrix generates an unramified quadratic algebra modulo p^3, the module is free of rank one, and the centralizer acts by multiplication. Equal cardinalities give the entire principal-unit subgroup.',
  'The conclusion is finite-level only: it does not supply a CM action on the full BT group, exclude or construct the p^4 branch, or decide the reducible residual and p^5 through p^8 branches.'
 ],
 'dependencies_freshly_read':[
  'B_first_wild_irreducible_image.tex: all 266 lines, including full valuation, denominator, matrix-layer, common-field leading-coordinate and orientation proofs.',
  'B_tame_cubic_wild_exhaustion.tex: complete B57 first-term, full anti-plane and remaining Cartan-line lemma proofs, lines1 through176; the later theorem proof is not claimed as freshly read here.',
  'B_tame_reducible_newton.tex: complete B60 lower-break lemma and proof, lines26 through58.'
 ],
 'primary_source_scope':'No new original-source proof read for this audit. The exact earlier Stacks032A coefficient-ring proof read for B78 is reused at its recorded scope; the internal coefficient calculation is fully rederived here.',
 'program':str(source.relative_to(w)),'program_sha256':source_before,
 'isolated_program':str(dest.relative_to(w)),
 'author_output_sha256_before_and_after':before,
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'independent_runtime_seconds':independent['runtime_seconds'],'wall_seconds':wall,
 'author_runtime_seconds':original['runtime_seconds'],
 'all_mathematical_output_fields_equal':True,'counts':independent['counts'],
 'executed_failures':[],
 'checkpoint_scope':'Post-CP28 audit. CP28 is unchanged; canonical promotion and CP29 integration are separate.'
}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in record['labels']:
  writer.writerow([label,now,record['reviewer'],'targeted proof check / unchanged independent exact-program rerun',
   'PASS: full final proof and checker read, actual lift and coefficient arguments rederived, copied checker passed with equal mathematical fields and unchanged author outputs. See outputs/root_B80_audit.json.'])
 for label in ['lem:B-RD79-layers','prop:B-RD79-minimal','lem:B-RD57-first-term','lem:B-RD57-anti','lem:B-RD57-Cartan','lem:B-RD60-break']:
  writer.writerow([label,now,record['reviewer'],'used and rechecked in this run',
   'Complete dependency proof freshly reread for B80, with its actual scope retained and coefficient calculation explicitly rederived at both target levels. See outputs/root_B80_audit.json.'])
print(json.dumps(record,indent=2))
