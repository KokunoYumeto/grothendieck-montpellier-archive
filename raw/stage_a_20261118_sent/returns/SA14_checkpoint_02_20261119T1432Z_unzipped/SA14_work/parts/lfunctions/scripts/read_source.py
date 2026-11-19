"""Print and save explicitly requested source ranges; never produce verdicts."""
from pathlib import Path
import sys,datetime,csv
part=Path(__file__).resolve().parents[1]
root=part.parents[2]
names={'t1':'sources/SA14_texts/pro/MPL_60_002-035_transcription.tex','t2':'sources/SA14_texts/pro/MPL_60_036-070_transcription.tex','n1':'sources/SA14_notes/pro/MPL_60_002-035_notes.md','n2':'sources/SA14_notes/pro/MPL_60_036-070_notes.md','d1':'sources/SA14_notes/pro/MPL_60_002-035_doubts.md','d2':'sources/SA14_notes/pro/MPL_60_036-070_doubts.md'}
p=root/names.get(sys.argv[1],sys.argv[1]); lines=p.read_text().splitlines()
lo=int(sys.argv[2]) if len(sys.argv)>2 else 1
hi=min(int(sys.argv[3]),len(lines)) if len(sys.argv)>3 else len(lines)
out='\n'.join(f'{i+1:04d} {lines[i]}' for i in range(lo-1,hi))+'\n'
(part/'outputs').mkdir(exist_ok=True,parents=True)
(part/'outputs'/f'read_{sys.argv[1]}_{lo}_{hi}.txt').write_text(out)
with (part/'read_log.tsv').open('a') as f:
    csv.writer(f,delimiter='\t').writerow([datetime.datetime.now(datetime.timezone.utc).isoformat(),str(p.relative_to(root)),lo,hi,'printed to researcher; source reading, not proof check'])
print(out)
