"""Extract source packets with stable, absolute source-file line numbers.

This is mechanical indexing only; it does not assign mathematical verdicts.
"""
import csv, json, re, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
out=ROOT/'work'
rows=list(csv.DictReader((ROOT/'sources/notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
inventory=[]
for package in dict.fromkeys(r['package'] for r in rows):
    d=out/package
    d.mkdir(parents=True,exist_ok=True)
    notes=ROOT/'sources/notes/pro'/f'{package}_notes.md'
    text=notes.read_text()
    headings=list(re.finditer(r'^### (.*)$',text,re.M))
    entries=[]
    for n,m in enumerate(headings,1):
        stop=headings[n].start() if n<len(headings) else len(text)
        entry={'id':f'{package}#{n}','heading':m.group(1),'source_start':text[:m.start()].count('\n')+1,'text':text[m.start():stop]}
        entries.append(entry)
    (d/'entries.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2))
    for src in [ROOT/'sources/texts/pro'/f'{package}_transcription.tex',notes,ROOT/'sources/notes/pro'/f'{package}_doubts.md']:
        numbered='\n'.join(f'{n:04d}  {line}' for n,line in enumerate(src.read_text().splitlines(),1))+'\n'
        (d/(src.stem+'.numbered.txt')).write_text(numbered)
    inventory.append({'package':package,'indexed_entries':sum(r['package']==package for r in rows),'actual_entries':len(entries)})
for src in (ROOT/'sources/texts/codex').glob('*.tex'):
    (out/(src.stem+'.numbered.txt')).write_text('\n'.join(f'{n:04d}  {s}' for n,s in enumerate(src.read_text().splitlines(),1))+'\n')
pages=[]
for src in sorted((ROOT/'sources/texts').rglob('*_transcription.tex')):
    cote=None; current=None
    for n,line in enumerate(src.read_text().splitlines(),1):
        c=re.search(r'\\cotefile\{([^}]+)\}',line)
        if c:cote=c.group(1)
        s=re.search(r'\\scanpage\{([^}]+)\}',line)
        if s:
            if current:current['end']=n-1; pages.append(current)
            current={'file':str(src.relative_to(ROOT/'sources/texts')),'cote':cote,'scan':s.group(1),'start':n}
    if current:current['end']=n; pages.append(current)
(out/'pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
(ROOT/'deliverable/outputs/source_inventory.json').write_text(json.dumps({'entries':inventory,'pages':pages,'source_sha256':{str(p.relative_to(ROOT/'sources')):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'sources').rglob('*')) if p.is_file()}},ensure_ascii=False,indent=2))
print(json.dumps({'packages':inventory,'total_entries':len(rows),'transcribed_scan_occurrences':len(pages)},indent=2))
