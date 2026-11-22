#!/usr/bin/env python3
"""Validate current B-prefixed literature PDFs, preserving failed-access receipts."""
import hashlib,json,re,subprocess,time
from pathlib import Path
start=time.perf_counter()
root=Path(__file__).resolve().parents[1]
dest=root/'logs/B_pdf_validation_receipts.json'
old=json.loads(dest.read_text()) if dest.exists() else []
records=[]
for path in sorted((root/'literature').glob('B_*.pdf')):
    data=path.read_bytes()
    check=subprocess.run(['pdfinfo',str(path)],capture_output=True,text=True)
    record={'file':str(path.relative_to(root)),
            'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
            'pdfinfo_valid':check.returncode==0 and data.startswith(b'%PDF-')}
    if record['pdfinfo_valid']:
        record['pages']=int(re.search(r'^Pages:\s+(\d+)',check.stdout,re.M)[1])
    else: record['error']=check.stderr[-500:]
    records.append(record)
paths={r['file'] for r in records}
records.extend(r for r in old if not r.get('pdfinfo_valid',True) and r['file'] not in paths)
dest.write_text(json.dumps(records,indent=2)+'\n')
summary={'current_pdfs':len(paths),'valid_current_pdfs':sum(r['pdfinfo_valid'] for r in records),
         'failed_access_receipts_preserved':sum(not r['pdfinfo_valid'] for r in records),
         'seconds':round(time.perf_counter()-start,6)}
(root/'logs/B_pdf_validation_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
