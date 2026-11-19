# Independent consolidated-table audit

Date: 2026-11-19. Reviewer: cote11b. No consolidated file, original source, or old cote11b count/data file was edited. Reference aliases and the known entry-reason spelling normalization were excluded as requested.

## Result and scope

The structural cross-table checks pass. The substantive event audit found corrections that need explicit target assertions, rather than a self-reference, a `.statement` pseudo-ID, or a related theorem with different hypotheses. The supplemental files below provide those assertions and exact target mappings. Two small source/link corrections remain for central integration.

The script reads all consolidated entries, items, claims, problems, readings, links, aliases and check events. It exposes candidates; the judgments below follow reading the actual claim fields, relevant manuscript passages, saved proofs and the specified primary passages. In particular, all 56 refutation events were examined, including the actual content of their proposed targets. This audit does not claim an independent proof audit of every mathematical result in the full dossier.

The initial snapshot is retained in `outputs/consolidated_structure_audit.json`. The later read-only snapshot is `outputs/consolidated_structure_audit_latest.json`, timestamp 2026-11-19T02:44:59Z, before incorporation of this supplement. It has 380 indexed-entry rows, 260 items, 380 claims, 102 problems, 183 readings, 151 main link rows and 1,178 events. Input hashes are recorded, so these are snapshot counts, not assertions about a later build.

No duplicate current IDs, dangling entry/item/claim/problem links, bad alias endpoints, missing indexed entries, or missing item/claim check events were found. All 46 records marked false under their stated interpretation have a refutation event. The absence of direct events keyed to problem IDs is not reported as a failure: the governing event requirement is satisfied through the items, claims and cited results on which the problems depend.

## Refutation targets: repaired by a separate supplement

Files ready for incorporation:

- `refinement_claims.json`: 16 manually authored current-run refinements, SA05-C4001 through SA05-C4016.
- `event_target_corrections.json`: 25 original-event keys with a valid `refined_id` and a scope-specific reason. SA05-C75 is the current key for the merged SA05-C3016 occurrence; the premerge ID is retained.
- `refinement_search_log.tsv`: 16 exact claim mappings to already performed family searches, with primary passages reopened in this audit identified separately.
- `refinement_CHECK_EVENTS.tsv`: 57 audit events: two for each new claim and one provenance/target-repair event for each of the 25 original subjects. These are not presented as 57 new refutations or computations.
- `refinement_reference_checks.tsv`: the six primary PDFs reopened for the supplemental audit, with theorem locators and limits.
- `outputs/refinement_validation.json`: successful item/target resolution, counts and the input-claim hash.

The original local counts and records are unchanged. New assertions are marked `status_on_pages: current reconstruction`, have explicit `refines` back-references, and preserve original source attribution separately from the present reconstruction. Each assertion states its hypotheses; it is not an editorial replacement of a manuscript passage. The original `his_statement` remains identified as the formulation being corrected.

The mappings resolve eleven cote11b pseudo-targets, the weight-zero self-target, and several structurally valid but mathematically different targets. Eight mappings use an existing precise correction; seventeen mappings use the sixteen new claims. The shared Hodge-level refinement explicitly covers both SA05-C3018 and SA05-C3026.

The principal distinctions preserved are:

- Pure lisse sheaves over a normal finite-field base are geometrically semisimple; the arithmetic representation need not be semisimple.
- Special weight zero under the recorded finite-dimensional Q_l subquotient definition means finite monodromy, not arbitrary lisse monodromy.
- Finite generation of an integral Hom subgroup needs an actual uniform denominator bound. Rationalization or a Serre quotient alone does not supply it.
- The low-ramification abelian-scheme extension theorem begins with an abelian scheme on the punctured spectrum. It does not infer that object from all-prime unramified generic realization data.
- The checked local elliptic example requires weight 4 at i = n = j = 1. A global cohomology bound is not a correction of the local claim.
- The Hodge-level correction is numerical and assumes the stated mixed-Hodge-compatible summand realization; it does not prove a geometric motivic level theorem.
- The abutment uses E-infinity subquotients. Identifying a whole E2 term requires degeneration and the relevant filtration compatibility.
- The exact type r of Q_l(-r) uses the late untwisted finite-field convention, not the earlier Tate-stable filtration.
- The ordinary-quadratic monodromy theorem retains regularity of the total space. The all-degree specialization claim retains H0, and the integral punctured-cone groups retain their coefficient restrictions and corrected degrees.

The search ledger distinguishes inherited family URLs from URLs actually reopened in this audit. It does not imply that every URL in a broad inherited search row supports every refinement. The new claims' exact reference keys and checked extents control that attribution. No earlier query was rerun merely to create a new event; no new computation or formal certificate execution is claimed.

## Remaining central corrections

### 1. SA05-C3008 source locator

The quotation about the two pieces and the bound 2n-i-1 is at physical line **168**, scan 105, of `sources/texts/pro/MPL_12_099-149_transcription.tex`. The claim currently cites only lines 178–180, which contain a different boundary calculation. Add line 168 (or use 168–180) to this claim's locator. Item SA05-3009 already contains the enclosing 134–180 range and does not need that repair. Preserve the existing reading alarm: the Pro/Codex quantifier discrepancy remains unresolved without the scan.

### 2. Mixed checked/unverified endpoint in Stage 5

At the later snapshot, physical TSV line 140 of `SA05_links.tsv` has `to = Demazure1971Motifs:§3Proposition1;SGA4:IV7.5 backward locator`. Its evidence correctly states that the Demazure endpoint was read and direct SGA4 retrieval failed. Keep the checked Demazure endpoint in the link, and put the SGA4 backward locator into an explicitly unverified lead field/row. A combined target cell must not imply that both published endpoints were checked.

### 3. Minor attribution consistency in a merged occurrence

The survivor SA05-C1081 correctly calls the standard-conjecture-letter comparison an earlier-run lead, not a directly witnessed manuscript assertion. Its `source_occurrences` entry for former SA05-C2080 still says `author: Alexander Grothendieck` without that qualification, although the relevant absent source was not read. Match the survivor's qualified provenance in that occurrence. This does not change an actual authored mathematical passage or justify any attribution to unseen cote 16 material.

## Stage 5 coverage and limits

The parent's removal of the 27 cote11a and five cote12c absent-archive links is visible in the later snapshot: the separate unavailable-archive table has 34 rows, including the earlier two cote11b leads. These are leads, not checked two-ended links.

The remaining 151 main rows consist of 45 folder links, 56 published-work links and 50 explicitly labeled `our projects` leads. Therefore the main-table row count is **not** the number of links with both endpoints read. Excluding the 50 project leads gives 101 folder/published relationship rows; the mixed Demazure/SGA4 endpoint above still needs its stated qualification. Published work may be an external checked endpoint, but it must retain the exact author and theorem scope. A later source discussing an old topic does not verify an absent archival endpoint.

Within the reviewed fields, Mumford's reused GIT pages, Antoine Delzant's attached offprint, the unidentified reflection typescript, and Grothendieck's manuscript material remain distinguished. The strict external-link verification status of the Delzant bibliography is being handled separately by cote11a; this audit does not convert the fully read attached transcription into an independently opened original publication.

## Reproducibility

`programs/audit_consolidated_structure.py` performs read-only integrity checks and accepts an optional output filename. `programs/build_refinement_supplement.py` materializes the manually authored statements and validates their current item and target IDs. It records the input claims hash and does not infer judgments from headings. It is intended to run before central incorporation; after the new IDs exist centrally, its duplicate-ID assertion intentionally prevents blind rematerialization against an already integrated table.
