"""Structural checks only; deliberately does not invoke TeX or compile."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

def uncomment(s):
    return re.sub(r'(?<!\\)%[^\n]*', '', s)

def check(path):
    s = uncomment(path.read_text())
    tokens = re.finditer(r'\\\\|\\(?:begin|end)\{[^}]+\}|\\[\[\]()]|\\[{}$%]|(?<!\\)[{}$]', s)
    braces = []
    envs = []
    maths = []
    issues = []
    for match in tokens:
        t = match.group()
        line = s.count('\n', 0, match.start()) + 1
        if t.startswith('\\begin{'):
            envs.append((t[7:-1], line))
        elif t.startswith('\\end{'):
            name = t[5:-1]
            if not envs or envs[-1][0] != name:
                issues.append(f'line {line}: unmatched {t}')
            else:
                envs.pop()
        elif t == '{':
            braces.append(line)
        elif t == '}':
            if braces:
                braces.pop()
            else:
                issues.append(f'line {line}: unmatched closing brace')
        elif t == '$':
            if maths and maths[-1][0] == '$':
                maths.pop()
            else:
                maths.append(('$', line))
        elif t in (r'\[', r'\('):
            maths.append((t, line))
        elif t in (r'\]', r'\)'):
            wanted = {r'\]': r'\[', r'\)': r'\('}[t]
            if maths and maths[-1][0] == wanted:
                maths.pop()
            else:
                issues.append(f'line {line}: unmatched {t}')
    if braces:
        issues.append(f'unclosed braces opened at lines {braces}')
    if envs:
        issues.append(f'unclosed environments {envs}')
    if maths:
        issues.append(f'unclosed math delimiters {maths}')
    return issues

def main():
    paths = sorted((ROOT / 'pages').glob('*.tex')) + [ROOT / 'K43-10_transcription.tex', ROOT / 'K43-10_standalone.tex']
    problems = 0
    print('Structural balance: braces, dollar math, display/inline delimiters, nested environments.')
    print('No TeX engine invoked; this is not a compilation or a layout check.')
    for path in paths:
        issues = check(path)
        problems += len(issues)
        print(str(path.relative_to(ROOT)) + ': ' + ('PASS' if not issues else 'FAIL — ' + '; '.join(issues)))
    print(f'Checked {len(paths)} files; {problems} structural errors.')
    return bool(problems)

if __name__ == '__main__':
    sys.exit(main())
