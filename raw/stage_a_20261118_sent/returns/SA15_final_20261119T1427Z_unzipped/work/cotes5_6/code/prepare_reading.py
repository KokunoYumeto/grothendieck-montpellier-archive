from pathlib import Path
import re,json

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parents[1]
PKG='MPL_5+6_001-037'
textpath=ROOT/'sources/SA15_texts/pro'/f'{PKG}_transcription.tex'
notepath=ROOT/'sources/SA15_notes/pro'/f'{PKG}_notes.md'
lines=textpath.read_text().splitlines()
pages=[]; cote=None; current=None
for i,line in enumerate(lines,1):
    cm=re.match(r'\\cotefile\{([^}]+)\}',line)
    if cm: cote=cm.group(1)
    sm=re.match(r'\\scanpage\{([^}]+)\}',line)
    if sm:
        if current: pages.append(current)
        current={'cote':cote,'scan':int(sm.group(1)),'start':i,'text':[]}
    if current: current['text'].append(f'{i:04d}: {line}'); current['end']=i
if current:pages.append(current)
nlines=notepath.read_text().splitlines(); entries=[];cur=None
for i,line in enumerate(nlines,1):
    if line.startswith('## '):
        if cur:entries.append(cur)
        cur={'ordinal':len(entries)+1,'heading':line,'start':i,'text':[]}
    if cur:cur['text'].append(f'{i:04d}: {line}');cur['end']=i
if cur:entries.append(cur)
for e in entries:
    m=re.search(r'Cote (\d+), scan (\d+)',e['heading'])
    e['cote']=m.group(1) if m else None;e['scan']=int(m.group(2)) if m else None
    e['id']=PKG+'##'+str(e['ordinal'])
for page in pages:
    pn=OUT/'outputs'/f"reading_c{page['cote']}_s{page['scan']:03d}.txt"
    sections=[f"COTE {page['cote']} SCAN {page['scan']} — transcription lines {page['start']}–{page['end']}",'\n'.join(page['text'])]
    for e in entries:
        if (e['cote'],e['scan'])==(page['cote'],page['scan']):
            sections += ['\nSOURCE ENTRY '+e['id'],'\n'.join(e['text'])]
    pn.write_text('\n'.join(sections))
(OUT/'outputs/page_inventory.json').write_text(json.dumps([{k:v for k,v in p.items() if k!='text'} for p in pages],indent=2))
(OUT/'outputs/supplemental_note_inventory.json').write_text(json.dumps(entries,indent=2))
print(json.dumps({'pages':len(pages),'supplementary_entries':len(entries),'cotes':sorted(set(p['cote'] for p in pages)), 'unplaced_notes':[e['id'] for e in entries if not e['cote']]},indent=2))
