"""Static checks only. No TeX engine, OCR, or source-image processing."""
from pathlib import Path
import re,json,hashlib
ROOT=Path(__file__).resolve().parent
SCANS=[67,68,69,70,71,72,74,75,76,77,78,79,80,81,82]

def clean(s):
 return re.sub(r'(?<!\\)%[^\n]*','',s)

def check(s):
 s=clean(s); errors=[];depth=0; dollars=0; display=0;paren=0;i=0
 while i<len(s):
  c=s[i]
  if c=='\\':
   if i+1<len(s) and s[i+1] in '{}%$\\':i+=2;continue
   if i+1<len(s) and s[i+1] in '[]()':
    q=s[i+1]
    if q=='[':display+=1
    if q==']':display-=1
    if q=='(':paren+=1
    if q==')':paren-=1
    if display<0 or paren<0:errors.append('closing math delimiter without opening')
    i+=2;continue
  if c=='{':depth+=1
  elif c=='}':
   depth-=1
   if depth<0:errors.append('closing brace without opening')
  elif c=='$':dollars+=1
  i+=1
 if depth:errors.append(f'brace balance {depth}')
 if display:errors.append(f'display delimiter balance {display}')
 if paren:errors.append(f'parenthesized math delimiter balance {paren}')
 if dollars%2:errors.append(f'odd dollar delimiter count {dollars}')
 stack=[]
 for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
  action,name=m.groups()
  if action=='begin':stack.append(name)
  elif not stack or stack.pop()!=name:errors.append('environment order mismatch: '+name)
 if stack:errors.append('unclosed environments: '+','.join(stack))
 for m in re.finditer(r'\\begin\{tikzcd\}(\[[^\]]*\])?',s):
  if 'ampersand replacement=\\&' not in m.group(0):errors.append('tikzcd lacks ampersand replacement')
 if re.search(r'\\(?:newcommand|renewcommand|def|includegraphics)\b',s):errors.append('custom macro or embedded image')
 if any(ord(c)<32 and c not in '\n\r\t' for c in s):errors.append('unexpected control character')
 return {'ok':not errors,'errors':errors,'braces':depth,'display_delimiters':display,'parenthesized_math_delimiters':paren,'dollar_delimiters':dollars,'environments_closed':not stack}

if __name__=='__main__':
 results={};texts=[]
 for n in SCANS:
  p=ROOT/'pages'/f'K70-05_70_scan{n:03d}.tex';s=p.read_text();texts.append(s);results[p.name]=check(s)
  if s.count(f'\\scanpage{{{n}}}')!=1:results[p.name]['errors'].append('scan marker mismatch');results[p.name]['ok']=False
 assembled=(ROOT/'K70-05_transcription.tex').read_text()
 results['K70-05_transcription.tex']=check(assembled)
 exact=assembled=='\n'.join(texts)
 counts={k:sum(s.count('\\'+k+'{') for s in texts) for k in ['unsure','illegible','deleted','inserted','margin','diagram','figure','handwritten']}
 report={'pages':SCANS,'results':results,'assembled_exact_concatenation':exact,'cotefile_once_at_start':assembled.startswith('\\cotefile{70}') and assembled.count('\\cotefile{70}')==1,'mark_counts':counts,'compiled':False}
 report['all_ok']=all(v['ok'] for v in results.values()) and exact and report['cotefile_once_at_start']
 (ROOT/'K70-05_balance_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(report,ensure_ascii=False,indent=2))
 raise SystemExit(0 if report['all_ok'] else 1)
