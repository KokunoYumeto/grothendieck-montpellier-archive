from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, difflib

root=Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work')
own=root/'agents/reduction_descent'
record_path=own/'outputs/B93_CP34_wiring.json'
assert not record_path.exists()
promotion=json.loads((own/'outputs/B93_promotion.json').read_text())
canonical=Path(promotion['canonical'])
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(canonical)==promotion['canonical_sha256']
history=own/'notes/CP34_before_B93_wiring'
history.mkdir(exist_ok=False)
conso=root/'code/consolidate.py'
config=root/'notes/checkpoint34_promoted_inputs.json'
old_conso=conso.read_text()
needle="                    'B_residual_wild_crossing.tex']:"
assert old_conso.count(needle)==1
assert "'B_residual_wild_last_crossing.tex'" not in old_conso
assert 'A4_general_odd_source_Cartier.tex' in old_conso
new_conso=old_conso.replace(needle,"                    'B_residual_wild_crossing.tex',\n                    'B_residual_wild_last_crossing.tex']:")
old_config=config.read_text()
items=json.loads(old_config)
assert 'agents/obstructions_crystals/A4_general_odd_source_Cartier.tex' in items
new_path='agents/reduction_descent/B_residual_wild_last_crossing.tex'
assert new_path not in items
items.append(new_path)
new_config=json.dumps(items,indent=2)+'\n'
changes=[]
for path,old,new in [(conso,old_conso,new_conso),(config,old_config,new_config)]:
    (history/path.name).write_text(old)
    path.write_text(new)
    (history/(path.name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=str(path)+':before',tofile=str(path)+':after')))
    changes.append({'path':str(path),'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':sha(path)})
compile(conso.read_text(),str(conso),'exec')
record={'status':'WIRED','actual_utc':datetime.now(timezone.utc).isoformat(),'canonical':str(canonical),'canonical_sha256':sha(canonical),'changes':changes,'history':str(history),'scope':'One B93 canonical include and one CP34 required path after OC release; the general odd-source Cartier include/config path is explicitly preserved. No build, report, bibliography or immutable checkpoint modification.'}
record_path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
