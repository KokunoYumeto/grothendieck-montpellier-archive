"""Verify final unchanged QA images are byte-identical to actually viewed images."""
from pathlib import Path
import hashlib,json,datetime
w=Path(__file__).resolve().parents[1]
groups={'root':[1,14,24,28,39,55],'reduction_descent':[70],
        'obstructions_crystals':[85,190,191,192,193,194]}
records=[]
for reviewer,pages in groups.items():
    for page in pages:
        name=f'page_{page:03d}.png'
        a=hashlib.sha256((w/'outputs/qa19'/name).read_bytes()).hexdigest()
        b=hashlib.sha256((w/'outputs/qa19_final'/name).read_bytes()).hexdigest()
        records.append({'reviewer':reviewer,'page':page,'identical':a==b,'sha256_initial':a,'sha256_final':b})
record={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status':'PASS' if all(r['identical'] for r in records) else 'FAIL',
        'scope':'Exact bytes of images already actually viewed; not a claim of fresh reinspection.',
        'pages':records}
(w/'outputs/checkpoint19_identical_QA_pages.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'pages':len(records),'differences':[r['page'] for r in records if not r['identical']]},indent=2))
assert record['status']=='PASS'
