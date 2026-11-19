#!/usr/bin/env python3
"""Structural/locator audit only; cannot choose or validate scholarly verdicts."""
import json,csv,re,hashlib,collections
from pathlib import Path
O=Path(__file__).resolve().parents[1];R=O.parents[2]
C=json.loads((O/'claims.json').read_text());I=json.loads((O/'items.json').read_text());P=json.loads((O/'problems.json').read_text())
E=list(csv.DictReader((O/'entries.tsv').open(),delimiter='\t'))
errs=[];warn=[];meta={}
def src(file):
 if file not in meta:
  ls=(R/'sources/texts'/file).read_text().splitlines();s=None;c=None;loc=[]
  for line in ls:
   m=re.search(r'\\cotefile\{(\d+)\}',line)
   if m:c=int(m[1])
   m=re.search(r'\\scanpage\{(\d+)\}',line)
   if m:s=int(m[1])
   loc.append((c,s))
  meta[file]=(ls,loc)
 return meta[file]
for objs,key in [(I,'his_words'),(C,'his_statement')]:
 for x in objs:
  texts=[]
  for l in x['lines']:
   ls,loc=src(l['file']);a,b=l['start'],l['end']
   if not(1<=a<=b<=len(ls)):errs.append((x['id'],'bounds',l));continue
   if not all(v==(l['cote'],l['scan']) for v in loc[a-1:b]):errs.append((x['id'],'scan/cote',l,loc[a-1],loc[b-1]))
   texts.append('\n'.join(ls[a-1:b]))
  q=x[key]
  if q and texts and not any(re.sub(r'\s+',' ',q) in re.sub(r'\s+',' ',t) for t in texts):errs.append((x['id'],'quote',q))
for objs,name in [(I,'items'),(C,'claims'),(P,'problems')]:
 ids=[x['id'] for x in objs]
 if len(ids)!=len(set(ids)):errs.append(('duplicate',name))
items={x['id'] for x in I};claims={x['id'] for x in C}
for e in E:
 if e['item_id'] not in items:errs.append(('baditem',e))
for c in C:
 if not set(c['items'])<=items:errs.append(('badclaimitem',c['id']))
 for d in c['computation']:
  if not (R/'deliverable'/d['code']).exists():errs.append(('badcode',c['id'],d))
  f=R/'deliverable'/d['output']
  if not f.exists() or d['section'] not in json.loads(f.read_text()):errs.append(('badsection',c['id'],d))
for p in P:
 for c in p['claim_ids']:
  if c not in claims:errs.append(('badproblemclaim',p['id'],c))
search=list(csv.DictReader((O/'search_log.tsv').open(),delimiter='\t'))
mapped={c for r in search for c in r['claim_ids'].split(';')}
if claims!=mapped:errs.append(('searchmap',list(claims-mapped),list(mapped-claims)))
refs=set(re.findall(r'^@\w+\{([^,]+),',(O/'references.bib').read_text(),re.M))
for c in C:
 if not set(c['refs'])<=refs:errs.append(('badreference',c['id']))
for p in P:
 if not set(p['refs'])<=refs:errs.append(('badproblemreference',p['id']))
expected={f'MPL_33_147-181+34_002-017#{i}' for i in range(1,114)}
if {e['entry_id'] for e in E}!=expected or len(E)!=113:errs.append(('entrycoverage',len(E)))
for obj in C+I+P:
 if any(ord(ch)<32 and ch not in '\n\r\t' for ch in json.dumps(obj,ensure_ascii=False)):errs.append(('controlchar',obj['id']))
result=dict(entries=len(E),items=len(I),claims=len(C),problems=len(P),readings=sum(1 for _ in csv.DictReader((O/'readings.tsv').open(),delimiter='\t')),references=len(refs),links=sum(1 for _ in csv.DictReader((O/'links.tsv').open(),delimiter='\t')),check_events=sum(1 for _ in csv.DictReader((O/'check_events.tsv').open(),delimiter='\t')),verdicts=dict(collections.Counter(e['verdict'] for e in E)),classes=dict(collections.Counter(c['class'] for c in C)),statuses=dict(collections.Counter(c['status_on_pages'] for c in C)),errors=errs,warnings=warn)
print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(errs))
