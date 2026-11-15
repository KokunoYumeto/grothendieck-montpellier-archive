#!/usr/bin/env python3
"""Static balance checks only. This script never runs a TeX engine.

Round parentheses and ordinary square brackets are deliberately not balanced:
some are unfinished in the manuscript and were retained diplomatically.
"""
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parent

def uncomment(text):
    out=[]
    for line in text.splitlines(keepends=True):
        for i,c in enumerate(line):
            if c=='%':
                n=0;j=i-1
                while j>=0 and line[j]=='\\':n+=1;j-=1
                if n%2==0:
                    line=line[:i]+'\n';break
        out.append(line)
    return ''.join(out)

def check(path):
    text=uncomment(path.read_text())
    groups=[];display=[];env=[];errors=[];dollars=[]
    i=0;line=1
    while i<len(text):
        c=text[i]
        if c=='\n':line+=1
        if c=='\\':
            match=re.match(r'\\(begin|end)\{([^{}]+)\}',text[i:])
            if match:
                kind,name=match.groups()
                if kind=='begin':env.append((name,line))
                elif not env:errors.append(f'line {line}: unexpected end {name}')
                elif env[-1][0]!=name:errors.append(f'line {line}: end {name} mismatches {env[-1]}')
                else:env.pop()
                i+=len(match[0]);continue
            if i+1<len(text):
                n=text[i+1]
                if n=='[':display.append(line)
                elif n==']':
                    if not display:errors.append(f'line {line}: unexpected display close')
                    else:display.pop()
                # Escaped braces, %, $, and backslash are single control symbols.
                if not n.isalpha():i+=2;continue
                match=re.match(r'\\[A-Za-z]+',text[i:])
                i+=len(match[0]);continue
        elif c=='{':groups.append(line)
        elif c=='}':
            if not groups:errors.append(f'line {line}: unexpected group close')
            else:groups.pop()
        elif c=='$':
            if dollars:dollars.pop()
            else:dollars.append(line)
        i+=1
    if groups:errors.append(f'unclosed groups from lines {groups}')
    if display:errors.append(f'unclosed display math from lines {display}')
    if dollars:errors.append(f'unpaired dollar from line {dollars[0]}')
    if env:errors.append(f'unclosed environments {env}')
    return errors

paths=sorted((ROOT/'pages').glob('*.tex'))
paths+=[ROOT/'J156-9-09_transcription.tex',ROOT/'J156-9-09_standalone.tex']
failed=False
for path in paths:
    errors=check(path)
    print(f'{path.relative_to(ROOT)}: '+('FAIL' if errors else 'PASS — braces, display delimiters, dollar pairs, environments'))
    for error in errors:print('  '+error)
    failed|=bool(errors)
print('No compilation attempted. Plain manuscript parentheses were not normalized.')
sys.exit(int(failed))
