#!/usr/bin/env python3
"""Check the delivered transcription without running a TeX engine."""
from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parent
SCANS = (89, 90, 91, 92, 93, 94, 96, 97, 98)
PAGES = [ROOT / 'pages' / f'B37-05_37_scan{n:03d}.tex' for n in SCANS]
MARKS = ('unsure', 'illegible', 'deleted')


def uncomment(text):
    """Discard comments while respecting escaped percent and backslash."""
    return re.sub(r'\\.|%[^\n]*', lambda m: '' if m[0].startswith('%') else m[0], text)


def check(path):
    text = uncomment(path.read_text(encoding='utf-8'))
    braces, displays, environments, errors = [], [], [], []
    dollars = 0
    for token in re.finditer(r'\\(?:begin|end)\{[^{}]+\}|\\[A-Za-z@]+|\\.|[{}$]', text):
        value = token[0]
        line = text.count('\n', 0, token.start()) + 1
        if value == '{':
            braces.append(line)
        elif value == '}':
            if braces:
                braces.pop()
            else:
                errors.append(f'line {line}: unmatched closing brace')
        elif value == '$':
            dollars += 1
        elif value == r'\[':
            if displays:
                errors.append(f'line {line}: nested display opening')
            displays.append(line)
        elif value == r'\]':
            if displays:
                displays.pop()
            else:
                errors.append(f'line {line}: unmatched display closing')
        elif value.startswith(r'\begin{'):
            environments.append((value[7:-1], line))
        elif value.startswith(r'\end{'):
            name = value[5:-1]
            if not environments or environments[-1][0] != name:
                errors.append(f'line {line}: unmatched environment end {name}')
            else:
                environments.pop()
    errors.extend(f'line {line}: unclosed brace' for line in braces)
    errors.extend(f'line {line}: unclosed display' for line in displays)
    errors.extend(f'line {line}: unclosed environment {name}' for name, line in environments)
    if dollars % 2:
        errors.append('odd number of unescaped dollar delimiters')
    counts = {name: len(re.findall(r'\\' + name + r'\s*\{', text)) for name in MARKS}
    return errors, counts, dollars


def main():
    failures, lines = [], ['B37-05 static balance and delivery checks', 'No TeX compiler invoked.', '']
    totals = dict.fromkeys(MARKS, 0)
    assembled = ROOT / 'B37-05_transcription.tex'
    standalone = ROOT / 'B37-05_standalone.tex'
    for path in PAGES + [assembled, standalone]:
        errors, counts, dollars = check(path)
        lines.append(f'{path.relative_to(ROOT)}: {"FAIL" if errors else "PASS"}; '
                     f'dollars={dollars}; ' + ', '.join(f'{key}={value}' for key, value in counts.items()))
        failures.extend(f'{path.name}: {error}' for error in errors)
        if path in PAGES:
            for key in totals:
                totals[key] += counts[key]
    fragment = assembled.read_bytes()
    if fragment != b''.join(path.read_bytes() for path in PAGES):
        failures.append('Assembly differs from exact ordered concatenation of page files.')
    text = fragment.decode('utf-8')
    if not text.startswith('\\cotefile{37}\n\\scanpage{89}\n'):
        failures.append('Fragment does not begin with the required cote and scan markers.')
    if len(re.findall(r'\\cotefile\{37\}', text)) != 1:
        failures.append('Cote marker is not unique.')
    if tuple(map(int, re.findall(r'\\scanpage\{(\d+)\}', text))) != SCANS:
        failures.append('Scan markers differ from the required order.')
    if re.search(r'\\(?:newcommand|renewcommand|def|documentclass|includegraphics|mathbf|boldsymbol)\b', text):
        failures.append('Unexpected definition, document class, image, or bold macro in fragment.')
    expected = '\\input{PREAMBLE.tex}\n\\begin{document}\n\\input{B37-05_transcription}\n\\end{document}\n'
    if standalone.read_text(encoding='utf-8') != expected:
        failures.append('Standalone wrapper differs from the required content.')
    with (ROOT / 'B37-05_inventory.csv').open(newline='', encoding='utf-8') as stream:
        reader = csv.DictReader(stream)
        expected_fields = 'cote,scan,sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed'.split(',')
        if reader.fieldnames != expected_fields:
            failures.append('Inventory columns differ from the specified columns.')
        rows = list(reader)
    if {int(row['scan']) for row in rows} != set(SCANS):
        failures.append('Inventory scan coverage mismatch.')
    if any(row['transcribed'] != 'yes' or row['cote'] != '37' for row in rows):
        failures.append('Inventory has unfinished or wrong-cote rows.')
    kinds = {'text', 'letter part', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion', 'handwritten'}
    hands = {'typed', 'Grothendieck', 'other hand', 'unknown'}
    sheet_kinds = {'text', 'letter', 'reused_typed', 'cancelled_draft', 'cover'}
    if any(row['kind'] not in kinds or row['hand'] not in hands or row['sheet_kind'] not in sheet_kinds for row in rows):
        failures.append('Inventory contains an unrecognized category.')
    progress = (ROOT / 'progress.log').read_text(encoding='utf-8')
    for scan in SCANS:
        for stage in ('done', 'audited'):
            if not re.search(rf'^scan {scan:03d} {stage} .+$', progress, re.M):
                failures.append(f'Missing scan {scan:03d} {stage} checkpoint.')
    lines.extend(['', f'Inventory: {len(rows)} rows, all transcribed=yes.' if not failures else f'Inventory: {len(rows)} rows.',
                  'Transcription marks (counted once): ' + ', '.join(f'\\{key}={value}' for key, value in totals.items()),
                  'Assembly is an exact byte concatenation in scan order.' if fragment == b''.join(path.read_bytes() for path in PAGES) else 'Assembly mismatch.',
                  'Result: ' + ('FAIL' if failures else 'PASS')])
    lines.extend(failures)
    report = '\n'.join(lines) + '\n'
    (ROOT / 'B37-05_balance_check.txt').write_text(report, encoding='utf-8')
    print(report, end='')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
