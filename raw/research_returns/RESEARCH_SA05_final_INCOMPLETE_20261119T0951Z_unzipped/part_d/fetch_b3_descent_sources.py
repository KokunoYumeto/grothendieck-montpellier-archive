"""Archive the exact primary sources used in the post-CP04 B3 audit."""
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, subprocess, urllib.request

root=Path(__file__).resolve().parent
items=[
 ('Kelly2018UniversalHomeomorphisms.pdf','https://www.ms.u-tokyo.ac.jp/~kelly/pdfs/uh%20non-fp.pdf'),
 ('Stacks0AF8RegularTorsors.html','https://stacks.math.columbia.edu/tag/0AF8'),
 ('Esser2022NontorsionBrauer.pdf','https://arxiv.org/pdf/2102.01799'),
 ('ColliotTheleneSkorobogatov2019Brauer.pdf','https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf'),
]
class Plain(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self,t,a):
        if t in ('script','style'): self.skip+=1
        if t in ('p','div','section','h1','h2','h3','h4','li','tr'): self.parts.append('\n')
    def handle_endtag(self,t):
        if t in ('script','style'): self.skip-=1
        if t in ('p','div','section','h1','h2','h3','h4','li','tr'): self.parts.append('\n')
    def handle_data(self,s):
        if not self.skip: self.parts.append(s)
def fetch(item):
    filename,url=item; row={'url':url,'archive':'sources/'+filename}
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(request,timeout=40) as response: data=response.read()
        path=root/'sources'/filename; path.write_bytes(data)
        row.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),status='obtained')
        if path.suffix=='.pdf':
            result=subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],capture_output=True,text=True)
            row['pdftotext_returncode']=result.returncode
            if result.stderr: row['pdftotext_stderr']=result.stderr
        else:
            parser=Plain(); parser.feed(data.decode('utf-8'))
            text='\n'.join(' '.join(x.split()) for x in ''.join(parser.parts).splitlines() if x.strip())
            path.with_suffix('.txt').write_text(text+'\n')
    except Exception as exc: row.update(status='failed',error=str(exc))
    return row
with ThreadPoolExecutor(max_workers=4) as pool: rows=list(pool.map(fetch,items))
result={'retrieved_utc':datetime.now(timezone.utc).isoformat(),'sources':rows}
(root/'fetch_b3_descent_sources_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
