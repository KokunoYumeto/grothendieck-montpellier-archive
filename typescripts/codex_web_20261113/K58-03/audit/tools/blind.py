from pathlib import Path
import csv,sys,json
n=int(sys.argv[1]); p=Path('out')
data=json.load(sys.stdin)
for fn,header,rows in [('K58-03_blind.tsv',['scan','place','what the crop shows'],data['rows']),('audit/blind_words.tsv',['scan','words and accents before opening the page'],[[data['words']]])]:
 dest=p/fn;init=not dest.exists()
 with dest.open('a',newline='') as f:
  w=csv.writer(f,delimiter='\t')
  if init:w.writerow(header)
  for row in rows:w.writerow([str(n)]+row)
