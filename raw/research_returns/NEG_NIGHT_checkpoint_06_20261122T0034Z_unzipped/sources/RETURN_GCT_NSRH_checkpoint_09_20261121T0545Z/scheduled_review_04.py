"""Fourth scheduled progress review, immutable and gated at05:00UTC."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
r=Path(__file__).resolve().parent;now=datetime.now(timezone.utc)
if now<datetime(2026,11,21,5,0,tzinfo=timezone.utc):raise SystemExit('Review04 is not yet due.')
out=r/'PROGRESS_REVIEW_04.md'
if out.exists():raise SystemExit('Refusing overwrite of review04.')
state=json.loads((r/'REVIEW_STATE.json').read_text());assert state['last_review_number']==3
oldfile=r/'QUESTIONS_at_review_03.tsv';assert hashlib.sha256(oldfile.read_bytes()).hexdigest()==state['questions_sha256']
with oldfile.open(newline='') as f:old={x['id']:x for x in csv.DictReader(f,delimiter='\t')}
with (r/'QUESTIONS.tsv').open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
assert all(fid in (r/'GCT_NSRH.tex').read_text() for fid in ['f:boundedSoergelNoGo','f:purerankthreekernels','f:iteratedChebyshevGate','f:jointRawCoefficientNormalization'])
def cell(s):return s.replace('|','/').replace('\n',' ')
changes='\n'.join('| '+' | '.join(map(cell,[x['id'],old[x['id']]['current_gate'],x['current_gate']]))+' |' for x in rows if x['id'] in old and (x['state']!=old[x['id']]['state'] or x['current_gate']!=old[x['id']]['current_gate']))
table='\n'.join('| '+' | '.join(map(cell,[x['id'],x['state'],x['current_gate']]))+' |' for x in rows)
head=f'''# Scheduled progress review04

Actual review: {now.isoformat()}. Scheduled review:2026-11-21 05:00UTC /06:00CET.
Reviewer /root; GPT-6 Astra Pro; effort not exposed; run GCT_NSRH_20261121.

## Decision: movement; continue

Compared frozen review03 questions and ledger with all current question states and checked main-paper findings. Movement means only a previously open row closing or a pre-existing main question reducing to a strictly smaller gate. New side rows, extra checks, source precision and packaging alone are not movement.

The pre-existing Q2/Q3-GCT realization gate has strictly narrowed since review03:

1. F59 closes every bounded ordinary type-A Soergel lift with the actual ambient generator class and original degree-zero quadratic coefficient. It is no longer only a direct-sum-candidate test. For an arbitrary bounded scalar k-complex, the continued proof forces uniform generic two-graph cohomology, excludes every all-flat cohomology lift, excludes every scalar multiple of the singular invariant correspondence, and excludes the specified pure three-root coefficient law even without flatness. A remaining scalar repair must use genuinely coupled nonflat cohomology and a mixed comparison outside these conditions. These full proofs and final text have recorded checks.

2. F60 closes the bounded finite-state repair if full cohomology retains the actual finite algebra with its original scalar grading. The actual negative word also excludes the displayed ordinary-isomorphism lift of its rank-one annihilator. Thus checking merely a few lower-rank presentation relations cannot suffice. Triangle-only or nontrivial coefficient relations remain different premises.

3. F61 supplies coherent pure derived arithmetic lifts of the actual rank-three coefficient kernels, their actual relation maps and correctly transported bar, with exact full-Tate and half-step domains. This closes the previously missing pure coefficient-object construction in that specified setting, while preserving the multiradius total-cohomology and independent-estimate limits. F63 then excludes strict effective simple-by-simple compatibility with the actual tensor-factor iteration from k4 at fixed strand rank3. Its containing whole tensor has positive unmarked traces, so the summand/projector premise is retained.

4. F62 and F64 construct and test actual nonproper standard flag operations. The torus coefficient has a nonzero Chern extension, excluding the constant coefficient replacement. Canonical weight grading and perverse/ordinary splitting fail to preserve the unchanged convolution, and the exact unit/Tate-preserving open-to-IC extraction cannot preserve the original relation. This leaves a filtered or mixed operation retaining extension data, not just a scalar factorization.

5. F65 tests the designated raw canonical coefficients directly, without named-generator effectivity. Proper-pure geometric isotypic multiplicities are pure point complexes. Two actual VIII multiplication constants cannot both be such pure Euler traces under any common nonconstant rational-power assignment of the source parameter. The isolated coefficient's alternate pure normalization is real but fails the companion constant and the separately stated hard-Lefschetz test. The source's signed/factored normalized positivity is not contradicted. Its formal parameter convention is audited separately from its extra arithmetic interpretation.

These are changes to the already open main realization gate, not movement manufactured by new row identifiers. They do not prove the unspecified global nonstandard-RH statement, the designated canonical basis comparison, normalized positivity in all requested cases, or independent local/reciprocal estimates.

Consecutive reviews without movement: **0**. Next scheduled review: **06:00UTC /07:00CET**. Continue under the user's two-consecutive-no-movement rule. Checkpoint08 is also due05:00UTC; checkpoint packaging is not counted as movement.

## Changes to existing questions since review03

| ID | Previous gate | Current gate |
|---|---|---|
'''
out.write_text(head+changes+'\n\n## Every question and current gate\n\nAll open rows appear below; closed rows are included for context.\n\n| ID | State | Current gate or proved boundary |\n|---|---|---|\n'+table+'\n')
(r/'QUESTIONS_at_review_04.tsv').write_bytes((r/'QUESTIONS.tsv').read_bytes())
state={'last_review_number':4,'last_review_utc':now.isoformat(),'movement':True,'consecutive_no_movement':0,'next_review_utc':'2026-11-21T06:00:00+00:00','decision':'continue','record':out.name,'questions_sha256':hashlib.sha256((r/'QUESTIONS.tsv').read_bytes()).hexdigest()}
(r/'REVIEW_STATE.json').write_text(json.dumps(state,indent=2)+'\n')
with (r/'LEDGER.md').open('a') as f:f.write('\n## '+now.isoformat()+' — scheduled progress review04\n\nMovement yes; consecutive no-movement count0. Counted strict main-gate changes: all-bounded ordinary-Hecke closure and altered-scalar restrictions; bounded full-cohomology relation exclusion; actual pure rank-three relation kernels and iterated effective-summand boundary; relative nonproper extension/extraction tests; direct joint raw-canonical purity comparison. Global labels, normalized mixed operations and independent weight estimates remain. Exact frozen comparison is PROGRESS_REVIEW_04.md /QUESTIONS_at_review_04.tsv. Next review06:00UTC.\n\n| ID | State | Current gate |\n|---|---|---|\n'+table+'\n')
with (r/'RUN_METADATA.md').open('a') as f:f.write('\nReview04 completed '+now.isoformat()+'; movement yes, no-movement count0. Next review06:00UTC. Checkpoint08 due05:00UTC.\n')
with (r/'CHECK_EVENTS.tsv').open('a',newline='') as f:csv.writer(f,delimiter='\t').writerow(['REVIEW04-GATE-COMPARISON',now.isoformat(),'/root','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','used and rechecked in this run','Compared frozen review03 with current checked main gates. This is a research-gate review, not a new mathematical proof or certificate.','PROGRESS_REVIEW_04.md; QUESTIONS_at_review_03.tsv; QUESTIONS_at_review_04.tsv'])
print(json.dumps(state))
