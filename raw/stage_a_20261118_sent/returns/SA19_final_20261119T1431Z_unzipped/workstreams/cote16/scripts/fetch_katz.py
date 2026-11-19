"""Fetch the author's publicly posted primary paper; preserve outcome metadata."""
import json, urllib.request, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
url='https://web.math.princeton.edu/~nmk/old/katzmessing.pdf'
started=time.time()
report={'url':url,'purpose':'Read the exact finite-field characteristic-polynomial statements and hypotheses.'}
try:
    with urllib.request.urlopen(url,timeout=35) as response:
        data=response.read()
    target=ROOT/'research/KatzMessing1974.pdf'
    target.write_bytes(data)
    report.update(status='downloaded',bytes=len(data),file=str(target))
except Exception as error:
    report.update(status='failed',error=repr(error))
report['elapsed_seconds']=round(time.time()-started,3)
(ROOT/'outputs/fetch_katz.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
