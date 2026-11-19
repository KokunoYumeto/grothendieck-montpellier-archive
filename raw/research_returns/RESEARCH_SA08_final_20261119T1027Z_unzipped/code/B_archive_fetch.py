from pathlib import Path
from urllib.request import Request,urlopen
import re,json,time
base=Path(__file__).resolve().parents[1]
u='https://grothendieck.umontpellier.fr/archives-grothendieck/'
t=time.monotonic();data=urlopen(Request(u,headers={'User-Agent':'SA08 research'}),timeout=40).read()
p=base/'sources'/'B_archive_catalogue.html';p.write_bytes(data)
s=data.decode('utf8',errors='replace')
for m in re.finditer('136',s):
    print(s[max(0,m.start()-350):m.start()+350])
print('SCRIPT URLS')
for m in re.finditer(r'<script[^>]+src=[\"\']([^\"\']+)',s):print(m.group(1))
print(json.dumps({'url':u,'bytes':len(data),'seconds':time.monotonic()-t}))
