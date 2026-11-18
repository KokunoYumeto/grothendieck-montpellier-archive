"""Syntax balance only. This script does not invoke TeX or check source readings."""
from pathlib import Path
import re, json

ROOT=Path(__file__).resolve().parent
def escaped(s,i):
    j=i-1
    while j>=0 and s[j]=='\\':j-=1
    return (i-j-1)%2==1
def without_comments(s):
    lines=[]
    for line in s.splitlines():
        for i,c in enumerate(line):
            if c=='%' and not escaped(line,i):
                line=line[:i];break
        lines.append(line)
    return '\n'.join(lines)
def check(path):
    s=without_comments(path.read_text());errors=[];braces=[];dollars=[]
    for i,c in enumerate(s):
        if escaped(s,i):continue
        if c=='{':braces.append(i)
        if c=='}':
            if braces:braces.pop()
            else:errors.append('unmatched closing brace')
        if c=='$':dollars.append(i)
    if braces:errors.append(f'{len(braces)} unmatched opening braces')
    if len(dollars)%2:errors.append('odd number of unescaped dollar signs')
    displays=[]
    for m in re.finditer(r'\\\[|\\\]',s):
        if m[0]=='\\[':displays.append(m.start())
        elif displays:displays.pop()
        else:errors.append('unmatched display close')
    if displays:errors.append('unmatched display open')
    envs=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        if m[1]=='begin':envs.append(m[2])
        elif envs and envs[-1]==m[2]:envs.pop()
        else:errors.append('mismatched environment end: '+m[2])
    if envs:errors.append('unclosed environments: '+str(envs))
    return {'file':str(path.relative_to(ROOT)),'balanced':not errors,'errors':errors,'dollar_pairs':len(dollars)//2,'display_pairs':len(re.findall(r'\\\[',s))}

if __name__=='__main__':
    pages=sorted((ROOT/'pages').glob('K46-03_46_scan*.tex'))
    report=[check(p) for p in pages+[ROOT/'K46-03_transcription.tex',ROOT/'K46-03_standalone.tex']]
    assert len(pages)==15
    assert all(x['balanced'] for x in report),report
    assert (ROOT/'K46-03_transcription.tex').read_bytes()==b''.join(p.read_bytes() for p in pages)
    s=(ROOT/'K46-03_transcription.tex').read_text()
    assert s.startswith('\\cotefile{46}\n\\scanpage{81}')
    assert s.count('\\cotefile{')==1
    assert [int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',s)]==list(range(81,96))
    print(json.dumps({'all_balanced':True,'assembly_matches_page_bytes':True,'files':report},indent=2))
