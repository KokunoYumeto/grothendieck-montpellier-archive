"""Keep URL/query/hash evidence without redistributing third-party full texts."""
from pathlib import Path
import json,re,csv,hashlib
B=Path(__file__).resolve().parents[1]
rows=[]
for p in sorted(B.rglob('*.json')):
    if 'research' not in p.parts:continue
    try:obj=json.loads(p.read_text())
    except Exception:continue
    if isinstance(obj,dict) and 'content' in obj:
        text='\n'.join(c.get('text','') for c in obj.get('content',[]) if isinstance(c,dict))
        refs=sorted(set(re.findall(r'【(turn[^】]+)】',text)))
        urls=sorted(set(x.rstrip('.,;') for x in re.findall(r'https?://[^\s<>"}\\]+',text)))
        requests=sorted(set(re.findall(r'Source: ([^\n]+)',text)))
        for u in urls:rows.append({'record_file':str(p.relative_to(B)),'record_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'url':u.rstrip(')'), 'source_refs':';'.join(refs),'request_evidence':' | '.join(requests)[:4000],'retention':'Raw retrieval text omitted from ZIP; bibliographic/access evidence retained.'})
with (B/'source_audit/retrieval_index.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['record_file','record_sha256','url','source_refs','request_evidence','retention'],delimiter='\t');w.writeheader();w.writerows(rows)
ocr=[]
for p in sorted(B.rglob('ocr_*.txt')):
    if p.stat().st_size>1024:ocr.append({'path':str(p.relative_to(B)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'retention':'Raw third-party primary-text OCR omitted; program, exact locators, access annotations and mathematical proof checks retained.'})
with (B/'source_audit/ocr_output_audit.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['path','bytes','sha256','retention'],delimiter='\t');w.writeheader();w.writerows(ocr)
print(json.dumps({'retrieval_url_rows':len(rows),'raw_OCR_output_hashes':len(ocr)},ensure_ascii=False))
