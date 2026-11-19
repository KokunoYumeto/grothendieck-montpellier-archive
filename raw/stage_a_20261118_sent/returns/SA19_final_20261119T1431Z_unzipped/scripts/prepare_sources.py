"""Index supplied sources for human/model reading; no verdicts are generated."""
from pathlib import Path
import csv, json, re, hashlib
from datetime import datetime, timezone

ROOT=Path('/workspace/scratch/a9424869c935')
SRC=ROOT/'source'
OUT=ROOT/'SA19_work'
entries=list(csv.DictReader((SRC/'SA19_notes/NOTES_INDEX.tsv').open(), delimiter='\t'))
pages=[]
manifest=[]
for path in sorted(SRC.rglob('*')):
    if not path.is_file(): continue
    raw=path.read_bytes()
    manifest.append({'file':str(path.relative_to(SRC)), 'bytes':len(raw), 'sha256':hashlib.sha256(raw).hexdigest()})
    if not path.name.endswith('_transcription.tex'): continue
    lines=path.read_text().splitlines()
    cote=None
    starts=[]
    for n,line in enumerate(lines,1):
        cm=re.search(r'\\cotefile\{([^}]+)\}',line)
        if cm: cote=cm.group(1)
        sm=re.search(r'\\scanpage\{([^}]+)\}',line)
        if sm: starts.append((n,cote,sm.group(1)))
    for k,(line,cote,scan) in enumerate(starts):
        end=starts[k+1][0]-1 if k+1<len(starts) else len(lines)
        pages.append({'file':str(path.relative_to(SRC)), 'cote':cote, 'scan':scan,'line_start':line,'line_end':end})
    (OUT/'source_audit'/f'{path.stem}_numbered.txt').write_text('\n'.join(f'{i:04d}\t{line}' for i,line in enumerate(lines,1))+'\n')
for package in sorted({r['package'] for r in entries}):
    path=SRC/'SA19_notes/pro'/f'{package}_notes.md'
    txt=path.read_text()
    starts=list(re.finditer(r'^###\s+(.*)$',txt,re.M))
    packet=[]
    indexed=[r for r in entries if r['package']==package]
    assert len(starts)==len(indexed),(package,len(starts),len(indexed))
    for n,m in enumerate(starts,1):
        end=starts[n].start() if n<len(starts) else len(txt)
        row=dict(indexed[n-1])
        assert row['entry_id']==f'{package}#{n}'
        row['entry_text']=txt[m.start():end]
        row['notes_line_start']=txt[:m.start()].count('\n')+1
        row['notes_line_end']=txt[:end].count('\n')
        packet.append(row)
    (OUT/'source_audit'/f'{package}_entries.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2))
(OUT/'source_audit/source_manifest.json').write_text(json.dumps(manifest,indent=2))
(OUT/'source_audit/page_index.json').write_text(json.dumps(pages,indent=2))
print('Source files:',len(manifest),'indexed entries:',len(entries),'transcribed scan markers:',len(pages))
for cote in sorted({p['cote'] for p in pages},key=int):
    pp=[p for p in pages if p['cote']==cote]
    print('Cote',cote,'markers',len(pp),'distinct scan labels',len({p['scan'] for p in pp}))
print('This script generates locators and immutable-source checksums only. All judgments require passage reading.')
