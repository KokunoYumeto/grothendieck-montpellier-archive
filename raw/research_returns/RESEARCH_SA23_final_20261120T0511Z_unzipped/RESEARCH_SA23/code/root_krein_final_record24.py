"""Record the final bounded Krein metadata branch without claiming original access."""
from pathlib import Path
import csv, datetime, json, time

root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
target=root/'logs/root_krein_final_record24.json'
if target.exists():
    raise SystemExit('Final Krein metadata branch already recorded.')
fetch=json.loads((root/'logs/root_krein_autographs23.json').read_text())
assert fetch['returncode']==22 and '503' in fetch['stderr']
record={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope':'Search-result metadata for the 2000 Krein autograph-book catalogue and two custodial articles; all their originals remain unopened.',
        'access_results':['2012 Archives of Ukraine PDF: web403, stopped',
                          '2012 National Memory PDF: web timeout, no local retrieval',
                          'NBUV catalogue page: web timeout',
                          'Rikun bibliographic guide: web timeout, one local HTTP503'],
        'original_inscriptions_read':0,'date_gate_changed':False,'new_events':1}
with (root/'notes/root_CHECK_EVENTS.tsv').open('a',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=['statement_id','date','who','type','outcome','where'],delimiter='\t')
    writer.writerow({'statement_id':'geo-H-history','date':'2026-11-20',
        'who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root',
        'type':'used and rechecked in this run',
        'outcome':'Read only search-result metadata for Krein autograph-book catalogue (Odessa2000,60pp) and additional custodial descriptions. No catalogue original, inscription or target letter read. Exact public access failures retained; no date witness. Gate unchanged.',
        'where':'notes/root_krein_correspondence_date_audit.md;notes/root_history_web79.json through root_history_web86.json;logs/root_krein_autographs23.json'})
record['elapsed_seconds']=time.perf_counter()-started
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
