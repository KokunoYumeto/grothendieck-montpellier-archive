"""Check delimiter/environment pairing only; does not invoke TeX or validate readings."""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parent
SCANS=list(range(116,129))+[130,131,132]

def escaped(s,i):
    n=0;i-=1
    while i>=0 and s[i]=='\\':n+=1;i-=1
    return n%2==1

def clean(s):
    lines=[]
    for line in s.splitlines(True):
        cut=next((i for i,c in enumerate(line) if c=='%' and not escaped(line,i)),len(line))
        lines.append(line[:cut]+('\n' if cut<len(line) else ''))
    return ''.join(lines)

def check(path):
    s=clean(path.read_text());errors=[];braces=[];math=[];env=[]
    for i,c in enumerate(s):
        if escaped(s,i):continue
        if c=='{':braces.append(i)
        elif c=='}':
            if braces:braces.pop()
            else:errors.append('unmatched closing brace at '+str(i))
        elif c=='$':
            if math and math[-1]=='$':math.pop()
            else:math.append('$')
        elif c=='\\' and i+1<len(s) and s[i+1] in '[]()':
            token=s[i+1]
            if token in '[(':math.append(token)
            else:
                wanted={']':'[',')':'('}[token]
                if math and math[-1]==wanted:math.pop()
                else:errors.append('unmatched math delimiter \\'+token+' at '+str(i))
    if braces:errors.append('unclosed braces: '+str(len(braces)))
    if math:errors.append('unclosed math delimiters: '+repr(math))
    for m in re.finditer(r'\\(begin|end)\s*\{([^{}]+)\}',s):
        action,name=m.groups()
        if action=='begin':env.append(name)
        elif env and env[-1]==name:env.pop()
        else:errors.append('environment closing mismatch: '+name)
    if env:errors.append('unclosed environments: '+repr(env))
    return {'file':str(path.relative_to(ROOT)),'balanced':not errors,'errors':errors}

if __name__=='__main__':
    paths=[ROOT/f'pages/K34-07_34_scan{n}.tex' for n in SCANS]
    paths += [ROOT/'K34-07_transcription.tex',ROOT/'K34-07_standalone.tex']
    rows=[check(p) for p in paths]
    report={'scope':'Braces, inline/display math delimiters, and environment pairing. No compilation.',
            'all_balanced':all(r['balanced'] for r in rows),'files':rows}
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report['all_balanced'] else 1)
