# D.1–D.4 and E.4–E.6: outcome and proof audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026.
Run: /root/real_weil. No priority is claimed. This report is a contribution
to the parent manuscript, not a replacement for the unresolved gates.

## Outcome table

| Item | Outcome | Statement IDs |
|---|---|---|
| C.3 local contribution | Full Picard restriction has an explicit exact additive kernel of dimension three for every N>=4. Ordinary Chow algebraic equivalence is different: in that cone example J1 restricts isomorphically, whereas the same additive kernel survives in Pic/Pic_alg. For arbitrary excellent normal strictly henselian local k-algebras with algebraically closed coefficient/residue field k and regular punctures, N>=3, ordinary restriction has zero kernel in characteristic zero and p-primary torsion kernel in characteristic p; rational J1 is injective in every characteristic. Prime-to-residue torsion Picard restriction is injective even without a coefficient field for arbitrary excellent normal strictly henselian rings with N>=3 and regular punctured divisor. A second explicit deformation refutes ordinary J1 surjectivity in every N>=4 over C: the source ordinary Pic_alg is zero and the target contains a nontorsion Fermat-Jacobian family. | C.3i–k, C.3m–n |
| D.1 | Exact slope-parity domain and Galois packet proved. The D(Q) repair is false. The q=25 example is fully computed. Full-category and full even-weight parity distinguished. | D.1a–e |
| D.2 | Complete orbit calculation for finite-type real tori; exact rational lattice invariant and explicit failure of rational transitivity. Full categories handled. Arbitrary infinite-rank transitivity is not claimed. | D.2a–b |
| D.3 | Infinite order of the actual relative gerbe class under R3's Tate-dependent band identification; therefore no canonical-involution lift. Coherent order-two lifting criterion proved in a compatible cocycle presentation. | D.3a–b |
| D.4 | The unqualified slope construction is undefined in an even-weight example. The quotient positivity criterion and effectivity-cone equivalence are proved. CM/Lefschetz reduction cases and arbitrary polarized abelian families with typed specialization functors are verified; abelian-type finite-field effectivity follows under the explicitly cited 2026 primary preprint theorem. Within the stated numerical framework, even Frobenius-identity effectivity is equivalent to the full Tate cycle conjecture. General geometric compatibility and motives outside the abelian-type category remain unresolved. | D.4a–g |
| E.4 | All finite-field groups in every twist, including the p-part, are proved. Exact integral identification is refuted and corrected; the compactified trace is identified. A coherent bounded integral family on every specified finite-prime open is constructed in all twists, with actual Artin–Verdier finite coefficients, the complete rational table, and explicit wild local support. Full integral purity holds for n≥2 and in every twist after inverting the residue characteristic. Twist-zero open groups are computed exactly. Sign deletion changes Kummer comparison. No universal comparison among all open topoi or arbitrary-scheme product theory is claimed. | E.4a–p |
| E.5 | Algebraically closed uniqueness follows from Wibmer without cardinality restrictions, assuming existence. Pro-uniqueness fails even over a perfect field of cohomological dimension one, with every finite quotient trivial; the counterexample lifts to Witt vectors. Connected kernels or compact point sets give precise positive pro-limit results. Explicit elliptic fibres differ already up to isogeny. The unspecified integral motivic model and literal continuous H1 remain unresolved. | E.5a–g |
| E.6 | Exact Artin–Tate comparison class and its number-field tuple proved. The Tate component is trivial; a quadratic Artin component is explicitly nontrivial at 3 and trivial at 5. | E.6a–b |
| Lead D1 | Refuted as a D(Q) parity repair and as a criterion for existence of every real fibre. Correct odd-denominator restriction criterion proved. | D.1a,c,d |
| Lead E2 | Finite-field and rational trace patterns verified; literal integral equality with the supplied theory is false. The corrected integral family retains finite coefficients and the rational pattern by including wild support and non-finitely-generated torsion. The separate sign-deleted construction preserves its stated localization and proper duality but changes the mod-two Kummer comparison. | E.4a–p |
| Lead E3 | A precise sigma-conjugacy/lattice interpretation is proved, but it does not identify an undefined continuous H1. Variation can already change the Newton class; unstructured smooth torsors over Witt vectors remain trivial under the stated hypotheses. | E.5c–e |

## Files

The main paper fragments are part_D.tex and part_E456.tex; the additional
local-cycle contribution is C3_picard.tex, C3_ordinary_picard.tex and
C3_torsion_picard.tex, C3_surjectivity.tex and C3_general_picard.tex. The companion
references.bib marks every entry's opening status. results.csv has one row
per numbered paragraph; CHECK_EVENTS.tsv records the actual kind of check.
SOURCE_AUDIT.md lists opened primary sources, precise locations, unsuccessful
retrievals and the search scope. code/verify_examples.py and its output
contain the exact finite computations. code/build_metadata.py constructs
the machine-readable ledgers without making mathematical inferences.
code/verify_localization.py checks the actual finite-coefficient chain
matrices of E.4e–f. code/acquire_sources.py records reproducible source
downloads, with byte counts and hashes in its output.
code/verify_protorsor.py checks the exact partial sums and finite
truncations in the inverse-limit counterexample E.5f.

## Background inspected and the precise corrections

### R3

Read broad_layer/SA05/STUDY.md section 1 and the c15:2–14 conclusions.
The identification of the band with the Weil-number character group is
retained under its Tate-conjecture hypothesis. It is not silently promoted
to an unconditional classification of all numerical motives. The use of
endomorphism division algebras as evaluations of the gerbe is rechecked in
D.3b using a morphism from the actual Artin/Tate-rigidified fibre gerbe:
Weil restriction descends the object, Artin rigidification selects its
geometric summand, and coefficient extension selects the K-linear
splitting module. Brauer invariants of orders r for every r>=3 show that
the compact component is not controlled by the mu_2 component.

### R8 and the prior reading of 15:125

Read c14_c15rest.md part 3 section C, the exact transcriptions of
15:117,119,121,123,125, and the cited P3 checks. Independently rechecked
the character identity c(m)=w(m)e-m, compact real torus H1, the
odd-denominator criterion, and the q=25 example. D.2 supplies the missing
real orbit proof and a counterexample to rational transitivity.

The prior reading's suggestion that Grothendieck's reason on 15:125 is
wrong because the class should have order dividing two is withdrawn:
D.3b gives infinite order. The transcribed French may state the necessary
order-two consequence of a hypothetical lift. No change to the
transcription is needed or justified.

### R15

Read part 3 section F, the SA05 reading, transcriptions 15:173–178 and the
attached Lichtenbaum source. Finite-field l-adic claims are checked for
l different from p; the p-part is separately computed in E.4a. Negative
twists require an explicit convention, and Z/(1-q^n) is not literally an
integral quotient for negative n.

The exact integral number-ring table of 15:173 omits the sign group.
Standard compactified Weil-etale cohomology has H1(Z(1))=Z/2 and
H3(Z(0))=Z/2. The rational table is correct. The open restriction
invariance condition is n different from 1, not n different from 0.
Page 15:178 itself keeps Z/2 in H0(G_m); its terse l=2 margin does not
define a global deletion of that group. E.4i subsequently gives
independent proofs of the strict-local-factorial Brauer injection
and the local finite-etale Azumaya descent criterion, with the
opened Bourbaki1966 numbering distinguished from the manuscript.

### R16

Read part 3 section H and transcriptions 15:191,193,197,199. Rechecked
the H1 rather than H2 degree for comparison of existing fibre functors,
and the nontriviality already on Artin motives, with explicit local data.
The uniqueness problem is separated into an affine torsor statement,
existence of a fibre functor, characteristic-p integral models, and
additional F,V structures. The first norm-torus counterexample has no
cohomological-dimension-one hypothesis and does not contradict the
separate finite-stage Lang–Steinberg claim under that hypothesis.
Steinberg's original Theorem 1.9 was subsequently opened and checked;
E.5e proves the required passage from residue-field torsors to Witt
vectors by smooth lifting. Thus the finite-stage uniqueness part of
R16 is checked with its precise connectedness and dimension hypotheses.
The stronger E.5f counterexample now treats the pro-limit separately:
over k = Fbar_3(t)^perf, every stage is a trivial G_m-torsor, but the
transition constants force a prospective compatible valuation to equal
-1/7, outside Z[1/3]. The affine fpqc torsor itself, its fibre-functor
interpretation, cd(k)<=1, and its Witt-vector lift are all proved.
Milne 2003 Proposition 2.8 and Lemma 2.10 were opened as the exact
characteristic-zero literature analogue for this lim^1 obstruction;
the characteristic-three example is proved directly. E.5g proves the
correct pro-level conclusions under connected-kernel or compactness
hypotheses, including the Z_l case.

The tau identity on 15:203 and the Hodge-level counterexample on 15:205
are not needed in this contribution and were not independently rechecked.

## Exact computations and scope

All computations use Python standard-library integer arithmetic and
fractions. The output file records elapsed wall time; it is a fraction of
a second on this run. Inputs and scope:

1. q=25, pi=2+i, lambda=5*pi^2. Exact Gaussian divisions verify norm 625
   and valuations 3,1; normalized slopes are 3/2,1/2.
2. q=17, alpha=1+4i, beta=3+2*sqrt(-2). Norms are 17; four parity
   homomorphisms give the two rational orbits in D.2b.
3. p=2,3,5,7,11 and r=3,4,5,6,7, with alpha^2=alpha-p. Exact reduction
   of alpha^(r-1)*bar(alpha) verifies norm p^r and the invariant orders.
   This finite check is not a proof for every p,r; the general argument
   is in D.3b and uses Honda–Tate.
4. q=2,4,3,9,5,25 and n=-3,-2,-1,1,2,3. Cyclic orders q^abs(n)-1 are checked
   prime to the residue characteristic.
5. All 25 affine pairs over F5 are tested for y^2=x^3+a*x+1, a=0,1.
   Discriminants are nonzero; point counts including infinity are 6,9,
   giving traces 0,-3 and the two Newton polygons.
6. x^2+1 modulo 3 and 5 is enumerated. At 5 the roots are simple, so
   Hensel's lemma applies; at 3 the quadratic extension is nontrivial.
7. code/verify_localization.py enumerates kernels and images of the
   displayed differentials modulo m=1,...,8, for |S|=0,...,3, both with
   and without the sign summand. It also checks coordinate-inclusion
   chain maps modulo 2,3,4,5. Runtime is recorded in its output
   (approximately 0.0006 seconds). The integral proof, not the finite
   check, establishes the formulas for every m and S.
8. code/verify_protorsor.py checks the periodic partial sum against
   -1/7 modulo 2^N for N=1,...,60, verifies integral solutions of all
   tested finite truncations, and verifies the geometric-sum identity
   for 20 periods. The proof in E.5f, not this finite check, establishes
   nonexistence of an infinite compatible point.
9. code/verify_wild_purity.py checks the quadratic derivative and CRT
   inverses exactly, its positive discriminant8, and the cyclotomic
   generator order for m=3,...,14, with the valuation identity through
   exponent2^10. The full infinite tower argument is proved in E.4k.
10. code/verify_local_picard.py gives exact homogeneous Jacobian and
    basepoint-free certificates for the Fermat quartic on its three
    affine charts, and exact rational contraction/quotient matrices
    for N=4,...,20. The ranks and zero compositions pass. The general
    all-dimensional rank argument and passage to actual strict-local
    line bundles are proved separately in C.3i. Runtime and output
    are recorded in code/verify_local_picard.out.
11. code/verify_picard_deformation.py checks the C.3m Fermat-Jacobian
    quotient over the rationals, the determinant-one contraction
    matrix, and all 337 ordered-quadruple Segre equations and 27
    minors for m=2,3. Its .out file records all exact passes and
    runtime. The uniform geometric proof, the actual Poincare
    obstruction and the completion descent are proved in the text.

## Local Picard refinements and literature scope

C.3i and C.3j were independently audited by root and frobenius against
Kollar's published actual-group sequences. The finite normalization of
the section ring is used because the target cone has a degree-two
section defect; the proof does not identify its cone contraction with
the blow-up of its maximal ideal. The fixed-scheme algebraic-equivalence
definition is distinguished from the local Picard functor's varying
etale neighbourhood convention.

C.3j proves that every ordinary algebraic-equivalence relation comes
from an abelian-subvariety image, by descending the whole family at a
single finite stage and extending its divisor to a smooth projective
compactification of the product. Kollar's unipotent-kernel theorem
then gives injectivity in dimension at least four. C.3k reaches
dimension three through a separate torsion-cover argument, including
the finite normalization/Hartogs calculation of all global divisor
units and the exact connectedness theorem after normal completion.
The final closed kernel is defined by the morphism of local Picard
functors; it does not presume a universal line bundle on an abelian
image of another Picard variety.

The new literature search opened Kollar2016 Theorem1.7, Definition3.3,
Section3.5 and Example4.2; Bhatt--deJong2014 Theorem0.1 and Examples1.31,
1.33--1.34; Wlodarczyk2005 Theorem1.0.2; Varbaro2009 Theorem1.6 and
Corollary1.12; Boutot1978 Introduction Theorem1(i)--(ii); and the exact
Stacks normalization, henselian, completion and connectedness lemmas.
Boutot's full ChapterII proof remains behind the publisher's subscription
wall, while the exact theorem statement in the publisher's introduction
was obtained and screenshot-checked. These standard source theorems
are cited inputs; no independent proof of resolution or local Picard
representability is claimed. No priority is claimed for the refinements.

No scan images were supplied. Statements about handwriting are limited
to the given transcriptions and their recorded uncertainty.

## Remaining gates and attempted approaches

**D.4:** A formal transport proof under a supplied compatible global
polarization does not prove that such algebraic polarizations exist and
specialize compatibly for all geometric motives. The slope expression
also fails before that question on the explicit even-weight example.
Milne's quotient positivity criterion now identifies the precise test
on additional endomorphisms. His 2002 Theorem 2.1 and Remark 3.7 give
actual CM and Lefschetz reduction cases. The 2026 van Hoften–Sempliner
preprint Theorem I, explicitly retained as a cited input, removes the
Hodge hypothesis in the abelian case and, through Milne 1999 Theorem
7.1, proves the abelian-type finite-field effectivity assertion. The
author's cofinal-field erratum was opened and retained. The general
specialization/positivity gate and effectivity outside the abelian-type
category have not been eliminated. D.4f identifies the latter exactly
with the full Tate cycle conjecture in the stated numerical-motive
framework: already every Frobenius-identity motive being effective
would force all Tate classes to be algebraic. D.4g extends the actual
polarization-preservation case from CM families to arbitrary relatively
polarized abelian families with exact faithful Tate-preserving
specialization functors, by the common generator-and-summand forms.
Its distribution conclusion retains the real-fibre identification and
slope-parity existence required by D.4a.

**E.4:** The literal identification with the attached integral theory is
refuted, not left as an open comparison: the proper sign terms in E.4b
and the Kummer contradiction in E.4d settle it. The corrected bounded
family is now constructed on every real-place-retaining finite-prime
open in every twist. E.4o proves that the twist-one localization cone
has the specified Artin–Verdier finite-coefficient comparison. E.4p
assembles all twists by keeping the proper rational correction and
using actual étale restrictions, with the separate explicit correction
in twist one. The complete rational manuscript table is preserved.

E.4l computes every twist-zero open group and identifies the actual
local support with the continuous dual of Z_p^× in degree three.
At the open over Z[1/2], degree two is Q_2/Z_2. E.4m identifies
RΓ(Q_p,Q_p/Z_p(n))[-2] as the extra negative-twist support. E.4n
proves full integral purity for n≥2 by Geisser2004 Proposition5.1
with its exact local cohomological-dimension bound; the historical
Bloch–Kato assumption is supplied by the opened Voevodsky2011 theorem.
All twists have purity after inverting the residue characteristic.
This explains the two refutations E.4j–k: naïve integral purity and
finite generation on opens cannot accompany all the desired finite
comparisons and rational values. The counterexamples and the corrected
complexes are compatible, not competing conjectures.

The remaining scope is explicit: these results do not identify every
open Weil–étale topos, every compact-support convention, or an
unspecified multiplicative theory on arbitrary arithmetic schemes.
Those are additional comparisons, not prerequisites left unfinished
for the stated family. The sign-deleted complexes E.4f still necessarily
lose the ordinary mod-two Kummer comparison. The named Morin, Chiu,
Beshenov, Geisser and Spitzweck sources were inspected in their actual
coefficient categories; no theorem from one category is silently
renamed as a theorem in another.

## Current-literature audit added after checkpoint 01

The full 25-page author PDF of van Hoften–Sempliner, The Hodge Conjecture
for CM abelian varieties, was opened and downloaded on 19 November 2026.
The Hexagon registry labels it 2610.00259v2, with v1 on 15 October and
the v2 submission on 18 October. Its Theorem I has no hypothesis beyond
being a complex CM abelian variety and concerns rational cycles. We
checked the elementary surface-to-cycle reduction (Theorem 2.3.4) and
read the proof chain through Theorems 2.2.1 and 4.0.2 and Lemmas
4.2.7–4.2.10. The auxiliary field is enlarged to have nontrivial totally
real part, as required for compact Picard modular surfaces. The analytic
imports from the theta-correspondence literature have not been independently
reproved here. Accordingly D.4d–e explicitly state dependence on this
primary preprint theorem; neither an announcement alone nor a statement
about all varieties is substituted for it. The parent's independent
audit of D.3b's actual relative-gerbe construction is recorded separately
in CHECK_EVENTS.tsv.

**E.5:** Wibmer settles uniqueness after existence over an algebraically
closed field. It does not manufacture the manuscript's unspecified
integral model of rational motives in characteristic p. The norm torus
and the stronger pro-torus construction settle universal perfect-field
claims, including the cohomological-dimension-one pro-limit refinement,
not the undeclared motivic subcase. The structured crystal moduli are
explicit, but the phrase
continuous H1 has no defined object to which an equivalence can be proved.

## Ordinary local surjectivity: actual-family counterexample

C.3m uses the Fermat quartic C and V=P^m times C, with m=N-2.
Inside the total space of O(-1,-1) over P^m times P^2, the equation
F+t*ell*H defines a smooth neighborhood of V. The proper Segre
contraction gives an explicitly presented affine image W. The ring
R is the strict henselization of the normalization of this original
affine W at its unique vertex. The auxiliary neighborhood used in
the proof does not enter the definition of R. The principal function
f=w00+w11+w22 has regular punctured divisor Y.

The first-neighborhood class has three independent curve components.
Contraction with holomorphic one-forms is injective. Illusie's actual
line-bundle obstruction formula, checked against his theorem and
errata, then forces an abelian family that extends to that first
neighborhood to have zero classifying map to Pic^0(C). The square-zero
unit sequence makes all its individual first-neighborhood fibres
equal. Higher coherent cohomology vanishes, giving compatible formal
trivializations. Proper formal full faithfulness and finite reflexive
module descent over the faithfully flat completion prove that every
ordinarily algebraically trivial line bundle on X is actually trivial.

On Y, the projection from the strict transform to C pulls back the
actual Poincare family. A boundary-divisor and fibre-degree argument
proves this gives an injection of Pic^0(C). A point with one coordinate
transcendental over the algebraic numbers gives an explicit infinite-order
line bundle, so the counterexample survives rational coefficients.
This settles ordinary J1 nonsurjectivity itself. The earlier full-Picard
counterexample C.3i alone did not do so. Root and frobenius independently
audited all actual-family and formal-to-local passages before integration.

## General coefficient-field injectivity

C.3n removes the algebraizability restriction from the positive ordinary
injectivity assertion and also treats characteristic p after rationalization.
An ordinary curve family extends by Cartier closure directly along the
proper parameter curve. Normalizing its degree and one parameter fibre
classifies it by a map from the puncture to that curve's Jacobian. The
dual-Jacobian Poincare family then gives an actual abelian-parameter
family on the puncture, with no compactification or resolution of the
source. Boutot's original arbitrary-noetherian hypotheses give the source
local Picard scheme and the target functor's closed unit section. Their
closed kernel in the proper abelian image has no prime-to-characteristic
torsion and is therefore finite with p-primary point group. Both root
and frobenius independently checked the complete proof and the actual
primary page before integration. The coefficient/residue field is part
of the theorem's data, not an implicit mixed-characteristic convention.

## Typesetting status

The initial local compile failed because lualatex.fmt was absent; that
attempt is preserved in code/build_fragments.py and build/build_commands.out.
The parent subsequently repaired the shared TeX installation and reported
successful master builds and statement-register checks. The parent remains
responsible for integrating these fragments and the final visual inspection.
No separate uninspected final PDF is supplied by this agent.

## Exact degree-one boundary dimensions over C

C.3o completes the small-dimensional ordinary rational J1 cases.
For N1 both groups vanish. For N2 the target vanishes, so surjectivity
is automatic, but the strict henselization of the Fermat quartic cone
contains its Jacobian in ordinary Pic_alg and restriction to z2=0
kills it. For N3 the same cone is a divisor in a regular strict-local
threefold, whose puncture has Pic=0; surjectivity therefore fails.
Together with C.3m--n, injectivity always holds for N>=3 overC,
whereas surjectivity fails in every dimension N>=3. The failures
use an infinite-order actual line bundle and survive Q coefficients.
Over Fpbar, by contrast, the actual abelian-family construction makes
ordinary Pic_alg torsion. These characteristic distinctions are retained.

The same Fpbar torsion conclusion now holds for ordinary algebraically
trivial Chow classes in every codimension under the precise curve-family
convention in C.3o. A horizontal cycle closes over a smooth projective
parameter curve and remains flat there. A principal multiple of the
marked degree-zero divisor pulls back to a principal cycle relation,
and proper pushforward kills the corresponding finite multiple of the
fibre difference. Taking the excellent regular puncture itself as the
universally catenary base makes all these maps finite type in the needed
Chow formalism. No finite-type-over-k assumption on the puncture is hidden.

## Local torsion, completion, and the exact positive-characteristic gate

C.3p is finalized after full independent root and frobenius audits.
Restriction of finite etale covers is fully faithful in dimension at
least three and an equivalence in dimension at least four, for the
specified excellent normal strictly local ring with regular puncture.
For a regular divisor puncture, the invertible-order Picard torsion
groups are consequently isomorphic in dimension at least four. This
includes mixed characteristic. A separate argument proves invariance of
the coefficient-field local Picard functor under completion, by comparing
the identical completions of the two henselized tensor pairs and applying
Elkik's exact Picard corollary. It does not remove the henselization from
an arbitrary family over a parameter scheme.

C.3q, also independently audited by both agents, treats the normal
essentially-finite-type characteristic-p scope. Every proper abelian
subgroup of the target local Picard functor lifts to a proper source
abelian subgroup up to two isogenies whose composite is a power of p.
Prime-to-p torsion density, finite generation of the normal local
Neron–Severi group, and Kollár's unipotent restriction kernel give the
proof. It is a theorem about the specified local functors. The additional
point-realization argument on the fixed puncture times curves is supplied
separately by C.3w; no universal actual family on the whole subgroup is
inferred from the functor theorem itself.

## A complete all-characteristic smooth-cone case

C.3u closes that ordinary-family issue for a smooth projective cone
source in dimension at least four, assuming its full section ring is
generated in degree one. The divisor element is arbitrary, including
nonhomogeneous elements, and its puncture is assumed regular. Pullback
identifies the actual ordinary algebraically trivial Picard group of
the source with the point group of Pic0_red of its smooth projective
exceptional variety. Restriction to the divisor puncture is integrally
surjective in every characteristic, with zero kernel in characteristic
zero and finite p-primary kernel in characteristic p. Ordinary rational
J1 restriction is therefore an isomorphism in this scope.

The proof detects every ell-power torsion line bundle, for one prime ell
outside the torsion of NS(V)/Z[L], by extending it to the regular cone
resolution and twisting by the single exceptional divisor. Proper
henselian finite-etale comparison then identifies it with a pullback
from Pic0(V). Dense torsion in each ordinary abelian image, combined
with C.3p, proves target surjectivity. The source Poincare family is
already an actual product family. No splitting of the full local
Picard functor or general family-algebraization theorem is invoked.
The result is consistent with the C.3m counterexamples because their
sources are deformations of cones. C.3w subsequently closes the ordinary
point-realization step for the general algebraizable scope of C.3q.
The cone theorem remains an independent all-characteristic result.

## General algebraizable positive-characteristic degree-one surjectivity

C.3w is proved after a full independent root proof/source audit. Let R
be the strict henselization of a normal local scheme essentially of
finite type over an algebraically closed coefficient/residue field k,
with dimension at least three and regular puncture X. Every k-point
of a proper abelian subgroup of the local Picard scheme is an actual
ordinary algebraically trivial line-bundle class on X. This is a
point-realization theorem; it does not claim a universal line bundle
on the fixed product X times the whole abelian subgroup.

The construction fixes a regular alteration and works over a proper
parameter curve. Cartier extension on smooth henselized parameter
charts has only a constant exceptional-divisor lattice ambiguity,
whose first etale cohomology on the curve vanishes. Rigidifying at a
closed-fibre point leaves a formal-unit gerbe. A recursive Amitsur
calculation on each fixed affine cover proves the needed ordinary
etale cohomology vanishings for its band, so the family exists formally.
Proper formal existence and Artin approximation then supply an actual
family on the alteration. The approximation preserves its fibre
differences because the Picard kernel of a nilpotent proper immersion
is quasi-affine, and a proper connected curve maps constantly into it.
Compatible trivializations follow from finite-dimensional
Mittag–Leffler images of the global-function rings. Finally the norm
on the actual finite-flat locus extends uniquely across codimension
two in the regular target. Divisibility of the abelian point group
removes the alteration degree.

Combining this with C.3q proves **integral ordinary Picard restriction
surjectivity in characteristic p for every dimension N>=4** in this
algebraizable scope, for any nonzero local divisor element whose
puncture Y is regular. C.3n gives the p-primary torsion kernel, so the
ordinary rational J1 map is an isomorphism. The proof assumes neither
resolution of singularities in positive characteristic nor a general
henselian GAGA essential-surjectivity theorem. The remaining broader
local questions are outside these stated scopes: in particular the
arbitrary nonalgebraizable excellent-ring extension and higher
codimension. Characteristic-zero unrestricted ordinary surjectivity
is already refuted by C.3m, while the all-characteristic smooth-cone
case is settled by C.3u.

## Superseded local drafts

`C3_smooth_cone_draft.tex` and `C3_alteration_family_draft.tex` are now
comment-only pointers to the canonical final fragments, preserving their
filenames without presenting competing proved versions. The separate
smooth-cone draft source/bibliography notes are likewise pointers to
`SOURCE_AUDIT.md` and `references.bib`. In C.3w the initial stronger
affine-unipotent Picard-kernel argument was replaced by the exact
quasi-affine pullback theorem of Cheng–Ji–Larson–Olander, Proposition1.4;
quasi-affineness is precisely sufficient for the proper-curve rigidity
step. This substitution was independently checked by root. No numbered
proved assertion was dropped.


## Positive-characteristic ordinary degree-one boundary closure

C.3x, in `C3_positive_characteristic_boundary.tex`, supplies the full
dimension table for algebraizable normal strict local germs over an
algebraically closed coefficient/residue field of characteristic p.
Over Fpbar both rational ordinary J1 groups vanish. Over every larger
algebraically closed field, the universal injectivity/surjectivity
answers are: N1 yes/yes (zero groups); N2 no/yes; N3 yes/no; N>=4 yes/yes.
The last row uses C.3w and therefore retains its algebraizability scope.
The characteristic-zero table remains different.

The boundary failures are explicit in every positive characteristic,
including 2 and 3. Smooth plane elliptic cubics are chosen over Fp; a
point with transcendental x-coordinate gives a non-torsion Pic0 class
because every finite torsion subgroup is defined over Fpbar. The cone
resolution proves actual Pic0 injection after strict henselization.
A transverse linear section has three field punctures in dimension two;
the same cubic divisor in a regular local threefold yields dimension-three
non-surjectivity. Exact polynomial certificates and finite independent
samples are saved, and no finite check is used as a non-torsion proof.


## Multiplicative local divisor quotient in every characteristic

C.3y gives a fully specified strict local surface, regular off its closed
point, with ordinary Pic_alg=0 and Pic=k* direct sum (Z/4)^2. The explicit
projective blowup contraction uses twelve transverse triangle-quartic
points, including a separate coefficient in characteristic229.
The formal Picard group stabilizes at the exceptional triangle, and
proper GAGA plus Elkik gives actual line bundles on the strict henselization.
Actual curve families extend to a proper parameter and have constant
triangle gluing, so none of the multiplicative subgroup becomes ordinary
algebraically trivial. This refutes integral local B1 finiteness in every
characteristic and rational finiteness over positive-transcendence-degree
positive-characteristic fields. The Fpbar rational quotient is zero.
Root and cycles have completed independent full audits.

## Non-top higher local quotients and the excellent-ring extension

C.3aa, in `C3_segre_nori_quotient.tex`, proves that for every
`N>=4` and `2<=r<=N-2` there is a fully specified complex strict local
normal isolated cone germ with `B^r(X)_Q != 0`. The starting cycle is the
exact Nori–Nagel witness already proved in C.1i, with ambient parameter
`c=r`, section dimension `n=r+1`, and section degree `4r+2`. For
`V=P^m x T`, `m=N-r-2`, the ordinary cycle quotient is exactly
`B^r(T)_Q / H^(m+1) B^(r-m-1)(T)_Q`; its denominator is contained in
`H B^(r-1)(T)_Q`, so the chosen primitive cycle survives. C.3e then gives
an actual class on the strict henselian puncture. Nonzero rationalization
refutes the original assertion of finite integral groups. No infinite
rational dimension is asserted, and the top range `r=N-1`, `N>=3`, is
not settled by this construction. Root and cycles independently read
and passed the complete typed proof. The exact sign/index certificate
and its runtime are retained with the text.

Root C.3z, in `research/sections/C3_completion_algebraization.tex`, has
also passed this agent's complete independent audit, including its
revised final step. It removes the algebraizability restriction from
C.3w and the characteristic-p table C.3x for excellent henselian normal
local rings with an algebraically closed coefficient/residue field and
regular puncture. The earlier scope limitations in this chronological
report are superseded to precisely that extent. The proof constructs an
actual regular map from an algebraic model with the same completion,
pulls back a regular alteration, and verifies every subsequent family
argument. Its local Neron–Severi transfer uses an isomorphism of the full
henselian-tensor Picard functors, including identity components. Its
kernel argument kills the whole finite-type group scheme by a p-power,
including infinitesimal multiplicative factors. No mixed-characteristic
or higher-codimension extension is inferred. The separate review is
`C3_completion_algebraization_independent_REVIEW.md`.
## C.3ab: an integral positive theorem inside the remaining top range

The final file `C3_surface_cone_top.tex` is proved and independently
audited by root and frobenius, including the exact primary statements.
For a strict henselian cone over a smooth projective surface in
characteristic zero, the hypothesis
`H2(V,Omega1_{V/Q} tensor L^j)=0` for every positive j gives

`CH2(X)=CH0(V)/(L.CH1(V))` and `B2(X)=Z/g`,

where g is the positive gcd of the L-degrees of integral curves.
The hypothesis holds for every such surface over Qbar and, over C,
for all K3 and geometric-genus-zero surfaces. In particular P2 with
O(d) gives Z/d, and the Fermat quartic example of C.3f has B2=0 because
it contains a line. Its non-torsion CH2 class is ordinarily algebraically
trivial, so there is no conflict with that earlier counterexample.

The proof uses finite-level detection deduced from Morrow's pro cdh
theorem, an integral relative-K2 calculation justified by unique
divisibility, a direct henselian-DVR zero-cycle argument, and the exact
codimension-two Riemann–Roch multiplier minus1. Source and certificate
records distinguish every input. The former draft is superseded by a
comment-only pointer. Arbitrary complex surface cones, arbitrary
three-dimensional germs and all unrestricted higher top cases remain
open here; this subset result is not counted as full main-gate closure.


## C.3ad: rational top quotients of all smooth cones over Qbar

The final proof is `C3_rational_top_cones.tex`. For every smooth projective
V/Qbar of dimension d>=2 with the stated normal degree-one section ring,
it proves `CH^d(X)_Q = CH0(V)_Q / L.CH^(d-1)(V)_Q` and hence
`B^d(X)_Q=0` for the actual strict henselian puncture and ordinary
fixed-product algebraic equivalence. Loday's arbitrary-commutative-algebra
Hodge decomposition and the exact relative Adams shift avoid applying
smooth HKR to a nilpotent thickening. The only possible descent diagonal
is killed by Nakano vanishing because absolute and relative differentials
agree over Qbar. Root and frobenius completed full proof and exact primary
source audits. The symbolic certificate runtime is92.695311seconds; the
full Loday PDF and retrieval/hash manifest are retained. The old draft is
a comment-only supersession pointer. This is a restricted rational theorem:
no integral finiteness in dimension d>2 and no unrestricted local top-degree
closure is claimed or counted as main-gate movement.

The further research note `TOP_QUOTIENT_RESEARCH.md` is part of this
deliverable. It contains the audited explicit proper-curve K2-symbol lemma,
the elliptic absolute-form construction, and the precise remaining
finite-thickening-to-actual-product-family gate. It also records source
limitations and rejected inferences, including the BEK inverse-limit
K0 algebraization counterexample. These observations do not settle that
remaining gate.

The research note Section7 now proves a separate integral completion
descent lemma for K0 modulo actual proper-curve family differences.
Popescu approximation and a smooth-stage henselian retraction descend
an already existing completed family. Frobenius independently checked
the full qcqs scope and freshly opened every primary Stacks input.
This does not algebraize formal classes or identify arbitrary Chow
quotients with K0; those limits remain explicit. The earlier C3i exact
certificate was rerun once to add its required runtime0.020695seconds.

## C.3aj: all higher-codimension high-dimensional ordinary restriction maps

The final complete proof is `C3_high_range_surjectivity.tex`, with the
independently audited auxiliary input `../frobenius/C3_product_Hodge_inputs.tex`.
For every r>=2 and N>=2r+2, it specifies an excellent normal strictly
henselian complex local ring and regular punctured principal divisor
whose ordinary CH^r restriction cokernel surjects onto the nonzero uniquely
divisible group Pic0(C)(C)/Pic0(C)(Kbar). This is a genuine universal-range
counterexample and settles this high-dimensional surjectivity range.

The full proof has independent passes from root, Frobenius and cycles.
It separates the jointly Hodge-generic quartic surfaces from the algebraically
independent section coefficients. The boundary is controlled by weak
Lefschetz and a tensor-degree calculation; its values descend through
actual Hilbert families on the projective exceptional section. The ensuing
countable-field quotient avoids an unsupported exact-boundary cancellation.
The degree-r Chern obstruction kills every actual source-family difference,
whereas the target product of specified divisors evaluates to (-9)^(r-1).

The exact finite certificate and its stdout/JSON are in
`code/check_high_range_incidence.py`, `code/check_high_range_incidence.out`,
and `code/check_high_range_incidence_output.json`; runtime0.057480419seconds.
The full Grothendieck Hilbert exposé and its erratum were downloaded with
SHA256 and actual timings in `code/acquire_hilbert_sources.out`.
The former draft is a comment-only supersession pointer.

Additional independent reviews of the parent's dimension-six C.3ag and
cycles' regular-ambient C.3ah are retained as
`C3ag_incidence_invariant_independent_REVIEW.md` and
`C3ah_regular_ambient_independent_REVIEW.md`, with their separate event
ledgers. Both full typed proofs passed, including exact primary-source
inspection; they are not duplicate statement rows owned here.
