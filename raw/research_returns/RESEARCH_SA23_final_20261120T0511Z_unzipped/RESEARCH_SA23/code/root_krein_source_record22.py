"""Record a bounded custodial finding-aid reading without claiming letter access."""
from pathlib import Path
import csv, datetime, json, time
root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
target=root/'logs/root_krein_source_record22.json'
if target.exists():
    raise SystemExit('Krein source scope already recorded.')
fetch=json.loads((root/'logs/root_krein_correspondence21.json').read_text())
assert fetch['returncode']==22 and '522' in fetch['stderr']
record={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'read_scope':'Returned web text on article pp651–657, ending mid-spread; no visual collation.',
    'unread':['article end pp658–659','underlying letters','complete fonds inventory'],
    'found_locator':'Institute of Archival Studies NBUV fonds346 inventory3; survey reports six Gohberg letters1957–1969.',
    'date_gate_changed':False,'new_events':1}
with (root/'notes/root_CHECK_EVENTS.tsv').open('a',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=['statement_id','date','who','type','outcome','where'],delimiter='\t')
    writer.writerow({'statement_id':'geo-H-history','date':'2026-11-20',
        'who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root',
        'type':'used and rechecked in this run',
        'outcome':'Partially read original custodial Krein correspondence survey in returned web text, pp651–657; ending and letters remain unopened. Fonds346 inventory3 and six Gohberg letters1957–1969 give a concrete finding aid without target-proof identification. Timeout searches are not zero-hit findings; local retrieval HTTP522. Gate unchanged.',
        'where':'notes/root_krein_correspondence_date_audit.md;logs/root_krein_correspondence21.json;logs/root_krein_source_record22.json'})
record['elapsed_seconds']=time.perf_counter()-started
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
