"""Full actual proof/code audit and unchanged isolated certificate rerun for B91."""
from pathlib import Path
import csv, datetime, hashlib, json, shutil, subprocess, sys, time
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=w/'agents/reduction_descent/B_residual_wild_high_quotient_candidate.tex'
source=w/'agents/reduction_descent/code/verify_residual_wild_high_quotient.py'
author=source.with_suffix('.output.json')
expected='a4cdbaf120302a26842df27c6eef3f428ff81cef454c573a314d3a476410c065'
assert sha(candidate)==expected
assert sha(source)=='e683a8e471c451104bd92be36c55db20cef005e7a91c1ec3293094b54dbc9d9e'
assert sha(author)=='40d3e0a114690187797c38faaed161dafaa5d039620da213d84083f61fbbe0c4'
before={str(p.relative_to(w)):sha(p) for p in (candidate,source,author)}
folder=w/'code/audit_snapshots/B91_root_independent'
assert not folder.exists()
folder.mkdir(parents=True)
copy=folder/source.name
shutil.copy2(source,copy)
snapshot=w/'notes/root_B91_audited_candidate.tex'
out=w/'outputs/root_B91_audit.json'
assert not snapshot.exists() and not out.exists()
shutil.copy2(candidate,snapshot)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(copy)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_B91_independent.stdout.json').write_text(run.stdout)
(w/'outputs/root_B91_independent.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=copy.with_suffix('.output.json')
a=json.loads(author.read_text());b=json.loads(independent.read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathpart(a)==mathpart(b)
assert before=={str(p.relative_to(w)):sha(p) for p in (candidate,source,author)}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:B-RD91-first-break','prop:B-RD91-divisibility','prop:B-RD91-parameters','thm:B-RD91-large','rem:B-RD91-scope']
r={'status':'FULL-INDEPENDENT-PROOF-CODE-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire final five-label candidate and entire exact finite checker actually read. Complete B60 break proof, B69 quotient proof, B82 Newton proof, B84 recovery proof, and B86 cyclotomic lemma freshly reread in canonical files.',
 'proof_checks':[
  'The common nontrivial residual unipotent group has unique fixed high line; every outside first-level point generates the same actual cyclic degree-p field R. Prime coordinate valuation gives the exact break ps-(p+1)B1; the second coordinate gives the unconditional inequality B1>=B2, strict for differing p-divisibility.',
  'The actual quotient p^2 module is the displayed subquotient of original p^3. The old-image valuation identifies high or low status without replacing the level. Below e two distinct stable lines and a p-group residual image make quotient first torsion L-rational; at equality the injective leading-coordinate map does so. Above e a prime parameter forces a nonintegral low coordinate and nontrivial residual degree p.',
  'The both-below case invokes B84 with D1/p=B1 prime; the crossing case contradicts rational versus wild quotient torsion, including B2=e; the both-above case reverses the strict first-break inequality through D=s-B. Thus both original parameters must be divisible by p.',
  'At p=5 the normalized high-character and determinant congruences give odd b_i in1..19 and b1=b2 modulo4. Applying B84 only at its actual quotient level leaves exactly crossing rows(5,45),(15,95); both-large rational quotients would force equal b and equal characters. These are necessary rows, not realizations.',
  'The upper residual entry u and lower divided entry v are genuine homomorphisms on the original p-group. They have opposite distinct tame weights. Nontrivial quotient residual action forces v nonzero on ker(u), hence a lower matrix in W1. Tame projection and conjugation by both unipotents force sl2 in W1; actual fifth powers give W1 contained in W2.',
  'For two traceless layers the determinant on the first kernel factors through a tame- and unipotent-invariant linear functional on sl2; the two off-diagonal weights and one conjugation kill it. The determinant image then has order at most5. In the cyclic cyclotomic image modulo125 this forces mu25 inside L and hence K. Exact absolute index identifies K with its Cohen coefficient field adjoining mu25, and the last cyclotomic field has degree5 and lower break576 over L.',
  'The determinant kernel is exactly the original residual kernel, so its cyclotomic degree5 field is R. The actual low first-level coordinate bounds its break by600-6B, strictly less than576 for B>20. This excludes shape(3,3), leaving only(3,4),(4,4), of wild orders5^8,5^9 in the both-large branch.',
  'The checker reconstructs inverse Newton hulls and multiplicities using exact fractions, runs every stated prime/divisible case, independently enumerates normalized finite characters, and tests conjugation of all linear functionals. Its finite ranges supplement the uniform proof and are not existence evidence.'
 ],
 'dependencies_freshly_reread':['lem:B-RD60-break','lem:B-RD69-quotients','lem:B-RD82-Newton','prop:B-RD84-tame','lem:B-RD86-cyclotomic'],
 'source_scope':'No new external primary-source opening is claimed. Original-source audits supporting the retained internal results remain referenced with their original scopes.',
 'program_sha256':sha(source),'author_output_sha256':sha(author),'author_bytes_unchanged':True,
 'independent_program':str(copy.relative_to(w)),'independent_output':str(independent.relative_to(w)),
 'independent_output_sha256':sha(independent),'independent_runtime_seconds':b['runtime_seconds'],
 'author_runtime_seconds':a['runtime_seconds'],'subprocess_wall_seconds':wall,
 'all_mathematical_output_identical':True,
 'counts':{k:b[k] for k in ['inverse_newton_quotient_rows','strict_prime_divisible_rows','normalized_distinct_character_rows','invariant_functionals_tested','cyclotomic_break_bound_rows']},
 'executed_failures':[],
 'scope_guard':'Only the residual-wild necessary patterns and both-large layer shapes shrink. The crossing rows are not examples; both surviving large shapes and the irreducible residual sector remain unresolved. No least-index closure is claimed.'}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'independent re-proof / computation or formal certificate','PASS: entire written proof/code and precise internal dependencies rederived; unchanged isolated rerun matches all mathematical output. See outputs/root_B91_audit.json.'])
 for label in r['dependencies_freshly_reread']:
  wr.writerow([label,now,r['reviewer'],'used and rechecked in this run','PASS: complete canonical proof passage freshly read and its exact role in B91 rederived; no fresh external-source claim.'])
with (w/'notes/checkpoint33_changes.md').open('a') as f:
 f.write('\n## Root audit of the residual-wild high quotients\n\nThe complete five-label B91 proof, exact checker and five internal proof dependencies passed at '+now+'. The unchanged isolated program ran in '+str(b['runtime_seconds'])+' seconds, matching all mathematical output and preserving author bytes. Different-character residual-wild comparisons require both original parameters divisible by p. At p5,e20 the crossings are restricted to(5,45) and(15,95); in the both-large branch only layers(3,4) and(4,4), of wild orders5^8 and5^9, remain. The unrestricted least-index interval remains{2,3}.\n')
print(json.dumps({k:r[k] for k in ['status','actual_utc','independent_runtime_seconds','all_mathematical_output_identical','counts']},indent=2))
