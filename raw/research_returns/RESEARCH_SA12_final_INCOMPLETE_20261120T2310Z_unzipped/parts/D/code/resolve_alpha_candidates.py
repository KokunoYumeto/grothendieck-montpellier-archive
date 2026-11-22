"""Archive the failed common-refinement argument and clean the table generator.

The mathematical replacement is in paper_D.tex.  The archived text is an
explicitly failed proof attempt and is not included in the checked report.
"""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
unresolved = root / "unresolved_D.tex"
text = unresolved.read_text()
marker = r"\subsection{D.7:"
changed = marker in text
if changed:
    prefix, failed = text.split(marker, 1)
    archive = root / "sources" / "failed_alpha_argument.tex"
    archive.write_text(
        "% FAILED ARGUMENT: archived 2026-11-20 after the finite counterexample\n"
        "% D:alpha-common-refinement refuted its assertions. Do not cite as proof.\n"
        + marker + failed
    )
    unresolved.write_text(prefix.rstrip() + "\n")

generator = root / "code" / "prepare_checkpoint.py"
code = generator.read_text()
summary = code[code.index("summaries={"):]
header = '''"""Regenerate Part D result and check-event tables from current fragments."""
from pathlib import Path
import csv, re, json

root=Path(__file__).resolve().parents[1]
paper=root/'paper_D.tex'
candidate=''

'''
generator.write_text(header + summary)
out = {
    "failed_candidate_archived": changed,
    "remaining_unresolved_fragment": "D.1/D.2(ii) fixed-boundary gate",
    "generator_now_read_only_on_tex": True,
}
(root / "code" / "resolve_alpha_candidates_output.json").write_text(
    json.dumps(out, indent=2) + "\n"
)
print(json.dumps(out, indent=2))
