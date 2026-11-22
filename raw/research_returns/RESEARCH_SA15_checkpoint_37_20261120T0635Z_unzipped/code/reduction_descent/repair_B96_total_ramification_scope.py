from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,difflib
own=Path(__file__).resolve().parents[1]
source=own/'B_full_Iwahori_selected_point_candidate.tex'
old=source.read_text()
before='Let $T/S$ be an actual elementary-abelian degree25 extension of\n'
after='Let $T/S$ be an actual totally ramified elementary-abelian degree25\nextension of\n'
assert old.count(before)==1
new=old.replace(before,after)
out=own/'notes/B96_total_ramification_scope_repair'
out.mkdir(exist_ok=False)
(out/'candidate.before.tex').write_text(old)
(out/'candidate.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='candidate.before.tex',tofile=source.name)))
source.write_text(new)
record={'actual_utc':datetime.now(timezone.utc).isoformat(),
        'reason':'Root full-draft audit requested explicit total ramification in the abstract coefficient lemma, so the fixed residue representatives in the base field are typed correctly. Every actual application already has algebraically closed residue and is totally ramified.',
        'before_sha256':hashlib.sha256(old.encode()).hexdigest(),
        'after_sha256':hashlib.sha256(new.encode()).hexdigest(),
        'mathematical_effect':'Restricts the abstract lemma to the hypotheses used in its proof and in every application; no displayed computation or actual-field conclusion changes.'}
(out/'record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
