# Rebuilding the core registers

The programs serialize manually composed decisions; they do not infer verdicts from headings. A full rebuild uses this order:

1. `build_stage1.py`
2. `build_claims.py`
3. `build_problems.py`
4. `finalize_core.py`
5. `late_primary_updates.py`
6. `close_fates.py`
7. `build_bibliography.py`
8. `build_registers.py`
9. `computations.py` with stdout saved to `computation_outputs.json` (wait until it finishes before validation)
10. `build_evidence_logs.py`
11. `../analysis_curves/assign_status_categories.py` (manually assigned per-claim categories)
12. `serialize_directions.py` (20 genuine additional Codex subjects and 12 numeric direction records)
13. `final_reference_origin_audit.py` (precise supporting citations, source-origin labels and final correction)
14. `add_lefschetz_request.py` (the separately recovered Deligne17October1966 proof request, exact primary comparisons and evidence)
15. `apply_publication_authorship_audit.py` (five manual A-to-B corrections for Raynaud/Berthelot published counterparts; preserve source authors and mathematical assessments)
16. `apply_problem_origin_audit.py` (approved81-record provenance audit; both owned parts, MP/ED split and Stage6/editorial direction partition)
17. `validate_core.py` and `../analysis_curves/validate.py`
18. `../../integration/validate_ega_origin_application.py` (cross-register provenance, narrative ID and overlay idempotence checks)

The dossier section, research directions and independent proof notes are authored Markdown and are not generated from headings. `external_source_checks.py` reproduces the rendered primary-page inspection cache if the shared PDFs are available. Those PDFs/images/full texts are excluded from the finalZIP. Do not run an intermediate builder alone and treat its pre-final state as the complete claim map.

Step12 also writes the20 additional-item text-concordance events in check_events.tsv if absent. The additional subjects do not add entry verdict rows. Indexed duplicate review is proposed separately in cross_owner_review/ and does not mutate source-owner registers.

Step12 reads its original twelve authored directions from `provenance/pre_origin_audit/directions.md`; the approved final overlay writes seven Stage6 directions and five separately preserved editorial directions. It must not parse its post-audit output as its original input. Step14 adds the21st additional Codex subject, SA23-1321. Step16 preserves23 whole MP-to-ED redirects and11 partial editorial contexts in the core, plus8 whole redirects and7 partial contexts in analysis/curves. Original81 records and directions remain in `provenance/pre_origin_audit`. Do not regenerate the approved audit from the reduced problem register: its serializer reads those preserved inputs when available. The final authorial problem counts are37 core and14 analysis/curves. The root finalizer aggregates `editorial_directions.json` outside Stage6.
