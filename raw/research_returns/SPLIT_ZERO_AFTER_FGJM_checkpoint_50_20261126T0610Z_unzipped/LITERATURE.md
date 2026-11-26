# Literature search and reading log

## 24 November 2026, initial searches

- Exact title “The case for inverse semirings”, with authors and citation-forward keywords: located arXiv:2411.12318, submitted 19 November 2024. Opened the arXiv landing page. The attached LaTeX provides the full source. No exhaustive forward-citation coverage has yet been established.
- Exact title “Clifford semigroups and the monoidal Grothendieck construction”: located arXiv:2607.12944 and Luca Mesiti’s author page. The search metadata identifies the July 2026 preprint. The direct arXiv page failed to fetch once; the attached source remains available.
- Alpöge, remark, recent official-site search: opened https://alpo.ge/remark.pdf (4 pages). It announces RH and generalized RH with a Lean archive. The theorem A requested as input is used as a cited external input; this run does not claim to have rebuilt that archive.
- https://hexagonmath.org/2611.00789: direct opening failed. Homepage opened successfully; it explicitly says deposits are not peer review. A neighbouring arithmetic-complexity deposit is being inspected by the circuit worker.
- Requested FORMAT.md at GitHub, both blob/main and raw/main routes: web fetch returned DisabledError. Format conformance cannot yet be certified; a documented approximation using permanent tags, check events, source citations, and version manifests is being prepared pending access.
- “Ramachandran zeta functions Witt ring motivic measures 2015 arxiv”: located arXiv:1407.1813 and the 2015 journal article, Bulletin des Sciences Mathématiques 139(6), 599–627. Full text still to be read.
- “Davenport Heilbronn 1936 zeros Hurwitz zeta function rational transcendental alpha”: secondary leads give the classical rational/transcendental parameter restriction. The original paper is required before any theorem is attributed to it.
- “Levinson 1975 a points zeta function 1/2”: located the original PNAS article, 72(4), 1322–1324, doi:10.1073/pnas.72.4.1322, in PubMed Central.
- “Deitmar schemes over F1 zeta function polynomial counting function finite type”: located Deitmar’s Remarks on zeta functions and K-theory over F1 and arXiv:1306.3681. Full text still to be read.

Searches establish discovery and locators only. They do not establish novelty, correctness, or exhaustive coverage. Sources are cited and not copied into the return archive.




## Further primary-source inspections before the first checkpoint

- Ramachandran, arXiv:1407.1813v2, 23 pages: opened the full PDF; used Witt definitions in §1 and Theorem 2.1 and Lemma 2.3 on pp. 9–10. The global Witt question later in the paper does not justify a map on the whole Witt ring from an injective map of a smaller sign-Tate semiring.
- Deitmar, arXiv:math/0605429v3, 6 pages: opened the full PDF and visually checked the first page. The 2006 convention uses positive powers in its F1-zeta limit; the commonly used reciprocal convention must be distinguished. Finite type is essential to the polynomial-counting statement.
- Mulmuley, arXiv:0709.0751v2, 71 pages: read Conjecture 3.4 (p.24), the displayed rank-three basis (p.28), the claimed verification (p.29), and Figures 1–2 (pp.30–31). Independently factored the displayed Figure 2 coefficient and checked its nonunimodal positive factor. Equation (17) repeats a basis symbol as printed, so the new matrix model is explicitly defined rather than silently repairing that typography.
- Levinson, PNAS72(4),1322–1324: original abstract and journal metadata opened; PDF endpoint returned a challenge. No uninspected detailed zero-distribution rate is attributed to it.
- Davenport and Heilbronn, JLMS11 (1936),181–185 and307–312: original journal metadata located, direct PDFs failed. The manuscript does not transfer the classical parameter statement to the shifted interval 1<a<2 without proof.










































































































































<!-- MERGED FRAGMENTS -->


## paper1_exchange_literature

# Exact ordinary exchange sources and convention comparison

Recorded 2026-11-25T04:21:15.154596+00:00; GPT-6 Astra Pro, effort setting not exposed. This is literature/source review, not an independent mathematical-check event.

## Ordinary primary inputs actually read

Nielsen, P. P. (2006). *The exchange property for modules and rings* [Doctoral dissertation, University of California, Berkeley]. Author URL: https://mathdept.byu.edu/~pace/PaceThesis_web.pdf . Local primary bytes outside the deliverable: `scratch_analysis/idempotent_lifting_primary/Nielsen_2006_Thesis.pdf`, 364694 bytes, SHA256 `e753c89125d6679e2652a64c3e96035e1e7da6b0ce47ae41b2bc78f8b17c8e90`.

Foundation read the complete proofs of Lemmas 2.3–2.4 on printed pp.2–3/PDF pp.9–10 and Proposition 2.7 on printed pp.4–6/PDF pp.11–13, together with Corollary 2.8 and Definition 2.9 on printed p.6, at04:05:23 UTC. Title and degree metadata were checked04:07:01. These establish fixed-cardinality exchange for finite sums and summands, and the module–endomorphism-ring criterion. The application to a finite complete orthogonal family uses right modules p_i B and End_B(p_i B)=p_i B p_i, with maps given by left multiplication. No infinite-sum assertion is used. Root separately read the same full arguments; its own evidence is in `paper1_root_exchange_sources_literature.md`.

Nicholson, W. K. (1977). Lifting idempotents and exchange rings. *Transactions of the American Mathematical Society, 229*, 269–278. https://doi.org/10.1090/S0002-9947-1977-0439876-2 . Primary full text uploaded by the author: https://www.researchgate.net/publication/238873439_Lifting_Idempotents_and_Exchange_Rings . The page identifies W. K. Nicholson as uploader, August8,2016. Foundation read all four implications of Proposition1.1 and the full Corollary1.3 argument on printed p.270 at04:09–04:10 UTC. Exact source retrieval ref at that stage: turn111087807view1. The needed calculation is p=rb and 1-p=s(1-b), hence p-b=(r-s)(b-b²); it proves lifting modulo any left ideal, and therefore every two-sided ideal. The manuscript reproduces only the short mathematical calculation, with attribution. AMS direct access was blocked and the author-page download link returned404; no local Nicholson PDF hash is claimed. Root subsequently read the same complete primary argument and recorded its source check04:14:56.935370.

The ordinary exchange equation, ideal lifting and finite-Peirce closure are established ring theory. Their application to the unital coefficient enlargement, its exact image ideal, and its annihilating transition kernel is proved in the manuscript. Scalar lifting alone is not used as a substitute for exchange. The previously verified Diesl–Dittmer–Nielsen matrix-lifting boundary remains separately recorded in `paper1_root_lifting_boundary_literature.md`.

## Bounded neighboring-source search

Between04:18:32and04:21:15UTC, system2 searches used `inverse semiring exchange rings projective semimodules idempotent lifting coefficient` and `"semilattice of rings" "exchange" idempotent lifting`. System1 then verified coverage with `"inverse semiring" "exchange" projective quotient` and `"Clean semiring" exchange semiring strongly clean definition`. These are bounded searches, not evidence of absence or priority. The existing Hexagon foundation paper is already credited elsewhere and is not independent priority evidence for this run.

A directly relevant terminology neighbor was located and opened: Das, D., and Kar, S. (2022). *Strongly clean semiring* (Version1) [Preprint]. Research Square. https://doi.org/10.21203/rs.3.rs-1751073/v1 . Primary PDF: https://assets-eu.researchsquare.com/files/rs-1751073/v1_covered.pdf?c=1655236994 . The title page and exact definitions on printed pp.3–5, including absorbing complements on p.4, and Definition3.11 on printed p.10 were read in full. Definition3.11 imposes a global absorbing-complement condition on every multiplicative idempotent and an equation inside the entire semiring. This differs in formulation from requiring the ordinary rings F(e) to be exchange. No equivalence or implication between the two hypotheses is claimed or used. The adjacent Theorem3.12 proof was visible and read, but was not independently checked or imported as a theorem premise. The full preprint was not reviewed line by line.

The Springer primary record for Kar and Das, *Clean semiring*, confirms publication in *Beiträge zur Algebra und Geometrie,64*,197–207(2023), online16February2022, DOI10.1007/s13366-022-00628-0. Only its abstract, metadata and references were accessible; no full-proof claim is made. A later published *Strongly Clean Semiring* record, DOI10.1007/s40010-024-00875-x, was located but not used for exact numbering. The manuscript explicitly cites the read2022version and its locators.

## Consequence for wording and scope

SZ1-110 retains exact finite matrix supports, including nonunital additive fibers and nonzero F(0), through arbitrary compatible coefficient quotients when all upper coefficient rings are exchange. SZ1-111 gives surjective V/K0 maps for those quotients and isomorphisms for the compatible Jacobson quotient using the earlier unconditional isomorphism-detection theorem. Neither result supplies local-idempotent multiplicity uniqueness outside the semiperfect hypothesis, a complete unrestricted projective classification, or an automatic research-review counter reset. No novelty claim is made.


## Primary-byte follow-up supplied by root

At04:26:53UTC root reported a successful primary download of the exact Das–Kar version read above: `scratch_analysis/idempotent_lifting_primary/Das_Kar_Strongly_clean_semiring_v1.pdf`, 257752bytes,22PDFpages, SHA256 `a62bdcb94249dd7b007f2d4c0b2388126c97498a8548e9a51feee597cbb17f29`. Root independently read the full absorbing-complement definitions on printedp4/PDFp5 and Definition3.11 on printedp10/PDFp11. This supplements the earlier web primary access; it does not retroactively change either worker's proof-check scope. The external source PDF remains outside the deliverable.


## paper1_literature

# Paper 1 literature search log

All searches and source readings below took place on **24 November 2026 UTC**, beginning at approximately 13:48; subsequent entries give their later times. Source URLs are public. No fetched paper or copied source text is included in the deliverable.

## Queries and outcomes

1. Queries: `"The case for inverse semirings" citations modules projective`; `"Clifford semigroups and the monoidal Grothendieck construction"`; `"projective commutative inverse monoids" semilattice`. Found the FGJM arXiv record, CFMM arXiv record, CFMM authors' publication pages, and the 2026 category-theory conference description. No complete forward-citation list was returned.
2. Queries: `"K_0" "Boolean semifield" projective`; `"projective" "commutative inverse" monoids`; `Horn Kimura category semilattices 1971 projective distributive theorem`; `Lorscheid blueprints semiring schemes quasi coherent modules`. Found Katsov–Nam–Zumbrägel (arXiv:1711.05163), the 1980 Bulman-Fleming–McDowell paper, Horn–Kimura references, and Lorscheid's 2026 comparison paper.
3. Queries: `"Flatness and projectivity in commutative regular semigroups"`; `"On congruence-semisimple semirings" "arxiv"`; `"projective" "semilattices of groups" finite`; `site:hexagonmath.org "inverse semiring"`. Found the author-uploaded full text of Bulman-Fleming–McDowell, Katsov–Nam–Zumbrägel's arXiv/journal metadata, and related regular-monoid K-theory literature. The Hexagon query produced no relevant indexed hit; that is not evidence of absence.
4. Queries: `Bulman Fleming McDowell 1980 flatness projectivity commutative regular semigroups doi`; `"Horn" "Kimura" "The category of semilattices" doi`; `"projective" "inverse monoids" "semimodules" ring`; `"Grothendieck" "Boolean" "connected" semiring K0`. Identified DOI 10.1007/BF02572519 and related projective-semimodule literature. No exact general-R classification was established from these results.
5. Queries: `"The category of semilattices" "pdf"`; `"Horn" "Kimura" "5.3" semilattices`; `"The category of semilattices" "10.1007"`. Identified DOI 10.1007/BF02944952; primary later papers explicitly cite Theorem 5.3 for the projectivity characterization. Original full text was not retrieved in this search.

## Opened sources and exact uses

- Faul, P. F., Goswami, A., Joubert, G., & Manuell, G. (2024), *The case for inverse semirings*, arXiv:2411.12318. https://arxiv.org/abs/2411.12318. The arXiv record was opened; attached source was read at Construction 3.5, Definition 3.6, §3.1, Propositions 4.13, 5.1–5.2 and 6.1. Its zero adjunction, inverse module structure, reflections and free-polynomial results are known and credited. Attached TeX bytes, rather than a fetched copy, are the content source.
- Caviglia, E., Faul, P. F., Manuell, G., & Mesiti, L. (2026), *Clifford semigroups and the monoidal Grothendieck construction*, arXiv:2607.12944v2. https://arxiv.org/abs/2607.12944. The attached source §§4–5 and §8 was read. Theorem 8.5 and Remark 8.7 are credited. The arXiv open returned `DisabledError`, while search and the author page https://lucamesiti.github.io/publications/2026-07-15-MonoidalGrothClifford/ exposed the metadata. No module classification occurs in the read sections.
- Bulman-Fleming, S., & McDowell, K. (1980), *Flatness and projectivity in commutative regular semigroups*, **Semigroup Forum 19**, 247–259. https://doi.org/10.1007/BF02572519. Springer article and PDF URLs were unavailable to the retrieval tool. The complete author-uploaded primary paper was opened at https://www.researchgate.net/profile/Sydney-Bulman-Fleming/publication/225145688_Flatness_and_projectivity_in_commutative_regular_semigroups/links/570cffe508ae3199889b4683/Flatness-and-projectivity-in-commutative-regular-semigroups.pdf. Pages 254–258 (Lemmas 3.1–3.2, Theorem 3.3, Corollary 3.4) were used. This is a genuine predecessor for the integral case, with a different identity convention. Its theorem involves projective semilattice, finite free component groups, surjectivity of the component product, split transition maps, and a compatible-pair condition. The ring-coefficient labelled-poset theorem was proved independently before this reading.
- Katsov, Y., Nam, T. G., & Zumbrägel, J. (2018), *On congruence-semisimple semirings and the K0-group characterization of ultramatricial algebras over semifields*, **Journal of Algebra 508**, 157–195. https://doi.org/10.1016/j.jalgebra.2018.04.024; preprint https://arxiv.org/pdf/1711.05163. Opened the full preprint. Used Definition 4.1 (preprint p.7), §§5–6, Remark 6.6(3) and Proposition 6.7 (preprint pp.21–22): ordinary projective versus strongly projective, definitions of V and K0, and a countably generated free subgroup of K0(B). This prevents confusing K0 with SK0.
- Lorscheid, O. (2026), *Two comparison theorems for semiring schemes*, arXiv:2603.28616. https://arxiv.org/html/2603.28616v1. Opened §1.1 and §1.4.1 and the introductory statements of the comparison theorems. These give the precise prime-spectrum/semiringed-space framework. They do not supply the module-sheaf equivalence proved in Paper 1.
- Horn, A., & Kimura, N. (1971), *The category of semilattices*, **Algebra Universalis 1**, 26–38. https://doi.org/10.1007/BF02944952. Theorem 5.3's locator was corroborated by the primary Bulman-Fleming–McDowell paper and by later primary articles; the original theorem text was not opened. The needed finite zero-preserving form is proved in full in Paper 1, Lemma 5.1.

## Forward citations and limits

The Google Scholar link from the opened FGJM arXiv page was attempted and returned HTTP 429 (Too Many Requests). Therefore the instruction to follow every citing paper is **not certified complete**. CFMM is a verified citing development, but the search cannot establish it is the only one. The general ring-coefficient classification, full labelled-poset K0 description, and stated QC-sheaf equivalence have no novelty designation in the paper. Their literature status remains unresolved beyond the identified known special cases. No claim corrects a published mathematical statement; the one-idempotent error is in an unpublished project note.

## Source-byte hashes

Attached source SHA-256 values are in `paper1_source_hashes.tsv`. The web retrieval tool exposes rendered/extracted content rather than downloadable bytes; no SHA-256 is fabricated for the fetched primary PDFs. If exact fetched-byte provenance is required for deposit, obtain those PDFs through an authorized byte-transfer route and add their hashes before marking the literature audit complete.

## Repeated-adjunction searches, approximately 14:07–14:14 UTC

Queries: `"projective semimodules" "finite chain"`; `"projective" "distributive lattice" semiring semimodule chain`; `"projective modules" "finite distributive" "semiring"`; `"Ultramatricial algebras over commutative chain semirings" pdf arxiv`; `"projective semimodule" "chain" "poset"`; `"projective semimodules" "chain" "posets"`. The last two searches did not locate the exact coloured-poset condition. This is not evidence of novelty.

Opened the official journal page of Di Nola, A., Lenzi, G., & Nam, T. G. (2020), *Ultramatricial algebras over commutative chain semirings and application to MV-algebras*, **Forum Mathematicum 32**(2), 287–305, https://doi.org/10.1515/forum-2019-0056, at https://www.degruyterbrill.com/document/doi/10.1515/forum-2019-0056/html. The abstract expressly classifies **strongly** projective semimodules over finite products of matrix semirings over commutative chain semirings, and uses ordered SK0. Only the abstract and reference list were accessible; no theorem number is assigned without the full text. This is a relevant predecessor for the strong-projective consequence, not verified evidence for the ordinary-projective coloured-poset classification. An institutional author publication page corroborates the bibliographic details.

A search also found Macpherson's *Projective modules over polyhedral semirings*, DOI 10.1016/j.jalgebra.2018.09.041, with a finite Boolean-poset theorem. Its full text has not yet been checked, and no statement from it is used as a premise.


## Two-idempotent projective classification, approximately 14:36–14:59 UTC

Queries: `site:stacks.math.columbia.edu projective modules fibre product patching surjective`; `site:stacks.math.columbia.edu idempotents lift locally nilpotent ideal projectives`; `"inverse semirings" "projective" "nilpotent"`; `"inverse semiring" projective bimodule`; `"semiring" "projective" "pullback" Milnor`; `"semiring" "projective" "square-zero"`. Primary sources found and opened:

- Stacks Project, Lemma 15.6.9, Tag 0D2G, https://stacks.math.columbia.edu/tag/0D2G: finite projective patching over a ring fiber product with a surjective leg. The theorem and proof were opened. This supplies a comparison, not an unproved extension to semirings.
- Stacks Project, Lemma 10.77.6, Tag 0D47, https://stacks.math.columbia.edu/tag/0D47: lifting finite projective modules over locally nilpotent ideals. The statement was opened; the semiring argument instead works directly in fixed-support matrix rings.
- Stacks Project, Lemma 10.32.6, Tag 00J9, https://stacks.math.columbia.edu/tag/00J9: idempotent lifting for commutative rings. No uniqueness assertion from this lemma is transferred to noncommutative matrix rings.
- Stacks Project, Lemma 10.32.7, Tag 05BU, https://stacks.math.columbia.edu/tag/05BU: a polynomial corrects an element with nilpotent idempotency defect in a possibly noncommutative algebra. The statement and proof were opened. Paper 1 proves and uses the square-zero formula inside the identified matrix group fiber.

At approximately 14:59 UTC, stronger-source searches were made for `"inverse semiring" projective site:eccc.weizmann.ac.il`, `"inverse semiring" projective site:hexagonmath.org`, `"semiring" "two idempotents" projective`, and `"inverse semirings" "projective" "bimodule"`. No exact match for the present gluing-triple classification was retrieved. ECCC returned an unrelated linear-operator complexity paper; the Hexagon query returned no pertinent indexed paper. These searches do not establish absence or novelty. The new classification remains without a priority claim.

The searches also returned Macpherson's *Projective modules over polyhedral semirings*, DOI 10.1016/j.jalgebra.2018.09.041, whose official article description concerns projectives over idempotent semirings freely generated by monoids. This is relevant to the unresolved arbitrary-Q support problem; the exact §4.2–4.3 statements have not yet been read and are not used as premises. Search results for derivations in inverse semirings involve other axioms and reverse/Jordan derivations; none was used to infer the normalized derivation theorem proved here.

All Stacks sources were read through the web retrieval view. Exact fetched-byte hashes are not available from that view and are not fabricated. No third-party text is copied into the returned workbench.

## Unit-fiber adjunction and Hurwitz endpoint, 24 November 2026

The unit-fiber adjunction was derived independently before checking the attached FGJM text. Definition3.6 and §3.1 give zero adjunction left adjoint to forgetting the zero condition; Proposition4.7 identifies the ring-of-scalars fiber G(0_1); Remark4.14 gives its right adjunction to the ring inclusion in the zeroless category. Their composite is exactly Hom(R_0,T)=Hom(R,U_1(T)). This is an already implicit composite of stated adjunctions, not a novelty claim. The independent derivation and exact attached-source line ranges are in `checks/paper1_unit_fiber_adjunction_independent.md`.

At approximately16:06UTC, the official NIST Digital Library of Mathematical Functions was opened at https://dlmf.nist.gov/25.11, including its definition/continuation paragraph and equations25.11.14 and25.11.18. The first gives zeta(-m,a)=−B_(m+1)(a)/(m+1), including m=0; the second gives zeta'(0,a)=logGamma(a)−log(2pi)/2 for a>0. Applying them at a=1 and1+t proves the corrected source endpoint. The bibliography fragment cites NIST directly; the analytical source's B1(0) substitution is explicitly refuted. Web retrieval did not expose fetched-byte hashes, and none are fabricated.

## Macpherson full-text continuation, approximately16:16UTC

Following the root's discovery, this worker independently opened the primary arXiv PDF https://arxiv.org/pdf/1507.07213. It is27pages and its title page dates the text14July2018. Theorem3.9, printedpp8–9 (also summarizedpp1–2), identifies projective Boolean modules with modules freely generated by lower-finite posets. Corollary4.13, printedpp15–16, classifies finite projective B[A]-modules for an F1-domain A by unique primitive decompositions, a free primitive A-module, nondegenerate order, and finite-quiver presentation. Both statements and the displayed proofs were read in the web view. The main manuscript now credits the Boolean result and names this substantial special case in its remaining general-(Q,F) question. No extension of that theorem to arbitrary coefficient-group diagrams F is assumed. The root records downloaded-byte hashes; this worker's web view does not provide a separate hash.

## Finite distributive support extension: targeted follow-up, 24 November2026,16:50–17:04UTC

Search systems2 and1 were used for the exact combinations “finite distributive lattice semiring projective semimodules classification poset”, “projective semimodules colored poset lattice”, and “projective semimodules admissible ideals distributive”. No exact G_L(R) admissible-ideal classification was located. This is limited negative search evidence, not a novelty conclusion. Macpherson’s published DOI10.1016/j.jalgebra.2018.09.041 and the already read preprint were repeatedly recovered. Ordinary projective distributive-lattice results use different morphisms and are not silently substituted for semimodule projectivity.

The primary preprint Il’in, Katsov and Nam, arXiv:1509.02997, “Toward Homological Structure Theory of Semimodules: On Semirings All of Whose Cyclic Semimodules Are Projective,” was opened (32pages). Its introduction/preliminaries, including printedp4 definition of projective as a free retract, were inspected; no full new theorem audit is claimed. A Taylor&Francis page for DOI10.1080/03081087.2020.1760192 returned403.

The official TAC abstract for Susan Niefield (2016), “Projectivity, continuity and adjointness: quantales, Q-posets and Q-modules,” Theory and Applications of Categories31(30),839–851, was opened at https://tac.mta.ca/tac/volumes/31/30/31-30abs.html. It states projectivity criteria via distributivity, continuity and adjointness in quantale modules. The linked official PDF timed out, and an EMIS mirror was inaccessible. Exact theorem hypotheses/proofs were therefore not read in this worker’s web session. This is a relevant support-only predecessor to investigate, not evidence that the coefficient-group classification has been settled elsewhere. Fetched-byte hashes were not exposed by the web views.

## General action-ringoid reduction, 24 November 2026, approximately 18:22–18:30 UTC

Queries were run first with search system 2 and then system 1: `"inverse semiring" "projective" modules ringoid`; `"rings with several objects" Mitchell modules projective additive functors`; `Barry Mitchell Rings with several objects 1972 Advances Mathematics 8 1 161 doi`; `"inverse semirings" "projective" "support" modules`; `"semilattice of groups" "projective" "semimodules"`; `"Facets of module theory over semirings" arxiv authors`; and `"Rings with several objects" Mitchell pdf 1972`. No exact action-category/support-section-cokernel criterion was located in this bounded search. This is not a novelty or priority conclusion.

Primary content read:

- Borger, J., & Jun, J. (2025), *Facets of module theory over semirings*, arXiv:2405.18645v3, June 30, 2025, 38 pages; https://arxiv.org/pdf/2405.18645. Definition 7.1 on printed page 18 specifies projectivity by preservation of surjections/equivalently free retracts. Proposition 7.2 and its proof were read there; Proposition 8.5 on page 22 gives the finite-projective/dualizable comparison. This reading provides general semiring-module context, not the new inverse-support criterion. Publisher metadata confirms *Advances in Mathematics*, 479, 110431, DOI10.1016/j.aim.2025.110431. Publisher full-text access returned HTTP403.
- Murfet, D. (2006), *Rings with Several Objects*, October5 author notes, 27 pages; https://therisingsea.org/notes/RingsWithSeveralObjects.pdf. Section1 Definition1, printed page1, uses covariant additive functors for left modules. Pages2–4 describe pointwise exactness and Proposition3 proves that representables are small projective generators. These definitions and the stated proposition/proof were read. This is direct author-note evidence for the formalism used, not evidence that the inverse-semiring criterion appears there.
- Mitchell, B. (1972), *Rings with several objects*, *Advances in Mathematics*,8(1),1–161, DOI10.1016/0001-8708(72)90002-3. Bibliographic metadata was verified. Attempts to open the publisher/DOI full text failed; no exact Mitchell theorem is claimed to have been read in this search. The citation credits the classical formalism, with Murfet's accessible author notes supplying the actually read conventions.

The manuscript gives complete proofs of fixed-support equivalence, finite generation, the criterion, and the obstruction. The independent root derivation was saved before proof comparison. Literature-search activity is recorded in SOURCE_EVENTS, not counted as a mathematical check.

## Post-checkpoint07 inverse-semimodule context, 24 November2026, approximately18:55–19:05UTC

Primary sources and exact reading scope are recorded in `checks/paper1_inverse_semimodule_literature_comparison.md`. Dokuchaev–Johari–Vilca-Rodríguez's published PDF was read directly; the categorical equivalence is Proposition3.12, not Example3.11. Sen–Bhuniya–Maity's publisher abstract was retrieved through search, while direct full text was403. The official indexed pages280–281 of Sen–Maity–Swomin's 2021 von Neumann regular semimodule paper give additional convention evidence; direct PDF requests were502. No source claim has been promoted from abstract to theorem-level comparison. The precise F_0 field comparison was checked after reading the definitions and is a targeted check.

## Finite-group projectives: primary context, approximately19:08–19:15UTC

After the finite-group author proof and the root's separate statement-only proof were durable and compared, search system2 was used for `"Boolean group semiring" projective modules posets`, `"projective" "semilattice" "group action" modules`, `"semiring" "projective" "stabilizer" group`, and `"rings with several objects" "transporter" projective modules`. Search system1 followed with `"projective modules" "Boolean" "group" semiring poset`, `"finite EI" "projective" modules automorphism groups`, and `"Representation theory over semifields" arxiv`. No exact R_0[Γ] classification by stabilizer-labelled Γ-posets was located in this bounded search. This is not an assertion of novelty or priority.

Primary reading and bibliographic verification:

- Macpherson, A. W. (2018). *Projective modules over polyhedral semirings*. July14 preprint, https://arxiv.org/pdf/1507.07213. Definition4.9, printedp14, defines the F1-domain monoid-pair hypothesis with a sharp saturated positive submonoid and group localization. This excludes nontrivial multiplicative torsion. Consequently the already read Corollary4.13 is not silently applied to a nontrivial finite group. No new theorem from this reading is used as a premise.
- Jun, J., Mincheva, K., & Tolliver, J. (2026). Representation theory over semifields. *Journal of Algebra,706*,243–265. https://doi.org/10.1016/j.jalgebra.2026.05.022. Publisher metadata was verified. The full text actually read was arXiv:2411.19883v3, datedFebruary14,2025,16pages, https://arxiv.org/pdf/2411.19883. Its Section1.1 and Definition3.1 concern actions on free underlying semifield modules. Section4, Corollary4.9 and Lemma4.11, printedp15, give Boolean group-module embeddings and the antichain property of group orbits. The manuscript explicitly identifies this numbering as arXivversion3. The published version's theorem numbering was not independently asserted.
- Fiore, T. M., Lück, W., & Sauer, R. (2011). Euler characteristics of categories and homotopy colimits. *Documenta Mathematica,16*,301–354. https://doi.org/10.4171/DM/333. The primary publisher page https://ems.press/journals/dm/articles/8965268 and54-page published PDF https://ems.press/content/serial-article-files/26117?nt=1 were opened. Printedpp306–307 define the splitting functor by quotienting images of nonisomorphisms, its extension functor, and the projective EI-category splitting statement in Theorem1.5. Their text credits Lück's book Theorem10.34; the book itself was not read in this session. This supplies classical category-module context for stabilizer rings and quotient labels. The manuscript gives a direct proof and separately checks noncommutative coefficient rings rather than assuming that extension of the cited formulation.

Web retrieval exposed no fetched-byte hashes for these views; none are fabricated. These searches and comparisons are SOURCE_EVENTS, not independent mathematical checks of the new classification. The finite-group statement and author proof preceded these new neighboring-source readings.


## Canonical ideal and public foundation follow-up, 24 November2026, approximately19:58–20:32UTC

The root worker searched both web systems and retrieved three primary PDFs. This foundation worker subsequently read the local primary bytes at the scopes stated below. Root retrieval records and files remain outside the returned workbench in scratch_analysis/literature_followup_1958; only our descriptions, citations and hashes are returned. These are literature/source events, not additional mathematical checks.

- Herbera, D., & Příhoda, P. (2014). *Reconstructing projective modules from its trace ideal*. Journal of Algebra,416,25–57. https://doi.org/10.1016/j.jalgebra.2014.06.010. The content read was arXiv:1309.5021v1, https://arxiv.org/pdf/1309.5021. This worker read the title/abstract onp1 and the trace-ideal discussion onp2, including the finite-idempotent-entry description. The root separately verified metadata and that passage. The matrix consequence of the canonical support ideal is an application of this ordinary trace-ideal argument; it has no novelty designation. PDF SHA256:71fcb80d4ee5b077f6bc64a33f83f698b6d4a8e57be69cbfec210250318f0853.
- Cortés-Izurdiaga, M., & Torrecillas, B. (2013). *Projective and flat objects over rooted rings with several objects*. Bulletin Mathématique de la Société des Sciences Mathématiques de Roumanie,56(104)(3),315–330. Primary PDF:https://ssmr.ro/bulletin/pdf/56-3/articol_5.pdf. This worker read the title page and the opening statement of Theorem1 in the printedpp320–322 region; an extraction display ended before its full proof, so no full-proof reading is credited to this worker. The root read Theorem1 and Remark3/Example1, printedp322. The manuscript's comparison uses the stated left-rooted hypothesis and the root's precise cycle comparison. No claim transfers that theorem to arbitrary action categories with scalar loops. PDF SHA256:8d3572f5d46434c3897d897610dafe3463704ec4850ad941963a3d3099599460.
- *Spectrum, semimodules and projectives of the inverse semiring R0 of Faul, Goswami, Joubert and Manuell*. (2026, November24). Hexagon2611.00993v1. https://hexagonmath.org/2611.00993v1. Primary PDF:https://hexagonmath.org/pdf/2611.00993v1. Both search engines now indexed this public version; direct web-opener access failed, but the root retrieved HTML/PDF with HTTP200 at19:58UTC. This worker read the public title/abstract page directly and the complete operator comparison record after it was saved. The operator worker read all10public pages and compared them against attached h22_note_v3.tex; exact result locators and reading chronology are in checks/paper3_hexagon_foundation_comparison.md. The only mathematical change is the ordinary-module projectivity correction in Section1.3(p3) and Remark5.4(p8), already SZ1-014. Other numbered statements/proofs agree. The public note is acknowledged as a direct foundation antecedent in Paper1. PDF SHA256:95eb60b92984ec13da5b9388afa7148ac81aa65ca7128350a4d139331121be6d. HTML SHA256:f0fbdef24ce6f2062eb5a16ca1082a1039459f5c5733c760d5e9a6f8808dcddb.

The public PDF author line and metadata author field are empty; the landing page identifies user Alderliefste as contributor, not author. The bibliography therefore begins with the title. No inference is made that this run caused the public deposit. Earlier log statements that no pertinent Hexagon result was retrieved or that the projectivity error existed only in an unpublished note describe the earlier search/read state; this later discovery supersedes that current-status wording. The public version contains the correction, while the attachment retains the error.

All exact primary-byte hashes above were recomputed from the downloaded files. No external source PDF or copied article text has been inserted into the deliverable. The new canonical support ideal itself has no priority claim. General action categories need not be left rooted, and identifying their finite projectives is still part of the residual problem.

## Finite inverse-semiring classification: ordinary primary context, approximately21:01–21:07UTC

After the author and root statement-only proofs were saved and compared, this worker searched system2 for `Henning Krause Krull Schmidt categories and projective covers krs.pdf`. It returned the author-hosted PDF, arXiv:1410.2822 and publisher metadata. This worker opened https://www.math.uni-bielefeld.de/~hkrause/krs.pdf (12pages, author version10October2014), then read the displayed definitions and full arguments around Lemmas3.4–3.6 (printedpp6–7), Proposition4.1 (pp8–9) and Theorem4.2 (p9). These supply the classical projective-cover, semiperfect-ring and uniqueness context. The published reference is Krause,H.(2015), *Krull–Schmidt categories and projective covers*, Expositiones Mathematicae,33(4),535–549, https://doi.org/10.1016/j.exmath.2015.10.001. Operator's independently downloaded PDF hash is00f58b3b618864545f16fc2ecb5288670b7498d0fbd617cf591ff68e2c1c038d; exact retrieval records are in checks/paper3_finite_ring_primary_sources.md and its JSON companion.

The finite inverse-semiring theorem proves its action-category finiteness before using ordinary ring theory, and includes a complete direct finite-ring cover proof. No new ordinary projective-cover or Krull–Schmidt theorem is claimed. The root supplied the original normalization/projective-cover direction; the foundation proof and root's separate derivation both preceded this source comparison. Root and operator additionally read Lam's Bass survey; this worker has read their records but has not independently opened Lam here, and does not claim that reading. Literature/source events carry no additional independent-check credit.

### Exact-form follow-up after the finite theorem, approximately21:08UTC

System2 searches were `"finite inverse semiring" projective semimodules`, `"inverse semiring" "projective" finite classification`, and `"finite semirings" "projective" "simple modules"`. System1 followed with `"inverse semiring" "projective" "finite"` and `"semimodules" "greatest" "projective" idempotent`. The searches recovered the public R_0 foundation note, Macpherson's polyhedral-support classification, Borger–Jun's general module theory, and papers about FP-injectivity or semiring identities of multiplicative inverse semigroups. No exact arbitrary finite inverse-semiring classification by a canonical action-category ideal and allowed simple-cover multiplicities was located. This is bounded negative search evidence, not a novelty or priority claim. No theorem from the merely returned neighboring papers was used as a new premise; previously read sources retain their recorded scope. The search was performed before checkpoint10, and this metadata paragraph was saved after its seal to preserve the requested file freeze.

## Action-category coefficient colimits and residuation, approximately21:18–21:21UTC

After the author colimit proof was saved, system2 searches used `"inverse semiring" semimodule "colimit"`, `"inverse semiring" "action category"`, and `"semilattice of groups" modules "direct limit" projective`. System1 followed with `"inverse semiring" modules "category" "colimit"` and `"idempotent semiring" "residual" "projective" modules`. No exact coefficient-colimit action-category identification was located. This is limited negative evidence, not a novelty claim. Returned general semimodule-colimit and nonstable-K-theory papers were not silently treated as sources for this particular theorem.

For the classical residual operation, a further system2 search used `Cohen Gaubert Quadrat Duality separation theorems idempotent semimodules 2004 pdf residuation`. The publisher metadata and primary arXiv PDF were opened. Reference: Cohen,G., Gaubert,S., & Quadrat,J.-P.(2004). *Duality and separation theorems in idempotent semimodules*. Linear Algebra and its Applications,379,395–422. https://doi.org/10.1016/j.laa.2003.08.010. The content read was arXiv:math/0212294v2, https://arxiv.org/pdf/math/0212294,24pages,29September2003. Sections2.1–2.2, printedpp4–6, define residuated maps and scalar-action residuals, particularly equations(2)–(3) and(13)–(14). The source uses right semimodules there; our left-action formula is the side-reversed convention, which is kept explicit. No completeness assumption is transferred to arbitrary Q: our general theorem uses directed coefficient colimits; finiteQ provides actual maxima. This credits the ordinary residual operation, not the new inverse-semiring coefficient formula. The web view did not expose fetched bytes, so no hash is fabricated.


## Finite-presentation decision obstruction,21:41–21:48UTC

The exact queries, accessible primary text, convention audit, failed screenshot/direct-download attempts and locators are recorded in checks/paper1_projective_decision_primary_sources.md. Bokut1970 §2p137 uses nonunital free algebras; §3p139 and §4pp142–143 supply the effective named-idempotent construction. The separately checked unitization/free-product bridge gives the modern unital-ring premise. Manolescu–Rozenblyum's six-page preprint Theorem2pp2–3 corroborates the unital statement; no publication date was inferred. No byte hash is claimed for the blocked direct download. No novelty claim is made.


## Finite-frame and support-ideal comparison,22:02–22:09UTC

See `checks/paper1_finite_frame_primary_sources.md` for exact queries, primary URLs, reading scope, platform-year discrepancy and downloaded-byte hashes. Deore–Patil2005 supplies the standard semimodule dual-basis lemma; Niefield–Wood2017 supplies the commutative finite-projective dualizability context; Niefield2016 Theorem4.4 supplies a complete-quantale category comparison whose stronger join hypotheses are retained. No exhaustive coverage or priority claim is made. The new finite-frame evaluation removes the function-search parameter after a projective support frame is given. Scalar-ideal idempotence does not imply coefficient-ideal idempotence.


## Modern undecidability corroboration: downloaded-byte update,22:28UTC

The root obtained the six-page author-hosted Manolescu–Rozenblyum preprint; foundation recomputed the278309-byte file's SHA256 as `4c46d370e36bb4bbae5f5ae459f3281892dc5f8898b138949cd1df3a2e604cc5` and reread Theorem2 and its unit-ideal explanation onpages2–3. Exact access provenance is appended to `checks/paper1_projective_decision_primary_sources.md`. This is source access, not an additional independent proof. No external PDF enters the returned archive.


## Integral-support candidate context, approximately23:00UTC

The bounded search and fresh reading of Stacks Tag05BU are recorded in `checks/paper1_integral_support_literature.md`. Standard noncommutative idempotent lifting is credited. No exact antecedent for the candidate matrix-fiber2nbound was verified, and no novelty claim is made. The candidate remains separate until statement-only proof comparison is complete.


## 25 November2026,01:00–01:05UTC: global-semiring radical comparison

Full primary Olson–Jenkins(1973),pp91–93 read from the publisher-linked facing-page scan; the earlier search-indexed PDF contained onlyp91 and was not treated as complete. DOI10.4064/fm-79-2-91-93. Their global-zero/Bourne-quotient radical is distinct from the support-preserving compatible family here. Rich1982Cor1p57 remains the exact ordinary corner predecessor. Wang–Ren2026publisher text was read but missing displayed formulas prevent use as a theorem source. Exact access, hashes, locators and bounds are in `checks/paper1_levitzki_source_comparison.md`. No priority claim.


## paper1_no_fixed_finite_objects_literature

# Bounded primary-source comparison for SZ1-109

Run: /root/foundation; model GPT-6 Astra Pro; effort setting not exposed. Search and comparison occurred after both complete mathematical proofs and before checkpoint19. This is a source event, not an independent mathematical check.

## Search scope

System2 queries: “bicyclic monoid semiring projective semimodules finite support category rings”; “small preadditive category projective modules finite full subcategory finitely generated”. System1 verification queries: “bicyclic” “semiring” “projective”; “preadditive category” “finite” “generating set” projective. Primary publisher and author-hosted pages were opened. Secondary search hits were not used as mathematical evidence. These bounded searches do not establish novelty, priority, or exhaustive absence of the construction.

## Primary comparisons

1. Prest, M. (2012, September26). *The functor category*. Categorical Methods in Representation Theory, Bristol lecture notes. Author PDF: https://personalpages.manchester.ac.uk/staff/mike.prest/BristolTalksNotes.pdf . Read the title/date, Example1.1, Theorem1.2, and Section1.2 through the retrieved Corollary1.10, including the representable-projectivity argument. The infinite-chain path-category example and representable functors supply familiar ordinary-category context: the source objects needed for a given finite projective need not form one fixed finite collection for every projective. SZ1-109 realizes a corresponding restriction failure within one inverse-semiring support, while keeping every upper coefficient ring semisimple. It does not claim the general functor-category phenomenon as new. Browser extraction was available after one initial timeout; a separate local-byte retrieval returned503, so no file hash is asserted.

2. Bertman, M. O. (1978). Bicyclic semirings. *Journal of the Australian Mathematical Society (SeriesA),26*,419–441. https://doi.org/10.1017/S1446788700011952 . Primary publisher PDF opened; printed419–420read for the abstract, bicyclic multiplication and exact definition. Here “inverse semiring” refers to multiplicative inverse-semigroup structure, and the paper classifies additions on the bicyclic carrier. It is not the additive-inverse coefficient reconstruction used here, whose support carrier is the finite-subset semiring. No full-paper reading or projective-classification comparison is claimed. Downloaded outside deliverable at scratch_analysis/paper1_109_primary/Bertman_1978.pdf:877828bytes,SHA256b7745e48972cd79acd929fa8d8be5f5792081082d78423f1127d5a4022de7f8e.

3. Miller, C. (2021). *Semigroups whose right ideals are finitely generated*. Proceedings of the Edinburgh Mathematical Society,64(4). https://doi.org/10.1017/S0013091521000638 . Publisher HTML passage immediately before Lemma6.23 was read: it gives the bicyclic pair multiplication and presentation. This is supporting context for the classical monoid, not a source of SZ1-109. The manuscript independently proves its required normal-form and unit facts. No whole-article read or local PDF hash is claimed.

## Conclusion and limits

The ordinary finite-representable framework and bicyclic monoid are established background. The explicit coefficient diagram and projective restriction example are proved in full in the manuscript and checked by separate derivations. No precise antecedent for that combined construction was identified in this bounded search, but no novelty claim follows. This boundary only excludes restriction to one fixed finite set of action objects; it does not exclude every universal ordinary-ring construction and does not reset the unrestricted classification gate.

Saved UTC: 2026-11-25T03:38:53.617591+00:00


## paper1_root_exchange_sources_literature

# Exchange-ring finite-corner source check

Recorded UTC: 2026-11-25T04:07:05.338206+00:00. This is a source audit, not a newly admitted inverse-semiring theorem or a main-gate reset.

Nielsen, P. P. (2006). *The exchange property for modules and rings* [Doctoral dissertation, University of California, Berkeley]. Author-hosted PDF: https://mathdept.byu.edu/~pace/PaceThesis_web.pdf. Retrieved25November2026. The downloaded file has364694bytes,74PDFpages and SHA-256 e753c89125d6679e2652a64c3e96035e1e7da6b0ce47ae41b2bc78f8b17c8e90.

Root read the complete proofs of Lemmas2.3 and2.4 on printed pages2–3 (PDFpages9–10), the complete statement and proof of Proposition2.7 on printed pages4–6 (PDFpages11–13), and Corollary2.8 and Definition2.9 on printed page6. Lemma2.4 proves closure of the fixed-cardinality exchange property under finite direct sums and direct summands, using the fixed-summand refinement of Lemma2.3. Proposition2.7 characterizes exchange of a module by orthogonal decompositions of summable identity decompositions in its endomorphism ring. Corollary2.8 specializes to two summands; Definition2.9 applies this to the regular module. These full proofs establish the finite Peirce closure route: a finite complete orthogonal family e_i in B identifies End_B(e_i B) with e_i B e_i, and the finite direct sum of these right modules is B_B. No assertion about arbitrary infinite sums is imported.

The author attributes the exchange-ring equivalence with lifting modulo all one-sided ideals to Nicholson on printed page6. That attribution by itself is not a full proof check of the lifting theorem. Foundation is separately checking the needed ordinary lifting input and its coefficient application.

A bounded search around03:59UTC also found Danchev's *Semi-Boolean Corner Rings* (2017), International Mathematical Forum12(16),795–802, DOI10.12988/imf.2017.7655, at https://m-hikari.com/imf/imf-2017/13-16-2017/p/danchevIMF13-16-2017.pdf. Its printed page797 explicitly attributes two-corner exchange closure to Nicholson. This is retained only as a secondary-attribution lead. Nicholson, W. K. (1977), *Lifting idempotents and exchange rings*, Transactions of the American Mathematical Society229,269–278, DOI10.1090/S0002-9947-1977-0439876-2, was located bibliographically, but the publisher download did not yield a local PDF. No full Nicholson proof read is claimed here.

No external PDF or text extraction is included in the deliverable. The source distinction matters: a finite exchange-ring subclass may strengthen an object-lifting theorem, but does not itself settle the unrestricted projectivity classification or reset its research counter.

## Nicholson primary text follow-up (2026-11-25T04:14:56.935370+00:00)

The full author-uploaded paper was retrieved at https://www.researchgate.net/publication/238873439_Lifting_Idempotents_and_Exchange_Rings. Its metadata explicitly identifies W.K.Nicholson as the author uploader. Root read the complete Proposition1.1 and Corollary1.3 on printed page270, including all four implications. In particular the exchange-equation identity p-a=(r-s)(a-a^2) proves lifting modulo every left ideal, and hence every two-sided ideal. This closes the earlier ordinary lifting source gate. The browser-readable primary text is available; the publisher PDF and a local downloadable copy remain unavailable, and no local SHA is claimed. No full Theorem2.1 read is claimed by root from the mere presence of the later source text.

## Global exchange-semiring terminology (2026-11-25T04:27:35.484601+00:00)

Root downloaded the exact Das–Kar2022version1primary PDF from https://assets-eu.researchsquare.com/files/rs-1751073/v1_covered.pdf?c=1655236994 . It has257752bytes,22PDFpages and SHA-256 a62bdcb94249dd7b007f2d4c0b2388126c97498a8548e9a51feee597cbb17f29. The complete absorbing-complement definitions on printed p4/PDFp5 and Definition3.11 on printed p10/PDFp11 were read. Their condition is global: every multiplicative idempotent has such a complement, and for each nonzero x an appropriate complementary pair lies in S(1+x) and Sx. The manuscript accurately distinguishes this formulation from ordinary exchange in each upper coefficient ring. No equivalence, implication or import of the adjacent Theorem3.12 is asserted. The title/version/DOI citation and neighboring publication records are in foundation's separate source record.


## paper1_root_finite_category_literature

# Ordinary finite-ring context checked by root

2026-11-24,21:01–21:04UTC. Root opened the author-hosted PDF of Henning Krause, *Krull–Schmidt categories and projective covers*, and used exact finds to inspect Lemma3.6(pp6–7), Proposition4.1(pp8–9), Theorem4.2(p9), and Theorem5.5(p11), in the12-page10October2014author version. These give projective-cover/local-endomorphism equivalences, the semiperfect-ring characterization, uniqueness, and finite-length decomposition. Published metadata: Krause,H.(2015). *Expositiones Mathematicae,33*,535–549. DOI10.1016/j.exmath.2015.10.001. URLhttps://www.math.uni-bielefeld.de/~hkrause/krs.pdf. The independently downloaded source hash recorded by operator is00f58b3b618864545f16fc2ecb5288670b7498d0fbd617cf591ff68e2c1c038d. No source copy is included.

Root also opened Lam,T.Y.(2000), *Bass’s work in ring theory and projective modules*, arXiv:math/0002217v1,42pages, URLhttps://arxiv.org/pdf/math/0002217, and inspected Theorem5.1,p20 of the PDF, on projective covers and semiperfect rings; the adjoining paragraph includes one-sided Artinian rings. Operator independently retrieved/read the relevant full pages, hashbd73ce7377d8838c45047d0f0d22c65373b9943286dedd1c9533c54c2e9d7eb1. Exact PDF pagination is distinguished from publication pagination.

The finite-S theorem applies this ordinary ring theory after proving that its action category ring is finite. The ideal filter IP=P iffI acts nontrivially on the simple top of an indecomposable projective is a short deduction from the superfluous cover kernel, proved explicitly. The paper additionally gives a direct finite-ring proof via Fitting kernels/images, simple quotients and Hom-to-simple multiplicities. No new ordinary projective-cover or Krull–Schmidt theorem is claimed, and this source inspection is a literature check rather than an additional fresh proof event.


## paper1_root_finite_models_literature

# Literature comparison for finite coefficient models and upper-ring hypotheses

Search and source-read record saved 2026-11-25T03:05:13.141778+00:00, root, GPT-6 Astra Pro, effort not exposed. This is source/comparison work, not a mathematical independent proof event. No priority claim is made.

## Ordinary inputs actually read

Krause, H. (2015). Krull–Schmidt categories and projective covers. *Expositiones Mathematicae, 33*(4), 535–549. https://doi.org/10.1016/j.exmath.2015.10.001. Author preprint: https://www.math.uni-bielefeld.de/~hkrause/krs.pdf. SHA-256: 00f58b3b618864545f16fc2ecb5288670b7498d0fbd617cf591ff68e2c1c038d; 285476 bytes;12pages. Root reread the complete primary Proposition4.1 on printed pp8–9, and Theorem4.2 plus Corollary4.3 on p9 at the current03:00–03:03 check. The equivalence between finite local-idempotent decompositions and semiperfect/projective-cover structure, and finite decomposition uniqueness, are classical inputs. They are not asserted as new results. This exact read verifies the locators used in the rewritten upper-semiperfect amplitude proof.

The elementary correction3a²−2a³ over a square-zero ideal is already attributed in the paper to the Stacks Project, Tag05BU, and was checked earlier in this run. The new107 proof has the stronger one-sided relation(ker pi)N=0 and therefore uses e=a² directly. Its ordinary polynomial calculation is included in full. The coefficient support calculation and exact mixed-corner bijections are the scope of107; no new ordinary idempotent-lifting theorem is claimed.

Katsov, Y., & Nam, T. G. (2012). *On radicals of semirings and related problems* (arXiv:1206.1580v1). https://arxiv.org/pdf/1206.1580. The primary PDF SHA-256 recorded and separately verified by the definition checker is572e6bfde64532c1c71646be1543f56f16074068078776b4c31bee314a5649fd. Foundation and operator directly checked printed pp4–5,12,14–15 and the matrix/corner results on pp32–36; root fully read their explicit new-example proofs and those exact read-scope records. Root does not relabel their primary read as a fresh root primary read. The Jacobson–Bourne and simple-semimodule definitions differ from the support-preserving coefficient quotient. Example106 gives an explicit calculation separating all three conventions.

## Current searches and bounded findings

On25November2026 around02:58–03:03UTC, engine1 queries included:

- inverse semirings / projective / modules, with arXiv, journal and TAC primary domains;
- Clifford semigroups / monoidal Grothendieck / projective, with arXiv and TAC domains;
- idempotent / annihilator / projective / semiring, with arXiv, EMS and Springer primary domains;
- site:eccc.weizmann.ac.il inverse semiring projective;
- site:hexagonmath.org inverse semiring projective coefficient;
- idempotent lifting / annihilator / ring / projective, with Stacks, arXiv and EMS primary domains.

Engine2 follow-ups used inverse semiring / projective / coefficient; projective / ringoid / inverse semiring; and semiperfect / inverse semiring. These produced substantial irrelevant dictionary/index material, which was not used as technical evidence. Search negatives are not a completeness claim.

The relevant direct results remained Faul–Goswami–Joubert–Manuell, arXiv:2411.12318, and Caviglia–Faul–Manuell–Mesiti, arXiv:2607.12944. Their attached primary texts were already checked and compared earlier in this run. A current open of the latter arXiv landing page failed with DisabledError, while the author's22-line publication page was directly opened: https://lucamesiti.github.io/publications/2026-07-15-MonoidalGrothClifford/. That page states the inverse-semiring/lax-monoidal-functor correspondence; it supplies metadata and scope, not a substitute proof of107. Its Theorem8.5 attribution remains grounded in the earlier full attached-source check.

Hexagon2611.00993v1 reappeared: https://hexagonmath.org/2611.00993v1. Its R0 spectrum/semimodule/projective claims and exact relation to the earlier work were already fully compared on24November; this repeated search is not counted as a new full read or new predecessor. No exact finite ordinary coefficient-model antecedent was verified in these searches. This does not establish novelty or priority. No relevant ECCC result was recovered by the named query.

A new primary lead was Diesl, Dittmer and Nielsen, *Idempotent lifting and ring extensions*, https://mathdept.byu.edu/~pace/Enabling_web.pdf. Only its retrieved title/abstract was exposed at this cutoff; its counterexamples to general lifting stability are not imported as theorem dependencies. A second lead, Pavešić's *Induced liftings, exchange rings and semi-perfect algebras*, https://users.fmf.uni-lj.si/pavesic/RESEARCH/Induced%20liftings%2C%20exchange%20rings%20and%20semi-perfect%20algebras.pdf, likewise remains a search lead, not an additional accepted lemma. A later exact primary read may inform further research, but neither lead changes the present proof or review counters.

No external PDF, extraction or unchanged attachment is included in the deliverable. New fetched-source hashes are recorded only after bytes are actually fetched; no hash is invented for the two unopened leads.


## paper1_root_followup_literature

# Further projectivity literature, 24 November 2026, 19:57–20:02 UTC

This is a dated search and comparison record, not an independent proof event. All downloaded sources remain outside the returned workbench. Their addresses, hashes and used locators are recorded below. The canonical support-admissible ideal criterion was independently derived before these searches; no priority claim is made.

## Search sequence and the newly accessible foundation deposit

At19:57UTC, searches for inverse-semiring projectives, Clifford semimodule projectivity, ringoid trace ideals and idempotent-semimodule support returned a public Hexagon deposit dated24November2026: *Spectrum, semimodules and projectives of the inverse semiring R_0 of Faul, Goswami, Joubert and Manuell*, hexagon:2611.00993v1. A second search engine verified the entry, its abstract, provenance and references. The site lists user Alderliefste as contributor; that metadata is not silently converted into an author byline.

- Landing page: https://hexagonmath.org/2611.00993v1
- PDF: https://hexagonmath.org/pdf/2611.00993v1
- Public date:24November2026; PDF10pages.
- PDF retrieval19:58:10UTC:413871bytes; SHA-256 `95eb60b92984ec13da5b9388afa7148ac81aa65ca7128350a4d139331121be6d`.
- HTML retrieval19:58:17UTC:113469bytes; SHA-256 `f0fbdef24ce6f2062eb5a16ca1082a1039459f5c5733c760d5e9a6f8808dcddb`.
- Initial direct tool opens failed, but opening the indexed PDF reference and then ordinary public download succeeded. The earlier failures remain historical access observations, not the current status of this deposit.

Its Theorems1–3 and Proposition5.3 give the foundation spectrum, module-diagram and finite-projective classification results, with zero labels permitted; Remark5.4 contains the corrected ordinary-module projectivity statement. Its Remark3.4 gives the quotient-counting formula used in Paper2. Its final open section names the two-idempotent, iterated-extension and general-pair module questions that this series develops. The exact public-source comparison with the attached foundation version is recorded separately by the operator worker. The public page also links the permanent recordWB-0008 and its workbench, but the linked GitHub pages and FORMAT.md still returned DisabledError through the browsing service on this attempt. The raw FORMAT.md URL also returned DisabledError. No exact remote-schema conformance is inferred from these unsuccessful reads.

The public provenance records a pre-deposit correction on24November. This record does not infer who performed any external publication or that the present workspace caused it. No publication, repository write or person-directed message was performed by this run.

## Ordinary trace ideals and the matrix reformulation

Herbera, D., & Příhoda, P. (2014). Reconstructing projective modules from its trace ideal. *Journal of Algebra, 416*,25–57. https://doi.org/10.1016/j.jalgebra.2014.06.010

The publisher metadata and primary arXiv manuscript were opened after searches for the exact title and for trace ideals in preadditive categories. The version used is arXiv:1309.5021v1,19September2013,29pages: https://arxiv.org/pdf/1309.5021 . Downloaded19:59:57UTC,360169bytes, SHA-256 `71fcb80d4ee5b077f6bc64a33f83f698b6d4a8e57be69cbfec210250318f0853`.

Used locator: introduction,p.2. For a finite projective module represented by an idempotent matrix, that passage identifies its trace ideal with the two-sided ideal generated by the matrix entries. This is the ordinary background for the criterion that an idempotent image is generated by an ideal exactly when its matrix entries lie in that ideal. The proof needed here is written out for covariant ringoid modules. The inverse-semiring contribution is the explicit support-admissible ideal and the support-frame argument; the elementary matrix/trace reformulation is not presented as a new general fact about ordinary projective modules. No assertion that the canonical ideal itself is idempotent, or is the unrestricted trace of some proposed family, is made without a separate proof. The paper's broader countable-projective lifting theorems are not invoked.

## Projective functors over rooted action categories

Cortés-Izurdiaga, M., & Torrecillas, B. (2013). Projective and flat objects over rooted rings with several objects. *Bulletin Mathématique de la Société des Sciences Mathématiques de Roumanie,56(104)*(3),315–330. https://ssmr.ro/bulletin/pdf/56-3/articol_5.pdf

Downloaded20:00:03UTC,16pages,383082bytes, SHA-256 `8d3572f5d46434c3897d897610dafe3463704ec4850ad941963a3d3099599460`.

Used locators: §2,pp.316–318 for additive covariant functors, representable projective generators and the tuple description; Definitions1–2,p.319 for the rootedness condition; Theorem1 and its proof,pp.320–322; Remark3 and Example1,p.322. The theorem describes projective functors for a left-rooted small preadditive category using projective quotients by the images from other objects and induction from the endomorphism rings. The example explains why the quotient test fails in the presence of cycles. The general action category in Paper1 is not assumed left-rooted, so this is a precise useful special-case comparison, not a solution of the unrestricted projectivity condition.

An indexed conference document headed *Homological theory of k-idempotent ideal in dualizing varieties* displayed a definition of trace ideals in a preadditive category. Its USP URL redirected to an inaccessible users.ime.usp.br URL; no full-text theorem or bibliographic identification is claimed from that snippet, and it is not used as a proof source.

## Scope of the search

The searches covered the phrases inverse semiring/projective, Clifford semimodule/projective, support/idempotent semimodule, ringoid/trace ideal, preadditive category/trace ideal and rings with several objects/projective. They found the sources above and the previously examined Macpherson and Borger–Jun work. They did not establish an exhaustive citation census or priority for the canonical ideal theorem. Earlier blocked forward-citation-service attempts remain documented in the other literature fragments. No search-result title by itself has been treated as a checked theorem.


## paper1_root_format_literature

# Remote record-format follow-up —24November2026,21:09:50UTC

The official FORMAT.md at https://github.com/KokunoYumeto/mathematics-workbenches was retried through the available public retrieval routes. The latest attempt returned DisabledError; search did not recover a relevant public copy. The detailed access record is root_format_retrieval_followup.md. No remote-schema verification is claimed. The requested local format1-compatible structure includes permanent statement tags, typed checks, cited rather than copied sources, and version manifests.

The GitHub plugin was suggested once as an additional possible official access route; no installation, connection, permission change, or repository push is claimed. This is an access/format record, not a mathematical check or a main-gate movement.


## paper1_root_idempotent_core_literature

# Largest idempotent ideals: source comparison for the canonical action ideal

Recorded 2026-11-24T23:55:40.260191+00:00, /root, GPT-6 Astra Pro; effort not exposed. Bounded searches began23:51:35UTC on24November2026, after deriving the proposed core construction but before its separate check. Engine2 searched “largest idempotent ideal projective”, “idempotent core ideal projective modules”, and “transfinite idempotent ideal trace”; engine1 verified the stable-part/trace and Emmanouil references. Further searches followed Smith's2010chapter and the two papers' primary arXiv versions. These ordinary constructions are known; no priority claim is made for them or for this application.

## Primary results actually read

Emmanouil,I.(2025). Residually nilpotent groups of homological dimension1. Bulletin of the London Mathematical Society,57(10),3223--3232. https://doi.org/10.1112/blms.70140 . Publisher full text: https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.70140 . Section1, particularly Lemmas1.1and1.3, was read in full. It distinguishes stable fixed-left-factor powers kappa(I) from the largest idempotent subideal lambda(I); Lemma1.3(ii)is the exact largest-ideal statement. The full-text HTML is available through the search service; the PDF download returned403, so no original PDF byte hash or unverified page locator is claimed. The paper calls the construction standard and refers to Smith2010.

Šťovíček,J.(2010). Telescope conjecture, idempotent ideals, and the transfinite radical. Transactions of the American Mathematical Society,362,1475--1489. https://doi.org/10.1090/S0002-9947-09-04812-0 . Primary preprint arXiv0802.2189v2: https://arxiv.org/pdf/0802.2189 . Preprint pp3--4, including the categorical ideal definition, transfinite construction and Lemma1, were read and visually checked. This is a categorical predecessor; the stated radical characterization has the Krull--Schmidt hypothesis. That hypothesis is not silently imposed on the arbitrary action category, whose elementary largest-subideal argument is written directly. The more restrictive Theorem8is neighboring context only, not a dependency.

Chen,X.-W.,Li,Z.-W.,Zhang,X.,&Zhao,Z.(2026). Comparing classical tilting modules and tau-tilting modules. arXiv2501.02466v2, revised27October2026; PDF date28October2026. https://arxiv.org/pdf/2501.02466v2 . Preprint pp2--3were read, and p3visually checked from the official arXiv bytes. The stable part of an ideal and projective trace criterion appear in Section2and Lemma2.1. This paper works over ARTIN algebras. Its finite-power stabilization and the converse from an idempotent ideal to a projective trace are not imported to arbitrary rings. A search mirror was an initial locator; the arXiv copy supplies the verified source bytes.

Smith,P.F.(2010). Projective modules, idempotent ideals and intersection theorems. In D.VanHuynh&S.R.López-Permouth(Eds.),Advances in ring theory(pp303--326). Birkhäuser. https://doi.org/10.1007/978-3-0346-0286-0_20 . The primary publisher metadata, abstract and references were opened. The full chapter is subscription content and was not read; no theorem locator or exact proof dependence is asserted from the abstract.

## Byte records

- Stovicek_2008.pdf: URL https://arxiv.org/pdf/0802.2189; 240049bytes, SHA256 058bbcd38dd7dec0d90fa7d687dd00efc34580ad55c4ed315c6fa8187b23752d, retrieved2026-11-24T23:54:14.375145+00:00.
- Chen_Li_Zhang_Zhao_2026.pdf: URL https://arxiv.org/pdf/2501.02466v2; 299732bytes, SHA256 4e1a0305d77bf024617936b8655d4423ff913f52a61c62a84bde599ae404697f, retrieved2026-11-24T23:54:14.387088+00:00.
- Emmanouil_2025.pdf: URL https://londmathsoc.onlinelibrary.wiley.com/doi/pdfdirect/10.1112/blms.70140; retrieval failed: HTTP Error 403: Forbidden.

External PDFs, images and text extractions remain outside the deliverable. The proposed paper application is to replace J_L by its largest idempotent subideal while keeping exactly the same finite idempotent matrices and amplitudes. This is not a solution of their classification, and no automatic review-counter reset is inferred from the source work.


## paper1_root_levitzki_literature

# Root direct primary reading: compatible locally nilpotent coefficient reduction

25 November2026. Root read the primary publisher PDF after the fresh new semiring proof was saved00:41:57and its finite-matrix consequence00:44:18. Full text pp52–57was opened between00:44:18and00:45:31; printedpp53and57were then read visually from publisher screenshots in the call clocked00:45:31. This is a source comparison, not independent semiring proof credit.

Rich, M. (1982). Some properties of the Levitzki radical in alternative rings. *Journal of the Australian Mathematical Society (Series A), 32*(1),52–60. https://doi.org/10.1017/S1446788700024393

Primary PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/06A2698C066CE8394EC441EEB457C2A3/S1446788700024393a.pdf/some_properties_of_the_levitzki_radical_in_alternative_rings.pdf

The downloaded primary bytes, independently located by foundation and retained outside the deliverable, have407429bytes and SHA25694c4ae6ee3d049b435f724908c634b7bdec4f89c9183cd1d9b61afb00825a8be. Root's direct retrieval refs are turn822107584view0and screenshots turn420981455view0/1. Printedp53defines the largest locally nilpotent ideal and zero-radical quotient. Corollary1onp57states the associative Peirce-corner ideal result without the alternative theorem's torsion or semiprime hypotheses. Its proof context onpp54–57was read, not transferred with inappropriate alternative-ring assumptions. The closingp57sentence attributes associative corner equality to Anderson1974; Anderson's paper has not been independently opened in this check, so that attribution remains via Rich.

The new proofs establish a context-compatible inverse-semiring coefficient ideal, its local nilpotence in support-derived matrix fibers, projective-class invariance and finite-matrix compatibility. The ordinary radical and corner input is known. Rich does not state this inverse-semiring construction; no exhaustive novelty or priority conclusion is drawn from this bounded source comparison. External PDF, extracted text and screenshots are excluded from returned archives.

## Direct primary comparison: Olson and Jenkins1973

Root fully read both local primary page images after01:11:06and before01:13:57UTC25November2026. They contain all printed pages91–93. The correct publisher download redirects to https://matwbn.icm.edu.pl/ksiazki/fm/fm79/fm7919.pdf . The web open returned403and is not treated as content access; local primary scans supplied the direct reading. External PDF remains outside the deliverable: scratch_analysis/levitzki_primary/Olson_Jenkins_1973_full.pdf,626685bytes,SHA256 c1bf6a13185289c9b08e2f9ad3bcd15a2879b6151f3d6d11cbe9508b62e8cf67; hash independently verified at01:13:57.

APA: Olson,D.M.,&Jenkins,T.L.(1973). A note on the Levitzki radical of a semiring. Fundamenta Mathematicae,79(2),91–93. https://doi.org/10.4064/fm-79-2-91-93 . The printed author name is Terry L.Jenkins; publisher metadata's Jankins spelling is not followed.

Definitions1–2p91use nilpotence at the semiring's global zero and the sum of locally nilpotent ideals; the text credits Barbut. The quotient convention is the Bourne quotient. Definition3and Lemma1p92concern subtractive closure and its local nilpotence; Theorem1pp92–93makes the radical subtractive. The unlabelled quotient lemma onp93states radical zero after the quotient. The present coefficient construction is different: it retains support and additive group structure, and tests ordinary fiber-ring radicals. For a zero-adjoined ring R0,the classical global radical is only the new zero, because even the old ring zero never powers to the newly adjoined zero; the compatible coefficient quotient may remove Lev(R). This distinction is now in Paper1. No priority claim for the ordinary radical itself is made.

Root comparison record appended: 2026-11-25T01:25:12.863460+00:00

## Exploratory nil-ideal extension: no theorem admitted

On25November2026after01:13:57and before01:21:44, root searched for broader nil-ideal projective lifting. Queries included “nil ideal K0 projective modules idempotent lifting matrix nil ideal exchange ring”; “idempotents lift modulo nil ideals matrix rings K0 Stacks”; exact-phrase nil ideal/K_0and nil ideal/projective/lift/matrices searches on author, arXiv, AMS and Cambridge domains; and “idempotents lift” “matrix” “nil ideal”. These were exploratory source checks, not evidence of a stronger semiring theorem.

Weibel's author-hosted K-book ChapterI, https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.I.pdf , was opened through the web PDF reader. Root inspected Exercise1.12p5and Exercises2.1–2.2p13(the reader indices are4and12). Exercise1.12records nil ideals inside the Jacobson radical and matrix stability of radical ideals. Exercise2.1gives uniqueness of finite projectives modulo radical ideals, while2.2states existence/bijection for nilpotent or complete ideals. The inspected text does not supply the desired arbitrary noncommutative nil-ideal matrix-lifting theorem. Only these passages were used; no full-book reading is claimed.

Př íhoda's author preprint “Fair-sized projective modules”,31May2006, https://ka.karlin.mff.cuni.cz/preprint/alg06_08.pdf , was opened. Root inspected the opening discussion and Lemma4.3on printedp12(readerindex11), which proves scalar idempotent lifting modulo a nil ideal by a polynomial in a chosen lift. It does not in that lemma assert that every finite matrix over a nil ideal is nilpotent. These web-reader PDF retrievals have no locally preserved bytes or SHA at this record; neither is an admitted new source dependency.

Additional primary search hits were the1974Canadian Mathematical Bulletin article “On lifting idempotents”; the2015Journal of Algebra article “Commuting idempotents, square-free modules, and the exchange property”,DOI10.1016/j.jalgebra.2015.07.015; and2021“Lifting potent elements modulo nil ideals”,DOI10.1016/j.jpaa.2021.106762. Only search-result passages were inspected; the2015DOIopen returned403. No full proof is credited from those hits. The commutative Stacks lifting result was not transferred to arbitrary noncommutative matrix rings.

The proposed extension from locally nilpotent compatible ideals to arbitrary nil ideals is unresolved in this attempt. Scalar lifting cannot silently replace the finite-matrix nilpotence/local-nilpotence argument. No stronger radical, projective invariance theorem, source novelty claim or review movement is recorded. The verified locally nilpotent quotient remains the current gate.

Record time: 2026-11-25T01:31:13.266382+00:00


## paper1_root_lifting_boundary_literature

# Ordinary lifting hypotheses: primary-source audit and research boundary

Recorded UTC: 2026-11-25T03:30:42.870719+00:00

This is source comparison and a research-route record. It is not a newly admitted theorem, an independent re-proof of the source paper, or a main-gate reset.

## Primary sources actually read

Diesl, A. J., Dittmer, S. J., & Nielsen, P. P. (2016). Idempotent lifting and ring extensions. *Journal of Algebra and Its Applications, 15*(6), Article 1650112. https://doi.org/10.1142/S0219498816501127

Author-hosted preprint: https://mathdept.byu.edu/~pace/Enabling_web.pdf. SHA-256: 65c6af9b6d210c0f206282b59547fd4ce80b8e2da6df30ac292617c4876e181e; 329498 bytes; 11 PDF pages. Publication metadata verified on the author's research list, https://mathdept.byu.edu/~pace/research.html, item36, on 25 November2026. The DOI fetch returned403 and is not represented as a full publisher read.

Root read the introduction and the complete statement and proof of Theorem2.1 on preprint pages2–3 through the web source, then reread the exact local PDF text by 03:28:24UTC. The source constructs a commutative ring S in which scalar idempotents lift modulo Jac(S), while a specified 2-by-2 idempotent does not lift modulo Jac(M_2(S)). The construction is S=(1+I)^(-1)k[a,b,c], I=(a^2-a+bc); its quotient has the indicated additive two-coordinate degree on reduced monomials. The unit and radical calculation, common-denominator UFD factor argument, and impossible degree of the proposed common factor were checked against the complete proof. This is attributed ordinary-ring mathematics, not a result of the present work.

The author's linked erratum was also read in full: https://mathdept.byu.edu/~pace/Enabling_web_errata.pdf; SHA-256 752b678c16e2a33fb9e651908d439c6d1fc996bd2688cc392593b578ad0850e4; 44628 bytes; one page. It supplies a necessary ideal condition in Corollary5.5 and does not alter Theorem2.1.

Pavešić, P. (2010). Induced liftings, exchange rings and semi-perfect algebras. *Journal of Pure and Applied Algebra, 214*, 1901–1906. Author-hosted preprint: https://users.fmf.uni-lj.si/pavesic/RESEARCH/Induced%20liftings%2C%20exchange%20rings%20and%20semi-perfect%20algebras.pdf. SHA-256 8e7cb926fe7665696ec7ea183adcef948c390150791bb8fd2b3cbe9e6972ab7f; 156183 bytes; nine PDF pages. Publication details checked against the author's publication list and university research page. Root read the introduction and the preliminary lifting discussion through the start of Theorem2.5/Corollary2.6, not the whole paper. Its exchange-ring characterization and statements of ordinary lifting results are background leads only; no unverified finite-corner exchange theorem is imported here.

Khurana, D., Lam, T. Y., & Nielsen, P. P. (2016). Exchange rings, exchange equations, and lifting properties. *International Journal of Algebra and Computation, 26*(6), 1177–1198. Author-hosted preprint https://mathdept.byu.edu/~pace/suit2_web.pdf. Root opened the introduction and early results through Section2 while tracing the classical lifting definitions. This source has not been downloaded or fully read, and no result from it is admitted into a manuscript on the basis of this scan.

## Search scope and consequences

At about03:23–03:28UTC, web searches for the exact titles above, author publication metadata and exchange-ring lifting led to the author-hosted primary papers. The first source directly invalidates a proposed shortcut: scalar idempotent lifting in each upper coefficient ring cannot automatically be substituted for a matrix-stable lifting hypothesis. Even the ordinary two-element-support specialization already contains the matrix obstruction. No claim that scalar lifting implies quotient projective-object lifting is made.

A separate potential extension through exchange rings would require a fully verified ordinary finite-corner closure theorem and a complete coefficient lift argument. Neither has been admitted. Likewise no use is made of an implication from an arbitrary nil ideal to nilpotence of its matrix ideal. The checked locally nilpotent route and the semiperfect lifting theorem retain their stated hypotheses.

External PDFs and any extractions remain outside the deliverable tree and are excluded from every returned ZIP. This record contains our own source comparison only. No priority claim is made.


## paper1_root_manolescu_source_followup_literature

# Later byte retrieval of the Manolescu–Rozenblyum primary preprint

Recorded 2026-11-24T22:29:45.297063+00:00 by /root, GPT-6 Astra Pro; effort not exposed.

The primary Stanford preprint at https://web.stanford.edu/~cm5/dgas.pdf was downloaded successfully during the22:17–22:18UTC follow-up. Its title is *Undecidability problems for semifree DG algebras*, by Ciprian Manolescu and Nick Rozenblyum. The printed source is undated in the bibliographic record used here. The earlier web reading had already checked its unital-ring statement (Theorem2, pp.2–3). This later retrieval supplies byte provenance; it is not a new mathematical check and is not used to retroactively alter checkpoint11.

Bytes: 278309. SHA256: `4c46d370e36bb4bbae5f5ae459f3281892dc5f8898b138949cd1df3a2e604cc5`. The external PDF remains outside the deliverable. The source's own AI acknowledgements describe that source, not the production or checking of this series.


## paper1_root_projective_decision_literature

# Root follow-up: exact ring-triviality premise

Read 2026-11-24T21:49:41.163731+00:00. Bokut', L. A. (1970). Unsolvability of certain algorithmic problems in a class of associative rings. *Algebra i Logika,9*(2),137–144. https://www.mathnet.ru/eng/al1237. Primary full PDF opened through its official retrieved reference. Printed137defines nonunital free coefficient algebras;139states the effective primitive-or-zero lemma;142–143uses a semigroup algebra and a free-product obstruction. The named-idempotent application overF2and the separate unital bridge were checked in root_projective_decision_source_comparison.md. Direct-byte retrieval failed, so SHA256remains unavailable rather than guessed. No source copy or extraction is included.

Manolescu, C., & Rozenblyum, N. (n.d.). *Undecidability problems for semifree DG algebras* [Research preprint]. https://web.stanford.edu/~cm5/dgas.pdf. Sixpages; Theorem2,pp2–3, explicitly gives the unital formulation. This corroborates the premise but does not replace checking the original convention. Its DGA results are not imported. Direct web-reading refscurrentlyturn102027989view0/1andturn322520999view1; these are retrieval identifiers only.

The algebraic reduction075was separately freshly proved before author access. The source and bridge review is targeted, with no fresh-proof or exhaustive novelty claim. Ordinary undecidability is classical input; the exact inverse-semiring/projective reduction and its scope are proved here.


## paper1_root_semiperfect_literature

# Finite-support semiperfect classification: primary-source comparison

Root/GPT-6 Astra Pro,25November2026. The semiring classification098and example099were completely authored01:45:38before operator's new statement-first proof. The ordinary inputs are classical and not claimed as new.

## Searches and bounded outcomes

Between01:40and01:46UTC,system2queries covered “semiperfect ring finite complete orthogonal idempotents local corners projective covers site:arxiv.org”; “semiperfect ring finite complete orthogonal idempotents local rings projective cover author pdf”; “inverse semiring semiperfect”; and “semilattice projective semiperfect semiring”. System1verified on arXiv,AMS,Cambridge and Springer with “semiperfect ring finite complete orthogonal local idempotents projective covers Bass theorem author pdf”,and searched “inverse semirings projective semiperfect Faul Goswami Joubert Manuell”,plus exact semiperfect/inverse-semiring searches on Hexagon and ECCC. No exact inverse-semiring classification under the stated upper-fiber hypothesis was verified. This bounded failure to locate an antecedent is not a priority claim.

The already fully compared Hexagon2611.00993v1foundation paper appeared again; its prior complete comparison and source hashes remain in paper3_hexagon_foundation_literature.md. It concerns the zero-adjoined-ring case and is not relabeled a new source. Other search snippets,including potentially misleading secondary summaries,were not used as theorem evidence.

## Direct ordinary source carrying the proof

Krause,H.(2015). Krull–Schmidt categories and projective covers. Expositiones Mathematicae,33(4),535–549. https://doi.org/10.1016/j.exmath.2015.10.001 . Author PDF:https://www.math.uni-bielefeld.de/~hkrause/krs.pdf ,10October2014version,12pages,285476bytes. SHA25600f58b3b618864545f16fc2ecb5288670b7498d0fbd617cf591ff68e2c1c038d. Local bytes rehashed for this record.

Root had previously read the relevant primary arguments in this run,and reread complete Proposition4.1on printedpp8–9and Theorem4.2p9in the01:53:09call,then the projective-cover definitions and Lemma3.6statement/proof contextp6at02:01:26. Proposition4.1equates semiperfectness with finite local-endomorphism decomposition and covers of simple or finite generated modules; Theorem4.2gives uniqueness. These are exactly the ordinary input used in098. The new argument identifies every finite action-category diagonal as F(r(l,l)),with r(l,l)upper idempotent,then assembles local idempotent decompositions of those corners. The ideal filter is explicitly proved from the cover kernel or Nakayama. No ordinary semiperfect/Krull–Schmidt result is claimed as new.

## Recent neighboring work, with precise scope

Positselski,L.,&Šťovíček,J.(2024). Topologically semiperfect topological rings. Algebras and Representation Theory,27,245–278. https://doi.org/10.1007/s10468-023-10217-x . Author preprint:https://arxiv.org/pdf/2201.03488v4 ,38pages,10July2023version,458755bytes,SHA256627a0ead6eadae6bd4add02174b3ec29f24f40abe6085c98d1ce8ccc424f9458. Root opened the primary abstract/PDF/HTML,read the introduction's scope and the classical discussion plus Lemma4.3on printedpp14–15. Complete local text of those two pages was checked at01:59:27and02:01:26. Corollary4.2p14identifies local corners with projective covers; the following paragraph states the classical finite orthogonal-local-idempotent characterization,citing Anderson–FullerTheorem27.6. Lemma4.3proves its module-decomposition form. The topological theory concerns complete separated right-linear topological rings and contramodules; none of those conclusions is transferred silently to an arbitrary infinite action category. Our finite block ring needs only the classical result. This supplies neighboring context,not a new assumption or priority proof.

A second primary author PDF,P.Pavešić,“Endomorphism rings of p-local finite spectra are semiperfect”,was opened at https://users.fmf.uni-lj.si/pavesic/RESEARCH/Endomorphism%20rings%20of%20p-local%20finite%20spectra%20are%20semiperfect.pdf . It has9pages,193015bytes,SHA2567be15058797438db30a6ab90a9d8dc69d83564fbf16413bb37ea88144bcc2f3c. Only its title/introduction and printedp2semiperfect characterization were read; its spectrum theorem is not used. Its attribution to Lam23.6is only reported via that source. Publication metadata was not needed or independently verified for a manuscript citation.

All external PDFs and text extractions stay outside the deliverable and returned archives. No full reading of either the topological paper or spectrum paper is claimed. The first attempt to write this record failed with a shared-disk-full error; after deleting only older reproducible page-image caches,the complete record was rewritten and verified. Recordtime:2026-11-25T02:06:51.834512+00:00


## paper1_root_upper_unit_literature

# Primary-source comparison for the unrestricted coefficient quotient

Recorded 2026-11-24T23:50:00.485948+00:00, /root, GPT-6 Astra Pro; effort not exposed. This is a source check, not a fresh mathematical proof. Root reopened the publisher PDF and Stacks Tag05BU at about23:48UTC on24November2026, read Bandelt--Petrich printed pp155--160, and visually inspected all of pp159--160 from the publisher PDF. The definition on p159 is the TWO-SIDED annihilator {x in R:xR=Rx=0}; the source calls it a double annihilator, which here does not mean an iterated Ann(Ann(-)).

Bandelt, H.-J., & Petrich, M. (1982). Subdirect products of rings and distributive lattices. Proceedings of the Edinburgh Mathematical Society,25,155--171. https://doi.org/10.1017/S0013091500016643 . Primary PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0590C1AC0914EB337DBF0FDCBBF364DB/S0013091500016643a.pdf/subdirect-products-of-rings-and-distributive-lattices.pdf . Bytes:629685; SHA256:688ce96d1784a68267b38c34e2955ea3a1f9765e634713ac2dcc6fb95af976e8. External bytes and text extraction remain outside the deliverable.

Lemma4,pp159--160, assumes(A1)--(A3), equivalently a distributive lattice of rings as established in Lemma1and its corollary,pp156--157. It proves the transition maps are ring homomorphisms, their images are ideals, and their kernels lie in the source's two-sided annihilator. This is an exact predecessor for the image-ideal and annihilation mechanism and is now credited in Paper1. It does not state the arbitrary-support context-defined coefficient ideal, the finite matrix-fiber exponent n+1, or the present finite-projective-class reduction. No exhaustive novelty conclusion is drawn.

The Stacks Project,Lemma10.32.7,Tag05BU, https://stacks.math.columbia.edu/tag/05BU , was read in full. Its possibly noncommutative algebra formulation supplies ordinary idempotent correction when e^2-e is nilpotent. The proof in the paper explicitly establishes the relevant nilpotent fiber ideal and writes its correction; the cited statement is not misrepresented as a theorem about inverse semirings. This HTML source has no locally downloaded byte hash.


## paper1_uniform_coefficient_literature

# Uniform coefficient category: primary-literature and scope comparison

Recorded UTC: 2026-11-25T05:31:30.740100+00:00

## Bounded searches

Before the complete mutual comparison closed on 25 November2026, the foundation worker used both search engines with the general queries `"inverse semiring" "coefficient" projective category admissible`, `"rings with several objects" "ideal" projective modules quotient`, `"inverse semirings" "projective" "category" coefficient`, and `"Rings with Several Objects" representable extension projective Murfet`. Individual search completion seconds were not separately clocked. These bounded searches located the ordinary preadditive-category formalism and did not locate this exact admissible-functional coefficient construction. This is neither an exhaustive literature claim nor a priority claim.

## Primary source read

Murfet, D. (2006, October5). *Rings with several objects*. Author-hosted notes,27pages. https://therisingsea.org/notes/RingsWithSeveralObjects.pdf . The primary PDF was opened in full in the web reader before the comparison and reopened during integration. A local primary copy was downloaded only outside the deliverable at `scratch_analysis/paper1_uniform_primary/Murfet_Rings_with_Several_Objects_2006.pdf`,344560bytes,SHA256 `b3c6a768e232102bc12b7f4c7bc885bdf98f5fafe61a2d5afecea4532f3021ab`.

Read scope: Section1,Definition1 printedp1 specifies covariant additive left modules; YonedaLemma1 printedp2 and Proposition3 with its complete proof printedpp3–4 give representables and small projectivity. Section4 printedpp23–25, including the complete displayed construction/proof of Theorem18 and Proposition19, gives extension, restriction, coextension and the explicit adjunction maps. These pages were reread from the downloaded PDF during integration. Theorem18 invokes earlier tensor-extension results, and Proposition19 invokes the earlier general adjunction formula; this event does not assert a new recursive reading of every earlier proof in those dependencies. The required extension-on-representables property is also checked directly by its adjunction and Yoneda, and the exact coefficient-category equivalence is proved in full in the new manuscript.

Murfet primarily writes right modules after Definition1; the left-module statement here applies his convention to the opposite category. For covariant representables H_x=C(x,-), Nat(H_x,H_y)=C(y,x), and the manuscript explicitly keeps this opposite in all corner formulas.

Mitchell, B. (1972). Rings with several objects. *Advances in Mathematics,8*(1),1–161. https://doi.org/10.1016/0001-8708(72)90002-3 . The existing source record identifies this as the classical formalism; full publisher text was not newly obtained in this search. No exact unchecked Mitchell theorem is used as the proof of the new coefficient construction.

## Exact comparison and residual gate

The ordinary small-category, representable, finite-projector and Kan-extension machinery is known. SZ1-112 explicitly constructs its category from admissible support functionals, proves the one-sided annihilator (ker pi)N=0, proves all exact mixed projective corners, and identifies the N-generated projective category with the canonical-ideal-generated amplitude category. The quotient C/N is diagonal with the stated upper-ring quotients.

SZ1-107 had already modeled every prescribed finite family and all its morphisms in one ordinary coefficient ring. SZ1-112 gives one category fixed by(T,L), independent of that family. It removes those family-dependent choices from the description but leaves projective support classification and arbitrary ordinary ideal-generated projective classification. In particular the singleton-support realization gives an arbitrary ordinary pair(R,I). No previously unresolved classification row is claimed closed, no general algorithm is asserted, and this record does not claim an automatic reset under the research stopping rule.

This is a source/scope event, not an independent mathematical-check event. The separate root statement-first proof and mutual comparisons are recorded at their actual times in the check notes.


## paper1_upper_jacobson_literature

# Compatible Jacobson quotient: exact primary-source comparison

25 November2026; /root/foundation, GPT-6 Astra Pro; effort not exposed. This is source/literature work, not an independent mathematical-check event. New quotient proof and separate-worker comparisons are recorded elsewhere.

## Primary material actually obtained and read

Katsov, Y., & Nam, T. G. (2014). On radicals of semirings and related problems. Communications in Algebra,42(12),5065–5099. Publisher contents page https://www.tandfonline.com/toc/lagb20/42/12 and the author institution's2014 publication list https://math.ac.vn/en/publications/2014 verify title, authors, volume and pages. The publisher article endpoint returned403. DOI10.1080/00927872.2013.833208 appeared in secondary metadata; its full publisher article was not obtained and no full published-text read is claimed. The manuscript cites the verified journal metadata and primary preprint URL.

Primary full preprint: https://arxiv.org/pdf/1206.1580, arXiv1206.1580v1,7June2012,42pages,408772bytes. Local outside deliverable: scratch_analysis/jacobson_primary/Katsov_Nam_2012.pdf. SHA256572e6bfde64532c1c71646be1543f56f16074068078776b4c31bee314a5649fd. Directly read: pp4–5 global-zero/semimodule/Bourne conventions; p12 irreducibility's cancellation; pp14–15 right-semiregularity/J and J_s definitions, Examples3.6–3.7 and Corollary3.9; pp32–34 all of Theorem5.8 and its proof; pp35–36 corner discussion and Proposition5.15 with proof. Earlier relevant pages were read02:17–02:28; pp14–15,32–36 were fully re-read during02:42–02:45, including the formerly truncated p34. The entire42-page paper has not been read.

## Exact comparison and ownership

The source's J and J_s are global semiring ideals with global-zero annihilators and Bourne ideal quotients. Its Theorem5.8 already gives matrix compatibility for J, J_s and the Brown–McCoy radical. Proposition5.15 already gives the J corner identity and its Bourne-quotient corner consequence. On ordinary rings both J and J_s equal the ordinary Jacobson radical. None of those ordinary or global identities is claimed as new here.

Our family C is a compatible family of subgroups of F(q), tested by ordinary Jacobson radicals only in upper-idempotent coefficient rings, and quotienting it retains Q. The new proof expressly establishes that phi(N_E) is an IDEAL of the unital enlargement; arbitrary radical subrings would not suffice. It proves a nonunital fixed-support radical kernel, exact-support lifting only under an extra upper-semiperfect hypothesis, and unconditional isomorphism lifting between existing projectives. It does not identify C with either established global radical, claim arbitrary-projective object lifting, or infer K0 injection merely from V injection. A separate three-support example has been sent for a fresh check; it is not admitted by this source comparison.

## Ordinary decomposition source

Krause,H.(2015), Krull–Schmidt categories and projective covers, Expositiones Mathematicae33,535–549, DOI10.1016/j.exmath.2015.10.001. Verified author PDF https://www.math.uni-bielefeld.de/~hkrause/krs.pdf; SHA25600f58b3b618864545f16fc2ecb5288670b7498d0fbd617cf591ff68e2c1c038d; Proposition4.1pp8–9, Theorem4.2 and Corollary4.3p9, Lemma3.6pp6–7. These exact primary locators were read earlier and are retained in records/paper1_root_semiperfect_literature.md and records/paper3_finite_ring_literature.md. The finite local-idempotent criterion, projective covers and uniqueness used in100/105 are ordinary known inputs. No assertion that every action ring is semiperfect is made.

## Bounded additional search and access limits

Both search engines were used for Jacobson/semiring/Morita-context context. Primary publisher abstract: Prasetyo,P.W., Marubayashi,H., & Wijayanti,I.E.(2022), On the restricted graded Jacobson radical of rings of Morita context, Turkish Journal of Mathematics46(5),1985–1993, DOI10.55730/1300-0098.3246, https://journals.tubitak.gov.tr/math/vol46/iss5/25/. Metadata and abstract were read; linked full PDF returned403 through both web and local requests, so no full-text proof or hash is claimed. Sands(1973), Radicals and Morita contexts, appeared as an ordinary antecedent in later references; its full primary paper was not obtained and is not used as a directly read proof source. No exact antecedent to the coefficient-diagram quotient/classification was verified in these bounded searches; this is not an absence-of-literature or priority claim.

No external PDF is copied into the deliverable. Source comparison does not add mathematical-check credit.

Record finalized UTC: 2026-11-25T02:47:37.441788+00:00

## Checked convention example update

The three-support example106 is now fully independently checked: operator fresh save02:52:47 before author access02:52:59, foundation full reverse read02:53:20. It is included as Example ex:jacobson-conventions. It separates the coefficient union, global J and global J_s, and their quotient conventions. This update records the mathematical result's status but does not duplicate the separate CHECK events.


## paper2_literature

# Paper2 literature continuation

## 24November2026,15:09UTC

Downloaded the exact primary PDF versions used for the Hurwitz/Witt/monoid arguments; hashes are in paper2_source_hashes.json. Johansson (2015), preprint arXiv:1309.2877v1, Theorem1 and pp3–4, supplies rigorous Euler–Maclaurin coefficient bounds; the manuscript proves its real-parameter specialization and the Rouché continuation lemma in full. Ramachandran (2015), arXiv:1407.1813v2, Theorem2.1,pp9–10, establishes the Witt-vector product mechanism; the present coefficient quotient and prime2obstruction are stated separately. Deitmar (2006), arXiv:math/0605429v3,Theorem1 andpp1–3, fixes finite type, torsion condition, and the printed positive zeta convention. These primary PDFs are cited and hashed, never copied into returned files.

Searched for Artin representation degree and tensor-product local factors with queries `site:math.mit.edu Artin L functions representation tensor product degree lecture notes` and `site:kskedlaya.org Artin L-functions representations dimension conductor`. Located Kedlaya's author-hosted ArtinL-function chapter and2015course notes, and Sutherland's Sato–Tate survey,Remark1.4. These are leads for an explicit representation-fusion pair; no result about a specific GCT arithmetic realization follows merely from the coefficient field.


## paper2_root_literature


## 2026-11-24, normalized Hurwitz series and antisymmetric residues

Root and separate worker opened the primary DLMF sections25.11 and25.4 after checking the algebra. Equations25.11.1 and25.11.17 give the defining series and parameter derivative;25.4.3–4 give the completed reflection identity. URLs: https://dlmf.nist.gov/25.11 and https://dlmf.nist.gov/25.4 . No external page or extraction is copied into the workbench. The ordinary-Dirichlet classification uses a direct uniqueness proof, and the tangency criterion is a local consequence of differentiated symmetry; neither is presented as a new priority claim.

Raw-byte provenance attempt: direct retrieval of bothDLMF HTML pages returned403 on24November2026. The primary equations were successfully read through the web tool. checks/paper2_hurwitz_primary_hashes.json records the failure; no hash is invented and no external text is included.


## paper3_arithmetic_literature

# Arithmetic intake literature

Serre, J.-P. (1977). *Linear representations of finite groups* (L. L. Scott, Trans.). Springer. https://doi.org/10.1007/978-1-4684-9458-7 . Exact locators checked in the primary book scan: Section2.3, Theorem4 and Corollary2, printed p.16 (PDF p.24), and Section2.5, Theorem6, printed p.19 (PDF p.27). The former gives multiplicities and character uniqueness; the latter gives the orthonormal basis of class functions. Publisher metadata and the translation credit were also checked. The scan was accessed at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-Reps.pdf on24November2026.

The manuscript input character_support.tex applies these classical facts to a separately chosen support set and the functorial zero adjunction. It makes no novelty claim for character inversion and no new claim of Monster or umbral module existence.

The remaining analytic CUE, compact-measure, Bernstein, principal-part and finite-matrix assertions are inventoried with exact source labels but are outside the R_0 series. This intake does not provide a new literature or proof verification for every excluded assertion. Classical norm multiplicativity is used only for rings of integers in the retained Dedekind result; the broader source formulation is refuted by an explicit finite-ring example.


## paper3_finite_ring_literature

# Finite-ring primary literature

Krause's author preprint and Lam's Bass survey were downloaded and read on2026-11-24. Full access scopes, exact page/theorem locators, ordinary noncommutative-ring qualifications, bibliography, hashes and the elementary primitive-projective/simple-top deductions are in `checks/paper3_finite_ring_primary_sources.md` and its JSON companion. No source copy or extraction is included in the deliverable. This is literature verification, not a new independent proof event for the finite inverse-semiring classification.


## paper3_hecke_word_literature

# Primary sources for the integral Hecke word-order result

Search and inspection date: 2026-11-24. No novelty or priority claim is made.

1. Blasiak, J., Mulmuley, K. D., & Sohoni, M. (2013). *Geometric complexity theory IV: Nonstandard quantum group for the Kronecker problem* (Version4), arXiv:cs/0703110v4. https://arxiv.org/abs/cs/0703110v4. The arXiv record verifies the three authors, version date6 June2013, and145-page final-journal-version description. The full primary PDF was downloaded outside the deliverable and inspected. Section3, equation(22), pp20–21, gives the free Hecke basis and quadratic convention. Section3.1 gives the lower and upper simple Kazhdan–Lusztig generators used here. Definition11.1, equation(93), p59, is the P-generator definition of the nonstandard Hecke algebra. Page59 was also rendered and visually inspected. Manuscript bibliography key: `BSM2013`; exact bibitem fragment: `checks/paper3_hecke_word_bibliography.tex`.

2. Mulmuley, K. D. (2008). *Geometric complexity theory VIII: On canonical bases for the nonstandard quantum groups* (Version2), arXiv:0709.0751v2. https://arxiv.org/abs/0709.0751v2. Section5.2 was opened in the primary arXiv text; its rank-four computation supplies only the trivial-block element and describes the remaining basis computation as incomplete. Existing manuscript key: `Mulmuley`. This locator distinguishes a fully specified word algebra from unavailable canonical-basis input.

The new text proves the finite torsion-free integral word order, faithful scalar extension, generic word basis, integral regular characteristic polynomials, and a selected-minor localization directly. It uses standard finite-module and field-descent arguments, all reproduced in the proof. No claim about the exact publication history of that assembled statement follows from this limited literature search. In particular the November source's numerical nonfreeness assertion is not adopted or independently verified here, and no individual irreducible-character descent is inferred from the regular trace statement.

3. The concrete rank-four certificate additionally uses Blasiak, Mulmuley and Sohoni (2013), Section11.8, pp67–68. The primary text explicitly gives generic dimension114 and the complete simple-module dimensions1,2,3,6,5,5,2,3,1; it also reports a word basis with maximum word degree9. The operator and root independently opened this passage and matched the Section3.1 normalization. Root's verified primary PDF SHA256 is cc28f69ca06c0c5e43c30b2cf801a1134712a596c87e74bff2ade1c49fb41638. The dimension upper bound is cited background; the new modular certificate supplies independent lower-bound/nonvanishing evidence and a finite polynomial localization. No generic upper bound is inferred from the modular rank.


## paper3_hexagon_foundation_literature

# Public foundation version comparison

On 2026-11-24T20:08:15.749784+00:00, all ten pages of Hexagon 2611.00993v1 were read and compared with `ours/foundation/h22_note_v3.tex`. Exact page/statement locators and SHA-256 values are in `checks/paper3_hexagon_foundation_comparison.md` and its JSON companion. Public Theorems 1–3 and Corollary 4 and all their proof content are unchanged. Public Section 1.3 p3 and Remark 5.4 p8 correct the ordinary-module projectivity interpretation, agreeing with SZ1-014; Remark 5.4 adds the zerosumfree-free-module proof. Other changes concern date, provenance, explicitly narrowed historical computation scope, Crossref-method disclosure, and WB-0008 links.

Citation: *Spectrum, semimodules and projectives of the inverse semiring R0 of Faul, Goswami, Joubert and Manuell*. (2026, November 24). Hexagon, 2611.00993v1. https://hexagonmath.org/2611.00993v1. The displayed author line and PDF Author metadata are empty; the site contributor is user Alderliefste, which is not treated as an author attribution. No causal inference about this run and deposit is made. This is an original comparison record, not a copied source or historical-check replay.


## paper3_literature

# Paper 3 literature searches

All searches in this fragment were performed on 2026-11-24. Primary sources were opened for assertions used in the paper. Fetched PDFs remain outside the deliverable; addresses, SHA-256 values and used pages are in paper3_source_hashes.json. No priority claim is made.

1. Searches for Connes–Consani–Marcolli semilocal adele examples located *The Weil proof and the geometry of the adeles class space*, arXiv:math/0703392v1. The correct locator is §10.2, equations (10.10)–(10.19), not the §8.2 locator in one earlier project note. This gives the earlier local geometric example.
2. Searches for Brown–Green–Rieffel stable isomorphism located the original 1977 Pacific Journal paper. Theorems1.1–1.2, pp350–352, justify stable Morita transport.
3. Searches for Blackadar mapping tori and Busby sums located the author's second-edition electronic text. Theorem9.3.1 and §9.3.2 pp67–68 give the six-term/exponential formula; Proposition10.4.1 p76 gives the mapping-torus map; §§15.3 and15.6 give pullback and stable sum.
4. Searches for Green free proper transformation-group actions located the primary 1977 Pacific Journal paper, Theorem14 and Corollary15 pp88–91. This replaces a less exact generic citation to Green1978.
5. Searches for profinite translation, coinvariants, Haar normalization, odometers and generalized Bunce–Deddens algebras found the standard finite-orbit method. The later paper of Guo, Proietti and Wang, *A geometric Elliott invariant and noncommutative rigidity of mapping tori* (JFA2024; arXiv2207.06840v2), §4.4 / published Proposition4.10, computes Haar trace ranges using reciprocal finite indices. It is a related known ingredient, not a proof of the semilocal matrix formula.
6. Searches for semilocal K-theory, at-most-one-zero adeles, and Connes–Consani unit quotients located Connes's September2024 Mondovi slides. Slides45–49 explicitly use the compact-unit quotient. Following Consani's author publication page located *Knots, primes and class field theory*, arXiv2501.06560v1 (2025), §5.3 Proposition5.4 pp23–24 and §5.4 Lemmas5.5–5.6 pp25–28. This is the closest primary source: it proves the scalar two-prime K0=Z³,K1=Z² calculation and the reflection model. Credit and title were revised accordingly. The 2024 predecessor arXiv2401.08401 states the earlier scalar computation.
7. General searches for “one-zero algebras”, “boundary K-theory semilocal”, “adele K-theory coinvariants” and the same topics restricted to hexagonmath.org did not locate the full unit-fibre finite matrix or the 2,3,5 torsion calculation. Cuntz–Li ring C*-algebra papers concern affine adele actions and were not treated as identical objects. Negative search results do not establish novelty.
8. A stronger-engine verification search for adele K-theory coinvariants, semilocal K-theory Connes Consani units, Bunce–Deddens Haar coinvariants, and Hexagon adele K-theory confirmed the foregoing distinctions. No exact antecedent for the assembled arithmetic matrix or the full K1 coboundary-lift presentation was found in the pages opened.

Literature status: compact-unit scalar case and reflection model are known; mapping-torus, imprimitivity and extension machinery are known. The paper provides explicit formulas and proofs for the full unit-fibre boundary, arithmetic finite reduction, torsion example and coherent chosen extension maps. The exact literature status of those assembled refinements is not established by the finite search; the text makes no claim of priority or correction of a published theorem.


## paper3_packet_literature

# Packet intake literature and scope

The Stacks Project Authors. (2026). *The Stacks Project*, Lemma20.12.3, Tag09SY. https://stacks.math.columbia.edu/tag/09SY . Primary locator checked on24November2026: flasque sheaves are acyclic. The vector-tail argument additionally verifies surjectivity of the map on global sections; that step is needed to conclude vanishing in degree one.

The Stacks Project Authors. (2026). *The Stacks Project*, Section6.17, Tag007X, especially Lemma6.17.2. https://stacks.math.columbia.edu/tag/007X . Primary locator checked on24November2026: sheafification preserves stalks. The particular discrete-support product construction is proved directly in the manuscript.

The Boolean-coordinate, truncated-jet, finite-orbit and endpoint calculations are elementary special constructions with full proofs in Paper2 and the independent intake note. No priority or novelty claim is made for them. The inverse-semiring input is credited in Papers1–2 to the primary zero-adjoined-ring literature.

The analytic products, Taylor factors, spectral coordinates, heat traces and spline statements listed in paper3_packet_other_results.md are outside the R_0 series. This intake does not supply a fresh literature or proof audit of every excluded result. Their source occurrences remain individually locatable in paper3_packet_crosswalk.tsv; they are not silently presented as new or checked results.

Neukirch, J. (1999). *Algebraic number theory* (N. Schappacher, Trans.). Springer. https://doi.org/10.1007/978-3-662-03983-0 . Exact mathematical locators: Chapter VII, Section5, Proposition5.2 and Corollary5.11. The former gives absolute convergence and the Euler product; the latter gives continuation to C minus1 and the simple pole residue. Publisher metadata and the mathematical book text were checked on24November2026. The norm-cutoff proof for all nonnegative shifts is a new derivation in this workbench, not a claim quoted from this reference.


## paper4_literature

# Paper 4 literature and live-source record

Research date: 24 November 2026, UTC. Researcher: GPT-6 Astra Pro, effort setting not exposed. This fragment is to be merged into the series `LITERATURE.md`. It records source comparisons, not an assertion of exhaustive coverage or priority. All public documents below are cited by link; none is copied into the workbench.

## Search history and retrieval limits

The initial searches and openings took place before 14:03 UTC. The public-node attempts specifically occurred in the recorded window 13:35–13:55 UTC. Individual seconds were not captured for those early calls, and are not reconstructed. The following exact fresh searches were repeated at 14:05:37 UTC using the primary-coverage search engine:

1. `monotone Boolean circuits C4 free graph edge function vertex cover exact complexity Jukna`: returned Jukna's single-level paper, its SIAM version, and the ECCC graph-complexity report. The single-level gap concerns other graphs; it does not settle the four-cycle-free exact count.
2. `Schnorr Jerrum Snir monotone circuit quadratic edge polynomial vertex cover`: returned Jukna's author commentary and tropical-complexity literature. Primary papers were opened separately below. No exact coefficient-independent graph formula was established as new from this search.
3. `"On the complexity of slice functions" Berkowitz Wegener`: returned the publisher entry and the full Wegener article. This corrected the bibliographic volume to 38 and established the exact theorem locator.
4. `site:pequalnp.com "L-meta-647" OR "L-meta-608" OR "L-meta-612"`: returned no live node-level records in the combined output. Absence from this search is not evidence about checker status.

At approximately 14:06–14:09 UTC, three further exact searches were made:

5. `"Notes on Boolean read-k and multilinear circuits" pdf`: returned the author's 20-page manuscript, ECCC TR22-094, arXiv:2207.08701 and the journal entry. The manuscript was opened and its Lemmas 1–2 and Theorem 1 read. This is decisive prior literature for the support criterion and the lower-envelope reduction.
6. `Jukna edge functions C4 free monotone circuits "edges" lower bound`: returned author material and graph-complexity references. No unrestricted exact count was located.
7. `Amano Maruoka quadratic Boolean functions AND gates C4 free`: returned the journal DOI, conference reference and authors' publication list. The DOI redirected to an inaccessible Springer page. No theorem of that paper is used as an unchecked premise.

Earlier searches covered the terms `Schnorr 1976 monotone additions`, `Jerrum Snir 1982 semiring exact complexity`, `Berkowitz 1982 monotone slice functions`, `Valiant negation exponentially powerful`, and recent OpenAI/Anthropic algebraic lower bounds. Their exact query strings were not preserved; the verified source findings and locators are recorded below. This distinction prevents a later audit from mistaking reconstructed topic descriptions for exact query logs.

The web reader exposes text and PDF pages, but not downloadable raw bytes in this environment. Direct local HTTP retrieval of the public project returned 403. Therefore SHA-256 values for newly opened web PDFs have not been fabricated. Hashes of the attached source files and of original verification programs are handled in the series manifest. Raw-source hashing of remote literature remains a retrieval limitation.

## Inverse semirings and the support model

- Faul, P. F., Goswami, A., Joubert, G., & Manuell, G. (2024). *The case for inverse semirings*. [arXiv:2411.12318](https://arxiv.org/abs/2411.12318). Attached LaTeX read. Definition 3.6 is the zero-adjoined ring. Proposition 5.2 identifies the free commutative inverse semiring with `Z_0[x]`; the paragraph following it explicitly identifies the ring reflection and the finite exponent-set idempotents. Proposition 6.1 gives inverse addition for semimodules. Thus the free-polynomial and support construction is prior work, not a new theorem here. The arbitrary commutative-monoid presentation is given explicitly as a compatible specialization/generalization of those data.
- Caviglia, E., Faul, P. F., Manuell, G., & Mesiti, L. (2026). *Clifford semigroups and the monoidal Grothendieck construction*, v2. [arXiv:2607.12944](https://arxiv.org/abs/2607.12944). Attached LaTeX read, especially §§4–5 and §8. Theorem 8.5 identifies inverse semirings with an idempotent semiring and a lax monoidal group-valued functor; Remark 8.7 treats the two-idempotent construction. The formulas in Paper 4 identify the data `S ↦ R^S` and `f ↦ F(f)`. The paper is not used as a classification of semimodules.

## Monotone circuits, read degree, and exact support

- Schnorr, C. P. (1976). A lower bound on the number of additions in monotone computations. *Theoretical Computer Science, 2*(3), 305–315. [DOI](https://doi.org/10.1016/0304-3975(76)90083-9); [author-hosted scan](https://web.vu.lt/mif/s.jukna/boolean/Schnorr-1976.pdf). Publisher metadata and full scan opened. The scanned theorem numbering has imperfect OCR, so the manuscript does not invent a theorem locator. This is prior support-based addition-count literature; its precise theorem is not assumed in the self-contained graph proof.
- Jerrum, M., & Snir, M. (1982). Some exact complexity results for straight-line computations over semirings. *Journal of the ACM, 29*(3), 874–897. [Author PDF](https://snir.cs.illinois.edu/listed/J7.pdf). §2.1, pp. 876–877, distinguishes formal polynomial representation from equality as functions; in particular Boolean powers need not be equal as formal polynomials. Theorems 3.2–3.4 and Corollary 3.5, pp. 882–884, provide parse/decomposition lower bounds. No claim is made that this search found the exact graph-count formula there.
- Jukna, S. (2015). Lower bounds for tropical circuits and dynamic programs. *Theory of Computing Systems, 57*, 160–194. [ECCC TR14-080 revision 1](https://eccc.weizmann.ac.il/report/2014/080/revision/1/); [PDF](https://eccc.weizmann.ac.il/report/2014/080/revision/1/download/). Full PDF opened. §§3–4 and Theorem 9 distinguish arithmetic, tropical and Boolean equivalence, with a homogeneous-target comparison. The version's multilinearity qualifications matter. Theorem 12 treats separated polynomials, Theorem 18 a freeness condition, and Lemma 22 rectangle decompositions. Only the model comparison is cited in Paper 4.
- Jukna, S. (2006). Disproving the single level conjecture. *SIAM Journal on Computing, 36*(1), 83–98. [DOI](https://doi.org/10.1137/S0097539705447001); [author manuscript](https://web.vu.lt/mif/s.jukna/ftp/single1.pdf); [ECCC TR05-021](https://eccc.weizmann.ac.il/report/2005/021/). Theorem 2.1, p. 4 of the author manuscript, gives quadratic Boolean functions with linear unrestricted monotone circuits and a much larger single-level requirement. Those examples are not asserted to be four-cycle-free. The theorem blocks a general unstated flattening argument. The paper's Boolean-sums discussion also warns against eliminating arbitrary AND gates without proof.
- Jukna, S. (2022). *Notes on Boolean read-k and multilinear circuits*. [ECCC TR22-094](https://eccc.weizmann.ac.il/report/2022/094/); [author manuscript](https://web.vu.lt/mif/s.jukna/ftp/readk-submit.pdf). Opened 24 November at approximately 14:07 UTC; ECCC record reopened at 14:09:45 UTC. Lemma 1, p. 5, is exactly the general support/prime-implicant criterion used for `Sup(G)`. Definition 1, p. 6, defines witness read degree. Lemma 2 and Theorem 1, p. 7, prove the lower-envelope reduction and equality of read-1 complexity with arithmetic complexity **up to positive coefficients** for homogeneous support. The arithmetic complexity there minimizes over similar polynomials, not one prescribed coefficient list. Paper 4's revised proof therefore gives a coefficient-independent quadratic bound before applying that reduction. Lemma 9, pp. 17–18, gives an exponential read-1/read-2 gap for a different family, so read degree is substantive. No priority is claimed for the reductions.
- Amano, K., & Maruoka, A. (2004). On the monotone circuit complexity of quadratic Boolean functions. *Algorithms and Computation: ISAAC 2004, Lecture Notes in Computer Science, 3341*, 28–40. [Publisher volume](https://doi.org/10.1007/b104582); [chapter DOI](https://doi.org/10.1007/978-3-540-30551-4_5). The publisher confirms the title, authors, pagination, and 15th symposium. Jukna's single-level paper, §3, manuscript p. 11, explicitly attributes the all-binary-gate **single-level** lower bound C_single(f_G) ≥ |E| for K_2,2-free graphs to this paper. We now cite that restricted result through Jukna, not as a firsthand theorem-level reading of Amano–Maruoka. Jukna pp. 4–6 also distinguishes their total-gate 29/28 gap for multiple outputs from his single-output result.
- Amano, K., & Maruoka, A. (2006). The monotone circuit complexity of quadratic Boolean functions. *Algorithmica, 46*, 3–14. [DOI](https://doi.org/10.1007/s00453-006-0073-0). Publisher metadata reopened and confirms publication 3 July 2006 and September 2006 issue; the previously uncertain 2006/2007 date is corrected to 2006. The abstract concerns AND count versus single-level AND count, and a set of quadratic functions for the total-gate comparison. The journal full text was not recovered. The IPSJ precursor [record](https://ipsj.ixsq.nii.ac.jp/records/31828) has the English title *On the Monotone Circuit Complexity of Quadratic Boolean Functions*, date 14 October 2004, and file IPSJ-AL04097006.pdf. Its record and [download](https://ipsj.ixsq.nii.ac.jp/record/31828/files/IPSJ-AL04097006.pdf) returned HTTP 429 in the 14:33–14:36 UTC reading window.
- Jukna, S. (2004). *On graph complexity*. [ECCC TR04-005 revision 1](https://eccc.weizmann.ac.il/report/2004/005/revision/1/download/). Full 25-page manuscript opened. Definition 1.1, p. 2, requires graph representation to be correct only on pairs, which is weaker than computing the edge function on all assignments. Theorem 7.3, p. 18, gives monotone formula length at least |E|/2 and monotone depth at least log_2|E|−1 when there are no triangles or four-cycles (indeed for functions accepting edges and rejecting independent sets of size at most twice the maximum degree). This is a formula/depth theorem, not the desired gate-count theorem for shared-wire DAGs. The lower bound is relevant prior work, not a solution of L-meta-608.
- Jukna, S. (2006). *Graphs and circuits: Some further remarks*. [Author PDF](https://web.vu.lt/mif/s.jukna/ftp/dagstuhl2006.pdf). Opened in the 14:38–14:40 UTC window. The introduction and Definition of graph representation again make the pair-only semantics explicit. Theorem 2.1 uses XOR/AND to represent a matching and does not compute its edge function on all assignments. Thus its logarithmic AND count is not a counterexample to the edge-function conjecture.

## Cancellation, clique, and slice functions

- Valiant, L. G. (1980). Negation can be exponentially powerful. *Theoretical Computer Science, 12*, 303–314. [DOI](https://doi.org/10.1016/0304-3975(80)90060-2); [full scan](https://web.vu.lt/mif/s.jukna/boolean/Valiant-negation.pdf). Opened and reread at approximately 14:04 UTC. Theorem 1, p. 307, is the monotone lower bound for triangular-grid perfect-matching polynomials; the introduction explains the efficient Pfaffian computation with subtraction. Lemma 1, p. 305, is the positive homogeneity principle. This already supplies classical arithmetic cancellation separations; it is not a proof of an unrestricted Boolean lower bound.
- Alon, N., & Boppana, R. B. (1987). The monotone circuit complexity of Boolean functions. *Combinatorica, 7*, 1–22. [DOI](https://doi.org/10.1007/BF02579196); [author PDF](https://web.math.princeton.edu/~nalon/PDFS/Publications/The%20monotone%20circuit%20complexity%20of%20Boolean%20functions.pdf). Theorem 3.9, p. 12, gives the clique lower bound used in the corrected supported-zero statement. The circuit-model translation is proved in Paper 4; the clique lower bound is cited as external background, not reproved.
- Wegener, I. (1985). On the complexity of slice functions. *Theoretical Computer Science, 38*, 55–68. [DOI and publisher](https://doi.org/10.1016/0304-3975(85)90209-9); [scan of article](https://www.mobt3ath.com/uplode/book/book-95108.pdf). Theorem 2.6 and Remark 2.7, pp. 57–58, establish the monotone slice simulation and attribute the original construction to Berkowitz, with a sharper overhead than the elementary cubic proof in Paper 4. The publisher's abstract also cautions that certain canonical clique slices have linear complexity.
- Berkowitz, S. J. (1982). *On some relationships between monotone and non-monotone circuit complexity*. University of Toronto technical report. This original report was not retrieved. Attribution is supported by the contemporary Wegener paper; the manuscript does not claim to have read the report or invent its theorem number.

## Recent algebraic complexity context

- Anthropic. (2026, November 23). *VP ≠ VNP over every field*. [Hexagon 2611.00954v1](https://hexagonmath.org/2611.00954v1); [PDF](https://hexagonmath.org/pdf/2611.00954v1). The first sections, Theorem 1.1 and §1.3 were opened. The preprint states lower bounds for Hamiltonian-cycle polynomials over every field and the permanent outside characteristic two, with an accompanying formalization. Its §1.3 explicitly specifies formal polynomial identity. Paper 4 reports this model comparison and does not depend on or claim to audit the 70-page proof.
- OpenAI. (2026, September 24). *A cubic lower bound for border determinantal complexity of the permanent*. [Formalization scope and paper link](https://github.com/openai/math/blob/main/lean/docs/108.md). Primary repository opened, then reread at approximately 14:04 UTC. The scope states exact and border determinant lower bounds over the complex numbers, `n ≥ m^3/(5529600e)` for `m ≥ 1408`, and distinguishes the algebraic branching-program corollaries from the Lean statements. Paper 4 cites only the model-specific neighboring result, not a Boolean consequence. The paper's GitHub PDF page was also opened; the scope document is the verified source for the explicit constant.

## Public node readings

Historical baseline: attached project map and proof-graph table, dated 23 November 2026. L-meta-606, L-meta-608, L-meta-612 and L-meta-647 are conjectural there; L-meta-649 is checked there. The map is by Claude Opus 5.5 at effort high and its one-sided proof sketch by Claude Opus 5.5 at effort max. These statuses are historical evidence, not live verification.

Live attempts, 24 November 2026, 13:35–13:55 UTC:

- [Homepage](https://pequalnp.com/), [board](https://pequalnp.com/board), [how](https://pequalnp.com/how), [feed](https://pequalnp.com/feed), and [join text](https://pequalnp.com/join.txt) opened. The reader exposed general/project text and dynamic placeholders, not the cited node records.
- [Public proof repository](https://github.com/brilliant-hq/pequalnp-proofs) opened. Its README describes a pinned Lean checker; this does not certify any particular requested node.
- Direct raw and GitHub blob requests for the proposed `L_meta_647.lean`, `L_meta_608.lean` and `L_meta_649.lean` paths were disabled or unavailable through the retrieval interface. A path guessed from an identifier is not evidence that the file exists.
- Local HTTP retrieval of the homepage returned 403. No signed-in browser session was probed, and no project enrollment, issue, lease or submission was made.
- The fresh 14:05:37 UTC search for the cited identifiers produced no live node records.
- Direct readings of `https://pequalnp.com/lemma#L-meta-647`, and the analogous 608, 612 and 649 pages, observed at **14:30:34 UTC**, returned only “Reading the record” templates. The public `/live` page likewise exposed no node data. The GitHub repository root opened, but its Lean subdirectories and a read-only contents-API request were unavailable. The public join instructions describe actions which lease work; none was invoked. No enrollment or submission was made.

Conclusion: the mathematical theorem corresponding to the stated degree-one formulation is proved in the manuscript, while the present external checker status is **unretrieved**. The unrestricted conjectures are unresolved by this work regardless of external status.

## Literature status used in the register

The zero-adjoined construction, its free polynomial structure, the support criterion, the lower-envelope reduction, read-degree terminology, slice simulation, and classical monotone lower bounds are known and credited. The coefficient-independent quadratic count and the fully specified one-sided exact count are given with complete proofs, but the searches do not establish their priority. They are marked as checked formulations/derivations with novelty undecided, not advertised as new theorems. The distinctions between formal coefficient zeros and semantic output zeros, and between cancellation and exponent identification, are explicit corrections to the project's proposed interpretations.

## Additional exact query log, 14:29–14:46 UTC

The following strings were issued, in this order within each batch. Primary papers and publisher records were opened where available; secondary search hits were used only as leads.

- `"L_meta_647"` and direct public node URLs listed above.
- `Amano Maruoka "quadratic" "pdf" circuits`; `"The Monotone Circuit Complexity of Quadratic Boolean Functions" pdf amano`; `"monotone" "circuit" "forest" "quadratic"`.
- `"quadratic Boolean" "disjunctive" complexity`; `"monotone circuits" "four-cycle" edge`; `"quadratic" "C4-free" "circuit"`; `"monotone" "graphs" "number of OR" gates quadratic`.
- `"conjunctive complexity" "cycle"`; `"conjunctive complexity" "bipartite"`; `"quadratic Boolean functions" "star"`.
- `Kazuyuki Amano publications quadratic Boolean 2006 pdf`; `Akira Maruoka quadratic functions Algorithmica pdf 2006`; `"31828" "IPSJ-AL04097006"`; `"quadratic Boolean" "vertex cover"`.
- `"On the Monotone Circuit Complexity of Quadratic Boolean Functions" "28–40" 2004 Springer`.

Find operations in Jukna's single1.pdf for `cover`, `cycle`, and `Amano` exposed the restricted-model attribution on manuscript p. 11. The query `cycle` itself had no text match. None of these searches establishes exhaustive priority or retrieves a counterexample for a C4-free edge function.

## Public-node retry and repository address, 15:12–15:23 UTC

At approximately15:12 UTC the public join text linked the repository `open-goat/pequalnp-proofs`, whereas the earlier attachment and index used `brilliant-hq/pequalnp-proofs`. This was verified again by opening [join.txt](https://pequalnp.com/join.txt) at **2026-11-24 15:23:14 UTC**, lines81–84 and115–123. The new repository root exposed only GitHub navigation/error text; its Outside directory was unavailable. This is an observed repository address in public instructions, not evidence of any node's state. The instructions also describe actions that enroll or lease work; none was performed.

At15:22–15:23UTC, the four exact queries `"L-meta-608" "pequalnp"`, `"L-meta-612" "pequalnp"`, `"L-meta-647" "pequalnp"`, `"L-meta-649" "pequalnp"` were run with a2-day freshness filter. They returned general repository and third-party activity summaries, without an authoritative record for the requested nodes. A third-party search lead named the public read-only JSON address [data.pequalnp.com/data/desk/gaps.json](https://data.pequalnp.com/data/desk/gaps.json); opening that primary endpoint returned “not accessible via this tool.” The lead is not used as technical evidence.

Direct reads of the four conventionally named raw Lean files under `https://raw.githubusercontent.com/open-goat/pequalnp-proofs/main/lean/PEqualNP/Outside/`, observed at **2026-11-24 15:23:25 UTC**, all returned DisabledError. These requests do not establish either existence or absence of the files. Present statuses of608,612,647,649 therefore remain unretrieved. The historical23November statuses and the independently proved mathematical statements remain separately identified.

Alon–Boppana's author-hosted PDF was also reopened at approximately15:15 UTC. Theorem3.9 on printedp12 gives an exponential clique monotone lower bound with the clique parameter of order(m/log m)^(2/3) and exponent of order(m/log m)^(1/3). The source was not used to infer any general Boolean lower bound or polynomial upper bound. The manuscript's conditional reference to the families covered by that theorem avoids introducing a misremembered parameter range.

## Equality and factor-count follow-up,15:50–15:52UTC

Queries: `"monotone arithmetic" "vertex cover" quadratic`; `"arithmetic circuits" "quadratic" "NP-hard" monotone`; `"quadratic polynomial" "circuit" "four-cycle"`; `"monotone" "star" "vertex cover" circuits`. The search returned general arithmetic-complexity papers and graph-representation discussions, but no exact prior statement of the new two-witness or factor-product refinements. This is not an exhaustive priority determination.

Opened the author-hosted first chapter of S.Jukna(2012), *Boolean Function Complexity: Advances and Frontiers*, Algorithms and Combinatorics27, Springer, DOI10.1007/978-3-642-24508-4_1, [chapter PDF](https://web.vu.lt/mif/s.jukna/boolean/chapter1.pdf). Printedpp42–43 explicitly define graph representation using only size-two assignments; this differs from computing f_G on all assignments. Printedp46 states the classical exact transposition principle for Boolean OR networks, credits Bordewijk(1956), Lupanov(1956), Mitiagin–Sadovskii(1965), and Fiduccia(1973) for bilinear circuits over commutative semirings, and proves it by reversing wires and counting edges minus vertices. This is relevant prior context for Paper4's degree-one transpose lemma; the original historical papers have not yet been opened. Printedpp45–47 discuss magnification for the weaker representation model, and do not yield the unrestricted edge-function lower bound. No current novel-status claim is based on these searches.

## Transposition, canonical determinant, and final public retry,16:08–16:17UTC

The Jukna2012 author-hosted chapter was reopened and its printedp46 transposition proof read in full. The exact OR-network reversal is now cited in the manuscript before lem:transpose. Our proof trims isolated marked variables and explicitly counts reads; it does not rely on an unqualified matrix dimension formula in the presence of unused rows or columns. The historical authors are attributed through Jukna; their original papers were not retrieved.

The Jerrum–Snir author PDF was reopened and §4.3, printedpp887–889, read. It proves the stronger exact permanent multiplication bound n(2^(n−1)−1) by the support/content method. Paper4's canonical-formal-determinant proposition uses a complete elementary binomial support-cover proof instead, with free scalar constants and inverse gates accounted for. Its novelty status is a known monotone-permanent consequence, not a new lower bound. The exact occupied-support qualifier prevents confusion with polynomial-size arbitrary lifts of the ordinary ring determinant. The foundation worker provided a fresh statement-only proof before any circuits-worker proof exposure; the full arguments were then compared.

The current node queries were repeated with a one-day freshness filter: `"L-meta-608" "pequalnp"`, `"L-meta-612" "pequalnp"`, and `"L-meta-647" "pequalnp"`. This batch returned unrelated matches, which provide no evidence of any node's status. Primary read-only openings of https://data.pequalnp.com/data/desk/gaps.json and https://github.com/open-goat/pequalnp-proofs again returned, respectively, tool inaccessibility and GitHub navigation with an action-unavailable message. These outputs were observed at **2026-11-24 16:17:27 UTC**. The public repository address is verified as open-goat, but the mathematical node statuses remain **unretrieved**. No enrollment, lease, mutation, PR or submission was attempted.

## Public-node observation18:28:54UTC

On24November2026 at18:28:54UTC, direct primary openings of the608,612,647 and649 node URLs again returned only the shared “Reading the record” template. The page now also displayed a generic checker-catching-up banner; this is not evidence about any particular node. The primary read-only gaps.json endpoint remained inaccessible through the retrieval tool. The one-day queries `"L-meta-608" "pequalnp"`, `"L-meta-612" "pequalnp"`, and `"L-meta-647" "pequalnp"` returned repository documentation and unrelated third-party activity records, not authoritative statuses for these nodes. Search-result third-party job instructions were not followed and are not technical evidence. No enrollment, lease, mutation or submission occurred. Current608/612/647/649 statuses remain unretrieved. Retrieval refs: turn651053343view0–view4 for the primary openings; turn651053343search0 for the repository documentation.


## Follow-up literature and public-status retrieval — 24 November 2026,20:09:32UTC

The additional targeted read-k/C4-free literature search is recorded in `checks/paper4_literature.md`, including primary Jukna pages opened at20:01:18UTC and the scope distinction from the STACS2026 conditional-hardness paper. It makes no priority claim and supplies no unrestricted edge-circuit theorem.

At20:09:32UTC, direct openings of https://pequalnp.com/lemma#L-meta-608 , https://pequalnp.com/lemma#L-meta-612 , https://pequalnp.com/lemma#L-meta-647 , and https://pequalnp.com/lemma#L-meta-649 again returned the common loading template without individual node records. The primary read-only endpoint https://data.pequalnp.com/data/desk/gaps.json remained inaccessible through the retrieval tool. Simultaneous exact-node searches with a one-day freshness filter returned no additional authoritative status records in the tool output. No enrollment, lease, mutation or submission was performed. All four current statuses remain unretrieved; the23November historical statuses remain separately credited. Primary retrieval refs: turn180429265view0–view4.

## Primary threshold-two follow-up 2026-11-25T04:26:23.127662+00:00

Root supplied the primary publisher/full-version result. Circuits opened https://arxiv.org/html/2603.28954v2 and read Section3.4(Theorem6) and complete AppendixA.2 through the search tool on25November2026 about04:25UTC. The upper bound2n+sqrt(2n)+O(n^(1/3)) and threshold-three subcircuit are explicit. Manuscript includes only this construction and its C4-containing complete-graph scope. The privately corrected Sergeev single-level lower bound mentioned by that source is not imported as an independently checked premise. Publisher DOI10.4230/LIPIcs.SAT.2026.23,Theorem9; full-version Theorem6. This is literature/context retrieval, not a new theorem proof event.


## paper4_root_attachment_literature

# Literature update for the four-witness attachment refinements

Recorded 2026-11-25T03:07:20.684828+00:00, root, GPT-6 Astra Pro, effort not exposed. This is a search/comparison record, not another proof event.

At03:06:31UTC on25November2026, engine1 queries were monotone circuits / four-cycle / graph edge function (arXiv, ECCC, Jukna's author domain) and edge functions / Boolean / quadratic / circuit / Jukna (arXiv, ECCC, Hexagon). The searches recovered Jukna's already-known *Disproving the single level conjecture*: ECCC TR05-021, https://eccc.weizmann.ac.il/report/2005/021/; the author page https://web.vu.lt/mif/s.jukna/papers/single.html; and the primary journal page https://epubs.siam.org/doi/abs/10.1137/S0097539705447001. The earlier full primary checks and locators in the existing circuit literature record remain authoritative. This search exposed the abstracts/metadata again and is not relabeled as another full proof read.

That work supplies the established warning that arbitrary monotone quadratic Boolean functions can differ sharply from a single-AND-level circuit model. The new attachment results concern exact original deleted-gate profiles in four-cycle-free graphs; they neither assume single-level normalization nor assert a lower bound for all monotone quadratic functions. No exact antecedent for116–121was verified by these bounded searches, which is not a novelty or priority claim.

A keyword hit, Hexagon2611.00751v1, *Four-cycles one edge above the extremal threshold*, https://hexagonmath.org/pdf/2611.00751v1, concerns extremal graph supersaturation. Its abstract was exposed but no circuit theorem or proof input was recovered from it; it is not used as a dependency and is not treated as a circuit predecessor merely because of the shared four-cycle keyword. No new external PDF or extraction is included in the deliverable.

## 25November2026,03:48UTC: bounded follow-up for122–124

Exact-topic searches for C4-free monotone circuits and additions, monotone AND counts and vertex covers, and the single-level conjecture returned the already compared Jukna primary sources (author abstract, ECCC TR05-021 and its revisions, and the SIAM publisher record). These current reads are search/abstract checks, not another full-paper proof check. No exact antecedent for the present bounded deletion profiles was verified in this search. Nearby work on circuit certificates and newer cardinality-constraint encodings was not used as a theorem. The broader single-level separation continues to preclude an unrestricted assumption that every Boolean quadratic function can be treated as a one-level arithmetic quadratic circuit. The present conclusions instead use the specified C4-free graph, exact quadratic extraction, original deleted-gate counts and actual insertion-low constraints. Priority remains unresolved and no novelty claim is made. Search references: turn402113647search0–search7 and search36; primary URLs include https://eccc.weizmann.ac.il/report/2005/021/ and https://web.vu.lt/mif/s.jukna/papers/single.html. Earlier full-source proofs and hashes remain in the existing literature record.


## paper4_root_context_literature

# Primary-source follow-up for the two-witness context argument

Recorded 2026-11-24T22:43:08.481450+00:00, GPT-6 Astra Pro, /root; effort not exposed.

Searches: `"edge functions" "C4" monotone circuits`; `"monotone" "vertex cover" "quadratic" circuits star`. These returned Jukna's existing primary ECCC papers and several nonprimary or irrelevant results. Only the primary ECCC sources were used. No novelty or priority claim follows from this search.

Jukna, S. (2004; revision1dated14February2005). *On graph complexity* (ECCC TR04-005). https://eccc.weizmann.ac.il/report/2004/005/revision/1/download/ . The official report page records the journal version as *Combinatorics, Probability and Computing,15*(2006),855–876. Definition1.1(p.2) specifies representation only on pairs. Section7.1, Theorem7.1andLemma7.2(p.16), instead concern computing the full edge function; the lemma derives a CNF bound by forcing adjacency when a shortened CNF accepts an independent set. This is relevant background for the safety/adjacency step in the present context argument. It does not state the exact deleted-gate or minimum-addition-frame result. The already cited Theorem7.3(p.18) remains a formula/depth bound, not an exact shared-gate count.

Jukna's ECCC TR05-021revision1PDF was reopened too; its current text extraction is garbled. No new conclusion was drawn from that unreadable extraction. The separately retrieved author version and earlier verified statement locators remain the basis for claims about that work.

The candidate circuit proof remains pending separate checks at this reading time. This source review is not a proof check or a main-gate movement event.


## paper4_root_live_followup_literature

# Live external-node follow-up —24November2026,22:17UTC

The homepage https://pequalnp.com/ was opened at22:17:18UTC. It displayed a paused-data template and did not expose the cited node records. Fresh engine1searches with a one-day recency filter for `site:pequalnp.com "L-meta-608"` and `site:pequalnp.com "L-meta-612" "L-meta-647"` returned no relevant indexed node evidence; an unrelated hit was ignored.

At22:17:37UTC, direct public reads were made of https://pequalnp.com/lemma#L-meta-606 , https://pequalnp.com/lemma#L-meta-608 , https://pequalnp.com/lemma#L-meta-612 , https://pequalnp.com/lemma#L-meta-647 and https://pequalnp.com/lemma#L-meta-649 . Every response exposed the same49-line page with the loading message and no theorem text or current checker status. The live status of all five nodes therefore remains unretrieved. Historical23Novemberstatuses stay explicitly separate from these unsuccessful live reads.

No sign-in session, enrollment, lease, contribution, comment or submission was attempted. This access check changes no mathematical claim or external status. The series' own bounded theorems and the unresolved unrestricted conjectures retain their exact scopes.

## 25November2026,00:46:13UTC: new direct node readings

The homepage was reopened between00:44:18and00:45:31UTCand again exposed paused live data without individual statuses (turn822107584view1). Direct public reads of https://pequalnp.com/lemma#L-meta-606 , https://pequalnp.com/lemma#L-meta-608 , https://pequalnp.com/lemma#L-meta-612 , https://pequalnp.com/lemma#L-meta-647 and https://pequalnp.com/lemma#L-meta-649 were observed at00:46:13UTC. Each returned the same49-line loading template without theorem text or checker status (turn294408789view0–view4). Engine1queries with recency1for `site:pequalnp.com "L-meta-608"` and `site:pequalnp.com "L-meta-612" "L-meta-647"` returned no results. The current statuses of all five nodes remain unretrieved; the historical23Novemberstatuses are not relabeled current. No enrollment, lease, mutation, message or submission was attempted.

## 25November2026,03:38:48UTC: direct live-node follow-up

Direct reads of the606,608,612,647and649node URLs at https://pequalnp.com/lemma#L-meta-608 (with the corresponding identifiers substituted) all returned the same47-line navigation shell without node statements or checker status. The former loading text was absent, but no status data became available. The read-only https://data.pequalnp.com/data/desk/gaps.json endpoint was inaccessible through the retrieval tool. Exact engine1queries with recency1for608and612/647/649returned general pages from the service, not the requested current node records. The indexed homepage contained an activity snapshot, whereas the direct homepage exposed paused/empty live data; neither establishes these exact nodes' current status. Historical23Novemberstatuses remain explicitly historical. No lease, enrollment, message, mutation or submission was performed. Retrieval references: turn488882744search0–search5, turn488882744view0, turn180227512view0–view5. These are source-retrieval events only, not checked mathematical claims.

## Direct live-node follow-up (2026-11-25T04:33:56.681107+00:00)

The exact node URLs https://pequalnp.com/lemma#L-meta-606 , https://pequalnp.com/lemma#L-meta-608 , https://pequalnp.com/lemma#L-meta-612 , https://pequalnp.com/lemma#L-meta-647 and https://pequalnp.com/lemma#L-meta-649 again returned47-line navigation shells without a node statement or current status. The data endpoint https://data.pequalnp.com/data/desk/gaps.json remained inaccessible. An engine1 exact-node query with recency1 returned no usable node-specific primary result. These observations do not verify any current node status or infer a status change. The attached23November status remains explicitly historical. No enrollment, lease, contribution or other site mutation occurred.

## Live follow-up observed2026-11-25at05:50:19UTC

The exact606,608,612,647and649node URLs at https://pequalnp.com/lemma#L-meta-608 with corresponding fragment identifiers again returned the same47-line navigation shell, with no node statement or current checker status. The public data endpoint https://data.pequalnp.com/data/desk/gaps.json was inaccessible. An engine1query for the exact608identifier with recency1returned general service pages and an indexed homepage activity snapshot, not current evidence for any of these five nodes. No node status or change is inferred from that aggregate snapshot; attached23November statuses remain historical. No enrollment, lease, contribution, message or site mutation was performed. References:turn287902317view0–view5;turn287902317search0–search4. These are retrieval observations, not mathematical check events.


##25November2026,06:53UTC: live nodes and bounded primary literature follow-up

At06:53UTC the exact pequalnp node URLs for L-meta-606,608,612,647and649 were opened again. Each returned the same47-line navigation shell without node text or status. No current node-specific status is verified;23November statuses remain historical. Search-service references: turn463374662view0throughview4. No external source copy is included.

At approximately06:18–06:20UTC, bounded searches used the phrases “quadratic Boolean functions” with “monotone” and “C4”, “monotone circuits” with “vertex cover” and “quadratic”, and “monotone circuit” with “two additions”. Engine2output was partly truncated and is not recorded as fully read. Primary-filtered engine1queries for two additions and C4-free quadratic circuits returned Jukna's already known report: Jukna, S.(2004). On graph complexity (ECCC TR04-005). https://eccc.weizmann.ac.il/report/2004/005/ . Its retrieved abstract allows arbitrary values away from weight-two inputs, unlike the full Boolean output semantics here. No new exact antecedent of the hidden profiles or five-factor claim was verified; this is bounded retrieval, not a priority or exhaustive novelty conclusion.

The official OpenAI math overview https://github.com/openai/math/blob/main/overview.tex was opened in that search (turn574625811view0); only navigation/metadata and an initial returned portion were inspected, not the full865-line source or a new relevant proof. Existing previously verified citations retain their earlier exact scope.


##25November2026,07:50:32UTC: five exact live node rereads

Opened https://pequalnp.com/lemma#L-meta-606 and the exact corresponding608,612,647,649URLs. All five again returned47-line navigation shells without individual statement or status content. Search-service references turn907684646view0–4. No current node-specific status was learned or promoted;23November statuses remain historical. This was a direct reread only; no new endpoint or indexed-search result is claimed. No external source copy or text extraction is included.


##25November2026,08:53:33UTC: five exact live node rereads

Opened https://pequalnp.com/lemma#L-meta-606 and the exact corresponding608,612,647,649URLs. All five returned47-line navigation shells with no individual statement or status content. Search-service references turn949104320view0–4. Current node-specific statuses remain unretrieved;23November statuses remain explicitly historical. This observation concerns only the direct node URLs and does not redate earlier endpoint or indexed-search attempts. No external source copy or plain-text extraction is included.


##25November2026,09:48:55UTC: five exact live node rereads

Opened https://pequalnp.com/lemma#L-meta-606 and the exact corresponding608,612,647,649URLs. All five returned47-line navigation shells without individual statement or current checker-status content. References turn730693455view0–4. These direct rereads do not establish a node status or change;23Novemberstatuses remain explicitly historical. Earlier endpoint and indexed-search observations retain their own dates. No external text extraction, enrollment, lease or site mutation is included.


##25November2026,10:32:23UTC: five exact live node rereads

Opened https://pequalnp.com/lemma#L-meta-606 and the corresponding608,612,647,649URLs. All five again returned47-line navigation shells without individual statements or current checker statuses. References turn644768844view0–4. No current node status or change is inferred;23Novemberstatuses remain historical. This observation is a direct reread only, without redating earlier endpoint or indexed-search attempts. No external source text is copied into the deliverables.


##25November2026,11:11:41UTC: five exact live node rereads

Opened https://pequalnp.com/lemma#L-meta-606 and the corresponding608,612,647,649 URLs. All five again returned47-line navigation shells, without individual statements or current checker statuses. Search-service references turn708894097view0–4. The reread does not establish any present node status or change, and23November statuses remain explicitly historical. This observation concerns only the exact node URLs; earlier endpoint and indexed-search observations retain their dates. No external text extraction is copied into the deliverables.


##25November2026,12:06:03UTC: five exact live node rereads

Opened https://pequalnp.com/lemma#L-meta-606 and the corresponding608,612,647,649 URLs. Each returned the same47-line navigation shell with no individual statement or current checker status. Search-service references turn167889441view0–4. No current node status or change is inferred;23Novemberstatuses remain historical. This reread concerns the exact node URLs only and does not redate earlier endpoint or indexed-search observations. No external text extraction is copied into the deliverables.


## 2026-11-25 13:04:34 UTC: five exact live node rereads

Opened https://pequalnp.com/lemma#L-meta-606 and the corresponding608,612,647,649 URLs. All five returned 47-line navigation/footer shells, without individual statements or checker statuses. Source references: turn227291389view0, turn227291389view1, turn227291389view2, turn227291389view3, turn227291389view4. The response-body hash (the numbered retrieved lines) was 577a270ca0a17d0c7dc051d680aecfc57a3b6c759dc556f282e0c7b798d09a66. The23November individual statuses remain explicitly historical. These are direct exact-URL observations only; earlier endpoint and indexed-search attempts keep their own dates. The execution outage prevented a contemporaneous filesystem write; this own observation was preserved from session records and actually saved 2026-11-25T15:53:22.245178+00:00. No external text extraction is included in the deliverable.


## 2026-11-25 14:07:52 UTC: five exact live node rereads

Opened https://pequalnp.com/lemma#L-meta-606 and the corresponding608,612,647,649 URLs. All five returned 47-line navigation/footer shells, without individual statements or checker statuses. Source references: turn511160915view0, turn511160915view1, turn511160915view2, turn511160915view3, turn511160915view4. The response-body hash (the numbered retrieved lines) was 577a270ca0a17d0c7dc051d680aecfc57a3b6c759dc556f282e0c7b798d09a66. The23November individual statuses remain explicitly historical. These are direct exact-URL observations only; earlier endpoint and indexed-search attempts keep their own dates. The execution outage prevented a contemporaneous filesystem write; this own observation was preserved from session records and actually saved 2026-11-25T15:53:22.245178+00:00. No external text extraction is included in the deliverable.


## 2026-11-25 15:51:22 UTC: five exact live node rereads

Opened https://pequalnp.com/lemma#L-meta-606 and the corresponding608,612,647,649 URLs. All five returned 58-line navigation/footer shells, without individual statements or checker statuses. Source references: turn197082492view0, turn197082492view1, turn197082492view2, turn197082492view3, turn197082492view4. The response-body hash (the numbered retrieved lines) was 63e82514a25a166cad2b4774384eafdb8a0100c765855ca6ffcc554a2c06a6c6. The visible shell changed from the earlier47-line response; this is no evidence of a mathematical node or checker-status change. The23November individual statuses remain explicitly historical. These are direct exact-URL observations only; earlier endpoint and indexed-search attempts keep their own dates. This own observation was saved 2026-11-25T15:53:22.245178+00:00. No external text extraction is included in the deliverable.


## 2026-11-25 16:55:12 UTC: five exact live node rereads

The exact node606,608,612,647,649 URLs again returned58-line navigation/footer shells without individual statements or checker statuses. Source references: turn851490297view0, turn851490297view1, turn851490297view2, turn851490297view3, turn851490297view4. The numbered-line SHA256 is 63e82514a25a166cad2b4774384eafdb8a0100c765855ca6ffcc554a2c06a6c6. No mathematical node-status change is established; the23November statuses remain historical. Own observation saved 2026-11-25T16:56:00.470418+00:00. No external text extraction is included.

## Exact-node follow-up at17:56:09UTC,25November2026

All five exact URLs606,608,612,647,649 were opened again. Each returned the same58-line navigation/footer shell and no individual statement or checker status. The numbered-line SHA256 equals the16:55observation,63e82514a25a166cad2b4774384eafdb8a0100c765855ca6ffcc554a2c06a6c6. No current node-status or mathematical-change claim follows. Exact observations and references are in checks/outage_20261125/root/live_source_observations_1756.json. Only own metadata is retained; no external page text is copied into this workbench. This is a source event, not a proof check or research movement.

## Exact-node follow-up at19:04:42UTC,25November2026

All five exact URLs606,608,612,647,649 again returned the identical58-line navigation/footer shell and no individual statement or checker status. The numbered-line SHA256 is63e82514a25a166cad2b4774384eafdb8a0100c765855ca6ffcc554a2c06a6c6, equal to17:56. No current status or mathematical-change claim follows. References and own observations are in checks/outage_20261125/root/live_source_observations_1904.json. No external page text is copied into the workbench; this is source metadata, not proof credit or research movement.

## Actual direct follow-up:25November2026,20:08:17UTC

The exact five public-node URLs606/608/612/647/649 again yielded58-line navigation/footer shells without individual statements or checker statuses. This does not establish current live statuses and creates no mathematical movement. Own retrieval metadata and numbered-line hashes are in checks/outage_20261125/root/live_source_observations_2008.json; no external page text is bundled. Historical status observations and their dates remain unchanged.

## Actual direct follow-up:25November2026,21:00:34UTC

The exact five public-node URLs606/608/612/647/649 again yielded the same58 numbered navigation/footer lines, with terminal-newline SHA256951677f00088060f85f8431bdc0936879e1cf97572dfa54da9bb3ad9bd306624 matching20:08. No individual statement or checker status was returned. No current status or mathematical movement is inferred. Exact own retrieval metadata and source references are in checks/outage_20261125/root/live_source_observations_2100.json; no external page text is bundled. Historical observations remain unchanged.

## Actual direct follow-up:25November2026,21:58:41UTC

The exact five public-node URLs606/608/612/647/649 again yielded the same58 numbered navigation/footer lines, with terminal-newline SHA256951677f00088060f85f8431bdc0936879e1cf97572dfa54da9bb3ad9bd306624 matching21:00. Retrieval occurred between21:58:20 and21:58:41UTC, with observation recorded after completion at21:58:41. No individual statement or checker status was returned. No current status or mathematical movement is inferred. Exact own retrieval metadata and source references are in checks/outage_20261125/root/live_source_observations_2158.json; no external page text is bundled. Historical observations remain unchanged.

## Actual direct follow-up:25November2026,23:09:07UTC

The exact five public-node URLs606/608/612/647/649 again returned58 numbered navigation/footer lines without individual statements or checker statuses. Their terminal-newline SHA256 is951677f00088060f85f8431bdc0936879e1cf97572dfa54da9bb3ad9bd306624, exactly matching21:58. The observation time was read after retrieval completed; no separate request-start time is asserted. No current status or mathematical movement is inferred. Exact own metadata and source references are in checks/outage_20261125/root/live_source_observations_2309.json; no external page text is bundled. Historical observations remain unchanged.

### Direct node follow-up observed 25 November 2026, 23:57:31 UTC

The five exact fragment URLs for L-meta-606,608,612,647 and649 again returned only the same58 numbered navigation/footer lines. No individual mathematical statement or checker status was exposed. The complete returned line digest equals the23:09 observation; this does not establish the current statuses of the historical nodes. Exact URLs, new retrieval references and hashes are in `checks/outage_20261125/root/live_source_observations_2357.json`. No external page text is bundled, and this source follow-up creates no mathematical movement.

## Observation26November2026,00:58:39UTC

The five exact URLs for L-meta-606,608,612,647,649 returned the same58 numbered navigation/footer lines as23:57:31. No individual statement, checker record or current node status was returned; no mathematical status change or movement is inferred. Exact references are turn831311730view0–4. The dated observation record is checks/outage_20261125/root/live_source_observations_0058.json. No external page text is bundled.

## Actual direct observations — 26 November 2026, 02:00:11 UTC

All five exact node URLs606,608,612,647,649 were reopened and their complete58-line outputs read. Each still supplied navigation and footer text without the individual node statement or checker status. References turn257389675view0–4 and the actual observation record checks/outage_20261125/root/live_source_observations_0200.json preserve this unsuccessful status check. The visible numbered content matches the preceding00:58 observation, but no new raw-response byte hash is asserted. The historical23 November statuses remain historical; no current project status, priority conclusion or mathematical movement follows.

## Direct observation window — 26 November 2026, 03:00:56 UTC

All five exact node URLs606,608,612,647,649 were reopened and the complete58-line returned outputs read. Each supplied navigation and footer text without its individual mathematical statement or checker status. References turn349558186view0–4 are recorded in checks/outage_20261125/root/live_source_observations_0300.json. The second-resolution observation window follows the concurrent local clock observation; exact HTTP completion times were not exposed. No raw response was saved and no new response byte hash is asserted. Historical statuses remain historical, and this check creates no mathematical movement.

## Actual direct-node-only observation,26November2026,04:00:20–21UTC

One web-open call requested the exact URLs for L-meta-606,608,612,647 and649. Each returned58 numbered navigation/footer lines with no individual statement or checker status. Root read every returned output untruncated. References: turn858648003view0, turn858648003view1, turn858648003view2, turn858648003view3, turn858648003view4. Second-resolution clocks bracketed this call; internal HTTP completion times were not exposed. Metadata: checks/outage_20261125/root/live_source_observations_0400.json. No raw-response copy or new byte hash is asserted. Historical23November statuses remain historical. Earlier endpoint/search observations retain their own actual dates. This source observation adds no proof, checked status or mathematical movement.

## Actual direct-node-only observation,26November2026,05:00:00–01UTC

One web-open call requested the exact URLs for L-meta-606,608,612,647 and649. Each returned58 numbered navigation/footer lines with no individual statement or checker status. Root read every returned output untruncated. References: turn303205668view0, turn303205668view1, turn303205668view2, turn303205668view3, turn303205668view4. Second-resolution clocks bracketed this call; internal HTTP completion times were not exposed. Metadata: checks/outage_20261125/root/live_source_observations_0500.json. No raw-response copy or new byte hash is asserted. Historical23November statuses remain historical. Earlier endpoint/search observations retain their own actual dates. This source observation adds no proof, checked status or mathematical movement.


## paper4_root_matching_literature

# Deleted-product and matching follow-up — 2026-11-24T21:37:55.450448+00:00

Searches: `monotone circuit matching AND gates lower bound vertex cover quadratic polynomial`; `"monotone" "AND gates" "matching" circuit complexity`. The primary publisher record for Amano–Maruoka2006 was found again, but its full text remained inaccessible. Perfect-matching detection results returned by the search concern a different function and are not evidence for the present fixed-matching edge-function bound.

Jukna, S. (2006). Disproving the single level conjecture. *SIAM Journal on Computing,36*(1),83–98. https://doi.org/10.1137/S0097539705447001. Author PDF https://web.vu.lt/mif/s.jukna/ftp/single1.pdf,19pages,248425bytes,SHA2564779a3ebabeebac7df7da74ccdc4aafb4636f2e8582ba7d5e38f31a3bdbd6dd4. Downloaded after two web-open timeouts. Source and extraction remain outside the returned workbench.

Theorem2.3,author-PDFp5, gives the induced-matching lower bound m(G)+1 for total unbounded-fanin circuit size. Its proof in§6,pp15–16, restricts to the matching and uses deterministic communication complexity. This is related classical context but does not by itself give the precise AND-only lemma used in SZ4-079. Our elementary global-resolution and gate-elimination proofs therefore remain necessary for the stated gate measure. Section3.1,p6,and§8,p17 distinguish graph representation on two-element inputs from computing the full edge function; this prevents misuse of the short-CNF representation of a matching in§7,p16. The current circuit uses the full function on every independent set.

The original ECCC report https://eccc.weizmann.ac.il/report/2005/021/download/ was also opened,17pages,with older numbering. Its results are not cited under the author's later numbering. ECCC revision2 was opened but its text extraction was garbled; an attempted direct download returned503. No theorem was credited from unreadable text. The matching count is treated as an elementary lemma without a priority claim; the specific maximum-cover-gain deletion theorem is stated with its hypotheses and a full proof, with no assertion of exhaustive novelty search.


## paper4_root_two_cut_literature

# Two-cut and three-cut circuit refinements: source comparison

Recorded UTC: 2026-11-25T04:18:54.291857+00:00. These are bounded source searches and comparisons, not independent proofs of the new circuit statements or priority claims.

## Searches and access limits

At03:55–03:57UTC, searches for quadratic Boolean functions and conjunctive complexity returned the primary Amano–Maruoka publisher abstract and Jukna sources. A direct recheck at03:56:57UTC of https://ipsj.ixsq.nii.ac.jp/records/31828 and https://ipsj.ixsq.nii.ac.jp/record/31828/files/IPSJ-AL04097006.pdf returned429; the publisher DOI fetch was inaccessible. No full original Amano–Maruoka proof was obtained, and no full-text check is claimed. No rapid retry or rate-limit workaround was attempted.

At04:16–04:18UTC, engine2 searches for “monotone quadratic C4-free circuit lower bound”, “monotone circuits two addition edge Jukna”, and a Hexagon monotone-circuit query were followed by engine1 searches for quadratic single-level circuits, C4 circuit bounds and ECCC's read-k paper. The primary ECCC records TR05-021 and TR22-094, Jukna's author abstract and the SIAM DOI page were recovered; the general Hexagon catalog results supplied no exact antecedent for the present deletion-profile statements. Search snippets are not treated as proof checks. The already checked Jukna primary argument remains the detailed single-level comparison.

Amano, K., & Maruoka, A. (2006). The monotone circuit complexity of quadratic Boolean functions. *Algorithmica, 46*,3–14. https://doi.org/10.1007/s00453-006-0073-0. The recovered primary abstract concerns differences between arbitrary and single-level circuits, including conjunctive complexity. It does not supply a proof of the exact unrestricted C4-free count or of the current deleted-addition refinements.

No exact antecedent for the arbitrary-product induced-path/triangle obstruction125 or the precise all-visible two-product slice126 was verified by these bounded searches. That finding does not establish priority or exhaustive literature coverage. The manuscripts state their own full arguments and their precise remaining gates.

## A recent threshold-circuit comparison

Krapivin, A., Przybocki, B., & Subercaseaux, B. (2026). *Near-optimal encodings of cardinality constraints*. SAT2026. https://doi.org/10.4230/LIPIcs.SAT.2026.23. Full version: https://arxiv.org/abs/2603.28954v2 (16April2026).

Downloaded PDF https://arxiv.org/pdf/2603.28954v2:792880bytes,37pages,SHA-256 ff5d585420858e34e7c0eff0f3f50dc3d3972fd3944de9f9cf98b7d23cb6f210. Root read §3.4,Theorem6,pp7–8 and the complete AppendixA.2 proof,p19. The publisher version numbers the circuit statement Theorem9. It constructs threshold-2 circuits of size2n+sqrt(2n)+O(n^(1/3)) by assigning variables to multipartite-graph edges, combining local threshold-2 computations and a threshold-3 computation across parts. The correctness partition and gate count were checked; its cited auxiliary threshold bounds remain attributed background. The reported correction to Sergeev's lower bound was not independently verified.

Threshold2 is the edge function of K_n, which contains a four-cycle for n>=4. Thus this recent construction helps explain why general quadratic Boolean circuits cannot be assumed single-level, while leaving the present C4-free conjecture and deletion-profile reductions unchanged. External PDFs and extractions are excluded from returned archives.

## One-visible-cut follow-up (2026-11-25T04:33:56.681107+00:00)

A bounded engine1 search for “conjunctive complexity” and “maximal independent sets” recovered general monotone CNF/DNF dualization and independent-set enumeration sources, but no exact antecedent for the extraction-specific128bound. The basic global conjunction-resolution inequality and the maximal-zero-assignment/positive-clause relation are elementary known ingredients and are proved explicitly where used; no priority is claimed for them. The new refinement applies these ingredients to the high network behind the sole visible extraction cut, with arbitrary hidden additions and no C4 hypothesis. No retrieved snippet is treated as an independent theorem check.

## Maximum missing-degree follow-up (2026-11-25T04:52:58.683695+00:00)

Bounded engine2 searches used the queries “quadratic Boolean functions monotone circuits”, “C4-free circuit edge”, “monotone circuit two additions”, and “monotone circuits girth vertex cover”. Engine1 follow-up used “C4-free monotone circuits” and “quadratic Boolean functions two additions”. Further engine2 queries asked for the Lenz–Wegener title and two addition gates in monotone quadratic circuits. Results recovered Jukna's primary author page and ECCC TR04-005/TR05-021, the Amano–Maruoka publisher abstract, and the Lenz–Wegener publisher record. No exact antecedent of the at-most-two-deleted-additions maximum-missing-degree theorem129 was verified. This is neither an exhaustive literature claim nor evidence of priority.

Lenz, K., & Wegener, I. (1991). The conjunctive complexity of quadratic Boolean functions. *Theoretical Computer Science, 81*(2), 257–268. https://doi.org/10.1016/0304-3975(91)90194-7. The publisher search record's abstract concerns conjunction counts, single-level circuits, and their difference from general monotone circuits. Direct primary-page opening returned403 at the 04:50–04:51UTC follow-up; no full proof was obtained or checked. The citation and author spelling were also read in full in reference14 on PDFpage18 of the already fetched Jukna author preprint https://web.vu.lt/mif/s.jukna/ftp/single1.pdf. The conference version, CSL'87, pp138–150, DOI10.1007/3-540-50241-6_35, appeared in the primary Springer volume listing; it was not silently identified with a newly read full journal paper.

The primary Jukna author abstract https://web.vu.lt/mif/s.jukna/papers/single.html was opened again in full. It distinguishes arbitrary monotone circuit size from single-level size and reports the almost-quadratic separation. The complete previously checked source remains the relevant detailed comparison. The recovered TR04-005 abstract concerns representation on inputs with exactly two ones, allowing arbitrary outputs elsewhere; that is not the full safe-support edge-function model used in129. No new theorem is imported from that abstract.

The new missing-degree proof uses the elementary C4 old-neighborhood fact and the already proved arbitrary-product two-addition normalization. It imposes no induced-star or optimal-frame hypothesis, and leaves every maximum-degree-two missing graph outside its conclusion. All fetched external papers remain outside the returned archives.

## Full missing-component follow-up (2026-11-25T05:22:11.616235+00:00)

Before any priority characterization of132, bounded engine2 queries used “monotone circuits homogeneous quadratic addition”, “monotone circuit missing quadratic”, and “C4-free monotone circuits path”; engine1 verification used “monotone circuits quadratic minimum degree sum” and “quadratic Boolean C4 path”. These recovered the existing primary Jukna, Amano–Maruoka and Lenz–Wegener records and broader arithmetic/formula sources. No exact antecedent for the two-deleted-additions K2/P3missing-component statement was verified. Unrelated secondary search results were not imported as theorem evidence. The new argument is compared with the same already checked lower-envelope and single-level sources; no source priority or exhaustive coverage is claimed. The elementary missing-graph consequences are proved in full, with the old-low/context condition kept explicit.


## paper5_literature

# Paper5 literature additions

## 24 November 2026,15:48–15:51 UTC

Queries: multisemigroup deformation positive structure constants nonnegative integers lift; multisemigroups realizable positively based algebra structure constants counterexample. Search returned Love Forsberg's primary paper, then the arXiv PDF and publisher full text were opened. Forsberg (2017), Multisemigroups with multiplicities and complete ordered semi-rings, Beiträge zur Algebra und Geometrie58,405–426, DOI10.1007/s13366-016-0320-8; arXiv1510.01478v1 p15 Proposition12 and Corollary13 prove the finite-positive-multiplicity obstruction used here. The current paper specializes it to the prescribed rank-three trace algebra and explicitly credits it; no priority claim is made. Binary hash is in checks/paper5_forsberg_source.json when download succeeds. No external PDF is returned.

Milne, Algebraic number theory, v3.08 (2020), primary author PDF opened: Theorem3.20 p53 for fractional ideal groups; Theorem4.4 for class-group finiteness; Theorem5.9 for the full archimedean unit-log lattice. Stacks Tag0B5B, Section53.5, Riemann–Roch opened for the function-field proof. These classical inputs prove global weight rigidity by a direct orthogonality argument. Milne binary fetch initially returned406; web PDF access succeeded, and no absent hash is invented.


## paper5_root_followup_literature

# Additional predecessor and forward-citation audit

24 November 2026, approximately18:41–18:46UTC. GPT-6 Astra Pro, root; effort not exposed. These are literature observations and scope comparisons, not independent proof events.

The primary-coverage queries were `"The case for inverse semirings" -site:chatgpt.com`, `"inverse semirings" "projective" modules`, and `"Clifford semigroups and the monoidal Grothendieck construction" -site:chatgpt.com`, with a365-day search setting. They returned the known arXiv and author records, Macpherson's projective-module paper, and Borger–Jun's published *Facets of module theory over semirings*. The latter has publisher page https://www.sciencedirect.com/science/article/pii/S0001870825003299; its Definition7.1 gives the projectivity convention used here. The search also exposed an older predecessor, and it was pursued without the date filter.

Sen, M. K., Bhuniya, A. K., & Maity, S. K. (2021). Inverse semimodules. *Asian-European Journal of Mathematics,14*(2),2150022. https://doi.org/10.1142/S1793557121500224. The publisher abstract reports a strong-semilattice description of Clifford semimodules and congruence results. The author's institutional publication list, https://www.caluniv.ac.in/academic/PureMath/S.K.Maity.pdf, p.3, confirms the2021 issue, article number and14-page length; the publisher records online publication9January2020. The publisher PDF was inaccessible, so no unobserved theorem number or exact equivalence with the manuscript's zero-preserving category is asserted. The source's cited Yusuf1966 paper remains a historical lead, not a full-text check.

Dokuchaev, M., Johari, F., & Vilca-Rodríguez, J. L. (2026). Inverse semialgebras and partial actions of Lie algebras. *Revista Matemática Iberoamericana,42*(5),1637–1680. https://doi.org/10.4171/RMI/1628. Opened the publisher page and44-page publishedPDF https://ems.press/content/serial-article-files/53723?nt=1. Read Definitions2.2–2.3 andLemma2.4, pp.1641–1643, andExample3.6/Proposition3.10, pp.1653–1657. They distinguish ordinary scalar-zero absorption from inverse semivector spaces and reconstruct semilattices of algebras from presheaves. This is a relevant neighboring framework, not a verified citer ofFGJM: neither searched version exposed that citation. The arXiv2505.03081v2 numbering differs, so the paper comparison uses the published locators. Downloaded bytes have SHA-256 fcb48509dec09707d9cd37134a1554e9cd79738125a16c5e37b1ade20b530d18; thePDF stays outside the deliverable. Root's elementary comparison for a field: a monoidal inverse semivector space extends to anF0-semimodule by letting the new zero act as the global additive identity; restricting old scalars reverses this. This uses the stated identity-preserving convention and is not a priority claim.

An author-uploaded full text of Sen, Maity andSwomin's *Von Neumann regular semimodule*,2021, pp.279–294, was opened at https://www.researchgate.net/publication/352080291_Von_Neumann_regular_semimodule. Section2, pp.280–281, permits additive semigroups with or without zero and adopts a distributive-lattice-of-rings setting; it is therefore not silently substituted for the present conventions. The direct primary journalPDF was attempted at https://www.math.uaic.ro/~annalsmath/pdf-uri_anale/F2%282021%29/8_MK_Sen_SK_Maity_Sabnam_Swomin.pdf and failed with502/503. There is no downloaded-byte hash for that unavailablePDF. The complete original inverse-semimodule decomposition theorem is still not inspected.

The FGJM arXiv landing page https://arxiv.org/abs/2411.12318 was opened again. Its SciX citation link returned a JavaScript verification wall, GoogleScholar returned429, andSemanticScholar redirected to an inaccessible page. No verification wall was bypassed. Consequently a complete citing-paper census remains uncertified. The exact FORMAT.md GitHub URL again returnedDisabledError, and https://hexagonmath.org/2611.00789 was inaccessible in this retry. Existing attached sources and earlier read material remain the basis for their recorded uses; the failures supply no novelty evidence.

Retrieval records: turn679810994academia7–8 andsearch0–3; turn263004695search0,search8,view2; turn636088288view1–4; turn803060410search0,search6,view0; turn226338855view1–3; turn884124258view0–4; turn706456443view0–2. These are locators for this research session, not manuscript references. Download success/failure data are preserved in checks/root_literature_followup_1840_hashes.json.

## Additional primary-access attempts, 24 November 2026, 19:27–19:31UTC

Queries: `Davenport Heilbronn 1936 "On the zeros of certain Dirichlet series" pdf` and `Sen Bhuniya Maity "Inverse semimodules" 2150022 full text pdf`. Primary Wiley/LMS metadata again confirmed the1936 articles at11(3),181–185 and11(4),307–312. Opening each publisher PDF URL redirected to its abstract/metadata page; following Download PDF repeated that redirect. The publisher supplied first-page preview links, but local retrieval of both returned403, so no preview image or full PDF was inspected or hashed. No access restriction was bypassed.

URLs: https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/jlms/s1-11.3.181 and https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/jlms/s1-11.4.307. The exact preview URLs/errors are in checks/root_dh_preview_retrieval.json. SHA256: unavailable because no paper bytes were retrieved. Pages used: publisher metadata only; no new theorem or proof attribution follows from this attempt.

The Sen–Bhuniya–Maity primary publisher abstract remained accessible and states its Clifford-semimodule/strong-semilattice characterization; https://www.worldscientific.com/doi/pdf/10.1142/S1793557121500224 remained inaccessible. SHA256: unavailable for the original full article. This leaves the already documented abstract-level scope unchanged; the separate2021 convention comparison and2026 published inverse-semialgebra text are treated at their own verified locators.


## paper5_root_literature

# Root continuation of the literature audit

Date: 24 November 2026, 16:09–16:25 UTC. Worker: GPT-6 Astra Pro; numerical effort not exposed.

- Queries: "The case for inverse semirings" excluding arxiv; "Clifford semigroups and the monoidal Grothendieck construction" modules; "Projective modules over polyhedral semirings" Macpherson arxiv; site:github.com/KokunoYumeto/mathematics-workbenches FORMAT.md. The first two found the known preprint and author pages, without an exhaustive forward-citation list. FORMAT.md remained inaccessible; no format-conformance claim is inferred.
- Macpherson, A. (2018). Projective modules over polyhedral semirings. Journal of Algebra. https://doi.org/10.1016/j.jalgebra.2018.09.041; arXiv:1507.07213, https://arxiv.org/pdf/1507.07213. Opened the full 27-page preprint. Theorem3.9, printedpp8–9, supplies the Boolean projective-poset antecedent. Corollary4.13, printedp15, treats the specified monoid-pair domain framework of Definition4.9,p14; it does not by itself classify projectives for arbitrary inverse-semiring data (Q,F).
- At16:14 UTC, followed the Google Scholar and Semantic Scholar links on https://arxiv.org/abs/2411.12318. Scholar returned429; Semantic Scholar redirected to an inaccessible endpoint. These failures leave the forward-citation audit incomplete.
- Fresh stronger searches: "The case for inverse semirings" citations semimodules; "Clifford semigroups and the monoidal Grothendieck construction" cited. Results included https://lucamesiti.github.io/publications/2026-07-15-MonoidalGrothClifford/ and https://ct2026.com/ct/abstracts/luca-mesiti/. These are author/conference descriptions of the same work, not evidence of a complete absence of further papers.
- Davenport and Heilbronn queries: "Davenport Heilbronn 1936 On the zeros of certain Dirichlet series pdf"; exact title with filetype:pdf and the publishers excluded; title plus Hurwitz. Confirmed the two separate articles: Journal of the London Mathematical Society11(3),181–185, July1936, DOI10.1112/jlms/s1-11.3.181; and11(4),307–312, October1936, DOI10.1112/jlms/s1-11.4.307. Publisher PDF links redirected to abstracts; the OUP PDF route was inaccessible. A linked public first-page image was exposed as an image-only URL but returned no readable text/image payload, and its direct download returned403. Full-text reading and exact historical theorem verification therefore remain incomplete. No unread theorem is used in the certified path proof.
- https://hexagonmath.org and the previously identified preprint endpoint were retried; access remained unavailable. Searches do not establish novelty by absence.

2026-11-24 16:50–16:52UTC. Searches: projective semimodules finite distributive lattice semiring classification join irreducible; exact projective semimodules/distributive lattice/classification; G_L/projective/semiring lattice; then stronger-engine colored-poset/Macpherson queries. Found Macpherson DOI10.1016/j.jalgebra.2018.09.041 and Katsov–Nam–Zumbrägel arXiv1105.5591 (Boolean-projective background), plus lattice-category results whose morphisms differ. No exact G_L(R) admissible-ideal theorem was located in these results. A globalresearchspace hit describes the project’s own earlier draft and supplies no independent priority evidence. Searches do not settle exhaustive novelty.

2026-11-24 17:03–17:06UTC. Exact a-point/extremal-real-part searches found and opened Arias de Reyna and van de Lune, Some bounds and limits in the theory of Riemann’s zeta function, arXiv1107.5134v1. Lemma2.2(pp3–4), Theorem3.1(pp4–5) give the exact 0<a<1 threshold; Theorem4.1(pp5–6) gives the separate a=1 threshold1.94010168…, correcting the unpublished approximate1.78 claim. The 0<a<1 proof had been independently derived before opening this primary proof; the result is known, not new. PDF https://arxiv.org/pdf/1107.5134,557682bytes, SHA2569e314dfe479213ca4ff1ff5a8c5a2fa9b3753839c742acbc558b72e7de78c6e5. DLMF25.10(i),equations25.10.1–2, opened for Hardy Z and theta definitions; no zeta-zero distribution theorem is inferred from a normalized CLT.


## 2026-11-24, approximately17:30 UTC: rank-four primary-source check

Search: exact GCT IV title with114 and11.8; opened https://arxiv.org/pdf/cs/0703110, which identifies itself as v4 of6June2013. The version-suffixed endpoint was temporarily disabled but the base PDF succeeded. Read printed pages20–21,59,67–68. Equation22 and Section3.1 give the adopted Hecke convention; Definition11.1/equation93 defines the generator. Section11.8 states generic dimension114, displays the nine simple-module dimensions, and reports a word computation reaching degree9. The current selected-minor computation is new reproducible evidence for the specified words; the upper dimension remains the cited primary input. Local fetched PDF SHA256cc28f69ca06c0c5e43c30b2cf801a1134712a596c87e74bff2ade1c49fb41638. No fetched PDF or extraction is included in the returned archive.
