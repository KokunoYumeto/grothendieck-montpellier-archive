"""Fetch only named primary sources; save HTTP evidence and text extraction logs."""
from pathlib import Path
import urllib.request, json, subprocess, sys, datetime
out=Path(__file__).resolve().parents[1]/'outputs'
catalog={
 'hua_lean_156_3':'https://raw.githubusercontent.com/Commutator-IO/grothendieck-project/main/lean/Grothendieck/Folder156_3.lean',
 'hua_lean_156_4':'https://raw.githubusercontent.com/Commutator-IO/grothendieck-project/main/lean/Grothendieck/Folder156_4.lean',
 'hua2026':'https://hexagonmath.org/pdf/2611.00125v2',
 'kochen_specker1967':'https://www.iumj.indiana.edu/IUMJ/FTDLOAD/1968/17/17004/pdf',
 'alexandroff1937_ft':'https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=rus&paperid=5579&what=fullt',
 'alexandroff1937':'https://www.mathnet.ru/links/4dae5ff4e7a43c780154e279b2eb15c1/sm5579.pdf',
 'stong1966':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/stong2.pdf',
 'birkhoff1948':'https://math.chapman.edu/~jipsen/summerschool/Birkhoff%201948%20Lattice%20Theory%20Revised%20Edition.pdf',
}
for key in sys.argv[1:]:
 rec={'key':key,'url':catalog[key],'date':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=urllib.request.urlopen(catalog[key],timeout=30); data=r.read(); rec.update(status=r.status,final_url=r.url,bytes=len(data),content_type=r.headers.get('Content-Type'))
  if r.status==200 and key.startswith('hua_lean'):
   (out/(key+'.lean')).write_bytes(data)
  elif r.status==200 and data.startswith(b'%PDF'):
   p=out/(key+'.pdf');p.write_bytes(data)
   proc=subprocess.run(['pdftotext','-layout',str(p),str(out/(key+'.txt'))],capture_output=True,text=True)
   rec.update(extract_exit=proc.returncode,extract_stderr=proc.stderr)
 except Exception as e: rec['error']=str(e)
 (out/(key+'_fetch.json')).write_text(json.dumps(rec,indent=2)+'\n'); print(json.dumps(rec))
