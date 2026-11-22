"""Retain the full root B84 proof audit and unchanged isolated exact rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_tame_residual_one_prime_recovery_candidate.tex'
source=w/'agents/reduction_descent/code/verify_tame_residual_one_prime_recovery.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='f08414cd26b408769ae16b0fcead57b758ea5e14df2569d396f077834f2950e9'
assert sha(candidate)==expected
assert sha(source)=='270960bfb0edf3a59d349b5bffd79956c3acdddaeffff0e1ee241cb047c711ac'
before=sha(author)
dest=w/'code/audit_snapshots/B84_root_independent_certificate.py'
snapshot=w/'notes/root_B84_audited_candidate.tex';out=w/'outputs/root_B84_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_B84_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_B84_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text());independent=json.loads(dest.with_suffix('.output.json').read_text())
mathematical=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathematical(original)==mathematical(independent)
assert sha(author)==before and sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,
 'labels':['prop:B-RD84-tame','cor:B-RD84-first-wild','rem:B-RD84-scope'],
 'proof_scope':'Entire three-assertion candidate and exact checker read. Full lower-break proof, full B82 Newton proof and full B77 finite-pattern corollary freshly reread. The arbitrary-index point-field and both displacement comparisons independently rederived.',
 'proof_checks':[
  'The arbitrary-e inverse polygon uses the universal coefficient inequalities already fully checked in B82, not the prime-to-p scope of a former conclusion. The rational low first-level coordinate has valuation b, and every primitive lift over it has valuation b/q. The parameter range is 0<b<e.',
  'The actual p²-torsion isomorphism identifies the point stabilizers. Since first-level points are L-rational, every conjugate P+Q lies in L(P), making the point field Galois of degree at mostq. One prime b gives denominatorq, so the degree is exactlyq and all first-level translations occur. This imposes no bound on the full division field.',
  'The fixed-representative lower-break lemma applies to this actual degree-q field. The first coordinate has valuation b1 prime to p and therefore exact displacement b1+r(g); the second has the unconditional lower bound b2+r(g), even when divisible byp.',
  'If the high lines differed, a nonzero translation high in the first and low in the second would contradict the cross inequality. Its maximum over both b_i<=e-1 is -q(p+1), strictly negative. Thus the high lines align.',
  'A low translation and a high translation in the same field give (q-1)(b2-b1)>=0 and (p³+1)(b1-b2)>=0. Consequently b1=b2, and the identified exact tame high-line characters recover c1=c2 moduloN.',
  'In the first-wild tame reducible branch, B77 excludes the one-slope scalar/square case. Rational first-level modules give B_i=p b_i. If either b_i were prime the proposition would recover the characters, so B_i=p²k_i with1<=k_i<=p-2. An aligned high line and the determinant congruence would recover k_i and c_i; the remaining high lines must be exchanged.',
  'Atp5, the justified common finite twist normalizes c_i=1 modulo4 without changing good-model parameters. B_i=c_i modulo6 forces k_i odd. Exact residual exponents permit only (25,1;75,9) or (25,13;75,21), up to interchange. Their finite types are A/B and C/B; the common quadratic twist interchanges A,C and fixes B. Thus only A/B remains up to that twist in this residual-tame sector.',
  'The {35,75} and {55,75} exploratory tame patterns are excluded at every full-image size. The surviving {25,75} pattern is a necessary parameter restriction, not a constructed torsion-congruent pair. Other residual types and the unrestricted first-wild index{2,3} remain open.'
 ],
 'dependencies_read_scope':'Fresh full lem:B-RD60-break, lem:B-RD82-Newton and cor:B-RD77 with proof; prior complete root B83 quotient and common-field audit retained. The direct determinant normalization is the already audited B50/B77 twist, not a new source claim.',
 'primary_source_scope':'No new original-source reading for B84; universal coefficient sources retain their previously audited exact scope. The new small-point-field proof is direct.',
 'program':str(source.relative_to(w)),'program_sha256':sha(source),
 'isolated_program':str(dest.relative_to(w)),
 'author_output_sha256_before_and_after':before,
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'independent_runtime_seconds':independent['runtime_seconds'],'wall_seconds':wall,
 'author_runtime_seconds':original['runtime_seconds'],'all_mathematical_fields_equal':True,
 'counts':independent['counts'],'normalized_p5_rows':independent['normalized_p5_rows'],
 'executed_failures':[]}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in record['labels']:
  writer.writerow([label,now,record['reviewer'],'targeted proof check / unchanged independent exact-program rerun',
   'PASS: entire proof and checker read; arbitrary-e point field, every translation and both break comparisons rederived. Exact p5 pattern scope checked. All mathematical fields agree and author bytes remain unchanged. See outputs/root_B84_audit.json.'])
 for label in ['lem:B-RD60-break','lem:B-RD82-Newton','cor:B-RD77']:
  writer.writerow([label,now,record['reviewer'],'used and rechecked in this run',
   'Entire invoked lower-break, universal Newton or finite-pattern corollary proof freshly reread for B84; exact scope in outputs/root_B84_audit.json.'])
print(json.dumps(record,indent=2))
