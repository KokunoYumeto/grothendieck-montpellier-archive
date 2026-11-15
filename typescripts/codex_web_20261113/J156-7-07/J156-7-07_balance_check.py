#!/usr/bin/env python3
"""Structural checks only: this script does not compile or validate readings."""
from pathlib import Path
import csv
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parent

def uncomment(text):
    lines = []
    for line in text.splitlines():
        for i, ch in enumerate(line):
            if ch == '%':
                k = i - 1
                slashes = 0
                while k >= 0 and line[k] == '\\':
                    slashes += 1
                    k -= 1
                if slashes % 2 == 0:
                    line = line[:i]
                    break
        lines.append(line)
    return '\n'.join(lines)

def balance(path):
    source = uncomment(path.read_text())
    errors = []
    stack = []
    dollar = False
    display = False
    envs = []
    tokens = re.compile(r'\\begin\{([^}]+)\}|\\end\{([^}]+)\}|\\\[|\\\]|\\.|[{}$]')
    for match in tokens.finditer(source):
        token = match.group()
        line = source.count('\n', 0, match.start()) + 1
        if match.group(1):
            envs.append((match.group(1),line))
        elif match.group(2):
            if not envs or envs[-1][0] != match.group(2):
                errors.append(f'line {line}: mismatched end {match.group(2)}')
            else:
                envs.pop()
        elif token == '{':
            stack.append(line)
        elif token == '}':
            if not stack:
                errors.append(f'line {line}: unmatched closing brace')
            else:
                stack.pop()
        elif token == r'\[':
            if display or dollar:
                errors.append(f'line {line}: nested/overlapping display opening')
            display = True
        elif token == r'\]':
            if not display:
                errors.append(f'line {line}: unmatched display closing')
            display = False
        elif token == '$':
            if display:
                errors.append(f'line {line}: dollar inside display')
            dollar = not dollar
    if stack:
        errors.append('unclosed braces at lines '+str(stack))
    if envs:
        errors.append('unclosed environments '+str(envs))
    if dollar:
        errors.append('unclosed dollar math')
    if display:
        errors.append('unclosed display math')
    return errors

page_paths = [ROOT/'pages'/f'J156-7-07_156-7_scan{n:03}.tex' for n in range(58,66)]
targets = page_paths + [ROOT/'J156-7-07_transcription.tex',
                       ROOT/'J156-7-07_standalone.tex',ROOT/'PREAMBLE.tex']
failures = []
for path in targets:
    errors = balance(path)
    failures.extend((str(path.relative_to(ROOT)),e) for e in errors)
    print(('FAIL' if errors else 'PASS')+' '+str(path.relative_to(ROOT))+
          ': braces, display delimiters, dollars, environments')

texts = [p.read_text() for p in page_paths]
assembled = (ROOT/'J156-7-07_transcription.tex').read_text()
expected = '\n\n'.join(s.rstrip() for s in texts)+'\n'
assert assembled == expected, 'assembled fragment differs from ordered page concatenation'
assert assembled.startswith(r'\cotefile{156-7}'+'\n'+r'\scanpage{58}')
assert assembled.count(r'\cotefile{') == 1
assert re.findall(r'\\scanpage\{(\d+)\}',assembled) == [str(n) for n in range(58,66)]
assert re.findall(r'\\mspage\{(\d+)\}',assembled) == [str(n) for n in range(57,65)]
assert not re.search(r'\\(?:documentclass|newcommand|includegraphics|include)\b',assembled)
for diagram in re.findall(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}', assembled,re.S):
    assert r'ampersand replacement=\&' in diagram
    assert not re.search(r'(?<!\\)&',diagram), 'bare alignment ampersand in diagram'
inventory = list(csv.DictReader((ROOT/'J156-7-07_inventory.csv').open()))
assert {int(r['scan']) for r in inventory} == set(range(58,66))
assert all(r['transcribed'] == 'yes' for r in inventory)
assert all(r['cote'] == '156-7' and r['hand'] == 'Grothendieck' for r in inventory)
log = (ROOT/'progress.log').read_text()
assert all(f'scan {n:03} done ' in log and f'scan {n:03} audited ' in log for n in range(58,66))
for name in ('unsure','illegible','deleted'):
    print(f'{name}: {len(re.findall(chr(92)+chr(92)+name+chr(92)+"{",assembled))}')
print(f'Inventory: {len(inventory)} elements, all yes; eight pages done and audited')
print('Assembly: exact ordered concatenation; cote once; scan/manuscript numbers complete')
print('TikZ-cd: all diagrams use the required ampersand replacement')
print('No compilation attempted; these checks do not establish mathematical or reading accuracy')
if failures:
    for path,error in failures:
        print('ERROR',path,error)
    sys.exit(1)
print('BALANCE CHECK PASSED')
