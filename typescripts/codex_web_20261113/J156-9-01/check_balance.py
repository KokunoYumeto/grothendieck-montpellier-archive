#!/usr/bin/env python3
"""Static delimiter/environment checks only; never invokes a TeX engine."""
from pathlib import Path
import re,sys
root=Path(__file__).resolve().parent
paths=sorted((root/'pages').glob('*.tex'))+[root/'J156-9-01_transcription.tex',root/'J156-9-01_standalone.tex']
all_ok=True
for p in paths:
    s=p.read_text(); braces=[];envs=[];math=None;dollars=False;errors=[];i=0;line=1
    while i<len(s):
        c=s[i]
        if c=='\n':line+=1;i+=1;continue
        if c=='%':
            j=s.find('\n',i);i=len(s) if j<0 else j;continue
        if c=='\\':
            if i+1<len(s) and s[i+1] in '{}%$\\&':i+=2;continue
            m=re.match(r'\\(begin|end)\{([^}]+)\}',s[i:])
            if m:
                action,name=m.groups()
                if action=='begin':envs.append((name,line))
                elif not envs or envs[-1][0]!=name:errors.append(f'line {line}: unexpected end {name}')
                else:envs.pop()
                i+=len(m.group());continue
            if i+1<len(s) and s[i+1] in '[]':
                token=s[i+1]
                if token=='[':
                    if math:errors.append(f'line {line}: display opens inside {math}')
                    math='display'
                elif math!='display':errors.append(f'line {line}: unexpected display close')
                else:math=None
                i+=2;continue
            m=re.match(r'\\[A-Za-z]+',s[i:]);i+=len(m.group()) if m else 2;continue
        if c=='{':braces.append(line)
        elif c=='}':
            if not braces:errors.append(f'line {line}: unmatched close brace')
            else:braces.pop()
        elif c=='$':
            dollars=not dollars
        i+=1
    if braces:errors.append(f'unclosed braces from lines {braces}')
    if envs:errors.append(f'unclosed environments {envs}')
    if math:errors.append(f'unclosed {math} math')
    if dollars:errors.append('unclosed dollar math')
    status='PASS' if not errors else 'FAIL';print(f'{status} {p.relative_to(root)}')
    for e in errors:print('  '+e)
    all_ok=all_ok and not errors
print('No LaTeX compilation was attempted.')
sys.exit(0 if all_ok else 1)
