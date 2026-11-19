"""Print requested scan blocks with original transcription file and line numbers."""
from pathlib import Path
import re,sys
root=Path(__file__).resolve().parents[2]/'input/RESEARCH_SA08_transcriptions/transcriptions'
want=set()
for arg in sys.argv[1:]:
    a,_,b=arg.partition('-')
    want.update(range(int(a),int(b or a)+1))
for path in sorted(root.glob('*transcription.tex')):
    lines=path.read_text().splitlines()
    scan=None
    for i,line in enumerate(lines,1):
        m=re.search(r'\\scanpage\{(\d+)\}',line)
        if m: scan=int(m.group(1))
        if scan in want: print(f'{path.name}:{i}: {line}')
