"""Record completed bounded source checks, preserving the unchanged date gate."""
from pathlib import Path
import csv, datetime, hashlib, json, time

root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
log = root / 'logs/root_thesis_seminar_record.json'
if log.exists():
    raise SystemExit('Already recorded; refusing to duplicate the source-check event.')
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
files = [
    'sources/root_thesis_sudoc108391841.html',
    'sources/root_thesis_sudoc108391841_rdf.html',
    'sources/root_schwartz1954_intro.pdf',
    'sources/root_schwartz1954_nuclear.pdf',
    'sources/root_paumier2014_schwartz.pdf',
]
sources = []
for name in files:
    data = (root / name).read_bytes()
    sources.append({'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
event = {
    'statement_id': 'geo-H-history', 'date': '2026-11-20',
    'who': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root',
    'type': 'used and rechecked in this run',
    'outcome': 'Opened primary1953 thesis catalogue (original thesis unopened), original Schwartz seminar introduction and nuclear-operator pp1,3, plus precise Paumier and Brazilian historical finding-aid passages. The seminar eigenvalue passage assumes Hermitian operators. Bourbaki red179/nbr082 is a new specific draft locator, not a date for cote1. No dated identification of target sheets found; gate unchanged.',
    'where': 'notes/root_thesis_seminar_date_audit.md;logs/root_history_fetch05.json;logs/root_history_fetch06.json',
}
with (root / 'notes/root_CHECK_EVENTS.tsv').open('a', newline='') as handle:
    csv.DictWriter(handle, fieldnames=list(event), delimiter='\t').writerow(event)
with (root / 'notes/root_source_log.md').open('a') as handle:
    handle.write('\n\n## Thesis, seminar and exact Bourbaki-draft finding aid\n\n')
    handle.write('The primary thesis catalogue and original Schwartz seminar pages were inspected with precise coverage, together with selected Paumier and Brazilian historical source passages. The original thesis remains unopened; the seminar eigenvalue criterion is explicitly Hermitian. The Paumier locator identifies a related May1953 Bourbaki draft, now assigned for original-source inspection, but no date for the particular cote1 leaves has been established. See notes/root_thesis_seminar_date_audit.md for source URLs, actual pages viewed, hashes, failures and limits.\n')
record = {
    'created_utc': now, 'sources': sources,
    'actually_viewed': {'Schwartz introduction': [2], 'Schwartz nuclear operators': [2, 4]},
    'new_events': 1, 'date_gate_changed': False,
    'elapsed_seconds': time.perf_counter() - start,
}
log.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
