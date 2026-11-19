"""Record file intervals actually exposed and read by cote11b.
This is a human-authored coverage ledger, not a machine claim of comprehension.
"""
from pathlib import Path
import csv,hashlib
base=Path('SA05/work/cote11b')
paths=[
 ('SA05/WORK_PROTOCOL.md','full protocol read twice'),
 ('upload/PROMPT(4).md','full governing prompt read twice'),
 ('sources/notes/pro/MPL_11_043-058+56_notes.md','all107 entries; exposures1-260,260-570,570-840,840-1050; tail970-1030 reread to repair truncated combined output'),
 ('sources/notes/pro/MPL_11_043-058+56_doubts.md','full doubts table read; final complete untruncated re-exposure'),
 ('sources/texts/pro/MPL_11_043-058+56_transcription.tex','entire1958lines read in overlapping intervals1-430,370-790,790-1170,1170-1545,1545-1965; selected claims re-read subsequently'),
 ('sources/notes/codex/K11-03_notes.md','full notes read'),
 ('sources/texts/codex/K11-03_transcription.tex','entire513lines read'),
 ('sources/notes/codex/K11-04_notes.md','full notes read'),
 ('sources/texts/codex/K11-04_transcription.tex','entire644lines read'),
 ('sources/notes/codex/B12-02_notes.md','full notes read after additional delegation'),
 ('sources/texts/codex/B12-02_transcription.tex','entire202lines read; all11scans including reused reflection sheets'),
]
rows=[]
for path,note in paths:
 p=Path(path);data=p.read_bytes()
 rows.append(dict(date='2026-11-19',reader='GPT-6 Astra Pro; SA05/cote11b',file=path,lines=f'1-{len(data.splitlines())}',method='actual prose/passage reading via tool exposure',note=note,sha256=hashlib.sha256(data).hexdigest()))
p=Path('sources/texts/pro/MPL_11_002-042_transcription.tex')
rows.append(dict(date='2026-11-19',reader='GPT-6 Astra Pro; SA05/cote11b',file=str(p),lines='1280-1309',method='actual prose/passage reading via tool exposure',note='Cross-package endpoint: scan42 Poincaré/Künneth example and preceding special-system paragraph; both endpoint and its continuation on44 read. This row does not claim full reading of the earlier Pro package.',sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
with (base/'reading_log.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print('Saved',len(rows),'reading records:11 full-file records and1 partial cross-package endpoint. Only actual read material listed.')
