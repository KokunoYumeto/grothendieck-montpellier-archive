"""Canonicalize verified duplicate-work citation keys, preserving source notes.

The bibliography merger, not this script, retains the union of locator notes.
Only citations in our TeX sources are changed; primary sources are excluded.
"""
from pathlib import Path
import csv, json, re, time
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic()
with (ROOT/'part_d/bibliography_alias_suggestions.tsv').open(newline='') as f:
    aliases={r['duplicate_key']:r['canonical_key'] for r in csv.DictReader(f,delimiter='\t')}
pattern=re.compile(r'(\\(?:cite[A-Za-z]*|nocite)\*?(?:\s*\[[^\]]*\]){0,2}\s*\{)([^}]*)(\})')
changes=[]
for path in sorted(ROOT.rglob('*.tex')):
    if any(x in path.relative_to(ROOT).parts for x in ['build','sources','primary_sources']):continue
    original=path.read_text()
    count=[0]
    def replace(match):
        keys=match.group(2).split(',')
        new=[aliases.get(k.strip(),k.strip()) for k in keys]
        if new!=[k.strip() for k in keys]:count[0]+=1
        return match.group(1)+','.join(dict.fromkeys(new))+match.group(3)
    updated=pattern.sub(replace,original)
    if updated!=original:
        path.write_text(updated)
        changes.append({'path':str(path.relative_to(ROOT)),'citation_groups_changed':count[0]})
result={'aliases':aliases,'files_changed':changes,'seconds':round(time.monotonic()-start,4)}
(ROOT/'code/canonicalize_references_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
