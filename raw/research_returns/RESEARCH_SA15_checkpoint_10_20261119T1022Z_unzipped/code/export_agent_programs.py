"""Place literal copies of every agent program and its local outputs under code/."""
from pathlib import Path
import shutil,json
w=Path(__file__).resolve().parents[1]
copied=[]
for owner in ['monodromy','reduction_descent','obstructions_crystals']:
 source=w/'agents'/owner/'code'
 if not source.exists():continue
 for p in sorted(source.rglob('*')):
  if not p.is_file() or '__pycache__' in p.parts:continue
  if p.suffix not in ['.py','.json','.txt','.md','.csv','.tsv']:continue
  target=w/'code'/owner/p.relative_to(source)
  target.parent.mkdir(parents=True,exist_ok=True)
  shutil.copy2(p,target)
  copied.append({'original':str(p.relative_to(w)),'copy':str(target.relative_to(w))})
(w/'outputs/exported_programs.json').write_text(json.dumps(copied,indent=2)+'\n')
print(f'Copied {len(copied)} program/output files verbatim into code/.')
