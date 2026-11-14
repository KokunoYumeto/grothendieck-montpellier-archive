#!/usr/bin/env python3
"""Assemble a standalone English guide from the explicit editorial manifest."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
from edition_core import read_tsv,write_tsv,sha256,tex_escape
from edition_render import PREAMBLE,CREDIT,RIGHTS_EN

EDITION=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--partial",action="store_true",help="Label a working guide and print explicit notices for missing sections")
    args=parser.parse_args()
    manifest=EDITION/"records/GUIDE_PARTS.tsv"
    entries=read_tsv(manifest)
    known={r["file"] for r in entries}
    unlisted=sorted(p.name for p in (EDITION/"guide_parts").glob("*.tex") if p.name not in known)
    missing=[r for r in entries if r.get("required","true")=="true" and not (EDITION/"guide_parts"/r["file"]).is_file()]
    working=[r["file"] for r in entries if (EDITION/"guide_parts"/r["file"]).is_file()
             and re.search(r"(?mi)^%\s*WORKING GUIDE\b",(EDITION/"guide_parts"/r["file"]).read_text())]
    if not args.partial and (missing or unlisted):
        raise SystemExit("Guide is incomplete: missing "+", ".join(r["id"] for r in missing)+"; unlisted parts "+", ".join(unlisted))
    if not args.partial and working:
        raise SystemExit("Guide parts retain explicit working status: "+", ".join(working))
    if args.partial:
        entries+= [dict(id="unplaced-"+Path(name).stem,title="Unplaced working guide material",file=name,required="false") for name in unlisted]
    hashes={"records/GUIDE_PARTS.tsv":sha256(manifest.read_text()),
            "scripts/build_guide.py":sha256(Path(__file__).read_text()),
            "scripts/edition_render.py":sha256((EDITION/"scripts/edition_render.py").read_text())}
    pre=PREAMBLE.replace("@MODE@","2").replace("@FRENCH@",r"\EditionFrenchfalse").replace("@FORM@","Guide to the manuscripts")
    pre=pre.replace("% A single-file reader generated from the common annotated page master.",
        "% A standalone guide assembled from the explicit editorial section manifest.")
    body=pre+r"""
\begin{document}
\selectlanguage{english}
\hypersetup{pageanchor=false}
\begin{titlepage}\thispagestyle{empty}\vspace*{20mm}
{\Large Alexandre Grothendieck\par}\vspace{12mm}
{\Huge\bfseries Nouveau EGA V\par}\vspace{8mm}
{\Large Guide to the manuscripts\par}\vspace{7mm}
{\large French prenotes and Piotr Blass's English typescript\par}\vspace{12mm}
"""
    if args.partial:
        body+=r"{\large\bfseries\color{deletedred}INCOMPLETE CHECKPOINT --- GUIDE IN PROGRESS\par}\vspace{10mm}"+"\n"
    body+="Université de Montpellier, fonds Grothendieck\\\\ Cotes 25 and 24\\\\\n14 November 2026\n"
    body+=r"\vfill\end{titlepage}\clearpage\hypersetup{pageanchor=true}"+"\n"
    body+=r"\section*{Provenance, credit, and rights}"+"\n"+tex_escape(CREDIT)+".\n\n"
    body+="Guide written by GPT-6 Astra (OpenAI, ChatGPT Pro mode).\n\n"
    body+="Cote 25 is described in the archive as dated “[à partir de 1967-1987]”. Cote 24 is Piotr Blass's translation typescript dated 1987.\n\n"
    body+="The translation in cote 24 is Piotr Blass's (1987); the rights in it belong to its translator or his heirs.\n\n"
    body+="The Grothendieck Circle scan EGA5.pdf, the P. and J. Blass translations (2004), J. C. Reinhold's web re-edition, and the Centre for Grothendieckian Studies item L49d are published texts not reproduced and not consulted for any reading. Published EGA references used for mathematical context are identified in the guide's editorial discussions and reference section.\n\n"
    body+=tex_escape(RIGHTS_EN)+"\n\n"
    if args.partial and missing:
        body+=r"\section*{Working-guide status}"+"\nThe following sections still await editorial assembly: "+tex_escape("; ".join(r["title"] for r in missing))+".\n\n"
    body+=r"\clearpage\gdef\CurrentScanLabel{Guide}"+"\n"
    status=[]
    for entry in entries:
        path=EDITION/"guide_parts"/entry["file"]
        exists=path.is_file()
        status.append(dict(part_id=entry["id"],title=entry["title"],file="guide_parts/"+entry["file"],
            status="included" if exists else "missing required part" if entry.get("required","true")=="true" else "optional part absent",
            sha256=sha256(path.read_text()) if exists else ""))
        if not exists:
            if args.partial and entry.get("required","true")=="true":
                body+=r"\subsection*{"+tex_escape(entry["title"])+r"}"+"\n"+r"\textit{This section is pending in the working guide.}"+"\n\n"
            continue
        part=path.read_text()
        if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]",part):
            raise SystemExit("Control character in guide part "+entry["file"])
        if re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|/(?:workspace|home|tmp|mnt|usr)/",part):
            raise SystemExit("Private path or address in guide part "+entry["file"])
        hashes["guide_parts/"+entry["file"]]=sha256(part)
        slug="guide-"+entry["id"]
        body+=r"\par\typeout{EGA-SOURCE-BEGIN "+slug+r" PDF-PAGE \thepage}"+"\n"
        body+=r"\pdfbookmark[1]{"+tex_escape(entry["title"])+r"}{source:"+slug+"}\n"
        body+=part.rstrip()+"\n"+r"\par\typeout{EGA-SOURCE-END "+slug+r" PDF-PAGE \thepage}"+"\n\n"
    body+=r"\end{document}"+"\n"
    path=EDITION/"readers/EGA_V_GUIDE.tex";path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body)
    expected=dict(reader="EGA_V_GUIDE",source_pages=0,guide_parts=sum(r["status"]=="included" for r in status),
        logical_link_marks=dict(scan=0,unsure=0,illegible=0,provenance=0),reader_sha256=sha256(body),
        source_files_sha256=hashes,typesetting_patch_source_keys=[],source_page_marks={},
        working_parts=working,status="INCOMPLETE CHECKPOINT" if args.partial else "assembled; compilation pending")
    (EDITION/"records/LINK_EXPECTATIONS_EGA_V_GUIDE.json").write_text(json.dumps(expected,ensure_ascii=False,indent=2)+"\n")
    write_tsv(EDITION/"records/GUIDE_ASSEMBLY.tsv",status)
    print(json.dumps(dict(file="readers/EGA_V_GUIDE.tex",included=expected["guide_parts"],missing=[r["id"] for r in missing],unlisted=unlisted,working=working,partial=args.partial)))


if __name__=="__main__":
    main()
