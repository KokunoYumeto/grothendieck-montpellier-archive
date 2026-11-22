"""Extract advertised periodical-copy links without following login or access gates."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin
import datetime,json,re,time
root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
source=root/'sources/root_russian_translation_periodical_listing.html'
base='https://pastuhova.ucoz.ru/load/nauchno_populjarnye_fiziko_matematicheskie_zhurnaly/serija_matematika_periodicheskij_sbornik_perevodov_inostrannykh_statej/serija_matematika_periodicheskij_sbornik_perevodov_inostrannykh_statej_37_vypuskov/28-1-0-276'
class Reader(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.current=None;self.text=[]
    def handle_starttag(self,tag,attrs):
        if tag=='a':
            self.current={'url':urljoin(base,dict(attrs).get('href','')),'text':''}
    def handle_endtag(self,tag):
        if tag=='a' and self.current is not None:
            self.links.append(self.current);self.current=None
    def handle_data(self,text):
        self.text.append(text)
        if self.current is not None:self.current['text']+=text
reader=Reader();reader.feed(source.read_text())
selected=[x for x in reader.links if re.search(r'скача|download|narod|disk|deposit|\.rar|\.zip|\.pdf|\.djvu',x['url']+' '+x['text'],re.I)]
text='\n'.join(reader.text)
contexts=[]
for match in re.finditer(r'Гротендик|1958|Фредгольма|скачать',text,re.I):
    contexts.append(text[max(0,match.start()-180):match.end()+350])
record={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source':str(source.relative_to(root)),'anchor_count':len(reader.links),
        'selected_links':selected,'contexts':contexts,
        'elapsed_seconds':time.perf_counter()-start}
(root/'logs/root_russian_translation_followup.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
