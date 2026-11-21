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
and Wake--Wang-Erickson; no simple-root hypothesis is needed. More generally, the one-variable Greenberg
condition that the plus Iwasawa module is finite suffices, through a
bounded rational-coordinate argument on the entire arithmetic group. At every
irregular prime satisfying this condition the integral Lie abelianization has nonzero
finite primary torsion in infinitely many even weights, so integral odd
generation fails. The examples at $37$ and $691$ locate explicit defects.
At $2$ a central-extension
parity induction constructs adapted Newton generators in every odd
weight and proves integral free generation in all weights. A separate
integral Steinberg-homology source theorem removes the rank-eleven term
from a finite $K_{12}$ criterion; a boundary-degree indexing discrepancy
in the older cell data is explicitly isolated. The other remaining
cases retain explicit gates. Cote 149, scans 79--85, is read through
exact limiting Kummer sequences. A marked generic Galois diagram
determines the geometric tangent subset, whereas the isolated normalizer
extension does not.

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
        s = s.replace(r"\subsection{The full-domain Soul\'e index}", (work/'k_polynomial_section.tex').read_text()+'\n'+(work/'host_uniformity_section.tex').read_text()+'\n'+(work/'k12_rank_reduction.tex').read_text()+'\n'+(work/'k12_index_safe_section.tex').read_text()+'\n'+(work/'k12_double_building_section.tex').read_text()+'\n'+(work/'k12_orientation_section.tex').read_text()+'\n'+(work/'k12_survivor_section.tex').read_text()+'\n'+(work/'k12_survivor_boundary_section.tex').read_text()+'\n'+(work/'k12_survivor_coface_section.tex').read_text()+'\n'+r"\subsection{The full-domain Soul\'e index}")
    if name=='tripod_section.tex':
        s = s.replace(r'\subsection{The integral comparison at', (work/'irregular37_section.tex').read_text()+'\n'+(work/'multieven_section.tex').read_text()+'\n'+(work/'pole_nv_section.tex').read_text()+'\n'+(work/'vandiver_kernel_section.tex').read_text()+'\n'+(work/'cup_ext_pole_section.tex').read_text()+'\n'+(work/'greenberg_kernel_section.tex').read_text()+'\n'+(work/'integral691_section.tex').read_text()+'\n'+r'\subsection{The integral comparison at')
        s = s.replace('The present run supplies no such all-weight theorem, so the irregular-prime field equality remains unresolved here.', 'The following subsections supply an all-weight separation proof at $37$, its general pole criterion, and the modular-symbol input that makes Vandiver alone sufficient. In particular the field equality holds for every prime below $2^{31}$; the remaining all-prime gate is explicit.')
    if name=='tripod_section.tex':
        s += '\n'+(work/'pro2_integral_section.tex').read_text()+'\n'+(work/'pro2_integral_newton_section.tex').read_text()+'\n'+(work/'pro2_integral_class2_section.tex').read_text()+'\n'+(work/'pro2_integral_allweights_section.tex').read_text()+'\n'+(work/'integral_classification_section.tex').read_text()+'\n'+(work/'greenberg_integral_corollary.tex').read_text()
    if name=='archive_section.tex':
        s += '\n'+(work/'archive_relative_section.tex').read_text()+'\n'+(work/'archive_generic_recognition_section.tex').read_text()
    s = re.sub(r'\\texttt\{([^{}]*\.(?:lean|py)[^{}]*)\}',lambda m:r'\path{'+m.group(1).replace(r'\_','_')+'}',s)
    parts.append(s)

parts.append(r'''
\clearpage
\part{Unresolved findings, failed implications, and continuation gates}
\section{Open assertions are not used as theorems}

\paragraph{OPEN-K-NUM: a specified new vanishing degree.}
The existential polynomial order bound and its explicit exponent do
not supply a small numerical constant. A new degree such as $K_{12}$
requires evaluated fixed-level cohomology bounds, or computation of the
two nonzero trace products and their gcd, or the three localized
Steinberg-homology vanishings in Proposition~\ref{prop:k12-three-ranks}.
The rank-$11$ term is eliminated independently. A dimension discrepancy
in the older enumeration leaves the announced $H_5(\mathrm{GL}_8;\mathrm{St}_8)$
endpoint without an independently checked source proof; it is retained
along with $H_4(\mathrm{GL}_9;\mathrm{St}_9)$ and
$H_3(\mathrm{GL}_{10};\mathrm{St}_{10})$ over $\mathbb Z[1/13!]$.
None of these three computations is claimed here.
Proposition~\ref{prop:k12-double-building} gives an alternative finite
criterion in terms of three explicitly identified double-building
homology groups for the last two ranks, with the rank-eight endpoint
still separate. These hypotheses remain unproved.
The small-index orientation elimination is proved, but
Proposition~\ref{prop:k12-orientation-survivor} gives an explicit
index-three chain generator with no orientation reverser. A full
vanishing proof must therefore address cycles and boundaries, not
just eliminate every cell by stabilizer parity.
Proposition~\ref{prop:k12-survivor-boundary} now supplies explicit
boundaries with coefficient one for the two displayed surviving
cycles; it does not cover the remaining cells.

\paragraph{OPEN-IRREG-KERNEL: irregular odd primes.}
The proved separation theorem handles cyclic even Iwasawa components of
arbitrary finite rank, including repeated and nonsplit roots.
Fukaya--Kato and Wake--Wang-Erickson supply its cup condition under
Vandiver, and Theorem~\ref{thm:greenberg-kernel} now extends the
conclusion to the weaker one-variable hypothesis that $X^+$ is finite.
It retains the entire free pro-$p$ group and permits bounded rational
Iwasawa coordinates and repeated roots. The remaining all-prime
question therefore reduces to Greenberg at the remaining primes, or
to a further argument with a positive-rank plus Iwasawa module.
Every prime below $2^{31}$ is already covered without that conjectural
hypothesis. The proof does not give a converse to Greenberg.

\paragraph{The former OPEN-2-LATTICE gate is closed.}
Theorem~\ref{thm:2-allweights} constructs every adapted Newton lift
by an integral parity correction. Proposition~\ref{prop:newton-basis}
then proves free generation in all weights, and
Proposition~\ref{prop:outer-sat} identifies the actual outer filtration.
The earlier finite and class-two computations remain separate checked
results; neither is extrapolated to obtain the theorem.

\paragraph{Scan-85 recognition: proved scope and the remaining marking.}
Theorem~\ref{thm:archive-generic} proves that a splitting over the
smooth normal arithmetic base is geometric exactly when its generic
restriction is geometric; no Picard finite-generation assumption is
needed for this equivalence.
Proposition~\ref{prop:archive-marked-recognition} determines that
subset from the full curve diagram with the marked generic absolute
Galois group over an identified number field. This is a functorial
recognition statement, not an effective finite-quotient algorithm.
Proposition~\ref{prop:archive-bare-extension} proves that the isolated
normalizer extension cannot determine the subset, even with its
cyclotomic inertia action. Recovering the additional generic marking
from a smaller unmarked diagram is not established. Arbitrary
fibrations and wild mixed-characteristic extensions are outside the
proved relative statement.

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
for name in ['k_groups_bibitems.tex','tripod_bibliography.tex','archive_bibliography.tex','framework_bibliography.tex','finite_bibliography.tex','vandiver_kernel_bibliography.tex','k12_rank_bibliography.tex','k12_mpp_bibitems.tex','archive_relative_bibliography.tex','greenberg_kernel_bibliography.tex','greenberg_integral_bibliography.tex','archive_recognition_bibliography.tex','k12_orientation_bibitems.tex','k12_index_bibliography.tex','k12_survivor_bibitems.tex','host_uniformity_bibliography.tex']:
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
