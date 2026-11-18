"""Structural LaTeX checks only. Deliberately does not compile or alter readings."""
from pathlib import Path
import re, json, collections

ROOT=Path(__file__).resolve().parent

def check(path):
    s=path.read_text();stack=[];env=[];math=[];dollar=False;errors=[];i=0;line=1
    while i<len(s):
        c=s[i]
        if c=='\n':line+=1;i+=1;continue
        if c=='%':
            j=s.find('\n',i);i=len(s) if j<0 else j;continue
        if c=='\\':
            em=re.match(r'\\(begin|end)\{([^}]+)\}',s[i:])
            if em:
                action,name=em.groups()
                if action=='begin':env.append((name,line))
                elif not env or env[-1][0]!=name:errors.append(f'line {line}: mismatched end {name}')
                else:env.pop()
                i+=len(em.group());continue
            m=re.match(r'\\(?:[A-Za-z]+|.)',s[i:],re.S)
            token=m.group() if m else '\\'
            if token in [r'\[',r'\(']:math.append((token,line))
            if token in [r'\]',r'\)']:
                want=r'\[' if token==r'\]' else r'\('
                if not math or math[-1][0]!=want:errors.append(f'line {line}: mismatched {token}')
                else:math.pop()
            line+=token.count('\n');i+=len(token);continue
        if c=='{':stack.append(line)
        elif c=='}':
            if stack:stack.pop()
            else:errors.append(f'line {line}: extra closing brace')
        elif c=='$':dollar=not dollar
        i+=1
    if stack:errors.append(f'unclosed braces at lines {stack}')
    if env:errors.append(f'unclosed environments {env}')
    if math:errors.append(f'unclosed math delimiters {math}')
    if dollar:errors.append('odd number of unescaped dollar signs')
    for m in re.finditer(r'\\begin\{tikzcd\}(?:\[([^]]*)\])?',s):
        if r'ampersand replacement=\&' not in (m.group(1) or ''):errors.append('tikzcd lacks ampersand replacement')
    return dict(file=str(path.relative_to(ROOT)),status='PASS' if not errors else 'FAIL',errors=errors)

if __name__=='__main__':
    paths=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'K70-03_transcription.tex',ROOT/'K70-03_standalone.tex']
    results=[check(p) for p in paths]
    print(json.dumps(dict(compiled=False,results=results),indent=2))
    raise SystemExit(any(r['errors'] for r in results))
