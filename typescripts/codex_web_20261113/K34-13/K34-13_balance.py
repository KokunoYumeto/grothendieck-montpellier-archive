"""Check the delivered fragment structurally without running a TeX engine."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CUSTOM = set('cotefile scanpage mspage handwritten deleted inserted margin diagram figure unsure illegible uline uuline'.split())
STANDARD = set('Theta alpha arrow bar begin bigl bigr boxed cap cdot circ dim ell end eta geq hookrightarrow in lambda ldots left leq longrightarrow mathbb mathfrak mathrel mathrm mid mu ne nu operatorname otimes overline overset phantom pi prod qquad quad right shortparallel sim simeq sqrt subset substack tag text theta to underline underset varepsilon varinjlim varprojlim wedge widehat widetilde xleftarrow xrightarrow zeta'.split())
ENV = {'aligned','tikzcd','array','tikzpicture'}
def verify(p):
 text=re.sub(r'(?m)(?<!\\)%.*$', '', p.read_text())
 stack=[]; errors=[]
 for m in re.finditer(r'\\(?:begin|end)\{[A-Za-z*]+\}|\\[A-Za-z]+|\\[^\n]|\$\$|\$|[{}]',text):
  t=m[0]
  if t.startswith(('\\begin{','\\end{')):
   name=t[t.index('{')+1:-1]
   if name not in ENV:errors.append('unknown environment '+name)
   if t.startswith('\\begin'):stack.append(('env',name))
   elif not stack or stack.pop()!=('env',name):errors.append('mismatched '+t)
  elif t in (r'\(',r'\[','{'):stack.append(t)
  elif t in (r'\)',r'\]','}'):
   if not stack or stack.pop()!={r'\)':r'\(',r'\]':r'\[','}':'{'}[t]:errors.append('mismatched '+t)
  elif t in ('$','$$'):
   if stack and stack[-1]==t:stack.pop()
   else:stack.append(t)
  elif t.startswith('\\') and t[1:].isalpha() and t[1:] not in CUSTOM|STANDARD:errors.append('undefined control word '+t)
 if stack:errors.append('unclosed '+repr(stack))
 if errors:raise ValueError(f'{p.name}: '+', '.join(errors))
def run():
 files=sorted((ROOT/'pages').glob('*.tex'));assert len(files)==15
 for n,p in enumerate(files,3):
  s=p.read_text();assert s.count(r'\scanpage{')==1 and r'\scanpage{'+str(n)+'}' in s
  assert s.count(r'\cotefile{')==(n==3);verify(p)
 assembled=ROOT/'K34-13_transcription.tex';verify(assembled)
 assert assembled.read_text()=='\n'.join(p.read_text() for p in files)
 assert (ROOT/'K34-13_standalone.tex').read_text()=="\\input{PREAMBLE.tex}\n\\begin{document}\n\\input{K34-13_transcription}\n\\end{document}\n"
 print('15 page files and assembled fragment passed: braces, inline and display math, dollar signs, environments, control words, scan order, assembly and wrapper.')
if __name__=='__main__':run()
