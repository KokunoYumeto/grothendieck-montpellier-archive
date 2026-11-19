#!/usr/bin/env python3
import sys,pathlib,fitz,json
p=pathlib.Path(sys.argv[1]);d=fitz.open(p)
out='\n'.join(f'\n===== PDF PAGE {i+1} =====\n'+page.get_text() for i,page in enumerate(d))
q=p.with_suffix('.txt');q.write_text(out)
print(json.dumps({'pdf':str(p),'text':str(q),'pages':len(d),'characters':len(out)}))
