"""Aggregate the independently maintained source registers without losing flags."""
from pathlib import Path
import re, json
root=Path(__file__).resolve().parents[1]
parts=sorted((root/'notes').glob('*_references.bib'))
seen={}; entries=[]
for path in parts:
    data=path.read_text()
    starts=list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,\s]+)\s*,',data))
    for i,match in enumerate(starts):
        body=data[match.start():starts[i+1].start() if i+1<len(starts) else len(data)].strip()
        key=match.group(1)
        if key in seen:
            if seen[key]!=body: raise ValueError(f'Conflicting bibliography key {key}')
            continue
        seen[key]=body; entries.append(body)
(root/'RESEARCH_SA23_references.bib').write_text('\n\n'.join(entries)+'\n')
cited=set()
for path in (root/'sections').glob('*.tex'):
    for match in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',path.read_text()):
        cited.update(x.strip() for x in match.group(1).split(','))
report={'parts':[str(p.relative_to(root)) for p in parts], 'entries':len(entries),
        'cited_keys':len(cited),'missing_keys':sorted(cited-set(seen)),
        'uncited_keys':sorted(set(seen)-cited)}
(root/'logs'/'bibliography_audit.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
