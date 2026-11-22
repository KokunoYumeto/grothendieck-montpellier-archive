from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
import hashlib
import subprocess

ROOT=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
sources=[
 ('Schneps_chapter4','https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Mathematics/chap4.pdf'),
 ('Kothe_index','https://kalliope-verbund.info/de/findingaid_index?fa.id=DE-611-BF-61480&lastparam=true'),
 ('Kothe_findingaid_landing','https://edocs.sub.uni-goettingen.de/handle/4/23583'),
]
class Anchors(HTMLParser):
    def __init__(self):
        super().__init__();self.href=None;self.parts=[];self.links=[]
    def handle_starttag(self,tag,attrs):
        if tag=='a':self.href=dict(attrs).get('href');self.parts=[]
    def handle_data(self,data):
        if self.href is not None:self.parts.append(data)
    def handle_endtag(self,tag):
        if tag=='a' and self.href is not None:
            self.links.append((self.href,''.join(self.parts).strip()));self.href=None

for name,url in sources:
    print('REQUEST',name,url,flush=True)
    try:
        with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as response:
            body=response.read();final=response.url;mime=response.headers.get('Content-Type','')
            print('RESULT',response.status,final,mime,len(body),hashlib.sha256(body).hexdigest(),flush=True)
        ext='pdf' if body.startswith(b'%PDF') else 'html'
        path=ROOT/f'notes/category_date_{name}.{ext}';path.write_bytes(body)
        if ext=='pdf':
            run=subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],capture_output=True,text=True)
            print('PDFTOTEXT',run.returncode,run.stderr.strip(),flush=True)
        else:
            html=body.decode('utf-8','replace');parser=Anchors();parser.feed(html)
            if name=='Kothe_index':
                for href,title in parser.links:
                    if 'Grothendieck' in title:
                        print('GROTHENDIECK_ACTUAL_LINK',urljoin(final,href),title,flush=True)
            else:
                for href,title in parser.links:
                    if any(x in (href+' '+title).lower() for x in ['pdf','bitstream','download','kothe','köthe']):
                        print('LANDING_LINK',urljoin(final,href),title,flush=True)
    except Exception as exc:
        print('FAILED',type(exc).__name__,str(exc),flush=True)
