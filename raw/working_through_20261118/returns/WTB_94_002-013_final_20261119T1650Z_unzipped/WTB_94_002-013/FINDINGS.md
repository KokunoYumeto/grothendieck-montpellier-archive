# WTB_94_002-013 — findings by unit

Scope: cote 94, scans 2–13. The sixteen units below replace the fourteen draft divisions as specified in `UNITS.tsv`. The root, GPT-6 Astra Pro (effort not exposed), performed the image reading and mathematics in one stream; the additional worker handled mechanical validation only. The whole sheets, thirds and enlargements are documented in `records/crop_manifest.jsonl`; the limited display-order exceptions are disclosed in `records/method.md`.

`PROOFS.tex` distinguishes our proofs, exact literature matches, and the certified `SETTLED` background that the prompt instructs us to carry. `records/SECOND_CHECKS.md` records later, separate targeted checks of our proofs, without claiming an independent worker. All six note entries have verdicts. The count and full disposition of individual reading decisions are in `SCAN_CHECKS.tsv`; reading uncertainty is not a mathematical correction.

## 94:2 — Construction des Modules cohérents

**What the sheet does.** This is a cover programme for constructing coherent modules and treating duality. It contains headings and a differential symbol, but no theorem, proof, or independently decidable construction.

**Checked.** The whole cover and its enlarged headings were compared with C and with H's actual cover paratext. H's page map says there is no text for this scan, but its section heading and unnumbered introductory note do quote the cover. These references in `SCAN_CHECKS.tsv` are to that paratext, not to a nonexistent H page.

**Findings.** The symbol following the visible differential notation remains uncertain; no mathematical interpretation resolves the ink. The cover is removed from the draft ranges assigned to Lemme 2 and the absolute-value classification. Note #1 is accurate as a description, subject to that uncertainty. No research direction arises from the headings.

## 94:3 — Construction de faisceau|faisceaux de modules; Lemme 1

**What he does.** He associates to a functor on A-modules its restriction to B-modules and gives a faithfully flat descent test for representability. The test includes left exactness as well as representability after changing rings.

**Checked.** C01 proves the base-change formula by explicit mutually inverse tensor–Hom maps. C02 supplies Yoneda descent, the cocycle, effectiveness of module descent, and recovery of the original functor by its preserved descent equalizer; finite generation and finite presentation also descend. The second check reconstructs the universal element and checks the two scalar structures in the equalizer. Exact opened references are Stacks Proposition 35.3.9, Descent p. 8, and Lemma 10.83.2, Commutative Algebra p. 198.

**Findings.** The right-hand side of the lemma really retains left exactness. Corrections to H concern the restriction/base-change notation and local letter readings; uncertain overwritten letters remain marked individually. The heading's singular/plural ending is not decided from grammar. The canceled par in Lemme 1 is retained against H's omission. Notes #1, #2 and #5 lead to C01–C02; no mathematical gate remains open.

## 94:3.2 — Lemme 2, scans 3–4

**What he does.** He combines representability over A localized at f and over all A/f^n with continuity over the f-adic completion. The purpose is to obtain one finite representing A-module.

**Checked.** C03 constructs compatible finite representatives over the quotients, passes to their finite inverse limit, identifies the functor first on finite completed modules and then on all completed modules, and descends along A to the product of its completion and A_f. The second check verifies surjectivity of the kernel transitions, the completeness comparison, and faithful flatness of that product, including nilpotent and invertible f. Stacks Lemma 30.23.1, Cohomology of Schemes p. 60, gives the exact formal-module existence result used.

**Findings.** The completed coefficient ring in the continuity hypothesis is live; an earlier hat on the argument is canceled. The proof's subsequent unhatched phrase about finite A-modules cannot identify the two module categories: Z_p is finite over itself but not over Z. C03b records this as an authorial wording slip and supplies the correct filtered union over finite completed-ring modules. The scan is not rewritten to insert a hat. Whether le before module P is canceled remains uncertain on the ink. Notes #1–#2 are completed by C03–C03b; no direction remains open.

## 94:4 — Proposition 3, scans 4–5

**What he does.** He turns the preceding local gluing criterion into a noetherian-induction criterion, testing every nonzero quotient of A on a nonempty principal open. The completion and colimit conditions are retained.

**Checked.** The certified statement H035.5 is carried in C04, without re-proving it. The small nonzero insertion, its curved leader, the quotient B, the order of the conditions, and the use of a nonzero power in the induction were read on enlarged images.

**Findings.** Proposition 3 is true as written: “non nul” is on the page, contrary to H's omission and a discarded earlier criticism. The correction is a scan error in H, not an added mathematical hypothesis. The arrow/condition issue flagged by note #6 is resolved by the written ordering. Notes #1, #2 and #5 are consistent after preserving this qualifier; no new direction is open.

## 94:5 — Proposition 4, scans 5–6

**What he does.** For a noetherian local ring he gives a representability test using completion, filtered colimits, left exactness and a finiteness condition. The proof passes through the indecomposable injective modules of the Artinian quotients.

**Checked.** C05 proves the Artinian comparison G(M) = Hom(DM,G(E)) using a copresentation by finite sums of the injective hull E, then applies finite-length duality, compatible inverse limits and faithful flat descent. C05b separately proves the preliminary assertion of strict prorepresentability before finiteness is imposed: finite submodules of G(E) dualize to a surjective system of finite representatives. Both assertions have later separate checks, including variance, naturality and the canonical scalar structure. The exact Artinian duality source is Stacks Lemmas 47.6.1–4, Dualizing Complexes pp. 8–9.

**Findings.** His parenthesis allowing the finiteness test on finite A-modules is valid. RD01 proves the stronger residue-field test: under the other hypotheses, finite dimension of F(k) alone suffices, by the bound length F(L) ≤ length(L) dim F(k). This is ours, not a completion attributed to his text. The handwritten grammatical “tels que” is retained against H's normalization. Notes #1–#2 and #4–#5 are accounted for; RD01 is settled.

## 94:6 — Lemme 5, scans 6–7

**What he does.** He seeks strict prorepresentability by finite modules with stationary local restrictions. His proof is organized around a smallest submodule supporting an element of the functor, with several margin insertions supplying the local-to-global argument.

**Checked.** The corrected sufficient criterion is the certified H035.8, carried as C06. Our C06b shows that the missing nonzero condition is essential, using the certified module L = sum over primes p of (1/p)Z: the element 1 in F(Z) has no smallest support although all four local hypotheses hold. A strict prorepresentation would supply such a support because its transition maps are surjective. The boxed and margin arguments, cancellation of the earlier equivalence, minimum-module letters and local restrictions are individually recorded in `SCAN_CHECKS.tsv`.

**Findings.** Condition (v) has no visible requirement f ≠ 0; with f = 0 it is vacuous and the literal sufficient criterion is false. The corrected theorem requires nonzero f in every integral quotient. The final connective is a sufficiency assertion after a deleted biconditional, and stationarity concerns the localized pro-object, without a single uniform global index. A mark near “est représentable” remains uncertain; note #3 cannot turn it into an explicit conjecture. Notes #1–#3 and #5 are decided; C06b closes the additional question raised by the omission.

## 94:8 — Remarque 5 bis

**What he does.** He compares generic representability on integral quotients with constructibility of the residue-field rank. A normal-open hypothesis is used in his proposed converse, whose proof invokes finite generation of F(N).

**Checked.** H035.10 supplies the certified counterexample and repair, carried in C07. The normal-open wording and its margin attachment, lattice notation, the equality-of-ranks passage and the actual assertion that F(N) is finite were checked on the image. The prior reading event for the normal-open phrase had checked only a transcription; this run actually checks its ink.

**Findings.** The forward implication holds; the converse fails even for the rank-one tensor functor from L = sum_p (1/p)Z. No localization L[1/n] is finite, despite the local rank and completion conditions. Finiteness of F(B), or of its restriction on a dense localization of each integral quotient, repairs the converse; the normality hypothesis is unnecessary for that repaired form. His hypothesis is the existence of a nonempty normal open, not openness of the entire normal locus. The agreement ending “égal|égale” remains a reading doubt. The domain of the rank function is written S; H's expansion to Spec A is corrected to that symbol. Notes #1, #2 and #4 are corrected accordingly; no further direction is open.

## 94:9 — Lemme 6

**What he does.** He chooses a dense open where the nilradical-graded structure sheaf and graded coherent module are locally free over the reduced scheme. He uses this to make every regular sequence of the local ring regular on the module, and therefore to obtain positive-degree Tor vanishing.

**Checked.** C08 proves generic freeness, the nilpotent-filtration lemma, the equality fM intersect J^q M = fJ^q M, the associated graded quotient formula and induction through all members of the sequence. The Koszul mapping-cone argument proves the Tor assertion in every positive degree. The second check explicitly allows the successive quotient of the reduced base to become nonreduced.

**Findings.** The live M is undefined after its earlier definition was canceled. C08b names it as the stalk of the coherent module, distinguishes lifts f_i from their graded images, and states the quotient coefficient ring. Freeness over the unchanged coefficient ring is false already for k over the DVR k[t]_(t); freeness is over the corresponding quotient ring. These are mathematical repairs to shorthand, not alternative readings. Notes #2 and #4 require all three qualifications; note #6's Koszul link is valid. The separate live insertion aussi is retained in the graded-regularity sentence, alongside the unresolved canceled word. The proof is complete.

## 94:9.2 — Corollaire 7, scans 9–10

**What he does.** He seeks a dense open where Hom into a fixed coherent module commutes with every quotient by a regular sequence. He models Hom by a two-term complex and proposes a Tor criterion for commuting its zeroth cohomology with tensor product.

**Checked.** The truth of Corollaire 7 is certified in H035.15 and carried as C09. C10 and C11 carry the certified counterexamples to the two written proof errors. RD02 independently derives the exact kernel and cokernel of the comparison from the two short exact sequences through the image of the differential; its second check recomputes both connecting maps and the flat specialization.

**Findings.** Both displayed tensor factors on scan 10 are P; the correct Hom complex uses Q. H silently repaired these factors and must be corrected back to the ink. The written Z^1 condition is genuinely insufficient; replacing it by B^1 gives the nearest sufficient repair, while RD02 gives the exact criterion with no flatness or finiteness assumptions. The final sequence index remains s|n; the expected mathematics does not decide that stroke. Plain display connectors are kept distinct from the explicit arrowheads supplied by H; their graphic status remains qualified. Notes #1, #2, #4 and #6 are corrected at these precise points. RD02 is settled.

## 94:11 — Preliminary equivalence

**What he does.** A short preliminary line relates a module for a Cohen–Macaulay ring to its quotients by systems of parameters and their indecomposable injectives. It precedes a canceled heading and the separate numbered Lemme 8.

**Checked.** The phrase “module de différentielles” is visible and is preserved. C12 states our precise dualizing-module interpretation, proves it by compatible Artinian quotient isomorphisms, passage to completion and faithfully flat descent of dualizing complexes, and proves that powers of one parameter system suffice. The second check verifies that the automorphisms used to make the isomorphisms compatible are units of the quotient ring and that these units lift.

**Findings.** A literal modern interpretation as the Kähler differential module is false: in a regular two-dimensional polynomial local ring it reduces to k², rather than the indecomposable injective k. This does not prove what his historical term meant and does not authorize changing it. The canonical-module formulation and its counterexample to the literal Kähler interpretation are fully decided; the historical wording and several canceled glyphs remain reading/interpretive qualifications. No complete separate canceled theorem can be recovered from the fragment. Notes #1–#2 are treated through this explicit reconstruction.

## 94:11.2 — Lemme 8

**What he does.** He asserts that a fundamental sheaf on a Cohen–Macaulay scheme descends to a fundamental sheaf on a regular-sequence closed subscheme. The quotient is also Cohen–Macaulay.

**Checked.** C13 defines the modern meaning of fundamental sheaf used here: coherent with dualizing stalks. It matches the finite-quotient dualizing theorem, the single nonzerodivisor theorem and the CM concentration theorem in Stacks Lemmas 47.16.2, 47.16.10 and 47.20.2 (Dualizing Complexes pp. 29–32 and 36). The Koszul shift is calculated explicitly and checked again.

**Findings.** The result holds with the stated modern definition. The calculation is stalkwise and does not presume a global normalized dualizing complex or a coefficient field. Notes #1, #2 and #5 have exact proof dependencies; no direction remains open.

## 94:11.3 — Corollaire 9

**What he does.** He specializes the preceding quotient assertion to a full system of parameters at a point. The resulting fundamental module over the Artinian quotient is the indecomposable injective.

**Checked.** C14 combines C13 with Stacks Lemma 47.16.8 (Dualizing Complexes p. 32), including the dimension-zero normalization. The omitted stalk subscript in his quotient notation is made explicit in our statement.

**Findings.** The corollary is correct. It supplies exactly the finite-length duality object needed on scan 13. Notes #1–#2 and #5 are confirmed at this passage; no direction is open.

## 94:11.4 — Corollaire 10, scans 11 and 13

**What he does.** For a locally noetherian scheme locally immersible in a regular scheme, he asserts existence of a dense CM open and a coherent module on the whole scheme with the required parameter-quotient injectives on that open. The continuation tests isomorphisms of finite modules by Hom into all those parameter quotients.

**Checked.** C15 proves the original existence statement by spreading a finite free resolution near each generic point, isolating its one nonzero Ext degree, taking disjoint generic opens and extending the resulting coherent module to all of X. Its second check addresses both the non-quasi-compact case and the absence of a global finite-dimensional ambient-ring assumption. C23 proves the Hom detection assertion by Artinian duality, Nakayama and Krull intersection; it also removes the initial surjectivity requirement and reduces the tests to powers of one parameter system.

**Findings.** Scan 13 continues scan 11 directly; the absolute-value typescript at scan 12 is inserted between them. The marginal enlargement to merely the CMU condition is false by the certified H035.21 counterexample; the excellent clause stands. The EGA IV 6.11.8 pointer is real, but the historical full-page theorem retrieval remains unverified and is not used as an independent proof. The possible deletion of “de” remains uncertain; grammar does not settle that stroke. Notes #1, #2, #4 and #5 are corrected or completed; C15 retains the coherent sheaf on all of X and does not weaken that requirement.

## 94:12 — Valeurs absolues et valuations; Proposition 1; Corollaire

**What he does.** The inserted typescript defines absolute values, relates ultrametric values to real-valued valuations, and proves the integer-value criterion by a binomial estimate. It then deduces the positive-characteristic case.

**Checked.** C17 carries the certified normalization counterexample f identically 1. C18 proves both exponential and logarithmic constructions, including zero and the trivial value group; the page's own definition includes an ordered embedding of the value group in the real numbers. C19 recomputes the exact n+1 binomial bound and its nth-root limit. C20 carries the certified correction to the prime-field argument. The handwritten additions, accents, cancellations and exponent/inequality details were read on the sheet.

**Findings.** Add f(0)=0 to obtain the intended normalized definition and field metric. The binomial proposition holds with that normalization; without it the same constant function defeats the claimed equivalence. Only nonzero prime-field elements are roots of unity; the omitted restriction matters at n=p, while the normalized corollary remains true. H has no body for this scan, and its general header claim that typed leaves lack handwriting is false here. Notes #1, #2 and #4 are corrected. This leaf is a separate absolute-value object, without a supplied handbook tag; H035 is not assigned to it merely because the sweep grouped it there.

## 94:12.2 — Equivalence paragraph; Proposition 2

**What he does.** He identifies equivalent absolute values with powers and with the same field topology, then states the classification over Q. The written proof begins a base expansion and stops before the following estimate.

**Checked.** C21 carries H035.25: the exponent in the equivalence must be strictly positive. C22 carries H035.26: the classification must include the trivial normalized value, alongside positive powers of p-adic values and powers of the ordinary value with exponent at most one. The integers greater than one, the bounds on the expansion digits and the unfinished last phrase were checked on the typescript. The whole neighbor scan 14 was inspected only for a continuation and is a different report.

**Findings.** No missing estimate or page is supplied as his. The Bourbaki chapter/paragraph pointer is recorded with its edition unverified and is not used as proof. Notes #1–#2 and #5 are corrected at the missing positivity and trivial case. The mathematical classification is decided by the certified input; the historical reference limitation does not leave it open.

## 94:13 — Corollaire 11, canceled draft

**What he does.** In a fully canceled draft, he combines regular-sequence base-change comparisons for two Hom functors with an isomorphism after evaluation at the fundamental module. The intended conclusion is that the original map of finite modules is an isomorphism.

**Checked.** C24 uses only the clearly rewritten final functors Hom(R,M) and Hom(R′,M). Its naturality square reduces the claim to C23, and the separate check verifies the direction of each Hom map and the role of the base-change assumptions. The canceled earlier Hom arguments and individual deleted glyphs remain separately inventoried. The visible functor letter is Phi throughout the final formulation; H's fraktur-L transcription is corrected at the definitions and each condition.

**Findings.** The final recoverable formulation is true, although the draft is canceled; cancellation is not a counterexample. Our stronger statement again needs only the cofinal parameter powers and no initial surjectivity. The margin asks for another exposition and is not an explicit open theorem. Notes #1–#3, #5–#6 are decided without inferring conventions from the unreadable earlier arguments. No research direction remains open.


## Delayed comparison with our research results

After the foundational check was complete, the supplied results folder was opened as logged. Its register contains zero data rows. Consequently there are no evidenced research-result links or corrected-reading quotations to add; CONSEQUENCES.tsv retains only its required header. This reports the supplied range-specific register, not a search result about all research outside it.
