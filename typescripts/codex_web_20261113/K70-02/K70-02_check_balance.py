"""Structural checks only. Run with Python 3; does not invoke TeX or OCR."""
from pathlib import Path
import json, re

ROOT=Path(__file__).resolve().parent

def escaped(text,i):
    n=0;i-=1
    while i>=0 and text[i]=='\\':
        n+=1;i-=1
    return n%2==1

def check(path):
    src=path.read_text(); cleaned=[]
    for line in src.splitlines(keepends=True):
        cut=next((i for i,c in enumerate(line) if c=='%' and not escaped(line,i)),len(line))
        cleaned.append(line[:cut]+'\n')
    text=''.join(cleaned); braces=[]; displays=[]; dollars=[]; envs=[];errors=[]
    for i,c in enumerate(text):
        if escaped(text,i):continue
        if c=='{':braces.append(i)
        elif c=='}':
            if braces:braces.pop()
            else:errors.append('unmatched closing brace at '+str(i))
        elif c=='$':
            if dollars:dollars.pop()
            else:dollars.append(i)
    for m in re.finditer(r'\\([\[\]])|\\(begin|end)\{([^}]+)\}',text):
        if escaped(text,m.start()):continue
        if m.group(1)=='[':displays.append(m.start())
        elif m.group(1)==']':
            if displays:displays.pop()
            else:errors.append('unmatched display close')
        elif m.group(2)=='begin':envs.append(m.group(3))
        elif not envs or envs.pop()!=m.group(3):errors.append('environment nesting mismatch at '+m.group())
    if braces:errors.append(str(len(braces))+' unclosed braces')
    if displays:errors.append(str(len(displays))+' unclosed displays')
    if dollars:errors.append('unpaired dollar delimiter')
    if envs:errors.append('unclosed environments: '+repr(envs))
    return {'file':str(path.relative_to(ROOT)), 'passed':not errors, 'errors':errors}

if __name__=='__main__':
    files=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'K70-02_transcription.tex',ROOT/'K70-02_standalone.tex']
    results=[check(p) for p in files]
    report={'scope':'braces, display delimiters, paired dollar delimiters, nested environments; no compilation','files':results,'passed':all(r['passed'] for r in results)}
    (ROOT/'K70-02_balance_check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report['passed'] else 1)
