#!/usr/bin/env python3
"""Structural checks only. This script does not invoke a TeX engine."""
from pathlib import Path
import re
import csv

ROOT = Path(__file__).resolve().parent

def unescaped(text, i):
    n = 0
    while i > 0 and text[i-1] == '\\':
        n += 1
        i -= 1
    return n % 2 == 0

def without_comments(text):
    lines = []
    for line in text.splitlines():
        for i, c in enumerate(line):
            if c == '%' and unescaped(line, i):
                line = line[:i]
                break
        lines.append(line)
    return '\n'.join(lines)

def check(path):
    s = without_comments(path.read_text())
    braces = []
    for i, c in enumerate(s):
        if not unescaped(s, i):
            continue
        if c == '{':
            braces.append(i)
        elif c == '}':
            assert braces, f'{path.name}: extra closing brace at {i}'
            braces.pop()
    assert not braces, f'{path.name}: unclosed brace(s)'
    displays = []
    for m in re.finditer(r'\\[\[\]]', s):
        if not unescaped(s, m.start()):
            continue
        if m.group() == r'\[':
            assert not displays, f'{path.name}: nested display'
            displays.append(m.start())
        else:
            assert displays, f'{path.name}: extra display close'
            displays.pop()
    assert not displays, f'{path.name}: unclosed display'
    dollars = [i for i,c in enumerate(s) if c == '$' and unescaped(s,i)]
    assert len(dollars) % 2 == 0, f'{path.name}: odd dollar count'
    envs = []
    for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}', s):
        action, name = m.groups()
        if action == 'begin':
            envs.append(name)
        else:
            assert envs and envs[-1] == name, f'{path.name}: mismatched {name}'
            envs.pop()
    assert not envs, f'{path.name}: unclosed environments {envs}'
    return f'{path.relative_to(ROOT)}: PASS (braces, displays, dollars, environments)'

if __name__ == '__main__':
    pages = sorted((ROOT/'pages').glob('*.tex'))
    assert len(pages) == 8
    for scan, page in zip(range(50,58), pages):
        text = page.read_text()
        assert f'\\scanpage{{{scan}}}' in text
        assert f'\\mspage{{{scan-9}}}' in text
        print(check(page))
    fragment = ROOT/'J156-8-07_transcription.tex'
    assert fragment.read_text() == '\n'.join(p.read_text().rstrip() for p in pages)+'\n'
    assert fragment.read_text().count(r'\cotefile{156-8}') == 1
    assert fragment.read_text().startswith(r'\cotefile{156-8}')
    assert r'\documentclass' not in fragment.read_text()
    print(check(fragment))
    print(check(ROOT/'J156-8-07_standalone.tex'))
    print(check(ROOT/'PREAMBLE.tex'))
    rows = list(csv.DictReader((ROOT/'J156-8-07_inventory.csv').open()))
    assert all(r['transcribed']=='yes' for r in rows)
    assert {int(r['scan']) for r in rows} == set(range(50,58))
    assert len({r['element'] for r in rows}) == len(rows)
    assert all(r['kind'] in {'text','letter part','display','diagram','drawing','margin note','insertion','deletion','handwritten'} for r in rows)
    print(f'Assembly and inventory: PASS ({len(rows)} rows, all yes)')
    print('No TeX compilation performed.')
