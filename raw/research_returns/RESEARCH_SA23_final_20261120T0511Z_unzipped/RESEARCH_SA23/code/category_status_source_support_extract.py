from pathlib import Path
import json,re
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
paths=[r/'notes/geometry_web_abelian_stack_Robert.json',r/'notes/geometry_web_abelian_stack_exact.json']
def strings(x):
    if isinstance(x,str):yield x
    elif isinstance(x,list):
        for y in x:yield from strings(y)
    elif isinstance(x,dict):
        for y in x.values():yield from strings(y)
snips=[]
for p in paths:
    if not p.exists():continue
    for s in strings(json.loads(p.read_text(encoding='utf-8'))):
        for m in re.finditer(r'Theorem\s+2\.3\.2|Théorème\s+2\.3\.2',s,re.I):
            snips.append({'source':str(p.relative_to(r)),'context':s[max(0,m.start()-700):min(len(s),m.end()+1600)]})
out={'snippets':snips,'note':'Existing raw retrieval outputs read for the stated theorem; no claim to have opened the older Faltings-Chai book.'}
(r/'notes/category_status_source_Robert_support.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
