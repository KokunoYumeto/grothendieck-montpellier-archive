#!/usr/bin/env python3
"""Assemble a self-contained paper from the preserved research sections."""
from pathlib import Path
import re, json, datetime
root=Path(__file__).resolve().parent.parent
read=lambda p:(root/p).read_text()
extension=read('sections/A2.tex')
first,e5=extension.split('\\begin{resultenv}{E5}',1)
e5,e6=e5.split('\\begin{resultenv}{E6}',1)
counts=read('sections/counts.tex')
counts=re.sub(r'\\paragraph\{(C\.\d+) \(([^)]+)\): ([^\n]+)\}',
 lambda m:'\\paragraph{Statement '+m[1]+' --- '+m[3]+' ('+('Proved under stated hypotheses' if m[1]=='C.03' else m[2])+')}\\label{'+m[1]+'}',counts)
body=(read('sections/preamble.tex')+read('sections/introduction.tex')
 +'\\section{A.1. The surface and its exact topology}\n'
 +first+read('sections/surface.tex')
 +'\\subsection{The topology formula and the refutation of L1}\n'
 +'The hypotheses in E5 below all hold for the surface of this paper, by T3.\n'
 +'\\begin{resultenv}{E5}'+e5+counts
 +'\\section{A.2. The cellular comparison and Lead L2}\n'
 +'\\begin{resultenv}{E6}'+e6+read('sections/A34.tex')
 +read('sections/L4.tex')+read('sections/audit_scope.tex'))
body=body.replace('SturmfelsZiegler1993','SZ1993')
body=re.sub(r'(\\begin\{resultenv\}\{[^}]+\})\{([^}]+)\}',
 lambda m:m[1]+'{'+('Known' if m[2].startswith('Known') else 'Refuted' if m[2].startswith('Refuted') else 'Proved under stated hypotheses' if m[2].startswith('Proved under') else 'Proved')+'}',body)
body+='\n\\nocite{*}\n\\bibliographystyle{apalike}\n\\bibliography{RESEARCH_SA11_references}\n\\end{document}\n'
(root/'RESEARCH_SA11_paper.tex').write_text(body)
# Merge source records; use one key for the twice independently opened SZ paper.
bib=read('extension.bib')+read('notes/polygons_references.bib')+read('sections/root_references.bib')
bib=re.sub(r'@article\{SturmfelsZiegler1993,.*?(?=\n@)', '', bib,flags=re.S)
(root/'RESEARCH_SA11_references.bib').write_text(bib)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bytes':len(body.encode()),'statements':re.findall(r'\\begin\{resultenv\}\{([^}]+)\}',body)+re.findall(r'\\label\{(C\.\d+)\}',body)}
(root/'audit/assemble_paper.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
