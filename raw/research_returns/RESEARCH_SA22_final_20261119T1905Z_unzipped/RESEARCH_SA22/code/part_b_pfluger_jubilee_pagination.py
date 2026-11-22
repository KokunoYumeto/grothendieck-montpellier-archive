#!/usr/bin/env python3
"""Read the two remaining public metadata pages actually reported by IA."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request,urlopen
import gzip,json,re,time

root=Path(__file__).resolve().parents[1];started=time.monotonic()
first=json.loads((root/'code/part_b_pfluger_jubilee_catalogues_output.json').read_text())['results'][0]
assert first['num_found']==601 and first['returned']==250
fields=['identifier','title','date','creator','description','year','publisher','mediatype']

def search(page):
    begin=time.monotonic()
    params=[('q',first['query']),('rows','250'),('page',str(page)),('output','json')]+[('fl[]',field) for field in fields]
    url='https://archive.org/advancedsearch.php?'+urlencode(params)
    record={'page':page,'query':first['query'],'url':url,'scope':'Public catalogue pagination only'}
    try:
        with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'}),timeout=25) as response:
            raw=response.read(6*1024*1024+1);record.update(http_status=response.status,bytes=len(raw))
        if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
        if len(raw)>6*1024*1024:record['status']='Response cap reached; not inspected'
        else:
            data=json.loads(raw);(root/'sources'/f'part_b_pfluger_golden_jubilee_page{page}.json').write_text(json.dumps(data,indent=2)+'\n')
            result=data['response'];docs=result['docs']
            record.update(status='Public metadata read',num_found=result['numFound'],returned=len(docs),records=docs)
    except Exception as error:record.update(status='Request failed; no retry/bypass',error=str(error))
    record['elapsed_seconds']=time.monotonic()-begin;return record

with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(search,[2,3]))
docs=first['records']+[d for r in results for d in r.get('records',[])]
unique={d['identifier']:d for d in docs}
candidates=[d for d in unique.values() if re.search(r'1907|1958|1961|mathem|Pfluger|Madras|Poona|Jubilee Commemoration',json.dumps(d),re.I)]
generic=[d for d in unique.values() if re.fullmatch(r'\s*(the\s+)?golden[ -]jubilee(\s+(volume|vol\.?|souvenir|book|celebration|celebrations|commemoration))*\s*',str(d.get('title','')),re.I)]
out={'results':results,'elapsed_seconds':time.monotonic()-started,'total_rows_read':len(docs),'unique_identifiers':len(unique),'reported_query_total':first['num_found'],'complete_distinct_inventory':len(unique)==first['num_found'],'candidate_records':candidates,'generic_title_records':generic}
(root/'code/part_b_pfluger_jubilee_pagination_output.json').write_text(json.dumps(out,indent=2)+'\n')
(root/'sources/part_b_pfluger_golden_jubilee_all_metadata.json').write_text(json.dumps(list(unique.values()),indent=2)+'\n')
for r in results:print(json.dumps({k:v for k,v in r.items() if k!='records'},indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in ['results','candidate_records','generic_title_records']},indent=2))
for d in candidates+generic:
    print(json.dumps({k:v for k,v in d.items() if k!='description'},ensure_ascii=False))
