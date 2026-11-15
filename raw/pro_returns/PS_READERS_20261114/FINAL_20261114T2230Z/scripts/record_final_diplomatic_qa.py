"""Append individual observations made after actually opening selected PDF renders."""
from pathlib import Path
import hashlib,json,sys
P=Path(__file__).resolve().parents[1]
selection=json.loads((P/'records/QA_SELECTION_PS_EN_diplomatic.json').read_text())
assert hashlib.sha256((P/selection['pdf']).read_bytes()).hexdigest()==selection['pdf_sha256']
target=P/'records/FINAL_VISUAL_QA_diplomatic_134_3_4.json'
data=json.loads(target.read_text()) if target.exists() else {'pdf':selection['pdf'],'pdf_sha256':selection['pdf_sha256'],'entries':[]}
assert data['pdf_sha256']==selection['pdf_sha256']
entries={x['page']:x for x in data['entries']}
lookup={x['page']:x for x in selection['selections']}
for number,observation in json.load(sys.stdin).items():
    n=int(number);s=lookup[n];assert observation.strip()
    row={k:s[k] for k in ('pdf','pdf_sha256','page','image','key')}
    row.update(image_sha256=hashlib.sha256((P/s['image']).read_bytes()).hexdigest(),viewed=True,observation=observation)
    entries[n]=row
data['entries']=[entries[n] for n in sorted(entries)]
target.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print(f"Recorded {len(entries)} actual page observations.")
