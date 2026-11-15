"""Structural checks only. Does not invoke TeX, OCR, or any network service."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parent

def check(path):
    text = path.read_text(encoding='utf-8')
    braces, envs, math = [], [], []
    errors = []
    i = 0
    line = 1
    while i < len(text):
        c = text[i]
        if c == '\n':
            line += 1
            i += 1
            continue
        if c == '%':
            end = text.find('\n', i)
            i = len(text) if end < 0 else end
            continue
        if c == '\\':
            match = re.match(r'\\(begin|end)\{([^{}]+)\}', text[i:])
            if match:
                action, name = match.groups()
                if action == 'begin':
                    envs.append((name, line))
                elif not envs or envs[-1][0] != name:
                    errors.append(f'line {line}: mismatched end of {name}')
                else:
                    envs.pop()
                i += match.end()
                continue
            match = re.match(r'\\[A-Za-z@]+|\\.', text[i:])
            if match:
                command = match.group()
                if command in (r'\[', r'\('):
                    if math:
                        errors.append(f'line {line}: nested math delimiter {command}')
                    math.append((command, line))
                elif command in (r'\]', r'\)'):
                    expected = {r'\]': r'\[', r'\)': r'\('}[command]
                    if not math or math[-1][0] != expected:
                        errors.append(f'line {line}: unmatched {command}')
                    else:
                        math.pop()
                i += match.end()
                continue
        if c == '{':
            braces.append(line)
        elif c == '}':
            if not braces:
                errors.append(f'line {line}: unmatched closing brace')
            else:
                braces.pop()
        elif c == '$':
            delimiter = '$$' if text[i:i+2] == '$$' else '$'
            if math and math[-1][0] == delimiter:
                math.pop()
            else:
                if math:
                    errors.append(f'line {line}: dollar inside another math delimiter')
                math.append((delimiter, line))
            i += len(delimiter)
            continue
        i += 1
    if braces:
        errors.append(f'unclosed braces opened on lines {braces}')
    if envs:
        errors.append(f'unclosed environments: {envs}')
    if math:
        errors.append(f'unclosed math delimiters: {math}')
    return errors

def main():
    paths = sorted((ROOT/'pages').glob('*.tex')) + [
        ROOT/'J156-7-11_transcription.tex',
        ROOT/'J156-7-11_standalone.tex',
    ]
    failed = False
    print('Checks: unescaped braces, inline/display math delimiters, environment stack.')
    for path in paths:
        errors = check(path)
        failed |= bool(errors)
        print(f'{path.relative_to(ROOT)}: '+('FAIL' if errors else 'PASS'))
        for error in errors:
            print('  '+error)
    print('No compilation attempted. Macro expansion, layout and mathematical correctness are outside this structural check.')
    return int(failed)

if __name__ == '__main__':
    sys.exit(main())
