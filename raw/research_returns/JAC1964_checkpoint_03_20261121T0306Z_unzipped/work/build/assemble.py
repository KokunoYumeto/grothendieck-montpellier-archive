from pathlib import Path
import datetime, re
R=Path(__file__).resolve().parents[2]
D=R/'deliverables'
head=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=27mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb,amsthm,mathtools,booktabs,longtable,array}
\providecommand{\mathscr}[1]{\mathcal{#1}}
\usepackage[dvipsnames]{xcolor}
\usepackage{microtype}
\PassOptionsToPackage{hyphens}{url}
\usepackage[hidelinks]{hyperref}
\Urlmuskip=0mu plus 1mu\relax
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
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\title{JAC1964: primitive incidence polarizations,\newline pencil heights, and the arithmetic complement}
\author{Run JAC1964--20261121\\GPT-6 Astra Pro; collaborative mathematical investigation}
\date{21 November 2026\\Working manuscript: continuously checked findings}
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
CM varieties and isolates its complementary height problem. For a
nonzero complementary Fermat-quartic Fourier--Ceresa class, an exact
finite Hodge-lattice calculation and a reproducible theta certificate
prove that its normalized height is greater than $1/100$.
Its central CM orbit is a positive rational plane. Algebraically
trivial cycles in the complementary motive lie in the height radical,
reducing the remaining semipositivity problem to a Griffiths quotient.
The full geometric height on an abelian fourfold pencil is semipositive;
the same holds in higher dimension for geometric-generic axes of the
specified degree. We also prove the primitive polarization on actual
codimension-two algebraic representatives in the stated cases.
The unrestricted seventh theorem, with the customary meaning of
$\tau$-equivalence, is false even for CM abelian threefolds.
Over finite fields and their algebraic closures, the accepted Tate
consequence and Kahn's theorem instead prove rational Chow equal to
numerical equivalence for all varieties of geometric abelian type.
The statement-level audit is in \texttt{CHECK\_EVENTS.tsv}.
Every assertion below distinguishes its hypotheses, check status, and
remaining gate. No general arithmetic Hodge-index theorem is claimed.
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

The attached 032, Theorem 1.1 and Corollaries 8.3--8.4, the supplied
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
parts=[R/'work/programme/sections.tex', R/'work/programme/finite_field_chow.tex',
       R/'work/programme/abelian_type_lefschetz.tex',
       R/'work/root/T4_proof.tex',
       R/'work/root/T4_algebraic_representative.tex',
       R/'work/h9/H9_results.tex', R/'work/h9/H9_monodromy.tex',
       R/'work/programme/H9_T6a.tex',R/'work/h9/H9_full_height.tex',
       R/'work/programme/generic_axis.tex', R/'work/h9/H9_incidence_height.tex',
       R/'work/h9/H9_regular_threefold.tex',
       R/'work/h9/H9_elliptic_reduction.tex',R/'work/h9/H9_base_change.tex',
       R/'work/h9/H9_complete_intersections.tex',
       R/'work/h9/H9_constant_finite_field.tex']
s=head
overview=R/'work/programme/programme_overview.tex'
if overview.exists(): s+=overview.read_text()+'\n'
s+='\n\n'.join(p.read_text() for p in parts)
s+=r'''\section{Checked arithmetic reductions and explicit remaining hypotheses}
The following deductions include conditional implications with substantive
hypotheses. A proved reduction is distinguished from a proof of its
remaining height inequality. The statement-level checking events are
recorded in the accompanying log.
'''
s+=(R/'work/arithmetic/ARITHMETIC_PROOF_FRAGMENT.tex').read_text()
s+=(R/'work/root/AR10_adelic.tex').read_text()
s+=(R/'work/root/AR18_sum_difference.tex').read_text()
s+=(R/'work/arithmetic/FERMAT_LDERIVATIVE_SIGN.tex').read_text()
s+=(R/'work/programme/fermat_hodge_lattice.tex').read_text()
s+=(R/'work/arithmetic/FERMAT_THETA_GATE.tex').read_text()
s+=(R/'work/arithmetic/FERMAT_THETA_CERTIFICATE.tex').read_text()
s+=(R/'work/programme/fermat_cm_orbit.tex').read_text()
s+=(R/'work/programme/fermat_motive_structure.tex').read_text()
s+=(R/'work/arithmetic/FULL_CHOW_GATE.tex').read_text()
s+=(R/'work/arithmetic/FERMAT_KATZ_NONVANISHING.tex').read_text()
s+=(R/'work/h9/H9_conductor_selmer.tex').read_text()
s+=r'''\part{Unresolved assertions and exploratory work}
\section{What remains to be proved}
The full primitive arithmetic height form on the complementary CM Chow
motive remains to be controlled. A formula for one special cycle does
not prove positivity for every cycle. Analytic derivative signs require
an applicable real self-dual $L$-function and a proved height identity
with its local terms and positive constants. The Bost slope inequality
requires an actual canonical height line and a proved norm estimate.
Neither missing input is silently supplied by purity or Dirichlet GRH.
For the specified Fermat class the height sign is now proved directly,
independently of any $L'$-height identity. The remaining Fermat gate is
positivity on its entire Griffiths quotient, together with vanishing
of its algebraically trivial subgroup if strict positivity on rational
Chow is required. The positive CM plane is known, but a spanning
theorem for the whole group has not been proved. The full abelian
endomorphism orbit cannot enlarge that plane.

The geometric H9 assertions cannot be completed in their original form:
the counterexamples above refute the general formula and the asserted
incidence domain. For abelian ambient varieties condition A is automatic.
The full geometric height problem reduces to an explicit primitive
intersection form on the axis. It closes for threefold fibres and for
geometric generic axes in every dimension covered by JAC-P09. These
statements extend through purely inseparable field extensions. For
finite separable covers the old subspace splits orthogonally from the
new norm-zero subspace; positivity on arbitrary new nonalgebraic cycles
is a remaining gate. The algebraically trivial primitive domain is
controlled after every finite extension.
'''
s+=bib
# Break long source URLs introduced by Markdown-to-TeX conversion.
s=s.replace(r'\textasciitilde ', '~')
def wrap_url(match):
    value=match.group(0)
    for escaped,literal in [(r'\_', '_'),(r'\&','&'),(r'\%','%')]:
        value=value.replace(escaped,literal)
    return r'\url{'+value+'}'
s=re.sub(r'(?<!\{)https?://[^\s{}]+', wrap_url, s)
s=re.sub(r'\\texttt\{([^{}]*?/[^{}]*?)\}',
         lambda m:r'\path{'+m.group(1).replace(r'\_','_')+'}',s)
s=s.replace('FERMAT\\_LDERIVATIVE\\_SIGN.md',r'\path{FERMAT_LDERIVATIVE_SIGN.md}')
s=s.replace('work/references/Gu2026.pdf/.txt',r'\path{work/references/Gu2026.pdf} and its extracted text')
s=s.replace(r'\path{LongoVigniWang2025.pdf/.txt}',
            r'\newline\path{LongoVigniWang2025.pdf} and its extracted text')
s=s.replace(r'''\Theta_{P,0}(z,w)=\frac1w+F(z+P)
 +\frac{F(z+P)^2-\wp(z+P)}2w
 +\frac{F(z+P)^3-3F(z+P)\wp(z+P)-\wp'(z+P)}6w^2+O(w^3),''',r'''\begin{aligned}
\Theta_{P,0}(z,w)&=\frac1w+F(z+P)
 +\frac{F(z+P)^2-\wp(z+P)}2w\\
&\quad +\frac{F(z+P)^3-3F(z+P)\wp(z+P)-\wp'(z+P)}6w^2+O(w^3).
\end{aligned}''')
# Keep long cycle-space definitions inside the text block.
s=s.replace(r''' I^p(V)=\{z\in A^p(V):\Gamma_*z=0\text{ in }\mathrm{Pic}^0(T)
 \text{ for every smooth projective }T
 \text{ and }\Gamma\in\mathrm{CH}^{d-p+1}(V\times T)\}.''',r'''\begin{split}
 I^p(V)=\{z\in A^p(V):{}&\Gamma_*z=0\text{ in }\mathrm{Pic}^0(T)\\
 &\text{for every smooth projective }T\text{ and }
 \Gamma\in\mathrm{CH}^{d-p+1}(V\times T)\}.
\end{split}''')
s=s.replace(r''' C_{\rm prim}=\{Z\in\operatorname{CH}^m(X)_{\mathbf Q}:
                          h\operatorname{cl}(Z)=0\},\quad
 R=\operatorname{im}(C_{\rm prim}\to\operatorname{CH}^m(Y)_{\mathbf Q}),
 \quad
 R_0=\operatorname{im}(\operatorname{CH}^m_{\rm hom}(X)_{\mathbf Q}
                         \to\operatorname{CH}^m(Y)_{\mathbf Q}).''',r'''\begin{split}
 C_{\rm prim}&=\{Z\in\operatorname{CH}^m(X)_{\mathbf Q}:
                          h\operatorname{cl}(Z)=0\},\\
 R&=\operatorname{im}(C_{\rm prim}\to\operatorname{CH}^m(Y)_{\mathbf Q}),\\
 R_0&=\operatorname{im}(\operatorname{CH}^m_{\rm hom}(X)_{\mathbf Q}
                         \to\operatorname{CH}^m(Y)_{\mathbf Q}).
\end{split}''')
D.joinpath('JAC1964.tex').write_text(s)
print('assembled',len(s),'characters')
