#!/usr/bin/env python3
"""Static delimiter check only. Does not compile LaTeX or assess readings."""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parent

def tokens(s):
    # TeX control sequences are tokens: escaped braces/dollars/percent do not count.
    return list(re.finditer(r'\\(?:[A-Za-z]+|.)|%[^\n]*|[{}$]|[^\\%{}$]+',s))

def check(p):
    s=p.read_text(); brace=[]; disp=[]; env=[]; dollar=[]; errors=[]
    def line(i):return s.count('\n',0,i)+1
    for m in tokens(s):
        t=m.group();n=line(m.start())
        if t.startswith('%'):continue
        if t=='{':brace.append(n)
        elif t=='}':
            if brace:brace.pop()
            else:errors.append(f'line {n}: unmatched closing brace')
        elif t=='\\[':disp.append(n)
        elif t=='\\]':
            if disp:disp.pop()
            else:errors.append(f'line {n}: unmatched display close')
        elif t=='$':
            if dollar:dollar.pop()
            else:dollar.append(n)
        elif t in ['\\begin','\\end']:
            e=re.match(r'\s*\{([^{}]+)\}',s[m.end():])
            if not e:errors.append(f'line {n}: environment name missing');continue
            e=e.group(1)
            if t=='\\begin':env.append((e,n))
            elif not env:errors.append(f'line {n}: unmatched end {e}')
            elif env[-1][0]!=e:errors.append(f'line {n}: end {e}, expected {env[-1]}')
            else:env.pop()
    for typ,stack in [('braces',brace),('display delimiters',disp),('dollar delimiters',dollar),('environments',env)]:
        if stack:errors.append(f'unclosed {typ}: {stack}')
    for m in re.finditer(r'\\begin\{tikzcd\}(\[[^\n]*\])?',s):
        if 'ampersand replacement=\\&' not in (m.group(1) or ''):errors.append(f'line {line(m.start())}: missing ampersand replacement')
    return {'file':str(p.relative_to(ROOT)),'braces':not brace and not any('brace' in x for x in errors),'display_open':s.count('\\['),'display_close':s.count('\\]'),'dollar_tokens':sum(m.group()=='$' for m in tokens(s)),'errors':errors,'result':'PASS' if not errors else 'FAIL'}

if __name__=='__main__':
    pages=sorted((ROOT/'pages').glob('*.tex'))
    results=[check(p) for p in pages]
    if (ROOT/'K43-04_transcription.tex').exists():results.append(check(ROOT/'K43-04_transcription.tex'))
    report={'method':'Static braces, display delimiters, dollar parity, nested environments and tikzcd ampersand options; no compilation. Literal mathematical parentheses/brackets intentionally not balanced.','results':results,'all_pass':all(not r['errors'] for r in results)}
    (ROOT/'K43-04_balance.json').write_text(json.dumps(report,indent=2)+'\n')
    for r in results:print(r['file'],r['result'],r['errors'])
    raise SystemExit(0 if report['all_pass'] else 1)
