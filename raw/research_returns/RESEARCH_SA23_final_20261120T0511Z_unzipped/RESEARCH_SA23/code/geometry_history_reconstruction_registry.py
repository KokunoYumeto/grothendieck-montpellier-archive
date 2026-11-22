from pathlib import Path
import csv
import json

root = Path(__file__).resolve().parents[1]
registry = root / 'notes/geometry_results.csv'
with registry.open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
for row in rows:
    if row['id'] == 'geo-H-history':
        row['depends_on'] += ';geo-H-1956-reconstruction;catSimon1977'
        row['depends_on'] = ';'.join(dict.fromkeys(row['depends_on'].split(';')))
        row['notes'] = ('Bourbaki91 gives the formula in a June1957-dated text; original Lidskii1959 points to Memoir16(1955) while attributing genus zero to Weyl. Memoir II1no4 states genus zero and actual unordered l1 continuity without proving those Hilbert inputs there. The1956 printed determinant foundations suffice for the complete reconstruction in geo-H-1956-reconstruction; final minimal-type and global trace steps are not displayed in that source. Actual source/version and manuscript-date limits remain explicit; all physical25-72 individually inspected, without a readable date or identifiable1953letter.')
new = {'id':'geo-H-1956-reconstruction',
       'statement':'Full Hilbert trace formula reconstructed from the printed1956 determinant foundations',
       'status':'Proved', 'where_proved':'sections/geometry_H.tex',
       'depends_on':'Grothendieck1956Fredholm',
       'manuscript_pages':'1/079-080;1/111-112;Lead6',
       'notes':'Printed mixed-rank vanishing I1p327 and normalized mixed bound I2p328/II2pp346-348 yield minimal exponential type by a finite-rank tail; zero-free logarithm gives quasinilpotent trace0; full primary-space quotient proof gives all trace-class operators. Reconstruction is explicitly separated from printed proof content.'}
if not any(row['id'] == new['id'] for row in rows):
    rows.append(new)
with registry.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

events = [
 ['geo-H-1956-reconstruction','2026-11-20','GPT-6 Astra Pro, inherited effort, crystalline_categories','independent re-proof','Current-run reconstruction and primary comparison: checked exact mixed coefficient normalization, finite-rank vanishing, minimal type, zero-free determinant, invariant primary flags and quotient quasinilpotence. Full reasoning in notes/category_simon_fredholm_audit.md.'],
 ['geo-H-1956-reconstruction','2026-11-20','GPT-6 Astra Pro, inherited effort, geometry_analysis','targeted proof check','Independently audited the complete reconstruction and supplied Schwarz-lemma proof of the zero-free logarithm bound; visually read original1956 pp327,328,348 and Simon1977 pp254,257,258. Wrote the numbered proposition with exact printed-input locators.'],
 ['geo-H-1956-reconstruction','2026-11-20','GPT-6 Astra Pro, inherited effort, root','targeted proof check','Root independently audited category full reconstruction, including finite-rank tail, quasinilpotent trace0, quotient quasinilpotence and trace splitting; passed. Exact1956 mixed-rank source I1Prop1/cor p327 and normalization I2eq1-4p328 independently checked by category.'],
 ['geo-H-history','2026-11-20','GPT-6 Astra Pro, inherited effort, geometry_analysis','used and rechecked in this run','Qualified the earlier printed-proof negative after checking a complete alternative reconstruction:1956 foundations are mathematically sufficient, although minimal-type and final global trace deductions are not displayed. Simon1977 exact primary full-proof locators are Thm3.4p254 and Thm4.1/4.2/Cor4.3pp257-258.'],
 ['geo-H-history','2026-11-20','GPT-6 Astra Pro, inherited effort, geometry_analysis','used and rechecked in this run','Individually inspected physical cote1 pages25-72 at1800px full-page width, recording every page in geometry_cote1_full_observations.tsv. No readable date or identifiable1953letter; physical26 has only Liebe Paula/Wieder ein Breif typed fragment. Damage, overlaps, cross-outs and show-through prevent absence proof.'],
 ['SA23-49','2026-11-20','GPT-6 Astra Pro, inherited effort, geometry_analysis','used and rechecked in this run','Current-run date-scope follow-up: complete individual inspection of physical25-72, not merely contacts or OCR. No particular trace/genus-zero folio date established. Public PDF footer numbers differ from archival pencil numbering; older event wording archive footers is corrected accordingly.'],
 ['geo-H-history','2026-11-20','GPT-6 Astra Pro, inherited effort, root','used and rechecked in this run','Root reports original archive-homepage confirmation that lower-left pencil numbers are archival numbering; printed bottom footer is public PDF sequential numbering. Physical79-80 have public footers78-79 and archival pencil80-81. No identification of skipped pencil3/4 with the1953letter is proved.']
]
event_path = root / 'notes/geometry_CHECK_EVENTS.tsv'
with event_path.open(newline='', encoding='utf-8') as f:
    existing = list(csv.reader(f, delimiter='\t'))
with event_path.open('a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    for row in events:
        if row not in existing:
            writer.writerow(row)

corrections = [
 ['upload/PROMPT(20261120-001045).md','56','Whether the1955-56 papers print the argument is not yet checked','Opened-source distinction: memoirstatements and June1957textual witness;1956 determinant ingredients suffice for a complete reconstruction whose final steps are not displayed there; sheetdate remains unproved','geo-H-history;geo-H-1956-reconstruction','Historical lead resolved at the level of inspected printed content and exact reconstructed implication; not a first-printing collation or priority claim'],
 ['upload/PROMPT(20261120-001045).md','118','Crossed-out79-80 and lemma111-112 without explicit numbering system','These are physical PDF pages; public PDF footers78-79 and110-111; lower-left pencil numbers are archival and form a distinct system','geo-H-history','Root direct original-page inspection and official archive numbering statement; no global offset imposed on unrelated records']
]
correction_path = root / 'notes/geometry_corrections.tsv'
with correction_path.open(newline='', encoding='utf-8') as f:
    existing_corrections = list(csv.reader(f, delimiter='\t'))
with correction_path.open('a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    for row in corrections:
        if row not in existing_corrections:
            writer.writerow(row)

result = {'registry_rows':len(rows), 'new_statement_id':new['id'],
          'events_supplied':len(events), 'corrections_supplied':len(corrections),
          'status':'success', 'source_note':'Category source/proof audit and root targeted audit attributed separately; no historical event copied as a current-run check.'}
(root/'logs/geometry_history_reconstruction_registry.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
