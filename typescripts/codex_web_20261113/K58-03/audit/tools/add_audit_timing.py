from pathlib import Path
import csv,re,datetime
p=Path('out/K58-03_audit.md')
s=p.read_text()
timings=re.findall(r'(?m)^## Scan (\d+)\s*\n(\d{4}-\S+) to (\d{4}-\S+) UTC\.',s)
assert len(timings)==15
with p.open('a') as f:
 print('\n## Duration of the timed second readings\n',file=f)
 print('The intervals below end with the corresponding audited entries. Fourteen of the fifteen intervals lasted under three minutes. Later image comparisons before the freeze and close readings of doubt marks during the witness check are separate from these intervals.\n',file=f)
 print('| Scan | Start UTC | End UTC | Elapsed (min:s) |\n|---|---|---|---:|',file=f)
 for n,start,end in timings:
  dur=int((datetime.datetime.fromisoformat(end.replace('Z','+00:00'))-datetime.datetime.fromisoformat(start.replace('Z','+00:00'))).total_seconds())
  print(f'| {n} | {start} | {end} | {dur//60}:{dur%60:02} |',file=f)
 print('\n## Final collation of overlapping blind differences\n',file=f)
 print('When a place was revisited, the independently written reading and its first decision remain above. Later dispositions at overlapping places follow.\n',file=f)
 print('| Scan | Place | Later disposition |\n|---|---|---|',file=f)
 for r in csv.DictReader(open('out/audit/blind_followup.tsv'),delimiter='\t'):
  print('| '+' | '.join(r.values())+' |',file=f)
