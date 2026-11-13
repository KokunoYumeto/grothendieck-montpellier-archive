"""Check delimiters and environments only. This does not invoke TeX."""
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parent

def strip_comments(text):
    return '\n'.join(re.split(r'(?<!\\)%', line, 1)[0] for line in text.splitlines())

def check(path):
    s = strip_comments(path.read_text())
    braces = []; displays = []; inline = False; errors = []; i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            nxt = s[i+1:i+2]
            if nxt == '[':
                displays.append(i); i += 2; continue
            if nxt == ']':
                if displays: displays.pop()
                else: errors.append('unmatched display close')
                i += 2; continue
            if nxt in ('{', '}', '$', '%', '\\'):
                i += 2; continue
        elif c == '{': braces.append(i)
        elif c == '}':
            if braces: braces.pop()
            else: errors.append('unmatched closing brace')
        elif c == '$': inline = not inline
        i += 1
    if braces: errors.append(f'{len(braces)} unclosed braces')
    if displays: errors.append(f'{len(displays)} unclosed displays')
    if inline: errors.append('unpaired dollar')
    envs = []
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}', s):
        action, name = m.groups()
        if action == 'begin': envs.append(name)
        elif not envs or envs.pop() != name: errors.append('mismatched environment ' + name)
    if envs: errors.append('unclosed environments: ' + ', '.join(envs))
    return errors

paths = sorted((root / 'pages').glob('*.tex')) + [root / 'B10-05_transcription.tex', root / 'B10-05_standalone.tex']
failed = False
for p in paths:
    errors = check(p)
    failed |= bool(errors)
    print(p.relative_to(root), ':', '; '.join(errors) if errors else 'PASS — braces, displays, dollars, environments balanced')
print('No compilation performed. Prose/mathematical parentheses and readings are not normalized by this check.')
sys.exit(1 if failed else 0)
