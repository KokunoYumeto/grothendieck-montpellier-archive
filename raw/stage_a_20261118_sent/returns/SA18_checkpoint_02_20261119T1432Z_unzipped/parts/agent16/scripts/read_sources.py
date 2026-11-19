from pathlib import Path
import re,sys,datetime,json
BASE=Path('/workspace/scratch/c38eb4e8f07f/sources')
OUT=Path('/workspace/scratch/c38eb4e8f07f/SA18_work/parts/agent16')
files={
 'text':BASE/'SA18_texts/pro/MPL_16+47+54+44_transcription.tex',
 'notes':BASE/'SA18_notes/pro/MPL_16+47+54+44_notes.md',
 'doubts':BASE/'SA18_notes/pro/MPL_16+47+54+44_doubts.md',
}
for p in (BASE/'SA18_notes/second_pass/MPL_16+47+54+44').glob('*.md'):
 files[p.stem]=p
key=sys.argv[1]
p=files[key]
lines=p.read_text().splitlines()
a=int(sys.argv[2]) if len(sys.argv)>2 else 1
b=int(sys.argv[3]) if len(sys.argv)>3 else len(lines)
content='FILE '+str(p)+'\n'+'\n'.join(f'{i}: {lines[i-1]}' for i in range(a,min(b,len(lines))+1))
name=f'{key}_{a}_{b}.txt'
(OUT/'outputs'/name).write_text(content+'\n')
with (OUT/'read_log.tsv').open('a') as f:
 f.write(f'{datetime.datetime.now(datetime.timezone.utc).isoformat()}\t{key}\t{a}\t{b}\t{name}\n')
print(content)
