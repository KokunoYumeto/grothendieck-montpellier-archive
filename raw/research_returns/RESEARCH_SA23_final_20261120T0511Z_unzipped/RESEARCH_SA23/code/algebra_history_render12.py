"""Inspect image-only inventory/fiches examples in the archival presentation."""
from pathlib import Path
import subprocess, json, time
root = Path(__file__).resolve().parents[1]
src = root/'sources/algebra_history_cirm_inventory.pdf'
out = []
for n in [9,13,16]:
 t=time.perf_counter()
 dest=root/'sources'/f'algebra_history_cirm_inventory_p{n:03d}'
 cmd=['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-scale-to','1900','-png',str(src),str(dest)]
 p=subprocess.run(cmd,capture_output=True,text=True)
 out.append({'source':str(src.relative_to(root)),'page':n,'command':cmd,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'elapsed_seconds':round(time.perf_counter()-t,6)})
(root/'logs/algebra_history_render12.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
