"""Record the fourth timed review from the actual canonical question register."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,re,shutil,hashlib
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
with (root/'QUESTIONS.tsv').open(newline='') as f:
 rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
with (root/'evidence/review_03_questions.tsv').open(newline='') as f:
 old={r['id']:r for r in csv.DictReader(f,delimiter='\t')}
extra={'Q-MA-SOURCE-BRIDGE','Q-MA-LA-GLOBAL','MA-Q1-RF002','MA-Q2','MA-Q1-HM001','MA-Q1-HM002','MA-Q3c','MA-Q1-PR009','MA-Q1-PR010','MA-Q-MEY-narrow','MA-Q1-PR007','MA-Q1-PR003','Q-MA-LD-FINITE','MA-Q2-FQ006B','MA-Q2-FQ-primes','Q-MA-CAUSAL-001'}
qualified=[r for r in rows if r['id'] in extra or re.search(r'open|unproved|unresolved|conditional|partially|not established|gate|regime|unmodified',r['state'],re.I)]
assert not (root/'evidence/review_04_questions.tsv').exists()
shutil.copyfile(root/'QUESTIONS.tsv',root/'evidence/review_04_questions.tsv')
changes=[]
for r in rows:
 prior=old.get(r['id'],{})
 for k in ['state','finding_ids','current_gate','next_step']:
  if prior.get(k,'')!=r[k]:changes.append({'id':r['id'],'field':k,'previous':prior.get(k,''),'current':r[k]})
with (root/'evidence/review_04_changes.tsv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=['id','field','previous','current'],delimiter='\t',lineterminator='\n');wr.writeheader();wr.writerows(changes)
reviews=json.loads((root/'evidence/movement_reviews.json').read_text())
assert len(reviews)==3
reviews.append({'number':4,'timestamp_utc':now,'movement':True,'consecutive_stalled_reviews':0,'question_rows':len(rows),'open_or_qualified_rows_reviewed':len(qualified),'changed_or_new_rows_since_previous_review':len({x['id'] for x in changes}),'next_review_utc':'2026-11-21T22:31:00+00:00','decision':'Continue; previously unresolved original common-sum domain routes are decided by actual source counterexamples and a complete restricted-domain construction. The FT002 and S5 arithmetic gates are unchanged.'})
(root/'evidence/movement_reviews.json').write_text(json.dumps(reviews,indent=2)+'\n')
body=f'''\n\n## Timed movement review04 — {now}

Decision: **continue**. Genuine movement: **yes**. Consecutive reviews without movement: **0**. Next review: **2026-11-21 22:31 UTC /23:31 Berlin**. The complete {len(rows)}-row snapshot is evidence/review_04_questions.tsv; all register changes from review03 are in evidence/review_04_changes.tsv. The comparison file records changes, not automatic claims of mathematical progress.

Movement is the resolution of the pre-existing original-domain questions MA-Q-MEY-narrow and MA-Q1-PR007 at their specified raw and restricted-source scopes. At review03 the original uncontinued common-space identification and possible cancellation on the smaller sum remained undecided. MO004–008 now identify the actual polar difference, provide genuine source counterexamples, and refute whole smaller-sum invariance and its once-imposed pole-free iteration repair. MO010–011 construct the actual restricted smoothed map and determine its exact codimension-two closure; MO013 excludes any nonzero translation-equivariant target map into that particular closure. These are decisions about the original maps and domains, not only their multiplier continuations. MO009 also supplies the formerly missing primary Hecke-universality extension, while MO012 gives an actual nontrivial-character ideal endomorphism in its two explicit regimes.

The independent full narrow identity still has exactly the FT002 arithmetic deficiency condition. No stronger arithmetic zero-location theorem is counted. RB010 is an equivalent residual-realization gate; the inspected nonregular Galois and quadratic-Hecke applications supply no smaller S5 gate. They do not count as movement. Neither do editorial reconciliation, PDF checks or packaging. The finite-codimension correction changes the rational source action, and the nontrivial-character trace retains its ideal projector.

### Every currently open or qualified route

The following table includes completed conditional implications where an antecedent, exceptional-width scope, distinct domain identification or arithmetic evaluation remains unproved. It was read against the current register; no conditional theorem is treated as an established antecedent.

| Row | Current state | Exact gate or next step |
|---|---|---|
'''
for r in qualified:
 esc=lambda s:s.replace('|','/').replace('\n',' ')
 body+='| '+esc(r['id'])+' | '+esc(r['state'])+' | '+esc((r['current_gate']+' '+r['next_step']).strip())+' |\n'
body+='''
### Main-question gates at this review

1. **Masullo/Q and Dirichlet:** the full requested finite Gram transport, all-weight/full-test slow-band formula and arbitrary thin source-profile comparison are proved. The literal rate-independent source statement and the specified raw direct-product and rational smaller-sum routes are refuted. The restricted rational pole-free completion admits the stated S1 smoothing but no nonzero translation-invariant subspace, so it cannot supply the proposed equivariant repair. Independent equality with unchanged full local geometry still means empty upper deficiency; all widths mean own-sector RH. A supplies rational/Dirichlet zero location explicitly.
2. **Non-induced imaginary-quadratic character:** the actual full-test trace formula is proved; MO009 extends the genuine raw first-diagonal obstruction without A/M. MO012 supplies an actual ideal endomorphism, unconditionally at generic widths for Gevrey tests and under a fixed zero gap for arbitrary smooth tests. Its trace retains the actual ideal projector. The own-character RH/FT002 deficiency condition remains for the full identity.
3. **S5:** beta=b+n is proved under R_B. Without R_B, the exact remaining comparison gate is exclusion of the shared real zero in the RB008 discriminant-aware interval, with normal-closure multiplicity at least9k. RB009 and RB010 establish limits of two proposed routes, not a new exclusion or an excess field. The inspected real-zero and nonregular Galois theorems do not meet the missing hypotheses.
4. **PF26:** full invoked algebraic proof reading, exact own analytic premise, complete bad-prime reduction and the explicit Kummer-Hecke family remain complete at their documented scope. The companion analytic theorem is a named outside input, not a freshly audited proof.
5. **Input column:** all563 supplied finding rows remain classified with secondary premises and exact coverage. Unavailable original CX sources remain an explicit provenance limit.

No final package is triggered. Active next routes concern the retained ideal projection and a rational completion carrying the polar modes. They are prospective until written and fully checked, and are not counted as completed findings here.
'''
with (root/'LEDGER.md').open('a') as f:f.write(body)
readme=(root/'README.md').read_text().replace('## Current research state — checkpoint08 preparation','## Current research state — checkpoint08')
readme=readme.replace('Work remains active. The fourth timed review and checkpoint08 are due21:31UTC /22:31Berlin.','Work remains active. The fourth timed review records genuine movement from decisions of the original common-sum domain questions, with zero stalled reviews. Checkpoint08 is scheduled for21:31UTC /22:31Berlin; the next checkpoint is22:16UTC /23:16Berlin and the next movement review is22:31UTC /23:31Berlin.')
(root/'README.md').write_text(readme)
h=hashlib.sha256((root/'MAS_ARTIN.pdf').read_bytes()).hexdigest()
state={'checkpoint':8,'prepared_utc':now,'scheduled_checkpoint_utc':'2026-11-21T21:31:00+00:00','status':'Active research. Original rational common-sum and pole-free equivariant routes decided; actual nontrivial-character ideal endomorphism proved in the stated regimes. Full trace arithmetic deficiency and S5 shared-zero exclusion remain open.','pdf_status':'341 pages; no TeX warnings/out-of-page text; all13 final contact sheets (49 affected pages) actually inspected','pdf_sha256':h,'next_checkpoint_due_utc':'2026-11-21T22:16:00+00:00','next_movement_review_due_utc':'2026-11-21T22:31:00+00:00','consecutive_stalled_reviews':0,'completed_since_checkpoint_07':['MA-MO-007 original narrow common-sum noninvariance','MA-MO-008 exact pole-free source and second-iteration exit','MA-MO-009 non-induced Hecke universality and genuine smooth-domain raw obstruction','MA-MO-010 actual inherited-norm pole-free smoothed S1 map','MA-MO-011 exact codimension-two closure and minimal rank-two correction','MA-MO-012 full-ideal division and actual character S1 endomorphism','MA-MO-013 convolution/translation obstruction and zero invariant subspace','MA-RB-010 exact odd residual-realization equivalence; no smaller gate'],'active_routes':['Explicit retained-projector trace computation','Equivariant rational completion retaining polar source modes','Independent arithmetic FT002 divisor and PR block-cost estimates','Additional arithmetic S5 shared-zero exclusion'],'pending_integration':['No unchecked new proof is included in the paper. New routes after this freeze remain prospective.']}
(root/'evidence/checkpoint_08_state.json').write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps({'review':4,'timestamp':now,'question_rows':len(rows),'qualified':len(qualified),'changed_rows':len({x['id'] for x in changes}),'movement':True,'stalled_reviews':0,'pdf_sha256':h}))
