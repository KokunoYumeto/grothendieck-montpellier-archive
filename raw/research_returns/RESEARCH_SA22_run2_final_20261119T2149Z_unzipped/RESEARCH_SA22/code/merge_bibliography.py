#!/usr/bin/env python3
"""Assemble component bibliography files and check keys and access notes."""
from pathlib import Path
import re, json
root=Path(__file__).resolve().parents[1]
files=["A_references.bib","A567_references.bib","B_references.bib","C_references.bib","ROOT_references.bib"]
parts=[(root/f).read_text() for f in files]
text="\n\n".join(parts)
keys=re.findall(r"@\w+\s*\{\s*([^,\s]+)",text)
assert len(keys)==len(set(keys)), "Duplicate bibliography keys"
entries=re.split(r"(?=@\w+\s*\{)",text)
unmarked=[re.search(r"@\w+\s*\{\s*([^,\s]+)",e).group(1)
          for e in entries if e.strip() and not re.search(r"\bopened\b",e,re.I)]
assert not unmarked,unmarked
(root/"RESEARCH_SA22_references.bib").write_text(text)
out={"entries":len(keys),"source_files":files,"access_note_check":"all marked opened/not opened"}
(root/"logs"/"bibliography_merge.json").write_text(json.dumps(out,indent=2))
print(json.dumps(out))
