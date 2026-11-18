"""Syntax-only checks; deliberately does not invoke any TeX engine."""
from pathlib import Path
import re,json,csv,hashlib

ROOT=Path(__file__).resolve().parent
def escaped(s,i):
    j=i-1
    while j>=0 and s[j]=='\\':j-=1
    return (i-j-1)%2==1
def uncomment(s):
    return '\n'.join(line[:next((i for i,c in enumerate(line) if c=='%' and not escaped(line,i)),len(line))] for line in s.splitlines())
def check(s):
    s=uncomment(s);errors=[];depth=0;mode=None;env=[]
    for i,c in enumerate(s):
        if c in '{}' and not escaped(s,i):
            depth+=1 if c=='{' else -1
            if depth<0:errors.append('premature closing brace');depth=0
    if depth:errors.append('unbalanced braces: '+str(depth))
    for m in re.finditer(r'\\\[|\\\]|(?<!\\)\$',s):
        t=m[0]
        if t==r'\[':
            if mode:errors.append('display opened within '+mode)
            mode='display'
        elif t==r'\]':
            if mode!='display':errors.append('display closed outside display')
            mode=None
        else:
            if mode=='display':errors.append('dollar inside display')
            mode=None if mode=='inline' else 'inline'
    if mode:errors.append('unclosed '+mode+' math')
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        if m[1]=='begin':env.append(m[2])
        elif not env or env.pop()!=m[2]:errors.append('environment mismatch '+m[2])
    if env:errors.append('unclosed environments '+repr(env))
    for m in re.finditer(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}',s,re.S):
        if r'ampersand replacement=\&' not in m[1]:errors.append('missing tikzcd ampersand replacement')
        if re.search(r'(?<!\\)&',m[1]):errors.append('unescaped tikzcd ampersand')
    return errors

pages=[ROOT/'pages'/f'K34-05_34_scan{n:03}.tex' for n in range(84,100)]
checks={p.name:check(p.read_text()) for p in pages}
assembled=ROOT/'K34-05_transcription.tex'
checks[assembled.name]=check(assembled.read_text())
assert assembled.read_bytes()==b''.join(p.read_bytes() for p in pages),'assembled bytes differ'
s=assembled.read_text()
assert s.startswith(r'\cotefile{34}') and s.count(r'\cotefile{')==1
assert re.findall(r'\\scanpage\{(\d+)\}',s)==[str(n) for n in range(84,100)]
rows=list(csv.DictReader((ROOT/'K34-05_inventory.csv').open()))
assert all(r['transcribed']=='yes' for r in rows)
assert {int(r['scan']) for r in rows}==set(range(84,100))
report={'balance_passed':not any(checks.values()),'page_and_fragment_checks':checks,
 'assembled_is_exact_concatenation':True,'page_order_correct':True,
 'mark_counts':{name:len(re.findall(r'\\'+name+r'\{',s)) for name in ['unsure','illegible','deleted']},
 'illegible_estimated_words':sum(map(int,re.findall(r'\\illegible\{(\d+)\}',s))),
 'inventory_rows':len(rows),'all_inventory_rows_transcribed':True,
 'compiled':False,'scope':'Braces, inline/display math delimiters, environments, diagram ampersands, page order, exact concatenation; literal manuscript parentheses are intentionally not normalized.'}
(ROOT/'K34-05_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
raise SystemExit(0 if report['balance_passed'] else 1)
