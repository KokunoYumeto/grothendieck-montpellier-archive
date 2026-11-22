# Cha 2026: exact source and cylinder scope audit

Audit date: 20 November 2026. This is an authored source/scope audit, not a new theorem promoted into the manuscript.

## Retrieved original

Jae Choon Cha, *Topological mapping class groups of non-simply connected 4-manifolds*, arXiv:2610.26400v1, 19 October 2026, 37 pages.

- Official original: <https://arxiv.org/pdf/2610.26400>.
- Direct ordinary HTTPS retrieval succeeded with HTTP 200 and PDF content, after the web reader returned `DisabledError`. No access-control bypass or credential was used.
- Original PDF: `/workspace/scratch/6b22741c5cd2/source_external/Cha2026_mapping_classes.pdf`.
- Extracted original text: `/workspace/scratch/6b22741c5cd2/source_external/Cha2026_mapping_classes.txt`.
- PDF length: 450,008 bytes.
- PDF SHA256: `27171c8dcde308b910bc8575bdd1637778e083b6729dcd7f81478499f69f207e`.

The original and its extract are outside the authored project directory. They are source material, not authored checkpoint content. The original text was read directly; this audit makes no claim to have visually inspected page images. The main introduction and definitions were read on printed pages 1–9; targeted subsequent reads covered Proposition 2.3 and Remark 2.4, the general invariant arguments on pages 11–14, Proposition 4.1 and its stated scope on pages 15–16, and the sphere-variant statements in §8.1 on pages 29–31. It does not claim a full proof audit of all 37 pages.

## Exact statements checked

The source uses oriented connected four-manifolds. Its `Homeo(M)` consists of orientation-preserving homeomorphisms fixed on the entire boundary, with isotopies relative to that boundary. `Homeo_h(M)` means homeomorphisms properly homotopic to the identity relative to the boundary. `Homeo_pi(M)` means homeomorphisms pseudo-isotopic to the identity, through a homeomorphism of the five-dimensional cylinder with its vertical boundary fixed. These are mapping classes of a four-manifold, and their pseudo-isotopy equivalence must not be conflated with path components of the ordinary concordance space of a three-manifold.

1. **Theorem A, printed page 3.** For a neat disk `D` it constructs a homomorphism from `pi_0 Homeo_h(M)` to the subgroup `Sigma_M` of the Dax target. This is an invariant. The theorem asserts neither injectivity nor a completeness/zero-test statement.

2. **Theorems B and C, pages 3–4; Theorem E, page 5.** Their realization and direct-factor/rank conclusions assume a neat disk with a geometric dual sphere in the boundary. The smooth refinement produces diffeomorphisms when the ambient manifold is smooth, and the stable refinement is explicitly a stable smoothability assertion. Neither changes the dual hypothesis.

3. **Proposition 2.3, pages 9–10; Remark 2.4, page 11.** Concordant neat disks have Dax difference in `Sigma_M`. The paragraph immediately after the proposition expressly identifies the later converse as requiring a boundary geometric dual. Remark 2.4 identifies the quotient of the Dax target by `Sigma_M` with the Freedman–Quinn target; it does not classify homeomorphism components.

4. **Proposition 3.2 and Lemma 3.3, pages 11–12.** A homeomorphism properly homotopic to the identity has vanishing Freedman–Quinn difference on every neat disk, hence Dax difference in `Sigma_M`. This is still a necessary restriction, not an isotopy or PL-smoothing sufficiency theorem.

5. **Proposition 3.4 and Lemma 3.5, pages 12–14; Corollary 3.9, page 14.** These establish additivity/naturality of the Dax invariant and its quotient on homotopy classes. They supply no identification of its kernel. In particular, no PL-to-TOP component kernel is calculated there.

6. **Proposition 4.1, pages 15–16.** This is the exact converse searched for. It assumes the two neat disks are homotopic relative to their boundary **and have a geometric dual in the boundary**. Under this hypothesis it equates disk concordance, membership of the Dax difference in `Sigma_M`, and being related by an ambient homeomorphism pseudo-isotopic or properly homotopic to the identity. Even in this scope it is a statement about moving a specified disk; it does not say a zero Dax invariant classifies every ambient mapping class.

7. **§8.1 and Theorems 8.2–8.3, pages 29–30.** The sphere variant starts with a framed interior sphere `G` and an embedded sphere `R` geometrically dual to it. Its quotient is by homotopy, and the realization theorem retains that pair of dual spheres. Lemma 8.5, page 31, explicitly makes the invariant zero for ambient homeomorphisms properly homotopic to the identity.

8. **Theorem F and Corollary G, page 6.** These concern compact complex surfaces, including finite even cyclic fundamental group examples, and produce homology-trivial classes which are not homotopic to the identity. Such a conclusion is not an ordinary concordance component calculation: an endpoint of a bottom-fixed concordance is necessarily homotopic to the identity. The associated smoothability discussion is stable and does not supply the missing unstable PL-image criterion.

## Why the boundary-dual hypothesis fails for every closed three-cylinder

Let `B` be a closed three-manifold and `M=B×I`. Suppose a neat disk `D` had a geometric dual sphere `S` in `partial M`. The connected loop `partial D` lies in one of the two boundary components, say `B×{0}`. It is nullhomotopic in `M`, because it bounds `D`. The inclusion `B×{0} -> M` is a homotopy equivalence, so the loop is already nullhomotopic in that boundary component. In particular its class in `H_1(B; F_2)` is zero.

The mod-two intersection of this loop with any embedded boundary sphere is therefore zero. A geometric dual requires precisely one transverse intersection, whose mod-two intersection is one. This is a contradiction. The argument does not require orientability of `B`; the paper's orientable case is included. It also applies componentwise when `B` is disconnected.

Thus the realization and converse theorems B/C/E and Proposition 4.1 cannot be applied to `RP^3×I`, or indeed to any closed-three-manifold product cylinder.

There is an analogous obstruction to the sphere-dual variant on this cylinder. The map `H_2(partial M; F_2) -> H_2(M; F_2)` is surjective, since one boundary inclusion is a homotopy equivalence. Consequently the map `H_2(M; F_2) -> H_2(M,partial M; F_2)` is zero. The intersection pairing of two closed interior surfaces factors through this map, so every such intersection number is zero. Two geometrically dual interior spheres would have intersection one. Hence the starting sphere pair of §8.1 does not exist in a closed-three-cylinder either.

## Consequence for the current gate

This new original source was successfully obtained and its potentially relevant converse was checked. It supplies useful general invariants, but it does not give either:

- a computation of `ker[pi_0 P_PL(RP^3) -> pi_0 P_TOP(RP^3)]`; or
- the implication that zero relative Casson–Sullivan class yields a PL representative in the same ordinary free-top concordance component.

No value of the Dax group for `RP^3×I` has been inferred here. No disk invariant is claimed complete. No stable smoothability statement has been converted into an ordinary PL/TOP isotopy comparison. This is a source-scope exclusion, not qualifying movement of the remaining general TOP comparison gate.
