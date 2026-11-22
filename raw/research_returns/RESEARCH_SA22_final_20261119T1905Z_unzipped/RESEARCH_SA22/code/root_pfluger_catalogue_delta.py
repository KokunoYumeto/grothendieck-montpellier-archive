"""Inspect only newly discovered public journal records after broadening the title."""
from pathlib import Path
import urllib.request,json,time,concurrent.futures,re
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter()
old=json.loads((ROOT/'sources/indian_math_full_catalogue.json').read_text())['response']['docs']
new=json.loads((ROOT/'sources/indian_mathematical_broad.json').read_text())['response']['docs']
known={record['identifier'] for record in old}
delta=[record for record in new if record['identifier'] not in known]
def inspect(record):
    name=record['identifier'];t=time.perf_counter()
    try:
        with urllib.request.urlopen('https://archive.org/metadata/'+name,timeout=30) as response:
            data=json.load(response)
        (ROOT/'sources'/('pfluger_delta_'+name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
        meta=data.get('metadata',{})
        return dict(identifier=name,title=meta.get('title'),date=meta.get('date'),
                    description=meta.get('description'),restricted=meta.get('access-restricted-item'),
                    candidate=bool(re.search(r'196[01]|\b24\b|xxiv',str(meta)+' '.join(x.get('name','') for x in data.get('files',[])),re.I)),
                    files=[{key:entry.get(key) for key in ['name','format','size','private']} for entry in data.get('files',[]) if entry.get('format') in ['Text PDF','Image Container PDF','DjVuTXT']],
                    seconds=time.perf_counter()-t)
    except Exception as error:return dict(identifier=name,error=str(error),seconds=time.perf_counter()-t)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:results=list(executor.map(inspect,delta))
output=dict(previous_records=len(old),broader_records=len(new),new_metadata_requests=len(delta),seconds=time.perf_counter()-start,results=results)
(ROOT/'code/root_pfluger_catalogue_delta_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
