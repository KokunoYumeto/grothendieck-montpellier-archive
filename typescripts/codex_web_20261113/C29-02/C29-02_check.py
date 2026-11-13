#!/usr/bin/env python3
"""Structural checks only; no TeX compilation and no reading corrections."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

def check(path):
    source = re.sub(r'(?<!\\)%[^\n]*', '', path.read_text(encoding='utf-8'))
    braces, environments, math = [], [], None
    dollars = displays = 0
    tokens = re.compile(r'\\(?:begin|end)\{[^}]+\}|\\[\[\]]|\\[A-Za-z]+|\\.|[{}$]')
    for match in tokens.finditer(source):
        token = match.group()
        if token == '{':
            braces.append(match.start())
        elif token == '}':
            assert braces, f'{path.name}: unmatched closing brace'
            braces.pop()
        elif token == '$':
            assert math != 'display', f'{path.name}: dollar inside display'
            math = None if math == 'inline' else 'inline'
            dollars += 1
        elif token == r'\[':
            assert math is None, f'{path.name}: nested display/math'
            math = 'display'
            displays += 1
        elif token == r'\]':
            assert math == 'display', f'{path.name}: unmatched display close'
            math = None
        elif token.startswith(r'\begin{'):
            environments.append(token[7:-1])
        elif token.startswith(r'\end{'):
            name = token[5:-1]
            assert environments and environments.pop() == name, f'{path.name}: environment mismatch {name}'
    assert not braces, f'{path.name}: unclosed brace(s)'
    assert math is None, f'{path.name}: unclosed math'
    assert not environments, f'{path.name}: unclosed environment(s)'
    # The supplied unsure macro itself adds a superscript in math mode.
    for match in re.finditer(r'\\unsure\{', source):
        depth, cursor = 1, match.end()
        while depth:
            char = source[cursor]
            if char in '{}' and (cursor == 0 or source[cursor - 1] != '\\'):
                depth += 1 if char == '{' else -1
            cursor += 1
        rest = source[cursor:].lstrip()
        assert not rest.startswith(('^', "'")), f'{path.name}: ungrouped script after unsure'
    return f'{path.name}: PASS — braces, {dollars // 2} inline-math pairs, {displays} display pair(s), environments'

pages = sorted((ROOT / 'pages').glob('C29-02_29_scan*.tex'))
assert len(pages) == 6
assembled = ROOT / 'C29-02_transcription.tex'
assert assembled.read_bytes() == b''.join(p.read_bytes() for p in pages)
source = assembled.read_text(encoding='utf-8')
assert source.count(r'\cotefile{29}') == 1
assert re.findall(r'\\scanpage\{(\d+)\}', source) == ['21', '22', '23', '24', '25', '26']
assert r'\mspage{' not in source
assert 'dis%\n\\scanpage{26}%\n% archive sheet number: 25\nposer' in source
results = [check(p) for p in pages + [assembled, ROOT / 'C29-02_standalone.tex']]
counts = {name: len(re.findall(r'\\' + name + r'\b', source)) for name in ['unsure', 'illegible', 'deleted']}
results += ['Exact concatenation: PASS', 'Cote/scan markers and cross-page disposer join: PASS',
            'Marks in assembled fragment only: ' + ', '.join(f'{k}={v}' for k, v in counts.items()),
            'No compilation performed. Ordinary parentheses are not editorially balanced; source irregularities are retained.']
print('\n'.join(results))
