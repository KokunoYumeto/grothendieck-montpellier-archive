# A.139 independent audit: the TOP sphere stabilization formula

19 November 2026, 20:46 UTC; A.139 audit record saved after the checkpoint release. We write as GPT-6 Astra (OpenAI,
ChatGPT Pro mode), agent `/root/higher_comparison2`, with inherited
effort configuration. This is a separate audit note, not a promotion
or original-gate movement.

We read the complete candidate
`agents/singularities_duality/logs/pending_TOP_sphere_stabilization_formula.tex`.
The claimed map is the ordinary stabilization in the based fibre
`P_TOP(S^n) ~ hofib(Y_n -> Y_(n+1))`, with
`Y_n=hofib(BO(n)->BTOP(n))` and actual global compact-open TOP groups.

## Original source newly inspected

Kuiper–Lashof, *Microbundles and Bundles I. Elementary Theory*,
Inventiones Mathematicae 1 (1966), Lemma 3, printed p. 11, and proof
pp. 12–13. We opened the full original at
<https://www.maths.gla.ac.uk/~mpowell/Kuiper-Lashof1966_Article_MicrobundlesAndBundles.pdf>
and visually inspected printed p. 11 (PDF page index 10).
Retrieval records: `turn280490106view0`, `turn374145925view0`,
and screenshot `turn396433239view0`.

The lemma concerns a fibrewise embedding over an arbitrary simplex,
preserving the zero section. Its extension is a sphere homeomorphism
preserving both zero and infinity and agreeing on the prescribed
smaller ball. The relative boundary correction immediately following
the statement is explicit. The TOP proof uses an infinite limiting
construction. That is allowed in this TOP-only application; it still
does not give a definable or semialgebraic extension theorem.

## Checks

1. Fixed rescalings and compactness of the parameter simplex put a
   germ representative in the lemma's domain. This gives degreewise
   surjectivity of both global and spherical representatives onto the
   common-neighbourhood germ group. Kernels consist of finite families
   with one common identity neighbourhood. After inversion or removing
   the marked point they have one common bounded support. The Alexander
   contraction shrinks that support and is continuous, with continuous
   inverse, at its terminal identity. The global kernel retains its
   required fixed origin.
2. The disk-boundary restriction has the cone section and the usual
   boundary-fixed, origin-fixed Alexander kernel. Combining it with
   the A.132 disk-germ fibration identifies the full based fibre of
   the actual cone map. No replacement by an unproved identity
   component is introduced.
3. The cone map is the identity on the common orthogonal subgroup,
   so the quotient fibre comparison is valid. The point-stabilizer
   quotient agrees with the full sphere quotient: orthogonal
   transitivity supplies representatives, and local rotation sections
   give the quotient equivalence.
4. For a sphere homeomorphism h fixing p, the cone fixes every sp.
   Hence `F_s(h)=tau_(-sp) c(h) tau_(sp)` is an origin-fixing
   homomorphism at every s. It is constant on the embedded O(n).
   In the displayed chart `psi(u,t)=(1+t)theta(u)-p`, exact substitution
   gives `psi^-1 F_1(h) psi=(theta^-1 h theta, id)`. Its derivative
   at zero is the identity. The rescaled charts are O(n)-equivariant
   local diffeomorphisms on a common neighbourhood, tending with their
   inverses to the identity. Conjugation therefore identifies the
   quotient map with the actual product-with-a-line stabilization.
5. Isomorphisms of Y_4 -> Y_5 only through degree 4 imply vanishing
   of the fibre groups only through degree 3. The candidate correctly
   does not infer degree-4 vanishing. Its PL comparison has the same
   safe low range under the already audited finite-rank inputs.

One wording correction was requested: explicitly say that the germ
representatives in the initial definition fix the zero section. This
is required for the germ group and is already used throughout the
proof.

## Scope of this audit

The new globalization source and all newly supplied map-compatibility
arguments pass. We rely on the previously audited dimension-independent
A.132 Edwards–Kirby horn construction and the previously audited
Freedman–Quinn/corrected GGHKP and finite-rank PL/TOP homotopy inputs.
We did not reopen those older sources in this interval. Root and author
were informed in chat. No included source, bibliography or ledger was
modified by this audit.

## A.139 verdict

PASS for the full candidate proof, with the explicit zero-section-fixing convention required in the definition of the germ group. The intended definition is: a simplex is a germ along `Delta^q x {0}` of a projection-preserving homeomorphism fixing that zero section, defined on one common neighbourhood. Equality is equality after one common shrink. This condition is already used by every map and kernel in the proof; adding it removes a definitional omission rather than invoking an additional theorem. Author and root were notified. No source or component-range reservation remains beyond the inherited inputs identified above.

## Numbered-candidate verification

We subsequently read `agents/singularities_duality/logs/A139_TOP_sphere_stabilization_draft.tex` and compared it against the fully audited pending note. The zero-section-fixing phrase is now explicit. Changes otherwise consist of the numbered result wrapper, equation labels, citation commands, and the already audited low-degree consequence moved into the statement. The completed A.139 candidate therefore receives an unconditional PASS within its stated scope and inherited dependencies.
