#!/usr/bin/env python3
"""Check source delimiters only; never invokes a TeX engine."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
ID = 'J156-9-18'


def uncomment(source):
    lines = []
    for line in source.splitlines(keepends=True):
        for i, ch in enumerate(line):
            if ch == '%':
                j = i - 1
                while j >= 0 and line[j] == '\\':
                    j -= 1
                if (i - j - 1) % 2 == 0:
                    line = line[:i] + '\n'
                    break
        lines.append(line)
    return ''.join(lines)


def balance(path):
    text = uncomment(path.read_text())
    braces = []
    math = None
    envs = []
    errors = []
    dollars = displays = environments = 0
    i = 0
    while i < len(text):
        ch = text[i]
        line = text.count('\n', 0, i) + 1
        if ch == '\\':
            env = re.match(r'\\(begin|end)\{([^{}]+)\}', text[i:])
            if env:
                kind, name = env.groups()
                if kind == 'begin':
                    envs.append((name, line))
                    environments += 1
                elif not envs or envs[-1][0] != name:
                    errors.append(f'line {line}: mismatched end {name}')
                else:
                    envs.pop()
                i += len(env.group())
                continue
            if i + 1 < len(text) and text[i+1] in '[]':
                sign = text[i+1]
                if sign == '[':
                    if math is not None:
                        errors.append(f'line {line}: display opened inside {math}')
                    math = 'display'
                    displays += 1
                elif math != 'display':
                    errors.append(f'line {line}: unmatched display close')
                else:
                    math = None
                i += 2
                continue
            cmd = re.match(r'\\[A-Za-z]+', text[i:])
            i += len(cmd.group()) if cmd else 2
            continue
        if ch == '{':
            braces.append(line)
        elif ch == '}':
            if not braces:
                errors.append(f'line {line}: unmatched grouping brace')
            else:
                braces.pop()
        elif ch == '$':
            dollars += 1
            if math == 'display':
                errors.append(f'line {line}: dollar delimiter inside display')
            elif math == 'inline':
                math = None
            else:
                math = 'inline'
        i += 1
    if braces:
        errors.append(f'unclosed grouping braces from lines {braces}')
    if math:
        errors.append(f'unclosed {math} math')
    if envs:
        errors.append(f'unclosed environments {envs}')
    return {'file': str(path.relative_to(ROOT)), 'status': 'PASS' if not errors else 'FAIL',
            'dollar_delimiters': dollars, 'display_pairs': displays,
            'environment_pairs': environments, 'errors': errors}


def main():
    paths = sorted((ROOT / 'pages').glob('*.tex'))
    assert len(paths) == 7
    fragment_path = ROOT / f'{ID}_transcription.tex'
    results = [balance(p) for p in paths + [fragment_path, ROOT / f'{ID}_standalone.tex']]
    assert all(r['status'] == 'PASS' for r in results), results
    fragment = fragment_path.read_text()
    expected = '\n'.join(p.read_text().rstrip() + '\n' for p in paths)
    assert fragment == expected, 'assembled fragment differs from page concatenation'
    assert fragment.startswith('\\cotefile{156-9}\n\\scanpage{134}')
    assert fragment.count('\\cotefile{') == 1
    assert re.findall(r'\\scanpage\{(\d+)\}', fragment) == [str(n) for n in range(134, 141)]
    assert re.findall(r'\\mspage\{(\d+)\}', fragment) == [str(n) for n in range(5, 12)]
    assert fragment.count('% archive sheet number:') == 7
    assert '\\includegraphics' not in fragment and '\\newcommand' not in fragment
    assert '\\documentclass' not in fragment
    with (ROOT / f'{ID}_inventory.csv').open(newline='') as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ['cote','scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
        rows = list(reader)
    assert all(r['transcribed'] == 'yes' for r in rows)
    assert {r['scan'] for r in rows} == {str(n) for n in range(134,141)}
    assert len({r['element'] for r in rows}) == len(rows)
    counts = {name: fragment.count('\\' + name + '{') for name in ['unsure','illegible','deleted']}
    report = ['Delimiter and environment checks: PASS',
              'No LaTeX compilation attempted.',
              'Source parentheses and literal mathematical delimiters are not normalized.', '']
    for result in results:
        report.append(f"{result['file']}: {result['status']}; braces balanced; "
                      f"{result['dollar_delimiters']} dollar delimiters; "
                      f"{result['display_pairs']} display pairs; "
                      f"{result['environment_pairs']} environment pairs")
    report += ['', 'Assembled fragment equals exact page-order concatenation: PASS',
               'Cote marker exactly once; scan markers 134–140; manuscript numbers 5–11: PASS',
               'Seven archive-number comments; no scan-image includes or custom macro definitions: PASS',
               f"Inventory: {len(rows)} distinct element rows, all transcribed=yes: PASS",
               'Marks in assembled fragment: ' + ', '.join(f'{k}={v}' for k,v in counts.items()),
               'Pages finished and audited: 134, 135, 136, 137, 138, 139, 140',
               'Unfinished pages: none', '']
    report_text = '\n'.join(report)
    (ROOT / f'{ID}_balance_check.txt').write_text(report_text)
    print(report_text)
    return results, counts


if __name__ == '__main__':
    main()
