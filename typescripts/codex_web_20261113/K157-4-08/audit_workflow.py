from pathlib import Path
from datetime import datetime,timezone
OUT=Path(__file__).resolve().parent
TASK=OUT.parent.name

def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def start(scan):
 p=OUT/'audit_preread';p.mkdir(exist_ok=True)
 (p/f'{scan:03}.md').write_text(f'## Scan {scan}\n\nSecond reading started: {utc()}\n\n',encoding='utf-8')
 print(f'Audit {scan} started {utc()}')

def observations(scan,text):
 p=OUT/'audit_preread'/f'{scan:03}.md'
 with p.open('a',encoding='utf-8') as f:f.write('### Image observations recorded before opening page TeX\n\n'+text.strip()+'\n\nRecorded: '+utc()+'\n')
 print(f'Image observations for {scan} recorded {utc()}')

def finish(scan,text):
 target=OUT/f'{TASK}_audit.md'
 if not target.exists():target.write_text('# Second reading audit\n\nEach section includes observations written from the supplied crops before reopening that page’s TeX. Times are real UTC wall-clock readings. No OCR, text layer or LaTeX compiler was used. Formula checking here is documentary comparison with ink, not mathematical verification.\n\n',encoding='utf-8')
 with target.open('a',encoding='utf-8') as f:
  f.write((OUT/'audit_preread'/f'{scan:03}.md').read_text(encoding='utf-8'))
  f.write('\n### Comparison with page TeX\n\n'+text.strip()+'\n\nSecond reading ended: '+utc()+'\n\n')
 with (OUT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'scan {scan:03} audited {utc()}\n')
 print(f'Audit {scan} completed {utc()}')
