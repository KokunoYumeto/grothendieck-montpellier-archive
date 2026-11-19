#!/usr/bin/env python3
"""Reproduce the initial archive inventory and normalized prompt comparison."""
from pathlib import Path
import csv, collections, difflib, hashlib, json, zipfile
base=Path(__file__).resolve().parents[2]
for p in sorted((base/'upload').glob('*.zip')):
    with zipfile.ZipFile(p) as z:
        print(json.dumps({'archive':p.name,'entries':[{'name':i.filename,'size':i.file_size} for i in z.infolist()]},ensure_ascii=False))
print((base/'sources/texts/TOPIC.md').read_text())
rows=list(csv.DictReader((base/'sources/notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
print('ROWS',len(rows),'PACKAGES',dict(collections.Counter(x['package'] for x in rows)))
print('\n'.join(difflib.unified_diff((base/'upload/PROMPT(3).md').read_text().splitlines(),(base/'sources/prompt/PROMPT.md').read_text().splitlines(),fromfile='attached prompt',tofile='zipped prompt')))
