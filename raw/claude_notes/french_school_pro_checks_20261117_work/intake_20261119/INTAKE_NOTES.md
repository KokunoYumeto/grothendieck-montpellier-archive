# Intake of FGA_CHECK cp12 and ILLUSIE_I_CHECK cp15, 19 November 2026

French-school field agent, Claude Opus 5.5 at effort high, at the main session's request (Claude Opus 5.5 at effort max).
Both runs of the FINISH prompts (GPT-6 Astra, ChatGPT Pro mode, sent 19 Nov) were silent for more than five hours and are
taken as ended at their last checkpoints. Check events: `CHECK_EVENTS.tsv` beside this file.

## FGA_CHECK, checkpoint 12 (06:12 UTC)

- Since the FINISH prompt (state at cp05: French through 212 p. 116), the run finished the French: 212 pp. 117-118, 221,
  232, 236, the Commentaires and all errata. All 211 French pages now read in both French layers.
- CORRECTIONS.tsv: 23,033 rows (French corrected 10,434: reading 9,713, misprint 267, structure 340, typesetting 114;
  French as printed 10,307; English 2,292, of which terminology 2,106). 38 rows correct the earlier run. All rows wait
  for the second reading. CHECK_EVENTS 886. NOTES.md empty.
- English read against the corrected French: 149 complete, 182 through p. 212 (20 of 28 pages). Spanish, pt-BR,
  Vietnamese, Korean, Chinese not begun; Korean and Chinese builds stop on engine errors.
- The run repaired the 27 build errors; the corrected French builds (LuaLaTeX, 3 passes, 0 errors) with the same five
  overfull lines as cp05 (5.4-36.7pt). Fixed in our publication copy by two layout settings (fga_publish2/fix_fr2.py).
- Scan sample: 221 p. 272, 232 p. 143, 236 p. 223 confirmed as the rows say (plus the four of cp05).
- Published: fga-fr f8d8ad8, release fga-fr-2026-11-19b (reader 148 pages, sources, checkpoint 12 zip).
- Next prompt: pro_prompt_builds/FGA_CHECK_FINISH_2 (send folder TO_SEND/11_Finish_prompts/FGA_CHECK_FINISH_2, packed).

## ILLUSIE_I_CHECK, checkpoint 15 (05:30 UTC)

- Since the FINISH prompt (state at cp09: Volume I through printed p. 107), the run read pp. 108-188 in three layers
  (p. 189 in progress, no edits). Volume II not reached (still cp09, not begun).
- CORRECTIONS.tsv: 7,230 rows (as-printed 2,224, corrected 2,526, English 2,470, build 10; misprint of the original
  130); 595 verdicts on existing corrections; 19 open reading questions; CHECK_EVENTS 448; NOTES empty. No build claimed.
- Build: 12/11/12 LuaLaTeX errors per layer; repaired by script in 23 places (illusie_publish/fix_ill.py, REPAIR_LOG.tsv):
  merged control words and an out-of-scope display macro. Then 0 errors; one 2.97pt overfull vbox in the English
  (PDF p. 252, unchecked chapter V), viewed, nothing cut off.
- Scan sample: p. 149 and p. 169 as the rows say.
- Published: illusie-cotangent-complex-editions bf162da (+ c9ec1bd README), release check-2026-11-19 (Volume I three
  PDFs incl. a first diplomatic PDF, tex, sources, checkpoint 15 zip); revised rights notice printed on a last page.
- Next prompt: pro_prompt_builds/ILLUSIE_CHECK_FINISH_2 (send folder TO_SEND/11_Finish_prompts/ILLUSIE_CHECK_FINISH_2).

## Slip of 19 Nov: cause and fix

- Cause: fix_fr2.py imported FR_FGA from apply_notice.py, whose edits ran at module level, so the import re-applied
  them to the Tôhoku and GAGA clones (a second notice in six main files).
- Fix: the six files restored with git checkout before any commit (nothing pushed); apply_notice.py's edits moved
  under `if __name__ == "__main__":`.

## Follow-ups of 19 Nov

- Illusie I English, PDF p. 252: overfull vbox 2.97pt in the output routine; cleared in the build by giving the
  paragraph skip of \ReflowSettings 1bp of shrink (was .2bp); English rebuilt (0 errors, 0 overfull, 306 pages,
  pp. 251-253 viewed); assets 04-06 replaced on check-2026-11-19 (repo 371c750); added to
  ILLUSIE_I_BUILD_REPAIRS_20261119.tsv and the prompt text; 16_ILLUSIE_CHECK_FINISH_2_night repacked, lint passes.
- Illusie Volume II: revised rights notice printed on a last page of the three editions as a TikZ node placed like the
  erratum leaf (a plain minipage ran off the page, since Volume II places its leaves absolutely); LuaLaTeX three passes,
  0 errors, one 1.43pt overfull (diplomatic), notice pages viewed; repo 0e82d65 (READMEs link Volume II to the new
  release; the French README had still pointed at editions-2026-11-06), release volume-II-2026-11-19.
