# Polygon workstream audit

Prepared by GPT-6 Astra (OpenAI), ChatGPT Pro mode, on 2026-11-19. This is an independent workstream within RESEARCH_SA11; no priority is claimed.

## Mathematical outcome

P1–P8 in `sections/A34.tex` contain the complete proofs. P4 is an exact finite image criterion, P5 refutes L3 with a fixed-base counterexample, and P6 reconstructs the weighted graph using the prescribed transport rule. P1–P3 settle R1–R3 with the precise one-class qualification in R1. P7 gives the full local sign cube. P8 supplies the exposed-fan/corridor alternative needed for the remaining same-apex generization corner in the parent A.1 proof.

The proof of P8 deliberately uses the added line itself as the infinity element: `g=d`, objective `f=i`. It requires no unproved existence of an extra infinity pseudoline. The proof applies to a new line containing exactly one old vertex, which is exactly the remaining case in the parent corner argument. No broader half-circle statement is silently inferred.

## Manuscript material independently read

We read the supplied transcription and its doubts table, rather than accepting the attached study's assertions:

- `MPL_154_001-045_transcription.tex`, scans 12–20: ordinary arrows, weights, corridor weights, polygon antipodality, injectivity, and question 2.
- Scans 17–19 give the ordinary weight `m-1`, total `2n`, corridor weight `n-m+1`, and modified supercritical weight `m-1`. These agree with P6.
- Scan 18's antipodality assertion is not itself a doubtful reading. P3 independently refutes its nonstable version and proves the exact reversal correction.
- Scan 20's question 2 asks for reconstruction of the directed weighted cellular graph from polygons. We answered that question in P6 and the stronger image question from the present prompt in P4.
- Scans 34–35 give the disk criterion. The two-packet condition appears explicitly after the disjointness equivalence condition. The doubts concern bracketed or deleted words, including antipodality/uniqueness wording. P1 proves the assertion for either reading by separating the automatic multi-class case from the necessary one-class condition.
- `MPL_154_077-126_transcription.tex`, scans 90–93, and the corresponding doubts table: reflection transport, withdrawal of an automatic valence-four assertion, and the exceptional half-circle/corridor claim. P8 proves the exact substable statement used in A.1 independently of doubtful marginal wording.

The earlier check events rechecked here are individually listed in `notes/polygons_CHECK_EVENTS.tsv`. We did not use Michel Hua's project or its Lean file in these proofs.

## Programs and scope

1. `code/polygons_certificates.py` implements exact determinants, alternating sign maps, the full signed basis-exchange test, signed endpoint extraction, and cluster expansion. It verifies the three-line antipodality counterexample and the one-class three-cap obstruction. Its original run took 0.553323 seconds. The script's initial four-line exploratory candidate was subsequently rejected as an adequate fixed-base L3 example, as described below. The corrected output is `audit/polygons_certificates_output.json`; the original output is retained as `audit/polygons_certificates_output_exploratory_superseded.json` with its status expressly superseded.
2. `code/polygons_l3_search.py` tests the direct triangle-sign condition against the fixed old chirotope. It exhausted 48 stable words for the four-element moment-curve base, 384 for the five-element moment-curve base, and 3840 for the A.1 six-line base, without finding an invalid candidate having at least three triangle candidates. For the six-element moment-curve base it found the P5 candidate at word 49. Runtime: 2.4894073799951 seconds. The full output includes signs, each local test, the GP witness and a full basis-exchange failure.
3. `code/polygons_l3_verify.py` independently checks the final P5 candidate without searching. Runtime: 0.011090514999523293 seconds. It verifies all old determinants, all twelve adjacent arc tests, exactly three accepted triangle candidates, total weight 12, and the all-negative GP relation.
4. `code/polygons_n4_supersession.py` independently verifies why the earlier four-line route was rejected: the fixed base has one triangle candidate, whereas the other moment-curve base has the three previously advertised candidates. Its exact output and runtime are in `audit/polygons_n4_supersession_output.json`.

The counts workstream separately tested the packet expansion formula over all positions in its small examples and used it to recover all ordinary specialization pairs. That is a separate computation, recorded in its own audit; it is corroboration rather than a substitute for P3's proof.

## Rejected exploratory route

The initial four-line word `(1,2,3,4,-1,-2,-3,-4)` with fixed base normals `(1,0,0),(0,1,0),(0,0,1),(1,1,1)` is globally incompatible with that base; a GP relation proves this. The same word is valid for a different four-line moment-curve base with three triangles. Those three triangles cannot be transferred to the prescribed base. The parent correctly required a stronger check, and only one of them passes the original fixed-base local test. We therefore do **not** use that four-line candidate as the refutation of L3. The six-line P5 candidate was searched and independently verified against its own fixed base throughout.

## Source access and exact locators

- **Opened:** Galashin–Postnikov, author PDF dated 2021-03-24, Definition 6.4 and Theorem 6.5, p. 25. These state all three colocalization patterns, including zeroes. We explicitly dualize nullity-two restrictions of `M*` to rank-one contractions of `M`. Proposition 6.6, p. 26, was also read.
- **Opened:** Bokowski–King–Mock–Streinu, arXiv `math/0209364`, full LaTeX source and PDF. Theorems 4–5, pp. 15 and 18–20, supply existence and uniqueness relative to the old arrangement cellwise.
- **Opened:** Richter-Gebert–Ziegler, author-hosted 24-page preprint, Sections 7.1.4 (pp. 6–7), 7.2.3 (pp. 10–11), and 7.2.4 (p. 12). We retain the support-matroid axiom as well as the three-term GP axiom; the latter alone must not silently replace the full criterion when zeroes occur.
- **Opened independently:** Sturmfels–Ziegler, published 1993 PDF, partially directed graph and path definitions pp. 30–31, Definition 3.8(i) and Proposition 3.9 p. 33, and proof of Corollary 4.5 p. 40. All wire edges in P8 are strict, so ordinary DAG source reasoning applies.
- **Opened for comparison:** Backman–Santos–Yuen, arXiv `1904.03562v3`, full LaTeX source, Lemma 2.6 p. 9. Its generic signature criterion is not used in place of the full zero-containing theorem.
- **Not opened:** Las Vergnas 1978 original. Exact-title searches (with and without accents), author/publications searches, conference-volume searches and PDF searches produced bibliographic records but no accessible original. Official Cambridge bibliography and Ziegler's bibliography give pp. 265–270; some older references say pp. 263–268. This discrepancy is recorded rather than resolved by invention.
- **Not opened in full:** BLSWZ (1999), chapters 6–7. The official Cambridge chapter metadata and table of contents were opened: chapter 6 pp. 247–280; chapter 7 pp. 281–337; Section 7.1 pp. 281–290. Theorem 7.1.8 is explicitly identified in the opened GP2021 source. No theorem text is claimed to have been read directly from the book.
- A scanned PDF reached through the misleading filename `BlandLasVergnas.pdf` was downloaded but not read successfully; it is not used as evidence.

Searches also included `oriented matroids bjorner filetype:pdf book`, `Las Vergnas Extensions ponctuelles 1978 pdf`, `Problèmes combinatoires et théorie des graphes 1978 pdf`, and author-hosted book/publication pages. We found no prior source for the specific P5 six-line word or the present polygon reconstruction formulation; no novelty or priority claim is made.

## Conventions that matter

The sign representative of the old chirotope is calibrated with the literal signed half-line labels of the fixed arrangement. In the linear model we use determinant signs of normal rows and positive affine endpoint direction `(-v,u)` for normal `(u,v,w)`. An arbitrary change of chirotope convention while holding every signed geometric label fixed is not a permitted intermediate comparison. P4 states this convention explicitly. The geometric content and the unoriented new-line position are independent of consistent convention changes.

P6 uses the manuscript's prescribed transition transport as part of the definition of the cellular map. It does not claim that an abstract unsigned cyclic rotation system by itself decides all twists of a nonorientable embedding. The parent A.1 proof supplies the endpoint-pairing convention and the independent valence-four/no-zigzag analysis.
