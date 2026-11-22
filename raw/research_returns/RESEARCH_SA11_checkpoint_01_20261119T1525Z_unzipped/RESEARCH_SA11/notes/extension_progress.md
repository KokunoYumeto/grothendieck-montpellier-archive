# Extension-space branch — 19 November 2026

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); branch extension.

## Source status

Opened full Sturmfels–Ziegler (1993), published PDF https://link.springer.com/content/pdf/10.1007/BF02573961.pdf (web ref turn515878159view0), and author preprint https://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/Preprintfiles/020PREPRINT.pdf (ref turn101835110view0; downloaded and extracted locally). Exact published locators: Theorem 1.2 p. 25; Lemma 3.2 p. 29; Definition 3.4 p. 30; Proposition 4.2 pp. 37–38; Lemma 4.1 p. 37; Corollary 4.5 p. 40. Theorem 2.3 pp. 27–28 is the cubical Baues-poset identification for realizable M. Lemma3.2 was rechecked against the published text and the parent independently reviewed its use.

Opened full Mnëv–Richter-Gebert (1993), https://link.springer.com/content/pdf/10.1007/BF02573981.pdf, web ref turn515878159view1. Its disconnected examples are rank FOUR, not rank three: pp. 271–273, introduction and §1. No contradiction to the rank-three result.

BKS1994 full published scan FOUND and opened at https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Billera/BilleraKapranovSturmfels.pdf, current web ref turn612036681view2. Publisher/JSTOR attempts were blocked, but the UC Davis archive contains the original paper. Complete OCR saved and theorem page visually inspected. Exact locators: Theorem1.2 p550; Proposition2.1 and Theorem2.3 p552; coherent-string monotone-path-polytope boundary p553; generalized Baues problem p554 and scope comments p555. Bibliography updated to opened. Its generic functional theorem does not identify the manuscript cyclic-port selection with coherence.

No arXiv source found for these 1993/1994 papers after exact-title searches; used author/publisher PDFs.

## Proved results

1. New-element reorientation σ↦−σ acts freely on order complex of extension poset. SZ contraction Π is equivariant and satisfies Babson's criterion; quotient E(M)/± is homotopy equivalent to RP².
2. Opposite ordinary extension poset is cubical: ν zero cocircuit pairs produce one ν-cube. Parallel extensions produce polygonal two-cells with link E(M/i). Every closed cell embeds literally as its principal-ideal order subcomplex; no colimit embedding assumption.
3. F(−1)=1−n for F(t)=Σ cν tν, ordinary unoriented extensions.
4. Fixed old vertex v, cocircuit±Y: P_v={σ:σ(Y)=0}. Restriction of Π gives P_v≃S¹, since target is suspension of two points. Removing μ(v) parallel pairs through v leaves Euler μ(v), so Σ_{D throughv}(−1)^{ν(D)−1}=μ(v). Sum over v gives F′(−1)=Σ_v μ(v).
5. Marked comparison for blowups: sector inverse images under Π contractible, meridian inverse images contractible. Parallel h≠g are regular interior interval points on their meridian and boundary half-disk points of adjacent sectors. They separate g+ and g−: evaluation on a second vertex w∈h is zero only at [h], opposite at g±. Thus the punctured extension complex is homotopy equivalent rel peripheral circles to sphere minus2n discs (equivariantly); projective quotient is RP² minus n discs. Attaching n Möbius bands yields homotopy N_{n+1}.
6. L2 is false: all ordinary relative positions are face labels in154/45, so all2^ν stable generizations occur. The complete comparison identifies the dual surface with a subcomplex of B(M): selected face-incidence diamonds plus the entire flag-subdivided Mobius bands. It contains the entire one-skeleton; omitted diamonds normally generate the kernel on pi1. Added relative k-cell counts are 2F''(1)-F'(1)+b in dimension2 and (2^k/k!)F^(k)(1) for k>=3. If c3=0, this subcomplex is the whole B(M). The blow-down collapses exactly the n inserted core circles. All attaching maps and embeddings are proved in E6.

## Root computation received

n6_three_pair has c=(80,150,75,10), and T3's surface theorem gives χ=−45. The convex moment-curve example instead has c=(74,132,57,4), χ=−21. Corrected formula χ=1−n−4Σ_{k≥1}k c_{2k+1}. Counts-branch matroid enumeration and gluing are independently compared with the complete cubical and band model by extension_compare_cells.py; this branch does not claim an independent re-enumeration of all oriented-matroid extensions.

## Additional proof/source checks

Parent independently reviewed E1–E4 against the published Sturmfels–Ziegler source and found the arguments sound. E4 includes the separator argument and explicit equivariant boundary maps, paths, sector fillings, and cofibration gluing. E5 is labelled Proved under stated hypotheses (T3 verifies all here); this branch reviewed T1–T3 and recorded those checks.

For the lune sweep in the parent's gluing proof, the preferred setup uses g=D as the affine hyperplane and f=i as objective, with the objective sign chosen toward the old wall i. Every old wire crossing the lune has its infinity point outside v=D∩i, so its directed edges are strict. Use SZ Definition3.8(i) and Proposition3.9 p33 for Euclidean/no-directed-cycle equivalence, and Corollary4.5 p40 for rank3. G_f's graph and directed-path conventions are on pp30–31. The polygons branch is supplying the detailed source/empty-fan proof.

Final owned integration files: `sections/A2.tex`, `audit/extension_results.csv`, `audit/extension_CHECK_EVENTS.tsv`, `extension.bib`, `notes/extension_source_audit.md`. The last audit records exact opened/not-opened source status, checked locators, literature search coverage, all finite checks, and no-priority language. No optional source search remains underway.
