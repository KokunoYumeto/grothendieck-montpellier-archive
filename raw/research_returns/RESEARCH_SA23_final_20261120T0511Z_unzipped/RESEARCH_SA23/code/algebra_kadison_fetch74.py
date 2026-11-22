from pathlib import Path
import urllib.request, hashlib, json, time, datetime, concurrent.futures, subprocess
import fitz

ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic()
jobs=[
 ('penn_findingaid','https://archives.upenn.edu/collections/finding-aid/upf8_5/','html'),
 ('ias_sm_findingaid','https://www.ias.edu/sites/default/files/library/page/SM.html','html'),
 ('ias_member_findingaid','https://www.ias.edu/sites/default/files/library/page/DO.MEMBERS.html','html'),
 ('fuglede1952','https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison/1950s/1952_DeterminantTheoryInFiniteFactors.pdf','pdf'),
 ('fuglede1951','https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison/1950s/1951_on_determinants_and_a_property_of_the_trace_in_finite_factors.pdf','pdf'),
 ('report1955','https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison/1950s/1955_report_on_operator_algebras.pdf','pdf')
]
def fetch(job):
 name,url,ext=job
 out={'name':name,'url':url,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url, timeout=25) as r:
   data=r.read();out.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'))
  p=ROOT/'sources'/f'algebra_kadison_{name}.{ext}'
  p.write_bytes(data)
  out.update(path=str(p.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  if ext=='pdf':
   d=fitz.open(p);out['pages']=len(d)
   txt='\n\f\n'.join(x.get_text() for x in d)
   p.with_suffix('.txt').write_text(txt)
   out['keyword_pages']={k:[i+1 for i,x in enumerate(d) if k.lower() in x.get_text().lower()] for k in ['Groth','letter','communicat','acknow','Hilbert','genus','Fredholm','received','determinant']}
   chosen={'fuglede1952':[1,6,11],'fuglede1951':[1,6,7],'report1955':list(range(1,8))}[name]
   out['renders']=[]
   for n in chosen:
    rp=ROOT/'sources'/f'algebra_kadison_{name}_page{n:03d}.png'
    d[n-1].get_pixmap(matrix=fitz.Matrix(2.2,2.2)).save(rp)
    out['renders'].append(str(rp.relative_to(ROOT)))
   if len(txt.strip())<100:
    out['ocr']='not run; original page images will be read'
 except Exception as e:out['error']=repr(e)
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 results=list(pool.map(fetch,jobs))
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':round(time.monotonic()-start,3),'sources':results,'scope':'Retrieval and rendering only. Actual visual reading is recorded separately. No denied endpoint retried.'}
(ROOT/'logs'/'algebra_kadison_fetch74.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2))
