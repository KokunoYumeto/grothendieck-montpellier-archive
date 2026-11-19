"""Static balance/command check only. This script does not compile LaTeX."""
from pathlib import Path
import collections
import json
import re

ROOT = Path(__file__).resolve().parent
ALLOWED = set('''Longrightarrow Psi alpha approx approxeq arrow backslash begin beta
big bigl bigr circ cong cotefile cup deleted delta diagram end forall gamma geq
hookrightarrow illegible in inserted kappa lambda ldots leq lim longleftrightarrow
longmapsto longrightarrow margin mathcal mathrel mathrm mathscr mspage ne ni
operatorname overline overset pi prime prod psi qquad quad rule scanpage simeq
subset substack tag text textcircled times uline underbrace underline unsure
uuline varepsilon varinjlim varphi vphantom widehat xi xrightarrow'''.split())

def check(path):
    s = re.sub(r'(?m)(?<!\\)%.*$', '', path.read_text())
    errors, stack, displays = [], [], []
    dollar_count = 0
    for match in re.finditer(r'\\[A-Za-z]+|\\.|[{}$]', s):
        token = match.group()
        if token == '{': stack.append(match.start())
        elif token == '}':
            if stack: stack.pop()
            else: errors.append('unmatched closing brace')
        elif token == r'\[': displays.append(match.start())
        elif token == r'\]':
            if displays: displays.pop()
            else: errors.append('unmatched display close')
        elif token == '$': dollar_count += 1
    if stack: errors.append(f'{len(stack)} unclosed braces')
    if displays: errors.append(f'{len(displays)} unclosed displays')
    if dollar_count % 2: errors.append('odd number of unescaped dollar delimiters')
    if '$$' in s: errors.append('unexpected double-dollar math delimiter')
    environments = []
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}', s):
        action, env = m.groups()
        if env not in {'aligned', 'tikzcd'}: errors.append('unexpected environment '+env)
        if action == 'begin': environments.append(env)
        elif not environments or environments.pop() != env:
            errors.append('mismatched environment '+env)
    if environments: errors.append('unclosed environments '+repr(environments))
    commands = set(re.findall(r'\\([A-Za-z]+)', s))
    unknown = sorted(commands - ALLOWED)
    if unknown: errors.append('unknown commands: '+', '.join(unknown))
    for m in re.finditer(r'\\begin\{tikzcd\}(\[[^\]]*\])?', s):
        if 'ampersand replacement=\\&' not in (m.group(1) or ''):
            errors.append('tikzcd missing ampersand replacement')
    counts = {name:len(re.findall(r'\\'+name+r'\{',s))
              for name in ('unsure','illegible','deleted','inserted','margin','diagram')}
    return {'file':str(path.relative_to(ROOT)), 'status':'PASS' if not errors else 'FAIL',
            'errors':errors, 'dollar_delimiters':dollar_count,
            'display_pairs':len(re.findall(r'\\\[',s)), 'commands':sorted(commands),
            'marks':counts}

pages = sorted((ROOT/'pages').glob('K157-5-11_157-5_scan*.tex'))
assert [int(re.search(r'scan(\d+)',p.name).group(1)) for p in pages] == list(range(165,181))
fragment = ROOT/'K157-5-11_transcription.tex'
assert fragment.read_bytes() == b''.join(p.read_bytes() for p in pages), 'fragment differs from concatenation'
combined = fragment.read_text()
assert combined.startswith('\\cotefile{157-5}\n\\scanpage{165}')
assert combined.count('\\cotefile{') == 1
assert re.findall(r'\\scanpage\{(\d+)\}',combined) == [str(n) for n in range(165,181)]
assert '\\documentclass' not in combined and '\\input' not in combined
results = [check(p) for p in pages] + [check(fragment)]
totals = dict(sum((collections.Counter(r['marks']) for r in results[:-1]),collections.Counter()))
report = {'scope':'Static balance and known-command check, no compilation or rendering',
          'status':'PASS' if all(r['status']=='PASS' for r in results) else 'FAIL',
          'page_count':len(pages), 'exact_concatenation':True,
          'marks_in_page_files_only':totals, 'files':results}
(ROOT/'K157-5-11_syntax_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='files'},ensure_ascii=False,indent=2))
for r in results:
    if r['errors']: print(r['file'],r['errors'])
raise SystemExit(0 if report['status']=='PASS' else 1)
