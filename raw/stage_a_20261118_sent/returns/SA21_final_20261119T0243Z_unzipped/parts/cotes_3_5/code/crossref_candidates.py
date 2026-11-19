"""Locator aid only. Human/model reads both endpoints before a link is kept."""
from pathlib import Path
import re,json
O=Path(__file__).resolve().parents[1];B=O.parents[2];out=[]
for ch in (3,4,5):
 for p in sorted((B/'sources/texts/codex').glob(f'J156-{ch}-*_transcription.tex')):
  scan='?'
  for n,line in enumerate(p.read_text().splitlines(),1):
   m=re.search(r'\\scanpage\{([^}]+)\}',line)
   if m:scan=m.group(1)
   if re.search(r'(?:\bp\.|page|GF\s*[IVX]|CF\s*[IVX]|ci-dessus|plus haut|plus bas)',line):
    out.append({'file':p.name,'scan':scan,'line':n,'text':line})
(O/'outputs/crossref_candidates.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
for i,r in enumerate(out,1):print(f"{i}: {r['file']} scan{r['scan']} line{r['line']}: {r['text']}")
