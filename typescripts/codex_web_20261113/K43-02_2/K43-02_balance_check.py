"""Static balance checks only. Does not invoke TeX or compile anything."""
from pathlib import Path
import re

def escaped(text, i):
    count = 0
    while i and text[i - 1] == '\\':
        count += 1
        i -= 1
    return count % 2 == 1

def check(path):
    text = '\n'.join(re.split(r'(?<!\\)%', line, 1)[0]
                     for line in path.read_text().splitlines())
    errors, stack, braces, dollars, displays = [], [], 0, 0, 0
    for i, char in enumerate(text):
        if escaped(text, i):
            continue
        if char == '{':
            braces += 1
        elif char == '}':
            braces -= 1
            if braces < 0:
                errors.append('unmatched closing brace')
        elif char == '$':
            dollars += 1
    for match in re.finditer(r'(?<!\\)\\[\[\]]', text):
        displays += 1 if match.group() == r'\[' else -1
        if displays < 0:
            errors.append('unmatched display close')
    for match in re.finditer(r'\\(begin|end)\{([^}]+)\}', text):
        action, name = match.groups()
        if action == 'begin':
            stack.append(name)
        elif not stack or stack.pop() != name:
            errors.append('environment mismatch: ' + name)
    if braces: errors.append('unbalanced braces')
    if dollars % 2: errors.append('odd number of dollar delimiters')
    if displays: errors.append('unbalanced display delimiters')
    if stack: errors.append('unclosed environments: ' + ', '.join(stack))
    return errors

if __name__ == '__main__':
    paths = sorted((Path(__file__).parent / 'pages').glob('*.tex'))
    assert len(paths) == 15
    failed = False
    for path in paths:
        errors = check(path)
        failed |= bool(errors)
        print(path.name + ': ' + ('; '.join(errors) if errors else 'PASS'))
    raise SystemExit(1 if failed else 0)
