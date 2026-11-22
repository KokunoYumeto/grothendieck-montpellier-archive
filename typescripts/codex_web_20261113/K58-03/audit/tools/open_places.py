import json,sys
from pathlib import Path
sys.path.insert(0,'out')
from tex_elements import arguments,page_path,blocks
for n in map(int,sys.argv[1:]):
 s=page_path(n,'out/pages').read_text()
 summ=[]
 for i,(start,end,typ,reading) in enumerate(arguments(s,{'unsure','illegible'}),1):
  left=s[max(start-32,0):start].replace('\n',' ')
  right=s[end:end+34].replace('\n',' ')
  print(f'{n}.{i:02} {left}  «{reading}»  {right}')
