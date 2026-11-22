# Root audit of A.134: natural real PL–TOP comparison in dimensions at most two

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. No priority is claimed.

## Verdict

PASS for the complete draft `agents/singularities_duality/logs/A134_low_dim_TOP_comparison_draft.tex`, with the explicit component normalization incorporated in the final proof. We read every line and rechecked the cited original passages listed below. The independent full audit is `agents/higher_comparison/Hamstrom_surface_comparison_audit.md`.

The conclusion concerns the actual natural map from the simplicial group of **jointly PL, parameter-projection-preserving** concordances to the singular complex of the compact-open TOP concordance group, with the entire bottom fixed and the top free. It holds for every compact real PL base without boundary whose components have dimension at most two, including finite mixed-dimensional disjoint unions and the empty base. It does not assert higher PL–semialgebraic equivalence.

## Source convention and component repair

We opened Hamstrom's original *Homotopy in homeomorphism spaces, TOP and PL*, Bulletin AMS 80 (1974), 207–230, at §0.2 p.208, §2.1 pp.222–223, Theorem 2.3.1 p.224 and Theorem 3.1.2 pp.225–226:

<https://www.maths.gla.ac.uk/~mpowell/Hamstrom%20homotopy%20in%20homeomorphism%20spaces.pdf>.

The manifold convention includes compact manifolds with boundary. The chosen PL model has jointly PL total simplex maps and homotopies preserving all parameters. It is explicitly distinguished from the topology of slice-wise PL homeomorphisms. The comparison theorem is the natural inclusion, not an unspecified equivalence of weak types.

Hamstrom's TOP notation means the identity component. Her PL vertices are all PL maps in that TOP component; their PL path connectedness is not assumed. The proof therefore supplies a separate argument on full components. We opened Laudenbach, *Topologie de la dimension trois*, Chapter I §1 Theorem 1.1 p.7 and the ordinary-isotopy conclusion p.8:

<https://smf.emath.fr/system/files/filepdf/AST_1974__12__1_0.pdf>.

Pointwise Moise–Bing approximation and TOP local path connectivity give a PL representative in each TOP component. For injectivity, normalize the initial PL endpoint to the identity. Approximate a finite subdivision of the TOP path by PL vertices in that TOP component, keeping endpoints exact. Uniform PL local 0-connectivity joins each small increment to the identity by a jointly PL isotopy; finite concatenation remains jointly PL. This proves the full component bijection. Translation by PL representatives then extends the higher comparison to every component.

Laudenbach's quasi-simplicial footnote is **not** the higher-family input. The earlier Morlet convention audit remains valid history and explains why that shortcut was rejected.

## Closed surfaces

For a closed surface F, the cylinder F×I is a compact PL three-manifold. The subgroup preserving its bottom setwise is a union of full components because boundary-component permutation cannot change along a path. Therefore the full comparison restricts to this subgroup.

Bottom restriction r has the product section s(a)=a×id. The two formulas

`h ↦ (h s(rh)^(-1), rh)` and `(p,a) ↦ p s(a)`

are mutually inverse at every simplicial degree, preserve the joint parameter condition and commute with the natural comparison. They are an actual product decomposition of the underlying spaces, although the group law is semidirect. A product map between nonempty spaces is a weak equivalence only if both factors are. This proves both the concordance comparison and the full homeomorphism comparison for every closed surface. No relative boundary fibration, separate surface comparison, smoothing choice or orientability assumption is concealed in this argument.

## Circles, points and components

We reopened Scott's original 1968 Warwick thesis, *Some Problems in Topology*:

<https://wrap.warwick.ac.uk/61719/1/WRAP_THESIS_Scott_1968.pdf>.

Chapter III §0 p.19 makes all maps PL and Definition 0.1 imposes parameter projection. Chapter IV uses those definitions. Theorem 3.1(b)(iii) p.51 and its annulus proof p.53 give the natural interior evaluation isomorphism in every positive degree. Moving the evaluation point along a fixed path to the bottom, and using Hamstrom's explicit degree-one PL circle evaluation, shows that bottom restriction induces all positive homotopy isomorphisms. The same product splitting forces positive concordance homotopy groups to vanish. We reread the complete circle argument of A.123 for components; its free-top PL twist removes the relative annulus winding. Thus the whole PL concordance space of the circle is weakly contractible.

We also opened Yagasaki's original preprint `math/0010223`, Lemma 2.1(ii) p.2 and proof p.3:

<https://arxiv.org/pdf/math/0010223>.

Its compact-surface boundary-fixed identity component is contractible. We opened Epstein's original Theorem A4 p.107:

<https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6005-11511_2006_Article_BF02392203.pdf>.

It gives an isotopy to a PL annulus homeomorphism. The formula `(a_t^(-1) × id) h_t`, where a_t is the bottom restriction, corrects this isotopy to fix the bottom throughout. Its endpoint is a PL concordance, and A.123 then connects it to the identity. This proves that the entire TOP concordance group is its contractible identity component. Epstein's conventions allow a boundary basepoint; his Theorem 5.2 explicitly discusses this case.

For points, the TOP interval contraction is valid. The PL argument instead uses Hamstrom's total-family Alexander cone construction (Theorem 2.2.1 p.223), avoiding bilinear interpolation. Bottom-fixed concordances preserve each cylinder component. Finite products and the one-element empty-base group finish the stated scope.

## Consequence for the main gate

Together with A.131 this supplies the whole explicit recursive TOP model in all base dimensions at most two. Together with the already proved comparison in dimensions at least five, it confines the remaining **general real PL–TOP comparison** to base dimensions three and four. A.132 separately computes the three-sphere TOP model and refutes unrestricted weak equivalence. Neither theorem settles the remaining general three- or four-dimensional branch, nor the higher PL–SA/arbitrary-definable comparison.

No finite counterexample is asserted here, so no new finite enumeration is required. The proof is a full parameter and component deduction from opened original theorems, and its scope is stated without claiming priority.
