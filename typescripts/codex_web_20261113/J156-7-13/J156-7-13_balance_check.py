#!/usr/bin/env python3
"""Static checks only. Never invokes a TeX engine."""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parent

def strip_comments(s):
    return re.sub(r'(?<!\\)%[^\n]*','',s)

def check(path):
    s=strip_comments(path.read_text())
    errors=[];stack=[]
    # Tokenize control words and escaped characters before structural braces.
    for m in re.finditer(r'\\[A-Za-z]+\*?|\\.|[{}$]',s,re.S):
        tok=m.group();line=s.count('\n',0,m.start())+1
        if tok=='{':stack.append(line)
        elif tok=='}':
            if stack:stack.pop()
            else:errors.append(f'unmatched closing brace at line {line}')
    if stack:errors.append('unclosed braces at lines '+str(stack))
    displays=[]
    for m in re.finditer(r'\\\[|\\\]',s):
        if m.group()==r'\[':displays.append(m.start())
        elif displays:displays.pop()
        else:errors.append('unmatched display close')
    if displays:errors.append('unclosed display delimiters')
    dollars=len(re.findall(r'(?<!\\)\$',s))
    if dollars%2:errors.append('odd number of dollar delimiters')
    env=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        action,name=m.groups()
        if action=='begin':env.append(name)
        elif not env or env[-1]!=name:errors.append('mismatched environment end '+name)
        else:env.pop()
    if env:errors.append('unclosed environments '+str(env))
    lr=[]
    for m in re.finditer(r'\\(left|right)\b',s):
        if m.group(1)=='left':lr.append(m.start())
        elif lr:lr.pop()
        else:errors.append('right delimiter without left')
    if lr:errors.append('left delimiter without right')
    if re.search(r'\\(?:newcommand|renewcommand|def)\b',s):errors.append('custom macro definition in transcription')
    for body in re.findall(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}',s,re.S):
        if r'ampersand replacement=\&' not in body:errors.append('tikzcd ampersand option missing')
        if re.search(r'(?<!\\)&',body):errors.append('unescaped tikzcd cell separator')
    return {'file':str(path.relative_to(ROOT)),'braces':'pass' if not stack and not any('brace' in e for e in errors) else 'fail',
            'display_pairs':len(re.findall(r'\\\[',s)), 'dollar_pairs':dollars//2,
            'environment_pairs':len(re.findall(r'\\begin\{',s)),'errors':errors,'result':'pass' if not errors else 'fail'}

pages=sorted((ROOT/'pages').glob('J156-7-13_156-7_scan*.tex'))
results=[check(p) for p in pages]
fragment=ROOT/'J156-7-13_transcription.tex'
results.append(check(fragment))
assert fragment.read_text()==''.join(p.read_text() for p in pages),'Fragment is not exact concatenation'
assert fragment.read_text().count(r'\cotefile{156-7}')==1
assert re.findall(r'\\scanpage\{(\d+)\}',fragment.read_text())==[str(n) for n in range(101,108)]
assert len(pages)==7
counts={cmd:len(re.findall(r'\\'+cmd+r'\{',fragment.read_text())) for cmd in ['unsure','illegible','deleted']}
report={'method':'static lexical checks; no TeX compilation','pages':results,'marks_in_assembled_fragment':counts,
        'exact_concatenation':True,'all_pages_present':True,'result':'pass' if all(r['result']=='pass' for r in results) else 'fail'}
(ROOT/'J156-7-13_balance_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
if report['result']!='pass':raise SystemExit(1)
