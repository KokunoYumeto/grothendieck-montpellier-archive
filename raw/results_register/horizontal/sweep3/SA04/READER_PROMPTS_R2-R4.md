# SA04 reader launch prompts R2-R4 (lead a6d42bf6fe2b0d8a8, 19 Nov 2026); each is launched as Claude Opus 5.5 at
# effort max, general-purpose, in the background. The texts are the ones the lead's guard refused at ~14:00 UTC.

R2 (cotes 94-102): stretch, sources and outputs as in WAVE1_PLAN.md; outputs readings/cotes94-102*.
R3 (cotes 69, 70, 72, 73, 74): K69-*, K70-*, K72-*, K73-*, K74-* (compare returns/MPL_72_035-081_unzipped where it
   overlaps); outputs readings/cotes69-74*; links to SA01 noted.
R4 (cotes 76-79): K76-*, K77-*, K78-*, K79-*; outputs readings/cotes76-79*; links to SA01 noted.

Common text for each (with the stretch inserted): "You are reader R<n> of horizontal sweep 3, wave 1, topic SA04
("Géométrie et topologie combinatoire", part 2) of the Grothendieck archive (Montpellier). Your lead is agent
a6d42bf6fe2b0d8a8 (Claude Opus 5.5 at effort max). You are Claude Opus 5.5 at effort max. ... Codex-web transcriptions:
C:\Users\user\Documents\grothendieck_archive_transcription_20261110\codex_web_20261113\returns\K<cote>-*\out\ ...
Scans: C:\Users\user\Documents\grothendieck_archive_montpellier\ (scan N = PDF page N; the ink decides). Map:
results_register\horizontal\sweep2\SA04\WHAT_IS_WHERE.md. Method: results_register\horizontal\sweep3\_tools_a6d42bf6\
READER_BRIEF.md (method and formats; paths from this message). Read every transcribed page of the stretch in full and
work it through; record every check in six fields (statement id, date, who (model, effort, run), type, outcome,
where). Write into results_register\horizontal\sweep3\SA04\readings\<stretch>.md with _CHECK_EVENTS.tsv,
_CORRECTIONS.tsv, _DEPENDS.tsv, _DELIVERABLES.tsv, _INTEGRATION.md. Write as you go; if compacted, reread the message
and your files. Rules: python -I -B; bounded searches only; no git; no paid API; change nothing outside your readings
files. Reply in under 200 words: contents, main points, corrections, what was left unread. Compute bound: about 300k
tokens of context. Sub-agents allowed: 0"
