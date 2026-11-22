from urllib.request import urlopen,Request
from pathlib import Path
import re
url='https://grothendieck.umontpellier.fr/archives-grothendieck/'
s=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode()
Path('RESEARCH_SA23/sources/category_archive_index.html').write_text(s)
for pattern in ['161-5','162-5','iframe','src=']:
 print('PATTERN',pattern)
 for m in list(re.finditer(re.escape(pattern),s))[-12:]:print(s[max(0,m.start()-300):m.end()+600])
