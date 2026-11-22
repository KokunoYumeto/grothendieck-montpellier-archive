"""Record the first scheduled substantive review, only at or after its due time.

This records the review actually made by the research lead. It does not
infer movement from file changes, source downloads, or archive creation.
"""
from pathlib import Path
import csv, datetime, json, time

root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
now = datetime.datetime.now(datetime.timezone.utc)
due = datetime.datetime(2026, 11, 20, 3, 10, tzinfo=datetime.timezone.utc)
if now < due:
    raise SystemExit('The first formal review is not yet due; no review recorded.')
path = root / 'logs/formal_reviews.json'
reviews = json.loads(path.read_text()) if path.exists() else []
if reviews:
    raise SystemExit('A formal review already exists; refusing to duplicate or overwrite it.')
with (root / 'notes/outcome_table.tsv').open() as handle:
    outcomes = list(csv.DictReader(handle, delimiter='\t'))
audit = json.loads((root / 'logs/registry_audit.json').read_text())
assert audit['statement_rows'] == audit['numbered_labels'] == 120
assert not audit['missing_rows'] and not audit['labels_without_events']
record = {
    'review': 1,
    'scheduled_utc': due.isoformat(),
    'created_utc': now.isoformat(),
    'movement': True,
    'comparison': 'Initial substantive ledger and the unresolved rows recorded during the first three hours.',
    'reason': 'All mathematical rows changed from unproved or assigned to proved, known with derivation, or refuted with repairs; A.1-A.4 have closed gates after independent checks. The Lead 6 publication-content branch also changed from unchecked to settled, including a complete reconstruction from the 1956 printed foundations. The manuscript writing-date branch remains unsettled.',
    'consecutive_reviews_without_movement': 0,
    'open_rows': [{
        'id': 'Lead6-manuscript-date',
        'status': 'Unsettled',
        'exact_gate': 'Establish whether the particular cote 1 trace sheets (physical PDF 79-80) and genus-zero lemma sheets (111-112) were written before 1959.',
        'strongest_proved_reduction': 'The full 150-page public dossier has been inspected individually; the catalogue and original institutional inventory distinguish undated mathematical notes from a 1953 letter. Neither the dated letter nor a dated enclosure identification has been tied to the target leaves. The printed-publication comparison is separately closed.',
        'next_discriminating_step': 'An independently public dated letter, enclosure list, authorial identification or archival collation linking these particular leaves or their distinctive argument to a pre-1959 date. Current routes are the Weyl archive, additional French correspondence holdings, and Brazilian editorial or institutional records.',
    }],
    'main_gates': {
        'A.1': 'Closed: characteristic-zero power-series differentials are not projective for n>0; complete proof and independent audit.',
        'A.2': 'Closed: separability of K/k and finite absolute p-rank give the exact positive-dimensional characteristic-p criterion.',
        'A.3': 'Closed in the actual stated nonlocal noetherian adic scope: full square-zero Cohen lifting, uniqueness and automorphisms, with both explicit meanings of the missing condition P proved.',
        'A.4': 'Closed: both blanket openness assertions are refuted by fully specified noetherian counterexamples; finite-presentation repairs are stated.',
    },
    'outcome_rows': len(outcomes),
    'numbered_statements': audit['statement_rows'],
    'check_events': audit['events'],
    'corrections': audit['corrections'],
    'excluded_from_movement': ['Packaging', 'Typesetting and page-image QA', 'Catalogue searches that supplied no date witness', 'Restatement of the remaining date gate', 'First-printing and unopened-original qualifications'],
    'next_review_due_utc': '2026-11-20T04:10:00+00:00',
}
ledger = root / 'PROGRESS_LEDGER.md'
with ledger.open('a') as handle:
    handle.write(f'''

## 20 November 2026, 03:10 UTC — first formal movement review

Actual review recorded at {now.isoformat()}. We compare the present state
with the initial substantive ledger and the open rows carried through the
first three hours. **Movement: yes. Consecutive reviews without movement: 0.**
All mathematical task rows now have complete proofs, exact derivations from
opened known results, or full refutations with proved repairs, under the
hypotheses expressly stated in the paper. The registry reconciles
{audit['statement_rows']} numbered statements, {audit['events']} check events
and {audit['corrections']} corrections. The outcome table has {len(outcomes)}
rows covering the Parts and six Leads.

The historical publication-content branch changed status: we have inspected
the memoir, 1956 article, metric resume, original Lidskii article and the
relevant contemporary and later primary texts. Proposition 8.9 supplies a
complete reconstruction from the printed 1956 foundations. Proposition 8.10
separates sufficient printed assertions and ingredients from a deduction
actually displayed in the source. This closes that branch of Lead 6.

| Main question | Current gate and status |
|---|---|
| A.1 | Closed. The explicit nonzero infinitely divisible differential proves failure of discrete formal smoothness in every characteristic-zero coefficient extension and n>0. |
| A.2 | Closed. The exact criterion is separability of K/k and finite absolute p-rank of K; the relative criterion alone is false. |
| A.3 | Closed under the actual nonlocal noetherian adic hypotheses. The full lift, uniqueness and automorphisms are proved; both explicit interpretations of formal projectivity are covered. The absent historical definition is a source qualification. |
| A.4 | Closed. The unrestricted openness claims are false; explicit noetherian counterexamples and the finite-presentation repairs are provided. |

| Every remaining open row | Exact status and strongest reduction | Next discriminating step |
|---|---|---|
| Lead 6: writing date of the particular trace/genus-zero sheets | Unsettled. All 150 public pages have been displayed individually. The original inventory explicitly leaves the mathematical notes undated while identifying a separate 1953 letter. The archive pencil gap and the chapter-reference matches do not supply a date for physical pages 79–80 and 111–112. The publication-content branch is closed. | Find a public dated letter, enclosure description, authorial identification or archival collation linking those leaves or their distinctive argument to a date before 1959. The current independent routes are Weyl holdings, additional French correspondence, and Brazilian editorial or institutional records. |

There is no other open task row. Edition collation, missing historical
terminology and uninspected original editions remain explicitly disclosed
qualifications, not invented extra problems. The checked statements retain
their stated hypotheses. We have not counted packaging, clean typesetting,
new search endpoints or restatement as movement. The overall response is
still **INCOMPLETE** because the sheet-date question is unresolved.
The next formal review is due at 04:10 UTC. The stopping rule has not fired.

### Fourth scheduled checkpoint, due 03:10 UTC

The current paper has 87 pages and 120 numbered statements. Its successful
LuaLaTeX build has zero warnings, zero overfull boxes and maximum overflow
0pt. Eleven page images were actually inspected, including the new proof
and the separate remaining-gate pages. The source, statement register and
check-event table are reconciled before the archive is created. Archive
creation and upload times are retained separately in checkpoint history.
''')
reviews.append(record)
path.write_text(json.dumps(reviews, indent=2) + '\n')
record['elapsed_seconds'] = time.perf_counter() - started
(root / 'logs/root_formal_review01.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
