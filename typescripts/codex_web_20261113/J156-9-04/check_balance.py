"""Structural checks only. This script does not compile or interpret LaTeX."""
from pathlib import Path
import re
import json

ROOT = Path(__file__).resolve().parent

def escaped(s, i):
    n = 0
    i -= 1
    while i >= 0 and s[i] == '\\':
        n += 1
        i -= 1
    return bool(n % 2)

def uncomment(s):
    result = []
    for line in s.splitlines():
        end = len(line)
        for i, char in enumerate(line):
            if char == '%' and not escaped(line, i):
                end = i
                break
        result.append(line[:end])
    return '\n'.join(result)

def check(path):
    s = uncomment(path.read_text())
    errors = []
    braces = []
    for i, char in enumerate(s):
        if char not in '{}' or escaped(s, i):
            continue
        if char == '{':
            braces.append(i)
        elif braces:
            braces.pop()
        else:
            errors.append(f'unmatched closing brace at offset {i}')
    if braces:
        errors.append(f'{len(braces)} unclosed brace(s)')

    display = []
    display_count = 0
    for m in re.finditer(r'\\[\[\]]', s):
        if escaped(s, m.start()):
            continue
        if m.group() == r'\[':
            display.append(m.start())
            display_count += 1
        elif display:
            display.pop()
        else:
            errors.append('unmatched display close')
    if display:
        errors.append('unclosed display')

    dollars = [i for i, c in enumerate(s) if c == '$' and not escaped(s, i)]
    if len(dollars) % 2:
        errors.append('odd number of dollar delimiters')

    envs = []
    env_count = 0
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}', s):
        action, env = m.groups()
        if action == 'begin':
            envs.append(env)
            env_count += 1
        elif not envs or envs[-1] != env:
            errors.append('environment nesting mismatch: ' + env)
        else:
            envs.pop()
    if envs:
        errors.append('unclosed environments: ' + ', '.join(envs))
    for m in re.finditer(r'\\begin\{tikzcd\}(?:\[([^]]*)\])?', s):
        if not m.group(1) or 'ampersand replacement=\\&' not in m.group(1):
            errors.append('tikzcd lacks ampersand replacement')
    return {
        'file': str(path.relative_to(ROOT)),
        'balanced': not errors,
        'display_pairs': display_count,
        'dollar_delimiters': len(dollars),
        'environment_pairs': env_count,
        'marks': {name: len(re.findall(r'\\' + name + r'\{', s))
                  for name in ('unsure', 'illegible', 'deleted')},
        'errors': errors,
    }

pages = sorted((ROOT / 'pages').glob('*.tex'))
assert len(pages) == 8, 'Expected eight page files'
results = [check(p) for p in pages]
assembled = ROOT / 'J156-9-04_transcription.tex'
results.append(check(assembled))
results.append(check(ROOT / 'J156-9-04_standalone.tex'))
source = assembled.read_text()
assert source == ''.join(p.read_text().rstrip() + '\n\n' for p in pages)
assert source.startswith('\\cotefile{156-9}\n\\scanpage{26}')
assert source.count('\\cotefile{156-9}') == 1
assert re.findall(r'\\scanpage\{(\d+)\}', source) == [str(n) for n in range(26, 34)]
assert re.findall(r'\\mspage\{(\d+)\}', source) == [str(n) for n in range(22, 30)]
assert not any(token in source for token in ('\\includegraphics', '\\newcommand', '\\documentclass'))
assert all(r['balanced'] for r in results), results
totals = {k: sum(r['marks'][k] for r in results[:8]) for k in ('unsure', 'illegible', 'deleted')}
report = {'status': 'PASS', 'compiled': False, 'page_count': len(pages),
          'mark_totals_counted_once_in_page_files': totals, 'files': results}
(ROOT / 'J156-9-04_checks.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'status': report['status'], 'pages': len(pages), 'marks': totals, 'compiled': False}))
