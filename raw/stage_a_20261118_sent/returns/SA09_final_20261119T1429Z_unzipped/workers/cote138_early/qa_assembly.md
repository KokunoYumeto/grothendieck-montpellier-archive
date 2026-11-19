# Final assembly consistency review

**Reviewer:** cote138_early worker, 19 November 2026. **Objects reviewed:** `SA09_work/SA09_dossier.md`, `SA09_work/programs/consolidate.py`, the explicit project-link decisions, root link additions and relevant worker records. This is a record of the files as reviewed before the root applied the proposed corrections. No root file was edited during this review, and no new literature search was conducted. The intentional main-count placeholder was not treated as an error.

## 1. Omitted checked cote-145 correspondence

The consolidator's worker-link loop read only `links.tsv` and `verified_project_links.tsv`. It omitted `workers/cote138_early/additional_folder_links.tsv`, whose independently checked comparison joins cote138 scans37/39 to cote145 scans11/24. The row was not duplicated in `root_verified_links.tsv`.

**Proposed correction:** include `additional_folder_links.tsv` in the loop. The dossier correctly reports that cote145 was retrieved and checked; its main links table should preserve the actual correspondence. This verification concerns the two transcriptions, not the separately unavailable INTAKE document or a proof of a full arithmetic-image assertion.

## 2. Historical project leads and current availability

The middle-worker mixed rows moved to the lead table still said that only the source end was available, that named returns were absent, or that cotes145/147 and working returns were unattached. Selected LM4, LM4_SUCCESSOR B.38/B.39, LM7_PUSH and LM6 endpoints had subsequently been read. The cote145 transcription had also been read, while the independently named INTAKE, WG, EXIT_TOWER and cote147 targets remained unavailable at this review.

**Proposed correction:** qualify initial absence historically and identify separately which targets were subsequently checked. Do not upgrade a missing target merely because a related research return or archive transcription became accessible. All project proof verdicts remain attributed; the new verification is textual correspondence.

The dossier also described `SA09_project_leads.tsv` as containing reports whose intended endpoint had not been established. The early-worker inventory deliberately retained 23 original leads now marked “selected target endpoint subsequently read.” Either retain that historical inventory and describe its updated verification statuses, or filter those resolved rows from a strictly unresolved-lead table. The original mixed rows can remain provenance records if this distinction is explicit.

## 3. The scan78 marked set

`MPL_138_046-089_transcription.tex:1375–1379` explicitly labels seven finite points: −1, 0, 1/2, 1, 2, −j and −jbar. Infinity is implicit in the ambient projective line rather than explicitly labelled in this diagram. Scan19 explicitly provides the eight-point special-fibre set and the rational function.

**Proposed correction:** say that the seven finite points marked on scan78 match the finite part of the eight-point set on scan19. The substantive SA09-234→SA09-129 merge is sound. Assignment of the earlier equation to the later unlabelled arrow remains a reconstruction, as the root already states; the comparison does not decide authorial intention from a marked set alone.

## 4. Exact Kummer index and its ambient group

The dossier correctly separates the rational saturated index 2^r from general number-field finite index. For precision, the former is the index in the intrinsic group A=Aut_{Γ0}(Γ∞), where Γ is a finitely generated subgroup of Q*, Γ∞ is its full radical group and Γ0=Γ∞∩Q*. It is not automatically the same index in coordinates supplied by arbitrary unsaturated generators.

The general number-field conclusion uses the uniform bound of Perucca–Sgobba Theorem1.1 and the independently written bounded-finite-quotient-index deduction. The bibliography correctly records that the theorem statement was read from the publisher-provided preview and that its full proof was not opened or independently checked. No mathematical correction to these conclusions was needed.

## 5. Minor expression

Replace “the eighteenth-transport programme” by “the eighteen-transport programme.” The source concerns eighteen proposed transports, not the eighteenth member of a list.

## 6. Chronology check from existing records

No date error was found in the early-packet summaries checked here: Schinzel1977; Belyi received1978, Russian1979 and English1980; Lenstra–Moree–Stevenhagen first preprint2011 and publication2014; Moree–Stevenhagen first preprint2012 and publication2014; Perucca–Sgobba2019. The geometric finite-kernel example preserves the Qbar-versus-Q hypothesis distinction, and the project summaries retain the gentle-GT0/full-GT and referee-scope qualifications.

For Bühler, the already verified worker bibliography `workers/cote137/references.bib`, entry `Buhler2009`, records:

- First arXiv circulation: **10 November 2008**.
- Version actually opened: **v2, 22 April 2009**, arXiv:0811.1480, <https://arxiv.org/abs/0811.1480>.
- Acceptance in *Expositiones Mathematicae* is recorded; verified journal year, volume, pages and DOI are not supplied in this existing entry.

Accordingly, “Bühler, T. (2009). *Exact categories* (arXiv version 2; first posted 2008)” is supported by the existing evidence. Do not present 2009 as a verified journal-volume year or describe journal publication metadata as checked on the strength of this record. This chronology check reads the existing opened-source report; it is not a new independent opening of the publisher page.

## Outcome

The root was notified of the missing link ingestion, stale availability descriptions, marked-point wording and minor expression. The exact Kummer theorem scopes, source-date distinctions and explicit cross-packet merges reviewed here otherwise remain sound. Matching check events are in `qa_assembly_events.tsv`; they record consistency verification, not additional independent proofs.
