"""Lexical balance checks only; deliberately does not compile TeX."""
from pathlib import Path
import re
import sys

def check(path):
    text=path.read_text()
    braces=[]; envs=[]; math=[]; errors=[]; i=0
    def line(pos): return text[:pos].count('\n')+1
    while i<len(text):
        c=text[i]
        if c=='%':
            j=text.find('\n',i); i=len(text) if j<0 else j+1; continue
        if c=='\\':
            if i+1>=len(text): errors.append('trailing backslash'); break
            nextc=text[i+1]
            if nextc in '{}%$\\': i+=2; continue
            if nextc in '[(':
                if math: errors.append(f'line {line(i)}: nested math delimiter')
                math.append((nextc,line(i))); i+=2; continue
            if nextc in '])':
                expected='[' if nextc==']' else '('
                if not math or math[-1][0]!=expected: errors.append(f'line {line(i)}: unmatched math close')
                else: math.pop()
                i+=2; continue
            m=re.match(r'\\(begin|end)\s*\{([^{}]+)\}',text[i:])
            if m:
                kind,name=m.groups()
                if kind=='begin': envs.append((name,line(i)))
                elif not envs or envs[-1][0]!=name: errors.append(f'line {line(i)}: mismatched end {name}')
                else: envs.pop()
                i+=len(m.group()); continue
            m=re.match(r'\\[A-Za-z@]+',text[i:])
            i+=len(m.group()) if m else 2
            continue
        if c=='{': braces.append(line(i))
        elif c=='}':
            if not braces: errors.append(f'line {line(i)}: unmatched closing brace')
            else: braces.pop()
        elif c=='$':
            if math and math[-1][0]=='$': math.pop()
            elif math: errors.append(f'line {line(i)}: dollar inside other math delimiter')
            else: math.append(('$',line(i)))
        i+=1
    if braces: errors.append(f'unclosed braces at lines {braces}')
    if envs: errors.append(f'unclosed environments {envs}')
    if math: errors.append(f'unclosed math delimiters {math}')
    return errors

base=Path(__file__).resolve().parent
paths=sorted((base/'pages').glob('*.tex'))+[base/'J156-7-08_transcription.tex',base/'J156-7-08_standalone.tex',base/'PREAMBLE.tex']
failed=False
for p in paths:
    errors=check(p)
    print(('FAIL' if errors else 'PASS')+' '+str(p.relative_to(base)))
    for e in errors: print('  '+e)
    failed |= bool(errors)
fragment=(base/'J156-7-08_transcription.tex').read_text()
assert re.findall(r'\\scanpage\{(\d+)\}',fragment)==[str(n) for n in range(66,73)]
assert fragment.startswith('\\cotefile{156-7}')
assert fragment.count('\\cotefile{')==1
assert len(paths)==10
assert '\\documentclass' not in fragment
print('Scan order, single initial cote, and fragment/wrapper separation: PASS')
print('No TeX compilation performed.')
sys.exit(1 if failed else 0)
