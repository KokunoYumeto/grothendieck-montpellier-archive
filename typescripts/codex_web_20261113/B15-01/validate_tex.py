#!/usr/bin/env python3
"""Structural checks only. Does not invoke TeX or compile anything."""
from pathlib import Path
import re
import json

ROOT = Path(__file__).resolve().parent
SCANS = [59, 62, 63, 64, 81, 82, 136, 170, 171, 181, 188]

def check(path):
    source = path.read_text()
    # TeX tokenization sufficient for braces, comments, math delimiters and environments.
    tokens = re.finditer(r"\\[a-zA-Z]+|\\.|%[^\n]*|[{}$]", source)
    braces = []
    environments = []
    display = []
    dollars = []
    errors = []
    for m in tokens:
        token = m.group()
        line = source.count('\n', 0, m.start()) + 1
        if token.startswith('%'):
            continue
        if token == '{':
            braces.append(line)
        elif token == '}':
            if braces:
                braces.pop()
            else:
                errors.append(f'line {line}: unmatched closing brace')
        elif token in (r'\begin', r'\end'):
            arg = re.match(r'\s*\{([^{}]+)\}', source[m.end():])
            if not arg:
                errors.append(f'line {line}: environment name missing')
            else:
                name = arg[1]
                if token == r'\begin':
                    environments.append((name, line))
                elif not environments or environments[-1][0] != name:
                    errors.append(f'line {line}: unmatched end of {name}')
                else:
                    environments.pop()
        elif token == r'\[':
            if display:
                errors.append(f'line {line}: nested display delimiter')
            display.append(line)
        elif token == r'\]':
            if display:
                display.pop()
            else:
                errors.append(f'line {line}: unmatched display close')
        elif token == '$':
            # Nested text-mode dollars in \text are paired by brace depth.
            depth = len(braces)
            if dollars and dollars[-1][0] == depth:
                dollars.pop()
            else:
                dollars.append((depth, line))
    if braces:
        errors.append(f'unclosed braces from lines {braces}')
    if environments:
        errors.append(f'unclosed environments: {environments}')
    if display:
        errors.append(f'unclosed displays from lines {display}')
    if dollars:
        errors.append(f'unclosed dollars: {dollars}')
    return {'file': str(path.relative_to(ROOT)), 'passed': not errors, 'errors': errors}

if __name__ == '__main__':
    files = [ROOT / 'pages' / f'B15-01_15_scan{s:03}.tex' for s in SCANS]
    files += [ROOT / 'B15-01_transcription.tex', ROOT / 'B15-01_standalone.tex']
    checks = [check(p) for p in files]
    assembled = (ROOT / 'B15-01_transcription.tex').read_text()
    pages = ''.join(p.read_text()+'\n' for p in files[:11])
    invariants = {
        'exact_concatenation': assembled == pages,
        'single_initial_cotefile': assembled.startswith(r'\cotefile{15}') and assembled.count(r'\cotefile{15}') == 1,
        'scan_order': [int(x) for x in re.findall(r'\\scanpage\{(\d+)\}', assembled)] == SCANS,
        'no_documentclass_in_fragment': r'\documentclass' not in assembled,
        'no_double_dollar_displays': '$$' not in assembled,
    }
    counts = {name: len(re.findall(r'\\'+name+r'\{', assembled)) for name in ('unsure', 'illegible', 'deleted')}
    result = {'passed': all(c['passed'] for c in checks) and all(invariants.values()),
              'compilation_attempted': False, 'files': checks, 'invariants': invariants,
              'macro_occurrences_in_assembled_fragment': counts}
    (ROOT / 'B15-01_validation.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['passed'] else 1)
