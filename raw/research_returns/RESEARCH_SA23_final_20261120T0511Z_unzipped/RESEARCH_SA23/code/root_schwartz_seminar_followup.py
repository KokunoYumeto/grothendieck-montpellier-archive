"""Index the three adjacent original seminar lectures for a bounded date inquiry."""
from pathlib import Path
import datetime, hashlib, json, re, time
import fitz

root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
pattern = re.compile(r'trace|fredholm|hilbert|genre|d[ée]termin|valeurs?\s+propre', re.I)
items = []
lines = []
for number in [13, 14, 15]:
    path = root / f'sources/root_schwartz1954_expose{number}.pdf'
    document = fitz.open(path)
    pages = []
    lines.append(f'## Expose {number}\n')
    for index, page in enumerate(document):
        text = page.get_text()
        matches = list(pattern.finditer(text))
        if not matches:
            continue
        pages.append(index + 1)
        lines.append(f'Physical page {index + 1}: {len(matches)} finding-aid matches')
        spans = []
        for match in matches:
            left, right = max(0, match.start() - 280), min(len(text), match.end() + 420)
            if spans and left <= spans[-1][1]:
                spans[-1][1] = max(right, spans[-1][1])
            else:
                spans.append([left, right])
        for left, right in spans:
            lines.append(text[left:right].strip())
        lines.append('')
    items.append({'lecture': number, 'physical_pages': len(document),
                  'native_characters': sum(len(page.get_text()) for page in document),
                  'hit_pages': pages, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
out = root / 'notes/root_schwartz_seminar_followup_contexts.txt'
out.write_text('\n'.join(lines) + '\n')
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'pattern': pattern.pattern, 'sources': items,
          'context_file': str(out.relative_to(root)),
          'scope': 'Native text keyword finding aid only; no claim of exhaustive absence or automatic visual inspection.',
          'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_schwartz_seminar_followup.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
