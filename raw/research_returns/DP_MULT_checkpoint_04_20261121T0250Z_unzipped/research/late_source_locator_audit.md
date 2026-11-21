# Integrated DP36 preservation and late source-locator audit

Reviewer: `/root/archive_binomial`, GPT-6 Astra Pro, inherited model; effort not exposed. Date: 2026-11-21 UTC. Actual reading interval: **01:41:32--01:44:06 UTC**. Events **ABA-CE31** (DP36 preservation) and **ABA-CE32** (targeted source audit). Main paper remained read-only.

## Outcome

**Integrated DP36 preserves the reviewed draft's mathematical content. The source audit found no incorrect numbered locator in DP30--DP34 or DP36.** The useful citation tightenings below are source-navigation improvements, not repairs to a false theorem citation. In particular, the previously missing dual-dimension reference in DP32 has already been restored.

This is a targeted citation audit and an integration-preservation check. It is not a fresh independent whole-proof audit of all six propositions/theorems. Their earlier actual mathematical checks remain separately recorded.

## DP36 preservation

I read the entire integrated statement and proof and compared every argument with the complete draft checked in ABA-CE30. The hypotheses, component weights, character relation, repeated-variable quantization, inverse substitution, logarithm threshold, coefficient extraction, scaling by $p$, multiindex factorial estimate and selected path estimate are all retained. The standing convention at the start of the paper supplies the perfectness of $k$ that was explicit in the draft.

The integrated version replaces the draft's elementary binomial proof by an internal reference to **DP29**. I read that complete referenced paragraph: it contains precisely the non-$p$-power digit argument and the $p$-power binomial identity needed here. Thus the reference is valid. The explicit sufficient-estimate qualification remains in the statement, and the adjacent scope text retains the unresolved geometric realization and optimality issues.

Exact integrated whole-block SHA-256: `6d271f98b2f952c441994eb8379baa439ec05e21399683769713962379bb93c0`.

Complete proof-only SHA-256: `ef2e3a991e97e17d6cf0bcfa9d6ae4c0fbc9eb5ed30518e694cb9e235de4d47b`.

The block starts at its proposition environment and ends at the complete proof environment with one trailing LF; it has 4,455 UTF-8 bytes. Snapshot: `late_proof_snapshots/DP36_integrated_archive_checked.tex`.

## Exact source findings

| Use | Current locator | Audit result |
|---|---|---|
| Finite Cartier duality and preservation of exact sequences in DP30 | Tate 1967, §§1.2--1.3, pp. 159--160 | Correct. The relevant statements are unnumbered. I re-read both sections in the primary extracted text, including the explicit assertion that the dual of an exact sequence is exact. No theorem number should be invented. |
| Frobenius/Verschiebung factorization in DP30 | Tate §2.2, diagram (3), pp. 163--164 | Correct. I rendered and directly viewed the original spread with printed pp. 162--163. The diagram on p. 163 is visibly labelled **(3)**; the OCR's occasional different digit is unreliable. |
| Formal-group correspondence and connected component in DP30/DP32 | Tate §2.2, Proposition 1, p. 162; equation (4), p. 164 | Correct. Proposition 1 begins on printed p. 162 and its proof continues through p. 164. The hypotheses cover the complete noetherian local bases in these uses. |
| Dual dimension in DP30/DP32 | Tate §2.3, Proposition 3, p. 166 | Correct. The explicit DP32 citation was restored in the previous version check and is present. |
| Display equivalence in DP31 | Zink, Theorem 9 or Theorem 103 | Correct numbered results. I re-read the primary statements. Theorem 9 is on printed **p. 132**, Theorem 103 on **p. 221**. The rings $W(k)/p^n$ satisfy the hypotheses. |
| Formal biextension injection in DP31 | Published Zink §4.4, Proposition 121 and (243), pp. 241, 246 | Correct. I re-read Proposition 121 and the sentence following (243): the map is always injective. Only that direction is needed. Theorem 122's stronger isomorphism is not silently used. |
| Dual-display Frobenius/Verschiebung interchange underlying DP31 | Currently attached to the cited duality framework | A useful local citation is **Zink Definition 19, (22)--(24), pp. 143--144**, read directly in this audit. The equations state the dual operators and their pairing relation. Add this for precision next to the dual-display/complementary-slope statement; retain Proposition 121 for the formal dual and biextension identification. |
| Vanishing of rational Hom for distinct slopes in DP31 | Katz 1979, §1.3, first paragraph of p. 120 | Correct. I directly viewed the original printed p. 120. It explicitly states the semisimplicity and simple objects after passage to an algebraically closed field. The classification statement is **unnumbered**. Number **1.3.1** on the same page concerns slope multiplicities and is not the correct replacement locator. |
| Integral logarithm/group construction in DP32 | Hazewinkel, Lemma 2.3, (2.2)--(2.6), p. 74 | Correct, as directly read in the original text/images during ABA-CE27. The matrix hypotheses include the displayed choices. |
| Congruence of the $p$-series in DP32 | Hazewinkel (2.8), p. 75 | Correct; this is the separate congruence equivalence in Lemma 2.3. |
| Lubin--Tate uniqueness and identification in DP32 | Hazewinkel §5, pp. 76--77, (5.1)--(5.4) | Correct. The uniqueness/strict-isomorphism statement occurs in the paragraph immediately after (5.1), printed p. 77; (5.2)--(5.4) provide the logarithm construction and reduction. The main-text locator correctly includes both. |
| Translation-operator, affine, witness and weight calculations in DP33/DP34/DP36 | Internal results DP32, DP33 and DP29, followed by explicit calculations | No omitted external theorem was found in these new calculations. DP36's internal binomial reference was specifically verified. These short calculations are the claimed model-specific forms, not long uncited reproductions of the classical source theorems. |

## Suggested citation edits, without mathematical changes

1. In DP31, strengthen the dual-display sentence with `\cite[Definition 19 and (22)--(24), pp.~143--144; Proposition 121, p.~241]{Zink}`. This makes the dual-operator and slope step easier to check from the exact source.
2. Optionally expand its equivalence citation to `\cite[Theorem 9, p.~132, or Theorem 103, p.~221]{Zink}`. The existing theorem numbers are already unambiguous.
3. In the Hazewinkel bibliography annotation, reflect all the clauses actually used: “Lemma 2.3, (2.2)--(2.8), pp. 74--75; §5, (5.1)--(5.4), pp. 76--77.” The main-text citations are already complete; the shorter existing bibliography annotation is not a false citation.

Keep the published Zink numbering **(243), p. 246**, distinct from the author-version numbering recorded in the bibliography. Keep Katz's classification locator explicitly unnumbered. No change to the mathematical statements or proofs is recommended by this audit.

## Version records and preservation limits

The six exact audited blocks, their individual SHA-256 hashes and extracted citation strings are preserved in `late_proof_snapshots/source_audit_DP30_34_36.tex` and `source_audit_DP30_34_36.json`.

| Block | SHA-256 |
|---|---|
| DP30 | `32eed2415e3ac16810d3e3e13973131df45e83e948979ba7395f6f698ff49b3a` |
| DP31 | `84bf7014febae0988bb54b2055d90cce452cef0e6cd97a376ddd630ddd6d81d0` |
| DP32 | `8a4b04104fe06d196f3ec0402270a7326c7931b3ded661bc28ded6a8702075a4` |
| DP33 | `79168ae11d5d8e2af3acd39c1b56e3820ed50aaca6c52eb1e9fc3a3320fe6bc4` |
| DP34 | `eb5be984ea9f34075f00480ee997f6d19af47421ba58b48ed0feb9328502c110` |
| DP36 | `6d271f98b2f952c441994eb8379baa439ec05e21399683769713962379bb93c0` |

The current DP31 differs from its earlier whole-proof snapshot only by the explicit Katz classification explanation and citation; I read that exact diff. The mathematical argument checked earlier is unchanged. Later root edits do not retroactively change these versioned records.
