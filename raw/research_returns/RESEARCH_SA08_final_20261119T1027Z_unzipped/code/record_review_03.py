"""Record the third formal review only at or after its scheduled UTC time."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, csv, json

parser=argparse.ArgumentParser()
parser.add_argument('--no-movement',action='store_true',required=True)
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
due=datetime(2026,11,19,10,21,tzinfo=timezone.utc)
if now<due:
    raise SystemExit('The10:21 formal review is not due yet.')
dest=root/'logs/PROGRESS_REVIEW_03.json'
if dest.exists():
    raise SystemExit('Refusing to overwrite an existing formal review.')
previous=json.loads((root/'logs/PROGRESS_REVIEW_02.json').read_text())
if previous['consecutive_no_movement']!=1:
    raise SystemExit('Unexpected prior stop-rule state; reassess manually.')
rows=len(list(csv.DictReader((root/'RESEARCH_SA08_results.csv').open())))
events=len(list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(),delimiter='\t')))
record={
 'review_number':3,'scheduled_utc':due.isoformat(),
 'recorded_utc':now.isoformat(),'baseline_review':previous['recorded_utc'],
 'qualifying_movement':False,'consecutive_no_movement':2,
 'open_requested_rows':['C.3','L7'],
 'C3_gate':'Common sources and terminal localization over arbitrary rings with infinitely many noninvertible rational primes, starting with Z. C34 supplies a weaker sufficient local-completion construction but neither existence nor necessity of its full admissible local completions is proved.',
 'stop_required':True,'further_investigation':'Stopped under the user rule; remaining work is final documentation, verification and packaging.',
 'statement_rows':rows,'check_events':events,
}
entry=f'''\n\n## Third formal review, {now.strftime('%Y-%m-%d %H:%M:%S UTC')}\n\nThis is the scheduled10:21 hourly review, comparing the original open rows and main-question gates with the09:21 review. The scheduled checkpoint06 at09:51 was not a formal review.\n\n### Open rows and main-question state\n\n| Item | State at this review | Exact remaining assertion |\n|---|---|---|\n| C.3 | Still undecided for rings with infinitely many noninvertible rational primes | For arbitrary admissible A and B over such a ring, beginning with Z, prove admissible common-source existence and terminal localization, or give a full counterexample with a proved correction. C17's finite-prime theorem is unchanged. |\n| L7 | Documentary date still undetermined | Establish a documentary link dating the actual mathematical leaves144–212 to1982–83. Filing material and the inspected related texts do not establish that interval for these leaves. |\n| A.1, the principal question | Proved in the exact stated conventions and scopes | A001–A009 and A025 retain the universal product, coefficient actions, arbitrary PD triple, completion and literal rational-specialization answers. A fresh direct audit found no change needed. |\n| All other Part items and Leads | Statuses unchanged from the first formal review and current outcome table | Proved or refuted with the explicit qualifications and strongest proved corrections in the paper. The D006E coherent recovery argument also passed a fresh adversarial audit. |\n\n### Actual advances and the movement criterion\n\nC30 proves conditional infinite arithmetic descent from compatible repairs of the common partial model. C32 extends it to the homotopy-equalizer targets needed to kill localization loops, explicitly retaining their nonzero eventual degree-one vertical cohomology. C34 genuinely weakens those sufficient hypotheses: it needs only finite form-truncation identifications and compatible target maps; higher relations of the partial model may be discarded. An independent rational elementary source and a two-edge simplicial path provide the missing overlap. Their complete proofs have independent audits.\n\nHowever, every local completion E_p must still be a full admissible theory in all weights and simplices, and the retained depths must tend to infinity. No such completion family has been constructed, no new coefficient-ring case has been settled, and neither necessity nor equivalence of this sufficient completion condition to C3 is proved. Weakening an unconstructed sufficient hypothesis does not, by itself, establish a demonstrably strictly smaller original main-question gate. This assessment was independently checked by the runs working on automorphisms, shadows and topos arguments; no result count is substituted for the user's criterion.\n\nC31 and C35 give fully checked failures of particular target-extension constructions, including admissible targets and the explicitly stated stable rows. They are not counterexamples to global uniqueness. C33 proves the moving-prime module example, its disappearance in the localizing shadow quotient, and the finite-prime detection limit for a fixed ordinary operation group. It yields no invariant distinguishing admissible theories. Further source checks found exact relative theorems with different categories, arrow directions or coefficient/range hypotheses; none supplies the missing classical strict completion theorem. These results and failed routes remain documented, with finite certificates where applicable.\n\nNeither requested open row has changed status since09:21, and no demonstrably strictly smaller original C3 gate has been proved. This review therefore has **no qualifying movement**. The consecutive formal reviews without movement count is now **2**.\n\n### Binding stop and final state\n\nThe user's rule now requires stopping the investigation. Research stops at this review; only final documentation, PDF verification and packaging continue. The final package is marked INCOMPLETE and retains C.3 and L7 as undecided. The strongest sufficient construction presently proved is C34, and the next mathematical step, if work is resumed in a later session, is an actual local finite-form completion theorem or an invariant of admissible theories giving a counterexample. The ledger records {rows} numbered statement rows and {events} consolidated check events at this review; these counts document the work and do not count as movement.\n'''
with (root/'PROGRESS_LEDGER.md').open('a') as f:f.write(entry)
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
