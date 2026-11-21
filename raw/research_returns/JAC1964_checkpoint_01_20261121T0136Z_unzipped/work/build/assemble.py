from pathlib import Path
import datetime
R=Path('/workspace/scratch/77a2c5da2d9d')
D=R/'deliverables'
head=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=27mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb,amsthm,mathtools,booktabs,longtable,array}
\usepackage[dvipsnames]{xcolor}
\usepackage{microtype}
\usepackage[hidelinks]{hyperref}
\usepackage{enumitem}
\setlist{itemsep=3pt,topsep=5pt}
\setlength{\parskip}{4pt}
\setlength{\parindent}{0pt}
\setlength{\emergencystretch}{3em}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
\DeclareMathOperator{\CH}{CH}
\DeclareMathOperator{\Pic}{Pic}
\DeclareMathOperator{\NS}{NS}
\DeclareMathOperator{\End}{End}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\Alb}{Alb}
\title{JAC1964: primitive incidence polarizations,\newline pencil heights, and the arithmetic complement}
\author{Run JAC1964--20261121\\GPT-6 Astra Pro; collaborative mathematical investigation}
\date{21 November 2026\\Working manuscript: checkpoint version}
\begin{document}
\maketitle
\begin{abstract}
Accepting the supplied 032 results, we prove that the correctly signed
primitive incidence self-duality of an odd-dimensional abelian variety is
a rational polarization in every characteristic. An explicit quadric
pencil refutes the proposed uncorrected H9 height identity, even when
all fibres are geometrically integral and the restricted cycles are
rationally zero. We give the admissible local correction and a precise
no-correction criterion. Algebraic Lefschetz correspondences prove the
restriction and fixed-part assertions of the sixth theorem. An
all-primes monodromy argument also determines the variable incidence
sign under explicit Lefschetz monodromy hypotheses. The arithmetic
investigation constructs an actual orthogonal Chow Picard summand for
CM varieties and isolates its complementary height problem. A Fermat
quartic Ceresa class shows that this complement is nonempty.
The unrestricted seventh theorem, with the customary meaning of
$\tau$-equivalence, is false even for CM abelian threefolds.
This is a checkpoint manuscript; the statement-level audit is in
\texttt{CHECK\_EVENTS.tsv}. Its arithmetic additions are still being
extended and reviewed. No general arithmetic Hodge-index theorem is
claimed.
\end{abstract}
\tableofcontents
\newpage
\section{Scope, inputs, and conventions}
All new deductions are labelled by stable finding IDs. ``Proved'' means
proved from the explicitly accepted and cited inputs, with the
whole-proof reading recorded in the check log; it does not mean formal
verification. The model effort setting is not exposed in this session.
The original archive images were not supplied, so the transcription
audit is mathematical, not palaeographic.

The incidence interpretation of the higher Picard variety is specified
below. We work with rational cycles and rational homomorphisms of
abelian varieties, clearing denominators on actual families. We do not
tensor geometric point groups with $\mathbf Q$ to define varieties.
No integral universal cycle or principal polarization is asserted.

The attached 032, Theorem 1.1 and Corollary 8.4, the supplied
van Hoften--Sempliner and Milne reports, and Alp\"oge's advertised
Riemann-hypothesis and Dirichlet-GRH statements are accepted as inputs,
as requested. Their full proofs and the omitted Lean dependency tree
were not independently certified here. The bridge sketch and H9 are
questions to test, not input theorems. The exact scopes of the analytic
inputs are recorded in the arithmetic section.

\part{Checked findings and cited background}
'''
bib=r'''\begin{thebibliography}{99}
\bibitem{Saito1979} H. Saito, \emph{Abelian varieties attached to cycles of intermediate dimension}, Nagoya Math. J. 75 (1979), 95--119. Definition 3.1; Proposition 3.4; Theorem 3.6; \S4.1; Proposition 4.4; Corollary 4.5; Theorem 4.6; Proposition 5.2. \url{https://doi.org/10.1017/S0027763000024855}.
\bibitem{Kleiman68} S. L. Kleiman, \emph{Algebraic cycles and the Weil conjectures}, in Dix expos\'es sur la cohomologie des sch\'emas (1968), 359--386, Theorem 2A11.
\bibitem{MilneAV} J. S. Milne, \emph{Abelian Varieties}, course notes, v2.00 (2008), Chapter I, Theorem 11.1; Chapter III, Theorem 6.8 and Summary 6.11. \url{https://www.jmilne.org/math/CourseNotes/AV.pdf}.
\bibitem{MumfordAV} D. Mumford, \emph{Abelian Varieties}, Oxford University Press, 1970. Chapter II, \S6, Application 1, p.~60; Chapter III, \S16, Index Theorem, p.~155.
\bibitem{ConradAV} B. Conrad, \emph{Abelian varieties}, notes by T. Feng (2015), Example 4.2.14, p.~38.
\bibitem{SGA7I} A. Grothendieck et al., \emph{Groupes de monodromie en g\'eom\'etrie alg\'ebrique, I}, SGA 7 I, Lecture Notes in Mathematics 288, Springer, 1972. Expos\'e IX, \S9.2, 10.3.5 (p.~443), Theorem 10.4 (p.~444), \S\S12.5 and 12.7.
\bibitem{SGA7II} P. Deligne and N. Katz, eds., \emph{Groupes de monodromie en g\'eom\'etrie alg\'ebrique, II}, SGA 7 II, Lecture Notes in Mathematics 340, Springer, 1973. Expos\'e XV, 3.3.3--3.3.6, pp.~191--192; XVII, \S2.2; XVIII, 5.3.2--5.3.5, pp.~287--288, Proposition 6.2, p.~319, Corollary 6.4, 6.7.2; XX, Theorem 4.1 and Remark 4.3, pp.~355--356.
\bibitem{Bloch1984L} S. Bloch, \emph{Algebraic cycles and values of L-functions}, J. reine angew. Math. 350 (1984), 94--108. Lemma 3.1, p.~99; Theorem 4.1, p.~104; Proposition 5.2, p.~107.
\end{thebibliography}
\end{document}
'''
parts=[R/'work/programme/sections.tex', R/'work/root/T4_proof.tex',R/'work/h9/H9_results.tex', R/'work/h9/H9_monodromy.tex']
s=head+'\n\n'.join(p.read_text() for p in parts)
s+=r'''\part{Arithmetic proof drafts and unresolved gates}
This part contains full arithmetic proof drafts, including conditional
lemmas whose hypotheses are substantive. The current checking status is
recorded by finding ID in the event log. Inclusion here does not assert
that the remaining arithmetic height-sign problem has been solved.
'''
s+=(R/'work/arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex').read_text()
s+=r'''\section{What remains to be proved}
The full primitive arithmetic height form on the complementary CM Chow
motive remains to be controlled. A formula for one special cycle does
not prove positivity for every cycle. Analytic derivative signs require
an applicable real self-dual $L$-function and a proved height identity
with its local terms and positive constants. The Bost slope inequality
requires an actual canonical height line and a proved norm estimate.
Neither missing input is silently supplied by purity or Dirichlet GRH.

The geometric H9 assertions cannot be completed in their original form:
the counterexamples above refute the formula and the asserted incidence
domain. Their repaired statements are the explicitly stated admissible
formula, no-correction criterion, and conditional quotient lemma.
'''
s+=bib
D.joinpath('JAC1964.tex').write_text(s)
print('assembled',len(s),'characters')
