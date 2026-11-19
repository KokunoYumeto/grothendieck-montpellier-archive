from pathlib import Path
import sys,json,datetime,csv
base=Path(__file__).resolve().parents[1]
entries=json.loads((base.parents[1]/'research/entries_source.json').read_text())
package=sys.argv[1];a=int(sys.argv[2]);b=int(sys.argv[3])
s='\n\n'.join(f"ENTRY {package}#{i}\nNOTE_LINES {entries[f'{package}#{i}']['start_line']}-{entries[f'{package}#{i}']['end_line']}\n{entries[f'{package}#{i}']['text']}" for i in range(a,b+1))+'\n'
print(s,end='')
(base/'outputs'/f'{package}_entries_{a}_{b}.txt').write_text(s)
with (base/'read_log.tsv').open('a') as f:csv.writer(f,delimiter='\t').writerow([datetime.datetime.now(datetime.timezone.utc).isoformat(),f'{package}_notes.md',f'entry {a}',f'entry {b}','rendered full entries for researcher'])
