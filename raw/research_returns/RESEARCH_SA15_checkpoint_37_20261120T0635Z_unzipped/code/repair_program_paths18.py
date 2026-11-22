"""Repair four older texttt references missed by the earlier path-only audit."""
from pathlib import Path
import datetime,json,shutil
w=Path(__file__).resolve().parents[1]
fail=w/'outputs/checkpoint18_program_path_verification.json'
saved=w/'outputs/checkpoint18_program_path_initial_failure.json';assert not saved.exists()
shutil.copy2(fail,saved)
r=json.loads(fail.read_text());made=[]
for rel in r['missing']:
    target=w/rel;assert not target.exists()
    candidates=[p for p in (w/'agents').glob('*/code/'+target.name) if p.is_file()]
    assert len({p.read_bytes() for p in candidates})==1,(rel,candidates)
    source=candidates[0];shutil.copy2(source,target)
    made.append({'reference':rel,'source':str(source.relative_to(w)),'literal_bytes_identical':True})
    for suffix in ['.output.json','.json','.output.txt']:
        sibling=source.with_suffix(suffix);alias=target.with_suffix(suffix)
        if sibling.exists() and not alias.exists():shutil.copy2(sibling,alias)
out={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'aliases_added':made,
     'scope':'Literal byte-identical aliases only; no mathematical program was rerun.'}
(w/'outputs/checkpoint18_program_path_repairs.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
