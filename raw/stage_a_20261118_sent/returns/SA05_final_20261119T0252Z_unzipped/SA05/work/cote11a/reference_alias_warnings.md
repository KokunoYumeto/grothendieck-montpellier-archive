# Cross-scope bibliography alias audit

Audit date: 2026-11-19. This proposal edits no source bibliography.

**Result:** 145 source records, 141 distinct keys, 19 duplicate-work groups, 20 distinct key aliases. Consolidating the unconditional groups gives **121 canonical records**. **No same-key work conflicts** were found.

The three repeated keys are `Hua2026`, `SGA1`, and `Oda1969`; their four extra occurrences are consistent. The machine-readable proposal includes source hashes, full member observations, URLs, version policy and scope-qualified aliases.

## Proposed key aliases

| Existing key | Canonical key |
|---|---|
| `ChoudhuryGallauer2017` | `R-CG2017` |
| `Deligne1968Degeneration` | `R-Deligne1968` |
| `Deligne1968Lefschetz` | `R-Deligne1968` |
| `Deligne1980WeilII` | `R-WeilII1980` |
| `DeligneMilne1982Tannakian` | `R-DM1982` |
| `EGAII` | `EGAII1961` |
| `Faltings1983German` | `R-Faltings1983` |
| `GrothStandard1969` | `Grothendieck1969` |
| `Hua2026` | `R-Hua2026` |
| `Hua2026Montpellier` | `R-Hua2026` |
| `Jannsen1992` | `R-Jannsen1992` |
| `Jannsen1992Motives` | `R-Jannsen1992` |
| `Kahn2025Descent` | `R-Kahn2025` |
| `Milne2026Report` | `R-MilneReport2026` |
| `MumfordGIT1982` | `GIT1982` |
| `MumfordGITPublisher` | `GIT1994Metadata` |
| `OpenAI2026CMHodge` | `R-CMHodge2026` |
| `StacksCorr` | `Stacks0FFZ` |
| `StacksMotives` | `Stacks0FG9` |
| `Tate1966Endomorphisms` | `R-Tate1966` |

## Warnings and decisions

- **RA-01 — preserve version:** SGA3 is the only plausible additional same-volume consolidation withheld from the automatic alias map. A fresh direct SGA3II.pdf open timed out; the prior successful re-edited-text check remains documented. Use an explicit original-versus-re-edition witness model before merging these records.
- **RA-02 — preserve locator:** Both author URLs presently show the corrected15August2012 Tannakian text. The first page says original theorem numbering is unchanged, but correction footnotes matter. Do not turn this into a claim that the uncorrected1982 typography was audited.
- **RA-03 — metadata discrepancy resolved:** The search/PDF wrapper calls2611.00244v1 Shimura Varieties; the actual first-page title is On the Hodge, Tate, and standard conjectures for abelian varieties, J.S.Milne,9November2026. The existing bibliographic titles are correct.
- **RA-04 — preserve scope:** All records use v2. Theorem1.1(graph rule) and Theorem1.2(restricted equivalence) are different nearby results, not a numbering conflict. Preserve commutative/ungraded assumptions, special Künneth and multiplicative-gauge hypotheses, the v1/v2 variance discrepancy, and author-reported versus executed formal verification. No Lean run was performed.
- **RA-05 — preserve edition:** Consolidate only within each edition. The1982 text was accessed through a mirror with incomplete OCR at3.6; the1994 publisher record proves chronology/metadata only. Neither date establishes the physical date of reused manuscript sheets.
- **RA-06 — preserve version:** Both theorem checks used arXivv4 of29May2025. Keep TAC7July2025 revision metadata separately; generic arXiv/pdf/2312.01825 is not a permanently version-pinned link. Do not silently transport theorem numbering between the two.
- **RA-07 — metadata discrepancy resolved:** Use PMIHES52(1980),137–252. Cote12c recorded erroneous volume42 on the IAS landing page; this does not identify a second work.
- **RA-08 — preserve access level:** Broad titles, metadata records, frontmatter checks and unavailable leads retain their actual verification levels. Do not upgrade them when consolidating a nearby work or series. SGA4’s URL targets ExposéIV and its direct access failed in the original scope.
- **RA-09 — preserve author role:** The scope bibliographies credit Grothendieck and Dieudonné, while Numdam’s metadata uses Grothendieck as its author field. This is an attribution convention, not evidence of different EGA works. Keep the collaborator credit explicit if normalizing to Numdam.
- **RA-10 — merge ledger carefully:** The alias map merges identities only. Keep each scope’s actual checked passages, original URLs, date/version notes and negative access results as separate observations. A provenance check is not a mathematical proof, and a broad verified flag must not erase a metadata-only or limited-proof-audit extent.
- **RA-11 — stable locator preferred:** Fresh web extraction line numbers can differ from earlier cached extraction for the same PDF. Prefer printed page, section and theorem numbers; preserve extraction source IDs and the raw saved evidence when using line locators.
- **RA-12 — external-link status correction recommended:** Delzant1962 is the only input record without URL or DOI. Its full supplied offprint transcription was read by cote11b, but no exact public original or usable primary bibliographic record was opened. Under the strict opened-link requirement, recommend note=unverified for external-reference status while preserving attached_source_read=true and the complete checked extent. Numdam Laborde bibliography corroborates the citation; zbMATH0108.04303 was blocked403, MathSciNet26:175 showed only a JavaScript shell, and Gallica access failed403. See delzant_external_reference_audit.json.

## Conditional relationship

`SGA3Publisher` describes the same original volume family as `SGA3II`, but it is intentionally excluded from the automatic map. The latter records a later re-edited witness. The separately dated `SGA3XII` is an exposé witness with its own pagination and a problematic lemma whose original ink was not collated. Preserve these distinctions before considering a shared work-level parent.

## Reproducibility

Run `python SA05/work/cote11a/audit_reference_inventory.py`, then `python SA05/work/cote11a/build_reference_alias_candidates.py`. The first program inventories supplied data; the second applies the documented manual decisions and validates counts, targets and cycles. `reference_alias_validation.txt` records the actual run. Fresh external evidence is in `web/reference_alias_web_1.json` through `_5.json`; the complete per-record observations are in `reference_audit_inventory.json`.

This is an identity/locator audit. It does not expand the original theorem verification or establish new mathematical results.
