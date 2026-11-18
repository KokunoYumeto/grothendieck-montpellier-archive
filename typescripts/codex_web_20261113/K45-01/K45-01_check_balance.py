#!/usr/bin/env python3
"""Lexical balance/coverage check only; never invokes a TeX engine."""
from pathlib import Path
import csv,json,re,hashlib
ROOT=Path(__file__).resolve().parent

def uncomment(text):
    out=[]
    for line in text.splitlines(keepends=True):
        cut=len(line)
        for i,ch in enumerate(line):
            if ch=='%':
                j=i-1
                while j>=0 and line[j]=='\\':j-=1
                if (i-j-1)%2==0:cut=i;break
        out.append(line[:cut]+'\n' if cut<len(line) else line)
    return ''.join(out)

def balance(path):
    s=uncomment(path.read_text());br=[];env=[];math=None;errors=[];i=0;line=1
    while i<len(s):
        ch=s[i]
        if ch=='\n':line+=1;i+=1;continue
        if ch=='\\':
            m=re.match(r'\\(begin|end)\{([^{}]+)\}',s[i:])
            if m:
                op,name=m.groups()
                if op=='begin':env.append((name,line))
                elif not env or env[-1][0]!=name:errors.append(f'line {line}: unmatched end {name}')
                else:env.pop()
                i+=len(m.group());continue
            if s.startswith(r'\[',i):
                if math is not None:errors.append(f'line {line}: display opened inside {math}')
                math='display';i+=2;continue
            if s.startswith(r'\]',i):
                if math!='display':errors.append(f'line {line}: unmatched display close')
                math=None;i+=2;continue
            if s.startswith(r'\illegible{',i) and math is not None:
                errors.append(f'line {line}: illegible macro in math')
            m=re.match(r'\\[A-Za-z]+',s[i:])
            i+=len(m.group()) if m else min(2,len(s)-i)
            continue
        if ch=='{':br.append(line)
        elif ch=='}':
            if br:br.pop()
            else:errors.append(f'line {line}: unmatched closing brace')
        elif ch=='$':
            if math is None:math='inline'
            elif math=='inline':math=None
            else:errors.append(f'line {line}: dollar in display')
        i+=1
    if br:errors.append(f'unclosed braces opened on lines {br}')
    if env:errors.append(f'unclosed environments {env}')
    if math is not None:errors.append(f'unclosed {math} math')
    for m in re.finditer(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}',s,re.S):
        block=m.group(1)
        if 'ampersand replacement=\\&' not in block:errors.append('tikzcd missing ampersand replacement')
        if re.search(r'(?<!\\)&',block):errors.append('unescaped ampersand inside tikzcd')
    return errors

pages=sorted((ROOT/'pages').glob('K45-01_45_scan*.tex'))
assert [int(p.stem[-3:]) for p in pages]==list(range(2,18))
files=pages+[ROOT/'K45-01_transcription.tex',ROOT/'K45-01_standalone.tex']
results={str(p.relative_to(ROOT)):balance(p) for p in files}
sources={int(p.stem[-3:]):p.read_text() for p in pages}
fragment=(ROOT/'K45-01_transcription.tex').read_text()
assert fragment==''.join(sources[n] for n in range(2,18)), 'assembly differs from page-file concatenation'
assert fragment.startswith('\\cotefile{45}\n')
assert fragment.count('\\cotefile{45}')==1
assert [int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',fragment)]==list(range(2,18))
assert not re.search(r'\\(?:includegraphics|newcommand|renewcommand|def)\b',fragment)
rows=list(csv.DictReader((ROOT/'K45-01_inventory.csv').open()))
assert all(r['transcribed']=='yes' for r in rows)
for n,s in sources.items():
    assert f'% archive sheet number: {n-1}' in s
    rs=[r for r in rows if int(r['scan'])==n]
    assert [int(r['element']) for r in rs]==list(range(1,len(rs)+1))
    for macro,kind in [('deleted','deletion'),('inserted','insertion'),('diagram','diagram'),('margin','margin note')]:
        assert s.count('\\'+macro+'{')==sum(r['kind']==kind for r in rs),(n,macro,'inventory count mismatch')
    assert s.count('\\[')==sum(r['kind']=='display' for r in rs),(n,'display inventory mismatch')
counts={m:fragment.count('\\'+m+'{') for m in ['unsure','illegible','deleted','inserted','margin','diagram']}
report={'scope':'lexical balance only; no compilation','files':results,'counts_in_fragment':counts,'inventory_rows':len(rows),'assembly_exact':True}
print(json.dumps(report,ensure_ascii=False,indent=2))
if any(results.values()):raise SystemExit(1)
