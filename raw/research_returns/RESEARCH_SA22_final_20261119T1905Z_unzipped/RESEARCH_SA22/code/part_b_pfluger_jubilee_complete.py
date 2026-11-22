#!/usr/bin/env python3
"""Resolve duplicated unsorted pagination with one bounded sorted query.

The previous three pages returned601rows but only505unique identifiers. This
new public metadata request asks for up to650sorted rows in one response, based
on the actually reported601total. It is not a retry of a denied endpoint.
"""
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request,urlopen
import gzip,json,re,time

root=Path(__file__).resolve().parents[1];started=time.monotonic()
query='title:("Golden Jubilee")'
fields=['identifier','title','date','creator','description','year','publisher','mediatype']
params=[('q',query),('rows','650'),('page','1'),('sort[]','identifier asc'),('output','json')]+[('fl[]',x) for x in fields]
url='https://archive.org/advancedsearch.php?'+urlencode(params)
record={'query':query,'url':url,'scope':'One sorted public metadata snapshot,650row cap; resolves actual duplicated pagination'}
try:
    with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'}),timeout=25) as response:
        raw=response.read(6*1024*1024+1);record.update(http_status=response.status,bytes=len(raw))
    if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
    if len(raw)>6*1024*1024:record['status']='Response cap reached; not inspected'
    else:
        data=json.loads(raw);result=data['response'];docs=result['docs'];unique={d['identifier']:d for d in docs}
        (root/'sources/part_b_pfluger_golden_jubilee_sorted.json').write_text(json.dumps(data,indent=2)+'\n')
        record.update(status='Public metadata read',num_found=result['numFound'],returned=len(docs),unique_identifiers=len(unique),complete_for_query=len(unique)==result['numFound'],records=docs)
        candidates=[d for d in docs if re.search(r'1907|1958|1961|mathem|Pfluger|Madras|Poona|Jubilee Commemoration',json.dumps(d),re.I)]
        record['candidate_records']=candidates
        with (root/'sources/part_b_pfluger_jubilee_titles.tsv').open('w') as out:
            out.write('identifier\ttitle\tdate\tcreator\tpublisher\n')
            for d in docs:
                out.write('\t'.join(str(d.get(k,'')).replace('\t',' ').replace('\n',' ') for k in ['identifier','title','date','creator','publisher'])+'\n')
except Exception as error:record.update(status='Request failed; no retry/bypass',error=str(error))
record['elapsed_seconds']=time.monotonic()-started
output={'results':[record],'elapsed_seconds':record['elapsed_seconds']}
(root/'code/part_b_pfluger_jubilee_complete_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['records','candidate_records']},indent=2))
for d in record.get('candidate_records',[]):print(json.dumps({k:v for k,v in d.items() if k!='description'},ensure_ascii=False))
