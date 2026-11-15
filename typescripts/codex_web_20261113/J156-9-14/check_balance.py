"""Static LaTeX delimiter checks only; does not invoke a TeX engine."""
from pathlib import Path
import re
import sys

def escaped(text, i):
    j = i
    while j and text[j-1] == '\\':
        j -= 1
    return (i-j) % 2 == 1

def uncomment(text):
    lines = []
    for line in text.splitlines():
        cut = next((i for i,c in enumerate(line) if c == '%' and not escaped(line,i)), len(line))
        lines.append(line[:cut])
    return '\n'.join(lines)

def check(path):
    s = uncomment(path.read_text())
    errors = []
    braces = []
    for i,c in enumerate(s):
        if escaped(s,i):
            continue
        if c == '{':
            braces.append(i)
        elif c == '}':
            if braces: braces.pop()
            else: errors.append('unmatched closing brace')
    if braces: errors.append(f'{len(braces)} unclosed brace(s)')
    math = None
    for m in re.finditer(r'\\\[|\\\]|\$\$|\$',s):
        if escaped(s,m.start()):
            continue
        t = m.group()
        if t == r'\[':
            if math: errors.append('display opens inside math')
            math = t
        elif t == r'\]':
            if math != r'\[': errors.append('display close without open')
            math = None
        elif math is None:
            math = t
        elif math == t:
            math = None
        else:
            errors.append('inconsistent dollar/display delimiters')
    if math: errors.append(f'unclosed math delimiter {math}')
    envs = []
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        action,name = m.groups()
        if action == 'begin': envs.append(name)
        elif not envs or envs.pop() != name: errors.append(f'environment mismatch: {name}')
    if envs: errors.append('unclosed environments: '+','.join(envs))
    return errors

if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    paths = sorted((root/'pages').glob('*.tex'))
    paths += [root/'J156-9-14_transcription.tex', root/'J156-9-14_standalone.tex']
    failed = False
    for path in paths:
        errors = check(path)
        failed |= bool(errors)
        print(str(path.relative_to(root))+': '+('; '.join(errors) if errors else 'PASS — braces, display delimiters, dollars, environments'))
    sys.exit(1 if failed else 0)
