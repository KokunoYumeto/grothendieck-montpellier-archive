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
real places and every odd prime satisfying Vandiver, hence every
prime below $2^{31}$. The proof combines a general pole-separation
criterion with the integral modular-symbol theorems of Fukaya--Kato
and Wake--Wang-Erickson; no simple-root hypothesis is needed. At every
irregular Vandiver prime the integral Lie abelianization has nonzero
finite primary torsion in infinitely many even weights, so integral odd
generation fails. The examples at $37$ and $691$ locate explicit defects.
At $2$ a central-extension
parity induction constructs adapted Newton generators in every odd
weight and proves integral free generation in all weights. A separate
integral Steinberg-homology source theorem reduces the $K_{12}$ gate to
two specified ranks. The other remaining cases retain explicit gates. Cote 149, scans
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
        s = s.replace(r"\subsection{The full-domain Soul\'e index}", (work/'k_polynomial_section.tex').read_text()+'\n'+(work/'k12_rank_reduction.tex').read_text()+'\n'+r"\subsection{The full-domain Soul\'e index}")
    if name=='tripod_section.tex':
        s = s.replace(r'\subsection{The integral comparison at', (work/'irregular37_section.tex').read_text()+'\n'+(work/'multieven_section.tex').read_text()+'\n'+(work/'pole_nv_section.tex').read_text()+'\n'+(work/'vandiver_kernel_section.tex').read_text()+'\n'+(work/'integral691_section.tex').read_text()+'\n'+r'\subsection{The integral comparison at')
        s = s.replace('The present run supplies no such all-weight theorem, so the irregular-prime field equality remains unresolved here.', 'The following subsections supply an all-weight separation proof at $37$, its general pole criterion, and the modular-symbol input that makes Vandiver alone sufficient. In particular the field equality holds for every prime below $2^{31}$; the remaining all-prime gate is explicit.')
    if name=='tripod_section.tex':
        s += '\n'+(work/'pro2_integral_section.tex').read_text()+'\n'+(work/'pro2_integral_newton_section.tex').read_text()+'\n'+(work/'pro2_integral_class2_section.tex').read_text()+'\n'+(work/'pro2_integral_allweights_section.tex').read_text()+'\n'+(work/'integral_classification_section.tex').read_text()
    if name=='archive_section.tex':
        s += '\n'+(work/'archive_relative_section.tex').read_text()
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
two nonzero trace products and their gcd, or the two localized
Steinberg-homology vanishings in Proposition~\ref{prop:k12-two-ranks}.
The formerly missing rank-$11$ term is now eliminated. The remaining
terms are $H_4(\mathrm{GL}_9;\mathrm{St}_9)$ and
$H_3(\mathrm{GL}_{10};\mathrm{St}_{10})$ over $\mathbb Z[1/13!]$.
Neither of these two computations is claimed here.

\paragraph{OPEN-IRREG-KERNEL: irregular odd primes.}
The proved separation theorem handles cyclic even Iwasawa components of
arbitrary finite rank, including repeated and nonsplit roots.
Fukaya--Kato and Wake--Wang-Erickson supply its cup condition under
Vandiver. Thus Vandiver alone is sufficient, and every prime below
$2^{31}$ is covered. The remaining all-prime question reduces to
Vandiver at the other odd primes, or to an argument that also handles
non-Vandiver modules. The rootwise noncancellation variant no longer
imposes an independent condition within the Vandiver range.

\paragraph{The former OPEN-2-LATTICE gate is closed.}
Theorem~\ref{thm:2-allweights} constructs every adapted Newton lift
by an integral parity correction. Proposition~\ref{prop:newton-basis}
then proves free generation in all weights, and
Proposition~\ref{prop:outer-sat} identifies the actual outer filtration.
The earlier finite and class-two computations remain separate checked
results; neither is extrapolated to obtain the theorem.

\paragraph{OPEN-149-GEOM and the scope of the relative comparison.}
Theorem~\ref{thm:archive-relative} proves the relative normalizer and
tame formal-tube comparison for smooth characteristic-zero bases,
with the manuscript's geometric homotopy-exactness hypothesis retained.
It identifies the finite Chern obstructions and proves splitting
equivalent to triviality of the conormal line when the Picard group
is finitely generated. Recognizing the uncompleted global-unit image
intrinsically inside all splitting classes remains the scan-85 problem.
The concrete extra local class does not prove that such recognition
is impossible. Arbitrary fibrations and wild mixed-characteristic
extensions are outside the proved relative statement.

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
for name in ['k_groups_bibitems.tex','tripod_bibliography.tex','archive_bibliography.tex','framework_bibliography.tex','finite_bibliography.tex','vandiver_kernel_bibliography.tex','k12_rank_bibliography.tex','k12_mpp_bibitems.tex','archive_relative_bibliography.tex']:
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
