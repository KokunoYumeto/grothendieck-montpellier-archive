#!/usr/bin/env python3
"""Static checks only; does not invoke TeX or change any source reading."""
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parent

def tokens(source):
    # Consume TeX control sequences first, so escaped braces/dollars/percent signs
    # and the two-character control sequence \\ are not counted as delimiters.
    i=0
    while i<len(source):
        c=source[i]
        if c=='%':
            j=source.find('\n',i);i=len(source) if j<0 else j+1;continue
        if c=='\\':
            m=re.match(r'\\(?:[A-Za-z]+|.)',source[i:],re.S)
            s=m.group();yield s,i;i+=len(s);continue
        yield c,i;i+=1

def check(path):
    source=path.read_text(encoding='utf-8')
    brace=[];env=[];math=None;errors=[];seq=list(tokens(source))
    for i,(tok,pos) in enumerate(seq):
        if tok=='{':brace.append(pos)
        elif tok=='}':
            if brace:brace.pop()
            else:errors.append(f'unmatched }} at {pos}')
        elif tok=='$':
            if math is None:math=('$',pos)
            elif math[0]=='$':math=None
            else:errors.append(f'$ inside {math[0]} at {pos}')
        elif tok=='\\[':
            if math is not None:errors.append(f'display opens inside math at {pos}')
            math=('\\[',pos)
        elif tok=='\\]':
            if math is None or math[0]!='\\[':errors.append(f'unmatched \\] at {pos}')
            else:math=None
        elif tok in ('\\begin','\\end'):
            m=re.match(r'\s*\{([^{}]+)\}',source[pos+len(tok):])
            if not m:errors.append(f'missing environment name at {pos}');continue
            name=m.group(1)
            if tok=='\\begin':env.append((name,pos))
            elif not env or env[-1][0]!=name:errors.append(f'mismatched end {name} at {pos}')
            else:env.pop()
    if brace:errors.append(f'{len(brace)} unclosed braces')
    if math:errors.append(f'unclosed math {math}')
    if env:errors.append(f'unclosed environments {env}')
    return errors

pages=sorted((ROOT/'pages').glob('A36-01_36_scan*.tex'))
assert len(pages)==9, f'Expected 9 pages, found {len(pages)}'
failed=False
for path in pages+[ROOT/'A36-01_transcription.tex',ROOT/'A36-01_standalone.tex']:
    errors=check(path);failed|=bool(errors)
    print(f'{path.name}: '+('; '.join(errors) if errors else 'PASS braces, dollars, display delimiters, environments'))
if failed:sys.exit(1)
print('No compilation performed. Literal source parentheses are outside this syntax check.')
