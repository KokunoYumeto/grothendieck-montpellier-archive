# Primary source and scope log: D-OL-01–03

Checked on 2026-11-21; final author arithmetic clock 20:25:53 UTC. Checker GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION.

## GLT2024 (published version)

Robert M. Guralnick, Michael Larsen, Pham Huu Tiep, *Character levels and character bounds for finite classical groups*, Inventiones mathematicae 235 (2024), 151–210, DOI 10.1007/s00222-023-01221-5. Publisher article and complete 60-page published PDF opened; online publication 29 September 2023, volume year 2024.

URL: https://link.springer.com/content/pdf/10.1007/s00222-023-01221-5.pdf

Retained cache `cache/GLT2024_published.pdf`, 1,605,824 bytes, SHA-256 ad6f1d3bf9e0acc60220f9098033513b521f96668967002914da7d5a91ced957. The adjacent text is an unedited pdftotext extraction. Cached copyrighted source is excluded from final packaging; retrieval metadata is retained.

Whole invoked passages/proofs read: Definition 3.2(ii), Lemmas 3.3–3.4, printed pp.160–161; Theorem 3.7 and complete proof pp.165–167; Theorem 1.5 degree upper bound with proof p.167; Proposition 6.3 with complete proof pp.193–194; Proposition 7.3 and complete proof pp.198–200. The two propositions were also visually rendered to verify exponent placement and hypotheses. No re-proof of their underlying classification or Deligne–Lusztig inputs is claimed.

Corollary 4.7 printed p.174 was read to test scope. It proves nonzero highest-level constituents, not the needed irreducibility/exhaustion theorem. Therefore it does not close the remaining unbounded-natural-dimension low-level gate and is not used as a stronger premise.

## Larsen–Tiep2024

*Uniform character bounds for finite classical groups*, Annals200(2024),1–70, DOI10.4007/annals.2024.200.1.1. Full accepted author version https://arxiv.org/pdf/2403.09046 (53 pages), local ../unitary_nonweil/cache/LT2024_author.pdf, SHA-256 70d2546d2a0f01f8e701aa718201216f2b334b6cd074c12b41c2c59e0b7cdd4f. Publisher metadata independently verified in the preceding UNW work.

The complete Theorem4.4/5.5 proofs were read for UNW and the precise orthogonal/spin hypotheses of Theorem5.5 author pp.25–26 were freshly read here. The spin-support convention is freshly checked on author p.30 before Proposition6.4. We use sigma=10^-29, smaller than the explicit 1/(6507*2^21*10^18)>7*10^-29. No claim to have retrieved the typeset Annals PDF is made.

## Universal-cover boundary

Hiss–Husen–Magaard, *Imprimitive irreducible modules for finite quasisimple groups*: ordinary-cover distinction on author p.4 and complete Chapter5 Table1 printed p.35 freshly reread from the sibling source cache. All exceptional orthogonal multipliers occur at natural dimensions below10. No new proof of this published classification is claimed. No outer-automorphism description is needed: the new transitive argument uses equal character degrees and the uniform Spin/Ω theorem for every factor, rather than invariance of character level.

## New proof versus exact computation

New universal proof: the factor-degree barrier a<q^((2*10^29)d), full normalizer/tensor support3/16, actual Hurwitz obstruction e<=24, level<10^30, and spin/nonextension dimension<2*10^30. The standalone arithmetic checker checks polynomial identities and 61,900 finite level-boundary pairs, plus enormous-integer boundary substitutions; it does not enumerate any group or replace the universal proof.

First attempt to save the TeX via an apply_patch literal failed before any file was written because one added line lacked its patch prefix. It was resubmitted successfully by generating all patch prefixes. This was a file-operation failure, not a mathematical or arithmetic failure.
