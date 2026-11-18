"""Static checks only. No TeX engine is invoked.

Checks lexical braces, display and inline math delimiters, environments,
required scan order, inventory completion and preservation of the preamble.
Ordinary source parentheses/brackets are deliberately not repaired or balanced:
several source fragments leave them open or contain an extra closing mark.
"""
import csv,hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def esc(s,i):
 n=0;i-=1
 while i>=0 and s[i]=='\\':n+=1;i-=1
 return n%2==1

def uncomment(s):
 return '\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in s.splitlines())

def check(path):
 s=uncomment(path.read_text());errors=[];brace=[];env=[];display=[];dollars=[]
 for i,c in enumerate(s):
  if c in '{}' and not esc(s,i):
   if c=='{':brace.append(i)
   elif brace:brace.pop()
   else:errors.append('unmatched closing brace at '+str(i))
  if c=='$' and not esc(s,i):dollars.append(i)
 for m in re.finditer(r'\\([\[\]])|\\(begin|end)\{([^{}]+)\}',s):
  if esc(s,m.start()):continue
  if m.group(1):
   if m.group(1)=='[':display.append(m.start())
   elif display:display.pop()
   else:errors.append('unmatched display close at '+str(m.start()))
  elif m.group(2)=='begin':env.append(m.group(3))
  elif not env or env.pop()!=m.group(3):errors.append('environment mismatch at '+m.group())
 if brace:errors.append('unclosed braces: '+str(len(brace)))
 if display:errors.append('unclosed display math: '+str(len(display)))
 if len(dollars)%2:errors.append('odd dollar count: '+str(len(dollars)))
 if env:errors.append('unclosed environments: '+str(env))
 if re.search(r'\\deleted\{\\margin\{',s):errors.append('marginpar nested in deletion')
 for m in re.finditer(r'\\unsure\{',s):
  d=1;j=m.end()
  while d and j<len(s):
   if s[j] in '{}' and not esc(s,j):d+=1 if s[j]=='{' else -1
   j+=1
  if s[j:].lstrip().startswith('^'):errors.append('external superscript after unsure at '+str(m.start()))
 return {'file':str(path.relative_to(ROOT)), 'status':'PASS' if not errors else 'FAIL','errors':errors,'dollar_pairs':len(dollars)//2,'display_pairs':sum(not esc(s,m.start()) for m in re.finditer(r'\\\[',s)),'environment_pairs':len(re.findall(r'\\begin\{',s))}

def main():
 files=sorted(ROOT.glob('*.tex'))+sorted((ROOT/'pages').glob('*.tex'))
 reports=[check(p) for p in files];errors=[]
 pages=sorted((ROOT/'pages').glob('*.tex'))
 if len(pages)!=15:errors.append('expected15 pages')
 scans=[];counts={x:0 for x in ['unsure','illegible','deleted']}
 for p in pages:
  s=uncomment(p.read_text());scans+=re.findall(r'\\scanpage\{(\d+)\}',s)
  for x in counts:counts[x]+=len(re.findall(r'\\'+x+r'\{',s))
  if p.stem[-3:]!='031' and r'\handwritten{' in s:errors.append('handwritten macro on all-hand page '+p.name)
 if list(map(int,scans))!=list(range(18,33)):errors.append('scan order mismatch')
 assembled=(ROOT/'K45-02_transcription.tex').read_text()
 expected='\n'.join(p.read_text().rstrip() for p in pages)+'\n'
 if assembled!=expected:errors.append('assembled text differs from page concatenation')
 if not assembled.startswith(r'\cotefile{45}'):errors.append('missing initial cotefile')
 if len(re.findall(r'\\cotefile\{',assembled))!=1:errors.append('cotefile count differs from1')
 for p in pages:
  for d in re.findall(r'\\begin\{tikzcd\}(\[[^\]]*\])?',p.read_text()):
   if 'ampersand replacement=\\&' not in d:errors.append('tikzcd without ampersand replacement in '+p.name)
 inventory=list(csv.DictReader((ROOT/'K45-02_inventory.csv').open()))
 cols=['cote','scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
 if list(inventory[0])!=cols:errors.append('inventory columns differ')
 if any(r['transcribed']!='yes' for r in inventory):errors.append('unfinished inventory row')
 if set(int(r['scan']) for r in inventory)!=set(range(18,33)):errors.append('inventory scan coverage differs')
 uploaded=ROOT.parent/'upload/PREAMBLE(20261117-204034).tex'
 preamble_hash=hashlib.sha256((ROOT/'PREAMBLE.tex').read_bytes()).hexdigest()
 preamble_unchanged=None
 if uploaded.exists():
  preamble_unchanged=(ROOT/'PREAMBLE.tex').read_bytes()==uploaded.read_bytes()
  if not preamble_unchanged:errors.append('preamble changed')
 result={'balance':'PASS' if all(r['status']=='PASS' for r in reports) else 'FAIL','package_checks':'PASS' if not errors else 'FAIL','files':reports,'package_errors':errors,'pages':len(pages),'scans':scans,'counts_page_files_only':counts,'inventory_rows':len(inventory),'preamble_sha256':preamble_hash,'preamble_unchanged':preamble_unchanged,'compiled':False,'unfinished_pages':[]}
 (ROOT/'K45-02_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(result,ensure_ascii=False,indent=2))
 return 0 if result['balance']==result['package_checks']=='PASS' else 1
if __name__=='__main__':sys.exit(main())
