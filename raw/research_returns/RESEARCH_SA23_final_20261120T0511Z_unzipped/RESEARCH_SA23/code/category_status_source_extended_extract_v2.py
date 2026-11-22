"""Correct the broad finding aid's word boundaries and exact citation keys."""
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
    r'\bnot\b.{0,35}(?:open|read|obtain|collat|access|authentic|identif|inspect|observ)|'
    r'\bunopened\b|\bunread\b|\buncollated\b|\bpartial\b|\bselected\b|different ENS', re.I)
files = [ROOT / 'RESEARCH_SA23_paper.tex', *sorted((ROOT / 'sections').glob('*.tex'))]
citations = {}
for path in files:
    contents = path.read_text(encoding='utf-8')
    for match in re.finditer(r'\\cite(?:\[[^\]]*\])*\{([^}]+)\}', contents):
        for key in match.group(1).split(','):
            citations.setdefault(key.strip(), []).append({
                'path': str(path.relative_to(ROOT)),
                'line': contents.count('\n', 0, match.start())+1,
                'citation': match.group(0)})
rows = []
for n, match in enumerate(starts):
    entry = text[match.start():starts[n+1].start() if n+1 < len(starts) else len(text)]
    note_match = re.search(r'\bnote\s*=\s*\{', entry)
    note = entry[note_match.start():] if note_match else ''
    if not pattern.search(note):
        continue
    key = match.group(1)
    rows.append({'key': key, 'bib_line': text.count('\n', 0, match.start())+1,
                 'note': note, 'uses': citations.get(key, [])})
result = {'utc': datetime.now(timezone.utc).isoformat(),
          'bib_sha256': hashlib.sha256(bib.read_bytes()).hexdigest(),
          'entry_count': len(starts), 'rows': rows,
          'scope': 'Finding aid for explicit uninspected/qualified portions. Read each actual use.'}
output = ROOT / 'notes/category_status_source_extended_extract_v2.json'
output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
for row in rows:
    print(row['key'], 'line', row['bib_line'])
    print(row['note'].strip())
    print('USES', json.dumps(row['uses'], ensure_ascii=False))
print('ENTRIES', len(starts), 'QUALIFICATION_HITS', len(rows))
print('SHA256', result['bib_sha256'])
