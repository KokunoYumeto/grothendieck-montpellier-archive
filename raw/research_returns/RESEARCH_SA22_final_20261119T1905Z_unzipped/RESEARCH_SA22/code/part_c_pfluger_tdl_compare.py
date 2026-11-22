"""Compare actually read TDL journal records to the parent's saved IA inventory.
This is a partial-catalogue comparison, not proof of exhaustive source absence.
"""
import datetime
import json
import pathlib
import re
import time

root=pathlib.Path(__file__).resolve().parents[1];start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic()
inventory=json.loads((root/'code/part_c_pfluger_tdl_inventory_output.json').read_text())
parent_path=root/'code/root_pfluger_public_ocr_inventory_output.json'
parent_ids=set(re.findall(r'tdl\.(\d+)',parent_path.read_text()))
rows=[]
for record in inventory['records']:
    decoded=record['decoded_url']
    if 'mathematical society' not in decoded.lower():continue
    match=re.search(r'/Articles/[^-]+-(\d+)-',decoded)
    item_id=match.group(1) if match else None
    rows.append(record|{'tdl_id':item_id,'in_parent_ia_inventory':item_id in parent_ids,'date_strings':re.findall(r'\b(?:18|19|20)\d{2}\b',decoded)})
payload={'started_utc':start,'elapsed_seconds':time.monotonic()-tick,'network_requests':0,'parent_inventory':str(parent_path),'parent_tdl_ids':len(parent_ids),'actually_read_jims_records':len(rows),'new_ids':[x for x in rows if not x['in_parent_ia_inventory']],'undated_rows':[x for x in rows if not x['date_strings']],'rows':rows,'scope':'Partial: seven pagination requests, two503 failures; only cached first page plus five further successful pages were read.'}
out=root/'code/part_c_pfluger_tdl_compare_output.json';out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n');out.with_suffix('.txt').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in payload.items() if k!='rows'},ensure_ascii=False,indent=2))
