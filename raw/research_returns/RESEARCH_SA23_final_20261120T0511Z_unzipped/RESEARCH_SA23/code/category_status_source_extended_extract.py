"""Find documentary scope qualifications; this is not a proof verifier."""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
bib = ROOT / 'RESEARCH_SA23_references.bib'
text = bib.read_text(encoding='utf-8')
starts = list(re.finditer(r'^@\w+\{([^,]+),', text, re.M))
pattern = re.compile(
    r'not.{0,35}(?:open|read|obtain|collat|access|authentic|identif|inspect|observ)|'
    r'unopened|unread|uncollated|not yet|only|partial|selected|different ENS', re.I)
files = [ROOT / 'RESEARCH_SA23_paper.tex', *sorted((ROOT / 'sections').glob('*.tex'))]
rows = []
for n, match in enumerate(starts):
    entry = text[match.start():starts[n+1].start() if n+1 < len(starts) else len(text)]
    note_at = entry.find('note')
    note = entry[note_at:] if note_at >= 0 else ''
    if not pattern.search(note):
        continue
    key = match.group(1)
    uses = []
    for path in files:
        for lineno, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if key in line:
                uses.append({'path': str(path.relative_to(ROOT)), 'line': lineno, 'text': line})
    rows.append({'key': key, 'bib_line': text.count('\n', 0, match.start())+1,
                 'note': note, 'uses': uses})
result = {'utc': datetime.now(timezone.utc).isoformat(),
          'bib_sha256': hashlib.sha256(bib.read_bytes()).hexdigest(),
          'entry_count': len(starts), 'rows': rows,
          'scope': 'Broad textual finding aid. A hit need not denote an unopened theorem source.'}
output = ROOT / 'notes/category_status_source_extended_extract.json'
output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
for row in rows:
    print(row['key'], 'line', row['bib_line'])
    print(row['note'].strip())
    print('USES', json.dumps(row['uses'], ensure_ascii=False))
print('ENTRIES', len(starts), 'QUALIFICATION_HITS', len(rows))
print('SHA256', result['bib_sha256'])
