# Locally finite coefficient rings: exact extension and arithmetic boundary

Agent dieudonne; run RESEARCH_SA17_FINISH-20261119;
GPT-6 Astra (OpenAI, ChatGPT Pro mode).
Full draft: sections/C_finish_locally_finite.tex.
No novelty or priority claim is made.

## Four numbered results

C:splitWG-filtered-colimits proves arbitrary filtered-ring continuity
for the split equivariant group and every exterior operation. The proof
uses finite projective idempotents, coaction coefficients, Gram matrices
and their inverses, together with finite identities in the coordinate
Hopf algebra and its tensor square. It does not impose exact-GW
metabolic relations, flatness of transitions, or a free bounded
coefficient coalgebra. Stable isometries give the explicit equality
criterion at a common later finite stage.

For locally finite R, finite unital subrings exhaust R and have2unit.
The transition maps are computed by extending finite coaction and form
matrices and applying the already-proved finite-base classification.
The direct limit is exact, but not called a uniform equality algorithm.

C:finite-ring-powers gives a quotient-free answer for A^I with A any
finite commutative ring with2unit, including nonfields:
finite-image functions I to WG_sp(BO_m/A), with pointwise operations.
Finite-partition subrings A^s exhaust A^I. The canonical indices are
the finite list of distinct nonzero canonical values and their exact
level sets. Computation requires a specified Boolean-set access model
for those subsets; arbitrary subsets are not presumed computable.

C:finite-ring-powers-scalar specializes to F3^I and O0:
bounded integer functions a and arbitrary F2 functions b, with
(a,b)(c,d)=(ac,ad+bc modulo2), and
lambda^r(a,b)=(binom(a,r), b binom(a-1,r-1) modulo2).
This follows from GW(F3)=Z[t]/(2t,t^2), t=<2>-1.

C:locally-finite-equality-obstruction proves no uniform ordinary
equality algorithm across computably presented locally finite fields.
Uniformly from a machine e, build finite-field towers with degrees
3^(s+1), switched to2*3^(s+1) once a halt is detected. Degree divisibility
gives computable inclusions. Exact arithmetic/equality of the union are
uniformly computable, including an injective natural-number presentation.
The class <2>-<1> vanishes exactly if e halts, since2 is a square in
F_(3^d) exactly for even d. Stable determinant comparison proves the
nonzero direction. Trivial action and forgetting give the same
obstruction for every fixed O_m.
This is a uniform impossibility across presentations, not a claim that
each fixed field has an undecidable equality problem. Root or splitting
access can supply extra information beyond arithmetic and equality.

## Source searches and openings

Searches before writing included:

- Grothendieck-Witt filtered colimits rings
- computable algebraic fields finite splitting undecidable
- Boolean powers rings Grothendieck Witt
- Tom Bachmann Some remarks on units in Grothendieck Witt rings
- Turing1936 computable numbers diagonal process undecidable

Opened Tom Bachmann, Some Remarks on Units in Grothendieck-Witt Rings,
arXiv1612.04728, AppendixB, Lemma49 on printedp26, Corollary51 on
printedp27 (physicalPDFpages26--27). Lemma49 concerns ordinary GW
and Noetherian essentially finite-type limits. Its proof descends
bundles and then the metabolic relations. The present statement
is proved separately for split equivariant groups and arbitrary
filtered rings; the source is cited only for the familiar underlying
continuity principle. Journal of Algebra499(2018),229--271,
DOI10.1016/j.jalgebra.2017.12.004.

Primary URL: https://arxiv.org/pdf/1612.04728 .
Opened the original Turing1936 primary scan:
https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf .
Also opened the Stanford-hosted transcription as a reading aid.
The exact locator is Section8, printedp248, impossibility
of deciding whether a machine ever prints a given symbol, equivalent
to the halt-event problem by a direct simulation.

## Scope and audits

All four complete written proofs passed separate independent audits by
root and descent_groups. Root owns compiled inclusion. The four result
rows and own used/rechecked events are saved in results_C_locally_finite.csv
and checks_C_locally_finite.tsv; descent_groups has its separate audit
file. Root events remain only in root records. No execution certificate
is claimed: the general continuity and impossibility proofs are
mathematical, and the scalar formula follows symbolically.
