"""Extract the already retrieved CIRM archival presentation; preserve command output."""
from pathlib import Path
import subprocess, json, time

root = Path(__file__).resolve().parents[1]
p = root / 'sources/algebra_history_cirm_inventory.pdf'
t = time.perf_counter()
run = subprocess.run(['pdftotext', '-layout', str(p), str(p.with_suffix('.txt'))], capture_output=True, text=True)
info = subprocess.run(['pdfinfo', str(p)], capture_output=True, text=True)
out = {'source': str(p.relative_to(root)), 'extraction_returncode': run.returncode,
       'extraction_stderr': run.stderr, 'pdfinfo_returncode': info.returncode,
       'pdfinfo': info.stdout, 'elapsed_seconds': round(time.perf_counter()-t, 6)}
(root / 'logs/algebra_history_extract11.json').write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(json.dumps(out, indent=2, ensure_ascii=False))
