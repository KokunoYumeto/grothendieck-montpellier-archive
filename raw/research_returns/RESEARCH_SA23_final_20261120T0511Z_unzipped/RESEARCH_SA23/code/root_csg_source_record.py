"""Record the completed CSG finding-aid check without implying source proofs."""
from pathlib import Path
import csv, datetime, json, time
root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
target=root/'logs/root_csg_source_record.json'
if target.exists():
    raise SystemExit('CSG source event already recorded; refusing a duplicate.')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
fields=['statement_id','date','who','type','outcome','where']
row={'statement_id':'geo-H-history','date':'2026-11-20',
     'who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root',
     'type':'used and rechecked in this run',
     'outcome':'Opened both CSG finding aids; searched complete extracted texts and read early scientific/correspondence descriptions and archive-scope paragraphs. The unpublished list is explicitly selective. No new original or dated identification of the target sheets was obtained; no date-gate movement.',
     'where':'notes/root_csg_date_audit.md;logs/root_csg_catalogue_audit.json;logs/root_history_fetch15.json;logs/root_history_fetch16.json'}
with (root/'notes/root_CHECK_EVENTS.tsv').open('a',newline='') as handle:
    csv.DictWriter(handle,fieldnames=fields,delimiter='\t').writerow(row)
with (root/'notes/root_source_log.md').open('a') as handle:
    handle.write('\n\n## CSG finding-aid follow-up\n\n')
    handle.write('The complete returned texts of the CSG unpublished-work and transcription catalogues were searched, and early entries plus archive-scope descriptions read. These are finding aids, not newly opened original manuscripts. The selective list and existing Dixmier pointers did not identify or date the particular proof. Exact scope and hashes are retained in notes/root_csg_date_audit.md.\n')
record={'created_utc':stamp,'new_events':1,'new_originals_read':0,
        'date_gate_changed':False,'elapsed_seconds':time.perf_counter()-started}
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
