"""Assemble the standalone AN_GRH.tex from the retained, checked section sources."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
src = root/'proof_sources'
preamble = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm]{geometry}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\setsansfont{Latin Modern Sans}
\setmonofont[Scale=0.87]{Latin Modern Mono}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{array,longtable,booktabs}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=MidnightBlue,citecolor=MidnightBlue,urlcolor=MidnightBlue,pdftitle={AN GRH: Anabelian point separation and effective Galois bounds},pdfauthor={AN GRH research audit}}
\usepackage{enumitem}
\setlist{itemsep=2pt,topsep=5pt}
\setlength{\parindent}{1.2em}
\setlength{\parskip}{3pt}
\setlength{\emergencystretch}{2em}
\renewcommand{\arraystretch}{1.15}
\newcommand{\et}{\mathrm{\acute et}}
\title{\textbf{AN\_GRH}\\[7pt]Anabelian point separation, cyclotomic certificates,\\and effective Galois bounds}
\author{Research audit of the supplied programme sources\\GPT-6 Astra Pro; run of 21 November 2026}
\date{21 November 2026 (Europe/Berlin)}
\begin{document}
\maketitle
\begin{abstract}
We reconstruct and check an unconditional proof of the curve point-separation
assertion A1 from the recovered later run. The requested Hooley route has a
separate geometric premise: we prove that its universal primitive-root theta
condition is false by a six-prime obstruction on an explicit genus-two curve.
We prove weaker prime-power and composite primitive-factor sufficient
conditions, including an all-genus characteristic-two geometric criterion,
with exact rank-one examples of degrees $13$ and $15$ and an
ordinary example of degree $4159$. A Lang--Weil test and its fixed-prime
limitation give a curve-dependent numerical route. Under M, a Hooley--Lenstra
calculation supplies a positive-density family of composite candidate orders.
Generic curves on both positive-rank strata avoid every nonzero odd torsion
order. For each fixed finite prime support, all geometric theta torsion is
confined to an explicit finite field; one rank-one example has no nonzero
three-primary theta point. No fixed finite prime support works uniformly over
finite fields, even allowing all exponents and products. A separate ordinary
example defeats the older large-prime quotient test over every constant
extension, despite having a theta witness. Frobenius-orbit and Weil-pairing
arguments give further exact restrictions on candidate primes and successful
numerical tests. The universal
positive-rank finite-field incidence or primitive-orbit coverage question
remains open.
Under the stipulated Alp\"oge theorem, Bach's applicable general unit-generator
constant is $3$, while exact unconditional coefficient-$2$ certificates are
provided for $53$ moduli and two infinite families. The Masullo draft claim
supplies specified Dedekind-GRH effective Chebotarev consequences, including
explicit full adic semisimplification tests. The audit covers every supplied
flag and all $800$ recovered full register rows, with $591$ available proof
blocks. The missing $390$ full register statements and $209$ further LM7
proof blocks prevent an exhaustive audit of the stated $1190$-row source set.
No proof through Hooley, formal verification of this paper, or verification
of Masullo's unfinished main theorem is claimed.
\end{abstract}
\tableofcontents
\clearpage
\part{Checked findings and precisely scoped cited consequences}
'''
parts = ['premises_section.tex','a1_section.tex','b23_section.tex','positive_rank_intro.tex','finite_prime_avoidance.tex','positive_rank_bridge.tex','lang_weil_criterion.tex','composite_primitive_bridge.tex','composite_theta_example.tex','composite_arithmetic_family.tex','geometric_primitive_bridge.tex','finite_support_theta.tex','no_three_power_theta.tex','generic_odd_torsion.tex','finite_support_avoidance.tex','b3_ordinary_obstruction.tex','frobenius_sidon.tex','lang_pairing_rank_bound.tex','effective_galois.tex','GT_section.tex','row_audit.tex']
contents = []
for name in parts:
 text = (src/name).read_text()
 if name=='GT_section.tex':
  text=text.replace(r'\input{GT_unit_table.tex}',(src/'GT_unit_table.tex').read_text())
 if name=='row_audit.tex':
  text=text.replace('Chapter V, Theorem 3.23, printed p.~164.',r'Chapter V, Theorem 3.23, printed p.~164 \cite{MilneCFT}.')
  text+=r'''
\paragraph{Proof of the new scope assertions R01--R03.}
For R01, the retained inventory parses all original flag records and
all recovered CSV registers, counts distinct run/statement identifiers,
and locates the numbered source blocks. Every claimed recovery has a
source hash; the nine LM7 block identifiers are separately listed.
This proves availability counts, not correctness of every source proof.
For R02 the full A.69 text spells out both genus and rank formulas,
while the other flag literally reports the disabled GRH option.
For the finite-prime claim in R03, Frobenius acts on primitive
$\ell$th roots as multiplication by $p$, so their minimal-polynomial
degrees are exactly $\operatorname{ord}_\ell(p)$. It follows that
$\Phi_\ell$ is irreducible precisely in the stated case, without
producing such a prime. For the displayed pair estimate, with the explicitly defined Lang
eigensheaves geometrically nontrivial, character
orthogonality gives $\sum_bN_b^2=|A|^{-1}\sum_\chi|S_\chi|^2$.
The trivial character contributes $N^2$ and every nontrivial one
contributes at most $(2g-2)^2q$ by the cited finite-field trace bound.
Subtracting $\sum_bN_b=N$ gives the formula. The stronger prime
existence and geometric implications are treated, with full proofs
or exact cited hypotheses, in A02--A06 and G01--G05.
'''
 contents.append(text)
ending = '\\clearpage\n\\part{Unchecked inputs and remaining gates}\n'+(src/'open_section.tex').read_text()+'\n\\clearpage\n'+(src/'bibliography.tex').read_text()+'\n\\end{document}\n'
(root/'AN_GRH.tex').write_text(preamble+'\n\n'.join(contents)+ending)
print('Wrote standalone AN_GRH.tex')
