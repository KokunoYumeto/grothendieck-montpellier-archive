"""Correct the PDF/scandata offset and render Lidskii's opening page."""
from pathlib import Path
import subprocess,time,json
r=Path(__file__).resolve().parents[1]; start=time.perf_counter()
cmd=['pdftoppm','-f','21','-l','21','-singlefile','-scale-to','2200','-png',str(r/'sources/algebra_history_lidskii_original_issue.pdf'),str(r/'sources/algebra_history_lidskii_original_pdfp021')]
p=subprocess.run(cmd,capture_output=True,text=True)
record={'command':cmd,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'elapsed_seconds':round(time.perf_counter()-start,6),'mapping':'PDF pages 21,22,23 = printed pages 485,486,487; scandata leaves 21,22,23. Two excluded leaves alter naive +1 conversion.'}
(r/'logs/algebra_history_render07.json').write_text(json.dumps(record,indent=2));print(json.dumps(record,indent=2))
