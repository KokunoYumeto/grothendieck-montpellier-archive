from pathlib import Path
import re, sys, datetime
root=Path('/workspace/scratch/208fb206de03')
kind,start,end=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
part=root/'work/parts/cote62'
if kind=='notes':
    p=root/'sources/SA16_notes/pro/MPL_62_002-050_notes.md'
    chunks=re.split(r'(?m)^### ',p.read_text())
    out='\n\n'.join('ENTRY '+str(n)+' ### '+chunks[n] for n in range(start,end+1))
else:
    if kind=='text': p=root/'sources/SA16_texts/pro/MPL_62_002-050_transcription.tex'
    elif kind=='doubts': p=root/'sources/SA16_notes/pro/MPL_62_002-050_doubts.md'
    elif kind.endswith('_notes'): p=root/('sources/SA16_notes/codex/'+kind+'.md')
    else: p=root/('sources/SA16_texts/codex/'+kind+'_transcription.tex')
    lines=p.read_text().splitlines()
    out='\n'.join(f'{n}: {lines[n-1]}' for n in range(start,min(end,len(lines))+1))
out=str(p.relative_to(root))+'\n'+out
(part/'outputs'/f'read_{kind}_{start}_{end}.txt').write_text(out)
with (part/'progress.log').open('a') as f:
    f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+f'\tREAD\t{kind} {start}-{end}\n')
print(out)
