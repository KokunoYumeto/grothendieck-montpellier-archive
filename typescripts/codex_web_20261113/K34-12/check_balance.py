"""Structural checks only. This script does not invoke a TeX engine."""
from pathlib import Path
import re, sys

def check(path):
    s=path.read_text(encoding='utf-8')
    s=re.sub(r'(?<!\\)%[^\n]*','',s)
    errors=[]; braces=[]; env=[]; displays=[]; dollars=[]
    # Consume a TeX line-break command before looking for display delimiters:
    # the second slash in \\[1em] is not the start of a \\[ display.
    tokens=re.compile(r'\\begin\{([^}]+)\}|\\end\{([^}]+)\}|\\\\|\\\[|\\\]|\\[{}%$]|[{}$]')
    for m in tokens.finditer(s):
        t=m.group(); line=s.count('\n',0,m.start())+1
        if m.group(1):env.append((m.group(1),line))
        elif m.group(2):
            if not env or env[-1][0]!=m.group(2):errors.append(f'L{line}: mismatched end {m.group(2)}')
            else:env.pop()
        elif t==r'\[':displays.append(line)
        elif t==r'\]':
            if not displays:errors.append(f'L{line}: unmatched display close')
            else:displays.pop()
        elif t=='{':braces.append(line)
        elif t=='}':
            if not braces:errors.append(f'L{line}: unmatched brace')
            else:braces.pop()
        elif t=='$':
            if dollars:dollars.pop()
            else:dollars.append(line)
    if braces:errors.append(f'unclosed braces at {braces}')
    if env:errors.append(f'unclosed environments {env}')
    if displays:errors.append(f'unclosed displays at {displays}')
    if dollars:errors.append(f'unpaired dollar at {dollars}')
    return errors

if __name__=='__main__':
    root=Path(__file__).resolve().parent
    files=sorted((root/'pages').glob('*.tex'))+[root/'K34-12_transcription.tex',root/'K34-12_standalone.tex',root/'PREAMBLE.tex']
    failed=False
    for p in files:
        e=check(p); failed|=bool(e)
        print(f'{p.relative_to(root)}: '+('; '.join(e) if e else 'PASS (braces, displays, dollars, environments)'))
    sys.exit(1 if failed else 0)
