"""Retain the second actual bibliography error before correcting plain prose."""
from pathlib import Path
import datetime,json,shutil
w=Path(__file__).resolve().parents[1]
out=w/'outputs/checkpoint27_bibliography_reviewer_fix';assert not out.exists();out.mkdir()
p=w/'notes/root_references.bib';shutil.copy2(p,out/p.name)
s=p.read_text();assert 'search, reduction_descent freshly' in s
s=s.replace('search, reduction_descent freshly','search, the reduction/descent reviewer freshly')
p.write_text(s)
record={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'failure':'Actual build attempt02 stopped on the unescaped underscore in the newly added reviewer name in the Hoshi bibliography note.',
        'repair':'Use ordinary prose reduction/descent reviewer; no mathematical or source-access content changed. Complete failed inputs and logs remain in attempt02.'}
(out/'record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
