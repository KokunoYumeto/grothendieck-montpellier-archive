"""Verify literal printed program paths without mathematical reruns."""
from pathlib import Path
import re,json,datetime
w=Path(__file__).resolve().parents[1]
sources=[w/'RESEARCH_SA15_paper.tex']+list((w/'sections').glob('*.tex'))
paths=set()
for p in sources:
    for s in re.findall(r'\\(?:path|texttt)\{([^}]+)\}',p.read_text()):
        s=s.replace('\\_','_')
        if s.startswith(('code/','agents/')) and '.py' in s:paths.add(s)
missing=sorted(p for p in paths if not(w/p).exists())
record={'status':'PASS' if not missing else 'FAIL',
        'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'referenced_program_paths':len(paths),'paths':sorted(paths),'missing':missing,
        'scope':'Existence of literal printed paths only; no mathematical rerun.'}
(w/'outputs/checkpoint27_program_path_verification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2));assert not missing
