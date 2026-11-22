#!/usr/bin/env python3
"""Reproducible source locators and citation audit of arXiv:2511.22614v4.

Reads source in ../../sources/CaradotLin.  Suppressed \\delete{...} bodies and
comments are replaced by spaces while preserving original line numbers.
This is a text audit, not a proof that there is no unstated mathematical use.
"""
import hashlib, json, re, time
from pathlib import Path

started=time.perf_counter()
root=Path(__file__).resolve().parents[2]
source=root/"sources/CaradotLin/HOMOTOPY_LIE_ALGEBRA.tex"
raw=source.read_text()
chars=list(raw)

def blank(a,b):
    for j in range(a,b):
        if chars[j] != "\n": chars[j]=" "

# Comments, including any command looking strings inside them.
for match in re.finditer(r"(?<!\\)%[^\n]*",raw): blank(match.start(),match.end())
active="".join(chars)
start_document=active.index(r"\begin{document}")
pos=start_document
deleted=[]
while True:
    m=re.search(r"\\delete\s*\{",active[pos:])
    if m is None: break
    a=pos+m.start(); j=pos+m.end(); depth=1
    while j<len(active) and depth:
        if active[j]=="{" and (j==0 or active[j-1]!="\\"): depth+=1
        elif active[j]=="}" and (j==0 or active[j-1]!="\\"): depth-=1
        j+=1
    assert depth==0
    deleted.append([raw.count("\n",0,a)+1,raw.count("\n",0,j)+1])
    blank(a,j); pos=j
active="".join(chars)

def line_at(pos):return raw.count("\n",0,pos)+1
events=[]
for m in re.finditer(r"\\section\*?\{|\\appendix|\\begin\{(theorem|lemma|proposition|corollary|conjecture|definition|remark|remarks|example|examples)\}|\\(?:eqref|ref|cref)\{([^}]+)\}|\\label\{([^}]+)\}",active[start_document:]):
    events.append((start_document+m.start(),m))
section=0; count=0; appendix=False; current="front matter"; labels={}; refs=[]; statements=[]
for p,m in events:
    command=m.group(0)
    if command.startswith(r"\appendix"): appendix=True; section=0; count=0
    elif command.startswith(r"\section"):
        if not command.startswith(r"\section*"): section+=1; count=0
    elif m.group(1):
        count+=1
        section_name=chr(64+section) if appendix else str(section)
        current=f"{m.group(1)} {section_name}.{count}"
        statements.append({"statement":current,"source_line":line_at(p)})
    elif m.group(2): refs.append({"from":current,"target_label":m.group(2),"source_line":line_at(p)})
    elif m.group(3): labels[m.group(3)]={"containing_statement":current,"source_line":line_at(p)}

prop_start=active.index(r"\begin{proposition}",active.index(r"\subsection{Lifting properties}"))
prop_end=active.index(r"\end{proposition}",prop_start)
prop_labels=re.findall(r"\\label\{([^}]+)\}",active[prop_start:prop_end])
refs_to_prop=[r for r in refs if r["target_label"] in prop_labels]
literal_310=[line_at(m.start()) for m in re.finditer(r"3\.10",active)]
literal_310_details=[]
for line in literal_310:
    # No source prose copied: identify the actual reference by a fixed label.
    literal_310_details.append({"line":line,"context":"Gulliksen--Levin bibliographic proposition, not the audited proposition"})

pdf=root/"sources/CaradotLin/2511.22614v4.pdf"
pdftext=root/"sources/CaradotLin/2511.22614v4.txt"
pages=pdftext.read_text().split("\f")
page_hits={name:[i+1 for i,page in enumerate(pages) if name in page] for name in
           ("Proposition 3.10", "Theorem 3.15", "Corollary 3.16", "Theorem 4.13")}
out={"source":str(source.relative_to(root)),"source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
     "pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),
     "source_lines":len(raw.splitlines()),"suppressed_delete_blocks":deleted,
     "numbered_statement_count":len(statements),"numbered_statements":statements,
     "proposition_3_10_source_lines":[line_at(prop_start),line_at(prop_end)],
     "proposition_3_10_labels":prop_labels,"references_to_its_labels":refs_to_prop,
     "active_literal_3_10_occurrences":literal_310_details,
     "references_to_comparison_and_free_extension":[r for r in refs if r["target_label"] in
        ("thm:3.15","cor:3.16","thm:freeness_TS")],
     "pdf_page_hits":page_hits,"elapsed_seconds":time.perf_counter()-started}
dest=root/"deliverable/logs/B_source_audit.json"
dest.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:out[k] for k in ("source_sha256","source_lines","numbered_statement_count","proposition_3_10_source_lines","proposition_3_10_labels","active_literal_3_10_occurrences","references_to_comparison_and_free_extension","pdf_page_hits","elapsed_seconds")},indent=2))
