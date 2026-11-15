"""Structural check only; does not invoke a TeX engine."""
from pathlib import Path
import re

def check(path):
    text=path.read_text(); braces=[]; env=[]; display=[]; dollar=None; errors=[]
    i=0; line=1; dollars=0; displays=0
    while i<len(text):
        c=text[i]
        if c=='\n': line+=1;i+=1;continue
        if c=='%':
            j=text.find('\n',i);i=len(text) if j<0 else j;continue
        if c=='\\':
            m=re.match(r'\\(begin|end)\{([^}]+)\}',text[i:])
            if m:
                if m[1]=='begin':env.append((m[2],line))
                elif not env or env[-1][0]!=m[2]:errors.append(f'line {line}: unmatched end {m[2]}')
                else:env.pop()
                i+=len(m[0]);continue
            if text[i:i+2]=='\\[':
                if display or dollar is not None:errors.append(f'line {line}: nested display/math opener')
                display.append(line);displays+=1;i+=2;continue
            if text[i:i+2]=='\\]':
                if not display:errors.append(f'line {line}: unmatched display closer')
                else:display.pop()
                i+=2;continue
            m=re.match(r'\\[A-Za-z]+|\\.',text[i:])
            i+=len(m[0]) if m else 1;continue
        if c=='{':braces.append(line)
        elif c=='}':
            if not braces:errors.append(f'line {line}: unmatched closing brace')
            else:braces.pop()
        elif c=='$':
            dollars+=1
            if display:errors.append(f'line {line}: dollar delimiter within display source')
            dollar=line if dollar is None else None
        i+=1
    errors += [f'line {n}: unclosed brace' for n in braces]
    errors += [f'line {n}: unclosed environment {e}' for e,n in env]
    errors += [f'line {n}: unclosed display' for n in display]
    if dollar is not None:errors.append(f'line {dollar}: unclosed dollar math')
    return errors,dollars//2,displays

if __name__=='__main__':
    root=Path(__file__).resolve().parent
    paths=sorted((root/'pages').glob('*.tex'))+[root/'J156-8-03_transcription.tex',root/'J156-8-03_standalone.tex']
    failed=False
    for path in paths:
        errors,pairs,displays=check(path);failed|=bool(errors)
        print(f'{path.relative_to(root)}: '+('FAIL' if errors else 'PASS')+f'; dollar pairs={pairs}; displays={displays}; braces and environments balanced={not errors}')
        for error in errors:print('  '+error)
    raise SystemExit(1 if failed else 0)
