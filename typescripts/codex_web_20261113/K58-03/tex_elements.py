"""Read balanced editorial arguments, math spans and manuscript blocks without TeX."""
import bisect
import re
from pathlib import Path
MACRO=re.compile(r'\\([A-Za-z]+)\s*\{')
def escaped(s,i):
    count=0
    while i>0 and s[i-1]=='\\':
        count+=1;i-=1
    return count%2==1
def arguments(s, allowed):
    for m in MACRO.finditer(s):
        name=m[1]
        if name not in allowed: continue
        level=1;j=m.end()
        while j<len(s) and level:
            if s[j] in '{}' and not escaped(s,j):
                level+=1 if s[j]=='{' else -1
            j+=1
        if level:raise ValueError((name,m.start(),'open argument'))
        yield (m.start(),j,name,s[m.end():j-1])
def blocks(raw):
    groups=[]
    for m in re.finditer(r'(?:[^\n]+\n?)+',raw):
        body=m.group().strip('\n')
        live='\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in body.splitlines()).strip()
        if live: groups.append((m.start(),live))
    return groups
def page_path(n,base):
    return Path(base)/f'K58-03_58_scan{n:03}.tex'
def stamp():
    from datetime import datetime,timezone
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
