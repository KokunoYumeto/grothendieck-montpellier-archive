#!/usr/bin/env python3
"""Fetch explicitly selected public primary sources and log their hashes.
Full external books remain in excluded reference_cache; only targeted audit notes
and this fetch log belong to the deliverable.
"""
import pathlib,urllib.request,hashlib,json,sys,datetime,subprocess,concurrent.futures
root=pathlib.Path(__file__).resolve().parents[1];cache=root/'reference_cache';cache.mkdir(exist_ok=True)
sources={
 'SerreTate1968':'https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf',
 'EGAIV4':'https://www.numdam.org/item/PMIHES_1967__32__5_0.pdf',
 'SGA4I':'https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-1.pdf',
 'SGA1':'https://arxiv.org/pdf/math/0206203',
 'SGA3XI':'https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo11.pdf',
 'Neron1964':'https://www.numdam.org/item/PMIHES_1964__21__5_0.pdf',
 'Deligne1980':'https://www.numdam.org/item/PMIHES_1980__52__137_0.pdf',
 'Neron1965':'https://annals.math.princeton.edu/wp-content/uploads/annals-v82-n2-p03.pdf',
}
def fetch(name):
 url=sources[name];dest=cache/(name+'.pdf');record={'name':name,'url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  if not dest.exists():
   with urllib.request.urlopen(url,timeout=45)as r:dest.write_bytes(r.read());record['http_status']=r.status
  data=dest.read_bytes();record.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),path=str(dest))
  r=subprocess.run(['pdftotext','-layout',str(dest),str(cache/(name+'.txt'))],capture_output=True,text=True)
  record.update(pdftotext_returncode=r.returncode,pdftotext_stderr=r.stderr)
 except Exception as e:record['error']=str(e)
 return record
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4)as pool:
 futures=[pool.submit(fetch,name)for name in sys.argv[1:]]
 for future in concurrent.futures.as_completed(futures):
  record=future.result();results.append(record)
  with (root/'outputs'/'fetch_primary.jsonl').open('a')as f:f.write(json.dumps(record)+'\n')
  print(json.dumps(record),flush=True)
print(json.dumps(results,indent=2))
