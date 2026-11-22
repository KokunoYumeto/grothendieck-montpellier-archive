"""Record the sixth scheduled checkpoint state, without an hourly review."""
from pathlib import Path
import csv, datetime, json, time
root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
target=root/'logs/root_checkpoint06_prepare.json'
if target.exists():
    raise SystemExit('Checkpoint06 preparation already recorded.')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
qa=json.loads((root/'logs/root_checkpoint06_visual_complete.json').read_text())
audit=json.loads((root/'logs/registry_audit.json').read_text())
reviews=json.loads((root/'logs/formal_reviews.json').read_text())
assert len(reviews)==2 and reviews[-1]['consecutive_reviews_without_movement']==1
assert not reviews[-1]['stopping_rule_fired']
with (root/'notes/manuscript_date_attempts.tsv').open() as handle:
    routes=list(csv.DictReader(handle,delimiter='\t'))
with (root/'PROGRESS_LEDGER.md').open('a') as handle:
    handle.write(f'''

### Sixth scheduled checkpoint, due 04:40 UTC

Preparation recorded {stamp}. This entry is **not** an hourly movement
review. The next formal review remains due at 05:10 UTC. The current
consecutive count without movement is one, from the 04:10 review.

The checked paper has {qa['pdf_pages']} pages and {audit['statement_rows']}
numbered statements, with {qa['bibliography_entries']} explicitly flagged
bibliography entries. All four build commands returned zero, warnings
and overfull boxes are zero, and seventeen rendered pages were individually
displayed and inspected. The registry contains {audit['events']} actual
check events and {audit['corrections']} corrections. The report's complete
manuscript-date table records {len(routes)} documented source routes.

A useful earlier printed witness was found in the 1951 Comptes rendus
note, p. 1557: it explicitly announces the Hilbert genus-zero assertion
while promising a detailed exposition elsewhere. Its three original
pages were read and the decisive page independently checked. This advances
the documented announcement chronology, but supplies neither that proof
nor a date or identification for the particular Montpellier sheets.

The additional original Bourbaki congress minutes date circulation of
report 230. The complete public Montpellier catalogue, the loan list,
the five unassigned pages, Cartier's exposition and the selected early
notices were checked within their precise recorded scopes. None supplies
a dated identification of the target trace/genus-zero leaves. Public
retrieval failures and later-edition limits remain explicit. The source-use
audit found no settled mathematical statement supported solely by an
unopened operative theorem.

The sole open row is unchanged: whether physical PDF pages 79–80 and
111–112 of cote 1 were written before 1959. All main Part A gates remain
closed under the exact hypotheses already recorded. No source-count,
announcement-chronology, typesetting, archive or restoration-utility change
is counted as formal movement. We continue the dating inquiry until the
next required review or an earlier actual resolution.

Archive creation and durable-save times are recorded separately. The final
package is planned to preserve all prior checkpoint contents through a
hash-verified manifest and a supplied restoration utility, without nesting
checkpoint ZIP files.
''')
record={'created_utc':stamp,'formal_review':False,'checkpoint_due_utc':'2026-11-20T04:40:00+00:00',
        'next_formal_review_utc':'2026-11-20T05:10:00+00:00',
        'manuscript_date_routes':len(routes),'statement_rows':audit['statement_rows'],
        'check_events':audit['events'],'corrections':audit['corrections'],
        'pdf_pages':qa['pdf_pages'],'pdf_sha256':qa['pdf_sha256'],
        'gate_changed':False,'elapsed_seconds':time.perf_counter()-started}
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
