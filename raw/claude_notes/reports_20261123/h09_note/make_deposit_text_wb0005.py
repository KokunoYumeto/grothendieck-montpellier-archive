"""H09 v3 -> deposit text for WB-0005 (main session 329fb1e6, Claude Opus 5.5 at effort max, 23 Nov 2026).
Writes h09_note_v4.tex from h09_note_v3.tex: the record link becomes the permanent page WB-0005, and the note on method
names the main session's reading of the edited text."""
import pathlib
NL = chr(10)
H = pathlib.Path(__file__).resolve().parent
t = (H / "h09_note_v3.tex").read_text(encoding="utf-8")
W = "https://github.com/KokunoYumeto/mathematics-workbenches/blob/main/works/WB-0005.md"
reps = [
    (r"\newcommand{\workbenchurl}{https://github.com/KokunoYumeto/zeta-and-l-functions-workbench}" + NL
     + r"\newcommand{\recordurl}{https://github.com/KokunoYumeto/mathematics-workbenches}",
     r"\newcommand{\workbenchurl}{" + W + "}"),
    (r"No human has checked this note. Our text is dedicated to the public domain under CC0~1.0. The workbench is \expandafter\url\expandafter{\workbenchurl}; the permanent records are at \expandafter\url\expandafter{\recordurl}.",
     r"Claude Opus 5.5 at effort max read the edited text again in full before deposit. No human has checked this note. Our text is dedicated to the public domain under CC0~1.0. The records of the checks are at the permanent page of this work, WB-0005: \expandafter\url\expandafter{\workbenchurl}."),
]
for old, new in reps:
    n = t.count(old)
    assert n == 1, (old[:70], n)
    t = t.replace(old, new)
assert "recordurl" not in t
(H / "h09_note_v4.tex").write_text(t, encoding="utf-8", newline=NL)
print("wrote h09_note_v4.tex")
