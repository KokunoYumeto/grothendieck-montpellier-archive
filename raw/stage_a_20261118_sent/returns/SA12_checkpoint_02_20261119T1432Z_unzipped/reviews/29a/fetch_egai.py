"""Fetch an opened primary reference for a precise citation check; cache excluded."""
from pathlib import Path
import urllib.request, subprocess, hashlib, json
from datetime import datetime, timezone
p=Path(__file__).parent/'reference_cache'
url='https://www.numdam.org/item/PMIHES_1960__4__5_0.pdf'
pdf=p/'EGAI1960.pdf'
with urllib.request.urlopen(url,timeout=45) as response:
    data=response.read()
    status=response.status
pdf.write_bytes(data)
out=p/'EGAI1960.txt'
cp=subprocess.run(['pdftotext','-layout',str(pdf),str(out)],capture_output=True,text=True)
print(json.dumps(dict(url=url,status=status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),opened_utc=datetime.now(timezone.utc).isoformat(),text_bytes=out.stat().st_size,extract_code=cp.returncode,stderr=cp.stderr)))
