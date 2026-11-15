#!/usr/bin/env python3
"""Syntax-balance checks only. Does not invoke TeX or repair source punctuation."""
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parent

def check(path):
    s=path.read_text(encoding='utf-8')
    groups=[]; displays=[]; errors=[]; dollars=[]; tokens=[]
    line=1; i=0; display_count=0
    while i<len(s):
        c=s[i]
        if c=='\n':line+=1;i+=1;continue
        if c=='%':
            end=s.find('\n',i)
            i=len(s) if end<0 else end
            continue
        if c=='\\':
            start=i;i+=1
            if i>=len(s):errors.append(f'l.{line}: trailing backslash');break
            if s[i].isalpha():
                while i<len(s) and s[i].isalpha():i+=1
                tokens.append((s[start:i],line))
                continue
            cmd=s[i];i+=1
            if cmd=='[':
                display_count+=1
                if displays:errors.append(f'l.{line}: nested display opener')
                displays.append(line)
            elif cmd==']':
                if not displays:errors.append(f'l.{line}: unmatched display closer')
                else:displays.pop()
            continue
        if c=='{':groups.append(line)
        elif c=='}':
            if groups:groups.pop()
            else:errors.append(f'l.{line}: unmatched group closer')
        elif c=='$':dollars.append(line)
        i+=1
    if groups:errors.append('unclosed groups at '+str(groups))
    if displays:errors.append('unclosed displays at '+str(displays))
    if len(dollars)%2:errors.append('odd dollar count '+str(len(dollars)))
    clean=re.sub(r'(?m)(?<!\\)%[^\n]*','',s)
    envs=[]
    for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
        action,name=m.groups()
        if action=='begin':envs.append(name)
        elif not envs or envs[-1]!=name:errors.append('environment order mismatch at '+m.group(0))
        else:envs.pop()
    if envs:errors.append('unclosed environments '+str(envs))
    left=sum(t=='\\left' for t,_ in tokens);right=sum(t=='\\right' for t,_ in tokens)
    if left!=right:errors.append(f'left/right counts differ: {left}/{right}')
    if any(t in ('\\def','\\newcommand','\\renewcommand','\\includegraphics') for t,_ in tokens):
        errors.append('unexpected notation definition or included image')
    return errors,{'dollar_signs':len(dollars),'display_pairs':display_count,'environment_pairs':len(re.findall(r'\\begin\{',clean))}

def main():
    paths=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'J156-9-03_transcription.tex',ROOT/'J156-9-03_standalone.tex']
    failed=False
    for path in paths:
        errors,stats=check(path)
        print(('FAIL' if errors else 'PASS')+' '+str(path.relative_to(ROOT))+' '+str(stats))
        for err in errors:print('  '+err)
        failed|=bool(errors)
    return 1 if failed else 0

if __name__=='__main__':sys.exit(main())
