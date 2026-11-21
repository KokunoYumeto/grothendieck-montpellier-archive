from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
work = root / 'work'
out = root / 'K17_package'
out.mkdir(exist_ok=True)

preamble = r'''\documentclass[11pt,a4paper]{article}
\pdfmapfile{+lm.map}
\pdfmapfile{+cm.map}
\pdfmapfile{+cmextra.map}
\pdfmapfile{+symbols.map}
\pdfmapfile{+euler.map}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=27mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{booktabs,longtable,array,enumitem}
\usepackage{xcolor}
\usepackage{microtype}
\usepackage{xurl}
\usepackage[colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black]{hyperref}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{sourcefact}[theorem]{Cited source statement}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\setlength{\emergencystretch}{2em}
\setlength{\parskip}{3pt}
\title{K17: Step 17, the $K$-groups of $\mathbb Z$,\\
Soul\'e characters and the pro-$\ell$ kernels of the tripod}
\author{Research run K17---checked deductions and explicit open gates}
\date{21 November 2026\\Timed checkpoint; research in progress}
\begin{document}
\maketitle
\begin{abstract}
The exact quantitative Selmer theorem behind step 17 is recovered from
the pinned source. Its rational-field specialization, together with
etale $K$-theory and arithmetic duality, bounds the orders of
$K_{4k}(\mathbb Z)$; a reconstruction at fixed levels yields exponent
seven. We separate the exact Vandiver equivalence, full-domain Soul\'e
indices, and the stronger integral generation claims. Complete
deductions settle the pro-$2$ kernel-field equality with unrestricted
real places and every odd prime below $1000$. A general sufficient
criterion uses Vandiver and odd cup-product surjectivity, with no
simple-root hypothesis. Integral odd generation fails at $37$ in
weight $32$ and at $691$ in weight $12$. At $2$ it holds through
weight $18$ by an exact compact-group computation; the all-weight
assertion and the remaining irregular-prime cases retain explicit gates. Cote 149, scans
79--85, is read through exact limiting Kummer sequences, with a concrete
completed-unit class outside the geometric tangent image.

This checkpoint is not the final package. Every completed new proof
has a whole-proof reading recorded in the check ledger. Literature
theorems, exact arithmetic computations and source inspections have
distinct check types. No new Lean build, formal certificate or external
peer review is claimed. Unresolved assertions appear separately.
\end{abstract}
\tableofcontents
\clearpage
\part{Checked deductions and rechecked source statements}
'''

parts = [preamble]
for name in ['step17_section.tex','host_refinement.tex','k_groups_section.tex','tripod_section.tex','archive_section.tex','framework_section.tex']:
    p = work / name
    if not p.exists():
        parts.append(r'\section{Section under active assembly}'+'\n'+name.replace('_',r'\_')+' is being incorporated from its checked research note.\n')
        continue
    s = p.read_text()
    s = s.replace(r'\input{pro2_section.tex}', (work/'pro2_section.tex').read_text())
    if name=='k_groups_section.tex':
        s = s.replace(r"\subsection{The full-domain Soul\'e index}", (work/'k_polynomial_section.tex').read_text()+'\n'+r"\subsection{The full-domain Soul\'e index}")
    if name=='tripod_section.tex':
        s = s.replace(r'\subsection{What remains integral at', (work/'irregular37_section.tex').read_text()+'\n'+(work/'multieven_section.tex').read_text()+'\n'+(work/'integral691_section.tex').read_text()+'\n'+r'\subsection{What remains integral at')
        s = s.replace('The present run supplies no such all-weight theorem, so the irregular-prime field equality remains unresolved here.', 'The following subsections supply an all-weight separation proof at $37$ and its generalization under Vandiver and odd cup-product surjectivity. In particular the field equality holds for every odd prime below $1000$; the remaining all-prime arithmetic conditions are explicit.')
    if name=='tripod_section.tex':
        s += '\n'+(work/'pro2_integral_section.tex').read_text()
    s = re.sub(r'\\texttt\{([^{}]*\.lean[^{}]*)\}',lambda m:r'\path{'+m.group(1).replace(r'\_','_')+'}',s)
    parts.append(s)

parts.append(r'''
\clearpage
\part{Unresolved findings, failed implications, and continuation gates}
\section{Open assertions are not used as theorems}

\paragraph{OPEN-K-NUM: a specified new vanishing degree.}
The existential polynomial order bound and its explicit exponent do
not supply a small numerical constant. A new degree such as $K_{12}$
requires evaluated fixed-level cohomology bounds, or computation of the
two nonzero trace products and their gcd, or a different integral
cohomology calculation. The available primary literature checks and
the exact trace-product reduction are documented in the evidence notes.

\paragraph{OPEN-IRREG-KERNEL: irregular odd primes.}
The proved separation theorem handles cyclic even Iwasawa components of
arbitrary finite rank, including repeated and nonsplit roots. Vandiver
and odd cup-product surjectivity suffice. Published computations verify
both inputs for every odd prime below $1000$. For remaining irregular
primes, the unresolved input is these arithmetic conditions (or a
weaker noncancellation criterion); primes failing Vandiver would also
require an extension to noncyclic even modules.

\paragraph{OPEN-2-LATTICE: integral odd generation at $2$.}
The exact outer-filtration comparison and compact-group calculation
prove integral odd generation through weight $18$. The all-weight gate
is an integral Hall/Newton correction and stability theorem for the
Gamma action. No all-weight proof or counterexample is asserted.

\paragraph{OPEN-149-REL and OPEN-149-GEOM.}
The local root-coordinate obstruction is computed. The complete
relative normalizer/formal-tube comparison in the generality of the
manuscript still requires precise homotopy-exactness and descent
hypotheses. Even after that comparison, recognizing the uncompleted
global-unit image intrinsically inside all splitting classes remains
the scan-85 problem. The concrete extra local class does not prove
that such recognition is impossible.

\paragraph{Source and transcription scope.}
The broader host-field point theorem now has a closed source proof
composition, with its numerical layer bounds retained as premises;
the character theorem and rational-field specialization are also checked. Missing original
round-one B3/S9 text and missing handwritten archive images are not
reconstructed from conjecture. Mathematical editorial flags are
distinguished from verified readings in TRANSCRIPTION\_NOTES.tsv.

\section{Audit conventions and source reproducibility}
CHECK\_EVENTS.tsv records actual source readings, whole-proof checks,
independent re-proofs and exact computations. A cited theorem may be
used with its statement and hypotheses checked without a fresh audit of
its entire original proof; that distinction is retained. The source
contract accepts Alp\"oge's supplied theorems and does not reopen RH.
The pinned mirror, checksums and retrieved Lean excerpts are in the
evidence directory. Research notes also record primary URLs and exact
page or declaration locators. Earlier candidate notes are retained for
continuity but do not supersede the checked paper and latest ledger.

\begin{thebibliography}{99}
''')

seen = set()
for name in ['k_groups_bibitems.tex','tripod_bibliography.tex','archive_bibliography.tex','framework_bibliography.tex','finite_bibliography.tex']:
    p=work/name
    if not p.exists(): continue
    s=p.read_text()
    chunks=re.split(r'(?=\\bibitem\{)',s)
    for c in chunks:
        m=re.match(r'\\bibitem\{([^}]+)\}',c)
        if not m: continue
        if m.group(1) in seen: continue
        seen.add(m.group(1))
        parts.append(c)
parts.append('\\end{thebibliography}\n\\end{document}\n')
(out/'K17.tex').write_text('\n'.join(parts))
print(f'Wrote standalone K17.tex: {(out/"K17.tex").stat().st_size} bytes; {len(seen)} bibliography entries')
