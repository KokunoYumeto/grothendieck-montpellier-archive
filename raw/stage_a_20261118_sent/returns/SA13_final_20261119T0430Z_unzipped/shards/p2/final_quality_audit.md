# Final quality audit — p2

**Review date:** 19 November 2026. **Disposition:** complete; no further correction identified in this final audit. All p2 writes stop after this report is saved, so the parent can assemble and hash the archive.

## Scope and limits

This final pass checked concrete classification, hypothesis, source-attribution, and cross-reference risks in the assembled claims, the revised root Codex records C-SA13-600–670, the p2 records, and the complete `SA13_dossier.md`. It followed the already completed full reading of the p2 Pro package, Codex K34-01–04, and the K34-12 weights passages. It was a targeted quality audit, not a new general literature search or a claim that every unresolved source-identification problem has been solved.

The underlying p2 review retains all 113 indexed source-entry verdicts. The added Codex-only objects represent actual distinct source leads and do not manufacture new Pro verdicts. Exact text collation, identification of a source family, independent proof, and a modern comparison theorem remain separate kinds of evidence.

## Corrections implemented in p2

| Record or file | Completed correction |
|---|---|
| C-SA13-198 | Replaced the inaccurate restriction to finite field extensions by a generic-parameter field extension, a suitable dominating valuation, and subsequent finite extensions as needed. The Grassmannian function-field extension is generally transcendental. The open-image condition on inertia remains the separate C-SA13-227. |
| C-SA13-203–204 | Changed class A to class C and retained medium confidence. The verified geometric semisimplicity ingredient is distinguished from the uncollated exact radicial constant-part adaptation in Grothendieck 1966, Proposition 4.4. This is a precise source-identification gap, not an assertion that the modern theorem is open. |
| C-SA13-157 and MP-SA13-51 | Replaced the stale assumption-mismatch account by the recovered common-completion lemma and its independently checked proof. The global canonical claim is C-SA13-064. The exact original printed source and the distinct quadratic-sequence assertion C-SA13-158 remain unresolved. |
| SA13-213–225 | Added thirteen distinct Codex-only source objects and linked the relevant claims, problems, and directions. Each has a source-summary comparison event, explicitly carried as background without fault found; these events do not assert an independent proof. |
| C-SA13-231–241 | Assigned existing source-item links; no claim in the p2 shard now has an empty `items` list. Where the existing object is a source-folio inventory, `item_relation` explicitly identifies the relation as provenance rather than mathematical identity. |
| `weights_references.bib` | Normalized all four records to `note={verified}` exactly, preserving the substantive access and scope information in `accessnote`. |
| `outputs/validation.json` | Refreshed after all substantive p2 changes. Its counts now agree with the current shard. |

The final authored patch script is `code/final_quality_patches.py`; it runs after the core and refinement builders. The relevant core claim/problem builders also retain the corrected mathematical wording. `outputs/final_quality_patches.json`, `review.md`, `directions.md`, and the progress log were updated consistently.

### Recovered completion lemma

The joined supplied source is scan 33:173, global lines 744–748, continuing to 33:137, global lines 957–983, and 33:135, global lines 908–910. Its assumptions are regular local domains of the **same dimension**, a common residue field, and extension of the maximal ideal to the maximal ideal. Under these assumptions their completions are canonically isomorphic; ideal contraction, descent of principality, and the stated fraction-field intersection follow.

The independent check identifies the regular associated graded polynomial rings, obtains the isomorphisms of all finite maximal-ideal quotients, passes to inverse limits, and uses faithful flatness for contraction. The faithful-flatness input was opened and checked directly at [Stacks Project, Lemma 10.97.3, Tag 00MC](https://stacks.math.columbia.edu/tag/00MC). That reference is a standard proof input, not an identification of the reused printed leaf. The added `Stacks00MC` entry matches the already existing p1 bibliography key and metadata. Search and check-event records preserve this distinction.

### Source-item assignments retained

| Claims | Source item(s) |
|---|---|
| C-SA13-168–171 | SA13-213 |
| C-SA13-172–179 | SA13-214 |
| C-SA13-180–183 | SA13-215 |
| C-SA13-184 | SA13-216 |
| C-SA13-185–188 | SA13-217 |
| C-SA13-189–192 | SA13-218 |
| C-SA13-193–198, 223, 227–228 | SA13-219 |
| C-SA13-199–202, 217–222, 224–226 | SA13-220 |
| C-SA13-203–205 | SA13-221 |
| C-SA13-206–208, 211–212, 216 | SA13-222 |
| C-SA13-209–210, 229 | SA13-223 |
| C-SA13-213–215 | SA13-224 |
| C-SA13-230 | SA13-225 |
| C-SA13-231 | SA13-174 |
| C-SA13-232–236, 240 | SA13-207, with the exact folio-provenance relation stated |
| C-SA13-237 | SA13-180 |
| C-SA13-238 | SA13-182, SA13-193 |
| C-SA13-239 | SA13-182 |
| C-SA13-241 | SA13-203 |

## Cross-shard corrections verified in the assembled claims

These changes were made by their owning agents or the parent. The final audit reread the current assembled records and confirmed the changes; this report does not leave them as outstanding requests.

| Record(s) | Verified final wording |
|---|---|
| C-SA13-802, 804, 809, 812, 815 | Properness is explicit for the global specialization-cone comparison or generic-fibre abutment. Local nearby-cycle constructions remain available without it. The smooth nonproper example obtained by deleting a special-fibre point from a relative projective line demonstrates why the distinction matters. |
| C-SA13-624 | The statement begins after the indicated completion reduction, over a complete noetherian strictly henselian base equipped with a Cohen-ring map. The fate attributes the deformation input to Schlessinger/Rim and distinguishes its use in Grothendieck's published exposition from independent authorship of that theorem. |
| C-SA13-311 | The authorship field now identifies a reused SGA7-style typescript matched to VIII 1.1.3–1.1.4 and 1.3.4. It does not infer the authorship or date of the physical leaf from that publication match. |

No forced identification was made between geometric and rectified étale depth, semisimplicity and Barsotti–Tate good reduction, distinct stable-model questions, or finite generation and finite presentation. These distinctions are material to the claims and problems.

## Dossier corrections and weights check

The parent applied the following concrete dossier corrections before the final pass:

| Location | Correction |
|---|---|
| §2.1 | Included C-SA13-015–018 for the qualified Künneth/projection statements and C-SA13-031 for uniform amplitude. |
| §2.2, adic paragraph | Replaced the unrelated L-function citation by C-SA13-024, 030, 034–035, with MP-SA13-06 and 08. |
| §2.3, surface claim | Stated the literal range as smooth surfaces in projective three-space of degree at least four; the Fermat quartic refutes that universal assertion. |
| §2.3, completion lemma | Restored the same-dimension hypothesis and the maximal-ideal extension condition. |
| §4.3, GIT paragraph | Used MP-SA13-205; MP-SA13-204 concerns the different inertia-weight problem. |

The complete weights discussion in §4.2 was checked against the prior saved audit. It keeps the proper normal-crossing Čech E2 statement distinct from the support/open Leray E3 statement, the arithmetic open-immersion rank r distinct from the nearby-cycle rank r−1, and the strict-base abutment over the maximal unramified extension distinct from either the original field or its algebraic closure. It retains the coinvariant Tate twist and the Tate-elliptic weights 0 and 2. Van Dobben de Bruyn's conditional equivalences are not described as a general solution, the singular/nonproper general question remains qualified by the checked Wan–Zhang comparison, and the 2026 Ito–Zou result is restricted to the verified hyper-Kähler scope.

The inline bibliography keys and fully written single object IDs in the dossier were also compared against the assembled bibliography and object/alias inventories. This check found no unresolved key or single-ID citation. The specific grouped citation corrections above were checked semantically rather than inferred from syntactic existence alone.

## Final p2 validation

The current `outputs/validation.json`, reread immediately before this report, records:

| Inventory | Count |
|---|---:|
| Indexed entries | 113 |
| Items | 121 |
| Claims | 142 |
| Problems | 49 |
| Readings | 82 |
| Bibliographic records | 44 |
| Links | 86 |
| Check events | 426 |
| Validation errors | 0 |
| Validation warnings | 0 |

The indexed entry verdicts remain 107 kept, 5 merged, and 1 corrected. Claim classes are A:27, B:12, C:20, E:67, F:16. No new Pro verdict was introduced by the Codex additions. There are no empty p2 claim-to-item lists. The parent separately reports that the assembled global validation passes with 390 items, 551 claims, 168 problems, and all 379 source-entry verdicts retained; these global counts are the parent's assembly result, not a replacement for the shard counts above.

**Final disposition:** the concrete corrections identified in this pass are saved or verified in the assembled records. The remaining bibliographic and mathematical uncertainties are stated in their existing claims/problems rather than hidden by a higher classification. No further p2 edits are pending.
