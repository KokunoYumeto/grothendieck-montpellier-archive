# Sub-agent "places": every row that names his page, linked to that page (brief, 18 Nov 2026)

You are Claude Opus 5.5 at effort max, sweep 2, sub-agent places. Read
`<local>/Documents\results_register\sweep2_global\COMMON_BRIEF_FOR_SUBAGENTS.md` first. Your folder:
`<local>/Documents\results_register\sweep2_global\sub_places\`.

## Why you

The companion reads his notes unit by unit and must point from each of his pages to our items. The rows name his
places in their manuscript column (REGISTER.tsv column `his_places`) and in their statements and notes, in three
systems, written in many forms:
- **The Montpellier archive:** cote, scan(s), manuscript page, section. Forms: `cote 149, section 1, manuscript p.17;
  scans 35-36`, `MPL149, manuscript pp.36-39; scans74-79`, `149; 32-36`, `149; 6–8, 52`, and JSON
  `{"cote": "142", "scan": "094--096", "page": "95 (scan 096)"}`.
- **La Longue Marche** (cote 140-2, pages 1-292, and its continuations 140-3 and 140-4, called C3 and C4 in the
  runs): section (§), folio(s), scan(s). Forms: `§42; fol.349 verso; scan120`, `Section 23, folios 140-141, scans
  279-281`, `C4 scans 228–233, §53.2–3`, `LM scan 483`, `(cote140-2)`.
- **Les Dérivateurs:** chapter (roman numeral) and manuscript page. Forms: `XII ms.94–97`, `II ms. 36ter`, `VII.65-67`,
  and the companion's block ids `XIIb-a-B035`, `VIIc-C004`, `II-C-003`.
Each run's results table states its column's format in the header (for example ANABELIAN_149_PUSH: "cote; page;
scan"; CYCLOTOMIC_KERNEL: "section; page; scan"; the LM runs: "section; folio; scan"; ANABELIAN_A1 and
SECTIONS_OVER_Q: "cote; scan"); where the cote is not written, it is the run's cote, given in its prompt. Many entries
in the column are not places at all ("Part E individual-type comparison", "Lead 1", "REVLOC D2.4"): those are not his
places and are left out (cross-run ids there are already in GRAPH_EDGES.tsv).

My first parse, by script and imperfect, is `sweep2_global/tools/places_parsed.tsv` (tag, run, status, field, work,
cote, scans, pages, section, raw): 3,470 lines for 2,769 tags, about 1,100 distinct places. It misreads some formats
(for example bare numbers after a cote read as further cotes, and the "section; page; scan" columns). Use it as a
start, not as the answer.

## Where his pages are transcribed

- The archive by cote: `<local>/Documents\grothendieck_archive_transcription_20261110\returns\MPL_<cote>_<scans>_unzipped\`
  (for example `MPL_149_001-090_unzipped`, `MPL_147_048-137_unzipped`, `MPL_142_001-093_unzipped`), and the Codex web
  returns `...\grothendieck_archive_transcription_20261110\codex_web_20261113\returns\<folder>\out\` with
  `*_mathnotes.md`. The companion's draft units (cote, folder, unit, scans, title):
  `...\grothendieck_archive_transcription_20261110\UNITS_DRAFT_20261118.tsv`.
- La Longue Marche: `<local>/Documents\longue_marche_pro_pilot_20261104\` (PACKAGES.md maps the packages
  LM_P01 ... to cote 140-2 and scans; the folders LM_C3-* and LM_C4-* hold 140-3 and 140-4 by scan range; `reader\`
  holds the reader).
- Les Dérivateurs: `<local>/Documents\derivateurs_companion_20261109\reader\LesDerivateurs_companion.tex` and
  `...\derivateurs_companion_20261109\packages\DER_*`.
List a folder before you open files in it; never search these trees recursively.

## What to do

1. Normalize every place each row names: `HIS_PLACES.tsv` with columns: tag, status, work (Montpellier archive / La
   Longue Marche / Les Dérivateurs), cote, scans, page or folio, section or chapter, unit (the UNITS_DRAFT unit id when
   the place falls in one), what he says there (one sentence in English, in our words, from his page as transcribed;
   at most a few words of his in quotation marks), source of that sentence (file and line, or "row text" when you took
   it from the row because the transcription is not at hand), how linked (column / statement / notes; script / read).
2. `PLACES_INDEX.tsv`: one line per distinct place (work, cote, scans, page, section, unit), with what he says there
   and every tag that points to it, so that the companion can go from his page to our items.
3. Work by script wherever the format allows; read his transcribed page to write "what he says there" for the places
   named by the most rows first (cote 149 and La Longue Marche carry most of them), then as many more as your budget
   allows, and say in REPORT.md how many places have a sentence from his page and how many from the row text.
4. Record in FINDINGS.tsv the places that are wrong or doubtful (a scan that does not hold what the row says; a cote
   misnamed; two rows citing different scans for the same claim of his), with what you read.

CLUSTERS.tsv is not needed; CHECK_EVENTS.tsv only if you compare a row's claim about his page with the page. Write
REPORT.md as the common brief says.
