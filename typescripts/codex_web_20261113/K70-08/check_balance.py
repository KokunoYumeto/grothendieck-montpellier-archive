"""Syntax/assembly checks only. Does not invoke TeX or perform text recognition."""
from pathlib import Path
import re,json,csv,collections,hashlib
ROOT=Path(__file__).resolve().parent
SCANS=[111,112,*range(114,126)]
def escaped(s,i):
 j=i-1
 while j>=0 and s[j]=='\\':j-=1
 return (i-j-1)%2==1
def uncomment(s):
 return '\n'.join(line[:next((i for i,c in enumerate(line) if c=='%' and not escaped(line,i)),len(line))] for line in s.splitlines())
def check(path):
 s=uncomment(path.read_text());errors=[];braces=[];math=None;envs=[]
 for i,c in enumerate(s):
  if escaped(s,i):continue
  if c=='{':braces.append(i)
  elif c=='}':
   if not braces:errors.append(f'unmatched closing brace at {i}')
   else:braces.pop()
  elif c=='$':
   if math is None:math='dollar'
   elif math=='dollar':math=None
   else:errors.append(f'dollar inside bracket display at {i}')
  elif c=='\\' and i+1<len(s) and s[i+1] in '[]':
   if s[i+1]=='[':
    if math is not None:errors.append(f'display begins within math at {i}')
    math='display'
   elif math!='display':errors.append(f'unmatched display end at {i}')
   else:math=None
 if braces:errors.append(f'{len(braces)} unmatched opening braces')
 if math:errors.append('unclosed '+math+' math')
 for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
  a,e=m.groups()
  if a=='begin':envs.append(e)
  elif not envs or envs[-1]!=e:errors.append('environment mismatch at '+m.group())
  else:envs.pop()
 if envs:errors.append('unclosed environments: '+','.join(envs))
 for m in re.finditer(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}',s,re.S):
  if '[ampersand replacement=\\&]' not in m.group():errors.append('tikzcd missing ampersand replacement')
  if re.search(r'(?<!\\)&',m.group()):errors.append('bare ampersand inside tikzcd macro')
 return {'file':str(path.relative_to(ROOT)),'passed':not errors,'errors':errors,'brace_pairs':sum(c=='{' and not escaped(s,i) for i,c in enumerate(s)),'display_pairs':s.count(r'\['),'dollar_pairs':sum(c=='$' and not escaped(s,i) for i,c in enumerate(s))//2,'environments':collections.Counter(re.findall(r'\\begin\{([^}]+)\}',s))}
files=[ROOT/'pages'/f'K70-08_70_scan{n}.tex' for n in SCANS]
assembled=ROOT/'K70-08_transcription.tex'
results=[check(p) for p in files+[assembled,ROOT/'K70-08_standalone.tex']]
a=assembled.read_text();expected='\n\n'.join(p.read_text().rstrip() for p in files)+'\n'
checks={'assembled_matches_pages':a==expected,'scan_order':list(map(int,re.findall(r'\\scanpage\{(\d+)\}',a)))==SCANS,'one_cotefile_at_start':a.startswith('\\cotefile{70}\n') and a.count('\\cotefile{70}')==1,'no_image_inclusions':not re.search(r'\\(?:includegraphics|includepdf)\b',a),'no_new_notation_macros':not re.search(r'\\(?:newcommand|def|DeclareMathOperator)\b',a)}
rows=list(csv.DictReader((ROOT/'K70-08_inventory.csv').open()))
checks['inventory_all_yes']=all(r['transcribed']=='yes' for r in rows)
checks['inventory_all_scans']=set(map(lambda r:int(r['scan']),rows))==set(SCANS)
checks['inventory_ids_unique']=len({r['element'] for r in rows})==len(rows)
checks['audit_all_scans']=list(map(int,re.findall(r'^## Scan (\d+)$',(ROOT/'K70-08_audit.md').read_text(),re.M)))==SCANS
for command,kind in [('deleted','deletion'),('inserted','insertion'),('margin','margin note'),('diagram','diagram'),('figure','drawing')]:
 for n,p in zip(SCANS,files):
  need=p.read_text().count('\\'+command+'{');have=sum(r['scan']==str(n) and r['kind']==kind for r in rows)
  checks[f'inventory_{n}_{command}']=have>=need
counts={name:len(re.findall(r'\\'+name+r'\{',a)) for name in ['unsure','illegible','deleted','inserted','margin','diagram','figure','handwritten']}
report={'passed':all(r['passed'] for r in results) and all(checks.values()),'compilation_attempted':False,'pages_checked':len(files),'results':results,'structural_checks':checks,'inventory_rows':len(rows),'counts':counts}
(ROOT/'K70-08_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':report['passed'],'pages_checked':len(files),'counts':counts,'inventory_rows':len(rows),'failed_checks':{k:v for k,v in checks.items() if not v},'syntax_errors':[r for r in results if not r['passed']]},indent=2))
if not report['passed']:raise SystemExit(1)
