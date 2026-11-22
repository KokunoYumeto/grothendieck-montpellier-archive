from pathlib import Path
import csv,json,re,sys,datetime,importlib.util
n=int(sys.argv[1]);code=f'{n:03}';out=Path('out');meta=json.load(sys.stdin)
page=out/'pages'/f'K58-03_58_scan{code}.tex'
raw=page.read_text();changes=meta.get('changes',[])
for old,new in changes:
 if old not in raw:raise ValueError('missing change: '+old)
 raw=raw.replace(old,new)
page.write_text(raw)
dest=out/'audit/anchors.tsv'
init=not dest.exists()
with dest.open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 if init:w.writerow(['scan','place','first excerpt','decision on ink'])
 for loc,old,decision in meta.get('anchors',[]):w.writerow([n,loc,old,decision])
blind=list(csv.DictReader((out/'K58-03_blind.tsv').open(),delimiter='\t'))
words=list(csv.DictReader((out/'audit/blind_words.tsv').open(),delimiter='\t'))[-1]
def utc():return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
stamp=utc();start=Path(f'work/audit_{code}_start').read_text().strip()
def exact_macro(text,name):
 data=[];pat=re.compile(r'\\'+name+r'\{')
 for m in pat.finditer(text):
  j=m.end();depth=1
  while j<len(text) and depth:
   if j==0 or text[j-1]!='\\':
    depth+=int(text[j]=='{')-int(text[j]=='}')
   j+=1
  data.append(text[m.end():j-1].replace('\n',' '))
 return data
plain=re.sub(r'(?m)^(?:%.*|\\(?:cotefile|scanpage|mspage)\{[^\n]+)\n?', '',raw)
formulas=[]
for m in re.finditer(r'\\\[(.*?)\\\]|\$(.*?)\$|\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}',plain,re.S):
 formulas.append(' '.join(x.strip() for x in m.groups() if x is not None).replace('\n',' '))
def mono(t):return chr(96)+t+chr(96)
p=out/'K58-03_audit.md'
if not p.exists():p.write_text('# Second reading from the scans\n\nThe independent words and hard-place readings were written before opening each first-pass file. The passages below are the results of reading the thirds and checking the local crops. The mathematical register lists occurrences in order, including repeats. The blind comparison retains the original page sources separately.\n')
with p.open('a') as f:
 print('\n## Scan',n,'\n',file=f)
 print(f'{start} to {stamp} UTC.\n',file=f)
 print('**Independent words and accents.** '+words['words and accents before opening the page']+'\n',file=f)
 print('**Local checks.** '+meta['notes']+'\n',file=f)
 f.write('**Formulas.** '+(' · '.join(mono(z) for z in formulas) if formulas else 'None.')+'\n\n')
 fi=[z for z in formulas if re.search(r'(?:\^|_)(?:\{[^}]*[ij]|[ij])',z) or r'\in' in z and re.search('_[ij]',z)]
 f.write('**Indexed or raised i and j.** '+(' · '.join(mono(z) for z in fi) if fi else 'None.')+'\n\n')
 for macro,head in [('handwritten','Ink on type'),('margin','Marginal wording'),('inserted','Insertions'),('deleted','Cancellations')]:
  arr=exact_macro(raw,macro)
  f.write('**'+head+'.** '+(' · '.join(mono(z) for z in arr) if arr else 'None.')+'\n\n')
 f.write('**Changes.** '+(' · '.join(mono(old)+' → '+mono(new) for old,new in changes) if changes else 'No change.')+'\n')
with (out/'progress.log').open('a') as f:print('scan',code,'audited',stamp,file=f)
print(code,'audited',start,stamp)
