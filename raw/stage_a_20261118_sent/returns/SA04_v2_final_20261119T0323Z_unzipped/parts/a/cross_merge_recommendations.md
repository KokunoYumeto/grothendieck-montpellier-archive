# Cross-stream duplicate review

Reviewed on 2026-11-19 against the current A, B and root item/claim JSON files. Recommendations below preserve the source-entry coverage and distinguish an exact duplicate from a consequence or a change of hypotheses. The A/B recommendation was agreed with notes_93_b. No other stream's files were changed.

## Exact claim merge

| Old claim | Canonical claim | Additional source to preserve | Required preservation |
|---|---|---|---|
| C-SA04-217 | C-SA04-122 | Cote93, scan80, `pro/MPL_93_047-091_transcription.tex:1286–1292` | Add the three displayed substitutions: multiplication by a base unit, addition of a base section, and inversion on the nonzero-coordinate locus. Keep their relative/base-coefficient condition. Append B's statement and its reference/check-event provenance; do not replace the integral certificate by a characteristic-zero citation. |

This is exactly the projective invariance already contained in C-SA04-122. The all-base three-jet identity and the Möbius zero calculation establish the shared claim. This merge does **not** absorb C-SA04-218, the separate ordinary-differential degeneracy criterion.

## Item and entry reassignment

SA04-217 currently combines two note entries with distinct assertions. The preferred consolidation is to split that grouping at the source-entry level, rather than to transfer its entire statement into a construction item.

| Source entry | Old item | Canonical item | Action |
|---|---|---|---|
| MPL_93_047-091#205 | SA04-217 | SA04-153 | Merge the repeated projective-invariance assertion into the integral-construction item. Add scan80 and lines1286–1292, preserving the relative base coefficients. |
| MPL_93_047-091#206 | SA04-217 | SA04-217 | Retain the item ID for the separate `df=dg` criterion. Restrict its statement, quotation and lines to the marginal assertion at Pro80:1294–1297 and its characteristic-zero scope; preserve the characteristic2/3 counterexamples. C-SA04-218 remains attached here. |

Thus there is no unconditional whole-item alias `SA04-217 → SA04-153`: only entry#205 is reassigned. The claim alias is unconditional because C-SA04-217 itself contains only projective invariance. For historical check events referring to the old bundled SA04-217, preserve the original event and identify which substatement it checked, instead of silently relabelling all such events as construction proofs.

## Closely related records that should remain separate

| Records | Why they should not be merged |
|---|---|
| C-SA04-121 and C-SA04-201 | A's claim classifies rational analytic coordinate cocycles with a quadratic target; B's claim allows an arbitrary coherent natural recipient and admits the unused-direct-summand objection. The target quantifier differs. |
| C-SA04-122 and C-SA04-202 | An identity `G=12G0` is different from pushout of a torsor by multiplication by12. The latter need not be an isomorphism when12 is not invertible. |
| C-SA04-123 and C-SA04-203 | Integral all-base universal uniqueness is different from uniqueness in one fixed characteristic under the margin's nonvanishing and order restrictions. |
| C-SA04-122 and C-SA04-218 | They share the test coordinates `t+t²` and `t+t³`, but C218 is the stronger proposed criterion based on equality of ordinary differentials. Keep it and cross-reference the existing computation. |
| C-SA04-120 and C-SA04-204 | The real C³ formulation changes the analytic category and the regularity of the output. |
| C-SA04-120 and C-SA04-252 | The local coordinate/torsor construction and the transverse connection/PGL2-oper description use different input objects and include different existence and invertibility assertions. Cross-link the two presentations. |
| C-SA04-120/122 and root C-SA04-609 | The exponential composition is a separately recorded explicit computation, including an intermediate coefficient corrected on the same leaf. Retain that correction history and the source's special formula. |
| C-SA04-120 and root C-SA04-610 | The latter is a global boundary condition with simple-pole lattice `K²(D)`, not merely the local quadratic-differential torsor. |
| C-SA04-120/122 and root C-SA04-611 | The Riemann–Roch dimensions are additional global computations depending on genus and the boundary divisor. |
| C-SA04-120 and root C-SA04-612 | Translation invariance on a genus-one torsor and the separate flat-implies-invariant question are not assertions of the local projective-coordinate theorem. |
| A's anonymous exercises C-SA04-34–47 and root C-SA04-608 | Root's detached mean-ergodic/Banach fragment on scans32/34 is a different text from the cancelled factorization/resolvent/Liouville exercises on scans50/52. Similar Banach vocabulary is insufficient for a merge. |

Root C-SA04-601–605 concern the printed Weierstrass formulaire, its exceptional automorphisms, modular forms and the formal-j quotient question. None is an exact duplicate of an A claim. Root C-SA04-606–607 concern the orientation offprint and the four-dimensional annulus theorem; A's Euler and conical-triangulation claims concern different invariants and questions. No claim or item alias is recommended for those ranges.

## Bibliographic checks and small corrections

1. **RDeligne1968 title.** I independently opened the IHES catalogue URL already used by root, `https://archives.ihes.fr/document/M_68_28.pdf`. It is a catalogue page, not an extracted PDF. It gives **Courbes elliptiques : Formulaire d’après J. Tate**, author Deligne, date1968, identifierM/68/28. Recommend that exact title for the bibliography, in place of “Formulaire de théorie des courbes elliptiques.” The source leaf's wording remains unchanged. Root's separation of circulation1968 from publication1975 is appropriate.
2. **RDeligne1975.** The opened Antwerp image-index page, `https://www.wstein.org/Tables/antwerp/deligne/`, identifies **Courbes elliptiques: Formulaire (d’après J. Tate)** and the page sequence53–73. No title discrepancy was found. I did not independently establish the year from that index; root's opened edition evidence supplies1975.
3. **Wanderley.** The primary supplied K93-11 scan28, line205, prints **Marcus Wanderley** and the issue date19January1981. Root's bibliography and itemSA04-606 use that name correctly. The `his_statement` field of root C-SA04-607 currently says “J. Wanderley”; change that attribution to Marcus Wanderley or quote the actual mathematical phrase instead. This is a source-text correction, not a new external identification.
4. **RdeJongICM1998.** Reopening the EMS primary PDF confirms **Barsotti–Tate Groups and Crystals**, ICM1998 volumeII pp259–265. The generic extension Theorems1–3 are in **§3, p261**; the ordinary-crystal counterexample is **§2(x), p261**. Root's distinction of these locators is correct. I corrected A's reference locator to include §3 explicitly.
5. **Reference aliases for final assembly.** `Groth1966` and `RGroth1966` are one work; `deJongICM1998` and `RdeJongICM1998` are one work; `SGA7I` and `RSGA7I` are one work; `Deligne1970` and `BDeligne1970` are one work. Preserve the union of opened URLs and exact locator/verification notes if choosing one canonical key. The original SGA 7 I scan was subsequently retrieved from SLMath/MSRI and its IX5.8–5.11 passages were read at printed pages382–386, with visual checks of the characteristic qualifications. See `SGA7I_primary_memo.md` for exact pagination and the distinction between the published proof and its cited unpublished Raynaud inputs. This supplies an exact primary publication match for root C-SA04-672/673. The AI-edited text page remains only a discovery aid; the original introduction was not independently collated.

The quick bibliographic pass was confined to the relevant overlaps. It is not an independent audit of every root reference.
