"""Source inventory and read-only navigation; no scientific verdicts generated."""
from pathlib import Path
import csv, json, hashlib, re, datetime

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'sources'
OUT = ROOT / 'SA18_work'
records = []
for p in sorted(SRC.rglob('*')):
    if not p.is_file():
        continue
    raw = p.read_bytes()
    lines = raw.decode('utf-8').splitlines()
    records.append({'path':str(p.relative_to(SRC)), 'bytes':len(raw),
                    'sha256':hashlib.sha256(raw).hexdigest(), 'lines':len(lines)})
(OUT/'source_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
idx=list(csv.DictReader((SRC/'SA18_notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
entries=[]
for p in sorted((SRC/'SA18_notes/pro').glob('*_notes.md')):
    package=p.name.removesuffix('_notes.md')
    lines=p.read_text().splitlines()
    heads=[i for i,x in enumerate(lines) if x.startswith('### ')]
    for n,start in enumerate(heads,1):
        end=heads[n] if n<len(heads) else len(lines)
        entries.append({'entry_id':f'{package}#{n}','file':str(p.relative_to(SRC)),
                        'start_line':start+1,'end_line':end,
                        'heading':lines[start][4:],'text':'\n'.join(lines[start:end])})
assert {e['entry_id'] for e in entries}=={r['entry_id'] for r in idx}
(OUT/'research/parsed_entries.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2))
pages=[]
for p in sorted((SRC/'SA18_texts').rglob('*_transcription.tex')):
    lines=p.read_text().splitlines(); cote=None; active=None
    for i,line in enumerate(lines,1):
        cm=re.search(r'\\cotefile\{([^}]+)\}',line)
        if cm:
            cote=cm.group(1)
        sm=re.search(r'\\scanpage\{([^}]+)\}',line)
        if sm:
            if active:
                active['end_line']=i-1; pages.append(active)
            active={'file':str(p.relative_to(SRC)),'cote':cote,'scan':sm.group(1),'start_line':i}
    if active:
        active['end_line']=len(lines);pages.append(active)
(OUT/'research/page_index.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
print('Source files:',len(records))
print('Indexed entries:',len(idx),'Parsed entries:',len(entries))
print('Transcribed scan blocks:',len(pages))
print('Source hashes, entry locators and scan locators saved; no verdicts inferred.')
