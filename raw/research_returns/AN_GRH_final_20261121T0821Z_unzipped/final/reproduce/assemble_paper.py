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
\providecommand{\mathscr}{\mathcal}
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
conditions, including an all-genus, all-characteristic rational primitive-factor criterion
for odd cyclic degrees prime to the characteristic,
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
numerical tests. A parity improvement gives a separate rational cover test,
and a rank-one curve defeats that size test over every extension. A
prime-power canonical-class criterion supplies prescribed-point rational
primitive factors without size inequalities, and strictly extends the
recovered prime-level detector on an actual curve. A genus-three example
refutes a proposed universal rule for detecting quotients. An exact
degree-seven geometric witness exists on the rank-one numerical-obstruction
curve even though its original rational points all miss the canonical detector.
A quintic reflection construction reduces the genus-two point-section
assertion to ordinary genus-two Jacobians with Rosati-invariant integral real
multiplication by $\mathbf Q(\sqrt5)$. A separate cyclic-cover criterion permits
nonzero rational two-primary Prym torsion of exponent $M$ when
$n>(2M-1)^2$; an exact degree-nineteen example realizes $M=2$.
Every purely two-primary canonical point lies over the field fixing geometric
four-torsion, of degree at most six, and over the degree-six extension in the
real multiplication target case. An ordinary degree-thirteen new factor
separately illustrates the distinction between rational units and geometric
rank zero. The real multiplication class is shown to be nonempty and proper.
Finite-support theta avoidance persists densely on it, including the
ramified prime five, while an actual quintic reflection target has no
rational five-primary canonical component.
An inverse dihedral construction realizes every ordinary real multiplication
curve as a reflection quotient of an etale quintic genus-two cover and
realizes its arbitrary points as actual split transferred images.
A quantitative refinement supplies fixed-field examples where every
lift and every reflection of one quintic cover miss the sufficient
canonical-prime test, including both Weierstrass points on rank-one
sources. A fixed Lang cover gives explicit equidistribution for prescribed
finite primary components and a dense set of canonically detectable target
points, without forcing a prescribed finite transfer fibre to meet that set.
In a tower of characteristic-power constant extensions, an explicit finite
set contains every signed-doubling-eligible torsion prime; all its primary
exponents stabilize in one computable field, although odd theta points
remain infinite. The finite set can contain successful witnesses. In an odd auxiliary-prime
tower, compatible orders instead have at most one new prime and a cofactor
from an explicit finite list; their theta incidence is not supplied.
The bounded-exponent criterion works over the original field with nonconstant
deck group, in every characteristic for genus at most that characteristic,
and otherwise leaves an explicit totally ramified wild elliptic map.
A pointed degree-thirty-nine example has whole Prym exponent two before
deck constantization and sixteen afterwards. Integral semilinear descent
proves equality for each primitive conductor over its own minimal deck field,
while identifying proper-conductor growth as the source of this difference.
An exact Riemann--Roch certificate separately gives three-primary
detectors at both Weierstrass points of a particular rank-one source.
An integral divisor-sign argument eliminates the earlier elliptic exception,
even with nonconstant geometric deck group. The remaining sufficient input
is a pointed rational primitive-factor unit over its specified finite field.
A weighted integral-sign argument further permits a nonzero rational
primitive exponent $M_n$ when $n>(2^{\omega(n)}M_n-1)^2$, in the
range $2\le g\le p$ and with a precise wild elliptic obstruction
in larger genus. This can ignore large proper-conductor torsion. A count of constant twists
gives good unpointed primitive factors, but an exact descent calculation
shows why pointing a different twist restores any original pointed torsion.
Actual norm compatibility and semilinear tower descent bound rational
generator numbers, but leave their orders uncontrolled. Ordinary principally
polarized Weil restrictions show that the listed weights and Frobenius
polynomial shape alone allow exponentially large exponents. A general small
integral-annihilator criterion and a fixed-field lattice construction give
another sufficient bound, with the same wild elliptic obstruction. The bound
requires an estimate on the actual annihilator index; trace relations
factor through earlier levels and do not improve the degree comparison.
Universal existence of such covers, including the residual ordinary real
multiplication case and universal literal primitive-cover existence, remains
open within the requested route.
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
parts = ['premises_section.tex','a1_section.tex','b23_section.tex','positive_rank_intro.tex','finite_prime_avoidance.tex','positive_rank_bridge.tex','lang_weil_criterion.tex','composite_primitive_bridge.tex','composite_theta_example.tex','composite_arithmetic_family.tex','geometric_primitive_bridge.tex','finite_support_theta.tex','no_three_power_theta.tex','generic_odd_torsion.tex','finite_support_avoidance.tex','b3_ordinary_obstruction.tex','frobenius_sidon.tex','lang_pairing_rank_bound.tex','rank_one_augmentation.tex','rank_one_augmentation_obstruction.tex','recovered_canonical_criterion.tex','prime_power_canonical.tex','genus_three_pointing_counterexample.tex','a27_theta_seven.tex','ordinary_rational_witness.tex','quintic_ordinary_reduction.tex','rm5_proper_locus.tex','rm5_nonempty_example.tex','bounded_prym_exponent.tex','bounded_prym_extensions.tex','two_primary_theta_field.tex','reflection_no_five.tex','rm5_finite_support_avoidance.tex','rm5_bad_canonical.tex','pointed_quintic_success.tex','inverse_dihedral.tex','all_reflection_images.tex','fixed_lang_density.tex','rank_one_weierstrass_images.tex','a43_general_target_supplement.tex','pro_two_tower_obstruction.tex','odd_auxiliary_tower.tex','nonconstant_deck_exponent.tex','primitive_integral_sign.tex','bounded_primitive_exponent.tex','bounded_primitive_weil.tex','twists_and_pointing.tex','a48_pullback_iteration.tex','a48_geometric_singular_arrows.tex','odd_quotient_fourier.tex','a49_variable_quotient_supply.tex','partial_packet_operator_limits.tex','norm_compatibility_towers.tex','a51_fox_rationality.tex','a51_transitive_deck.tex','a51_reflection_fields.tex','a51_weighted_weil.tex','small_integral_annihilator.tex','a52_trace_norm_boundary.tex','a52_point_differential.tex','a52_collective_packets.tex','effective_galois.tex','GT_section.tex','row_audit.tex']
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
