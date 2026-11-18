#!/usr/bin/env python3
"""Delimiter/environment checks only; this does not invoke a TeX engine."""
from pathlib import Path
import re, json, sys
ROOT=Path(__file__).resolve().parent
SCANS=[79,80,81,82,84,85,86,87,89,90,91,92,93,143,144]
def escaped(s,i):
    n=0; j=i-1
    while j>=0 and s[j]=='\\': n+=1; j-=1
    return n%2==1
def clean(s):
    return '\n'.join(line[:next((i for i,c in enumerate(line) if c=='%' and not escaped(line,i)),len(line))] for line in s.splitlines())
def check(path):
    s=clean(path.read_text()); errors=[]; braces=[]; envs=[]; math=[]; dollars=0
    i=0
    while i<len(s):
        c=s[i]
        if c in '{}' and not escaped(s,i):
            if c=='{': braces.append(i)
            elif not braces: errors.append('Unmatched closing brace')
            else:braces.pop()
        if c=='$' and not escaped(s,i):dollars+=1
        if c=='\\' and not escaped(s,i):
            m=re.match(r'\\(begin|end)\{([^}]+)\}',s[i:])
            if m:
                if m[1]=='begin':envs.append(m[2])
                elif not envs or envs.pop()!=m[2]:errors.append('Mismatched environment: '+m[2])
            t=s[i:i+2]
            if t in (r'\[',r'\('):math.append(t)
            elif t in (r'\]',r'\)'):
                expected={r'\]':r'\[',r'\)':r'\('}[t]
                if not math or math.pop()!=expected:errors.append('Mismatched display/inline delimiter '+t)
        i+=1
    if braces:errors.append(f'{len(braces)} unclosed brace(s)')
    if envs:errors.append('Unclosed environments: '+repr(envs))
    if math:errors.append('Unclosed math delimiters: '+repr(math))
    if dollars%2:errors.append('Odd number of unescaped dollar delimiters')
    for m in re.finditer(r'\\begin\{tikzcd\}(\[[\s\S]*?\])?',s):
        if not m[1] or r'ampersand replacement=\&' not in m[1]:errors.append('tikzcd lacks ampersand replacement')
    return {'file':str(path.relative_to(ROOT)), 'status':'PASS' if not errors else 'FAIL','unescaped_dollars':dollars,'errors':errors}
if __name__=='__main__':
    paths=[ROOT/'pages'/f'K43-06_43_scan{n:03d}.tex' for n in SCANS]+[ROOT/'K43-06_transcription.tex',ROOT/'K43-06_standalone.tex']
    report={'scope':'Braces, dollar parity, math delimiters, environment nesting, tikzcd ampersand replacement. No compilation or layout validation.', 'results':[check(p) for p in paths]}
    print(json.dumps(report,indent=2))
    sys.exit(any(x['status']!='PASS' for x in report['results']))
