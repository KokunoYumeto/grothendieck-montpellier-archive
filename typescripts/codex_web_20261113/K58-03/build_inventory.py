#!/usr/bin/env python3
"""Inventory each text block, display, diagram and nested pen intervention."""
import csv,re,bisect
from pathlib import Path
from tex_elements import arguments
root=Path(__file__).resolve().parent
kinds={'margin':'margin note','inserted':'insertion','deleted':'deletion','handwritten':'handwritten','diagram':'diagram','figure':'drawing'}
first=root/'audit/first_inventory.csv'
target=root/'K58-03_inventory.csv'
if not first.exists(): first.write_bytes(target.read_bytes())
prior=list(csv.DictReader(first.open()))
scans=sorted({int(r['scan']) for r in prior})
def compact(s):
 return re.sub(r'\s+',' ',s).strip()
def blank_comments(raw):
 return re.sub(r'(?m)(?<!\\)%[^\n]*',lambda m:' '*len(m[0]),raw)
def phrase(t):
 return compact(t)[:170]
def wording(m):
 s=re.sub(r'\\(?:unsure|inserted|deleted|uline|uuline|handwritten|text|mathrm|mathcal|mathscr)\{', '',m.lower())
 return re.sub(r'[^a-zà-ÿ0-9]+',' ',s).strip()
def labels(n,kind,content):
 candidates=[r for r in prior if r['scan']==str(n) and r['kind']==kind and 'character' not in r['position'] and not r['position'].startswith('body block')]
 w=wording(content)
 for r in candidates:
  v=wording(r['first_words_or_objects'])
  if len(v)>3 and (w.startswith(v) or v.startswith(w) or (len(v)>8 and v in w)):return r['position']
 return ''
rows=[]
for n in scans:
 raw=blank_comments((root/'pages'/f'K58-03_58_scan{n:03}.tex').read_text())
 sheet=next(r['sheet_kind'] for r in prior if r['scan']==str(n))
 main='typed' if sheet=='reused_typed' else 'Grothendieck'
 events=[]
 def event(offset,order,kind,label,loc,hand=None):
  events.append((offset,order,kind,phrase(label),loc,hand or main))
 for a,b,_,value in arguments(raw,{'mspage'}):event(a,-3,'text',value,'head, centre')
 for m in re.finditer(r'\\\[(.*?)\\\]',raw,re.S):event(m.start(),-2,'display',m[1],f'displayed formula, source line {raw.count(chr(10),0,m.start())+1}')
 blocks=list(re.finditer(r'(?s)(?:^|\n[ \t]*\n)(.*?)(?=\n[ \t]*\n|\Z)',raw))
 starts=[m.start(1) for m in blocks]
 for j,m in enumerate(blocks,1):
  seg=m[1]
  s=re.sub(r'\\(?:cotefile|scanpage|mspage)\{[^{}]*\}', '',seg)
  s=re.sub(r'\\(?:begin|end)\{samepage\}', '',s)
  if not s.strip() or s.lstrip().startswith((r'\[',r'\diagram',r'\figure')):continue
  # A stand-alone marginal note already has an element of its own.
  other=s
  for a,b,_,_ in reversed(list(arguments(s,{'margin'}))):other=other[:a]+other[b:]
  if not other.strip():continue
  desc=re.sub(r'\\tikz\[remember picture,overlay\]\{[^{}]*\}', '',other).strip()
  if not desc:continue
  if n==32 and 'lgstart' in desc:desc='1. Généralisation des th. de finitude formelle'
  if n==32 and 'lgeight.base' in desc:desc='8. Théorèmes de pureté'
  if n==33 and 'lgcaption.base' in desc:desc="“Pseudolim” de catégories"
  event(m.start(1),0,'text',desc,f'block {j}, source line {raw.count(chr(10),0,m.start(1))+1}')
 for a,b,name,content in arguments(raw,set(kinds)):
  j=bisect.bisect_right(starts,a)
  kind=kinds[name]; line=raw.count('\n',0,a)+1
  around=compact(raw[max(0,a-27):a]).split(' ')
  previous=' '.join(around[-4:])
  loc=labels(n,kind,content) or f'block {j}, source line {line}, after {previous or "start"}'
  hand='unknown' if name=='handwritten' else main
  if name=='diagram':loc='centre, two rows of five objects'; content='H^i(L), H^i(G), H^{i+1}(F), H^{i+1}(L), H^{i+1}(G)'
  if name=='margin' and n==32:loc='left, slanted boxed reference, pointing to items 6 and 8';content='utilise IV, section sur les morphismes étales'
  event(a,1,kind,content,loc,hand)
 rules={21:[('lgma','Vertical rule beside Lemme 4')],23:[('lgta','Vertical rule alongside the statement'),('lgtc','Second rule beside the dominance hypothesis')],25:[('lgfa','Vertical rule beside Lemme 5')],33:[('lgda','Vertical rule beside the first two definitions')]}
 for key,title in rules.get(n,[]):
  event(raw.index(key),3,'drawing',title,'left of the corresponding manuscript lines')
 if n==32:
  for key,title in [('lgstart.base','Left grouping bracket with lower division'),('lgpi.base','Oval around pi with subscript 1'),('lgeight.base','Oval around 8.'),('lgnote.east','Arrow to the circled pi-one'),('lgnote.south east','Arrow to the circled 8')]:
   p=raw.index(key);event(p,3,'drawing',title,'outline; see marked targets and labelled margin')
 if n==33:
  event(raw.index('lgcaption.north east'),3,'drawing','Two-ended diagonal leader between the caption and Lim','lower half, beside last display')
 for i,(_,_,kind,content,loc,hand) in enumerate(sorted(events),1):rows.append((58,n,sheet,hand,i,kind,loc,content,'yes'))
with target.open('w',newline='') as f:
 w=csv.writer(f);w.writerow('cote,scan,sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed'.split(','));w.writerows(rows)
print(len(rows),'elements in',len(scans),'scans')
