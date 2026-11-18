"""Static LaTeX delimiter checks only; never invokes a TeX compiler."""
from pathlib import Path
import re, json

TOKEN = re.compile(r'\\(?:begin|end)\{[^{}]+\}|\\[A-Za-z]+|\\.|[{}$]')
MATH_ONLY = set('widetilde tilde bar overline underline mathbb mathscr mathcal mathfrak boldsymbol operatorname sigma gamma Gamma psi phi varphi theta Theta Pi Omega alpha beta delta partial lambda mu pi rho iota forall exists in ne equiv sim simeq subset otimes times circ prod sum bigcup lim varinjlim longrightarrow longmapsto rightsquigarrow xrightarrow underbrace underset substack cdot cdots lvert rvert Vert shortparallel'.split())
# underline is also valid in text, as are a few generic layout primitives.
MATH_ONLY.discard('underline')
MATH_ENVS={'aligned','gathered','array','tikzcd'}

def strip_comments(s):
    return re.sub(r'(?<!\\)%[^\n]*','',s)

def check(path):
    s=strip_comments(path.read_text())
    braces=[]; envs=[]; displays=[]; dollar=None; errors=[]
    brace_pairs=0; display_pairs=0; dollar_pairs=0; env_pairs=0
    for m in TOKEN.finditer(s):
        t=m[0]; line=s.count('\n',0,m.start())+1
        if t=='{':braces.append(line)
        elif t=='}':
            if not braces:errors.append(f'line {line}: unmatched closing brace')
            else:braces.pop();brace_pairs+=1
        elif t==r'\[':displays.append(line)
        elif t==r'\]':
            if not displays:errors.append(f'line {line}: unmatched display close')
            else:displays.pop();display_pairs+=1
        elif t=='$':
            if dollar is None:dollar=line
            else:dollar=None;dollar_pairs+=1
        elif t.startswith(r'\begin{'):envs.append((t[7:-1],line))
        elif t.startswith(r'\end{'):
            name=t[5:-1]
            if not envs or envs[-1][0]!=name:errors.append(f'line {line}: unmatched environment close {name}')
            else:envs.pop();env_pairs+=1
    errors += [f'line {x}: unclosed brace' for x in braces]
    errors += [f'line {x}: unclosed display' for x in displays]
    errors += [f'line {x}: unclosed environment {n}' for n,x in envs]
    if dollar is not None:errors.append(f'line {dollar}: unmatched dollar')
    # Additional conservative math-mode check, allowing text islands inside math.
    mode=False;groups=[];modes=[];pending_text=False
    for m in TOKEN.finditer(s):
        t=m[0];line=s.count('\n',0,m.start())+1
        if t in {r'\text',r'\textrm',r'\textsf',r'\textnormal'}:pending_text=True
        elif t=='{':
            inside=False if pending_text else mode
            groups.append((mode,inside,line));mode=inside;pending_text=False
        elif t=='}':
            if groups:
                outer,inside,startline=groups.pop()
                if mode!=inside:errors.append(f'line {line}: math mode changed across brace group opened on line {startline}')
                mode=outer
        elif t=='$':mode=not mode
        elif t==r'\[':mode=True
        elif t==r'\]':mode=False
        elif t.startswith(r'\begin{'):
            name=t[7:-1];modes.append(mode)
            if name in MATH_ENVS:mode=True
        elif t.startswith(r'\end{'):
            if modes:mode=modes.pop()
        elif t.startswith('\\') and t[1:] in MATH_ONLY and not mode:
            errors.append(f'line {line}: math command outside math mode: {t}')
    # The supplied unsure macro contributes a question-mark superscript in math.
    # An immediately following exponent therefore needs an outer group.
    for m in re.finditer(r'\\unsure\{',s):
        i=m.end();depth=1
        while depth and i<len(s):
            if s[i]=='\\':
                tok=re.match(r'\\(?:[A-Za-z]+|.)',s[i:]);i+=len(tok[0]);continue
            if s[i]=='{':depth+=1
            elif s[i]=='}':depth-=1
            i+=1
        if s[i:].lstrip().startswith('^'):
            errors.append(f'line {s.count(chr(10),0,m.start())+1}: unsure followed directly by exponent')
    return dict(file=str(path),brace_pairs=brace_pairs,display_pairs=display_pairs,dollar_pairs=dollar_pairs,environment_pairs=env_pairs,errors=errors)

if __name__=='__main__':
    root=Path(__file__).resolve().parent
    files=sorted((root/'pages').glob('*.tex'))+[root/'K46-02_transcription.tex',root/'K46-02_standalone.tex']
    rows=[check(p) for p in files]
    result={'check':'static delimiters and conservative math-mode check; no compilation','passed':all(not r['errors'] for r in rows),'files':rows}
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result['passed'] else 1)
