"""Record new bibliography entries after the 99-entry dependency audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
old = json.loads((ROOT/'notes/category_status_source_extended_extract.json').read_text())
# That preserved overbroad first pass recorded 98 of the old 99 entries.
# The remaining entry is RobertAV2023, separately inspected in the audit.
baseline = {row['key'] for row in old['rows']} | {'RobertAV2023'}
assert len(baseline) == old['entry_count'] == 99
bib = ROOT/'RESEARCH_SA23_references.bib'
text = bib.read_text()
starts = list(re.finditer(r'^@\w+\{([^,]+),', text, re.M))
entries = {match.group(1):text[match.start():starts[i+1].start() if i+1<len(starts) else len(text)]
           for i,match in enumerate(starts)}
new = []
for key in sorted(set(entries)-baseline):
    uses = []
    for path in sorted((ROOT/'sections').glob('*.tex')):
        for lineno,line in enumerate(path.read_text().splitlines(),1):
            if key in line:
                uses.append({'path':str(path.relative_to(ROOT)), 'line':lineno,'text':line})
    new.append({'key':key,'entry':entries[key].strip(),'uses':uses})
record = {'utc':datetime.now(timezone.utc).isoformat(),
          'initial_entries':len(baseline),'current_entries':len(entries),
          'bib_sha256':hashlib.sha256(bib.read_bytes()).hexdigest(),
          'new_entries':new,'removed_keys':sorted(baseline-set(entries))}
(ROOT/'notes/category_status_source_checkpoint06_delta.json').write_text(
    json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
