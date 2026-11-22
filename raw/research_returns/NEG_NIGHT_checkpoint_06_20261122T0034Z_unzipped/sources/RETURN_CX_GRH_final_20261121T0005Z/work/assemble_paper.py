#!/usr/bin/env python3
"""Assemble the self-contained paper from reviewed component fragments."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
W = ROOT / 'work'
D = ROOT / 'deliverables'
D.mkdir(exist_ok=True)

preamble = r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=25mm,headheight=14pt]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{booktabs,longtable,array}
\usepackage{microtype}
\usepackage{xcolor}
\usepackage{xurl}
\usepackage[unicode,colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black]{hyperref}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small CX\_GRH: exact hypotheses and transfers}
\fancyhead[R]{\small 21 November 2026}
\fancyfoot[C]{\thepage}
\setlength{\parskip}{4pt}
\setlength{\parindent}{0pt}
\setlength{\emergencystretch}{2em}
\setcounter{tocdepth}{2}
\title{\textbf{CX\_GRH}\\[5pt]
\large What the stipulated Dirichlet GRH and ETH theorems,\newline
and the conditional all-number-field Hecke claim,\newline
change in computational complexity}
\author{Research run CX\_GRH-20261121}
\date{21 November 2026 (Europe/Berlin)}
\begin{document}
\maketitle
\begin{abstract}
We identify the analytic premise at the point where it enters each
selected algorithm and then prove the corresponding transfer.
The stipulated Dirichlet theorem covers the Miller--Bach test,
prime-field nonresidues, and qualified primitive-root and
extension-field constructions. Koiran's general AM proof uses
Dedekind zeta functions of bounded, possibly nonnormal solution fields;
it is covered by the all-number-field Hecke claim, conditionally on
that claim. We preserve the equation-access and output-size distinctions
in GCT~V, the degree dependence of finite-field factoring, and the
separate search costs in class-group computation. The supplied ETH
theorem refutes the usual exponential-time hypotheses and gives
explicit parameter-preserving counting transfers and its stated
nearly linear Boolean circuit lower bound. These deductions supply
no P/NP or VP/VNP separation or collapse. A separate part carries
every finding into schemes over $\mathbb Z$, finite étale covers,
representation $K_0$, exterior and Schur operations, Hilbert schemes,
and the appropriate weight and Artin-motive language. Exact source
locators, inspected archive scans, proof checks, and unresolved
extensions are recorded explicitly.
\end{abstract}
\clearpage
\tableofcontents
\clearpage
\part{Checked analytic and computational findings}
'''

def read(name):
    return (W / name).read_text(encoding='utf-8')

parts = [preamble, read('root_intro.tex'), read('koiran_gct.tex'),
         read('number_algorithms.tex'), read('koiran_quadratic_transfer.tex')]
if (W / 'number_automorphism_gate.tex').exists():
    parts.append(read('number_automorphism_gate.tex'))
if (W / 'eth_factoring_composition.tex').exists():
    parts.append(read('eth_factoring_composition.tex'))
if (W / 'koiran_factoring_gate.tex').exists():
    parts.append(read('koiran_factoring_gate.tex'))
parts += [read('eth_consequences.tex'),
          r'\clearpage\part{Checked geometric restatements and dictionaries}',
          read('koiran_geometry.tex'), read('eth_geometry.tex'),
          read('root_geometry.tex'),
          r'\clearpage\part{Unproved extensions and verification record}',
          read('paper_scope.tex'), r'\clearpage\begin{thebibliography}{99}']

bibnames = ['root_bibliography.tex','koiran_bibliography.tex',
            'number_bibliography.tex','eth_bibliography.tex']
if (W/'koiran_factoring_bibliography.tex').exists():
    bibnames.append('koiran_factoring_bibliography.tex')

seen = set()
for name in bibnames:
    for item in re.split(r'(?=\\bibitem\{)', read(name)):
        match = re.match(r'\\bibitem\{([^}]+)\}', item)
        if match and match.group(1) not in seen:
            seen.add(match.group(1)); parts.append(item)
parts += [r'\end{thebibliography}', r'\end{document}']

text = '\n\n'.join(parts)
aliases = {'Gao2001':'CXNGao01', 'IKRS2008':'CXNIKRS08',
           'BachSorenson96':'CXNBachSorenson96'}
for old,new in aliases.items():
    # Normalize references and remove duplicate entries separately below.
    text = re.sub(r'(?<=\{)'+re.escape(old)+r'(?=[,}])',new,text)
    text = re.sub(r'(?<=,)'+re.escape(old)+r'(?=[,}])',new,text)
seen = set(); cleaned=[]
for chunk in re.split(r'(?=\\bibitem\{)',text):
    m = re.match(r'\\bibitem\{([^}]+)\}',chunk)
    if m and m.group(1) in seen:
        # Duplicate final entries must not remove the document suffix.
        suffix = re.search(r'\\end\{thebibliography\}[\s\S]*',chunk)
        if suffix: cleaned.append(suffix.group())
        continue
    if m: seen.add(m.group(1))
    cleaned.append(chunk)
text=''.join(cleaned)
citations=set()
for match in re.finditer(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',text):
    citations.update(match.group(1).split(','))
missing=sorted(citations-seen)
if missing: raise SystemExit(1)
# Retrieval-only leads remain in the source-audit notes; the paper's
# bibliography contains the sources actually cited by its final text.
trimmed=[]
for chunk in re.split(r'(?=\\bibitem\{)',text):
    m=re.match(r'\\bibitem\{([^}]+)\}',chunk)
    if m and m.group(1) not in citations:
        suffix=re.search(r'\\end\{thebibliography\}[\s\S]*',chunk)
        if suffix: trimmed.append(suffix.group())
        continue
    trimmed.append(chunk)
text=''.join(trimmed)
(D/'CX_GRH.tex').write_text(text,encoding='utf-8')
print(f'Assembled {len(text):,} characters; {len(citations)} bibliography entries; missing citations: {missing}')
