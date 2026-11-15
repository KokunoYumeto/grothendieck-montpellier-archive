"""Syntax-only check; never invokes TeX. Run from any working directory."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent


def uncomment(source):
    lines = []
    for line in source.splitlines():
        for i, ch in enumerate(line):
            if ch == '%':
                j = i - 1
                while j >= 0 and line[j] == '\\':
                    j -= 1
                if (i - j - 1) % 2 == 0:
                    line = line[:i]
                    break
        lines.append(line)
    return '\n'.join(lines)


TOKEN = re.compile(r'\\(?:begin|end)\{[^}]+\}|\\[\[\]()]|\\[$%{}\\]|[{}$]')


def check(path):
    source = uncomment(path.read_text())
    braces, envs, math = [], [], []
    for match in TOKEN.finditer(source):
        token = match.group()
        line = source.count('\n', 0, match.start()) + 1
        if token == '{':
            braces.append(line)
        elif token == '}':
            assert braces, f'{path.name}:{line}: unmatched closing brace'
            braces.pop()
        elif token.startswith('\\begin{'):
            envs.append((token[7:-1], line))
        elif token.startswith('\\end{'):
            assert envs and envs[-1][0] == token[5:-1], (path.name, line, token, envs)
            envs.pop()
        elif token in ('\\[', '\\('):
            assert not math, (path.name, line, 'nested math delimiter', math)
            math.append((token, line))
        elif token in ('\\]', '\\)'):
            opening = '\\[' if token == '\\]' else '\\('
            assert math and math[-1][0] == opening, (path.name, line, token, math)
            math.pop()
        elif token == '$':
            if math:
                assert math[-1][0] == '$', (path.name, line, 'dollar in delimited math')
                math.pop()
            else:
                math.append(('$', line))
    assert not braces, (path.name, 'unclosed braces', braces)
    assert not envs, (path.name, 'unclosed environments', envs)
    assert not math, (path.name, 'unclosed math', math)
    assert '$$' not in source, (path.name, 'non-prescribed display delimiter')
    for match in re.finditer(r'\\begin\{tikzcd\}\[([^\]]*)\]', source):
        assert 'ampersand replacement=\\&' in match[1], (path.name, 'tikzcd ampersands')
    return f'PASS {path.relative_to(ROOT)}: braces, math delimiters, environments'


if __name__ == '__main__':
    files = sorted((ROOT / 'pages').glob('*.tex'))
    files += [ROOT / 'J156-7-12_transcription.tex', ROOT / 'J156-7-12_standalone.tex']
    for path in files:
        print(check(path))
    print('Syntax-only checks passed. No TeX compilation was performed.')
