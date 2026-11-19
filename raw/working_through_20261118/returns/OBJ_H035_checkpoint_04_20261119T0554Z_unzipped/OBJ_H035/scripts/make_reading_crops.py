"""Human-selected crops only. No OCR or manuscript text recognition."""
from pathlib import Path
from PIL import Image
import csv
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'OBJ_H035_work/readings'
items=[
 (2,'cover_invariants',(1300,610,1710,1140)),
 (3,'lemma1',(185,745,1660,1230)),
 (4,'prop3_quantifiers',(230,1650,1660,2100)),
 (5,'prop4_finite_values',(280,1760,1660,1990)),
 (6,'lemma5_conditions',(320,1340,1660,1760)),
 (7,'question_mark',(1290,1650,1665,1790)),
 (8,'finite_F_N',(220,1340,1560,1590)),
 (9,'undefined_M',(205,1270,1660,1790)),
 (10,'P_in_complex',(220,730,1430,960)),
 (10,'Z1_Tor',(450,1400,1470,1520)),
 (11,'header',(290,25,1580,235)),
 (11,'EGA_margin',(30,1640,345,1960)),
 (12,'abs_definition',(100,430,1650,660)),
 (12,'root_unity_exponent',(100,1560,1630,1870)),
 (13,'cancelled_definitions',(330,1220,1660,1470)),
 (15,'strict_cancelled',(270,200,1570,650)),
 (16,'vi_nonzero',(340,1710,1580,1990)),
 (20,'R_F_gr',(345,845,1570,1510)),
 (21,'s_in_S',(320,200,1565,485)),
 (22,'programme',(300,190,1580,750)),
 (23,'missing_pushforward',(400,1570,1580,1850)),
 (24,'Murre',(350,1170,1570,1390)),
]
with (OUT/'CROP_MANIFEST.tsv').open('w') as o:
 w=csv.writer(o,delimiter='\t');w.writerow(['file','source','box','scale'])
 for scan,name,box in items:
  p=ROOT/'sources'/('OBJ_H035_scans/94_scan%03d.jpg'%scan if scan<=13 else 'additional_scans/94_scan-%02d.jpg'%scan)
  im=Image.open(p).crop(box)
  im=im.resize((im.width*2,im.height*2))
  dest=OUT/('94_%03d_%s.jpg'%(scan,name));im.save(dest,quality=90)
  w.writerow([dest.name,str(p.relative_to(ROOT)),','.join(map(str,box)),2])
  print(dest.name,im.size)
