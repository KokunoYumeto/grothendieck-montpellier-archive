import fitz
from pathlib import Path
p=Path('RESEARCH_SA23/sources/category_manuscript_161-5.pdf')
d=fitz.open(p)
for pg,rect,name in [(23,(110,70,580,350),'023_top'),(27,(60,180,580,490),'027_bottom'),(28,(70,60,580,750),'028_all')]:
 q=d[pg-1].get_pixmap(matrix=fitz.Matrix(2.5,2.5),clip=fitz.Rect(*rect));out=p.parent/('category_scan_1615_'+name+'.png');q.save(out);print(out)
