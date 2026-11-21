"""Static checks for the cote 7 fragments; run from any directory with Python 3."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parent
KNOWN = set(r"""cotefile scanpage mspage handwritten deleted inserted margin uline uuline diagram figure unsure illegible
S mathscr mathcal mathbb mathfrak mathrm mathbf mathbin mathrel operatorname overset tag substack text textsuperscript
begin end arrow draw node fill longrightarrow longleftarrow Longleftarrow leftarrow rightarrow xleftarrow xrightarrow to
simeq sim equiv subset subseteq supset in otimes times ltimes circ circledast cdot bullet star underline frac bar
widetilde tilde widehat hat Delta Sigma Omega Theta xi zeta nu alpha beta gamma varphi ell geq leq lim varprojlim varinjlim
rightsquigarrow boxed underbrace log quad qquad hfill rule linewidth noindent makeatletter tagsleft@true makeatother
reversemarginpar normalmarginpar baselineskip raisebox begingroup endgroup mkern rotatebox wr vert textnormal itshape mathop limits rightarrowleftarrow colon pm
phantom mathord subscript scriptstyle left right textit textrm mbox stackrel overset underset mathsf ast mapsto
ne neq mathring atop cr centered smallmatrix tfrac prime epsilon varnothing longmapsto longleftrightarrow""".split())
def check(path):
    s='\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in path.read_text().splitlines())
    stack=[]; math=[]; env=[]; issues=[]
    for m in re.finditer(r'\\(?:begin|end)\{[^{}]*\}|\\(?:[a-zA-Z@]+|.)|[{}$]',s,re.S):
        t=m.group()
        if t.startswith((r'\begin{',r'\end{')):
            name=t.split('{')[1][:-1]
            if name not in {'tikzcd','tikzpicture','center','aligned','gathered','array','matrix','smallmatrix'}:issues.append('unknown environment '+name)
            if t.startswith(r'\begin'): env.append(name)
            elif not env or env.pop()!=name:issues.append('environment '+t)
        elif t=='{':stack.append(m.start())
        elif t=='}':
            if stack:stack.pop()
            else:issues.append('extra }')
        elif t==r'\[':math.append(t)
        elif t==r'\]':
            if not math or math.pop()!=r'\[': issues.append('unpaired display')
        elif t=='$':
            if math and math[-1]=='$':math.pop()
            else:math.append('$')
        elif re.fullmatch(r'\\[a-zA-Z@]+',t) and t[1:] not in KNOWN:issues.append('unknown command '+t)
    if stack or math or env:issues.append('unclosed group, math delimiter or environment')
    return list(dict.fromkeys(issues))
if __name__=='__main__':
    import sys
    paths=sorted((ROOT/'pages').glob('*.tex'))
    failed=False
    for p in paths:
        issues=check(p);failed|=bool(issues);print(p.name,', '.join(issues) or 'PASS')
    if len(paths)!=14:failed=True
    fragment=ROOT/'K7-04_transcription.tex'
    if fragment.exists() and fragment.read_bytes()!=b''.join(p.read_bytes() for p in paths):
        print('Assembled bytes differ from concatenation');failed=True
    sys.exit(int(failed))
