# D.1–D.4 and E.4–E.6: outcome and proof audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026.
Run: /root/real_weil. No priority is claimed. This report is a contribution
to the parent manuscript, not a replacement for the unresolved gates.

## Outcome table

| Item | Outcome | Statement IDs |
|---|---|---|
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

The paper fragments are part_D.tex and part_E456.tex. The companion
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

## Typesetting status

The local fragment compile reached an environment failure before TeX
input was processed: lualatex.fmt was absent. The exact attempt is
recorded in code/build_fragments.py and build/build_commands.out.
The parent is repairing the shared TeX installation and is responsible
for the final master build and visual inspection. No uninspected final
PDF is supplied by this agent.
