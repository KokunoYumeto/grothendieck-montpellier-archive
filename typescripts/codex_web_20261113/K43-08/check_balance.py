"""Structural checks only; deliberately does not invoke a TeX engine."""
from pathlib import Path
import json
import re

SCANS = [161, 162, 163, 164, 165, 167, 168, 169, 170, 171, 172, 173, 174, 176, 177]

def without_comments(source):
    result = []
    for line in source.splitlines(keepends=True):
        i = 0
        while i < len(line):
            if line[i] == '\\':
                result.append(line[i:i+2]); i += 2
            elif line[i] == '%':
                result.append('\n'); break
            else:
                result.append(line[i]); i += 1
    return ''.join(result)

def check(path):
    s = without_comments(path.read_text())
    braces, displays, envs, errors = [], [], [], []
    dollars = 0
    i = 0
    while i < len(s):
        c = s[i]
        line = s.count('\n', 0, i) + 1
        if c == '\\':
            m = re.match(r'\\(begin|end)\{([^{}]+)\}', s[i:])
            if m:
                action, env = m.groups()
                if action == 'begin': envs.append((env, line))
                elif not envs or envs[-1][0] != env:
                    errors.append(f'line {line}: unexpected end of {env}')
                else: envs.pop()
                i += len(m.group()); continue
            if s[i:i+2] == r'\[': displays.append(line)
            elif s[i:i+2] == r'\]':
                if displays: displays.pop()
                else: errors.append(f'line {line}: unmatched display close')
            m = re.match(r'\\[A-Za-z]+|\\.', s[i:], re.S)
            i += len(m.group()) if m else 1
            continue
        if c == '{': braces.append(line)
        elif c == '}':
            if braces: braces.pop()
            else: errors.append(f'line {line}: unmatched closing brace')
        elif c == '$': dollars += 1
        i += 1
    if braces: errors.append(f'unclosed braces at lines {braces}')
    if displays: errors.append(f'unclosed displays at lines {displays}')
    if envs: errors.append(f'unclosed environments {envs}')
    if dollars % 2: errors.append('odd number of unescaped dollar delimiters')
    return {'file': str(path.name), 'balanced': not errors,
            'dollar_delimiters': dollars, 'errors': errors}

def main():
    root = Path(__file__).resolve().parent
    files = [root / 'pages' / f'K43-08_43_scan{n}.tex' for n in SCANS]
    files += [root / 'K43-08_transcription.tex', root / 'K43-08_standalone.tex']
    report = {'scope': 'Braces, display delimiters, dollar parity, and properly nested environments. No compilation or visual layout validation.',
              'files': [check(p) for p in files]}
    source = (root / 'K43-08_transcription.tex').read_text()
    report['scan_order'] = list(map(int, re.findall(r'\\scanpage\{(\d+)\}', source)))
    report['cote_marks'] = source.count(r'\cotefile{43}')
    report['counts'] = {m: len(re.findall(r'\\' + m + r'\{', source))
                        for m in ['unsure', 'illegible', 'deleted']}
    report['all_passed'] = (all(x['balanced'] for x in report['files']) and
                            report['scan_order'] == SCANS and report['cote_marks'] == 1 and
                            source.startswith(r'\cotefile{43}'))
    (root / 'K43-08_balance.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report['all_passed'] else 1)

if __name__ == '__main__': main()
