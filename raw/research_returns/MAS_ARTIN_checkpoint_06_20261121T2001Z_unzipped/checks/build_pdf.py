#!/usr/bin/env python3
"""Build MAS_ARTIN.pdf from the installed TeX files, without network downloads.

This workspace has pdfTeX and the LaTeX sources but lacks a usable default
format/font-map setup.  The temporary format and maps below repair that setup
without changing the installed distribution.  Run from any directory:
    python3 /path/to/MAS_ARTIN_work/checks/build_pdf.py
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ROOT / "checks"


def main() -> None:
    engine = shutil.which("pdftex")
    if engine is None:
        raise SystemExit("pdftex is required; install a TeX distribution first.")
    roots = [Path("/usr/share/texlive/texmf-dist"), Path("/usr/share/texmf")]
    roots = [p for p in roots if p.is_dir()]
    if not roots:
        raise SystemExit("This fallback expects the installed Debian TeX trees.")
    env = os.environ.copy()
    # Searching the actual trees avoids this workspace's stale ls-R databases.
    env["TEXMF"] = "{" + ",".join(str(p) for p in roots) + "}"
    transcript: list[str] = []

    def run(args: list[str], cwd: Path) -> None:
        result = subprocess.run(args, cwd=cwd, env=env, text=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, check=False)
        transcript.append(result.stdout)
        if result.returncode:
            (CHECKS / "pdf_build_log.txt").write_text("\n".join(transcript))
            raise SystemExit(result.stdout[-8000:])

    with tempfile.TemporaryDirectory(prefix="mas_artin_tex_") as directory:
        temp = Path(directory)
        maps: list[Path] = []
        for tree in roots:
            maps.extend(tree.glob("fonts/map/dvips/lm/lm.map"))
            maps.extend(tree.glob("fonts/map/dvips/amsfonts/*.map"))
            maps.extend(tree.glob("fonts/map/dvips/rsfs/rsfs.map"))
        if not maps:
            raise SystemExit("The installed scalable-font maps were not found.")
        (temp / "pdftex.map").write_text("\n".join(p.read_text() for p in maps))
        env["TEXFONTMAPS"] = str(temp) + os.pathsep
        run([engine, "-etex", "-ini", "-interaction=nonstopmode",
             "-halt-on-error", "-jobname=pdflatex", "-progname=pdflatex",
             "pdflatex.ini"], temp)
        for _ in range(3):
            run([engine, "-fmt=" + str(temp / "pdflatex.fmt"),
                 "-progname=pdflatex", "-interaction=nonstopmode",
                 "-halt-on-error", "MAS_ARTIN.tex"], ROOT)

    (CHECKS / "pdf_build_log.txt").write_text("\n".join(transcript))
    pdf = ROOT / "MAS_ARTIN.pdf"
    final_log = (ROOT / "MAS_ARTIN.log").read_text(errors="replace")
    report: dict[str, object] = {
        "file": pdf.name,
        "bytes": pdf.stat().st_size,
        "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "engine": "pdfTeX with a locally initialized LaTeX format",
        "passes": 3,
        "network_required": False,
        "warnings": re.findall(r"^.*(?:Warning|Overfull|Undefined control).*$",
                               final_log, re.MULTILINE),
    }
    try:
        import fitz
        with fitz.open(pdf) as doc:
            report["pages"] = len(doc)
            outside = []
            for number, page in enumerate(doc, 1):
                bounds = page.rect
                for block in page.get_text("blocks"):
                    if block[6] == 0 and not bounds.contains(fitz.Rect(block[:4])):
                        outside.append({"page": number, "bbox": list(block[:4])})
            report["text_blocks_outside_page"] = outside
    except ImportError:
        report["page_bounds_check"] = "PyMuPDF unavailable; skipped"
    (CHECKS / "pdf_build_report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
