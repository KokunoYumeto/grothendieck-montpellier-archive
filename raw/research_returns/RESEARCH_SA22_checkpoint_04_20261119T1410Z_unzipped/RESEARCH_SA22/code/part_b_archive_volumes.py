#!/usr/bin/env python3
"""Read public Internet Archive catalogue metadata for original source volumes."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen,Request
from urllib.parse import urlencode
import json,time
root=Path(__file__).resolve().parents[1]
queries={
 'gabber_volume':'collection:pub_israel-journal-of-mathematics AND year:1994',
 'fujiwara_volume':'title:("Duke Mathematical Journal") AND year:1995',
 'gabber_article':'title:("Affine analog of the proper base change theorem")',
 'fujiwara_article':'title:("Theory of tubular neighborhood")',
 'lieberman_volume':'title:("American Journal of Mathematics") AND year:1968',
 'kleiman_book':'title:(Motives) AND year:1994',
}
def run(item):
 name,q=item;url='https://archive.org/advancedsearch.php?'+urlencode({'q':q,'fl[]':['identifier','title','access-restricted-item','date','collection'],'rows':30,'output':'json'},doseq=True);out={'query':q,'url':url};t=time.time()
 try:
  with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'}),timeout=25) as r:j=json.load(r)
  out['response']=j.get('response',j)
 except Exception as e:out['error']=str(e)
 out['elapsed_seconds']=round(time.time()-t,2);return name,out
with ThreadPoolExecutor(max_workers=6) as pool:results=dict(pool.map(run,queries.items()))
(root/'code/part_b_archive_volumes_output.json').write_text(json.dumps(results,indent=2)+'\n')
for k,v in results.items():print(k,json.dumps(v))
