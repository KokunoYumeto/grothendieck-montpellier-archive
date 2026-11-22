from pathlib import Path
import fitz,sys,time
cote=sys.argv[1];pages=[int(a) for a in sys.argv[2:]]
p=Path('RESEARCH_SA23/sources/category_manuscript_'+cote+'.pdf')
d=fitz.open(p);print(cote,'pages',len(d))
for n in pages:
 if n>len(d):print('OUT OF RANGE',n);continue
 t=time.monotonic();pix=d[n-1].get_pixmap(matrix=fitz.Matrix(1.2,1.2))
 out=p.parent/('category_scan_'+cote+'_'+str(n).zfill(3)+'.png');pix.save(out)
 print(n,out,pix.width,pix.height,'seconds',time.monotonic()-t)
