# PSL3(4): complete compatible-normalizer coverage

**Status:** authored proof complete, author whole-proof read; independent whole-proof and primary-source audit by `/root/imprimitive` passed at frozen proof SHA-256 `b6a53359d99547f2ed8f302f168771e37a30055a79f6d4d89378c07b646cd2c8`. The reviewer separately reconstructed all 20 kernels, eight orbits and 36 pairs. Their report is `agents/imprimitive/audit_l34_normalizer/PEER_AUDIT.md`. The exact finite multiplier count has actually run and passed. The character-table spectrum scan belongs to the root agent and is not claimed as this agent's independent work.

`normalizer_coverage.tex` contains the complete argument and `normalizer_bibitems.tex` its primary citation. The proof uses Breuer–Malle–O’Brien (2017), §3.3.1 and Lemma 3.1, which lists exactly 36 bicyclic extensions up to isoclinism. The whole invoked argument was read on author pages 5–6. Publisher metadata confirms *Contemporary Mathematics* 694 (2017), 21–31, DOI 10.1090/conm/694/13960. Author pagination and published metadata are stated separately.

The new proof fills the representation-theoretic gap: isoclinism identifies the perfect derived groups and their conjugation actions; irreducible representations invariant under a cyclic extension extend after rescaling one operator. Thus every actual compatible normalizer spectrum is present in a listed table, up to a scalar, among rows whose core restriction is irreducible. No characteristic-kernel assumption, cyclic-center shortcut for the universal cover, or claim that isoclinism preserves character tables is made.

The complete table inventory is:

| Perfect core | Outer extensions, in addition to the core | Count |
|---|---|---:|
| L3(4) | .2_1, .2_2, .2_3, .3, .6 | 6 |
| 2.L3(4) | .2_1, .2_2, .2_3 | 4 |
| 3.L3(4) | .2_1, .2_2, .2_3, .3, .6 | 6 |
| 4_1.L3(4) | .2_1, .2_2, .2_3 | 4 |
| 4_2.L3(4) | .2_1, .2_2, .2_3 | 4 |
| 6.L3(4) | .2_1, .2_2, .2_3 | 4 |
| 12_1.L3(4) | .2_1, .2_2, .2_3 | 4 |
| 12_2.L3(4) | .2_1, .2_2, .2_3 | 4 |

`check_multiplier.py` independently enumerates all 48 central characters, their 20 distinct kernels, eight outer kernel orbits, and all 36 simultaneous kernel/cyclic-outer-subgroup orbits. It imports no character-table arithmetic. The two order-four kernel orbits are deliberately unnamed: the source's centralization prose conflicts with its displayed action, but completeness of the full list is unaffected. The proof records and bypasses that discrepancy.

`check_input_coverage.py` checks that all 36 names are present in the root's retained input and validates the 28 normal core fusions by orders, identity kernel, and class-size unions. This is structural consistency checking, not a character-spectrum reconstruction. Its JSON records the exact input hash read.

## Primary source retained

- Author PDF: https://agag-malle.math.rptu.de/~malle/download/atlas.pdf
- Local: `../sources/BreuerMalleOBrienAtlas.pdf`
- SHA-256: `0f619a98eb52cdb2622b6c4fa6a71d1c454442c1d141ab77d18f28bdf4d3512f`
- Retrieved successfully through the local HTTP client. Browser PDF opening timed out; the complete local PDF was converted and read.
- Publisher metadata: https://doi.org/10.1090/conm/694 and article DOI above.

No new finite-group classification or independent reconstruction of the root's numerical eigenspace bounds is claimed.
