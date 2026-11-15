#!/usr/bin/env python3
"""Lexical checks only; deliberately does not invoke a TeX compiler."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parent

def check(path):
    s = path.read_text(); braces=[]; environments=[]; math=None; group=0
    i=0; line=1; errors=[]; counts={'dollars':0,'displays':0,'environments':0}
    while i < len(s):
        c=s[i]
        if c=='\n': line+=1; i+=1; continue
        if c=='%':
            end=s.find('\n',i); i=len(s) if end<0 else end; continue
        if c=='\\':
            if i+1>=len(s): errors.append(f'L{line}: dangling backslash'); break
            nxt=s[i+1]
            if nxt in '[]':
                if nxt=='[':
                    if math is not None: errors.append(f'L{line}: display opens inside {math}')
                    math='display'; counts['displays']+=1
                else:
                    if math!='display': errors.append(f'L{line}: unmatched display close')
                    math=None
                i+=2; continue
            if not (nxt.isalpha() or nxt=='@'): i+=2; continue
            m=re.match(r'\\([A-Za-z@]+)',s[i:]); command=m.group(1); i+=len(m.group())
            if command in ('begin','end'):
                m=re.match(r'\{([^{}]+)\}',s[i:])
                if not m: errors.append(f'L{line}: missing environment name'); continue
                name=m.group(1); i+=len(m.group())
                if command=='begin': environments.append((name,line)); counts['environments']+=1
                elif not environments or environments[-1][0]!=name: errors.append(f'L{line}: unmatched end {name}')
                else: environments.pop()
            elif command=='begingroup': group+=1
            elif command=='endgroup':
                group-=1
                if group<0: errors.append(f'L{line}: unmatched endgroup')
            continue
        if c=='{': braces.append(line)
        elif c=='}':
            if not braces: errors.append(f'L{line}: unmatched closing brace')
            else: braces.pop()
        elif c=='$':
            counts['dollars']+=1
            if i+1<len(s) and s[i+1]=='$': errors.append(f'L{line}: $$ is not an allowed display form')
            if math=='display': errors.append(f'L{line}: raw dollar inside display')
            else: math=None if math=='inline' else 'inline'
        i+=1
    if braces: errors.append('unclosed braces at '+str(braces))
    if environments: errors.append('unclosed environments '+str(environments))
    if math: errors.append('unclosed '+math+' math')
    if group: errors.append('unbalanced explicit groups: '+str(group))
    return errors,counts

if __name__=='__main__':
    files=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'J156-9-11_transcription.tex',ROOT/'J156-9-11_standalone.tex']
    failed=False
    for p in files:
        errors,counts=check(p); failed|=bool(errors)
        print(('FAIL' if errors else 'PASS')+' '+str(p.relative_to(ROOT))+' '+str(counts))
        for e in errors: print('  '+e)
    print('No compilation attempted. Balance checks do not establish rendered layout or mathematical correctness.')
    sys.exit(1 if failed else 0)
