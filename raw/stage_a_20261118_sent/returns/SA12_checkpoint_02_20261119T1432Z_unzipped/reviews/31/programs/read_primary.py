from pathlib import Path
import sys,datetime,json
root=Path('/workspace/scratch/a77a578fa7d4/SA12_work/reviews/31')
name=sys.argv[1];a=int(sys.argv[2]);b=int(sys.argv[3])
p=root/'external'/f'{name}.txt'
lines=p.read_text().split('\n')
text='\n'.join(f'{i+1}: {lines[i]}' for i in range(a-1,min(b,len(lines))))
dest=root/'outputs'/f'primary_{name}_{a:05d}_{b:05d}.txt';dest.write_text(text+'\n')
with (root/'primary_read_log.tsv').open('a') as f:f.write('\t'.join([datetime.datetime.now(datetime.timezone.utc).isoformat(),name,str(a),str(b),str(dest.relative_to(root))])+'\n')
print(text)
