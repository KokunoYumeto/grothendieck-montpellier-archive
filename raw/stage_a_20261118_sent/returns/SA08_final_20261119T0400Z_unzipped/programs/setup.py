"""Extract supplied archives safely and prepare line-addressable research inputs.

Run from the conversation workspace. No editorial verdicts are generated here.
"""
from pathlib import Path
import csv, json, zipfile, datetime, hashlib, re

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'SA08_work'
for sub in ['sources/notes','sources/texts','work','outputs','logs','programs','research']:
    (WORK/sub).mkdir(parents=True,exist_ok=True)
for kind in ['notes','texts']:
    archive = ROOT/'upload'/f'SA08_{kind}.zip'
    with zipfile.ZipFile(archive) as z:
        for name in z.namelist():
            dest = (WORK/'sources'/kind/name).resolve()
            if not dest.is_relative_to((WORK/'sources'/kind).resolve()):
                raise ValueError(name)
        z.extractall(WORK/'sources'/kind)
rows=list(csv.DictReader((WORK/'sources/notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
print('Index columns:',list(rows[0]))
print('Indexed entries:',len(rows))
print((WORK/'sources/texts/TOPIC.md').read_text())
print('First rows:',json.dumps(rows[:3],ensure_ascii=False,indent=2))
inventory=[]
for path in sorted((WORK/'sources').rglob('*')):
    if path.is_file():
        b=path.read_bytes()
        inventory.append({'path':str(path.relative_to(WORK)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
        if path.suffix in ['.md','.tex']:
            relative=path.relative_to(WORK/'sources')
            numbered=WORK/'work/numbered'/relative
            numbered.parent.mkdir(parents=True,exist_ok=True)
            numbered.write_text(''.join(f'{i:5d}  {s}\n' for i,s in enumerate(path.read_text().splitlines(),1)))
(WORK/'outputs/source_inventory.json').write_text(json.dumps(inventory,indent=2))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (WORK/'outputs/progress.log').open('a') as f:
    f.write('2026-11-19T02:29:00Z\tSTART\tSA08 part 1; input prompt read; supplied archives inspected.\n')
    f.write(now+'\tSTAGE 1 START\tArchives extracted; source hashes and line-numbered working copies created. No second-pass files supplied.\n')
print('Prepared:',WORK)
