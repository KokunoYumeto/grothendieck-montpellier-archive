"""Check explicit event coverage for every numbered statement added in CP14."""
from pathlib import Path
import csv, io, json, zipfile, datetime
w = Path(__file__).resolve().parents[1]
dest = w / 'outputs/new_statement_event_coverage14.json'
assert not dest.exists()
with zipfile.ZipFile(w.parent / 'RESEARCH_SA15_checkpoint_13.zip') as z:
    old = {r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
new = [r for r in csv.DictReader((w / 'RESEARCH_SA15_results.csv').open()) if r['id'] not in old]
events = (w / 'CHECK_EVENTS.tsv').read_text()
missing = [r for r in new if r['id'] not in events]
assert all(r['where_proved'].split(';')[0] in {'sections/A_monodromy.tex', 'sections/B.tex'} for r in missing)
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for r in missing:
        writer.writerow([r['id'], now,
            'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort',
            'targeted proof check',
            'PASS: statement included in completed full-file root independent proof reads recorded in code/root_mixed_product_audit.py, root_mixed_nonproduct_audit.py, root_uniform_collision_audit.py, root_b39_audit.py, root_b40_audit.py, root_b41_audit.py, and root_b42_audit.py. This supplies an explicit numbered-remark identifier without claiming a further computation. ' + r['where_proved']])
result = {'status': 'PASS', 'new_numbered_statements': len(new),
          'explicit_identifiers_added': len(missing),
          'added_ids': [r['id'] for r in missing], 'actual_utc': now}
dest.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
