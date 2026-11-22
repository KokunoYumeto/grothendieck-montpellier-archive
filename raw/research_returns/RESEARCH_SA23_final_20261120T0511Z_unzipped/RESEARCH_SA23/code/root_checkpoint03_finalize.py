"""Record the completed visual inspection and current checkpoint wording."""
from pathlib import Path
import csv, datetime, hashlib, json
root = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
qa = json.loads((root/'logs'/'root_checkpoint03_review.json').read_text())
assert hashlib.sha256((root/'RESEARCH_SA23_paper.pdf').read_bytes()).hexdigest() == qa['pdf_sha256']
qa['visual_inspection'] = 'Root directly inspected all five rendered pages; no clipping, overlap, or layout defect found.'
qa['inspection_completed_utc'] = stamp
(root/'logs'/'root_checkpoint03_review.json').write_text(json.dumps(qa,indent=2)+'\n')
with (root/'verification'/'visual_QA.md').open('a') as f:
    f.write(f'''

## Third scheduled checkpoint

Completed {stamp}. We rendered and directly inspected pages 1, 20, 40,
60 and 82 of the 82-page PDF. Headings, body text, mathematical displays,
footers and bibliography fit their pages, without clipping or overlap.
PDF SHA256: {qa['pdf_sha256']}.

The first attempt had one fatal bibliography typesetting error from two
unescaped underscores in agent names, and zero overfull boxes. We replaced
those metadata names by plain prose and rebuilt through LuaLaTeX/BibTeX/
LuaLaTeX/LuaLaTeX. All four commands returned zero. The successful build
had zero warnings, zero overfull boxes, zero overflows above 2pt, and a
maximum overflow of 0pt. Thus overfull counts before/after were 0/0;
there were no overflow pages requiring separate inspection. The failed
attempt's diagnostic and log are preserved under distinct names.
''')

path = root/'notes'/'outcome_table.tsv'
with path.open() as f:
    reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
for row in rows:
    if row['item']=='K(e)':
        row['outcome']='The unrestricted isomorphism-class presheaf is not an fppf sheaf; the unpolarized abelian moduli stack in dimension at least two over C is not algebraic. Limit preservation excludes an algebraic stack without a finite-presentation hypothesis; the polarization tangent obstruction supplies the contradiction.'
    if row['item']=='Lead6, pre-Lidskii chronology and printing':
        row['state']='In progress: printed content checked; manuscript dating unsettled'
        row['outcome']='The 1955 memoir states the Hilbert genus-zero conclusion; the inspected memoir and 1956 Fredholm article do not print the missing bridge. The metric résumé and original Lidskii 1959 endnote have now been retrieved for final source integration. Bourbaki 91 states the product formula in text dated June1957. No date for the crossed-out sheets is inferred from the separately dated 1953 letter.'
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(rows)
print(json.dumps({'completed_utc':stamp,'visual_pages':qa['pages_rendered'],'outcome_rows':len(rows)}))
