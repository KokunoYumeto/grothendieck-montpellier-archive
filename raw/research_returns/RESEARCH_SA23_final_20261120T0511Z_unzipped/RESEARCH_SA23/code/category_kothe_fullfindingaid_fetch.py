from pathlib import Path
from urllib.request import Request,urlopen
from html.parser import HTMLParser
import hashlib

ROOT=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
url='https://kalliope-verbund.info/de/findingaid?fa.id=DE-611-BF-61480&htmlFull=true&lang=de'
print('REQUEST',url,flush=True)
try:
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as response:
        body=response.read()
        print('RESULT',response.status,response.url,len(body),hashlib.sha256(body).hexdigest(),flush=True)
    path=ROOT/'notes/category_date_Kothe_fullfindingaid.html';path.write_bytes(body)
    html=body.decode('utf-8','replace')
    class Text(HTMLParser):
        def __init__(self):super().__init__();self.parts=[]
        def handle_data(self,text):self.parts.append(text)
    parser=Text();parser.feed(html);text='\n'.join(parser.parts)
    path.with_suffix('.txt').write_text(text)
    start=0
    while True:
        i=text.find('Grothendieck',start)
        if i<0:break
        print('MATCH_CONTEXT',repr(text[max(0,i-900):i+1300]),flush=True)
        start=i+len('Grothendieck')
except Exception as exc:
    print('FAILED',type(exc).__name__,str(exc),flush=True)
