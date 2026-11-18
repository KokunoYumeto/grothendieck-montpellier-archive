#!/usr/bin/env python3
"""Static checks only. Does not invoke or compile LaTeX."""
from pathlib import Path
import re,json,sys
ROOT=Path(__file__).resolve().parent
def escaped(s,i):
 k=i-1;n=0
 while k>=0 and s[k]=='\\':n+=1;k-=1
 return n%2==1
def uncomment(t):
 return '\n'.join(line[:next((i for i,c in enumerate(line) if c=='%' and not escaped(line,i)),len(line))] for line in t.splitlines())
def check(path):
 s=uncomment(path.read_text());errors=[];depth=0
 for i,c in enumerate(s):
  if c in '{}' and not escaped(s,i):
   depth+=1 if c=='{' else -1
   if depth<0:errors.append('closing brace before opening');break
 if depth:errors.append(f'brace balance {depth}')
 ds=[]
 for m in re.finditer(r'\\\[|\\\]',s):
  if m.group()=='\\[':ds.append(m.start())
  elif not ds:errors.append('display closes without opening')
  else:ds.pop()
 if ds:errors.append('unclosed display')
 dollars=sum(c=='$' and not escaped(s,i) for i,c in enumerate(s))
 if dollars%2:errors.append(f'odd dollar count {dollars}')
 env=[]
 for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',s):
  typ,name=m.groups()
  if typ=='begin':env.append(name)
  elif not env or env[-1]!=name:errors.append('environment mismatch '+name)
  else:env.pop()
 if env:errors.append('unclosed environments '+str(env))
 if len(re.findall(r'\\left\b',s))!=len(re.findall(r'\\right\b',s)):errors.append('left/right count mismatch')
 for m in re.finditer(r'\\begin\{tikzcd\}(\[[^\]]*\])?',s):
  if not m.group(1) or r'ampersand replacement=\&' not in m.group(1):errors.append('tikzcd missing ampersand replacement')
 return {'file':str(path.relative_to(ROOT)),'brace_display_dollar_environment_balance':'PASS' if not errors else 'FAIL','dollar_delimiters':dollars,'errors':errors}
paths=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'K70-04_transcription.tex',ROOT/'K70-04_standalone.tex']
results=[check(p) for p in paths]
report={'compiled':False,'files_checked':len(results),'all_passed':all(not r['errors'] for r in results),'results':results}
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(0 if report['all_passed'] else 1)
