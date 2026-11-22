"""Compare the actually recovered delayed TDL inventory with saved IA IDs."""
import datetime
import json
import pathlib
import re
import time

root = pathlib.Path(__file__).resolve().parents[1]
start = datetime.datetime.now(datetime.timezone.utc).isoformat(); tick = time.monotonic()
inventory = json.loads((root / 'code/part_c_pfluger_tdl_inventory_delayed_output.json').read_text())
parent_path = root / 'code/root_pfluger_public_ocr_inventory_output.json'
parent_ids = set(re.findall(r'tdl\.(\d+)', parent_path.read_text()))
rows = []
for record in inventory['records']:
    decoded = record['decoded_url']
    if 'mathematical society' not in decoded.lower(): continue
    match = re.search(r'/Articles/[^-]+-(\d+)-', decoded)
    item_id = match.group(1) if match else None
    rows.append(record | {'tdl_id': item_id, 'in_parent_ia_inventory': item_id in parent_ids,
                          'date_strings': re.findall(r'\b(?:18|19|20)\d{2}\b', decoded)})
failed = [r for r in inventory['results'] if r.get('status') != 200]
payload = {'started_utc': start, 'elapsed_seconds': time.monotonic() - tick,
           'network_requests': 0, 'parent_inventory': str(parent_path),
           'parent_tdl_ids': len(parent_ids), 'actually_read_jims_records': len(rows),
           'new_ids': [r for r in rows if not r['in_parent_ia_inventory']],
           'undated_rows': [r for r in rows if not r['date_strings']],
           'failed_catalogue_pages': failed, 'rows': rows,
           'scope': 'Only successfully read catalogue pages are compared; failed pages are not zero results.'}
out = root / 'code/part_c_pfluger_tdl_compare_delayed_output.json'
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
out.with_suffix('.txt').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in payload.items() if k != 'rows'}, ensure_ascii=False, indent=2))
