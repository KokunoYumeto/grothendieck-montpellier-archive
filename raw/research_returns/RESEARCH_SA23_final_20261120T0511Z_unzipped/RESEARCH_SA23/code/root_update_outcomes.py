"""Record the exact current scope of the final item audit.

This is a documentary update, not a new mathematical certification.
The proofs and independently authored check events remain the authorities
for the current outcome descriptions.
"""
from pathlib import Path
import csv, datetime, json

root = Path(__file__).resolve().parents[1]
path = root / 'notes' / 'outcome_table.tsv'
with path.open() as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)

updates = {
    'F': {
        'statement_ids': 'geo-F-fixed;geo-F-augmentation;geo-F-categorical;geo-F-finite;geo-F-infinite;geo-F-descent',
        'outcome': 'Fixed-order classification uses augmented jet-group actions and effective descent. A finite counterexample refutes the unaugmented replacement. Formal locality, finite presentation and quasi-compactness give finite order; neither arbitrary targets nor unrestricted infinite-order values satisfy that conclusion.'},
    'K(g)': {
        'outcome': 'The whole finite locally free case is the explicit faithfully flat Hopf-comodule algebra groupoid, including noncommutative and nonétale groups. Constant finite groups reduce to continuous fundamental-group homomorphisms modulo conjugacy; alpha_p gives R/R^p. Nonflat groups retain the complete cover-and-cocycle description.'},
    'K(h)': {
        'outcome': 'Field splitting is proved over every field. Over an arbitrary base the entire groupoid is given by projective chart modules and Laurent gluing maps, explicitly by idempotent and rectangular matrices with their equations and morphisms. Splitting types can jump in a one-parameter family.'},
    'Lead6, pre-Lidskii chronology and printing': {
        'state': 'In progress: dated textual occurrence checked; original printing and manuscript dating under investigation',
        'outcome': 'Bourbaki 91, §4(c), p.383 states the genus-zero product, and p.384 dates the text June 1957. The inspected fourth printing of the 1955 memoir states the Hilbert conclusion. Full-text checks of the 1955–56 publications are being completed; no date for the crossed-out manuscript sheets is inferred from the dossier’s dated letter.'}
}
for row in rows:
    row.update(updates.get(row['item'], {}))

additions = [
    {
        'item': 'D, literal 0-IV 19.5.5',
        'state': 'Proved',
        'statement_ids': 'SA23-D-17',
        'outcome': 'The finite-conormal infinitesimal testing criterion in chapter zero is independently proved. Polynomial truncation tests recover the completed algebra and lift every square-zero test map; it is distinct from the correction to IV 19.5.5.'
    },
    {
        'item': 'D, literal 0-IV 19.5.6(ii)',
        'state': 'Numbering conflation refuted; both actual texts checked',
        'statement_ids': 'SA23-D-6;SA23-D-17',
        'outcome': 'Chapter-zero 19.5.6 is a proof heading with decimal subparagraphs and has no standalone assertion (ii). The letter’s nonhomogeneous-generator claim is actual IV 19.5.6(ii), refuted and repaired separately.'
    }
]
existing = {row['item'] for row in rows}
index = next(i for i,row in enumerate(rows) if row['item']=='D, IV19.5.5')
rows[index:index] = [row for row in additions if row['item'] not in existing]
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)
record = {'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'rows':len(rows), 'updated_items':list(updates),
          'added_items':[row['item'] for row in additions if row['item'] not in existing]}
ledger = root / 'PROGRESS_LEDGER.md'
marker = '### Final scope audit: atomic documentary gates'
if marker not in ledger.read_text():
    entry = f'''

{marker}

Recorded {record['utc']}. This is a working-state update, not the first
formal three-hour movement review and not an additional checkpoint.

| Open row | Exact state | Approaches tried and next discriminating check |
|---|---|---|
| Lead 6: date of the crossed-out cote 1 sheets | Unsettled. The archive catalogue dates a letter to 1953 while explicitly leaving the mathematical notes undated. | Catalogue and supplied transcriptions checked. We are retrieving the entire original dossier and will inspect the correspondence and relevant folios for an explicit link. Dossier order alone will not be treated as a date. |
| Lead 6: whether the 1955–56 publications print the complete Hilbert trace argument | Full-text verification in progress. The inspected memoir states the genus-zero result; its later two-thirds proof uses that assertion. | Whole memoir OCR, all relevant theorem references, the 1956 erratum, and the full Fredholm paper are being compared. The additional metric résumé is a distinct publication still to inspect. |
| Lead 6: first-printing identity | Unsettled as a documentary qualification. Our memoir scan is the fourth printing (1966), with 1955 copyright. | Original-printing and publisher-record retrieval is under way. A reprint advertisement alone will not certify line-for-line identity. |

The original Bourbaki text with a June 1957 author date has been opened,
including its Hilbert product formula and coefficient identities. This
establishes that precise textual witness without assigning its date to
other sheets or to an uninspected physical edition. The main question A.1,
the exact characteristic-p criterion A.2, the general square-zero lifting
theorem A.3, and both openness refutations A.4 have passed independent
audits. The new finite pointed-jet counterexample and full relative
Hopf/idempotent classification descriptions have also passed root's audit.
The separate final coverage audit is still in progress.
'''
    with ledger.open('a') as f:
        f.write(entry)
(root/'logs'/'root_update_outcomes.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record, indent=2))
