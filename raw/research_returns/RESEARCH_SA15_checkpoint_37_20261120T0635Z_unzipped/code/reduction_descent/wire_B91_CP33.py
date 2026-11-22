from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import difflib

ROOT = Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work')
OWN = ROOT / 'agents/reduction_descent'
record_path = OWN / 'outputs/B91_CP33_wiring.json'
assert not record_path.exists()
promotion = json.loads((OWN / 'outputs/B91_promotion.json').read_text())
canonical = Path(promotion['canonical'])
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(canonical) == promotion['canonical_sha256']
conso = ROOT / 'code/consolidate.py'
config = ROOT / 'notes/checkpoint33_promoted_inputs.json'
history = OWN / 'notes/CP33_before_B91_wiring'
history.mkdir(exist_ok=False)
records = []
before = conso.read_text()
needle = "                    'B_p5_third_point_ramification.tex']:"
assert before.count(needle) == 1
assert "'B_residual_wild_high_quotient.tex'" not in before
after = before.replace(needle, "                    'B_p5_third_point_ramification.tex',\n                    'B_residual_wild_high_quotient.tex']:")
for path, old, new in [(conso, before, after)]:
    (history / path.name).write_text(old)
    path.write_text(new)
    (history / (path.name + '.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile=str(path)+':before', tofile=str(path)+':after')))
    records.append({'path':str(path), 'before_sha256':hashlib.sha256(old.encode()).hexdigest(), 'after_sha256':sha(path)})
old = config.read_text()
items = json.loads(old)
required = 'agents/reduction_descent/B_residual_wild_high_quotient.tex'
assert required not in items
items.append(required)
new = json.dumps(items, indent=2) + '\n'
(history / config.name).write_text(old)
config.write_text(new)
(history / (config.name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=str(config)+':before',tofile=str(config)+':after')))
records.append({'path':str(config),'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':sha(config)})
compile(conso.read_text(), str(conso), 'exec')
result = {'status':'WIRED', 'actual_utc':datetime.now(timezone.utc).isoformat(), 'canonical':str(canonical), 'canonical_sha256':sha(canonical), 'changes':records, 'scope':'One late-B canonical insertion and one CP33 required input; all released OC/Mono paths preserved. No build, report, bibliography, or immutable checkpoint modification.', 'history':str(history)}
record_path.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result,indent=2))
