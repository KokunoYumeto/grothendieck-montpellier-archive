"""Read-only structural checks; does not compile or alter the transcription."""
from pathlib import Path
import re,json,sys
ROOT=Path(__file__).resolve().parent
def escaped(s,i):
    n=0;i-=1
    while i>=0 and s[i]=='\\':n+=1;i-=1
    return n%2==1
def check(p):
    source=p.read_text();s='\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in source.splitlines())
    errors=[];depth=0
    for i,c in enumerate(s):
        if c in '{}' and not escaped(s,i):
            depth+=1 if c=='{' else -1
            if depth<0:errors.append('closing brace before opening brace');break
    if depth:errors.append('brace depth '+str(depth))
    stack=[];display_count=0
    for m in re.finditer(r'\\([\[\]])',s):
        if escaped(s,m.start()):continue
        if m.group(1)=='[':stack.append(m.start());display_count+=1
        elif stack:stack.pop()
        else:errors.append('unmatched display close')
    if stack:errors.append('unclosed display')
    dollars=sum(c=='$' and not escaped(s,i) for i,c in enumerate(s))
    if dollars%2:errors.append('odd number of dollar delimiters')
    envs=[];env_count=0
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        typ,name=m.groups()
        if typ=='begin':envs.append(name);env_count+=1
        elif not envs or envs.pop()!=name:errors.append('environment nesting mismatch: '+name)
    if envs:errors.append('unclosed environments: '+','.join(envs))
    left=len(re.findall(r'\\left\b',s));right=len(re.findall(r'\\right\b',s))
    if left!=right:errors.append('left/right delimiter count mismatch')
    for m in re.finditer(r'\\begin\{tikzcd\}(\[[^\]]*\])?',s):
        if 'ampersand replacement=\\&' not in (m.group(1) or ''):errors.append('tikzcd lacks ampersand replacement')
    return {'file':str(p.relative_to(ROOT)),'pass':not errors,'brace_balance':depth,'display_pairs':display_count,'dollar_pairs':dollars//2,'environment_pairs':env_count,'left_right_pairs':left,'errors':errors}
files=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'K34-09_transcription.tex',ROOT/'K34-09_standalone.tex']
results=[check(p) for p in files]
report={'compiled':False,'all_pass':all(r['pass'] for r in results),'results':results}
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(0 if report['all_pass'] else 1)
