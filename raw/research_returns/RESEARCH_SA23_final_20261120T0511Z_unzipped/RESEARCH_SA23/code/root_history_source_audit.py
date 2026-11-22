"""Record completed original-page inspections without turning them into date proofs."""
from pathlib import Path
import csv, datetime, json, time

start = time.perf_counter()
root = Path(__file__).resolve().parents[1]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
path = root / 'notes/root_CHECK_EVENTS.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
who = 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root'
additions = [
    dict(statement_id='RUN-COTE1-DATE', date=now, who=who,
         type='used and rechecked in this run',
         outcome='Original cote1 physical79–81 and every physical111–150 displayed individually, plus cover and physical26 Paula fragment. Physical79–80 and111–112 match the prompt content; archive footers are one lower. No date witness identified. This is a source inspection, not a proof of absence or an inferred manuscript date.',
         where='notes/root_cote1_date_audit.md; code/root_render_cote1.py; corresponding rendering logs'),
    dict(statement_id='geo-H-history', date=now, who=who,
         type='used and rechecked in this run',
         outcome='Original memoir II§1 no4 Remark4 printedp21 displayed: Hilbert eigenvalue continuity has actual unordered l^p target, including p=1; it is stated as an input to the sketched Banach reduction. The finite-rank implication to trace equality was checked. Category dependency audit distinguishes this assertion from a printed Hilbert proof.',
         where='notes/category_memoir_remark4-222.png; notes/category_memoir_continuity_audit.md'),
]
added = []
for row in additions:
    if not any(old['statement_id'] == row['statement_id'] and old['outcome'] == row['outcome'] for old in rows):
        rows.append(row)
        added.append(row['statement_id'])
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)
log = root / 'notes/root_source_log.md'
text = log.read_text()
heading = '## Complete final-range dating inspection and alternative spectral assertion'
if heading not in text:
    text += '\n\n' + heading + '\n\n'
    text += ('We directly displayed every physical cote1 page111–150, physical79–81, '
             'the cover, and the typed Paula fragment on physical26. The precise '
             'numbering table, observed subjects, rendering sizes and limitations '
             'are in notes/root_cote1_date_audit.md. We identified no date witness '
             'in those pages and do not infer one from dossier adjacency.\n\n')
    text += ('We also directly displayed memoir II§1 no4 Remark4 p21. Its Hilbert '
             'continuity assertion uses genuine unordered l^p, not the weaker '
             'intersection over larger exponents. At p=1, finite-rank approximation '
             'would imply trace equality by the inequality between the difference '
             'of spectral sums and the unordered l1 distance. The paragraph states '
             'this Hilbert assertion as an input to its Banach reduction. The '
             'separate category audit traces the stated dependencies and appendix '
             'omission explanation; it does not mistake a statement for its proof.\n')
    log.write_text(text)
result = {'created_utc': now, 'added_event_ids': added,
          'event_count': len(rows), 'seconds': time.perf_counter() - start}
(root / 'logs/root_history_source_audit.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
