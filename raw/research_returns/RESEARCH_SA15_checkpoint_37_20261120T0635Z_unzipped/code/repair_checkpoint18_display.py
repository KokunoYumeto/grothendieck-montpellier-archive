"""Preserve the actual failed CP18 build, then repair one display delimiter."""
from pathlib import Path
import datetime,json,shutil
w=Path(__file__).resolve().parents[1]
out=w/'outputs/failed_checkpoint18_build'
out.mkdir(exist_ok=False)
for rel in ['outputs/build_console.txt','outputs/build_failure.json','RESEARCH_SA15_paper.log',
            'RESEARCH_SA15_paper.tex','agents/reduction_descent/B_tame_primitive_norm_orbits.tex']:
    shutil.copy2(w/rel,out/rel.replace('/','__'))
p=w/'agents/reduction_descent/B_tame_primitive_norm_orbits.tex'
s=p.read_text()
old='\\tag{B-RD51.2}\nhas $q$ elements'
assert s.count(old)==1
p.write_text(s.replace(old,'\\tag{B-RD51.2}\n\\]\nhas $q$ elements'))
record={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'failure':'Missing closing display delimiter after B-RD51.2; first delimiter B-RD51.1 was already repaired.',
        'repair':'Inserted only the missing closing display delimiter; no mathematics changed.',
        'failed_build_seconds':json.loads((out/'outputs__build_failure.json').read_text())['seconds']}
(out/'repair_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
