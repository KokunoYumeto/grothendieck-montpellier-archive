"""Record the completed bounded Schatten source inspection, including failed retrieval."""
from pathlib import Path
import csv, datetime, hashlib, json, time

root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
target=root/'logs/root_schatten_source_record20.json'
if target.exists():
    raise SystemExit('The completed Schatten inspection is already recorded.')
source=root/'sources/root_schatten1964.pdf'
sha=hashlib.sha256(source.read_bytes()).hexdigest()
assert sha=='8c77d430264e51a5d5f9b69cfaee6283f6b61135ef287324918ca4725be1fbad'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
failed={
    'program':'code/root_schatten_correspondence18.py',
    'url':'https://www.diva-portal.org/smash/get/diva2%3A1849851/FULLTEXT01.pdf',
    'exit_code':130,'cancelled_by_root':True,'pdf_produced':False,
    'stdout_creation_utc':datetime.datetime.fromtimestamp((root/'logs/root_schatten_correspondence18.txt').stat().st_mtime,datetime.timezone.utc).isoformat(),
    'cancellation_bracket_utc':['2026-11-20T04:48:42+00:00','2026-11-20T04:49:06+00:00'],
    'elapsed_seconds':None,
    'runtime_note':'The interrupted program did not emit its own runtime. Cancellation is bracketed by the adjacent observed clock readings; these are not an exact process runtime.',
    'recorded_utc':now,
    'outcome':'Local download remained pending and was cancelled; later web text was read with explicit scope. No local PDF or hash is claimed.'}
(root/'logs/root_schatten_correspondence18.json').write_text(json.dumps(failed,indent=2)+'\n')
with (root/'notes/root_CHECK_EVENTS.tsv').open('a',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=['statement_id','date','who','type','outcome','where'],delimiter='\t')
    writer.writerow({'statement_id':'geo-H-history','date':'2026-11-20',
        'who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root',
        'type':'used and rechecked in this run',
        'outcome':'Schatten historical finding-aid passages and bibliography read with exact text-only scope; NBS7580 catalogue opened but original remains unopened after non-retryable redirect error. Independently advertised original1964 NBS journal article: all nine pages read in text, first/last original pages185/193 visually inspected; no dated Grothendieck proof or manuscript identification. No date-gate movement.',
        'where':'notes/root_schatten_correspondence_date_audit.md;logs/root_schatten_correspondence18.json;logs/root_schatten_journal19.json;logs/root_schatten_source_record20.json'})
record={'created_utc':now,'source_sha256':sha,'original_pages_visually_read':[185,193],
        'pdf_pages_text_read':list(range(1,10)),'new_events':1,'date_gate_changed':False,
        'elapsed_seconds':time.perf_counter()-started}
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
