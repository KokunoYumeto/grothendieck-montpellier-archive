# Independent full audit of C.3az

Reviewer: /root/real_weil, GPT-6 Astra (OpenAI), ChatGPT Pro mode;
effort setting not exposed. Completed 2026-11-19T11:38:43.203963+00:00.
Reviewed entire agents/frobenius/C3_smooth_exceptional_top_draft.tex.
Outcome: PASS in exactly its stated algebraizable, characteristic-p,
single smooth exceptional Cartier divisor with ample conormal scope.
No mathematical correction is required. No computational program was
independently rerun as part of this review.

## Proof reconstruction

1. KST applies to the noetherian abstract blow-up square without any
resolution assumption. Both local K0 groups are Z, and quotient by
the graph of the structure sheaf leaves the claimed constant-pro
monomorphism. Its actual kernels are decreasing subgroups with
inclusion transitions, so pro-zero really implies a zero kernel at
one finite thickening. GH applies in every nonconnective degree;
finite affine Mayer-Vietoris descent globalizes the nilpotent
comparison after inverting p. No uniform exponent is needed.

2. The rational Chern-character argument has an appropriate finite
smooth model. Projectivity makes the image of the nonsmooth locus
closed; the selected closed fibre is regular, and over the perfect
coefficient field the finite-stage regularity/smoothness condition
spreads. Finite vector bundles, cycles and their relations descend.
Contravariant Chern character matches refined pullback without an
extra Todd factor. Injectivity of the full K0 map therefore gives
injectivity in each graded Chow degree. Actual curve families are
preserved by the refined Cartier pullback.

3. The surface W through the prescribed x,o is cut by sufficiently
positive relative sections. Serre vanishing lifts their restrictions
from E. Prescribed-point Bertini produces a smooth connected curve C;
the argument uses the geometric construction in Stacks45.8.3, not
its later prime-to-characteristic divisibility conclusion. Transverse
jets on E give a regular surface and regular sequence near C. Any
bad locus or extra component would have a nonempty proper closed
image in Spec R, hence meet the closed point, a contradiction.
The resulting W is integral because each component meets connected
C and distinct components of a regular scheme are disjoint.

4. At the nth Cartier thickening the ideal is exactly L_C^n.
On C times the entire proper parameter curve P, the obstruction is
H1(C,L_C^n) tensor H1(P,O_P). For the finitely many nonzero groups,
the pth tensor power kills the obstruction. All earlier restrictions
are raised simultaneously; a fixed finite exponent then suffices
for every later stage by Serre vanishing. This is a compatible
whole-family construction, not a pointwise lifting argument.

5. Cartier and base-adic ideals have cofinal powers. Projective GAGA
over Rhat algebraizes the whole family and its inverse; full
faithfulness verifies invertibility. Regular completion plus Popescu
allows descent of this actual line bundle to one smooth R-algebra.
The henselian lifting lemma supplies an R-point with the same residue
point. Because C lies over Spec k, the pulled-back line bundle on
W times P has exactly the prescribed p-power restriction on C times P.
No claim of essential surjectivity for arbitrary henselian GAGA is
being made or needed.

6. Applying that construction to O(Delta-{o}times C) gives actual
ordinary cycle differences on W, then on Z. The square with E is
transverse, so refined base change gives p^e([x]-[o]) with coefficient
one. Rational coefficients lift every degree-zero zero-cycle. A curve
in E has nonzero ample-conormal degree; its boundary supplies the
remaining degree. Injectivity, localization and self-intersection
prove all stated isomorphisms. The boundary kills the one-dimensional
ordinary quotient on Z, giving the ordinary quotient zero on X.
The proof also works at d=1 with W=Z and C=E.

## Fresh primary inspections in this audit

- Kerz--Strunk--Tamme, arXiv1611.08466v4, PDF header16August2017,
  manuscript date17August2017, complete48page PDF opened at
  https://arxiv.org/pdf/1611.08466 . Read TheoremA and its exact
  equivalent long sequence(1.6), authorpp2-3. The version-specific
  /pdf/1611.08466v4 endpoint initially failed; the unversioned endpoint
  successfully returned the explicit v4 file. No hypothetical later
  version is substituted.
- Geisser--Hesselholt2011, complete published21page PDF opened at
  https://math.mit.edu/~larsh/papers/025/bounded.pdf . Read TheoremA,
  printedp29, including the immediately preceding definition of
  nonconnective Bass-completed K-theory and the all-integer degree
  quantifier. The nilpotent-exponent hypotheses match exactly.
- Thomason--Trobaugh1990, complete189page primary PDF reopened at
  https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Thomason-Trobaugh.pdf .
  Read Theorem8.1 and proof, printedp367. The quasi-separated,
  quasi-compact-open Mayer-Vietoris hypotheses hold here.
- Freshly opened full exact Stacks statements/proofs: 30.17.1
  (01XO), 45.8.3 (0FH7), 37.4.1 (0C6R), 30.24.3 (0885),
  32.10.3(2) (0B8W), 15.13.3 (0H74), 16.12.1 (07GC),
  15.51.14 (0AH2). The cited applications match their hypotheses.
- Fulton Example15.2.16(b) is the previously audited rational
  Chern-character input from C.3ad; I rechecked its role here but
  do not claim a new primary opening of that book in this audit.

The result does not claim arbitrary SNC-fibre or unrestricted-germ
vanishing. Its stated single smooth exceptional divisor scope is
preserved throughout. No formal class is silently identified with an
actual ordinary family.
