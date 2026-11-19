from pathlib import Path
from urllib.request import urlopen, Request
sources={
 'EGA_IV3.pdf':'https://www.numdam.org/item/PMIHES_1966__28__5_0.pdf',
 'Milne_LAG.pdf':'https://www.jmilne.org/math/CourseNotes/LAG.pdf',
 'Li_BasicRep.pdf':'https://www.wwli.asia/downloads/BasicRep.pdf',
 'Deligne_HodgeII.pdf':'https://www.numdam.org/item/PMIHES_1971__40__5_0.pdf',
 'Deligne_Milne_tc2012.pdf':'https://www.jmilne.org/math/xnotes/tc.pdf',
}
for name,url in sources.items():
 path=Path('agents/p15/evidence')/name
 try:
  data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read()
  assert data.startswith(b'%PDF')
  path.write_bytes(data)
  print(name,len(data),url,'OK')
 except Exception as exc:print(name,url,type(exc).__name__,str(exc))
