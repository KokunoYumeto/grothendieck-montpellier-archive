"""Structural checks only. This script does not invoke a TeX compiler."""
from pathlib import Path
import re
import csv
import json

ROOT = Path(__file__).resolve().parent

def check(path):
    text = path.read_text(encoding='utf-8')
    braces = []
    envs = []
    mode = None
    errors = []
    counts = {'brace_pairs': 0, 'inline_math_pairs': 0,
              'display_math_pairs': 0, 'environment_pairs': 0}
    i = 0
    while i < len(text):
        c = text[i]
        if c == '%':
            end = text.find('\n', i)
            i = len(text) if end < 0 else end + 1
            continue
        if c == '\\':
            m = re.match(r'\\(begin|end)\{([A-Za-z*]+)\}', text[i:])
            if m:
                action, name = m.groups()
                if action == 'begin':
                    envs.append((name, i))
                elif not envs or envs[-1][0] != name:
                    errors.append(f'mismatched environment {name} at {i}')
                else:
                    envs.pop()
                    counts['environment_pairs'] += 1
                i += len(m.group(0))
                continue
            if text[i:i+2] == r'\[':
                if mode is not None: errors.append(f'display opens in {mode} at {i}')
                mode = 'display'
                i += 2
                continue
            if text[i:i+2] == r'\]':
                if mode != 'display': errors.append(f'display closes in {mode} at {i}')
                else: counts['display_math_pairs'] += 1
                mode = None
                i += 2
                continue
            # An escaped non-letter token cannot act as a delimiter.
            if i+1 < len(text) and not text[i+1].isalpha():
                i += 2
                continue
            i += 1
            continue
        if c == '{': braces.append(i)
        elif c == '}':
            if not braces: errors.append(f'extra closing brace at {i}')
            else:
                braces.pop()
                counts['brace_pairs'] += 1
        elif c == '$':
            if mode == 'display': errors.append(f'dollar inside display at {i}')
            elif mode == 'inline':
                mode = None
                counts['inline_math_pairs'] += 1
            else: mode = 'inline'
        i += 1
    if braces: errors.append(f'{len(braces)} unclosed braces')
    if envs: errors.append(f'unclosed environments: {envs}')
    if mode: errors.append(f'unclosed {mode} math')
    return {'file': str(path.relative_to(ROOT)), 'balanced': not errors,
            **counts, 'errors': errors}

def main():
    pages = [ROOT/'pages'/f'B10-09_10_scan{n}.tex' for n in range(123,131)]
    fragment = ROOT/'B10-09_transcription.tex'
    results = [check(p) for p in pages+[fragment,ROOT/'B10-09_standalone.tex']]
    text = fragment.read_text()
    rows = list(csv.DictReader((ROOT/'B10-09_inventory.csv').open(newline='')))
    checks = {
        'all_files_balanced': all(r['balanced'] for r in results),
        'exact_page_concatenation': fragment.read_bytes() == b''.join(p.read_bytes() for p in pages),
        'one_cotefile_at_start': text.startswith(r'\cotefile{10}') and text.count(r'\cotefile{') == 1,
        'scan_order': re.findall(r'\\scanpage\{(\d+)\}',text) == [str(n) for n in range(123,131)],
        'all_inventory_rows_transcribed': all(r['transcribed']=='yes' for r in rows),
        'all_scans_in_inventory': sorted({int(r['scan']) for r in rows}) == list(range(123,131)),
        'no_custom_notation_definitions': not re.search(r'\\(?:newcommand|renewcommand|def|let)\b',text),
        'cross_page_word_join': bool(re.search(r'préli%\n\\scanpage\{130\}%\n(?:%[^\n]*\n)*minaire',text)),
    }
    report = {
        'scope': 'Structural balance and packaging checks; no TeX compilation.',
        'checks': checks, 'files': results,
        'mark_counts': {name:len(re.findall(r'\\'+name+r'\{',text)) for name in ('unsure','illegible','deleted')},
        'inventory_rows': len(rows), 'unfinished_scans': []
    }
    (ROOT/'B10-09_balance_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    raise SystemExit(0 if all(checks.values()) else 1)

if __name__ == '__main__': main()
