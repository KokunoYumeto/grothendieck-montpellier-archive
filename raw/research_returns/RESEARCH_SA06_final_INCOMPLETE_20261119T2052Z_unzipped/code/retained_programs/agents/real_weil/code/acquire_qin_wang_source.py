from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, time, urllib.request
root=Path(__file__).resolve().parents[3]
url='https://arxiv.org/pdf/math/0405600'
started=datetime.now(timezone.utc).isoformat()
tick=time.perf_counter()
data=urllib.request.urlopen(url,timeout=45).read()
target=root/'sources/qin_wang2005_integral_operators_v2.pdf'
target.write_bytes(data)
proc=subprocess.run(['pdftotext','-layout',str(target),str(target.with_suffix('.txt'))],capture_output=True,text=True)
result={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'seconds':time.perf_counter()-tick,'url':url,'file':str(target.relative_to(root)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'pdftotext_returncode':proc.returncode,'pdftotext_stderr':proc.stderr}
(root/'agents/real_weil/output/qin_wang_source_acquisition.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
