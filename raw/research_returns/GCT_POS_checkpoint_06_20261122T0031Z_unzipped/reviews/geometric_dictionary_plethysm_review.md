# Independent dictionary review: plethysm, lambda/Schur operations, archive scope

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

## Outcome

**PASS for the mathematical translation**, with the wording and attribution
clarifications below sent to the author. Read all of
`branches/root/grothendieck_dictionary.tex`; the required detailed review
covers its general schemes/representation/lambda-Schur section, every
plethysm and positive-formula paragraph, and the archive-correction table.
The new branch proofs were already fully constructed and separately reviewed;
the Cox and determinant-twist dictionaries were reread directly here.

Read the entire supplied archive `SOURCE_NOTES.md`, the complete A-012
integral tensor-power proof, A-013 finite-set-functor proof, A-023 local-ring
counterexample, and the complete PLE-F7 pure-Tate/IC proof. The remaining
historical source numbering is explicitly inherited verified background,
not a claim of a fresh reading of every original source or manuscript scan.

## Mathematical checks

The vector-bundle convention uses `Spec Sym E^vee`; group actions are
coactions, diagonalizable actions are character gradings, and exact K0 is
distinguished from the split Grothendieck group. Integral Cauchy identities
are transferred using the actual free integral filtration, with the
conjugation of ABW's exterior-row convention. The symmetric/exterior Koszul
identity and Schur polynomial operations do not imply effective
representatives for arbitrary virtual classes.

The cubic quotient and Veronese constructions preserve the stated graded
multiplicity algebra; their constituent-index inequalities remain numerical
consequences of the proved waves. The determinant-twist argument preserves
the entire graded algebra, hence intrinsic grading inertia, without asserting
a uniform statement about every raw GL presentation. Fixed-embedding density
has its exact encoding and nonzero-initial-coefficient condition; no
varying-embedding uniformity is inferred.

G-040's cokernel is an actual finite graded module. Its generator lower bound
is the dimension of the fibre modulo the homogeneous maximal ideal, hence
an obstruction to a small literal free presentation. It does not obstruct a
compressed counting rule. The Cox identification retains all divisor degrees
and the actual signed permutation action. Its scalar sections give two-row
balanced Schur spaces, while general flag tails remain a separate problem.
The PNEW-012 bounds of 45 polytopes and 11 variables are within precisely
that scalar scope. Characteristic-zero Hadamard–Howe kernel statements do
not silently become integral splitting or good-reduction theorems.

The finite-set and exact-K0 meanings in the archive table are properly
distinguished. A-012 uses an integral filtration and three exact torus-weight
extractions, not injectivity of rational characters. A-023's character
`1+epsilon` is distinct from both signs in the explicit characteristic-zero
local ring and gives a valid determinant obstruction to generation.
PLE-F7 concerns the same obstructing Kleinian cone over the stated finite
fields; its cohomological purity does not identify Hilbert grading with
cohomological degree.

## Requested precision edits

1. For PNEW-008, determinant twisting **can change** a raw GL central kernel;
   do not assert that every presentation's kernel changes.
2. Credit Pak–Panova–Swanson's marked-tree positive interpretation, using the
   classical KOH identity of O'Hara/Zeilberger and GOS identity of
   Goodman–O'Hara–Stanton, based on Kirillov–Reshetikhin. Those identities
   themselves should not be attributed to PPS.
3. State A-013's false assertion with **one single** map-power `Hom(I,-)`.
   Finite coproducts of representables are summands of finite coproducts of
   map powers; the two-copy constant functor only refutes the single-power
   assertion.
4. A-023 refutes the unrestricted **generation** assertion, as detected by a
   determinant character. The determinant construction itself is valid.
5. In the composite SGA3 I locator, section 4.5 has original marginal page29;
   pages34–36 apply to Propositions4.7.2–4.7.3.

These are attribution/precision corrections, not defects in the underlying
proofs. The root owns the dictionary and is applying them there.

## Addendum: K-022, K-023, R-NEW-004, K-024 and PNEW-013

Read all five complete new dictionary paragraphs. PASS. The trace is an
identity of characteristic-zero characters; its integral coefficient
congruence is not an assertion that invariant formation commutes with
reduction modulo three. The hook Lie computation is in characteristic
zero, and the coefficient determinant three is explicitly disclosed.
The Euler term is evaluated in the dyadic cyclotomic field, where every
nonzero moving difference is invertible after inverting two. Its unit
property at primes over three is arithmetic, requiring no smooth special
fibre. The absence of higher colliding auxiliary poles is justified by
the complete inertia calculation and the finite-length Koszul argument.

Two terminology refinements were requested and the root reports applying
them: rectangular Schur coefficient extraction gives the graded character,
not an algebra isomorphism; the remaining r=0 gate concerns the exact
primitive-M pole of the tensor Hilbert series, not an exact inertia order
equal to the exponent r. No new proof gap was found.

## Addendum: integral coherent support and the positive trace model

Read the complete new K026–K028 and PNEW014 dictionary paragraphs. PASS.
The closed-orbit inertia interpretation, finite character coset, integral
coherent module class with support, equivariant extension and dimension
induction transport exactly the reviewed proofs. The scalar Euler product
is inverted only after Hilbert evaluation, and the text correctly declines
to endow singular coherent G0 with vector-bundle lambda operations.
The formal trace countermodel is confined to effective rational C3 objects
in each degree, without multiplication, affine quotient, or motive.
No correction was needed. The later all-finite-stabilizer proposal is not
part of this checked dictionary addition.

## K030–K031 all-stabilizer addition, 2026-11-21

PASS. Read the entire new paragraph and its source/scope continuation.
The inertia-character wording matches the finite subgroup F intersected
with H in K031; triviality on H° is exactly what preserves the character
image. The generic type uses Luna on a smooth affine full-group chart.
The source locators BS64 Lemma5.11 p152 and Luna III.2 Corollaries3–4
p100 agree with the primary passages read. No characteristic-three
geometric base change is asserted. The remaining class is confined to
collision closures (and the origin), with no claimed value or cancellation
resolution. No correction required.

## Tensor exterior source-scope paragraph, 2026-11-22

PASS. Read all of branches/root/tensor_exterior_scope.tex. The exterior
realization, ambient bound, complement identity, square-boundary1 and
vanishing beyond the square exactly match the primary BOR2015 section4
passage and the independent alternating-projector derivation in the branch
note. Empty rectangles and positive s are correctly handled. The stated
PNEW014 n16,s4 value matches the exact certificate. The paragraph correctly
limits the consequence to attained coefficients and does not infer strict
constituent inequalities. The local sufficiency misstatement in Remark9
is not used. No correction required.
