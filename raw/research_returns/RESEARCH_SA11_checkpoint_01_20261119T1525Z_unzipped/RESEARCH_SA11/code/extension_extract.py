from pathlib import Path
import re
root=Path('/workspace/scratch/eccd14a17414')
paths=list((root/'input/RESEARCH_SA11_transcriptions/transcriptions/154_Pro').glob('*transcription.tex'))
for p in paths:
 s=p.read_text()
 s=re.sub(r'\\figure\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}', '[FIGURE]', s, flags=re.S)
 (root/'RESEARCH_SA11_work/audit'/('extension_'+p.stem+'.txt')).write_text(s)
print('Extracted figure-free LaTeX from',len(paths),'files; figures omitted only for prose search, originals unchanged.')
