"""Lexical balance and command checks only; never invokes a TeX compiler."""
from pathlib import Path
import re,hashlib,csv,json
OUT=Path(__file__).resolve().parent
TASK=OUT.parent.name
# Explicit source: standard LaTeX/amsmath/amssymb, mathrsfs, TikZ/tikz-cd,
# ulem, and the supplied state macros. No command is added from an error list.
STANDARD=set('Biggl Biggr Bigl Bigr Delta Omega Phi Psi Sigma Upsilon Vert alpha amalg backslash bar begin cdots circ downarrow end hfill in kappa ldots left lim longleftrightarrow longmapsto longrightarrow mapsto mathbb mathbin mathcal mathrm mathscr operatorname overline overset pm qquad quad rho right sigma simeq subset tag text textsuperscript times to underline underset varphi vert widehat widetilde xi xrightarrow'.split())
# Individually reviewed standard commands used in this task. In particular,
# the regex substrings "de"/"non" after \\ are text, not control words.
STANDARD.update('Leftarrow Longrightarrow Pi aleph beta bigl bigr cdot coprod equiv forall ge geq hookrightarrow hspace le leftarrow leftrightarrow leq mathfrak mathrel mid ne nu phi pi prime shortstack sim substack textcircled underbrace varinjlim varprojlim wr'.split())
PACKAGE=set('arrow draw node uline uuline'.split())
STATE=set('cotefile scanpage mspage handwritten deleted inserted margin unsure illegible diagram figure'.split())
ALLOWED=STANDARD|PACKAGE|STATE
ENV={'aligned','gathered','matrix','tikzcd','tikzpicture','array'}
TOKEN=re.compile(r'\\(?:[A-Za-z]+|.)|%[^\n]*|[{}$]',re.S)

def check(p):
 s=p.read_text();stack=[];dollar=False;display=False;env=[];errors=[];commands=set()
 for m in TOKEN.finditer(s):
  t=m.group();line=s.count('\n',0,m.start())+1
  if t.startswith('%'):continue
  if t=='{':stack.append(line)
  elif t=='}':
   if stack:stack.pop()
   else:errors.append(f'line {line}: extra closing brace')
  elif t=='$':dollar=not dollar
  elif t=='\\[':
   if display:errors.append(f'line {line}: nested display opener')
   display=True
  elif t=='\\]':
   if not display:errors.append(f'line {line}: unmatched display closer')
   display=False
  elif len(t)>1 and t[1].isalpha():
   name=t[1:];commands.add(name)
   if name not in ALLOWED:errors.append(f'line {line}: unknown command {name}')
   if name in ('begin','end'):
    z=re.match(r'\{([^{}]+)\}',s[m.end():])
    if not z:errors.append(f'line {line}: environment argument missing');continue
    e=z.group(1)
    if e not in ENV:errors.append(f'line {line}: unexpected environment {e}')
    if name=='begin':env.append((e,line))
    elif not env or env[-1][0]!=e:errors.append(f'line {line}: mismatched end {e}')
    else:env.pop()
 if stack:errors.append(f'unclosed braces at lines {stack}')
 if dollar:errors.append('unpaired dollar delimiter')
 if display:errors.append('unclosed display delimiter')
 if env:errors.append(f'unclosed environments {env}')
 return {'file':p.name,'result':'PASS' if not errors else 'FAIL','errors':errors,'commands':sorted(commands)}

if __name__=='__main__':
 pages=sorted((OUT/'pages').glob('*.tex'))
 results=[check(p) for p in pages]
 inv=list(csv.DictReader((OUT/f'{TASK}_inventory.csv').open()))
 s='\n'.join(p.read_text() for p in pages)
 extra={'page_count':len(pages),'scan_tags':re.findall(r'\\scanpage\{(\d+)\}',s),'cotefile_count':s.count('\\cotefile{157-4}'),'inventory_rows':len(inv),'inventory_all_yes':all(r['transcribed']=='yes' for r in inv),'inventory_ids_unique':len({r['element'] for r in inv})==len(inv),'marks':{n:len(re.findall(r'\\'+n+r'\{',s)) for n in ('unsure','illegible','deleted')}}
 good=all(x['result']=='PASS' for x in results) and extra['inventory_all_yes'] and extra['inventory_ids_unique'] and extra['cotefile_count']==1
 report={'scope':'Lexical checks; no compilation or mathematical validation','overall':'PASS' if good else 'FAIL','pages':results,'summary':extra}
 (OUT/'syntax_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(report['overall']);print(json.dumps(extra,ensure_ascii=False))
 for r in results:
  print(r['file'],r['result'], '; '.join(r['errors']))
 raise SystemExit(0 if good else 1)
