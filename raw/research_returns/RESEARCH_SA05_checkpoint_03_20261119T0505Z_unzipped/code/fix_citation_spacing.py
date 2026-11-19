"""Insert missing interword spaces before citations in the manuscript sections."""
from pathlib import Path
import json,re,time
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic();changed=[]
for path in sorted((ROOT/'sections').glob('*.tex')):
    old=path.read_text()
    new,count=re.subn(r'(?<=[A-Za-z0-9)}])(?=\\cite)',r'~',old)
    if count:
        path.write_text(new);changed.append({'path':str(path.relative_to(ROOT)),'spaces_inserted':count})
result={'changes':changed,'seconds':round(time.monotonic()-start,4)}
(ROOT/'code/fix_citation_spacing_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
