from pathlib import Path
import re, json
from datetime import datetime, timezone

def escaped(s,i):
    n=0; i-=1
    while i>=0 and s[i]=='\\': n+=1;i-=1
    return n%2==1
def strip_comments(s):
    return '\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in s.splitlines())
def balance(s):
    s=strip_comments(s);errors=[];braces=[];env=[];display=False;dollars=0
    tokens=re.finditer(r'\\begin\{([^}]+)\}|\\end\{([^}]+)\}|\\\[|\\\]|[{}$]',s)
    for m in tokens:
        t=m.group();line=s[:m.start()].count('\n')+1
        if t.startswith('\\begin'):
            env.append((m.group(1),line));continue
        if t.startswith('\\end'):
            if not env or env[-1][0]!=m.group(2):errors.append(f'L{line}: environment close {m.group(2)} mismatched')
            else:env.pop()
            continue
        if t==r'\[':
            if display:errors.append(f'L{line}: nested display opening')
            display=True;continue
        if t==r'\]':
            if not display:errors.append(f'L{line}: display close without opening')
            display=False;continue
        if escaped(s,m.start()):continue
        if t=='{':braces.append(line)
        elif t=='}':
            if braces:braces.pop()
            else:errors.append(f'L{line}: extra closing brace')
        elif t=='$':dollars+=1
    if braces:errors.append('Unclosed braces at '+str(braces))
    if env:errors.append('Unclosed environments '+str(env))
    if display:errors.append('Unclosed display')
    if dollars%2:errors.append('Odd number of inline-dollar delimiters')
    return {'errors':errors,'inline_dollar_delimiters':dollars,'display_pairs':s.count(r'\['),'environment_pairs':len(re.findall(r'\\begin\{',s))}


if __name__ == '__main__':
    out=Path(__file__).resolve().parent
    pages=sorted((out/'pages').glob('*.tex'))
    checks={p.name:balance(p.read_text()) for p in pages}
    report=json.loads((out/'K43-05_validation.json').read_text())
    report['checked_at_utc']=datetime.now(timezone.utc).isoformat(timespec='seconds')
    report['pages_checks']=checks
    report['all_balanced']=not any(v['errors'] for v in checks.values())
    report['assembled_exact_concatenation']=(out/'K43-05_transcription.tex').read_text()=='\n'.join(p.read_text().rstrip() for p in pages)+'\n'
    (out/'K43-05_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['checked_at_utc','all_balanced','assembled_exact_concatenation','counts']},indent=2))
    raise SystemExit(0 if report['all_balanced'] and report['assembled_exact_concatenation'] else 1)
