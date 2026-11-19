"""F3.34: exact reconstruction of the specific Johnson R-detector check."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

ROOT=Path('/workspace/scratch/f6dbb6638732')
WHO='GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_triangle'
DATE='2026-11-19';LEDGER='work/audit_after12_CHECK_EVENTS.tsv'
events=[]
def sha(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def event(s,t,o,agent='period_triangle'):
    events.append(dict(statement_id=s,date=DATE,who=WHO.replace('agent period_triangle','agent '+agent),type=t,outcome=o))

event('F.3.34','independent re-proof',
 'Reconstructed the specific R-vanishing proof omitted from the sketch of MSS2026Prop4.1. Six literal left-nested sevenfold brackets of actual degree-one Johnson triples on five handles have weight x1. Six H-valued equivariant cap maps give an integer6x6 matrix of determinant-203784, and the displayed R formula gives zero on all six vectors. The earlier published stable bound that J7 has H-multiplicity at most6 makes their H-isotypic projections a basis of its weight-x1 space. Equivariance then kills the full H component and all other irreducible components. Actual boundary extension and R_G(i^tensor9 T)=iR_g(T) give all genera>=3 and every Q_l. Only six maps and actual Lie closure are needed; completeness of105 caps and whole-J7 degree-one generation are unnecessary.')
event('F.3.34','targeted proof check',
 'The retained older dimension input is MSS2015v2 proof of Th7.5(iv)pp29-30: h7 H-multiplicity10, j7 H-multiplicity3, ES ranks3 and2, and J7 intersection j7=0 from Prop3.5(ii)pp16-17 imply J7 H-multiplicity<=6. These source character and ES-rank calculations are imported explicitly, not claimed independently recomputed. Work first in any sufficiently large stable genus G>=5, then embed every smaller actual genus. No unverified minimal stable cutoff is assigned.')
event('F.3.34','independent re-proof',
 'Root read the complete work proof and fixed certificate, reread originalMSS2015pp28-30 and visually reopenedp30. Its exact sequence gives the required stable multiplicity six. Root checked the explicit H-isotypic projection argument, actual stable-genus map and separation of the published dimension input from the newly reconstructed R calculation. Root approved F3.34 and the F29/F32 source-dependency updates after checkpoint10.',agent='root')
event('F.3.34','independent re-proof',
 'Elliptic independently read the full work proof and every line of the frozen certificate, reopened the older source p30 and Prop3.5(ii)pp16-17, and checked all signs against the original R formula. It verified that the six nonzero cap vectors prove independence only after projecting to the H-isotypic component, then uses the multiplicity bound and Sp-orbits. Actual genus extension and strict-image scope passed. Rerun exit0, external3.423437879seconds, internal3.275287986seconds, start2026-11-19T11:25:09.425831+00:00. Audit:work/elliptic_audit_R_J7_reconstruction.md.',agent='elliptic_splitting')

run=next(r for r in csv.DictReader((ROOT/'output/RESEARCH_SA07/COMPUTATION_RECORD.tsv').open(),delimiter='\t') if r['script']=='check_R_J7_six_generators.py')
code='output/RESEARCH_SA07/code/'+run['script'];output='output/RESEARCH_SA07/'+run['output']
assert run['exit_code']=='0' and sha(code)==run['script_sha256'] and sha(output)==run['output_sha256']
event('F.3.34','computation or formal certificate',
 'The fixed self-contained program constructs all six complete noncommutative word derivations, verifies degree7 and weightx1 on every term and literal specialness, computes all630 last-slot cap coefficients, and verifies the exact minor determinant-203784 and six exact Rzero values. No stored matrix, search result or witness file is read. Arithmetic is arbitrary-precision Python integers and rational SymPy matrices. Registered production program46; exit0, wall'+run['runtime_seconds']+'seconds; source SHA256'+sha(code)+'; output SHA256'+sha(output)+'.')
for result in ('F.3.29','F.3.32','F.3.33'):
    event(result,'targeted proof check',
     'The specific universal R-vanishing step is now proved by F3.34 from six explicit actual Johnson brackets, an exact determinant and the older published multiplicity bound. The five-term formula remains attributed to MSS2026Prop4.1; the conclusion no longer imports the omitted specific generator calculation in its sketch. The older dimension result and the actual stabilization/strict-image maps remain explicit dependencies. All previously proved arithmetic conclusions are preserved.')

sources=[]
details={
 'AuditMoritaSakasaiSuzuki2015v2':
  'Original2015v2 source reopened: proof of Th7.5(iv)printedpp29-30 states the stable exact sequence with J7 H-multiplicity6; root visually reopenedp30. Its dimension argument uses h7 H-multiplicity10, j7 multiplicity3 and ES ranks3/2. Prop3.5(ii)pp16-17 gives actual Johnson image intersection j7=0 in degree7. These published inputs bound the H multiplicity by6. The new six-witness computation proves the specific Rzero formula using that bound; the source dimension/ES-rank computations are not claimed reimplemented.',
 'AuditMoritaSakasaiSuzuki2026v1':
  'Originalv1 printedpp9-11 explicitly defines R as a Johnson-image detector and lists its five contraction coefficients. The p11 proof is a one-paragraph sketch without the six concrete generator/detector matrix. F3.34 now reconstructs that missing specific finite calculation and its exact H-isotypic/stabilization argument. This source is used for the explicit five-term formula; its asserted Rvanishing is no longer a necessary imported theorem in the final proof. Originalv1 edition/date and previously recorded narrow arithmetic corrections remain unchanged.'}
for row in csv.DictReader((ROOT/'work/audit_after11_source_checks.csv').open()):
    if row['source_key'] not in details:continue
    row=dict(row);row.update(status='OPENED ORIGINAL; SPECIFIC R-CALCULATION RECONSTRUCTED WITH PUBLISHED DIMENSION INPUT',locator_and_access=details[row['source_key']],dependent_statement_ids='F.3.34; F.3.29; F.3.32; F.3.33',date=DATE,who=WHO)
    sources.append(row);event('SRC.'+row['source_key'],'used and rechecked in this run',row['locator_and_access'])

claims=list(csv.DictReader((ROOT/'work/audit_claims.csv').open()))
before=Counter(r['status'] for r in claims);ids={'I.B05.01','I.B05.02','II.MB15.02'}
history=ROOT/'work/audit_after12_superseded_scopes.json'
if not history.exists():history.write_text(json.dumps({r['assertion_id']:r['remaining_obligation_or_scope'] for r in claims if r['assertion_id'] in ids},indent=2)+'\n')
for row in claims:
    if row['assertion_id'] not in ids:continue
    scope=row['remaining_obligation_or_scope']
    scope=scope.replace('The separate general affine extension is recorded under F3.33 when integrated.','F3.33 now proves the general affine number-field classification and the corresponding common-kernel exclusion through its explicit covering maps.')
    scope=scope.replace('The general affine extension is separately assigned to F3.33.','F3.33 now proves the general affine number-field classification and the corresponding common-kernel exclusion through its explicit covering maps.')
    addition=' F3.34 independently reconstructs the specific all-genus R-vanishing step from six actual Johnson brackets, determinant-203784 and the older published multiplicity bound; the 2026 sketch supplies the formula attribution, while the older dimension input remains explicit.'
    if ' F3.34 independently' not in scope:scope+=addition
    row['remaining_obligation_or_scope']=scope
    for key in ('proof_or_locator','canonical_dependencies'):
        for statement in ('F.3.33','F.3.34'):
            if statement not in row[key]:row[key]+='; '+statement
    row['check_event_statement_id']=row['assertion_id'];row['check_event_type']='targeted proof check';row['check_event_ledger']=LEDGER
    event(row['assertion_id'],'targeted proof check','Historical assertion status '+row['status']+' retained; F3.33 general affine conclusion and F3.34 independent R reconstruction added to current proof dependencies. Original register reading and truncated-proof claims keep their original meanings.')
assert before==Counter(r['status'] for r in claims)
with (ROOT/'work/audit_claims.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(claims[0]));w.writeheader();w.writerows(claims)
p=ROOT/'work/audit_claims.md';md=p.read_text();escape=lambda x:str(x).replace('|','&#124;').replace('\n',' ')
for row in claims:
    if row['assertion_id'] not in ids:continue
    line='| '+' | '.join(escape(row[k]) for k in ('assertion_id','status','claim','proof_or_locator','remaining_obligation_or_scope'))+' |'
    md,count=re.subn(r'^\| '+re.escape(row['assertion_id'])+r' \|.*$',lambda _:line,md,flags=re.M);assert count==1
md=md.replace('Supplemental proofs F.3.1–F.3.32','Supplemental proofs F.3.1–F.3.34')
if '`audit_after12_CHECK_EVENTS.tsv`' not in md:md+='\nThe independent R-detector reconstruction and current source-dependency records are in `audit_after12_CHECK_EVENTS.tsv`.\n'
p.write_text(md)

for path,rows,delim in [(LEDGER,events,'\t'),('work/audit_after12_source_checks.csv',sources,',')]:
    with (ROOT/path).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter=delim);w.writeheader();w.writerows(rows)
record=dict(statement_id='F.3.34',code=code,output=output,code_sha256=sha(code),output_sha256=sha(output),actual_wall_seconds=run['runtime_seconds'],started_utc=run['started_utc'],exit_code=0,independent_elliptic_wall_seconds='3.423437879',agent_work_internal_seconds='2.430248686',inputs='Six fixed sevenfold Johnson brackets;105 H-valued contractions each; exact6x6 minor; five-term R formula.',retained_source_input='Older MSS2015 stable H-multiplicity<=6; actual stabilization maps.')
(ROOT/'work/audit_after12_computation_records.json').write_text(json.dumps([record],indent=2)+'\n')
validation=dict(assertion_count=len(claims),source_entry_count=len({r['note_id'] for r in claims}),status_counts=dict(before),addendum_event_count=len(events),source_record_count=len(sources),updated_claim_ids=sorted(ids),changed_statuses=[],canonical_new_result_ids=['F.3.34'],new_bibliography_keys=[],dependency_change='The specific R-vanishing assertion of the2026 sketch is replaced by the F3.34 reconstruction; older published multiplicity input remains explicit.',production_code_sha256=sha(code),production_runtime_seconds=run['runtime_seconds'])
(ROOT/'work/audit_after12_validation.json').write_text(json.dumps(validation,indent=2)+'\n')
print(json.dumps(validation,indent=2))
