"""Preserve a failed preparation build and correct its plain-text bibliography note."""
from pathlib import Path
import datetime, json, shutil, time
root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
diagnostics = json.loads((root/'logs/build_diagnostics.json').read_text())
retained = []
sources = [root/'logs/build_diagnostics.json', root/'RESEARCH_SA23_paper.log',
           root/'RESEARCH_SA23_paper.bbl']
sources += [root/f'logs/build_{i:02d}.txt' for i in range(1, len(diagnostics['commands'])+1)]
for source in sources:
    target = root/'logs'/('build_checkpoint04_attempt01_'+source.name)
    if not target.exists():
        shutil.copy2(source,target)
    retained.append(str(target.relative_to(root)))
path = root/'notes/geometry_references.bib'
text = path.read_text()
count = text.count('Hilbert constant k_n=1')
if count:
    assert count == 1
    path.write_text(text.replace('Hilbert constant k_n=1','Hilbert constant k(n)=1'))
result = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'failure': 'Unescaped underscore in plain-text bibliography note: k_n=1',
          'replacement': 'k(n)=1', 'replacements': count, 'preserved_outputs': retained,
          'before_overfull_count': diagnostics['overfull_count'],
          'before_overfull_gt_2pt': diagnostics['overfull_gt_2pt'],
          'seconds': time.perf_counter()-started}
(root/'logs/root_checkpoint04_build_fix.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
