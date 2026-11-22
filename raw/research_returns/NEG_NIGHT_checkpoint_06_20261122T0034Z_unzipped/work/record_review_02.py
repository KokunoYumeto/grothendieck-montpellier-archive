"""Record the second scheduled comparison against its preserved formal baseline."""
import argparse, csv, datetime as dt, json
from pathlib import Path

p=argparse.ArgumentParser(); p.add_argument('--utc',required=True); args=p.parse_args()
now=dt.datetime.strptime(args.utc,'%Y-%m-%d %H:%M:%S UTC')
assert now>=dt.datetime(2026,11,22,0,4,37)
out=Path('work/reviews/review_02.json')
assert not out.exists(), 'A formal review is immutable.'
gates=json.loads(Path('work/main_gates.json').read_text())
by={r['id']:r for r in gates}
def ids(key,*new):
 r=by[key]; r['finding_ids']=';'.join(dict.fromkeys(r['finding_ids'].split(';')+list(new)))
for key in ['Q-MAIN01','Q-MAIN02','Q-MAIN06']:
 ids(key,'NN-C034')
 by[key]['approaches_tried']+=' The integral symbolic construction now permits explicitly listed factors of polylogarithmic scope, O(n) total ordinary degree and O(n) factor count, keeping the original n Boolean coordinates. Heavy incidence variables are branched on; no truth-table or verifier-variable expansion is used.'
ids('Q-MAIN12','NN-S019')
by['Q-MAIN12']['approaches_tried']+=' NN-S019 proves an exponential monotone arithmetic circuit lower bound for a fixed-degree-expander local counting polynomial, while NN-C034 constructs a subexponential integral circuit for it. Its existence support nevertheless has an O(n^3) monotone Boolean circuit, by the exact forbidden-tuple 2SAT duality; this distinguishes coefficient multiplicity from Boolean support without changing the CLIQUE endpoint.'
ids('Q-MAIN09','NN-A035','NN-A036')
by['Q-MAIN09']['state']='positive arithmetic robust-transversality proportion proved; signed high-zero half-balance and joint marked-phase gates remain open'
by['Q-MAIN09']['approaches_tried']+=' NN-A035 proves strict left second bending for every initially vertical branch at a multiple zeta zero, with primitive Dirichlet and high-height Dedekind variants. NN-A036 combines fixed-prime Landau averages, the Hardy-phase mean and the two-thirds simplicity theorem under A: at least4/87 of all positive-ordinate zero occurrences, and2/29 of simple zeros, have normal velocity magnitude at least1/30 of full velocity. This controls magnitude, not the left/right sign. Signed residue moments do not give sign counts without control of multiple-zero residues and velocity tails.'
by['Q-MAIN09']['next_step']='Seek odd marked-phase cancellation, or control multiple-zero residues and uniform integrability of velocity weights before converting signed residue moments into sign counts. Universal simple-zero transversality is not established.'
ids('Q-DIMOPT','NN-G032','NN-G033','NN-G034','NN-G035','NN-G036')
r=by['Q-DIMOPT']
r['state']='2744 incumbent; closed-table minimum in[2604,2744] with8 remaining first-cell mass triples; unrestricted symmetric minimum remains open'
r['current_gate']='NN-G033 gives2744 cancelling pairs,1296 in the bottom coefficient,total dimension mass9931. Every symmetric lift of no greater cost has an equal-cost representative of degree below2^9953, allowing all1000 table positions; NN-G032 decides numerical mass-budget feasibility in F(N)(L+1)^c time. Within the closed table, NN-G034 and G036 prove2744 is the unique mass-eight minimum; the smallest first-action mass64 also forces that realization. A strict improvement now requires one of17 base mass rows,26 auxiliary increments and8 first-cell mass triples with gluing mass10 or12. The necessary lower bound is2604, with no support-degree cutoff imposed and no claim that surviving rows are realizable. The unrestricted extra-position minimum and a practical optimization method remain open.'
r['approaches_tried']+=' Complete arbitrary-degree polynomial, content and mod-four arguments successively exclude mass-eight, equal/action-mass-ten and five mass-twelve competitors. The second exact projection, independently rerun after full proof readings, leaves17 rows/26 increments/8 first-cell triples and raises the closed-table lower bound to2604.'
r['next_step']='Analyze the remaining17 closed-table mass rows with unrestricted support indices, or a different symmetric table shape; no global optimum is claimed.'
Path('work/main_gates.json').write_text(json.dumps(gates,indent=2)+'\n')

review_path=Path('work/review_status.json'); status=json.loads(review_path.read_text())
status['NN-S019']['date_utc']='2026-11-21 23:43:22 UTC'
status['NN-S019']['scope_and_method']+=' Original whole-proof reviewer/date retained here; the root Boolean support addendum review is separately recorded at2026-11-21 23:59:12 UTC.'
status['NN-G036'].update(date_utc='2026-11-22 00:03:47 UTC',who='/root',outcome='PASS; complete deduction proof and later refinements read',scope_and_method=status['NN-G036']['scope_and_method']+' Fully read all147 lines of the four-row small-gluing addendum, checked its imported divisibility interfaces, and read/reran the second exact projection. Root-authored five mass-twelve exclusions were read in full by /root/gct at00:01:02 UTC; both reviewers and dates are separately retained.',evidence=status['NN-G036']['evidence']+'; work/gct/g036_small_gluing_final_draft.tex; work/root/w12_exclusions.tex; work/gct/verify_second_competitive_refinement.py')
review_path.write_text(json.dumps(status,indent=2)+'\n')
event_path=Path('work/root/CHECK_EVENTS.tsv')
with event_path.open() as f:
 reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; events=list(reader)
def event(sid,date,who,method,evidence):
 events.append(dict(statement_id=sid,date_utc=date,who=who,model='GPT-6 Astra Pro',effort='not exposed by runtime',type='targeted proof check',outcome='PASS; whole stated deduction proof read',scope_and_method=method,limitations='Targeted reading, not independent re-proof or formal verification.',evidence=evidence))
event('NN-S019','2026-11-21 23:43:22 UTC','/root/complexity','Retained original complete chapter11 review; reviewer checked shared-DAG multihomogeneity, balanced internal gates, compatible rectangles and expander constant. Internal-gate size convention corrected and rechecked at23:47:27. Later root addendum has its separate23:59:12 event.','work/root/chapter11.tex; recorded collaboration review')
event('NN-G036','2026-11-22 00:01:02 UTC','/root/gct','Read every line of root w12_exclusions.tex: mass12 classification, H(0), D-adic valuation, both84/88 orientations,84/84 and both80/96 degree-four orientations. No finite-degree assumption; reverse mod-four necessary condition verified.','work/root/w12_exclusions.tex')
event('NN-G036','2026-11-22 00:03:47 UTC','/root','Read the complete147-line small-gluing addendum: last mass-eight row, equal mass-ten actions100 and both84/100 orientations. Read and reran exact finite projection:17 rows,26 increments,8 triples,minimum2604.','work/gct/g036_small_gluing_final_draft.tex; work/gct/verify_second_competitive_refinement.py; work/gct/second_competitive_refinement_certificate.json')
with event_path.open('w') as f:
 writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n'); writer.writeheader(); writer.writerows(events)

baseline=json.loads(Path('work/gate_history/formal_review_01.json').read_text())['gates']
before={r['id']:r for r in baseline}
movement={
 'Q-MAIN06':'NN-C033 closes the fixed-F2 construction restriction; NN-C034 closes the integral-gate and all-ring base-change restriction with constant-free polynomial-formal-degree circuits. Polynomial proof size and arbitrary IPS verification remain open.',
 'Q-DIMOPT':'The incumbent improves3352 to2744; necessary arbitrary-degree closed-table gates shrink to17 mass rows/26 increments/8 triples and lower2604. Extra-position optimization remains open.'}
notes={
 'Q-MAIN03':'Fixed-F2 realization strengthens the deterministic finite-field construction, but the baseline already closed smooth specialization. Polynomial isolation and invariant extraction are unchanged; no extra movement counted.',
 'Q-MAIN08':'Integral motivic and lambda/gamma descriptions are proved, but the specified canonical GCT object and efficient extraction remain missing; no movement counted.',
 'Q-MAIN09':'The actual positive robust-transversality proportion is a substantive partial theorem. The baseline signed half-law and correlation gate is unchanged, so no main-row movement counted.',
 'Q-MAIN10':'New arithmetic central examples and bending results do not decide the actual zeta endpoint multiplicities or extreme-gap transfer; no movement counted.',
 'Q-MAIN11':'Exact endpoint detection and finite orbital formulas were already closed at review01. Canonical realization and remaining analytic gates are unchanged.'}
comparisons=[dict(id=r['id'],before=before[r['id']],after=r,counts_as_movement=r['id'] in movement,assessment=movement.get(r['id'],notes.get(r['id'],'No solved/refuted open row or strictly smaller current main gate is counted. Structural additions remain recorded without inflating movement.'))) for r in gates]
questions=[]
for track in ['root','complexity','gct','analytic']:
 with Path('work',track,'QUESTIONS.tsv').open() as f:
  for row in csv.DictReader(f,delimiter='\t'):
   questions.append(dict(id=row.get('question_id',row.get('id','')),source_and_locator=row.get('source_and_locator',row.get('source_locator',f'work/{track}/QUESTIONS.tsv')),question=row.get('question',''),state=row.get('state',row.get('status','')),finding_ids=row.get('finding_ids',row.get('finding_id','')),counterexample=row.get('counterexample',''),current_gate=row.get('current_gate',row.get('remaining_gate','')),approaches_tried=row.get('approaches_tried',''),next_step=row.get('next_step','')))
questions.extend(gates)
open_rows=[r for r in questions if r['id'].startswith('NN-QG') and r['id'] in {'NN-QG017','NN-QG018','NN-QG019','NN-QG020','NN-QG021'}]
prior=json.loads(Path('work/reviews/review_01.json').read_text())
review=dict(date_utc=args.utc,kind='formal movement review',number=2,due_utc='2026-11-22 00:04:37 UTC',previous_formal_review='work/reviews/review_01.json',comparison_baseline='work/gate_history/formal_review_01.json',baseline_policy='Compare the preserved prior formal state; interim snapshots never reset the baseline. Only main gates or genuinely open rows count.',main_rows=comparisons,open_track_rows=[dict(id=r['id'],state=r['state'],current_gate=r.get('current_gate',''),assessment='Reviewed against the prior formal question snapshot; no additional movement counted separately from the main gate changes.') for r in open_rows],question_snapshot=questions,reviewed_findings=len(status),movement_main_rows=list(movement),consecutive_no_movement_reviews=0,decision='CONTINUE',next_review_due_utc='2026-11-22 01:04:37 UTC',limitations='Whole deduction readings, exact finite computations and primary-source checks remain distinct. No general formal verification is claimed. M remains conditional.')
out.write_text(json.dumps(review,indent=2)+'\n')
Path('work/gate_history/formal_review_02.json').write_text(json.dumps(dict(date_utc=args.utc,kind='formal movement review baseline',gates=gates),indent=2)+'\n')
ledger=Path('deliverables/LEDGER.md')
text=ledger.read_text().replace('At the next scheduled review,2026-11-22 00:04:37 UTC, compare every open row and main gate against formal_review_01.json','At the next scheduled review,2026-11-22 01:04:37 UTC, compare every open row and main gate against formal_review_02.json')
text+='\n\n## Formal movement review02: '+args.utc+'\n\nCompared all14 main rows and the current track question registers against the preserved first formal review. Two main rows moved under the prompt criterion:\n\n- **Q-MAIN06:** fixed-small-characteristic and integral-gate restrictions are closed by NN-C033–034. One integral circuit and its ordinary ideal certificates survive every coefficient-ring base change. Polynomial proof size and arbitrary IPS verification remain open.\n- **Q-DIMOPT:** the incumbent falls from3352 to2744. Complete arbitrary-degree closed-table exclusions now leave17 base mass rows,26 auxiliary increments and8 first-cell mass triples, with necessary lower bound2604. The extra-position global minimum remains open.\n\nThe fixed-F2 projective construction, integral motivic/lambda/gamma descriptions, actual positive-proportion arithmetic transversality theorem and monotone arithmetic/Boolean support contrast are retained as proved advances, without counting them as closures of the unchanged main isolation, canonical-GCT, signed-half-law or CLIQUE gates. All125 registered findings have complete deduction-proof readings, including the newly added statements. Consecutive no-movement reviews: **0**. Continue; next formal review2026-11-22 01:04:37 UTC. Full before/after rows and the question snapshot are in `work/reviews/review_02.json`.\n'
ledger.write_text(text)
print(json.dumps(dict(date_utc=args.utc,main_rows=len(gates),question_rows=len(questions),open_track_rows=len(open_rows),reviewed_findings=len(status),movement_main_rows=list(movement),consecutive_no_movement_reviews=0,decision='CONTINUE')))
