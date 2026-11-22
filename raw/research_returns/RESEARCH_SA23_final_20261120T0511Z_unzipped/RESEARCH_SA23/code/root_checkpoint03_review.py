"""Prepare the third scheduled checkpoint's actual review and visual samples.

This records a targeted proof check just performed, and a documentary state
update. It does not manufacture completion or a formal movement review.
"""
from pathlib import Path
import csv, datetime, hashlib, json, time
import fitz

root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
events_path = root / 'notes' / 'root_CHECK_EVENTS.tsv'
with events_path.open() as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields = reader.fieldnames
    events = list(reader)
event = {
    'statement_id': 'cat:J1', 'date': stamp,
    'who': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root',
    'type': 'targeted proof check',
    'outcome': 'The unconditional factor-set formula, gauge action, fixed-subgroup centralizer, empty case, and continuity criterion were checked directly. Multiplication of beta(gamma)=c(gamma)s(gamma) gives exactly the printed equation; no pre-existing extension is assumed.',
    'where': 'sections/category_J.tex, cat:J1, unconditional formulation and proof'
}
if not any(e['statement_id']=='cat:J1' and e['outcome']==event['outcome'] for e in events):
    events.append(event)
    with events_path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
        writer.writeheader()
        writer.writerows(events)

ledger = root / 'PROGRESS_LEDGER.md'
marker = '## 20 November 2026, 03:25 CET — third scheduled checkpoint'
if marker not in ledger.read_text():
    with ledger.open('a') as f:
        f.write(f'''

{marker}

Snapshot preparation recorded at {stamp}. All 119 numbered statements have
matching registry rows and actual check events. The additional literal
chapter-zero erratum, augmented-jet counterexample, full Hopf and idempotent
classification groupoids, and unconditional section equations are incorporated.
K(e) now excludes algebraicity itself using limit preservation. The core
mathematical items remain settled with their explicitly stated scope.

| Open row | Exact state | Next discriminating step |
|---|---|---|
| Lead 6: date of the crossed-out cote 1 sheets | Still unsettled. The complete original dossier is retrieved and all contact sheets were inspected; no date has yet been tied to the relevant folios. | Inspect readable folios across all three portions of the dossier, locate the catalogue's 1953 letter, and test whether it actually dates the trace argument. |
| Lead 6: proof content of the 1955–56 publications | The whole accessible memoir and the 1956 Fredholm article have been audited independently. They state/use the Hilbert bridge but do not supply its proof. The metric résumé has been retrieved and its relevant operator material visually checked; its final integration is in progress. | Finish the résumé comparison and visually collate Lidskii's original 1959 endnote, whose public issue OCR has now been retrieved. |

First-printing collation is retained as an edition qualification, not an
extra requested theorem or a reason to refuse a verified reprint. We
identify publication dates and inspected physical editions separately.
This clarification does not count as movement under the user's rule.
The cautious original Lead that the manuscript may predate 1959 is not
replaced by an asserted priority claim. No date is inferred from dossier
order. This scheduled checkpoint is not a formal movement review; the
first such review remains due at 03:10 UTC.
''')

pdf = root / 'RESEARCH_SA23_paper.pdf'
doc = fitz.open(pdf)
pages = sorted(set([1,20,40,60,len(doc)]))
rendered = []
for number in pages:
    path = root / 'verification' / f'paper_checkpoint03_{number:02d}.png'
    doc[number-1].get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False).save(path)
    rendered.append(str(path.relative_to(root)))
record = {
    'created_utc': stamp, 'pdf_pages': len(doc), 'pages_rendered': pages,
    'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'rendered': rendered, 'visual_inspection': 'pending direct image inspection',
    'elapsed_seconds': time.perf_counter()-started,
}
(root/'logs'/'root_checkpoint03_review.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
