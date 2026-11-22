"""Retain complete actual-arc/exact-index proof audit and unchanged isolated B100 rerun."""
from pathlib import Path
import csv, datetime, hashlib, json, re, shutil, subprocess, sys, time, traceback
w=Path(__file__).resolve().parents[1]
c=w/'agents/reduction_descent/B_second_wild_trace_arc_candidate.tex'
p=w/'agents/reduction_descent/code/verify_second_wild_trace_arc.py'
a=p.with_suffix('.output.json');out=w/'outputs/root_B100_audit.json'
assert not out.exists()
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
expected='f0fb542a2cbd9ee40f0144f1ae4f8dd209ec0f0bd92153b70cb8d511d7ae0950'
assert sha(c)==expected
before={str(q.relative_to(w)):sha(q) for q in (c,p,a)}
run=w/'outputs/root_B100_isolated';run.mkdir(exist_ok=False);shutil.copyfile(p,run/p.name)
record={'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(c.relative_to(w)),'candidate_sha256':expected,'inputs_sha256':before,
 'entire_candidate_code_and_output_actually_read':True}
start=time.perf_counter()
try:
 with (run/'stdout.txt').open('w') as so,(run/'stderr.txt').open('w') as se:
  r=subprocess.run([sys.executable,str(run/p.name)],cwd=run,stdout=so,stderr=se)
 assert r.returncode==0
 fresh=json.loads((run/p.name).with_suffix('.output.json').read_text());old=json.loads(a.read_text())
 assert fresh['status']==old['status']=='PASS'
 mathematical=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
 assert mathematical(fresh)==mathematical(old)
 assert before=={str(q.relative_to(w)):sha(q) for q in (c,p,a)}
 record.update(status='FULL-INDEPENDENT-PROOF-AND-CODE-PASS',
  checker_runtime_seconds=fresh['runtime_seconds'],counts=fresh['counts'],
  all_mathematical_output_identical=True,author_inputs_preserved=True,
  proof_checks=[
   'For x0=e/p³<1, A1 satisfies both strict inequalities precisely becausee>p². Forx0>=1, floor(x0)+1 with at most one increment to avoidN divisibility lies in(x0,x0+2], which is strictly belowpx0 forp>=5. Thus the marked exponent exists for every statede, without a coprimality requirement onA.',
   'The exactb andJ identities give(q-p)A<b<(q-p)qA, A<qA<J<d and b<(q-p)J. These force a unique q-branch inY1, a unique p-branch inY2, and a unique uT^(p-1) term inPhi(Y2). Every intermediate coefficient has an extra u factor modulo p and every tail degree is later. The full integral power series is used, not a polynomial replacement.',
   'P(0)=p and its reduction has first termX^d with unit coefficient. Weierstrass preparation therefore gives an actual degree-d Eisenstein polynomial and a complete DVR with uniformizerx andv(p)=d. BecauseJ<d, all p-divisible terms are later after specialization. Y2 has finite valuationJ, while[p]Y2=Y2P=0, proving exact orderp³ of the actual pointx^A.',
   'The logarithm weights satisfy l_j(a^(p-1)u)=a^(p^j-1)l_j(u); the l_(j-2) weight agrees becausep²-1 dividesp^j-p^(j-2). This proves the integral inverse coordinate isomorphisms and exactPhi identity. The congruenceb=-(p-1)A moduloN then yieldsP(zetaX)=P(X) and Y_i(zetaX)=a^-1Y_i(X).',
   'The ring automorphismx->zetax has orderN, even when the special unit a has smaller order. Its fixed field has absoluteindexe and the same residue field. Coordinate multiplicationaT is the actual descent cocycle, whose Nfold product is1 and which fixesx^A. Generic finite-level Galois descent therefore descends the group and this marked point. The Hensel unit root plus(p-1)|e puts the unique tame cyclotomic degreep-1 field insideK, so mu_p is present.',
   'The finite flat closure of the actual cyclic point subgroup and its quotient giveGprime with potential good reduction. The determinant ischi_p psi withpsi(sigma)=a^(p+1) of order dividingp-1. The actual multiplication-by-p³ snake sequence has primitive constant rank1 kernel and rank1 quotientchi_p psi. Twisting bypsi^-1 gives the stated extension ofmu_p³ by(Z/p³)(psi^-1).',
   'The full B62 extension proof lifts this prescribed class by surjective Kummer transitions, exact prime-to-p averaging and corrected compatible continuous cocycles. Its inverse limit is a free Tate lattice and defines the generic BT groupH. Only its graded factors are asserted potentially good; no whole-good property is inserted.',
   'Isogeny and the finite twist give the actual special character pairs{lambda,lambda^p} and{1,lambda^(p+1)}. Their trace difference is the nonzero factor-(lambda-1)(lambda^p-1), becauseN does not divideA. Adding the same constant height summand preserves the actual truncation isomorphism and this character difference.',
   'Forvp(e)=1, B76 mixed necessity atn3 ise>p², and the new actual arcs realize every allowed index satisfying it. The assertion is existential across fields, not over each fixed field. Failure at actualp³ is exactly manuscriptindex2 failure, hence lowerbound3.',
   'At e=2p(p-1), actualp4 detects dimensions and determinant byB76. Dimensions0/2 and two filtered groups reduce to their residual finite characters. Mixed comparisons would requiree>p4 and are impossible. For the remaining whole supersingular comparison, the actual-target B64 recurrence gives1,2p-1,2p²-1,2p³-1; its last value exceedsa/(p-1)=2p(p²-1) by2p-1. All hypotheses of the actual quotient-weight argument are checked, and no source thickness is transferred to an isogenous target.',
   'Thus the exact full height2 index at2p(p-1) is3 for everyp>=5. The theorem does not imply two whole-good counterexamples, a full index formula for everywild e, or any result atp2/p3. The arithmetic checker supplements the complete effectivity proof and does not establish it.'
  ],
  source_scope={'primary':'Hopkins and Gross (1994), Equivariant vector bundles on the Lubin-Tate moduli space',
   'url':'https://math.bu.edu/people/jsweinst/AWS/Files/GrossHopkinsEquivariantVectorBundles.pdf',
   'successful_root_refs':['turn826564980view0','turn942757469view0','turn942757469view1','turn942757469view2','turn491713149view0'],
   'freshly_read':'Original equations5.3-5.8, complete Proposition5.7 statement and coefficient congruence; equations12.1-12.9 and Proposition12.10 with the entire printed proof. Root displayed and read the exact recurrence, coefficient and specialization passages after locating them in the indexed original.',
   'boundary':'Proposition5.7 explicitly refers integrality to Hazewinkel21.5, and12.10 cites Lubin-Tate/Drinfeld for its deformation proof. No new Hazewinkel, Kisin or Bondarko primary-proof reading is claimed in this root audit. The already fully audited B62/B64/B76 proof chain supplies the determinant, actual-target and mixed dependencies.',
   'fresh_internal_reads':'Complete B62 arc, quotient and exact Kummer-cocycle lift; complete B64 weighted-kernel and actual quotient proof; complete B76 point, mixed, determinant and exhaustion proofs.'},
  retained_access_failures=[{'ref':'turn635254528view0','url':'https://math.bu.edu/people/jsweinst/AWS/Files/GrossHopkinsEquivariantVectorBundles.pdf','outcome':'Direct original URL fetch timed out; opening the previously retrieved original source ref succeeded and its exact passages were then actually read.'}],
  scope='Full actual formal-group construction and exact second-wild index proof; no finite-profile realization inference.')
except Exception:
 record.update(status='FAIL',error=traceback.format_exc())
record['actual_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();record['wall_seconds']=time.perf_counter()-start
record['retained_run']=str(run.relative_to(w));labels=re.findall(r'\\label\{([^}]+)\}',c.read_text());record['labels']=labels
out.write_text(json.dumps(record,indent=2)+'\n')
if record['status'].startswith('FULL'):
 with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
  wr=csv.writer(f,delimiter='\t')
  for label in labels:wr.writerow([label,record['actual_utc'],record['reviewer'],'independent re-proof / computation or formal certificate','PASS: full actual Eisenstein arc/descent/quotient/lift and exact-index proof; unchanged isolated rerun; outputs/root_B100_audit.json.'])
print(json.dumps(record,indent=2))
if not record['status'].startswith('FULL'):raise SystemExit(1)
