"""Fetch a specified public primary reference, preserving each actual outcome."""
import json,sys,time,urllib.request
from pathlib import Path
root=Path(__file__).resolve().parents[1]
label,url=sys.argv[1:3]
start=time.time();report={'url':url,'label':label}
try:
    with urllib.request.urlopen(url,timeout=40) as response:
        data=response.read()
    file=root/'research'/f'{label}.pdf';file.write_bytes(data)
    report.update(status='downloaded',bytes=len(data),file=str(file))
except Exception as error:report.update(status='failed',error=repr(error))
report['elapsed_seconds']=round(time.time()-start,3)
(root/'outputs'/f'fetch_{label}.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
