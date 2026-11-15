#!/usr/bin/env python3
"""Check source balance without compiling or changing the transcription."""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
TOKEN = re.compile(r'\\begin\{([^}]+)\}|\\end\{([^}]+)\}|\\[A-Za-z]+|\\.|[{}$]', re.S)


def strip_comments(source):
    return re.sub(r'(?<!\\)%[^\n]*', '', source)


def check(source):
    source = strip_comments(source)
    braces, environments, math = [], [], []
    errors = []
    for match in TOKEN.finditer(source):
        token = match[0]
        line = source[:match.start()].count('\n') + 1
        if match[1]:
            environments.append((match[1], line))
        elif match[2]:
            if not environments or environments[-1][0] != match[2]:
                errors.append(f'line {line}: unmatched end {match[2]}')
            else:
                environments.pop()
        elif token == '{':
            braces.append(line)
        elif token == '}':
            if braces:
                braces.pop()
            else:
                errors.append(f'line {line}: unmatched closing brace')
        elif token in (r'\[', r'\('):
            if math:
                errors.append(f'line {line}: nested math delimiter {token}')
            math.append((token, line))
        elif token in (r'\]', r'\)'):
            expected = {r'\]': r'\[', r'\)': r'\('}[token]
            if not math or math[-1][0] != expected:
                errors.append(f'line {line}: unmatched math delimiter {token}')
            else:
                math.pop()
        elif token == '$':
            if math and math[-1][0] == '$':
                math.pop()
            elif math:
                errors.append(f'line {line}: dollar delimiter inside display')
            else:
                math.append(('$', line))
    errors.extend(f'line {line}: unclosed brace' for line in braces)
    errors.extend(f'line {line}: unclosed environment {name}' for name, line in environments)
    errors.extend(f'line {line}: unclosed math delimiter {name}' for name, line in math)
    for match in re.finditer(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}', source, re.S):
        if r'ampersand replacement=\&' not in match[1]:
            errors.append('tikzcd lacks ampersand replacement')
        if re.search(r'(?<!\\)&', match[1]):
            errors.append('tikzcd has an unescaped ampersand')
    return errors


def main():
    pages = sorted((ROOT / 'pages').glob('*.tex'))
    expected = [f'J156-9-06_156-9_scan{scan:03}.tex' for scan in range(42, 50)]
    errors = []
    report = {'compiled': False, 'pages': [], 'counts': {}, 'checks': {}}
    if [p.name for p in pages] != expected:
        errors.append('page file list differs from expected scans 42–49')
    for page in pages:
        failures = check(page.read_text())
        report['pages'].append({'file': page.name, 'balanced': not failures, 'errors': failures})
        errors.extend(f'{page.name}: {failure}' for failure in failures)
    assembled_path = ROOT / 'J156-9-06_transcription.tex'
    assembled = assembled_path.read_text()
    combined = ''.join(page.read_text() for page in pages)
    report['checks']['exact_concatenation'] = assembled == combined
    report['checks']['one_cotefile_at_start'] = (
        assembled.startswith(r'\cotefile{156-9}') and assembled.count(r'\cotefile{') == 1
    )
    report['checks']['scan_order'] = re.findall(r'\\scanpage\{(\d+)\}', assembled) == list(map(str, range(42, 50)))
    report['checks']['assembled_balanced'] = not check(assembled)
    report['checks']['standalone_balanced'] = not check((ROOT / 'J156-9-06_standalone.tex').read_text())
    report['checks']['no_images_or_custom_notation_macros'] = not re.search(
        r'\\(?:includegraphics|newcommand|renewcommand|def)\b', assembled
    )
    with (ROOT / 'J156-9-06_inventory.csv').open(newline='') as handle:
        inventory = list(csv.DictReader(handle))
    report['checks']['all_inventory_elements_transcribed'] = all(row['transcribed'] == 'yes' for row in inventory)
    report['checks']['inventory_scan_coverage'] = sorted({int(row['scan']) for row in inventory}) == list(range(42, 50))
    report['inventory_rows'] = len(inventory)
    for name in ('unsure', 'illegible', 'deleted', 'inserted', 'margin', 'diagram', 'figure'):
        report['counts'][name] = len(re.findall(r'\\' + name + r'\{', assembled))
    for name, passed in report['checks'].items():
        if not passed:
            errors.append('failed check: ' + name)
    report['sha256'] = {
        str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in [*pages, assembled_path]
    }
    report['passed'] = not errors
    report['errors'] = errors
    (ROOT / 'J156-9-06_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    for page in report['pages']:
        print(f"{page['file']}: {'PASS' if page['balanced'] else 'FAIL'}")
    print('Assembled / standalone / inventory:', 'PASS' if all(report['checks'].values()) else 'FAIL')
    print('Marks:', json.dumps(report['counts']))
    print('Compilation: not attempted')
    for error in errors:
        print(error)
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
