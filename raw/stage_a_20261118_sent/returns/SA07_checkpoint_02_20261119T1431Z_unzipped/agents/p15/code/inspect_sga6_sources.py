from urllib.request import urlopen
from pathlib import Path
from html.parser import HTMLParser
urls={
 'sga6_assembly.tex':'https://library.slmath.org/nonmsri/sga/sga/pdf/pdftex/sga6.tex',
 'sga6_raw_index.html':'https://wstein.org/sga/sga/6/',
}
for name,url in urls.items():
 try:
  data=urlopen(url,timeout=40).read(); (Path('agents/p15/evidence')/name).write_bytes(data)
  print(url,'bytes',len(data)); txt=data.decode(errors='replace')
  if name.endswith('.tex'):
   lines=txt.splitlines()
   for i,line in enumerate(lines):
    if '580' in line or '586' in line or '587' in line: print(i+1,'\n'.join(lines[max(0,i-3):i+4]))
  else:
   class Links(HTMLParser):
    def handle_starttag(self,tag,attrs):
     if tag=='a':
      href=dict(attrs).get('href','')
      if any(x in href for x in ['579','580','581','586','587','247']):print(href)
   Links().feed(txt)
 except Exception as exc:print(type(exc).__name__,str(exc))
