"""Split the PDF inspection contact sheet into readable display-sized parts."""
from pathlib import Path
from PIL import Image
import json
import time

ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic()
source=Image.open(ROOT/'build/qa/contact_sheet.png')
outputs=[]
for index,top in enumerate(range(0,source.height,2400),1):
    path=ROOT/f'build/qa/contact_sheet_part_{index:02d}.png'
    source.crop((0,top,source.width,min(top+2400,source.height))).save(path)
    outputs.append(str(path.relative_to(ROOT)))
result={'outputs':outputs,'source_size':list(source.size),'seconds':round(time.monotonic()-start,6),
        'scope':'Display preparation only; no visual-inspection status is inferred.'}
(ROOT/'code/split_qa_contactsheet_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
