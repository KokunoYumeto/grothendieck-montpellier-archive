"""Download opened primary sources for the middle dossier; preserve failures."""
from pathlib import Path
import urllib.request, json, subprocess
root=Path(__file__).resolve().parents[1]
dest=root/'work/middle/references'
sources={
 'CenklPorter1982':'https://mat.uab.cat/~pubmat/fitxers/download/FileType:pdf/FolderName:v26(3)/FileName:26382_01.pdf',
 'CenklPorter1984':'https://msp.org/pjm/1984/112-1/pjm-v112-n1-p04-s.pdf',
 'ScheererTanre1991':'https://mat.uab.es/pubmat/fitxers/download/FileType:pdf/FolderName:v35(2)/FileName:35291_05.pdf',
 'Mandell2001':'https://mmandell.pages.iu.edu/papers/einffinal.pdf',
 'BachmannBurklund2026':'https://link.springer.com/content/pdf/10.1007/s00029-026-01141-1.pdf',
}
results=[]
for name,url in sources.items():
 try:
  with urllib.request.urlopen(url,timeout=40) as r:data=r.read()
  assert data.startswith(b'%PDF'),data[:80]
  pdf=dest/(name+'.pdf');pdf.write_bytes(data)
  out=subprocess.run(['pdftotext','-layout',str(pdf),str(dest/(name+'.txt'))],capture_output=True,text=True)
  row={'name':name,'url':url,'bytes':len(data),'pdftotext_returncode':out.returncode,'stderr':out.stderr}
  if name in ('CenklPorter1982','CenklPorter1984','ScheererTanre1991'):
   pages={'CenklPorter1982':[2,3],'CenklPorter1984':[2,11],'ScheererTanre1991':[2]}[name]
   for p in pages:
    render=subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-scale-to','1500','-png','-singlefile',str(pdf),str(dest/(name+'_p'+str(p)))],capture_output=True,text=True)
    row['render_'+str(p)]={'code':render.returncode,'stderr':render.stderr}
 except Exception as e:row={'name':name,'url':url,'error':repr(e)}
 results.append(row);print(json.dumps(row),flush=True)
(dest/'fetch_more_results.json').write_text(json.dumps(results,indent=2)+'\n')
