"""Build navigation aids only. No mathematical verdicts are generated."""
from pathlib import Path
import csv, json, re, hashlib, datetime
ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'SA14_work'
SRC=ROOT/'sources'
rows=list(csv.DictReader((SRC/'SA14_notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
manifest=[]
for p in sorted((SRC/'SA14_texts').rglob('*_transcription.tex')):
    lines=p.read_text().splitlines()
    scans=[]
    cote=None
    for n,line in enumerate(lines,1):
        cm=re.search(r'\\cotefile\{([^}]+)\}',line)
        if cm:cote=cm.group(1)
        sm=re.search(r'\\scanpage\{([^}]+)\}',line)
        if sm:scans.append({'cote':cote,'scan':sm.group(1),'line':n})
    for i,s in enumerate(scans):s['end_line']=scans[i+1]['line']-1 if i+1<len(scans) else len(lines)
    manifest.append({'file':str(p.relative_to(SRC)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'lines':len(lines),'scans':scans})
    out=WORK/'reading_packets'/f'{p.stem}.numbered.txt'
    out.write_text('\n'.join(f'{n:04d} {s}' for n,s in enumerate(lines,1))+'\n')
entries={}
for package in dict.fromkeys(r['package'] for r in rows):
    p=SRC/'SA14_notes/pro'/f'{package}_notes.md'
    lines=p.read_text().splitlines()
    starts=[i for i,s in enumerate(lines) if s.startswith('### ')]
    for n,start in enumerate(starts,1):
        end=starts[n] if n<len(starts) else len(lines)
        eid=f'{package}#{n}'
        entries[eid]={'id':eid,'file':str(p.relative_to(SRC)),'start_line':start+1,'end_line':end,'text':'\n'.join(lines[start:end])}
    (WORK/'reading_packets'/f'{package}_notes.numbered.txt').write_text('\n'.join(f'{i:04d} {s}' for i,s in enumerate(lines,1))+'\n')
(WORK/'research/source_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(WORK/'research/entries_source.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
assert set(entries)=={r['entry_id'] for r in rows}
summary={'entry_count':len(rows),'packages':{p:sum(r['package']==p for r in rows) for p in dict.fromkeys(r['package'] for r in rows)},'transcription_files':len(manifest),'transcribed_scan_occurrences':sum(len(m['scans']) for m in manifest),'second_pass_present':(SRC/'SA14_notes/second_pass').exists()}
print(json.dumps(summary,ensure_ascii=False,indent=2))
