# Intrinsic exceptional top quotient: exact source scope

Research record, 19 November2026,17:43UTC. This record supplies no new numbered theorem, vanishing claim, or movement assessment. It follows the finalized C.3bm–C.3bn endpoint reduction.

## 1. The current mathematical question

Under C.3bn's stated hypotheses, the remaining group is the top gamma part of K0(E)_Q modulo actual endpoint differences of perfect families on E times a **smooth proper curve**, together with the actual exceptional cycle image. Ambient two-endpoint lifting is proved. Neither a full prescribed-family K0 lift nor vanishing of its fixed-product negative-K obstruction is required for this comparison.

One must still compute the intrinsic proper-family subgroup. A comparison with a Chow or motivic group modulo rational equivalence does not by itself compute it. An algebraic part defined using arbitrary smooth connected parameters is also not automatically this subgroup. Even for the elementary global-units functor, proper connected parameter curves have constant units and hence zero endpoint differences, whereas the coordinate on Gm realizes every difference of two nonzero scalar values. This is a relation-theoretic distinction, not merely a choice of terminology.

## 2. Binda–Krishna2022: what was actually read

Binda, F., & Krishna, A. (2022). Zero-cycle groups on algebraic varieties. *Journal de l'École polytechnique — Mathématiques, 9*,281–325. https://doi.org/10.5802/jep.183 . Full primary PDF: https://www.numdam.org/item/10.5802/jep.183.pdf .

Freshly opened/read: introductory Theorems1.1–1.2 and1.6; Section7 setup and Lemma7.1 on pp313–314; Definition7.5, Lemma7.6, and Proposition7.7 statement on pp316–317; Lemma8.1 and the modulus setup on p319; Theorem8.3 and its complete induction proof on pp320–321; and Theorem8.4 with its complete proof on pp322–323. The complete proof of Proposition7.7 and every intervening Section7 lemma have **not** been freshly checked in this research window.

Theorem8.3 gives a map from the modulus zero-cycle group of a component to the Levine–Weibel group of the normal-crossing union under condition(8.1). Theorem8.4 identifies the latter with top cdh/Friedlander–Voevodsky motivic cohomology after inverting p in positive characteristic, and in the stated invertible finite coefficients. Its proof uses the two explicit EKW rational relations: a function equal to one at the component boundary, or a function invertible at the nodes of an SNC subcurve. The comparison is a rational-equivalence theorem. It does not assert that arbitrary such parameter families are compactifiable to actual perfect families on E times a proper curve, and it does not compute our proper-family subgroup.

The full PDF and extracted text are retained as `../../sources/binda_krishna2022_zero_cycles.pdf` and `.txt`. Acquisition provenance, byte count, hash and elapsed time are in `output/intrinsic_quotient_source_manifest.json`.

## 3. Kohrita2024v3: the parameter-class distinction is explicit

Kohrita, T., with an appendix by B. Kahn. (2024, April10). *The algebraic part of motivic cohomology* (arXiv1512.02320v3). https://arxiv.org/pdf/1512.02320v3 . The original2015 title in search metadata differs; this record uses the actual title/version of the opened35-page PDF.

Freshly read: introduction; Section2.1 pp4–5; Definition2.3/Proposition2.4, Definition2.5/Axiom2.6, Lemma2.9 and Proposition2.10 with their proofs, pp6–8; Lemma3.14 and Lemma3.15 with their displayed proofs, pp23–25; Remark3.16 and its complete argument, pp25–26; Theorem3.17 statement and its proof pp26–27. The entire paper, and the appendix's theorems, are not claimed as independently audited.

Definition2.3 allows an arbitrary chosen class of smooth connected parameter schemes. Its designated algebraic part uses all smooth connected quasi-projective parameters. Proposition2.10 reduces that part to multiplicative families on semiabelian varieties. It does **not** replace them by abelian varieties or proper curves in general.

The exact place where the classical proper conclusion is proved is Remark3.16. There X is smooth proper. Removing one torus factor uses an associated line bundle over the lower-rank semiabelian variety, and the proof explicitly invokes surjectivity of ordinary Chow restriction from the whole line bundle to its nonzero locus. This is the precise step that is unavailable merely from a singular exceptional perfect-K0 comparison. It would be circular to use that remark to solve the present compactification/gluing issue.

Theorem3.17 yields universal regular semiabelian quotients in its index range. Existence of a universal regular homomorphism does not identify its kernel or replace the stipulated parameter class. No equality with our J_K is inferred.

Retained full PDF/text: `../../sources/kohrita2024_algebraic_part_v3.pdf` and `.txt`.

## 4. Levine2026v1: a new actual primary source, with limited read scope

Levine, M. (2026). *Riemann–Roch for 0-cycles on a singular variety* (arXiv2609.32599v1). https://arxiv.org/pdf/2609.32599v1 . The arXiv version is stamped26September2026; the manuscript title page is dated29September2026. This is a74-page preprint, not silently treated as a published article.

The full primary PDF was obtained directly after the web PDF/HTML routes failed. Local file `../../sources/levine2026_zero_cycle_RR_v1.pdf`,869676bytes,SHA25651856a95c8ae8c481813d2bf185f388daad58c180eaae3c3949b6f567629a1b1. The acquisition manifest `output/levine2026_RR_access.json` records the actual9.763574852-second operation beginning17:29:36.575308UTC.

Read: introduction and Theorem1/Corollary pp1–4; Definition2.1 and conditions(2.1), Theorem2.3 statement and Remark2.4 pp15–17; complete displayed proof of Theorem2.3 pp23–25. The intervening supporting lemmas and full Riemann–Roch proof have not been independently read, and the source is not used as a new numbered-proof input.

Theorem1's target F^dK0 is expressly the subgroup generated by regular closed-point classes. It is not identified with the entire top gamma subgroup merely by that theorem's notation. The cycle map/Chern inverse is up to the displayed factorial. Theorem2.3 gives a formulation of **rational equivalence** by admissible curves in X times P1. It supplies no theorem about the required proper-curve algebraic equivalence of all perfect classes. The surface case may agree with familiar SK0 descriptions under separate inputs, but that does not remove the family issue.

## 5. Exact current conclusion and useful next test

No source inspected in this block supplies the missing intrinsic proper-perfect-family theorem. The actual restrictions at triple strata remain the concrete obstruction: a moving edge divisor times a scalar unit can restrict to a nonzero class in K1(P), even though its endpoint restriction to K1(k) has zero corresponding higher weight. Relations on separate strata therefore cannot be declared compatible solely from endpoint compatibility.

Kohrita's explicit semiabelian formulation suggests studying the torus-extension contribution, but no motive factorization, Albanese-kernel vanishing, or identification of the proper-family quotient with an affine algebraic group has been proved here. C.3bo's separately audited weighted isogeny removes the component Albanese coordinates by actual exceptional Poincare families; it does not remove the remaining component Albanese kernels or triple-stratum compatibility.

Source-acquisition program: `code/acquire_intrinsic_quotient_sources.py`; full provenance manifest: `output/intrinsic_quotient_source_manifest.json`. The two-source run took21.781646244seconds, completing17:38:31.874392UTC. It is an acquisition record, not a mathematical certificate. Primary web refs were freshly opened; no metadata-only page is used as proof evidence.

## 6. Follow-up primary readings,18:30–18:36UTC

The earlier dated source limits remain historical. The ESV1999 read was extended at18:30:42UTC through Definition1.7 and the full proof of Lemma1.8 (printed602), Lemma1.10 and Corollary1.11 with their proofs (printed603–604), and the full proof of Lemma1.12 (printed604–605), in the primary PDF at https://userpage.fu-berlin.de/esnault/preprints/ec/inv99.pdf . Lemma1.12 explicitly uses generalized Picard groups of admissible projective curves to generate the degree-zero singular Chow group. These connected algebraic groups can be nonproper. The result is a criterion for regular homomorphisms; it does not replace their parameter groups by actual proper perfect families. In particular, proving that a torus subgroup has zero image after a pushforward would not by itself produce an actual family on the abelian quotient. No full-paper ESV audit is claimed.

At18:32–18:35UTC the full Kohrita v3 was reopened, including the exact Definition2.3 and Remark3.16 passages described above. Its arXiv metadata now confirms the journal reference *Pure and Applied Mathematics Quarterly20*(6)(2024),2667–2710. This is a publication-metadata check, not a fresh reading of the published44-page layout. The opened35-page v3 remains the proof source. The v1/v2 PDF and HTML browser routes returned access errors; their abstract pages do not count as theorem evidence. A separate retained acquisition program is attempting the historical v2 so that any older proper-parameter formulation can be checked rather than inferred from search snippets.

These literature checks do not supersede the separately proved C.3br/C.3bs component-family results. The new marked edge-family construction and its totalization consequence are being audited separately; no status change is inferred from these source observations.
