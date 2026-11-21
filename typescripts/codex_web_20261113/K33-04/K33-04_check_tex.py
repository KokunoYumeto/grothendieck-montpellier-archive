"""Static fragment checks. No TeX engine is started."""
from pathlib import Path
import re,sys
root=Path(__file__).resolve().parent
allowed=set("""
cotefile scanpage mspage handwritten deleted inserted margin uline uuline diagram figure unsure illegible
begin end textcircled rule noindent linewidth tag left right big bigg Big Bigg bigl bigr Bigl Bigr biggl biggr
mathbb mathscr mathcal mathfrak mathrm mathit operatorname mathbin mathrel text textrm textnormal
boxed aligned substack underbrace overbrace underset overset overline underline bar hat tilde widetilde
simeq sim approx cong equiv neq ne leq geq ge le ll gg in notin ni subset subseteq supset supseteq
to mapsto longmapsto longrightarrow longleftarrow rightarrow leftarrow xrightarrow xleftarrow Longleftrightarrow
leftrightarrow Rightarrow implies iff cap cup otimes oplus bigotimes times cdot bullet circ bigcirc
ldots dots cdots ldotp prime ast star colon mid vert Vert lVert rVert langle rangle partial infty
sum prod int Gamma Delta Phi Psi Sigma dim ker lim max min gcd binom frac dfrac tfrac
alpha beta gamma delta epsilon varepsilon zeta eta theta iota kappa lambda mu nu xi rho sigma tau phi varphi chi psi omega
quad qquad hspace hfill hfil cr ooalign scriptscriptstyle scriptstyle displaystyle textstyle
longmapsto textsuperscript textsubscript uparrow downarrow wedge vee log
arrow draw path node curve coordinate scriptsize small footnotesize strut mathord hline
""".split())
allowed_environments={'aligned','gathered','array','center','tikzcd','tikzpicture'}
def validate(path):
 s=re.sub(r'(?<!\\)%[^\n]*','',path.read_text());stack=[];env=[];dollars={};display=False;errs=[]
 def error(i,msg):errs.append(f'{path.name}:{s.count(chr(10),0,i)+1}: {msg}')
 for m in re.finditer(r'\\(?:begin|end)\{[^}]+\}|\\[a-zA-Z]+|\\.|[{}$]',s):
  v=m.group();i=m.start()
  if v.startswith(r'\begin{'):
   name=v[7:-1]
   if name not in allowed_environments:error(i,'unlisted environment '+name)
   env.append(name)
  elif v.startswith(r'\end{'):
   e=v[5:-1]
   if not env or env.pop()!=e:error(i,'unbalanced environment '+e)
  elif v=='{':stack.append(i)
  elif v=='}':
   if not stack:error(i,'closing brace')
   else:
    if dollars.get(len(stack),False):error(i,'open dollar at brace boundary')
    stack.pop()
  elif v=='$':dollars[len(stack)]=not dollars.get(len(stack),False)
  elif v==r'\[':
   if display:error(i,'nested display')
   display=True
  elif v==r'\]':
   if not display:error(i,'closing display')
   display=False
  elif re.fullmatch(r'\\[A-Za-z]+',v) and v[1:] not in allowed:error(i,'unlisted command '+v)
 if stack or env or display or any(dollars.values()):error(len(s),'unclosed groups, environments or math')
 return errs
if __name__=='__main__':
 pages=sorted((root/'pages').glob('*.tex'))
 problems=[s for p in pages for s in validate(p)]
 combined=root/'K33-04_transcription.tex'
 if combined.read_bytes()!=b''.join(p.read_bytes() for p in pages):problems.append('Concatenation differs.')
 if len(pages)!=13:problems.append('Expected 13 page files.')
 if problems:print('\n'.join(problems));sys.exit(1)
 print('13 pages passed braces, math delimiters, environment nesting, command catalogue and exact concatenation.')
