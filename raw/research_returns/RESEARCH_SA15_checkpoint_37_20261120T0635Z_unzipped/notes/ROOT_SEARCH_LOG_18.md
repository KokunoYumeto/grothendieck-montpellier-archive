# Root source and search log after checkpoint 17

## 2026-11-19, 15:57–15:58 UTC: fixed degree-two monodromy literature check

Root searched the first search system with exact queries `"monodromy" "Hasse-Witt" "elliptic" "product"`, `"hyperplane" "monodromy" "wreath" "étale"`, and `"p-rank" "linear systems" "abelian surfaces" monodromy`. The independent stronger system queries were `"Monodromy of Hyperplane Sections of Curves" Entin`, `"Hasse-Witt" "mixed" "elliptic" monodromy GL32`, and `"etale covers" "hyperplane sections" "wreath" monodromy curve`.

The relevant primary parallel was the already catalogued Entin2021, arXiv1805.05454v3. Root freshly opened its original PDF and read Theorem2 on printedp3, the quasireflexive definition and discussion onp6, and the complete Proposition3.1 and proof of Theorem2 onpp7–8. The exact opened refs are turn782329776view0 and turn514117024view0/view1. The unlabelled S18 result is a known application of that theorem after our jet argument verifies quasireflexivity. The elementary-abelian labelled wreath extension, all gluing translations, and common-grid finite-Lang comparison are proved directly here. No exact fixed-mixed degree-two Hasse–Witt group theorem was located in these searches, and no priority claim is made. Unrelated metadata and nonprimary search results were not used as mathematical sources.

## 2026-11-19, after 15:41 UTC: topic-specific literature searches for B50-B51

Root searched both available search systems. Exact first-system queries were:

- `Bondarko finite height formal groups generic fibre kernel Frobenius logarithm ramification p squared tame inertia`
- `potentially Barsotti Tate representations congruent modulo p squared different inertial type ramified base e p minus one`
- `height two p divisible groups tame inertia finite determinant norm one torsion congruence`

The independent stronger-system queries were:

- `"Barsotti" "modulo p2" "ramified"`
- `"height two" "inertial type" "torsion"`
- `"Bondarko" "Frobenius" "ramification" formal groups`

The searches returned the previously opened original Bondarko article, Savitt's potentially Barsotti-Tate papers, and Daniel Le's *Multiplicity one for wildly ramified representations*. The last source is a lead being inspected separately by the reduction/descent agent; its unramified-base restriction prevents using its introduction's modulo-p² statement for the present e=p-1 base. Other results were search metadata only and were not used as theorems. These searches did not locate the exact closed product-height-two bound or the present primitive-norm remaining-case statement. No novelty or priority claim follows from that outcome. B51's finite cyclic-character arithmetic is proved directly.

## 2026-11-19T15:39:14.659534+00:00: B50 closed logarithm boundary and square finite determinants

Root read the complete candidate B_tame_norm_square_boundary.tex and reread the entire earlier B_height_two_logarithm_gate.tex, including the coefficientwise logarithm, bounded-projection and saturation proofs. Root freshly opened the original Bondarko PDF at https://www.mathnet.ru/links/143cd4ef0c053a08f030f68ecac286cd/im691_eng.pdf, actually read Propositions9-12 with their written proofs and Lemma3, printed pp674-676, and the whole statement and proof of Proposition16, p681. The web views were turn498664735view0/view1 and turn985317369view0/view1. No new visual page inspection is claimed. The exact ideal in Proposition9 is m^(-floor(a/(1-p))), so equality gives the same ceiling exponent; the argument is coefficientwise in a formal augmentation variable. The previously audited Theorem2(8), equation6 supplies the covariant Frobenius identification, and the previously audited Tate1967 Theorem4/Corollaries1-2 supplies the actual integral duality maps used by B33.

The full program verify_tame_norm_square_boundary.py was read and independently rerun; its output is retained in outputs/root_verify_tame_norm_square_boundary.json and its stdout in the adjacent text file. Author output is unchanged. Runtime 1.491409575995931 seconds. The companion complete proof/source/code audit is agents/obstructions_crystals/B50_independent_audit.json. All three statements pass. The proposed m=2(p-1) refinement is separate and is not included in this verdict. No priority claim and no existence claim for a remaining pair is made.

## 2026-11-19T15:51:50.923536+00:00: complete fixed-mixed degree-two wreath/grid audit

Root read the complete five-assertion candidate and its entire graph program, and independently rederived every proof. Fresh original Stacks0BMB,0BTN,09ZS and04GK statements and proofs were opened and read; their web refs were turn262867968view0/view1 and turn183462683view1/view2. The direct Kantor-Seress author URL https://pages.uoregon.edu/kantor/PAPERS/ksfinal.pdf returned a content-length error (57,682,627 bytes), retained as a failed fresh retrieval. Root instead read the previously downloaded original text and actually viewed its retained original printed-page22 image, agents/monodromy/outputs/kantor_seress_theorem_page22.png. The four exact alternatives of Theorem3.6 are SL, Sp, the two orthogonal groups overF2, and the stated symmetric groups; all proper alternatives in dimension32 preserve a nondegenerate alternating form. This is use of the opened Kantor-Seress statement, not a claim to have opened McLaughlin's unavailable original full text.

Root reread the complete elementary H1 cocycle proof in quintic_exact.tex, the product-small-degree-jets proof, and the finite-Lang/purity/projective-space argument in product_full_groups.tex. The extension of the old fixed-cubic jet proof to arbitrary E_a and E0 was explicitly checked through their polar partials. The common-grid proof keeps the rank30 finite part distinct from the generic rank34 fibre. The graph certificate rerun passed in 0.00013814800331601873 seconds and preserved the author's output. Independent reduction/descent and obstruction/crystal mathematical audits also passed; their separately recorded source/code scopes remain distinct.

## 2026-11-19T16:02:09.241057+00:00: positive-index toral-bundle source/proof audit

Root read all three proofs in post_CP17_positive_index_bundle_notes.tex, with the explicit algebraically closed base correction. Root actually read original Edixhoven–van der Geer–Moonen Lemma7.19 and its full proof, printedp105, from the retained original full-book extraction agents/obstructions_crystals/sources/edixhoven_geer_moonen_AV.txt (the associated original PDF is retained). This is a fresh content read of an already opened source, not a claim of a new network retrieval or new visual inspection. The proof's acyclicity conclusion is exactly the needed one for the nontrivial Picard line P. The prior actual theta descent and toral Cartier pairing arguments were rechecked at their uses. All three lemmas pass. The remaining residue formula and determinant nonvanishing are still unproved. No finite computation is substituted for this missing geometric step.
