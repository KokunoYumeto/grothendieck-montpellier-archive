from pathlib import Path
import sys,datetime,csv
base=Path(__file__).resolve().parents[1]
p=Path(sys.argv[1]);a=int(sys.argv[2]);b=int(sys.argv[3])
lines=p.read_text().splitlines()
s='\n'.join(f'{i+1:04d} {lines[i]}' for i in range(a-1,min(b,len(lines))))+'\n'
print(s,end='')
out=base/'outputs'/f'{p.stem}_{a}_{b}.txt';out.write_text(s)
with (base/'read_log.tsv').open('a') as f:
 csv.writer(f,delimiter='\t').writerow([datetime.datetime.now(datetime.timezone.utc).isoformat(),str(p),a,min(b,len(lines)),'rendered for researcher; actual reading judged in written analysis'])
