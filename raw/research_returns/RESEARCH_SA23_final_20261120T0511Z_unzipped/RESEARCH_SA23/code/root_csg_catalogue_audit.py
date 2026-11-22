"""Extract the two actual CSG finding aids, retaining full audit text and links.

We use Python's standard HTML parser. An earlier unsaved exploratory import
of bs4 failed with ModuleNotFoundError; it read or changed no source content.
This program replaces that unavailable dependency and records its outcome.
Keyword matching here is a finding aid, not a claim about unopened originals.
"""
from pathlib import Path
from html.parser import HTMLParser
import datetime, hashlib, json, re, time, unicodedata

ROOT = Path(__file__).resolve().parents[1]
started = time.perf_counter()

class Extract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.parts = []
        self.links = []
        self.active = None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {'script', 'style'}:
            self.hidden += 1
        if tag == 'a' and not self.hidden:
            self.active = {'href': attrs.get('href', ''), 'text': []}
    def handle_endtag(self, tag):
        if tag in {'script', 'style'}:
            self.hidden = max(0, self.hidden - 1)
        if tag == 'a' and self.active is not None:
            self.active['text'] = ' '.join(self.active['text'])
            self.links.append(self.active)
            self.active = None
    def handle_data(self, data):
        if self.hidden:
            return
        text = ' '.join(data.split())
        if text:
            self.parts.append(text)
            if self.active is not None:
                self.active['text'].append(text)

def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text.lower())
                   if unicodedata.category(c) != 'Mn')

records = []
for stem in ['root_csg_unpublished_catalogue', 'root_csg_transcription_catalogue']:
    path = ROOT / 'sources' / (stem + '.html')
    raw = path.read_bytes()
    parser = Extract()
    parser.feed(raw.decode('utf-8'))
    lines = parser.parts
    target = ROOT / 'sources' / (stem + '_text.txt')
    target.write_text('\n'.join(f'{i:04d}: {s}' for i, s in enumerate(lines, 1)) + '\n')
    linkpath = ROOT / 'sources' / (stem + '_links.json')
    linkpath.write_text(json.dumps(parser.links, ensure_ascii=False, indent=2) + '\n')
    queries = ['fredholm', 'lidskii', 'nucleair', 'trace', 'cote 1', '1953', '1954', '1955']
    hits = {q: [{'line': i, 'text': s} for i, s in enumerate(lines, 1)
                if q in normalize(s)] for q in queries}
    records.append({'source': str(path.relative_to(ROOT)), 'bytes': len(raw),
                    'sha256': hashlib.sha256(raw).hexdigest(),
                    'text_lines': len(lines), 'links': len(parser.links),
                    'text_output': str(target.relative_to(ROOT)),
                    'link_output': str(linkpath.relative_to(ROOT)), 'keyword_hits': hits})
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'preliminary_dependency_check': 'bs4 unavailable; standard-library parser used instead',
          'records': records, 'elapsed_seconds': time.perf_counter() - started}
(ROOT / 'logs/root_csg_catalogue_audit.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False, indent=2))
