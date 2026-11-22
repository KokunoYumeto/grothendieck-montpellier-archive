"""Full independent root proof/code/source-scope audit of the PH2 countermodel."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
p=w/'agents/monodromy/post_CP32_birational_Pfaffian_height_two_counterexample_candidate.tex'
source=w/'agents/monodromy/code/verify_birational_Pfaffian_height_two.py'
author=w/'agents/monodromy/outputs/birational_Pfaffian_height_two_checks.json'
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
expected='f2b37e75b60aba9f39cc6ef4e72388dfd2edbcc9e676ce7c5a8d83930ae19915'
assert sha(p)==expected
before_source=sha(source);before_output=sha(author)
folder=w/'code/audit_snapshots/PH2_root_independent';assert not folder.exists()
(folder/'code').mkdir(parents=True)
copy=folder/'code'/source.name;shutil.copy2(source,copy)
snapshot=w/'notes/root_PH2_audited_candidate.tex';out=w/'outputs/root_Pfaffian_height_two_audit.json'
assert not snapshot.exists() and not out.exists();shutil.copy2(p,snapshot)
start=time.perf_counter();run=subprocess.run([sys.executable,str(copy)],cwd=w,capture_output=True,text=True);wall=time.perf_counter()-start
(w/'outputs/root_PH2_independent.stdout.json').write_text(run.stdout)
(w/'outputs/root_PH2_independent.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=folder/'outputs/birational_Pfaffian_height_two_checks.json'
a=json.loads(author.read_text());b=json.loads(independent.read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathpart(a)==mathpart(b)
assert sha(source)==sha(copy)==before_source and sha(author)==before_output
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['prop:abstract-birational-Pfaffian-height-two','cor:abstract-Pfaffian-common-incidence','rem:abstract-Pfaffian-height-two-scope']
r={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(p.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'proof_read_scope':'Entire three-label candidate and entire dependency-free exact checker read. Uniform matching proof, exact gcd, inverse compositions, radical ideal and reciprocal common-rank pair independently rederived.',
 'proof_checks':[
  'The lower block has m-1 alternating pairs weighted x0 and one pair weighted x1. It is invertible on x0*x1!=0, giving generic rankN-1. Deleting i>0 forces the unique matching pairing0 with the abandoned partner ofi, giving precisely the three displayed raw Pfaffian formulas.',
  'The exact raw common factor is x0^(m-2), including m=2. After cancellation sigma2=x1^2 and either final coordinate x0*x_j are coprime, so the entire vector has gcd1. The two polynomial composition identities give birational inverse tau over every characteristic-two field, without a finite-field inference.',
  'The homogeneous radical ideal has exactly the two minimal primes(x0,x1) and(x1,x_(2m-1),x_(2m)). They are incomparable for everym>=2, and their projective codimensions are2 and3. No multiplicity or scheme-theoretic equality of the original ideal with its radical is asserted.',
  'The coordinate formula for beta is obtained from the coefficient of each lambda_k in the alternating B_lambda pairing. At s=e0+e2 it produces(t1,t1,t2+t0,t3,...), so M_s has rankN-1 and left kernel e0*+e1*. The same lambda makes every lower pair ofB equal1, so the common pair is literal and works overF2.',
  'The exact identity M_s^t lambda=B_lambda s and generic uniqueness of both kernels identify the left-kernel map with tau. Thus the counterexample satisfies the common maximal section/dual-rank hypotheses and separable birationality, while its reduced base has height2. It supplies no actual Cartier realization or failure of monodromy.',
  'The checker reconstructs Pfaffians by independent perfect-matching recursion, not by installing the stated formulas as its output. Sparse exponents and parity implement F2 polynomial arithmetic. Exact minimal support hitting sets give the monomial minimal primes. It reconstructs M fromB coefficients and checks the literal rank pair. All five sizes are supplements to the uniform proof, not extrapolation.'
 ],
 'source_scope':'Fresh root original-source reading: Kustin--Polini--Ulrich Data3.1, full Proposition4.1 proof, full Theorem9.1 final proof and Remark9.2; Polishchuk introduction/TheoremB statement, end of2.3, and full Lemma2.4.1 proof. Deeper KPU dependencies and a full Polishchuk TheoremB audit were not newly completed. Russo--Simis Example2.5 and its proof chain were already fully audited earlier. These are scope comparisons, not imported solutions. See notes/ROOT_SEARCH_LOG_33.md.',
 'program':str(source.relative_to(w)),'program_sha256':before_source,
 'author_output_sha256':before_output,'author_bytes_unchanged':True,
 'independent_program':str(copy.relative_to(w)),'independent_output':str(independent.relative_to(w)),
 'independent_output_sha256':sha(independent),'independent_runtime_seconds':b['runtime_seconds'],
 'author_runtime_seconds':a['runtime_seconds'],'subprocess_wall_seconds':wall,
 'all_mathematical_output_identical':True,'cases':[x['N'] for x in b['cases']],
 'executed_failures':[],
 'scope_guard':'Refutes only an abstract height-three implication. Actual Cartier theta equivariance, rank-four bundle origin and global Lang connectivity remain separate. No main-gate closure is inferred.'}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:wr.writerow([label,now,r['reviewer'],'independent re-proof / computation or formal certificate','PASS: uniform abstract counterexample and reciprocal common pair rederived; unchanged isolated checker matches every mathematical output. Original source-scope comparisons checked. See outputs/root_Pfaffian_height_two_audit.json.'])
with (w/'notes/checkpoint33_changes.md').open('a') as f:
 f.write('\n## Root audit of the height-two Pfaffian countermodel\n\nThe full proof/code/source-scope audit passed at '+now+'. The unchanged isolated checker took '+str(b['runtime_seconds'])+' seconds and matched all five exact cases and every mathematical output; author bytes were preserved. The uniform proof covers every oddN>=5, includingN9 after exact gcd cancellation. It refutes the abstract codimension inference only, and is not a Cartier or monodromy counterexample.\n')
print(json.dumps({k:r[k] for k in ('status','actual_utc','candidate_sha256','independent_runtime_seconds','all_mathematical_output_identical','cases')},indent=2))
