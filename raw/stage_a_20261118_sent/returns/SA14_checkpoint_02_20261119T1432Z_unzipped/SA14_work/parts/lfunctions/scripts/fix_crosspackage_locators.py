"""Authored supplementary loci requested by the independent structural reviewer."""
from pathlib import Path
import json,subprocess,sys,datetime
R=Path(__file__).resolve().parents[1]
p=R/'scripts/build_claims.py';s=p.read_text()
block='''# Supplementary second-package loci, confirmed by direct rereading.
for c in C:
    extra={408:'379–382',417:'554–568',422:'569–578',425:'593–615'}.get(int(c['id'].split('-')[-1]))
    if extra:
        loc='MPL_60_036-070_transcription.tex:'+extra
        if loc not in c['lines']:c['lines'].append(loc)
'''
if '# Supplementary second-package loci' not in s:
 s=s.replace('def save():\n',block+'def save():\n');p.write_text(s)
print(datetime.datetime.now(datetime.timezone.utc).isoformat())
for script in ['build_claims.py','build_check_events.py','validate.py']:
 q=subprocess.run([sys.executable,str(R/'scripts'/script)],check=True,text=True,capture_output=True)
 print(script);print(q.stdout,end='')
for c in json.loads((R/'claims.json').read_text()):
 if c['id'] in {f'C-SA14-{n}' for n in [408,417,422,425]}:
  print(c['id'],'; '.join(c['lines']))
with (R/'progress.log').open('a') as f:
 f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+' independent-review repair: added actual second-package loci for C408/417/422/425; no mathematical verdict or main assembled register changed.\n')
