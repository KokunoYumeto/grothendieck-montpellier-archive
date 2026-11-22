"""Integrate completed publication audits and the precise remaining date question."""
from pathlib import Path
import csv, datetime, json, time

start = time.perf_counter()
root = Path(__file__).resolve().parents[1]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
path = root / 'notes/outcome_table.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
changed = []
for row in rows:
    if row['item'].startswith('Lead6,'):
        row['state'] = 'Publication comparison proved; manuscript date unsettled'
        row['statement_ids'] = 'geo-H-history;geo-H-1956-reconstruction'
        row['outcome'] = ('The memoir states Hilbert genus zero and actual unordered l1 spectral continuity. '
            'The 1956 Fredholm paper prints sufficient determinant foundations for a complete reconstruction, '
            'which we supply; its final deduction is not displayed in that article. The metric resume and '
            'original Lidskii endnote are checked. Bourbaki91 states the product formula in text dated June1957. '
            'All150 public cote1 pages were visually surveyed, but no date has been tied to the specific sheets.')
        changed.append(row['item'])
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)

event_path = root / 'notes/root_CHECK_EVENTS.tsv'
with event_path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    event_fields = reader.fieldnames
    events = list(reader)
outcome = ('Root directly displayed physical cote1 pages2,3,4: public PDF footers1,2,3 '
    'and archival pencil1,2,5. Opened official archive method identifying the pencil numbering '
    'as archival. Earlier archive-footer terminology is corrected to public PDF footer; '
    'the trace/lemma numerical correspondences are unchanged. The gap does not identify '
    'its contents or date the mathematical sheets.')
if not any(row['statement_id'] == 'RUN-COTE1-NUMBERING' and row['outcome'] == outcome for row in events):
    events.append(dict(statement_id='RUN-COTE1-NUMBERING', date=now,
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root',
        type='used and rechecked in this run', outcome=outcome,
        where='notes/root_cote1_date_audit.md; notes/algebra_cote1_date_audit.md; https://grothendieck.umontpellier.fr/'))
with event_path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=event_fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(events)

ledger = root / 'PROGRESS_LEDGER.md'
text = ledger.read_text()
heading = '### Publication-content gate closed; precise manuscript-date gate retained'
if heading not in text:
    text += '\n\n' + heading + '\n\nRecorded ' + now + '. This is a working-state entry, not a formal movement review.\n\n'
    text += ('The complete memoir dependency audit includes both genus zero (IIp13) and '
        'actual unordered l1 spectral continuity (IIRemark4p21). The metric resume '
        'and all three original Lidskii1959 pages are now inspected. A specific '
        'alternative proof risk was resolved by opening Simon1977 and comparing its '
        'arguments with the1956 source: the1956 paper prints mixed coefficient bounds, '
        'mixed-rank vanishing and spectral correspondence sufficient for a full '
        'reconstruction. The new proposition geo-H-1956-reconstruction supplies '
        'minimal type, quasinilpotent trace zero and the global primary-space '
        'quotient argument in full. These deductions are not displayed in the1956 '
        'article. The history statement now distinguishes printed ingredients, '
        'printed sufficient assertions, and a reconstruction.\n\n')
    text += ('The remaining open row is the writing date of the specific cote1 '
        'trace/genus-zero sheets. All150 public PDF pages have been surveyed '
        'individually at readable resolution, within the faint/cancelled-mark '
        'limits recorded by each reader. No date witness is identified. Physical '
        'pages2,3,4 show archival pencil1,2,5, despite consecutive public PDF '
        'footers1,2,3. The official general correspondence restriction does not '
        'identify those skipped numbers as the1953 letter. The next discriminating '
        'step is an independently public dated letter, enclosure description or '
        'archival collation connecting the specific proof to a pre1959 date. '
        'Kothe and other contemporary correspondence inventories are being checked.\n\n')
    text += ('The main PartA gates remain closed under the stated hypotheses. '
        'The first formal review remains due03:10UTC; packaging and the wording '
        'clarification above are not themselves movement.\n')
    ledger.write_text(text)

result = {'created_utc': now, 'updated_outcomes': changed,
          'root_event_count': len(events), 'seconds': time.perf_counter() - start}
(root / 'logs/root_history_integrate.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
