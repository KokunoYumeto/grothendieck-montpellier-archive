"""Inspect public metadata of four journal records lacking year in search fields."""
from pathlib import Path
import urllib.request,json,time,concurrent.futures
R=Path(__file__).resolve().parents[1];t=time.perf_counter()
items=['tdl.26553-the-journal-of-the-indian-mathematical-society','tdl.28360-the-journal-of-the-indian-mathematical-society','tdl.28834-the-journal-of-the-indian-mathematical-society','tdl.28223-the-journal-of-the-indian-mathematical-society-new-series']
def fetch(item):
 t0=time.perf_counter();url='https://archive.org/metadata/'+item
 try:
  with urllib.request.urlopen(url,timeout=35) as r:data=json.load(r)
  (R/'sources'/('metadata_'+item+'.json')).write_text(json.dumps(data,indent=2)+'\n')
  return dict(item=item,seconds=time.perf_counter()-t0,metadata=data.get('metadata'),files=[{k:f.get(k) for k in ['name','format','size','private']} for f in data.get('files',[]) if f.get('format') in ['Text PDF','Abbyy GZ','DjVuTXT','Image Container PDF']])
 except Exception as e:return dict(item=item,error=str(e),seconds=time.perf_counter()-t0)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(fetch,items))
out=dict(requests=len(items),seconds=time.perf_counter()-t,results=rows)
(R/'code/root_pfluger_catalogue_metadata_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
