from pathlib import Path
import sys,re,csv
ROOT=Path('/workspace/scratch/c38eb4e8f07f')
SRC=ROOT/'sources'
OUT=ROOT/'SA18_work/parts/agent46/outputs'
mode=sys.argv[1]
if mode=='lines':
 p=SRC/sys.argv[2]; start=int(sys.argv[3]); end=int(sys.argv[4])
 lines=p.read_text().splitlines()
 text='\n'.join(f'{i}: {lines[i-1]}' for i in range(start,min(end,len(lines))+1))
elif mode=='entries':
 p=SRC/'SA18_notes/pro/MPL_46_002-048_notes.md'
 lines=p.read_text().splitlines(); heads=[i for i,l in enumerate(lines) if l.startswith('### ')]
 start,end=map(int,sys.argv[2:4]); chunks=[]
 for j in range(start,end+1):
  a=heads[j-1]; b=heads[j] if j<len(heads) else len(lines)
  chunks.append(f'ENTRY MPL_46_002-048#{j}\n'+'\n'.join(f'{i+1}: {lines[i]}' for i in range(a,b)))
 text='\n\n'.join(chunks)
elif mode=='structure':
 p=SRC/sys.argv[2]
 lines=p.read_text().splitlines()
 text='\n'.join(f'{i}: {l}' for i,l in enumerate(lines,1) if any(x in l for x in ['\\cotefile','\\scanpage','\\section','\\subsection','\\mspage']))
else: raise ValueError(mode)
name='read_'+mode+'_'+re.sub('[^A-Za-z0-9_-]+','_', '_'.join(sys.argv[2:]))+'.txt'
(OUT/name).write_text(text+'\n')
print(text)
