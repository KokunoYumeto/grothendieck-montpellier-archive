#!/usr/bin/env python3
"""Non-compiling checks of the delivered LaTeX sources; standard library only."""
from pathlib import Path
import re, sys, json
ROOT=Path(__file__).resolve().parent

def uncomment(s):
    out=[];i=0
    while i<len(s):
        if s[i]=='\\':
            out.append(s[i:i+2]);i+=2
        elif s[i]=='%':
            k=s.find('\n',i)
            i=len(s) if k<0 else k
        else:out.append(s[i]);i+=1
    return ''.join(out)

def check(p):
    s=uncomment(p.read_text());errors=[];braces=[];displays=[];dollars=[]
    # Lex control sequences so escaped braces/dollars and linebreaks are not counted.
    for m in re.finditer(r'\\[A-Za-z]+|\\[^A-Za-z]|[{}$]',s):
        tok=m.group();line=s.count('\n',0,m.start())+1
        if tok=='{':braces.append(line)
        elif tok=='}':
            if braces:braces.pop()
            else:errors.append(f'unmatched closing brace near line {line}')
        elif tok==r'\[':displays.append(line)
        elif tok==r'\]':
            if displays:displays.pop()
            else:errors.append(f'unmatched display close near line {line}')
        elif tok=='$':dollars.append(line)
    if braces:errors.append(f'unclosed braces opened near {braces}')
    if displays:errors.append(f'unclosed displays opened near {displays}')
    if len(dollars)%2:errors.append(f'odd unescaped dollar count {len(dollars)}')
    env=[];env_count=0
    for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',s):
        action,name=m.groups();line=s.count('\n',0,m.start())+1
        if action=='begin':env.append((name,line));env_count+=1
        elif not env:errors.append(f'unmatched end {name} near {line}')
        elif env[-1][0]!=name:errors.append(f'env mismatch {env[-1][0]} / {name} near {line}')
        else:env.pop()
    if env:errors.append(f'unclosed environments {env}')
    for m in re.finditer(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}',s,re.S):
        body=m.group(1)
        if r'ampersand replacement=\&' not in body:errors.append('tikzcd lacks explicit ampersand replacement')
        if re.search(r'(?<!\\)&',body):errors.append('tikzcd contains a raw unescaped ampersand')
    return {'file':str(p.relative_to(ROOT)),'pass':not errors,'brace_pairs':sum(1 for m in re.finditer(r'(?<!\\)\{',s)),'display_pairs':len(re.findall(r'\\\[',s)),'dollar_pairs':len(dollars)//2,'environment_pairs':env_count,'errors':errors}

def main():
    pages=sorted((ROOT/'pages').glob('*.tex'))
    paths=pages+[ROOT/'J156-7-14_transcription.tex',ROOT/'J156-7-14_standalone.tex']
    results=[check(p) for p in paths]
    joined='\n'.join(p.read_text().rstrip() for p in pages)+'\n'
    assembled=(ROOT/'J156-7-14_transcription.tex').read_text()
    extra=[]
    if joined!=assembled:extra.append('assembled file differs from ordered page concatenation')
    if not assembled.startswith(r'\cotefile{156-7}'):extra.append('wrong starting cote')
    if assembled.count(r'\cotefile{')!=1:extra.append('cote must occur exactly once')
    if re.findall(r'\\scanpage\{(\d+)\}',assembled)!=[str(n) for n in range(108,115)]:extra.append('wrong scan sequence')
    if re.findall(r'\\mspage\{(\d+)\}',assembled)!=[str(n) for n in range(107,114)]:extra.append('wrong manuscript page sequence')
    if re.search(r'\\(?:includegraphics|newcommand|renewcommand|def)\b',assembled):extra.append('unexpected image inclusion or macro definition')
    counts={name:len(re.findall(r'\\'+name+r'\{',assembled)) for name in ['unsure','illegible','deleted']}
    result={'status':'PASS' if all(r['pass'] for r in results) and not extra else 'FAIL','scope':'Static balance checks only; no TeX compilation or rendering attempted. Dollar check is lexical pairing, not a TeX expansion check.','results':results,'assembly_errors':extra,'marks_in_single_assembled_transcription':counts}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result['status']=='PASS' else 1
if __name__=='__main__':sys.exit(main())
