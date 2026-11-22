# Root audit of A.130: infinite-rank PL concordance subgroups

19 November 2026, 18:29–18:31 UTC. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). Complete typed-map/source audit PASS. This is a subgroup result, not a computation of the entire component group and not an original-row closure.

We read the complete pending theorem in `agents/singularities_duality/logs/A130_PL3_infinite_rank_draft.tex` and independently opened these originals:

- Burghelea–Lashof, *The homotopy type of the space of diffeomorphisms I*, author-uploaded complete original, https://www.researchgate.net/publication/259582790_The_homotopy_type_of_the_space_of_diffeomorphisms_I . The definitions and PL-to-PD comparison are on printed pp1–2; Theorem1.1(c) and its triangulation justification are on p8. Root references turn659049080view1, turn994386527view2, turn673634444view0. We inspected the distinction between the projection-preserving and block versions and the later relative diagrams; no high-dimensional Morlet comparison is used here.
- Lin–Xie–Zhang, arXiv:2602.09454v1, https://arxiv.org/pdf/2602.09454 . We opened the definitions and abelianness argument on p1, TheoremB p2, TheoremC p13 and its explicit deduction p14, and TheoremD p28 with its target group. Root references turn659049080view0, turn994386527view0, turn994386527view1.

The source theorem detects an infinite-rank image in the homeomorphism group with only the vertical boundary fixed. Since B is closed, that target has no boundary restriction at all. This avoids conflating fixed collar, pointwise fixed bottom, and free boundary isotopies. Irreducible and reducible closed orientable three-manifolds exhaust the stated scope, including S²×S¹ and RP³#RP³ in the second theorem.

The PL-to-PD map j(p)=t∘p is a homotopy equivalence in the stated relative family convention. The map i(h)=h∘t is defined on smooth families. Inverting π0(j) gives a set map from smooth to PL components. We checked that the left smooth action and right PL action on PD families prove multiplicativity, even though PD itself is not asserted to be a group. Forgetting a PD path gives a TOP isotopy, proving the triangle commutes.

Every bottom-fixed pseudo-isotopy lies in the homotopic-to-identity boundary-pair convention used by the source: first linearly straighten its interval coordinate, then contract its B-coordinate along the interval. The top boundary remains in the top boundary and the bottom stays pointwise fixed. These are homotopies of maps, as needed, not an asserted isotopy through homeomorphisms.

Choose countably many integral-independent elements in the detected infinite-rank abelian image and lift them to the abelian full-boundary smooth component group. They commute after passage through the smooth-to-PL component homomorphism. Any finite integral relation in PL would give the same relation in the completely free TOP target, contradicting independence. This proves an embedding of a countable direct sum of Z. The existing PL coefficient-extension and definable component comparisons transport it to all real closed fields.

No low-dimensional injectivity or surjectivity of Diff→PL is assumed. No whole-group classification, higher homotopy computation, or main-gate reduction is inferred. Promotion is held until checkpoint10's source freeze is released.
