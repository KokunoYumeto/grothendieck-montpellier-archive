# Higher concordance comparison working report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort,
agent `/root/higher_comparison`; RESEARCH_SA20, 19 November 2026.
No priority is claimed. Parent owns final assembly and persistence.

## Current outcome

**A.133 proved and authorized for promotion:** elementary extensions
in one fixed o-minimal language preserve the entire definable
concordance simplicial group up to weak equivalence. The proof is in
`part_elementary_extensions.tex`, and the records are in `results.csv`
and `checks.tsv`. It applies more generally to marked automorphism
groups of closed bounded definable sets. Root independently read the
full proof and opened Coste's original framework and Hardt theorem.

The proof replaces the false inference from pointwise transfer to a
family by a graph-space continuity argument. Hardt triviality on each
coefficient cell produces a continuous bijection from the product
with one compact graph fibre to the product with the fixed domain.
Definable curve selection and compactness prove that its inverse is
continuous. Evaluation and inverse evaluation are therefore jointly
continuous on each cell. Cell paths retain all prescribed relative
homeomorphism conditions. Exact nullhomotopies descend by a single
first-order existential sentence.

For a fixed finite rational PL manifold, the PL-to-definable comparison
commutes with these extensions. If a complete o-minimal theory has a
real model, the established real-field comparison properties transfer
to every model of that theory. In dimension at least five this yields
injectivity in every degree and the fundamental-group isomorphism
from A.114. The real-model condition is retained explicitly. A
countable elementary submodel gives a countable model only; no
effective presentation or solution of the remaining comparison gate
is claimed from an undecidable elementary diagram.

**A.132 independently audited: PASS.** The full written proof of the
real PL–TOP discrepancy for S3 was read, including the common-radius
relative germ lifting, the free outer boundary of its strict fibre,
the identity-component restriction, and the compatibility of the
actual maps with O4→TOP4. Original Edwards–Kirby, Hatcher,
Freedman–Quinn, corrected GGHKP2026, Burghelea–Lashof and
Kirby–Siebenmann locators were independently inspected as recorded
in `A132_independent_audit.md`. This result is about PL–TOP and does
not settle PL–semialgebraic comparison.

## Remaining higher comparison gate

The active objective is still a relative parameter-preserving
straightening of a definable or semialgebraic homeomorphism of a
trivial bundle over a simplex, with prescribed jointly PL boundary.
The established one-parameter argument does not yet give the
two-parameter family theorem. A.131 computes separate effective PL
and SA models; it does not establish their weak equivalence.

The exact failed routes and opened sources are recorded in
`notes_1906.md`: Nariman's fragmentation lemma requires an appropriate
local contraction and isotopy fragmentation; Gauld's infinite
endpoint construction is not shown definable; Yagasaki's vector
bundle result is slice-wise PL; Shiota's compact-fibre bundle
triangulation remark is prospective, while the proved conclusion is
stable microbundle reduction. Ordinary mapping-space approximation
does not retain homeomorphisms.

`finite_PL_approximation_obstruction.md` proves an additional precise
method limitation: any N-piece affine approximation to x² on [0,1]
has error at least 1/(8N²), over every ordered field. Thus finite PL
maps are not dense at positive infinitesimal tolerances over a
non-Archimedean field. This does not obstruct isotopy—the map x² has
an explicit semialgebraic isotopy to the identity—and it is not
counted as a higher-family counterexample.

The next research direction is an actual semialgebraic bundle
classification theorem over compact bases, or a finite local
extension construction that supplies coherent parameters. It must
go beyond generic Hardt trivializations and the prospective compact
bundle statement in Shiota's Remark2.7.

## A.138: fixed-format metric theorem

Root independently audited and authorized promotion of `part_finite_format_metric.tex`. For every fixed finite collection of graph formulas, the space of actual marked definable homeomorphisms is affine in the uniform map-and-inverse metric over every o-minimal real closed field. Its sufficiently small relative open stars give strong definable contractions through the same marked homeomorphisms, with joint evaluation and inverse evaluation. The proof uses the compact-graph continuity argument and the exact original Walsberg Theorem 7.1, p. 16, together with the quotient convention on p. 1 and uniform formulation Corollary 7.24, p. 26.

The theorem also proves the sharp method bound `sup|x^2-p| >= 1/(8m^2)` for every m-piece affine map, so finite PL density fails at positive infinitesimal tolerances. The endpoint-fixed semialgebraic isotopy `(1-s)x^2+s*x` shows why this is not an isotopy counterexample. The attached checker passed 76 exact checks with zero failures; its recorded author runtime is 0.04335108300438151 seconds.

This is method-only: the contraction radius depends on the formula formats, and increasing PL approximation complexity still changes that radius. No original higher comparison gate or review movement is claimed.

## A.141: support-localized ordinary loops and the component image

Root and singularities_duality independently audited the complete proof and authorized `part_support_localized_four.tex`. For a compact simply connected codimension-zero PL four-submanifold W of a closed oriented PL four-manifold B, ordinary TOP loops supported inside W realize the image of H2(W;Z/2) in H2(B;Z/2), expressed by Poincare-Lefschetz duality as extension by zero in relative cohomology. The construction retains the vertical boundary throughout OPR block realization, corrected GGHKP ordinary pseudo-isotopy trivialization, and the passage to actual ordinary loops. Spatial collar compression and time collars give one common support, and naturality of the universal KS lift difference gives the exact ambient class.

When the homology inclusion is onto, J_B is all of H2 cohomology and the PL concordance component image is exactly I_B, the subgroup specified by the TOP-isotopy-to-PL condition on the top map. This applies to C#D where C is simply connected and H2(D;Z/2)=0, including C#k(S1xS3). No assembly condition on the ambient fundamental group is imposed. If H2 cohomology is nonzero, the ordinary automorphism comparison also fails pi1-surjectivity. The endpoint condition and the whole concordance spaces remain unevaluated; no automatic original-gate movement is claimed.

## A.162: the projective concordance fibre and its split forgetting kernel

The full proof in `part_RP3_equivariant_germs.tex` gives a natural real TOP model
`P_TOP(RP3) ≃ hofib(O4 → |G_odd|)`, where simplices of `G_odd` are joint germs
along an entire compact parameter zero section. A canonical Edwards--Kirby
operator on the free projective quotient annulus supplies relative finite-family
extension. BCC's annulus theorem is used only for individual vertex extension.
The fixed-radius fibre is the actual free-top projective concordance space.
The middle group is replaced by O4 using Bamler--Kleiner's projective Smale
theorem and the ordinary three-dimensional Diff--TOP comparison, not the
nonequivariant sphere assertion alone.

The exact A132.11 bridge preserves O4 and identifies ordinary joint-germ pi1
with pi1 TOP4. It splits the linear Z/2 subgroup in odd-germ pi1. Therefore
pi0 P_TOP(RP3) is abelian and naturally equals the kernel of the forgetting
map from odd to ordinary joint-germ pi1. This kernel remains unevaluated.
For K equal to that kernel, I the PL image and chi its surjective CS map,
the proved exact sequence is `0 → ker(chi)/I → K/I → F2 → 0`.
No assertion I=ker(chi), no PL-to-TOP component injectivity, and no whole-space
row closure follows. This is a structural result with NO qualifying main-gate
movement. The original candidate is preserved unchanged for provenance.

Source and review metadata are in `A162_metadata.json`; five pending Bib entries
are in `A162_references_pending.bib`, reusing the existing EdwardsKirby1971 key.
Root and dual independently audited the full candidate; root also read the
complete promoted source and checked the added algebra and natural model bridge.
