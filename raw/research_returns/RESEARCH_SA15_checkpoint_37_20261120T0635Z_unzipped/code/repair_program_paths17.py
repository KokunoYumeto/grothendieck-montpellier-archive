"""Supply literal program aliases for unambiguous legacy paper references."""
from pathlib import Path
import datetime,json,re,shutil
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/checkpoint17_program_path_verification.json';assert not dest.exists()
references=set()
for p in (w/'sections').glob('*.tex'):
    references.update(re.findall(r'\\path\{(code/[^}]+)\}',p.read_text()))
made=[];unresolved=[]
for rel in sorted(references):
    target=w/rel
    if target.exists():continue
    candidates=[p for p in (w/'agents').glob('*/code/'+target.name) if p.is_file()]
    if not candidates:
        candidates=[p for p in (w/'code').glob('*/'+target.name) if p.is_file()]
    unique={p.read_bytes() for p in candidates}
    if len(unique)!=1:
        unresolved.append({'reference':rel,'candidates':[str(p.relative_to(w)) for p in candidates]})
        continue
    source=candidates[0];target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source,target)
    made.append({'reference':rel,'source':str(source.relative_to(w)),'literal_bytes_identical':True})
    # Preserve the adjacent output expected by a literal invocation, when available.
    for suffix in ['.output.json','.json','.output.txt']:
        sibling=source.with_suffix(suffix)
        alias=target.with_suffix(suffix)
        if sibling.exists() and not alias.exists():shutil.copy2(sibling,alias)
out={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'referenced_program_paths':len(references),'literal_aliases_added':made,
     'unresolved':unresolved,'status':'PASS' if not unresolved else 'UNRESOLVED_PATHS'}
dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
