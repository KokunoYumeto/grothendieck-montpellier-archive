# Independent final assembly audit

Checked on 19 November 2026 by `/root/cotes_156_8_9`. The live assembly was still being updated during the audit. The saved snapshot hashes identify the versions actually inspected. This report concerns concrete integration and provenance risks. It is not an independent proof certificate for all 446 claims.

Only this audit directory and the assigned VIII/IX01–08 contribution were written. The assembler, master tables and other readers’ files were not modified by this auditor. Root received each actionable finding while working on the final assembly.

## 1. Findings and their dispositions

| Finding | Evidence and consequence | Disposition |
|---|---|---|
| An unresolved manuscript target was initially counted as a verified endpoint. | The VI/VII manuscript-page-52 link from `J156-7-04_transcription.tex`, scan39, lines166–196, to `J156-6-07_transcription.tex`, scan53, lines98–124, says that the chapter reading remains unresolved and is “not as a proved identification.” The classifier initially recognized only the wording without “as.” Reading the two candidates did not settle which was cited. | Root added the missing phrase. The exact row was then found in `SA21_unresolved_links.tsv`, outside the verified table. |
| Bibliography events were arriving after the bibliography records. | The first snapshot lacked direct-key events for Shmuely1974, CoeckeMoore2000, DomenachLeclerc2001 and Ischi2010. Their source checks already existed in the IX reader’s report. | The now-stable IX events explicitly name the four keys and their theorem/proof locators. The final snapshot has no bibliography key without a recorded event. This audit checked the event/source-report agreement; it does not relabel those as fresh independent readings by this auditor. |
| Three original works remain unverified. | Raney1952, DeJonghTroelstra1966 and Dacey1968 are absent from every claim/problem `refs` list. Their bibliography records explicitly describe failed access or the use of a later statement. | Root’s added events accurately record bibliographic/access inspection only. They expressly deny an original theorem check and preserve `unverified`. No mathematical result has been credited to an unread original. |
| A mixed problem/claim pointer string initially remained in `note_ids`. | The VIII88–89 to IX124 link begins its pointer string with `MP-SA21-…`, followed by claim IDs. The initial cleanup tested only strings beginning with `C-SA21-…`. | Root changed the classifier to accept both prefixes and move them to `evidence`. That code correction was directly inspected. The saved pre-rebuild master snapshot still contains the old row; the next final assembly must regenerate it. This is a known stale output, not an unfixed classifier. |
| Two retrieval envelopes escaped text redaction. | `audit/library_crossproject_search2.json` uses `results` rather than singular `result`; a newly arrived `parts/cotes_9_14_18/open_O9E_06.json` uses `response`. The initial tests would retain long contextual or primary-source response text. | Root added both envelopes and generalized the filename pattern. The revised packager also reduces complete source-reading echoes, including the tail’s `source_checks.txt`, to byte/line/hash metadata. The targeted rerun now reports neither retrieval payload as retained. |
| Birkhoff’s chapter was misidentified in this contribution. | The cached primary book starts Chapter IV at OCR3855–3857 and Chapter V at4886–4887. The polarity and Galois sections occur in IV. | Corrected all current mathematical assessments and generated files in the assigned contribution. IV §5 Theorem9 and Corollary pp54–56, and IV §6 Theorem10 p56, are the retained locators. Literal earlier search-query wording is historical evidence and remains unchanged. |
| The early support-functor question needed its late correction stated explicitly. | IX95 inserts compatibility on singleton closures; IX97 acknowledges the addition. This is stronger than preservation of joins alone. | Directly reread the full corrected proposition/proof at `J156-9-12:242–355`, updated MP-SA21-9-08, and linked it to C-SA21-9-054 / MP-SA21-9-10. Root merges the repeated question while preserving versions. Section6 gives the targeted check. |

## 2. Structural consistency

The completed input snapshot contains **446 claim records and 446 assembled claim records**, with no omitted, extra or duplicated claim ID. No claim points to a nonexistent Stage1 item. No top-level claim or problem cites a missing master bibliography key. All item, claim and problem pointers in the inspected generated directions resolve; the exact direction count is saved in the snapshot as the final direction list is being expanded. The raw parts contain69 distinct bibliography spellings before the assembler’s declared aliases are applied.

These are explicit structural checks, performed by `audit_snapshot.py`; they do not infer a mathematical verdict from strings. The script reads the current classifier’s actual exclusion phrases and the same event filenames the assembler consumes. Its output includes input and master hashes. The first intermediate snapshot briefly showed48 tail claims not yet in the master; the next assembly included all48, so that temporary difference was not a loss of claims.

The bibliographic aliases and old-to-global problem-ID mapping are explicit. Original problem IDs and source versions are retained as provenance. The assembler intentionally leaves the raw `versions` subrecords unchanged; those are not alternate canonical IDs. No overlapping claim ownership was detected.

## 3. Repeated problems and mathematical boundaries

The three initial cross-cote merges were read as full problem records, not inferred from titles:

- IV’s subdivision extension question and VI’s stricter unchanged-exterior/canonical extension question concern a continuing programme. Their different requested conclusions must remain visible as versions; the record must not say that a relative triangulation theorem establishes uniqueness or unchanged incidence.
- IV’s Boolean virtual-support expectation and VII’s later distributivity question share the same failed unconditional expectation. The later ortholattice countermodels and the additional orthomodularity/distributivity requirements remain explicit.
- VII’s realization axioms and VIII’s set-support representation question belong to one continuing problem, but ortholattice representation does not establish a realization by ordinary subsets reflecting every face/refinement relation.

The later merge of MP-SA21-9-10 into MP-SA21-9-08 is more direct: the corrected Proposition4 answers the earlier functoriality/pretranspose question. The correction is included in both the early problem’s current assessment and the later version. The nonsurjective injection still refutes only the complement formula; the independent closure counterexample is a distinct record.

The normalized faithful external-support example is correctly linked across VIII and IX. Mere faithfulness, full faithfulness and Boolean commensurability are separate assertions. The linked P4 certificate answers the separating-example question; it does not invalidate the theorem that retains full faithfulness. No new finite enumeration was run in this final audit.

The earlier targeted review of root’s support, restriction, finite-PL and rive/sheaf arguments remains in `parts/cotes_8_9/root_proof_review.md`. It found no concrete overstatement at the stated scope. This final integration audit does not extend that assessment to unrestricted spaces or to the entire manuscript programme.

## 4. Cross-project endpoint coverage

The project audit records54 named targets:20 located at an exact register entry, selected excerpt, run summary or recovered companion passage; two indirect mentions; thirty missing exact targets; and two original-context/version mismatches. The categories and exact locators are in `parts/project_links/project_targets.json` and `project_links.tsv`. All125 original Context paragraphs were covered.

The two recovered registers are neighboring context versions, not the original SA21 context package. A located historical assertion is evidence of what the earlier run recorded. It is not a fresh proof of that assertion and must not be described as such. The twenty located cases include partial excerpts and summaries with explicitly different evidential strength. The54 target rows are not54 verified mathematical endpoints.

The assembler currently puts this detail in `SA21_project_leads.tsv` rather than adding all54 rows to the main verified link count. This prevents false inflation. The final dossier should give the20/2/30/2 coverage separately so that successful targeted recovery is visible without suppressing the unresolved endpoints.

## 5. Source-copy and packaging inspection

`audit_package_inputs.py` loads the packager’s definitions without importing a module or running its `main`; no ZIP is created. It applies the actual exclusion/redaction rules to the current tree and stores paths, byte counts and hashes. It inspects potentially retained JSON text fields and large text files without copying their contents into the audit.

The updated rules exclude primary PDFs, images, HTML, paired PDF-text extractions, the named primary-book/article OCR files and the full recovered context navigation copies. Web retrieval JSON is replaced by request/URL/reference/hash metadata. The plural `results` and `response` cases are covered. Complete source-reading program echoes are likewise represented by metadata with their original hash, byte and line counts and a reproduction instruction. This meets the practical need to preserve evidence of executed reading commands while keeping the attached source files out of the package. The last targeted dry-run inspected575 files outside this audit directory, excluded60 and sanitized228; those counts describe that snapshot and may increase with final authored files.

The remaining automated candidates are selected manuscript cross-reference snippets, not a discovered unredacted primary publication or a complete recovered context file. The check is limited to the known input forms and suspicious text fields; it is not a semantic claim that every authored sentence is free of quotation. The final packager still needs its normal archive integrity test, which root owns.

## 6. Targeted check of the corrected IX criterion

Let E,F be disjoncteurs, with double-polar closures c_E,c_F. For an arbitrary correspondence α:E→P(F), set ᾱ(A)=⋃_{x∈A}α(x), and f(S)=c_F(ᾱ(S)) for closed S⊆E. All subsets and all joins, including the empty ones, are quantified.

For each y∈F let Γ(y)={x∈E:α(x)⊥y}. A pretranspose β means α(x)⊥y iff x⊥β(y). Thus Γ(y)=β(y)⊥ is closed. Conversely, if every Γ(y) is closed, choosing β(y)=Γ(y)⊥ gives the required equivalence. This establishes the closed-fiber/pretranspose equivalence without a single-valuedness assumption on α.

With a pretranspose, the condition ᾱ(A)⊥y says that every member of A is orthogonal to β(y), and is unchanged on replacing A by c_E(A). Testing all y shows that ᾱ(A) and ᾱ(c_E(A)) have the same perpendicular, hence the same closure. Conversely, closure commutation forces Γ(y) to be closed: ᾱ(Γ(y))⊆{y}⊥, so the same containment holds after replacing Γ(y) by c_E(Γ(y)). More generally it makes {x:α(x)⊆T} closed for each closed T⊆F, as the manuscript states.

Closure commutation gives preservation of all joins by f, and substitution A={x} gives f(c_E{x})=c_F(α(x)). Conversely, if f preserves all joins **and** this generator equality holds, then

\[
f(c_E A)=f\!\left(\bigvee_{x\in A}c_E\{x\}\right)
=\bigvee_{x\in A}c_F(\alpha(x))=c_F(\bar\alpha(A)).
\]

The empty A case uses preservation of the empty join and is included. This verifies the repaired implication. Preservation of joins alone cannot replace the generator equality; nor does the criterion imply preservation of orthocomplements. The insertion at J156-9-12:253–257 and its acknowledgment at351–355 match exactly the hypothesis required in this calculation.

The supplemental ledger records one targeted check of C-SA21-9-054 and one Birkhoff locator/source-scope check. It does not add theorem checks for the three inaccessible originals or for the packaging and pointer audits.
