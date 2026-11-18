#!/usr/bin/env python3
"""Static delimiter checks only. Does not invoke a TeX engine."""
from pathlib import Path
import re, json

ROOT=Path(__file__).resolve().parent

def tokens(text):
    i=0
    while i<len(text):
        c=text[i]
        if c=='%':
            end=text.find('\n',i);i=len(text) if end<0 else end+1;continue
        if c=='\\':
            m=re.match(r'\\([A-Za-z]+|.)',text[i:])
            token=m.group(0);yield token;i+=len(token);continue
        yield c;i+=1

def check(path):
    ts=list(tokens(path.read_text())); stack=[];errs=[];dollar=0;displays=0;envs=[]
    for i,t in enumerate(ts):
        if t=='{': stack.append(i)
        elif t=='}':
            if not stack: errs.append('extra closing brace')
            else: stack.pop()
        elif t=='$': dollar+=1
        elif t=='\\[': displays+=1
        elif t=='\\]':
            displays-=1
            if displays<0: errs.append('display closes before opening')
        elif t in ('\\begin','\\end'):
            j=i+1
            while j<len(ts) and ts[j].isspace():j+=1
            if j>=len(ts) or ts[j]!='{': errs.append('environment name lacks brace');continue
            k=j+1
            while k<len(ts) and ts[k]!='}':k+=1
            name=''.join(ts[j+1:k])
            if t=='\\begin':envs.append(name)
            elif not envs or envs[-1]!=name:errs.append('mismatched environment '+name)
            else:envs.pop()
    if stack:errs.append(f'{len(stack)} unclosed braces')
    if dollar%2:errs.append('odd number of unescaped dollar signs')
    if displays:errs.append('display delimiters do not balance')
    if envs:errs.append('unclosed environments: '+', '.join(envs))
    return {'file':str(path.relative_to(ROOT)),'braces':not stack and 'extra closing brace' not in errs,
            'display_delimiters':displays==0 and 'display closes before opening' not in errs,
            'dollar_delimiters':dollar%2==0,'environments':not envs and not any('environment' in e for e in errs),
            'dollar_count':dollar,'errors':errs,'pass':not errs}

if __name__=='__main__':
    paths=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'K43-03_transcription.tex',ROOT/'K43-03_standalone.tex']
    checks=[check(p) for p in paths]
    report={'compiled':False,'scope':'Braces, display delimiters, dollar parity and nested environments; plain manuscript parentheses intentionally not normalised.',
            'all_pass':all(c['pass'] for c in checks),'files':checks}
    (ROOT/'K43-03_balance.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report['all_pass'] else 1)
