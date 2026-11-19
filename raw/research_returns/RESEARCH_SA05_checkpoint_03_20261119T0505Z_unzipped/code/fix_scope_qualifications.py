"""Keep the report's finite-even criterion within its proved complex scope."""
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1];start=time.monotonic();records=[]
replacements={
'for every smooth projective variety with pure-even cohomology':'for every smooth projective complex variety with pure-even rational cohomology',
'For a pure-even cohomology algebra, invariant theory gives':'For the rational cohomology algebra of a smooth projective complex variety with no odd cohomology, invariant theory gives',
'General mixed-parity classification remains an independent open row.':'Classification over arbitrary algebraically closed fields and in mixed parity remains an independent open row.'}
for rel in ['PROGRESS_LEDGER.md','RESEARCH_SA05_report.md','code/record_checkpoint_03_research.py']:
    path=ROOT/rel;old=path.read_text();new=old
    for a,b in replacements.items():new=new.replace(a,b)
    if new!=old:path.write_text(new)
    records.append({'path':rel,'changed_in_this_idempotent_run':new!=old,'desired_complex_scope_present':'smooth projective complex variety' in new})
result={'files':records,'scope':'The earlier identical edit is preserved by this idempotent reproducible script.','seconds':round(time.monotonic()-start,4)}
(ROOT/'code/fix_scope_qualifications_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
