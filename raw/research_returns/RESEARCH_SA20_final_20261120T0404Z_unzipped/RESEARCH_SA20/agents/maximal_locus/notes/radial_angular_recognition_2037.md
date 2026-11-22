# Radial normal form and exact angular recognition criterion

Research note, 2026-11-19, drafted after 20:37 UTC. This is outside the included TeX/Bib/CSV/check files, which remain frozen. Status: a directly proved pointwise reformulation, not an A5 closure, not yet a strictly smaller equivalent uniform gate, and no movement credit.

## 1. Scope and source input

Let R be a real closed field with a fixed o-minimal expansion. Let f:X→Y be continuous and definably proper. Fix y in a definable manifold chart of Y of positive dimension m, and identify that chart with an open subset of R^m. We discuss local triviality at y in this chart. Choose a closed Euclidean ball B̄(y,r₀) in the chart. Its inverse image X₀ is definably compact. If f⁻¹(y) is empty, definable properness gives an empty inverse image over a sufficiently small neighborhood, so this case is already trivial. Assume henceforth that the central fibre is nonempty.

The only non-elementary input to the normal form is exact triangulation of one scalar function. Shiota, *PL and Differential Topology in O-Minimal Structure*, arXiv:1002.1508v3, Theorem 2.2(1), printed p. 6, states that a continuous definable scalar function on a compact definable set becomes PL after a definable homeomorphism of its source; there is no target reparametrization. Section 2, printed pp. 5–6, explicitly works over a real closed field. Original full PDF: https://arxiv.org/pdf/1002.1508 . Locally read original text: `source_external/shiota_1002.1508.txt`, especially the displayed theorem on printed p. 6. The relative uniqueness complement on p. 7 does not by itself give a topological-to-definable comparison.

Apply this theorem to r(x)=|f(x)−y| on X₀. After subdivision and passage to the standard abstract realization of its finite simplicial complex, obtain a finite complex K with vertices the standard basis vectors of R^V and a definable homeomorphism π:|K|→X₀ such that

    g = r∘π

is linear on every simplex. Write c_v=g(v)≥0. The zero set L=g⁻¹(0) is precisely the subcomplex consisting of zero-height vertices and their simplices. The standard abstract realization is used only to make the later map depend on the finite pair (K,L), rather than on the geometric positions of vertices.

If there are no positive-height vertices, the sufficiently small band is just L. For a nonempty L and positive-dimensional target this cannot be a local product, and the criterion below has no possible homeomorphism. Otherwise put

    c = min{c_v:c_v>0}>0

and fix 0<d<c. All formulas below concern 0≤s≤d.

## 2. A fixed PL attachment map

Let λ_v be the global barycentric coordinate functions on |K|. Define the binary-height PL function g₀ by assigning value 0 to zero-height vertices and value 1 to positive-height vertices. Put

    E = g₀⁻¹(1/2),
    q(e) = 2 Σ_{c_v=0} λ_v(e)v  (e∈E).

On E the zero and positive barycentric masses are each 1/2, so q(e)∈L. The map q:E→L is PL after a finite subdivision of the level polyhedron E. It depends only on the finite pair (K,L). It need not be onto: some components of L might be isolated from all positive-height simplices.

Classical source check: Cohen, *Simplicial structures and transverse cellularity*, §9, printed p. 239, already defines precisely this binary-height PL attachment T:g⁻¹(1/2)→L for a full subcomplex L. We used the full original scan locally at `source_external/maximal_locus/cohen1967_transverse_cellularity.pdf` and visually rechecked printed p. 239 (`cohen1967_ocr/page_23.png`) at 20:43 UTC. There is no novelty claim for the PL attachment construction. The formulas below supply the exact rescaling from unequal scalar vertex heights used here.

For e∈E set

    A(e) = Σ_{c_v>0} c_v λ_v(e) ≥ c/2.

Define R_s:E→|K|, for 0<s≤d, by its barycentric coordinates:

    μ_v(R_s(e)) = (s/A(e))λ_v(e),                     if c_v>0;
    μ_v(R_s(e)) = 2(1−s/(2A(e)))λ_v(e),              if c_v=0.

These coordinates are nonnegative, sum to 1, and are supported in the simplex supporting e. They satisfy g(R_s(e))=s. Extend the same expression to s=0; then R₀(e)=q(e).

Each R_s with s>0 is a definable homeomorphism E→g⁻¹(s). Indeed, if x∈g⁻¹(s), put P(x)=Σ_{c_v>0}λ_v(x). Then

    0<P(x)≤s/c<1.

The inverse point e has coordinates

    λ_v(e)=λ_v(x)/(2P(x))              if c_v>0;
    λ_v(e)=λ_v(x)/(2(1−P(x)))          if c_v=0.

It lies in E, has A(e)=s/(2P(x)), and substitution in the formula for R_s returns x. Both maps are continuous and definable. Since K is a finite compact polyhedron and A≥c/2, there is a constant C such that

    |R_s(e)−q(e)|≤Cs

for every e∈E and 0≤s≤d. No rate uniform in a variable triangulation is claimed.

Define the embedded mapping-cylinder model

    C_q = {(s,se,q(e)):0<s≤d,e∈E}
          ∪ {(0,0,z):z∈L}.

This is definably compact, including when q is not onto. The assignment

    (s,se,q(e))↦R_s(e),   (0,0,z)↦z

is a continuous definable bijection C_q→g⁻¹([0,d]), hence a definable homeomorphism. Continuity at s=0 follows from the displayed uniform bound. The usual compact-to-Hausdorff argument here is its definable version: a continuous definable map from a definably compact set is definably closed.

**Correction preserved.** If one starts with the actual level g⁻¹(d), the natural retraction is

    x↦(Σ_{c_v=0}λ_v(x)v)/(1−Σ_{c_v>0}λ_v(x)),

which is generally piecewise rational, not PL. The binary-height level E and the formulas above give a genuinely PL q. We do not call the first retraction PL.

## 3. All remaining map data are angular

For s>0 define

    θ(s,e) = (f(π(R_s(e)))−y)/s ∈ S^{m−1}.

This is jointly definable and continuous on (0,d]×E. No extension to s=0 is asserted or needed. In C_q coordinates the map f is

    (s,e)↦y+sθ(s,e),   L↦y.

Thus source topology and the zero attachment have a fixed finite PL description; the angular family retains the unresolved information.

## 4. Exact pointwise criterion

The following are equivalent.

1. f is definably locally trivial over a neighborhood of y in the chosen manifold chart.
2. For some 0<η≤d there is a jointly definable continuous map

       h:(0,η]×L×S^{m−1}→E

   such that each h_s is a homeomorphism L×S^{m−1}→E and

       θ(s,h_s(z,u))=u,

   while

       q(h_s(z,u))→z as s↓0

   uniformly for (z,u)∈L×S^{m−1}.

The uniform assertion means: for every ε>0 there exists δ>0 such that 0<s<δ and all z,u imply |q(h_s(z,u))−z|<ε. It is a definable condition once a formula for h has been fixed. The criterion requires one jointly definable map h, not independent approximants for each s or each tolerance.

### Proof of necessity

Take a product chart T:L×B(y,η′)→f⁻¹(B(y,η′)), normalized by T(z,y)=π(z). Such normalization is obtained from any product chart by identifying its central fibre with L. Shrink to a closed ball of positive radius η≤min(d,η′), lying strictly inside the chart. For s>0 set

    h_s(z,u)=R_s⁻¹(π⁻¹(T(z,y+su))).

This is jointly definable and continuous. At each s, the product chart identifies L×S^{m−1} with the whole inverse image of the radius-s sphere, and π⁻¹ followed by R_s⁻¹ identifies that set with E. Consequently h_s is a homeomorphism, and the θ identity follows directly.

On g⁻¹([0,d]) the formula

    Q(x)=(Σ_{c_v=0}λ_v(x)v)/(1−P(x))

defines a continuous definable retraction to L, since P(x)≤d/c<1. It satisfies Q(R_s(e))=q(e). Therefore

    q(h_s(z,u))=Q(π⁻¹(T(z,y+su))).

The right side extends continuously to s=0 as z. Definable compactness of the closed parameter domain and uniform continuity give the required uniform convergence.

### Proof of sufficiency

For b≠y write s=|b−y| and u=(b−y)/s. Define

    H(z,b)=π(R_s(h_s(z,u))),   H(z,y)=π(z).

The assumed uniform convergence and |R_s(e)−q(e)|≤Cs imply continuity at all points of L×{y}; elsewhere continuity is immediate. The identity involving θ gives f(H(z,b))=b. Since each h_s is a homeomorphism, restricting it to a slice L×{u} identifies L with θ_s⁻¹(u), so H is bijective onto the inverse image of each sufficiently small closed ball. Its domain L×B̄(y,η″), 0<η″<η, is definably compact. Hence H on this closed ball is a definable homeomorphism. Restriction to the open ball supplies the desired bundle chart.

This proves both directions over every real closed field in the stated category. Disconnected central fibres are allowed. If E is empty and L is nonempty, condition 2 is impossible, as it should be.

## 5. What this does and does not reduce

The proof replaces a local source by the mapping cylinder of a fixed finite PL map q, and replaces the original target map by an angular family on a source level of one lower dimension. It is stronger than merely assuming an arbitrary mapping-cylinder presentation: the presentation exists for every continuous definably proper f at every manifold point, using exact scalar triangulation.

It does **not** prove that the existence predicate in condition 2 is definable as y varies. Quantification over all possible formula formats for h is precisely the unresolved issue. Calling the criterion an angular restatement does not earn movement credit.

There is a possible compactness route to finitely many scalar-triangulation certificate formats in a fixed input family, analogous to the already audited A5.013 argument: the scalar theorem holds in elementary extensions, each finite triangulation/homeomorphism certificate can be expressed by one first-order formula, and failure of a finite list could be compactness-realized. This observation has not been developed here into a separate audited family lemma. Even finite pointwise certificate formats would not give joint continuity in the centre y. We therefore do not assert that an arbitrary parameterized angular-family recognition problem is equivalent to the original one-map A5 question, nor that it is a strictly smaller uniform gate.

To count as new A5 movement, one must still prove either a uniform bound/selection theorem for the h in this exact criterion, or an independently meaningful lower-dimensional criterion whose parameter dependence is proved equivalent and genuinely simpler. Neither follows from the normal form alone.

## 6. Surface cell-like collar route: exact pending claims

For one continuous definable cell-like q:F→G between closed surfaces, the special mapping-cylinder criterion asks for a jointly definable continuous family h_s:G→F of homeomorphisms with qh_s→id_G uniformly. Classical near-homeomorphism approximation over R supplies individual approximants and, with additional classical isotopy/selection machinery, potentially a topological collar. A classical family produced by infinitely many concatenated approximants is not automatically definable.

One tempting route is: establish that the mapping cylinder is a topological 3-manifold with boundary G; use uniqueness of the 3-dimensional PL structure; then obtain a definable collar preserving the prescribed scalar height. The last phrase is essential. An ordinary PL collar of G is not, without further proof, a collar in which the given nonnegative PL height equals the collar coordinate.

Rourke–Sanderson, *Introduction to Piecewise-Linear Topology* (1972), Theorem 2.25, p. 24, globalizes local collars; Corollary 3.9, p. 34, makes a regular neighborhood of a compact locally collared subpolyhedron into a collar; Theorem 3.24, p. 38, gives regular-neighborhood uniqueness. Full original PDF read at https://webhomes.maths.ed.ac.uk/~v1ranick/papers/rsplx.pdf . We have not located an explicit prescribed-height conclusion in those statements, and have not supplied its proof. Those citations therefore do not yet discharge the scalar-preserving collar step.

Cohen's Theorems 7.1 and 8.1, stated on printed p. 219, characterize transverse cellularity through a PL product of the simplicial mapping-cylinder triple. Proposition 9.8, p. 240, compares simplicial and topological mapping cylinders. These exact statements do not explicitly require their homeomorphisms to preserve the mapping-cylinder scalar coordinate. We therefore do not silently substitute them for a height-preserving collar theorem.

For a family q_a with a two-dimensional parameter a, the required conclusion is a single jointly definable family h(a,s,g) with each h_{a,s} a homeomorphism and q_a h(a,s,g)→g jointly at s=0 (uniformly on compact parameter neighborhoods). Even a proof for each individual q leaves this parameter-preserving assertion open. The family cylinder has additional dimensions; uniqueness of PL structures on individual 3-manifold fibres does not solve it. No verified parametric semialgebraic monotone-map triangulation theorem has been located.

### Ledger decision

Retain this note for the exact reduction and correction of q. Do not add a theorem-ledger closure row or change the remaining target-dimension ≥3 / fibre-dimension ≥2 gate on its basis. Preserve A5.015 as method-only.
