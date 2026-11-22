"""Retain CP27 bibliography compile failure and fix its literal TeX paths."""
from pathlib import Path
import datetime,json,shutil
w=Path(__file__).resolve().parents[1]
out=w/'outputs/checkpoint27_bibliography_path_fix';assert not out.exists();out.mkdir()
p=w/'notes/root_references.bib';shutil.copy2(p,out/p.name)
s=p.read_text()
assert 'notes/post_CP26_four_squares_source_read.md.' in s
s=s.replace('notes/post_CP26_four_squares_source_read.md.',
            '\\path{notes/post_CP26_four_squares_source_read.md}.')
assert 'epsilon_Fon definition' in s
s=s.replace('epsilon_Fon definition','epsilon\\_Fon definition')
p.write_text(s)
record={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'failure':'Actual build attempt01 failed at the raw underscore in the Hardy/Wright bibliography note; the complete actual inputs and log are retained.',
        'repair':'Use path macro for the literal filename and escape the Hoshi note underscore; no mathematical or source-access claim changed.'}
(out/'record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
