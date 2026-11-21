"""Record a due formal movement review from the current question register."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv, json

root=Path(__file__).resolve().parents[1]
p=root/'RUN_STATE.json'
state=json.loads(p.read_text())
now=datetime.now(timezone.utc)
start=datetime.fromisoformat(state['start_utc'])
number=state.get('formal_reviews_completed',0)+1
due=start+timedelta(hours=number+2)
if now<due:
    raise SystemExit(f'Formal review not due until {due.isoformat()}')
if number!=1:
    raise SystemExit('Later reviews require a fresh substantive comparison; do not reuse review01.')
with (root/'QUESTIONS.tsv').open(newline='') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
open_rows=[r for r in rows if r['state'] in ('active','open','unchecked')]
text=f'''\n## Formal movement review01 — {now.isoformat()}\n\nThree-hour review, due {due.isoformat()}. This is the first formal review.\n\n**Movement: YES. Consecutive reviews without movement:0.** Compared with the opening question register, targets1,3 and the n3 actual-object alternative have acquired complete checked proofs; all class-number-one split sixfold numerical gates have closed; every fourfold determinant now has a stated bound via compensation. Since checkpoint03, Q2p changed from active to proved, Q2r/Q2s closed the branch-exponent and Fermat-product supplier questions, and Q2q strictly reduced to correspondence-degree accounting plus explicit nonsplit target-lattice comparison. Packaging and side obstructions are not counted as movement.\n\n### Every open row at this review\n\n| Row | State | Strongest proved reduction and remaining gate |\n|---|---|---|\n'''
for r in open_rows:
    text+=f"| {r['id']} | {r['state']} | {r['finding_ids_or_current_gate'].replace('|',' / ')} |\n"
text+='''\n### Main-question gates\n\n- **Target1, Gaussian principal fourfolds:** proved with D0=3656994324480 and an explicit quadratic division coefficient. The restricted polarization and published period-rank locator were checked.\n- **Target2, all class-number-one sixfolds and determinants:** every split datum is numerically bounded using the authorized Perry input; every Eisenstein determinant is bounded by the independent G34 compensation. Gaussian determinant class3 has two checked rank9 proofs and effective Fermat suppliers. Its numerical correspondence and lattice transfer remain active. Other nonsplit field/determinant classes still require a new source: the proved reflection reductions leave only the Gaussian E8 case, so remaining curve searches are reflection-free and nonmonomial of degree at least9. A split-eightfold CM construction is the other main route.\n- **Target3, split Eisenstein eightfolds:** complete independent G34 reconstruction, actual rank16, cycle supplier/Brauer transfer, and explicit fixed-polarization/order bound proved. No unrefereed Severn theorem is used.\n- **Target4, natural imprimitive sources:** signature criterion and absence of dominance proved; exact maximal n5 ranks15/14 attained. The exact image dimension of every Nielsen component remains Q4c; explicit four-branch components have rank1.\n- **Target5, one actual complex for n3 or n4:** n3 actual-object request proved, including ordinary negative Ext, full character and numerical coherent variant. The n4 route is still an approach to the unresolved sixfold determinants; the new local obstruction requires even D|G| in the stated ramified-at2 setup but does not settle that route.\n\nContinue the main Gaussian determinant3 degree calculation, then the unresolved sixfold sources and component-specific imprimitive rank problem. The next formal review remains anchored at2026-11-21T14:38:55+00:00. No stopping rule is triggered.\n'''
with (root/'LEDGER.md').open('a') as f:f.write(text)
state.update(last_review=now.isoformat(),formal_reviews_completed=1,
             consecutive_reviews_without_movement=0,
             next_review_utc=(start+timedelta(hours=4)).isoformat())
p.write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps({'review':1,'time_utc':now.isoformat(),'movement':True,
                  'open_rows':[r['id'] for r in open_rows]}))
