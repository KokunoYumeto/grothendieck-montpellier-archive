#!/usr/bin/env python3
"""Mirror the authoritative directly maintained B56.tex contribution.

The proof source is edited directly; no hidden generator is needed to
reconstruct it. This records the final section normalization and creates
the secondary TeX and Markdown mirrors used in the working documentation.
"""
from pathlib import Path
import datetime
import json
import subprocess
import time

started = time.perf_counter()
work = Path(__file__).resolve().parents[1]
source = work / "B56.tex"
text = source.read_text()
text = text.replace(r"\subsubsection{", r"\subsection{")
source.write_text(text)
(work / "agent_B56.tex").write_text(text)
subprocess.run([
    "pandoc", str(source), "--from=latex", "--to=markdown+tex_math_dollars",
    "--wrap=none", "--output=" + str(work / "agent_B56_proofs.md")
], check=True)
print(json.dumps({
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "authoritative_source": str(source),
    "section_headings": [line for line in text.splitlines()
                         if line.startswith(r"\section{")],
    "tex_mirror_identical": source.read_bytes() == (work / "agent_B56.tex").read_bytes(),
    "markdown_bytes": (work / "agent_B56_proofs.md").stat().st_size,
    "seconds": round(time.perf_counter() - started, 9)
}, indent=2))
