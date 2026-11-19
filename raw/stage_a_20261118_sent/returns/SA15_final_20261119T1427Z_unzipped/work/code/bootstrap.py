from pathlib import Path
import re, json, csv, hashlib
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'work'
(OUT / 'outputs').mkdir(parents=True, exist_ok=True)
(OUT / 'root_review').mkdir(exist_ok=True)
(OUT / 'root_review' / 'code').mkdir(exist_ok=True)
(OUT / 'root_review' / 'outputs').mkdir(exist_ok=True)
now = datetime.now(timezone.utc).isoformat()
with (OUT / 'progress.log').open('a') as f:
    f.write('2026-11-19T13:02:39+00:00\tSTART\tRead supplied brief; extracted SA15_Cristaux.zip once.\n')
    f.write(now + '\tSTAGE 1 START\tParallel manuscript reading, note adjudication and claim extraction.\n')
inventory=[]; pages=[]; notes=[]
for p in sorted((ROOT / 'sources').rglob('*')):
    if not p.is_file(): continue
    b=p.read_bytes()
    inventory.append({'path':str(p.relative_to(ROOT / 'sources')), 'size':len(b), 'sha256':hashlib.sha256(b).hexdigest()})
    if p.name.endswith('_transcription.tex'):
        lines=p.read_text().splitlines(); cote=None; cur=None
        for n,l in enumerate(lines,1):
            cm=re.search(r'\\cotefile\{([^}]+)\}',l)
            if cm:
                if cur:
                    cur['line_end']=n-1; pages.append(cur); cur=None
                cote=cm.group(1)
            sm=re.search(r'\\scanpage\{([^}]+)\}',l)
            if sm:
                if cur: cur['line_end']=n-1; pages.append(cur)
                cur={'file':str(p.relative_to(ROOT / 'sources')), 'cote':cote,'scan':sm.group(1),'line_start':n}
        if cur: cur['line_end']=len(lines); pages.append(cur)
    if '/pro/' in str(p) and p.name.endswith('_notes.md'):
        lines=p.read_text().splitlines(); package=p.name.removesuffix('_notes.md')
        level=3 if package=='MPL_7_061-072+8_001-078' else 2
        starts=[(n,l) for n,l in enumerate(lines,1) if re.match(r'^#{'+str(level)+r'} ',l)]
        for i,(n,heading) in enumerate(starts):
            notes.append({'source_id':package+('#' if level==3 else '##')+str(i+1), 'package':package,'heading':heading,'line_start':n,'line_end':starts[i+1][0]-1 if i+1<len(starts) else len(lines),'indexed':level==3})
(OUT/'source_inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
(OUT/'page_map.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2)+'\n')
(OUT/'note_map.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
result={'start_utc':'2026-11-19T13:02:39+00:00','first_checkpoint_due_utc':'2026-11-19T13:47:39+00:00','source_files':len(inventory),'transcribed_scan_occurrences':len(pages),'indexed_notes':sum(x['indexed'] for x in notes),'unindexed_notes':sum(not x['indexed'] for x in notes),'note_counts':{p:sum(x['package']==p for x in notes) for p in sorted({x['package'] for x in notes})},'second_pass_present':(ROOT/'sources/SA15_notes/second_pass').exists()}
(OUT/'outputs/bootstrap.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
