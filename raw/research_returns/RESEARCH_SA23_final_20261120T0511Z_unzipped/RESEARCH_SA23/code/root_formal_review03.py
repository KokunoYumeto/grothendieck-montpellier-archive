"""Record the third review only when due and explicitly assessed unchanged.

Preparing this program is not the review. Its time and prior-review guards
prevent a premature or duplicate stopping record. It must be run only
after root has checked the current task statuses and the strongest gates.
"""
from pathlib import Path
import argparse, csv, datetime, json, time

parser=argparse.ArgumentParser()
parser.add_argument('--confirm-unchanged',action='store_true',required=True)
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
now=datetime.datetime.now(datetime.timezone.utc)
due=datetime.datetime(2026,11,20,5,10,tzinfo=datetime.timezone.utc)
if now<due:
    raise SystemExit('The third formal review is not yet due; nothing recorded.')
path=root/'logs/formal_reviews.json'
reviews=json.loads(path.read_text())
if len(reviews)!=2 or reviews[-1]['review']!=2:
    raise SystemExit('Expected exactly two earlier reviews; refusing duplicate or overwrite.')
previous=reviews[-1]
assert previous['consecutive_reviews_without_movement']==1
assert not previous['stopping_rule_fired']
audit=json.loads((root/'logs/registry_audit.json').read_text())
assert audit['numbered_labels']==audit['statement_rows']==120
assert not audit['missing_rows'] and not audit['labels_without_events']
assert not audit.get('invalid_event_types',[])
with (root/'notes/outcome_table.tsv').open() as handle:
    outcomes=list(csv.DictReader(handle,delimiter='\t'))
with (root/'notes/manuscript_date_attempts.tsv').open() as handle:
    routes=list(csv.DictReader(handle,delimiter='\t'))
unsettled=[row for row in outcomes if 'unsettled' in row['state'].lower()]
assert len(unsettled)==1 and unsettled[0]['item'].startswith('Lead6')
gate=dict(previous['open_rows'][0])
gate['next_discriminating_step']='A publicly inspectable dated letter, enclosure list, authorial identification or archival collation explicitly linking the particular cote1 trace/genus-zero leaves or a distinctive matching proof to a pre-1959 date. Unopened originals and exact access limits remain listed in the complete attempts table; no further research is undertaken after this stopping review.'
record={
    'review':3,'scheduled_utc':due.isoformat(),'created_utc':now.isoformat(),
    'movement':False,
    'comparison':'The exact open row and strongest main gates at the 04:10 second formal review.',
    'reason':'No open task row changed status and no main question was proved to reduce to a strictly smaller gate. Additional original readings, public catalogue checks and independently bounded retrieval routes did not identify a writing date for the particular cote1 trace/genus-zero leaves. The publication-content comparison and the mathematical outcomes remain settled under their stated hypotheses.',
    'consecutive_reviews_without_movement':2,
    'open_rows':[gate],'main_gates':previous['main_gates'],
    'outcome_rows':len(outcomes),'numbered_statements':audit['statement_rows'],
    'check_events':audit['events'],'corrections':audit['corrections'],
    'documentary_routes':len(routes),
    'excluded_from_movement':previous['excluded_from_movement']+[
        'Dated Bourbaki report-ID circulation without identification of the target leaves',
        'Complete public Montpellier title audit and inspected loan/unassigned-page lists',
        'The earlier 1951 printed Hilbert-genus-zero announcement, without the distinctive proof or a date for its manuscript',
        'Additional original published notices and reception sources without a matching dated proof',
        'Independent public-copy searches retaining their actual access limits',
        'Sixth checkpoint, source-flag audit, report refinement and final packaging preparation'],
    'next_review_due_utc':None,'stopping_rule_fired':True,
    'research_stopped_utc':now.isoformat(),'overall_state':'INCOMPLETE',
}
with (root/'PROGRESS_LEDGER.md').open('a') as handle:
    handle.write(f'''

## 20 November 2026, 05:10 UTC — third formal movement review and stop

Actual review recorded at {now.isoformat()}. We compare the exact open
row and strongest reductions with the 04:10 review. **Movement: no.
Consecutive reviews without movement: 2. The user's stopping rule fires.**
We stop further research and prepare the final **INCOMPLETE** package.
This stopping requirement takes precedence over untried source approaches.

| Main question | Current gate and status |
|---|---|
| A.1 | Closed. Every characteristic-zero coefficient extension in positive power-series dimension fails discrete formal smoothness; ordinary differentials are not projective. |
| A.2 | Closed. The exact criterion is separability of K/k and finite absolute p-rank of K. |
| A.3 | Closed under the stated nonlocal noetherian adic hypotheses; lift, uniqueness, automorphisms and both explicitly defined meanings of condition P are proved. The absent historical definition is not guessed. |
| A.4 | Closed. Explicit noetherian counterexamples refute the unrestricted openness claims, and the stated finite-presentation repairs are proved. |

| Every remaining open row | Exact status and strongest reduction | Missing witness |
|---|---|---|
| Lead 6: date of the particular trace/genus-zero sheets | Unsettled. The unchanged gate is whether physical PDF pages 79–80 and 111–112 of cote 1 were written before 1959. The publication-content branch is closed. | A dated original, enclosure record, authorial identification or archival collation that specifically connects these leaves or their distinctive proof to a pre-1959 date. |

The current register contains {audit['statement_rows']} numbered statements,
{audit['events']} check events and {audit['corrections']} corrections. The
outcome table has {len(outcomes)} rows and the documentary attempts table
has {len(routes)} routes. These counts do not constitute movement.

The newly inspected 1951 notice explicitly announces Hilbert genus zero
and promises a detailed exposition elsewhere. This advances the documented
announcement chronology, but its missing proof and absent manuscript
identification leave the open sheet-date gate unchanged. The additional
Bourbaki minutes date circulation of report 230 but do not
identify the Montpellier proof. The complete public catalogue and the
loan/unassigned-page checks supply no dated duplicate. Further published
sources and independent public-copy attempts retain exact reading and
access limits. No general career period, catalogue heading, later edition,
publication date or neighbouring leaf has been substituted for the missing
identification. All mathematical statements keep their stated scope.

There is no other open task row. The remaining source approaches and
their failure points are preserved in the report and source notes. We
make no priority claim and do not label the overall request complete.
Subsequent activity is restricted to assembling, verifying and saving the
final deliverable, including all prior checkpoint contents without nesting
the checkpoint ZIP files.
''')
reviews.append(record)
path.write_text(json.dumps(reviews,indent=2)+'\n')
record['elapsed_seconds']=time.perf_counter()-started
(root/'logs/root_formal_review03.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
