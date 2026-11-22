# Post-checkpoint 14 research and restoration record

Restoration verified at 2026-11-20 01:11:47 UTC. The prior workspace was absent. We restored checkpoint 14 only; we did not unpack the original attached ZIP again.

Checkpoint 14: 88,120,353 bytes, 892 entries, SHA-256 d4e32738bf1f9f6131d6d6beae4f1216cc6b74f574ea6c35f1b6f0743d323221. ZIP CRC passed. Its last verified paper is build31d, 345 pages, PDF SHA-256 1311152d5526ca4b56ca7ac52de169281e92a5f5b6970f83c995127aacd32ccd. We checked that every source hash in its visual-QA record and the PDF hash still match after restoration.

## Actual checkpoint attempts during the outage

| Number | Attempt time UTC | Outcome |
| --- | --- | --- |
| 15 | 2026-11-19 22:19:22 | Execution unavailable; no archive created or saved. |
| 16 | 2026-11-19 23:04:04 | Execution unavailable; no archive created or saved. |
| 17 | 2026-11-19 23:49:02 | Execution unavailable; no archive created or saved. |
| 18 | 2026-11-20 00:34:06 | Execution unavailable; no archive created or saved. |

The next scheduled archive is checkpoint 19 at 2026-11-20 01:19 UTC. We preserve the verified build31d without claiming that it contains the subsequent results. Newly restored proof sources and audits are checkpoint payload even before their integration into the paper.

## Scheduled review history restored from the conversation

Reviews 1–8 remain in the restored ledger. The recorded movement sequence through review 12 is YES, YES, NO, YES, YES, YES, YES, YES, NO, YES, YES, YES.

- Review 9, scheduled 2026-11-19 22:04 UTC: no qualifying movement. The exact review timestamp is not retained in this restoration summary and is not invented here.
- Review 10, scheduled 2026-11-19 23:04 UTC: qualifying movement from the fully audited A.147/A.148 regularity and pair criteria. The exact separate review timestamp is not retained here.
- Review 11, actual 2026-11-20 00:04:19 UTC: qualifying movement from A.152, which reduced the named main comparison gate. Consecutive reviews without movement reset to zero.
- Review 12, actual 2026-11-20 01:05:09 UTC (scheduled 01:04): qualifying movement. A.154 closes real higher surjectivity, including the named pi2(T6) instance; A.156 closes real PL-to-definable injectivity in dimensions three and four; A.158 closes the all-RCF compact-graph Lipschitz-resolution input. Consecutive reviews without movement: zero.

The next review is scheduled for 2026-11-20 02:04 UTC. No original outcome row has changed: A.1(b), the unresolved maximal-locus part of A.5, and C.2(b) remain open.

## Complete audited results obtained after checkpoint 14

The following are proof/audit facts from the conversation, not claims that build31d already contains these statements.

- A.142–A.143: component obstruction and homomorphism for three-dimensional bases. Pre-promotion full drafts were recovered inside checkpoint 14.
- A.144–A.146: finite-fundamental-group realization, supported realization in summands, and the three-torus component-class vanishing. Their proofs require reconstruction from recorded arguments where literal earlier text is absent.
- A.147: forward parameter-Lipschitz sufficient criterion. Root full proof audit 2026-11-19 22:57:10 UTC.
- A.148: common-data factor-pair criterion. Root full audit 2026-11-19 23:03:32 UTC; independent audit recorded.
- A.149: transfer of sufficient criteria to theories with a real model; explicitly reconstructed and fully audited 2026-11-20 00:25:39 UTC.
- A.150/A.150H: one-parameter clock and Hausdorff version. Root full audit 2026-11-19 23:09:04 UTC.
- A.151: explicit family not regularizable by any parameter homeomorphism; nullhomotopy and noninjective regularization retained. Root full audit 2026-11-19 23:23:23 UTC; item 5 at 23:32:38 UTC. The exact finite checks must be saved/rerun with code.
- A.152/A.152G: real relative compact-graph regularization and exact comparison gate. Root full audit 2026-11-19 23:46:56 UTC; independent audit 23:49:05 UTC.
- A.153: real-model transferred graph-regular representative, not a literal nonreal reparameterization claim. Reconstructed full audit 2026-11-20 00:25:39 UTC.
- A.154: simultaneous spatial Lipschitz factors over every fixed o-minimal RCF; real PL-to-definable surjectivity in every degree. Root full audit 00:08:48 UTC; independent full audit 00:12:33 UTC.
- A.155: real weak equivalences outside dimensions three and four, and transfer corollaries with explicit real-model hypotheses. Root full audit 00:17:52 UTC; independent full audit recorded.
- A.156: exact relative PL extension over the reals; PL-to-definable weak equivalence in every dimension. Root full audit 00:36:24 UTC; both proof portions independently audited.
- A.157: finite universal homotopy-equivalent resolution into a fibrewise join over arbitrary o-minimal RCFs. Root full audit 00:43:26 UTC; independent full audit recorded.
- A.158: compact Lipschitz resolution, with standard integer bounds for Hausdorff families over arbitrary o-minimal RCFs. Root full audit 00:52:27 UTC; independent full audit recorded.
- A.159: all-field higher surjectivity via standard bounds and finite target constructions. Root read all four complete parts and passed the full proof at 01:14:14 UTC, with moving-band range 0<=j<R-1 and the marked-star inference made explicit. Independent audit pending at that time.
- A.115: the actual earlier full proof was recovered in parts/parametric_concordance.tex and rechecked in full at 01:13:14 UTC. The separate 11,721-character A.115R source is an independent fresh reconstruction; it is supplementary proof documentation, not a replacement or a second claim of priority.

A.160, arbitrary-field injectivity using real-algebraic PL boundary representatives, is in progress and is not promoted in this record.

## Source verification and limits

We reopened Shiota arXiv:1002.1508, Lemma 1.1 p.2, Lemma 1.2 pp.3–5, and Theorem 2.1 p.5. We reopened Mnev arXiv:0708.4039v3, Propositions 4–5 pp.21–23, Lemma 3 pp.24–25, Proposition 36 pp.62–63, Lemma 8 pp.67–68, and Proposition 57 pp.89–90. The marked seam-pair use is derived from conic-star invariance and local flatness; it is not quoted as a separate literal assertion of Proposition 36.

A.157 uses Barton–Commelin, arXiv:2108.11952, Proposition 6.17 p.29 (closed-by-proper pushouts and pullback stability), Proposition 8.5 p.47 (HEP), Proposition 8.6 pp.47–48, and Propositions 9.28 and 9.31 pp.60 and 63.

A.158 uses Kocel-Cynk, Pawlucki, and Anna Valette, C^p-parametrization in o-minimal structures, Canadian Mathematical Bulletin 62 (2019), 99–108, DOI 10.4153/CMB-2018-030-x. The introduction p.99 explicitly includes arbitrary real closed fields; the generic C1 boundary-extension claim in the proof of Lemma 2.4 is on pp.102–103. The 2014 Kocel Hausdorff paper was not silently extended beyond its stated real scope.

Fresh publisher/JSTOR, author-profile, filtered-PDF and thesis searches still did not yield the required original Hartshorne 1968 Proposition 4.3/Theorem 7.5 or Ogus 1973 section 3. Metadata and later citations do not close C.2(b).

All work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). We make no priority claim.

