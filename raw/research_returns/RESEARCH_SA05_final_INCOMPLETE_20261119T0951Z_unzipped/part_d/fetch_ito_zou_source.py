"""Archive the author-hosted October 2026 full-text article and readable text."""
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
import hashlib
import json
import urllib.request

root=Path(__file__).resolve().parent
url='https://www.math.uni-bielefeld.de/~hzou/papers/semisimplicity/'
request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
with urllib.request.urlopen(request,timeout=35) as response:
    data=response.read()
path=root/'sources/ito_zou2026_semisimplicity.html'
path.write_bytes(data)

class Plain(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts=[]
        self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):
            self.skip+=1
        if tag in ('p','div','section','h1','h2','h3','h4','h5','h6','li','tr'):
            self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style'):
            self.skip-=1
        if tag in ('p','div','section','h1','h2','h3','h4','h5','h6','li','tr'):
            self.parts.append('\n')
    def handle_data(self,text):
        if not self.skip:
            self.parts.append(text)

parser=Plain()
parser.feed(data.decode('utf-8'))
plain='\n'.join(' '.join(line.split()) for line in ''.join(parser.parts).splitlines() if line.strip())
path.with_suffix('.txt').write_text(plain+'\n')
manifest={'retrieved_utc':datetime.now(timezone.utc).isoformat(),'url':url,
          'title':'Semisimplicity, Purity and Mumford–Tate Conjecture for hyper-Kähler Varieties',
          'authors':['Kazuhiro Ito','Haitao Zou'],'article_date':'2026-10-06',
          'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
          'archive':str(path.relative_to(root)),'text':str(path.with_suffix('.txt').relative_to(root))}
(root/'fetch_ito_zou_source_output.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
