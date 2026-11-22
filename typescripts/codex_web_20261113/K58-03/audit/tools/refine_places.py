from pathlib import Path
import csv
from PIL import Image
base=Path('out'); dest=Path('crops')
items='''
21.05 .00 .20 .40 1
21.06 .53 .00 .64 .76
21.09 .16 .12 .47 .96
21.10 .475 .15 .56 .92
23.02 .02 .05 .38 .57
23.03 .15 .42 .77 .98
23.08 .12 .1 .26 .80
23.09 .57 .24 .96 .99
27.03 .00 .22 .24 .93
27.04 .40 .13 .86 .97
27.08 .055 .00 .28 .46
27.09 .37 .19 .9 .91
27.12 .02 .00 .47 .36
27.13 .13 .36 .25 .94
27.14 .01 .39 .40 .78
27.15 .28 .62 .46 .99
27.16 .53 .38 .81 .74
27.18 .49 .77 .96 1
30.08 .74 .19 .845 .86
30.09 .88 .16 .995 .88
30.10 .525 .08 .61 .80
30.11 .76 .03 1 .81
30.12 .00 .35 .46 .64
30.13 .31 .38 .66 .70
30.14 .015 .75 .32 1
30.15 .20 .69 .45 1
30.16 .43 .63 .80 .98
30.20 .32 .17 .58 .65
30.22 .28 .48 .43 1
33.07 .53 .00 .90 .22
33.09a .20 .28 .52 .58
33.13 .49 .105 .67 .34
33.14 .655 .105 .77 .34
33.15 .108 .38 .61 .59
34.09 .41 .51 .62 .69
34.10 .72 .51 .89 .74
'''
boxes={s.split()[0]:list(map(float,s.split()[1:])) for s in items.strip().splitlines()}
path=base/'audit/frozen_places.tsv'
with path.open() as f:
 rd=csv.DictReader(f,delimiter='\t');fn=rd.fieldnames;rows=list(rd)
records=[]
for r in rows:
 if r['id'] not in boxes:continue
 parent=r['crop'];name=r['scan'].zfill(3)+'_focus'+r['id'].split('.')[1]+'.png'
 with Image.open(dest/parent) as im:
  bounds=tuple(round(c*s) for c,s in zip(boxes[r['id']],im.size*2))
  im.crop(bounds).save(dest/name)
 records.append([r['scan'],name,parent,*bounds]);r['crop']=name
with (base/'crop_details.tsv').open('w') as f:
 wr=csv.writer(f,delimiter='\t');wr.writerow(['scan','crop','parent','left','top','right','bottom']);wr.writerows(records)
with path.open('w') as f:
 wr=csv.DictWriter(f,fieldnames=fn,delimiter='\t');wr.writeheader();wr.writerows(rows)
assert len(rows)==len({r['crop'] for r in rows})
print(len(rows),'distinct crops linked')
