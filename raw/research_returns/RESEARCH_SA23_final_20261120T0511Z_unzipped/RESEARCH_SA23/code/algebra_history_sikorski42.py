"""Record completed bounded search and clarify a manually labelled raw timestamp."""
import datetime, json, pathlib
base = pathlib.Path(__file__).resolve().parents[1]
out = {'utc_recorded': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'changes': []}
raw_path = base / 'notes/algebra_history_web79.json'
data = json.loads(raw_path.read_text())
old = data.get('utc_interval')
data['superseded_unverified_manual_label'] = old
data['utc_interval'] = '2026-11-20 03:18:34--03:19:25 UTC'
data['timestamp_scope'] = 'Bracketed by observed clocks before and after this search sequence; not an exact query timestamp.'
raw_path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
out['changes'].append({'path': str(raw_path.relative_to(base)), 'old_manual_label': old, 'corrected_scope': data['timestamp_scope']})
event = '\t'.join(['geo-H-history', '2026-11-20', 'GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters', 'used and rechecked in this run', 'Bounded Sikorski-letter search completed: complete IHES tag lists four 1966 reports, not letters; complete downloaded PAN inventory has no case-insensitive Sikors occurrence. No original letter, enclosure, or public item description identifying cote1 found; no absence claim beyond checked records.', 'notes/algebra_sikorski_correspondence_search.md;logs/algebra_history_sikorski41.json;notes/algebra_history_web78.json;notes/algebra_history_web79.json;notes/algebra_history_web80.json;notes/algebra_history_web81.json;notes/algebra_history_web82.json;notes/algebra_history_web83.json;notes/algebra_history_web84.json'])
event_path = base / 'notes/algebra_history_CHECK_EVENTS.tsv'
with event_path.open('a') as stream:
    stream.write(event+'\n')
out['changes'].append({'path': str(event_path.relative_to(base)), 'event_added': event})
payload = json.dumps(out, ensure_ascii=False, indent=2)
(base / 'logs/algebra_history_sikorski42.json').write_text(payload+'\n')
print(payload)
