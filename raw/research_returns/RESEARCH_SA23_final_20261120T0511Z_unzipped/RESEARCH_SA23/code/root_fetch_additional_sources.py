"""Fetch the identified primary texts and author publication index."""
from pathlib import Path
import urllib.request, hashlib, time, json, concurrent.futures
root=Path(__file__).resolve().parents[1]
sources={
 'neeman_1992.pdf':'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/neeman-chrom.pdf',
 'blickle_fink_2025_source':'https://arxiv.org/src/2501.09437v1',
 'perez_2008_source':'https://arxiv.org/src/0801.2846',
 'terng_publications.html':'https://www.math.uci.edu/~cterng/Publications-with-preprints.html',
}
def fetch(item):
    name,url=item;start=time.perf_counter()
    record={'file':name,'url':url}
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 ResearchSourceVerification'})
        with urllib.request.urlopen(request,timeout=30) as response:
            data=response.read()
            record.update(status=response.status,content_type=response.headers.get('Content-Type'))
        (root/'sources'/name).write_bytes(data)
        record.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    except Exception as exc:record.update(status='failed',error=str(exc))
    record['seconds']=time.perf_counter()-start
    return record
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    records=list(executor.map(fetch,sources.items()))
(root/'logs'/'root_additional_sources.json').write_text(json.dumps(records,indent=2))
print(json.dumps(records,indent=2))
