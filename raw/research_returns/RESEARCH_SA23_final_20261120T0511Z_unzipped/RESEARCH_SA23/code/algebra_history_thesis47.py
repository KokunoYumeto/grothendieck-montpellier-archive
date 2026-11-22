"""Record exact public thesis catalogue fields and scope of direct visual readings."""
import datetime
import hashlib
import json
import pathlib
import xml.etree.ElementTree as ET

base = pathlib.Path(__file__).resolve().parents[1]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
path = base / 'sources/algebra_history_thesis_unimarc108391841.xml'
raw = path.read_bytes()
record = ET.fromstring(raw)
tags = ['034', '200', '214', '215', '328', '801', '930', '940', '941']
fields = []
for field in record.findall('datafield'):
    if field.get('tag') in tags:
        fields.append({
            'tag': field.get('tag'),
            'subfields': [{'code': s.get('code'), 'text': s.text} for s in field.findall('subfield')],
        })
output = {
    'utc_recorded': now,
    'source_path': str(path.relative_to(base)),
    'bytes': len(raw),
    'sha256': hashlib.sha256(raw).hexdigest(),
    'fields': fields,
    'has_856': bool(record.findall("datafield[@tag='856']")),
    'actual_direct_visual_readings': [
        {'path': 'sources/algebra_history_thesis_exhibition_p005.png', 'physical_page': 5, 'printed_page': 4, 'scope': 'Modern exhibition source credits, actually displayed and read at approximately 03:37 UTC; not a thesis facsimile'},
        {'path': 'sources/algebra_history_thesis_exhibition_p010.png', 'physical_page': 10, 'printed_page': 9, 'scope': 'Modern illustrated chronology with 1953 thesis entry, actually displayed and read at approximately 03:37 UTC; not an original thesis cover or leaf'},
    ],
    'access_limits': {
        'sorbonne_primo': 'Actual public catalogue link returned403; stopped, no bypass',
        'numir': 'Public entry returned502 in webreader then503 in one ordinary unauthenticated HTTP retrieval; no collection content opened; no proxy used',
    },
    'result': 'Exact physical holding identified; no original thesis scan or cote1 identity/date established',
}
event = '\t'.join([
    'geo-H-history', '2026-11-20',
    'GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters',
    'used and rechecked in this run',
    'Public1953thesis UNIMARC and multiwhere records identify shelfmark Y Math 1953 (2) -4, exemplar28780237X, RCR751052113; CCFr resolves BCPR at Jussieu. No856digital link, originalthesis scan or cote1 date identified. Primo403 stopped; publicNUMiR502/503; modernexhibition timeline visually classified.',
    'notes/algebra_thesis1953_source_search.md;logs/algebra_history_thesis45.json;logs/algebra_history_thesis46.json;logs/algebra_history_thesis47.json;notes/algebra_history_web97.json;notes/algebra_history_web98.json;notes/algebra_history_web99.json;notes/algebra_history_web100.json;notes/algebra_history_web101.json;notes/algebra_history_web102.json',
])
event_path = base / 'notes/algebra_history_CHECK_EVENTS.tsv'
existing = event_path.read_text()
if event not in existing:
    with event_path.open('a') as stream:
        stream.write(event + '\n')
output['event'] = event
payload = json.dumps(output, ensure_ascii=False, indent=2)
(base / 'logs/algebra_history_thesis47.json').write_text(payload + '\n')
print(payload)
