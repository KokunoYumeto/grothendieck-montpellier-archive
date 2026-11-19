from pathlib import Path
import argparse,re,csv,datetime
ROOT=Path('/workspace/scratch/208fb206de03')
BASE=ROOT/'work/parts/cote64_late'
p=argparse.ArgumentParser();p.add_argument('kind',choices=['notes','tex','doubts','index']);p.add_argument('package');p.add_argument('start',type=int,nargs='?',default=1);p.add_argument('end',type=int,nargs='?',default=9999);a=p.parse_args()
if a.kind=='index':
 rows=list(csv.DictReader((ROOT/'sources/SA16_notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
 out='\n'.join('\t'.join([r['entry_id'],r['heading'],r['kind'],r['scans_cited']]) for r in rows if r['package']==a.package)
else:
 path=ROOT/'sources'/('SA16_texts/pro' if a.kind=='tex' else 'SA16_notes/pro')/(a.package+('_transcription.tex' if a.kind=='tex' else '_'+a.kind+'.md'))
 lines=path.read_text().splitlines();out=[]
 if a.kind=='notes':
  entry=0
  for n,l in enumerate(lines,1):
   if l.startswith('### '):entry+=1
   if a.start<=entry<=a.end:out.append(f'{n:04d} [entry {entry}] {l}')
 elif a.kind=='tex':
  scan=0
  for n,l in enumerate(lines,1):
   m=re.search(r'\\scanpage\{(\d+)\}',l)
   if m:scan=int(m[1])
   if a.start<=scan<=a.end:out.append(f'{n:04d} [scan {scan}] {l}')
 else:
  out=[f'{n:04d} {l}' for n,l in enumerate(lines,1) if a.start<=n<=a.end]
 out='\n'.join(out)
name=f'{a.kind}_{a.package}_{a.start}_{a.end}.txt'
(BASE/'outputs'/name).write_text(out+'\n')
with (BASE/'progress.log').open('a') as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+'\tREAD\t'+name+'\n')
print(out)
