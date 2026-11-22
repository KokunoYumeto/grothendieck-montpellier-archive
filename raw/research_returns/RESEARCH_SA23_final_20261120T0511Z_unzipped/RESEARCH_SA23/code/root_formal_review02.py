"""Record the second hourly review after an explicit unchanged-gate assessment."""
from pathlib import Path
import argparse,csv,datetime,json,time

parser=argparse.ArgumentParser()
parser.add_argument('--confirm-unchanged',action='store_true',required=True)
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
now=datetime.datetime.now(datetime.timezone.utc)
due=datetime.datetime(2026,11,20,4,10,tzinfo=datetime.timezone.utc)
if now<due:
    raise SystemExit('The second formal review is not yet due; nothing recorded.')
path=root/'logs/formal_reviews.json'
reviews=json.loads(path.read_text())
if len(reviews)!=1 or reviews[0]['review']!=1:
    raise SystemExit('Expected exactly the first review; no duplicate or overwrite allowed.')
audit=json.loads((root/'logs/registry_audit.json').read_text())
assert audit['numbered_labels']==audit['statement_rows']==120
assert not audit['missing_rows'] and not audit['labels_without_events']
assert not audit.get('invalid_event_types',[])
with (root/'notes/outcome_table.tsv').open() as handle:
    outcomes=list(csv.DictReader(handle,delimiter='\t'))
with (root/'notes/manuscript_date_attempts.tsv').open() as handle:
    routes=list(csv.DictReader(handle,delimiter='\t'))
previous=reviews[0]
gate=dict(previous['open_rows'][0])
gate['next_discriminating_step']='An independently public dated letter, enclosure list, authorial identification or archival collation linking these particular leaves or their distinctive argument to a pre-1959 date. Current specific routes include Bourbaki congress records and the 1954 Villavicencio-Mendoza symposium publication; original thesis or evaluation materials remain qualified by their actual access limits.'
record={
 'review':2,'scheduled_utc':due.isoformat(),'created_utc':now.isoformat(),
 'movement':False,
 'comparison':'The exact open row and main gates recorded at the 03:10 UTC first formal review.',
 'reason':'No open task row changed status, and no main question was proved to reduce to a strictly smaller gate. Further original source readings, correspondence and institutional finding aids did not identify a writing date for the particular cote1 trace/genus-zero leaves. The mathematical rows and completed publication-content comparison remain settled under their stated hypotheses.',
 'consecutive_reviews_without_movement':1,
 'open_rows':[gate],'main_gates':previous['main_gates'],
 'outcome_rows':len(outcomes),'numbered_statements':audit['statement_rows'],
 'check_events':audit['events'],'corrections':audit['corrections'],
 'documentary_routes':len(routes),
 'excluded_from_movement':previous['excluded_from_movement']+[
  'Retrieval and content comparison of Bourbaki179,187,230 without a target-leaf date',
  'Original 1954 CR notes and seminar/reception checks without manuscript identification',
  'More precise physical thesis holdings and institutional series descriptions',
  'A complete attempts table and fifth checkpoint'],
 'next_review_due_utc':'2026-11-20T05:10:00+00:00','stopping_rule_fired':False,
}
with (root/'PROGRESS_LEDGER.md').open('a') as handle:
    handle.write(f'''

## 20 November 2026, 04:10 UTC — second formal movement review

Actual review recorded at {now.isoformat()}. We compare the exact open row
and strongest reductions with the 03:10 review. **Movement: no.
Consecutive reviews without movement: 1.** No open task row changed
status; no main gate became strictly smaller.

| Main question | Current gate and status |
|---|---|
| A.1 | Closed. Failure of discrete formal smoothness for every characteristic-zero coefficient extension and positive number of variables; the complete proof and independent audit remain valid. |
| A.2 | Closed. The exact criterion remains separability of K/k and finite absolute p-rank of K. |
| A.3 | Closed under the stated nonlocal noetherian adic hypotheses, including the lift, uniqueness, automorphisms and both explicit meanings of condition P. |
| A.4 | Closed. Fully specified noetherian counterexamples refute the blanket openness claims; the finite-presentation repairs remain proved. |

| Every remaining open row | Exact status and strongest reduction | Next discriminating step |
|---|---|---|
| Lead 6: writing date of the particular trace/genus-zero sheets | Unsettled. The gate is exactly the same as at 03:10: establish whether physical PDF pages 79–80 and 111–112 were written before 1959. The complete public dossier and inventory distinguish undated notes from a separate 1953 letter, but no dated identification has been tied to these leaves. The publication-content branch remains closed. | Read an independently public dated letter, enclosure record, authorial identification or archival collation that explicitly links these leaves or their distinctive proof to a pre-1959 date. Current routes include Bourbaki congress records and the 1954 Villavicencio–Mendoza publication. |

The registry currently has {audit['statement_rows']} numbered statements,
{audit['events']} check events and {audit['corrections']} corrections. The
outcome table retains {len(outcomes)} rows. The report records {len(routes)}
documentary routes with evidence, failure point and next step. These counts
are inventory facts and are not evidence of formal movement.

During this interval we obtained more precise thesis holdings and read
additional original seminar, Bourbaki, reception and 1954 publication
material. R230 explicitly distinguishes a proved Hermitian genus-zero
case from the general Hilbert result announced in the thesis. It does not
identify the Montpellier leaves. Source dates, negative content checks,
unopened-original qualifications, the attempts table, clean typesetting
and checkpoint creation do not reduce the remaining date gate.

There is no other open task row. The overall response remains
**INCOMPLETE**. The stopping rule has not fired: this is the first
consecutive review without movement. The next formal review is due at
05:10 UTC. If that review also finds no movement, we must stop and deliver
the final incomplete package under the user's rule.
''')
reviews.append(record)
path.write_text(json.dumps(reviews,indent=2)+'\n')
record['elapsed_seconds']=time.perf_counter()-start
(root/'logs/root_formal_review02.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
