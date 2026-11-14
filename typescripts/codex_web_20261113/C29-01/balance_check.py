#!/usr/bin/env python3
"""Check literal LaTeX delimiters and environments without compiling."""
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def check(path):
    source=path.read_text(encoding='utf-8')
    source=re.sub(r'(?<!\\)%[^\n]*','',source)
    braces=[]; environments=[]; math=None; errors=[]; inline=0; display=0
    token_re=re.compile(r'\\(?:begin|end)\{[^{}]+\}|\\\[|\\\]|\\\(|\\\)|\\[A-Za-z@]+|\\.|[{}$]',re.S)
    for match in token_re.finditer(source):
        token=match.group(); line=source.count('\n',0,match.start())+1
        if token.startswith('\\begin{'):
            environments.append((token[7:-1],line))
        elif token.startswith('\\end{'):
            name=token[5:-1]
            if not environments or environments[-1][0]!=name:errors.append(f'line {line}: unmatched {token}')
            else:environments.pop()
        elif token=='{':braces.append(line)
        elif token=='}':
            if braces:braces.pop()
            else:errors.append(f'line {line}: extra closing brace')
        elif token=='$':
            if math is None:math=('$',line);inline+=1
            elif math[0]=='$':math=None
            else:errors.append(f'line {line}: dollar inside {math[0]}')
        elif token in ('\\[','\\('):
            if math is not None:errors.append(f'line {line}: nested math delimiter {token}')
            else:math=(token,line)
            if token=='\\[':display+=1
        elif token in ('\\]','\\)'):
            expected={'\\]':'\\[','\\)':'\\('}[token]
            if math is None or math[0]!=expected:errors.append(f'line {line}: unmatched {token}')
            else:math=None
    if braces:errors.append(f'unclosed braces at lines {braces}')
    if environments:errors.append(f'unclosed environments: {environments}')
    if math:errors.append(f'unclosed math delimiter: {math}')
    return errors,inline,display

if __name__=='__main__':
    paths=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'C29-01_transcription.tex',ROOT/'C29-01_standalone.tex']
    failed=False
    for path in paths:
        errors,inline,display=check(path)
        print(f'{path.relative_to(ROOT)}: '+('; '.join(errors) if errors else f'PASS; {inline} inline math pairs, {display} display pairs; braces and environments balanced'))
        failed |= bool(errors)
    print('No compilation attempted.')
    raise SystemExit(1 if failed else 0)
