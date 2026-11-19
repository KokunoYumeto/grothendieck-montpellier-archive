"""Normalize the six verified bibliography flags; retain every detail in annote."""
from pathlib import Path
import re,json,datetime
R=Path(__file__).resolve().parents[1];p=R/'references.bib';s=p.read_text()
seen=[]
def normalize(m):
 seen.append(m.group(1));return ' note = {verified},\n annote = {'+m.group(1)+'}'
t=re.sub(r'(?m)^ note = \{verified; (.*)\}$',normalize,s)
assert len(seen) in (0,6),len(seen)
assert len(re.findall(r'(?m)^ note = \{verified\},$',t))==6
assert len(re.findall(r'(?m)^ annote = \{',t))==6
p.write_text(t)
out={'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'changed_records':len(seen),'verified_flags':6,'annote_fields':6,'metadata_preserved':True}
(R/'outputs/normalize_bib_notes_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
with (R/'progress.log').open('a') as f:f.write(out['time_utc']+'\tBibliography metadata normalized: note={verified}; original details retained in annote; no mathematics changed.\n')
