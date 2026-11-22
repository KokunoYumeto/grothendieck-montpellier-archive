"""Record source readings actually completed after the first seminar audit."""
from pathlib import Path
import csv, datetime, hashlib, json, time

root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
target = root / 'logs/root_seminar_followup_record.json'
if target.exists():
    raise SystemExit('Source follow-up already recorded; no duplicate event.')
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
events = [
    ('Read complete native text of Serre1965 report as printed1989; visually inspected pp199-200,204. Searched complete native texts of Schwartz1954 exposés13-15 and viewed seven specified pages. Exposé13 section3 is the Hermitian nuclear criterion and duality, not a general spectral-trace proof or dated cote1 identification. No date-gate movement.',
     'notes/root_report_and_seminar_followup.md;logs/root_history_fetch07.json;logs/root_history_fetch08.json;logs/root_schwartz_seminar_followup.json'),
    ('Independently displayed Bourbaki179/NBR082 catalogue cover, first typed page and enlarged margin. Confirmed visible Schwartz/mai53 wording and document identifier; annotation authorship/time unverified. The category agent separately read all eight typed pages. This date mark does not identify Montpellier cote1; gate unchanged.',
     'notes/category_bourbaki_nbr082_date_audit.md;notes/root_thesis_seminar_date_audit.md'),
]
with (root / 'notes/root_CHECK_EVENTS.tsv').open('a', newline='') as handle:
    fields = ['statement_id', 'date', 'who', 'type', 'outcome', 'where']
    writer = csv.DictWriter(handle, fieldnames=fields, delimiter='\t')
    for outcome, where in events:
        writer.writerow({'statement_id': 'geo-H-history', 'date': '2026-11-20',
            'who': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root',
            'type': 'used and rechecked in this run', 'outcome': outcome, 'where': where})
with (root / 'notes/root_source_log.md').open('a') as handle:
    handle.write('\n\n## Adjacent seminar lectures and original Bourbaki draft\n\n')
    handle.write('The completed original-source follow-up is in notes/root_report_and_seminar_followup.md. Root read the original Serre report in native extraction and viewed its relevant section, then inspected the indicated original Schwartz lecture pages. The latter concern a Hermitian nuclear criterion, duality and approximation, without identifying the target leaves. The category agent obtained and read all of Bourbaki179/NBR082; root independently inspected its cover and date marks. The draft concerns elementary projective tensor-product properties. These are completed bounded source checks, not a smaller date gate.\n')
record = {'created_utc': now, 'new_events': len(events),
    'serre_visual_physical_pages': [1, 2, 6],
    'schwartz_visual_physical_pages': {'13': [2, 4, 5, 6], '14': [2], '15': [2, 8]},
    'bourbaki_root_views': ['cover', 'first typed page', 'enlarged pencil margin'],
    'date_gate_changed': False, 'elapsed_seconds': time.perf_counter() - start}
target.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
