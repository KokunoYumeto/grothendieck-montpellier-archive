"""Static LaTeX balance and command check for the cote 58 fragments."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
APPROVED = set(r"""
cotefile scanpage mspage handwritten deleted inserted margin uline uuline diagram figure unsure illegible
begin end text texttt textrm mathrm mathbf mathcal mathscr mathfrak mathbb operatorname mathop mathbin
underline overline hat widehat tilde widetilde bar leq geq le ge neq ne in notin ni subset subseteq
supset supseteq varnothing emptyset cap cup times otimes oplus circ wedge vee prod coprod sum lim
varprojlim varinjlim projlim injlim to mapsto leadsto longrightarrow longleftarrow rightarrow leftarrow
rightarrowtail hookrightarrow Longrightarrow Longleftarrow Leftrightarrow Rightarrow Leftarrow
longleftrightarrow Longleftrightarrow leftrightarrow sim simeq cong equiv approx overset underset
mathrel stackrel substack tag textstyle displaystyle scriptstyle scriptscriptstyle
Gamma gamma Pi pi Phi phi varphi Lambda lambda Delta delta alpha beta xi rho eta mu nu
mathopen mathclose mathord mathpzc ell cdot cdots ldots dots ldotsinfty infty pm mp
mid vert Vert left right big bigl bigr Big Bigl Bigr lbrace rbrace tfrac frac
mathrm mathit hspace vspace hfill hphantom phantom quad qquad S P small normalfont
noindent rule linewidth textsuperscript emph textbf textit fbox boxed par
node draw fill path coordinate arrow ar label glqq grqq forall exists dim max min
ker hom log exp limits nolimits vec bigcirc csname endcsname ensuremath
""".split())
TOKENS=re.compile(r'\\begin\{([^{}]+)\}|\\end\{([^{}]+)\}|\\([a-zA-Z]+)|\\(.)|([{}$])', re.S)
ENVS={'center','aligned','array','tikzpicture','tikzcd','matrix','smallmatrix','gathered',
      'enumerate','itemize','cases'}
def check(path):
    text=re.sub(r'(?<!\\)%[^\n]*','',path.read_text(encoding='utf8'))
    braces=[]; modes=[]; envs=[]; issues=[]
    for match in TOKENS.finditer(text):
        start,stop,command,escaped,char=match.groups()
        line=text.count('\n',0,match.start())+1
        if start:
            if start not in ENVS:issues.append((line,'unknown environment '+start))
            envs.append((start,line))
        elif stop:
            if not envs or envs[-1][0]!=stop:issues.append((line,'unexpected end '+stop))
            else:envs.pop()
        elif command:
            if command not in APPROVED:issues.append((line,'unknown command '+repr(command)))
        elif escaped in ('[','('):
            if modes:issues.append((line,'nested math opening'))
            modes.append((escaped,line))
        elif escaped in (']',')'):
            expect={']':'[',')':'('}[escaped]
            if not modes or modes[-1][0]!=expect:issues.append((line,'mismatched math close'))
            else:modes.pop()
        elif char=='{':braces.append(line)
        elif char=='}':
            if not braces:issues.append((line,'extra }'))
            else:braces.pop()
        elif char=='$':
            if modes and modes[-1][0]=='$':modes.pop()
            elif modes:issues.append((line,'dollar within display'))
            else:modes.append(('$',line))
    return issues+[('end',f'unclosed {name} {value}') for name,value in [('braces',braces),('math',modes),('environments',envs)] if value]

if __name__=='__main__':
    files=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'K58-04_transcription.tex']
    failed=False
    for f in files:
        issues=check(f)
        print(f.name,'PASS' if not issues else repr(issues))
        failed |= bool(issues)
    raise SystemExit(int(failed))

