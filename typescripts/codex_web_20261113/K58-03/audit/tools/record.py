import json,sys,csv,datetime,re
from pathlib import Path
out=Path('out'); meta=json.load(sys.stdin)
n=meta['n']; code=f'{n:03d}'
tex=out/'pages'/f'K58-03_58_scan{code}.tex'
text=tex.read_text()
rows=[]
def add(kind,position,label,hand=None):
 rows.append((58,n,meta.get('kind','reused_typed'),hand or ('Grothendieck' if meta.get('kind') in ('text','cover','cancelled_draft') else 'typed'),len(rows)+1,kind,position,label,'yes'))
def record(key,header,line):
 p=out/key
 with p.open('a') as f:
  if p.stat().st_size==0:f.write(header+'\n')
  if line:f.write(line.strip()+'\n')
mp=re.search(r'\\mspage\{(.*?)\}',text)
if mp:add('text','head, centre',mp[1])
head=re.search(r'\\hfill (.+)',text)
if head:add('text','head, right',head[1])
blocks=text.split('\n\n')[1:]
for j,block in enumerate(blocks,1):
 display=block.strip().startswith(r'\[')
 if block.strip().startswith('%') or not block.strip(): continue
 label=re.sub(r'\\(uline|handwritten|unsure|deleted|inserted)\{', '',block.strip())
 label=label.replace('$','').replace('}','').replace('{','')
 add('display' if display else 'text',f'body block {j}',label[:72].split('\n')[0])
 for obj in meta.get('extras',[]):
  if obj[0]==j:add(*obj[1:])
 for m in re.finditer(r'\\handwritten\{((?:[^{}]|\{[^{}]*\})*)\}',block):
  if not any(obj[0]==j and obj[1]=='handwritten' and len(list(re.finditer(r'\\handwritten\{',block)))==1 for obj in meta.get('extras',[])):
   add('handwritten',f'block {j}, character {m.start()+1}',m[1],'unknown')
for obj in meta.get('extras',[]):
 if obj[0]==0:add(*obj[1:])
inv=out/'K58-03_inventory.csv'
with inv.open('a',newline='') as f:
 writer=csv.writer(f)
 if inv.stat().st_size==0:writer.writerow('cote,scan,sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed'.split(','))
 writer.writerows(rows)
record('K58-03_hand_log.md','# Hand and type log\n\nThe body is predominantly typescript. The attributions below distinguish individually inked characters from the typewriter impressions. Fine corner numerals belong to the archive.\n','\n## Scan '+str(n)+'\n\n'+meta['hand']+'\n')
record('K58-03_doubts.md','# Readings and apparatus\n\n## Notation table\n\n| Scan and place | Form visible | LaTeX reading and comparative evidence |\n|---|---|---|',meta['notation'])
with (out/'progress.log').open('a') as f:print('scan',code,'done',datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),file=f)
print(code, len(rows),'inventory entries')
