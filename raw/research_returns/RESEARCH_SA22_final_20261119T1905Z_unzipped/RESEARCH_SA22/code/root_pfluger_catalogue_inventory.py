"""Inventory advertised public filenames; never request private archive files."""
from pathlib import Path
import urllib.request,json,time,concurrent.futures,re
R=Path(__file__).resolve().parents[1];start=time.perf_counter()
docs=json.loads((R/'sources/indian_math_full_catalogue.json').read_text())['response']['docs']
def scan(doc):
 item=doc['identifier'];path=R/'sources'/('metadata_'+item+'.json');t=time.perf_counter()
 try:
  cached=path.exists()
  if cached:data=json.loads(path.read_text())
  else:
   with urllib.request.urlopen('https://archive.org/metadata/'+item,timeout=30) as r:data=json.load(r)
   path.write_text(json.dumps(data)+'\n')
  meta=data.get('metadata',{})
  files=[{k:f.get(k) for k in ['name','format','size','private']} for f in data.get('files',[]) if f.get('format') in ['Text PDF','Image Container PDF','DjVuTXT']]
  desc=' '.join([str(meta.get('original_url','')),str(meta.get('date','')),str(meta.get('volume','')),str(meta.get('description',''))]+[f['name'] for f in files])
  candidate=bool(re.search(r'196[01]|(?:Vol(?:ume)?[._\s%20-]+24\b)|\bXXIV\b',desc,re.I))
  return dict(item=item,cached=cached,seconds=time.perf_counter()-t,candidate=candidate,original_url=meta.get('original_url'),files=files)
 except Exception as e:return dict(item=item,error=str(e),seconds=time.perf_counter()-t)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:rows=list(ex.map(scan,docs))
out=dict(records=len(rows),requests=sum(not x.get('cached',False) for x in rows),seconds=time.perf_counter()-start,candidates=[x for x in rows if x.get('candidate')],errors=[x for x in rows if 'error' in x],results=rows)
(R/'code/root_pfluger_catalogue_inventory_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))
