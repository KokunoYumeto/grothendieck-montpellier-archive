"""Rebuild after the two actually inspected CP18 overflow repairs."""
from pathlib import Path
import subprocess,sys,shutil,json,datetime
w=Path(__file__).resolve().parents[1]
for name in ['consolidate.py','number_statements.py','build_paper.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
for name in ['build_summary.json','build_console.txt']:
    dest=w/'outputs'/('checkpoint18_final_'+name);assert not dest.exists()
    shutil.copy2(w/'outputs'/name,dest)
record={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'root_actually_viewed_initial_overflow_pages':[243,245],
        'repairs':['Kept status short and moved the unchanged audit scope into ordinary prose.','Split the exact sequence and the definition of R into two gathered lines.'],
        'mathematical_change':False}
(w/'outputs/checkpoint18_layout_repair.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
