#!/usr/bin/env python3
"""Structural checks only. Does not invoke TeX or claim compilation success."""
from pathlib import Path
import re,json,sys,csv
ROOT=Path(__file__).resolve().parent
SCANS=[39,40,41,42,43,44,45,66,67,68]
def uncomment(src):
 out=[]
 for line in src.splitlines(keepends=True):
  for i,ch in enumerate(line):
   if ch=='%':
    n=0;j=i-1
    while j>=0 and line[j]=='\\':n+=1;j-=1
    if n%2==0:line=line[:i]+'\n';break
  out.append(line)
 return ''.join(out)
def check(p):
 s=uncomment(p.read_text());braces=[];env=[];mode=None;errors=[];i=0
 def loc(at):return s.count('\n',0,at)+1
 while i<len(s):
  c=s[i]
  if c=='\\':
   if s.startswith('\\[',i):
    if mode is not None:errors.append(f'line {loc(i)}: display opens inside {mode}')
    mode='display';i+=2;continue
   if s.startswith('\\]',i):
    if mode!='display':errors.append(f'line {loc(i)}: unmatched display close')
    mode=None;i+=2;continue
   m=re.match(r'\\(begin|end)\{([^{}]+)\}',s[i:])
   if m:
    action,name=m.groups()
    if action=='begin':env.append((name,loc(i)))
    elif not env or env[-1][0]!=name:errors.append(f'line {loc(i)}: mismatched end {name}, stack {env}')
    else:env.pop()
    i+=len(m.group());continue
   m=re.match(r'\\[A-Za-z]+|\\.',s[i:],re.S)
   i+=len(m.group()) if m else 1;continue
  if c=='{':braces.append(loc(i))
  elif c=='}':
   if not braces:errors.append(f'line {loc(i)}: extra closing brace')
   else:braces.pop()
  elif c=='$':
   if mode is None:mode='inline'
   elif mode=='inline':mode=None
   else:errors.append(f'line {loc(i)}: dollar within display')
  i+=1
 if braces:errors.append(f'unclosed braces at lines {braces}')
 if env:errors.append(f'unclosed environments {env}')
 if mode:errors.append(f'unclosed math mode {mode}')
 for m in re.finditer(r'\\begin\{tikzcd\}(\[[^\]]*\])?',s):
  if not m.group(1) or r'ampersand replacement=\&' not in m.group(1):errors.append('tikzcd lacks ampersand replacement')
 return {'file':str(p.relative_to(ROOT)),'status':'PASS' if not errors else 'FAIL','errors':errors}
files=[ROOT/'pages'/f'B37-03_37_scan{n:03}.tex' for n in SCANS]+[ROOT/'B37-03_transcription.tex',ROOT/'B37-03_standalone.tex',ROOT/'PREAMBLE.tex']
results=[check(p) for p in files]
s=(ROOT/'B37-03_transcription.tex').read_text();clean=uncomment(s)
extra=[]
if s!=''.join((ROOT/'pages'/f'B37-03_37_scan{n:03}.tex').read_text() for n in SCANS):extra.append('assembled fragment differs from direct page concatenation')
if not s.startswith('\\cotefile{37}\n\\scanpage{39}'):extra.append('fragment start incorrect')
if re.findall(r'\\scanpage\{(\d+)\}',clean)!=[str(n) for n in SCANS]:extra.append('scan order or page markers incorrect')
if clean.count('\\cotefile{37}')!=1:extra.append('cotefile count incorrect')
if re.search(r'\\(?:newcommand|renewcommand|def|documentclass)\b',clean):extra.append('custom macro or documentclass in fragment')
rows=list(csv.DictReader((ROOT/'B37-03_inventory.csv').open()))
if any(r['transcribed']!='yes' for r in rows):extra.append('inventory contains an incomplete element')
if set(int(r['scan']) for r in rows)!=set(SCANS):extra.append('inventory page coverage incorrect')
counts={k:len(re.findall(r'\\'+k+r'\{',clean)) for k in ['unsure','illegible','deleted']}
report={'scope':'Textual balance only; no compilation or rendering performed.','checks':'Unescaped braces; display delimiters; inline dollar delimiters; nested environments; tikzcd separator option; direct concatenation; page order; macro policy; inventory completion.','files':results,'package_errors':extra,'counts_in_assembled_fragment':counts,'inventory_rows':len(rows),'status':'PASS' if not extra and all(r['status']=='PASS' for r in results) else 'FAIL'}
(ROOT/'B37-03_balance_report.json').write_text(json.dumps(report,indent=2)+'\n')
summary=['# B37-03 structural check','',report['scope'],'',report['checks'],'','| File | Result |','| --- | --- |']+[f'| {r["file"]} | {r["status"]} |' for r in results]+['',f'Package result: **{report["status"]}**.',f'Marks in the assembled fragment: unsure={counts["unsure"]}; illegible={counts["illegible"]}; deleted={counts["deleted"]}.',f'Inventory: {len(rows)} elements, all transcribed=yes.' if not any(r['transcribed']!='yes' for r in rows) else 'Inventory: incomplete.']
for r in results:
 for err in r['errors']:summary.append(r['file']+': '+err)
summary.extend(extra);(ROOT/'B37-03_balance_report.md').write_text('\n'.join(summary)+'\n')
print(json.dumps({'status':report['status'],'counts':counts,'inventory_rows':len(rows),'file_failures':[r for r in results if r['errors']],'package_errors':extra},indent=2))
sys.exit(0 if report['status']=='PASS' else 1)
