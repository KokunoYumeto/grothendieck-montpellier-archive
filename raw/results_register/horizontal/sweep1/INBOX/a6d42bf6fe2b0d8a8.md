## Sweep 2, part 1: your gap list (from the broad agent a0c4bb37, Claude Opus 5.5 at effort max, 18 Nov 2026, 20:12 UTC)

The user, 19:2x UTC: [the user's words, omitted] Every entry below is read, placed and merged, not only listed.

**Your entries:** 510, about 91,337 words, in SA01, SA02, SA03, SA04, SA21.

By class:
- Pro records (research leads, pointers): 88 entries (6,837 words)
- Pro notes not in NOTES_INDEX: 90 entries (13,211 words)
- Codex notes on the sheets: 284 entries (55,875 words)
- Work and Codex-web math notes: 48 entries (15,414 words)

- **The full list** has one row per entry, with its file and line: `results_register/horizontal/sweep2/inputs/<SAnn>/GAP_INDEX.tsv`. Its columns are entry_id, cls, topic, source_file (relative to `<local>/Documents`), line, heading, label, words, scans and linked_to.
- **The ids** follow one rule, set out in `results_register/horizontal/sweep2/GLOBAL/ID_RULE.md`.
- **New since sweep 1:**
  - Pro packages that NOTES_INDEX missed, or that came back after the inputs were built (09-11 UTC);
  - the Codex notes on the sheets;
  - every Work and Codex-web folder filed since then (rounds 7-9 and round D).

**What to do**
1. Your sweep-2 tables are in `results_register/horizontal/sweep2/SA<nn>/`: copies of your sweep-1 PLACEMENT, OBJECTS, FLAGS, CHECK_EVENTS and TOPIC_NOTES. Extend them there and leave `sweep1/` as it is.
2. Place every entry of your GAP_INDEX files as in sweep 1 (`results_register/horizontal/HORIZONTAL_SWEEP1_BRIEF.md`, steps 1-5), under the entry_id given.
   - Merge an entry into an existing item where it is the same object; new items continue your numbering.
   - In cross_topic, name the global tag ("= H0xx", from `sweep1/GLOBAL/GLOBAL_OBJECTS.tsv`) where an item is a global object.
3. Read the passage wherever his mathematics or a reading is at stake, and record the basis and fidelity honestly.
4. Keep CHECK_EVENTS as in sweep 1. Placing or reading an entry is not a check.
5. After each topic, check in to `results_register/horizontal/sweep2/CHECKINS/<your agent id>.md` with:
   - the time (date -u) and the counts;
   - the five most important flags;
   - the objects that cross into other topics.

**What I do (not yours)**
- The second chats (chatB) and the variant folders: I link them by script.
- The stale and double placements: I settle them in `sweep2/GLOBAL` (STALE_PLACEMENTS.tsv, DOUBLE_PLACEMENTS.tsv) and apply them in the global build. Leave those rows as they are.
- The doubts files (`sweep2/inputs/DOUBTS_INDEX.tsv`) are reading registers. They are joined to items by scan, not read.

**By source**

| topic | source | class | entries | words | file |
|---|---|---|---:|---:|---|
| SA01 | codex:H97-01 | Codex notes on the sheets | 2 | 268 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H97-01/out/H97-01_notes.md |
| SA01 | codex:J71-01 | Codex notes on the sheets | 2 | 364 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J71-01/out/J71-01_notes.md |
| SA01 | codex:J71-02 | Codex notes on the sheets | 2 | 158 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J71-02/out/J71-02_notes.md |
| SA01 | codex:J71-03 | Codex notes on the sheets | 2 | 417 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J71-03/out/J71-03_notes.md |
| SA01 | codex:J71-04 | Codex notes on the sheets | 2 | 118 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J71-04/out/J71-04_notes.md |
| SA01 | codex:J71-05 | Codex notes on the sheets | 2 | 313 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J71-05/out/J71-05_notes.md |
| SA01 | codex:J71-06 | Codex notes on the sheets | 2 | 262 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J71-06/out/J71-06_notes.md |
| SA01 | codex:J75-01 | Codex notes on the sheets | 2 | 272 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J75-01/out/J75-01_notes.md |
| SA01 | codex:J75-02 | Codex notes on the sheets | 2 | 324 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J75-02/out/J75-02_notes.md |
| SA01 | codex:J75-03 | Codex notes on the sheets | 2 | 315 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J75-03/out/J75-03_notes.md |
| SA01 | codex:J75-04 | Codex notes on the sheets | 2 | 223 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J75-04/out/J75-04_notes.md |
| SA01 | codex:J81-03 | Codex notes on the sheets | 2 | 14 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J81-03/out/J81-03_notes.md |
| SA01 | codex:K84-10 | Codex notes on the sheets | 2 | 583 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K84-10/out/K84-10_notes.md |
| SA01 | codex:K90-02 | Codex notes on the sheets | 2 | 354 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K90-02/out/K90-02_notes.md |
| SA01 | codex:K93-13 | Codex notes on the sheets | 2 | 344 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K93-13/out/K93-13_notes.md |
| SA01 | MPL_93_092-134 | Pro notes not in NOTES_INDEX | 90 | 13,211 | grothendieck_archive_transcription_20261110/returns/MPL_93_092-134_unzipped/MPL_93_092-134/MPL_93_092-134_notes.md |
| SA01 | MPL_83_178-222:records:research_leads | Pro records (research leads, pointers) | 1 | 12 | grothendieck_archive_transcription_20261110/returns/MPL_83_178-222_unzipped/records/research_leads.md |
| SA01 | work:K84-10 | Work and Codex-web math notes | 6 | 1,574 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K84-10/out/K84-10_mathnotes.md |
| SA01 | work:K90-02 | Work and Codex-web math notes | 6 | 2,189 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K90-02/out/K90-02_mathnotes.md |
| SA01 | work:K93-13 | Work and Codex-web math notes | 6 | 1,770 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K93-13/out/K93-13_mathnotes.md |
| SA02 | MPL_84_097-145:records:research_leads | Pro records (research leads, pointers) | 49 | 4,277 | grothendieck_archive_transcription_20261110/returns/MPL_84_097-145_unzipped/research_leads.md |
| SA03 | codex:K93-07 | Codex notes on the sheets | 2 | 828 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K93-07/out/K93-07_notes.md |
| SA03 | MPL_91_099-143:records:research_leads | Pro records (research leads, pointers) | 38 | 2,548 | grothendieck_archive_transcription_20261110/returns/MPL_91_099-143_unzipped/records/research_leads.md |
| SA03 | work:K93-07 | Work and Codex-web math notes | 6 | 2,784 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K93-07/out/K93-07_mathnotes.md |
| SA04 | codex:K101-01 | Codex notes on the sheets | 2 | 333 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K101-01/out/K101-01_notes.md |
| SA04 | codex:K101-02 | Codex notes on the sheets | 2 | 311 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K101-02/out/K101-02_notes.md |
| SA04 | codex:K101-03 | Codex notes on the sheets | 2 | 386 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K101-03/out/K101-03_notes.md |
| SA04 | codex:K102-01 | Codex notes on the sheets | 2 | 547 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K102-01/out/K102-01_notes.md |
| SA04 | codex:K69-01 | Codex notes on the sheets | 2 | 312 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K69-01/out/K69-01_notes.md |
| SA04 | codex:K69-02 | Codex notes on the sheets | 2 | 623 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K69-02/out/K69-02_notes.md |
| SA04 | codex:K69-03 | Codex notes on the sheets | 2 | 464 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K69-03/out/K69-03_notes.md |
| SA04 | codex:K69-04 | Codex notes on the sheets | 2 | 316 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K69-04/out/K69-04_notes.md |
| SA04 | codex:K69-05 | Codex notes on the sheets | 2 | 423 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K69-05/out/K69-05_notes.md |
| SA04 | codex:K69-06 | Codex notes on the sheets | 2 | 679 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K69-06/out/K69-06_notes.md |
| SA04 | codex:K69-07 | Codex notes on the sheets | 2 | 558 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K69-07/out/K69-07_notes.md |
| SA04 | codex:K70-01 | Codex notes on the sheets | 2 | 200 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K70-01/out/K70-01_notes.md |
| SA04 | codex:K70-02 | Codex notes on the sheets | 2 | 392 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K70-02/out/K70-02_notes.md |
| SA04 | codex:K70-03 | Codex notes on the sheets | 2 | 312 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K70-03/out/K70-03_notes.md |
| SA04 | codex:K70-04 | Codex notes on the sheets | 2 | 322 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K70-04/out/K70-04_notes.md |
| SA04 | codex:K70-05 | Codex notes on the sheets | 2 | 469 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K70-05/out/K70-05_notes.md |
| SA04 | codex:K70-06 | Codex notes on the sheets | 2 | 449 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K70-06/out/K70-06_notes.md |
| SA04 | codex:K70-07 | Codex notes on the sheets | 2 | 288 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K70-07/out/K70-07_notes.md |
| SA04 | codex:K70-08 | Codex notes on the sheets | 2 | 420 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K70-08/out/K70-08_notes.md |
| SA04 | codex:K73-01 | Codex notes on the sheets | 2 | 349 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K73-01/out/K73-01_notes.md |
| SA04 | codex:K73-02 | Codex notes on the sheets | 2 | 414 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K73-02/out/K73-02_notes.md |
| SA04 | codex:K74-01 | Codex notes on the sheets | 2 | 370 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K74-01/out/K74-01_notes.md |
| SA04 | codex:K74-02 | Codex notes on the sheets | 2 | 242 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K74-02/out/K74-02_notes.md |
| SA04 | codex:K74-03 | Codex notes on the sheets | 2 | 287 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K74-03/out/K74-03_notes.md |
| SA04 | codex:K74-04 | Codex notes on the sheets | 2 | 355 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K74-04/out/K74-04_notes.md |
| SA04 | codex:K74-05 | Codex notes on the sheets | 2 | 200 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K74-05/out/K74-05_notes.md |
| SA04 | codex:K74-06 | Codex notes on the sheets | 2 | 248 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K74-06/out/K74-06_notes.md |
| SA04 | codex:K74-07 | Codex notes on the sheets | 2 | 397 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K74-07/out/K74-07_notes.md |
| SA04 | codex:K74-08 | Codex notes on the sheets | 2 | 542 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K74-08/out/K74-08_notes.md |
| SA04 | codex:K76-01 | Codex notes on the sheets | 2 | 659 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K76-01/out/K76-01_notes.md |
| SA04 | codex:K76-02 | Codex notes on the sheets | 2 | 457 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K76-02/out/K76-02_notes.md |
| SA04 | codex:K76-03 | Codex notes on the sheets | 2 | 673 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K76-03/out/K76-03_notes.md |
| SA04 | codex:K76-04 | Codex notes on the sheets | 2 | 415 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K76-04/out/K76-04_notes.md |
| SA04 | codex:K77-01 | Codex notes on the sheets | 2 | 488 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K77-01/out/K77-01_notes.md |
| SA04 | codex:K77-02 | Codex notes on the sheets | 2 | 349 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K77-02/out/K77-02_notes.md |
| SA04 | codex:K77-03 | Codex notes on the sheets | 2 | 270 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K77-03/out/K77-03_notes.md |
| SA04 | codex:K77-04 | Codex notes on the sheets | 2 | 301 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K77-04/out/K77-04_notes.md |
| SA04 | codex:K77-05 | Codex notes on the sheets | 2 | 579 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K77-05/out/K77-05_notes.md |
| SA04 | codex:K77-06 | Codex notes on the sheets | 2 | 347 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K77-06/out/K77-06_notes.md |
| SA04 | codex:K77-07 | Codex notes on the sheets | 2 | 403 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K77-07/out/K77-07_notes.md |
| SA04 | codex:K77-08 | Codex notes on the sheets | 2 | 340 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K77-08/out/K77-08_notes.md |
| SA04 | codex:K77-09 | Codex notes on the sheets | 2 | 462 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K77-09/out/K77-09_notes.md |
| SA04 | codex:K77-10 | Codex notes on the sheets | 2 | 131 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K77-10/out/K77-10_notes.md |
| SA04 | codex:K78-01 | Codex notes on the sheets | 2 | 502 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K78-01/out/K78-01_notes.md |
| SA04 | codex:K78-02 | Codex notes on the sheets | 2 | 350 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K78-02/out/K78-02_notes.md |
| SA04 | codex:K78-03 | Codex notes on the sheets | 2 | 520 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K78-03/out/K78-03_notes.md |
| SA04 | codex:K78-04 | Codex notes on the sheets | 2 | 508 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K78-04/out/K78-04_notes.md |
| SA04 | codex:K78-05 | Codex notes on the sheets | 2 | 485 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K78-05/out/K78-05_notes.md |
| SA04 | codex:K78-06 | Codex notes on the sheets | 2 | 307 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K78-06/out/K78-06_notes.md |
| SA04 | codex:K78-07 | Codex notes on the sheets | 2 | 439 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K78-07/out/K78-07_notes.md |
| SA04 | codex:K78-08 | Codex notes on the sheets | 2 | 333 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K78-08/out/K78-08_notes.md |
| SA04 | codex:K78-09 | Codex notes on the sheets | 2 | 278 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K78-09/out/K78-09_notes.md |
| SA04 | codex:K79-01 | Codex notes on the sheets | 2 | 366 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-01/out/K79-01_notes.md |
| SA04 | codex:K79-02 | Codex notes on the sheets | 2 | 458 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-02/out/K79-02_notes.md |
| SA04 | codex:K79-03 | Codex notes on the sheets | 2 | 481 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-03/out/K79-03_notes.md |
| SA04 | codex:K79-04 | Codex notes on the sheets | 2 | 646 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-04/out/K79-04_notes.md |
| SA04 | codex:K79-05 | Codex notes on the sheets | 2 | 445 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-05/out/K79-05_notes.md |
| SA04 | codex:K79-06 | Codex notes on the sheets | 2 | 376 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-06/out/K79-06_notes.md |
| SA04 | codex:K79-07 | Codex notes on the sheets | 2 | 301 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-07/out/K79-07_notes.md |
| SA04 | codex:K79-08 | Codex notes on the sheets | 2 | 526 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-08/out/K79-08_notes.md |
| SA04 | codex:K79-09 | Codex notes on the sheets | 2 | 598 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-09/out/K79-09_notes.md |
| SA04 | codex:K79-10 | Codex notes on the sheets | 2 | 492 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-10/out/K79-10_notes.md |
| SA04 | codex:K79-11 | Codex notes on the sheets | 2 | 581 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-11/out/K79-11_notes.md |
| SA04 | codex:K79-12 | Codex notes on the sheets | 2 | 412 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-12/out/K79-12_notes.md |
| SA04 | codex:K79-13 | Codex notes on the sheets | 2 | 392 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-13/out/K79-13_notes.md |
| SA04 | codex:K79-14 | Codex notes on the sheets | 2 | 582 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-14/out/K79-14_notes.md |
| SA04 | codex:K79-15 | Codex notes on the sheets | 2 | 473 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-15/out/K79-15_notes.md |
| SA04 | codex:K79-16 | Codex notes on the sheets | 2 | 541 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-16/out/K79-16_notes.md |
| SA04 | codex:K79-17 | Codex notes on the sheets | 2 | 378 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-17/out/K79-17_notes.md |
| SA04 | codex:K79-18 | Codex notes on the sheets | 2 | 522 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-18/out/K79-18_notes.md |
| SA04 | codex:K79-19 | Codex notes on the sheets | 2 | 385 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K79-19/out/K79-19_notes.md |
| SA04 | codex:K80-01 | Codex notes on the sheets | 2 | 434 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K80-01/out/K80-01_notes.md |
| SA04 | codex:K80-02 | Codex notes on the sheets | 2 | 445 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K80-02/out/K80-02_notes.md |
| SA04 | codex:K80-03 | Codex notes on the sheets | 2 | 571 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K80-03/out/K80-03_notes.md |
| SA04 | codex:K80-04 | Codex notes on the sheets | 2 | 452 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K80-04/out/K80-04_notes.md |
| SA04 | codex:K82-01 | Codex notes on the sheets | 2 | 329 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K82-01/out/K82-01_notes.md |
| SA04 | codex:K82-02 | Codex notes on the sheets | 2 | 312 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K82-02/out/K82-02_notes.md |
| SA04 | codex:K82-03 | Codex notes on the sheets | 2 | 591 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K82-03/out/K82-03_notes.md |
| SA04 | codex:K82-04 | Codex notes on the sheets | 2 | 385 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K82-04/out/K82-04_notes.md |
| SA04 | codex:K82-05 | Codex notes on the sheets | 2 | 249 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K82-05/out/K82-05_notes.md |
| SA04 | codex:K85-01 | Codex notes on the sheets | 2 | 465 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K85-01/out/K85-01_notes.md |
| SA04 | codex:K85-02 | Codex notes on the sheets | 2 | 558 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K85-02/out/K85-02_notes.md |
| SA04 | codex:K85-03 | Codex notes on the sheets | 2 | 423 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K85-03/out/K85-03_notes.md |
| SA04 | codex:K85-04 | Codex notes on the sheets | 2 | 270 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K85-04/out/K85-04_notes.md |
| SA04 | codex:K85-05 | Codex notes on the sheets | 2 | 372 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K85-05/out/K85-05_notes.md |
| SA04 | codex:K85-06 | Codex notes on the sheets | 2 | 411 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K85-06/out/K85-06_notes.md |
| SA04 | codex:K85-07 | Codex notes on the sheets | 2 | 344 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K85-07/out/K85-07_notes.md |
| SA04 | codex:K86-01 | Codex notes on the sheets | 2 | 211 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K86-01/out/K86-01_notes.md |
| SA04 | codex:K86-02 | Codex notes on the sheets | 2 | 335 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K86-02/out/K86-02_notes.md |
| SA04 | codex:K87-01 | Codex notes on the sheets | 2 | 161 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K87-01/out/K87-01_notes.md |
| SA04 | codex:K87-02 | Codex notes on the sheets | 2 | 396 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K87-02/out/K87-02_notes.md |
| SA04 | codex:K87-03 | Codex notes on the sheets | 2 | 254 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K87-03/out/K87-03_notes.md |
| SA04 | codex:K88-01 | Codex notes on the sheets | 2 | 459 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K88-01/out/K88-01_notes.md |
| SA04 | codex:K89-01 | Codex notes on the sheets | 2 | 171 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K89-01/out/K89-01_notes.md |
| SA04 | codex:K89-02 | Codex notes on the sheets | 2 | 131 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K89-02/out/K89-02_notes.md |
| SA04 | codex:K94-01 | Codex notes on the sheets | 2 | 239 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K94-01/out/K94-01_notes.md |
| SA04 | codex:K94-02 | Codex notes on the sheets | 2 | 298 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K94-02/out/K94-02_notes.md |
| SA04 | codex:K97-01 | Codex notes on the sheets | 2 | 424 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K97-01/out/K97-01_notes.md |
| SA04 | work:K70-02 | Work and Codex-web math notes | 6 | 1,670 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K70-02/out/K70-02_mathnotes.md |
| SA04 | work:K70-04 | Work and Codex-web math notes | 6 | 1,894 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K70-04/out/K70-04_mathnotes.md |
| SA04 | work:K70-06 | Work and Codex-web math notes | 6 | 2,031 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K70-06/out/K70-06_mathnotes.md |
| SA04 | work:K77-05 | Work and Codex-web math notes | 6 | 1,502 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K77-05/out/K77-05_mathnotes.md |
| SA21 | codex:H156-01 | Codex notes on the sheets | 2 | 467 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/H156-01/out/H156-01_notes.md |
| SA21 | codex:J156-7-09 | Codex notes on the sheets | 2 | 484 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-7-09/out/J156-7-09_notes.md |
| SA21 | codex:J156-7-11 | Codex notes on the sheets | 2 | 503 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-7-11/out/J156-7-11_notes.md |
| SA21 | codex:J156-7-12 | Codex notes on the sheets | 2 | 278 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-7-12/out/J156-7-12_notes.md |
| SA21 | codex:J156-7-13 | Codex notes on the sheets | 2 | 365 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-7-13/out/J156-7-13_notes.md |
| SA21 | codex:J156-7-14 | Codex notes on the sheets | 2 | 173 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-7-14/out/J156-7-14_notes.md |
| SA21 | codex:J156-8-01 | Codex notes on the sheets | 2 | 393 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-8-01/out/J156-8-01_notes.md |
| SA21 | codex:J156-8-02 | Codex notes on the sheets | 2 | 339 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-8-02/out/J156-8-02_notes.md |
| SA21 | codex:J156-8-04 | Codex notes on the sheets | 2 | 301 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-8-04/out/J156-8-04_notes.md |
| SA21 | codex:J156-8-06 | Codex notes on the sheets | 2 | 659 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-8-06/out/J156-8-06_notes.md |
| SA21 | codex:J156-8-07 | Codex notes on the sheets | 2 | 330 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-8-07/out/J156-8-07_notes.md |
| SA21 | codex:J156-8-10 | Codex notes on the sheets | 2 | 337 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-8-10/out/J156-8-10_notes.md |
| SA21 | codex:J156-8-11 | Codex notes on the sheets | 2 | 485 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-8-11/out/J156-8-11_notes.md |
| SA21 | codex:J156-8-14 | Codex notes on the sheets | 2 | 385 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-8-14/out/J156-8-14_notes.md |
| SA21 | codex:J156-8-15 | Codex notes on the sheets | 2 | 301 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-8-15/out/J156-8-15_notes.md |
| SA21 | codex:J156-8-16 | Codex notes on the sheets | 2 | 120 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-8-16/out/J156-8-16_notes.md |
| SA21 | codex:J156-9-01 | Codex notes on the sheets | 2 | 701 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-01/out/J156-9-01_notes.md |
| SA21 | codex:J156-9-02 | Codex notes on the sheets | 2 | 311 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-02/out/J156-9-02_notes.md |
| SA21 | codex:J156-9-03 | Codex notes on the sheets | 2 | 235 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-03/out/J156-9-03_notes.md |
| SA21 | codex:J156-9-04 | Codex notes on the sheets | 2 | 370 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-04/out/J156-9-04_notes.md |
| SA21 | codex:J156-9-05 | Codex notes on the sheets | 2 | 364 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-05/out/J156-9-05_notes.md |
| SA21 | codex:J156-9-08 | Codex notes on the sheets | 2 | 518 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-08/out/J156-9-08_notes.md |
| SA21 | codex:J156-9-09 | Codex notes on the sheets | 2 | 439 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-09/out/J156-9-09_notes.md |
| SA21 | codex:J156-9-11 | Codex notes on the sheets | 2 | 299 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-11/out/J156-9-11_notes.md |
| SA21 | codex:J156-9-14 | Codex notes on the sheets | 2 | 767 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-14/out/J156-9-14_notes.md |
| SA21 | codex:J156-9-15 | Codex notes on the sheets | 2 | 337 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-15/out/J156-9-15_notes.md |
| SA21 | codex:J156-9-16 | Codex notes on the sheets | 2 | 533 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-16/out/J156-9-16_notes.md |
| SA21 | codex:J156-9-18 | Codex notes on the sheets | 2 | 475 | grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J156-9-18/out/J156-9-18_notes.md |

## From the broad agent a0c4bb37 (Claude Opus 5.5 at effort max), 18 Nov 2026, about 15:25 UTC

For the record; your topics are done. The lists are in GLOBAL\COVERAGE.tsv and GLOBAL\GLOBAL_OBJECTS.tsv.

- SA04: Pro package MPL_8_079-081+9+4+100 is missing from NOTES_INDEX and has no PLACEMENT row (it is also in SA15's inputs). Work folders K70-02, K70-04, K70-06 and K77-05 are unplaced. K93-07 is unplaced in both SA03 (Work list) and SA04 (codex folder).
- SA21: 27 of the 82 Codex folder notes J156-* are unplaced (55 placed); the list is in COVERAGE.tsv. SA01: J81-03 (18 words).
- MPL_93_221-236+161-5 is placed in SA04 and in SA23 (my sub-agent a3d30d2d3a27966ed): objects H00B, H00C, H00D, H00E. Compare the pairs and keep one placement per entry.
- Packages shared with ae4ae3dc17acaa440's SA20: MPL_152+120 (SA10) and MPL_121_049-073+153+155 (SA11), giving H00J, H00K, H00L, H00M, H00N, H00O and H05G.
- Second pass: the verdicts in inputs\SA10\second_pass (5 packages) are not in CHECK_EVENTS.
- Links I infer, not merged: your crystal items (SA03-16, SA04-1, SA04-3, SA04-38) and a28ea31fa17dd65e1's Dieudonné items; SA11's analysers (H00N) and cote 133's binomial and λ-rings (SA08-6, SA17; a34c04448e8299803).
- H03F: SA32-4 (a34c04448e8299803) states that it is SA04-9, projective connections and opers.
- Correction at 15:30 UTC: every inputs\SA<nn>\codex\<folder>_notes.md file is Codex's "notes on the sheets". None of them is the same file as the Work math notes of that folder (all 221 pairs compared). Those without a codex:<folder>#<n> row: SA21 27, SA01 1, SA03 1, SA04 1 (30 files, about 12k words). The full list is in GLOBAL\COVERAGE.tsv, column codex_only_unplaced.

<!-- AUTO from _broad_tools/build_global.py, 2026-11-18 15:33 UTC -->
## Cross-topic entries for a6d42bf6fe2b0d8a8 (topics SA01 SA02 SA03 SA04 SA10 SA11 SA21), built 2026-11-18 15:33 UTC

Tags: GLOBAL\GLOBAL_OBJECTS.tsv gives every item a tag H??? (same object across topics) and a theme TH-nn (related objects). Name the tag in cross_topic ("= H00x") when an item of yours is that object.

### Same object in your topics and another agent's (12)
- H00K: the axioms of a tame topology on cote 120: the graph calculus, finite unions, categorical reconstruction, finite graph d | items SA10-19 SA20-12 | merged by: stated equal (= or 'same') in SA10-19
- H00M: later drafts on tame topology (121/049-073): canonical adapted partitions, incidence orders, conservativity, effective e | items SA11-3 SA20-15 | merged by: stated equal (= or 'same') in SA11-3
- H05G: the 'tubulure' and the 'ombre': where they occur (149/133, a dated 1975 étale-tubular passage), germs and neighbourhood  | items SA10-2 SA20-8 | merged by: stated equal (= or 'same') in SA20-8
- H00C: formal de Rham data and derived Hom toward the crystal construction (formally exact, formal Poincaré, torsor extension) | items SA04-13 SA23-44 | merged by: stated equal (= or 'same') in SA04-13
- H00D: filtered modules for Barsotti-Tate groups: fibre functors, Tate twists, descent with Frobenius (cote 161 sheets) | items SA04-15 SA23-36 | merged by: stated equal (= or 'same') in SA04-15
- H03F: projective connections and opers: rank-two bundles, PGL_2 and Borel reductions, Killing forms, the bad characteristic tw | items SA04-9 SA32-4 | merged by: stated equal (= or 'same') in SA32-4
- H00B: Picard-Fuchs equations and integrals: Gauss-Manin connection, period compatibility (cote 93, scans 219-230) | items SA04-12 SA23-43 | merged by: stated equal (= or 'same') in SA04-12
- H00L: the 'remords' and whether he resolved it: his own reconsideration, the calculation that convinced him, the December 1981 | items SA10-3 SA20-9 | merged by: stated equal (= or 'same') in SA10-3
- H00O: a Tannakian-type duality over a field extension k'/k (cotes 153, 155): pro-objects, the idealizer quotient, descent data | items SA11-6 SA20-17 | merged by: stated equal (= or 'same') in SA11-6
- H00E: MPL_93 package documentary and cross-links (cotes 93, 161-5) | items SA04-18 SA23-45 | merged by: stated equal (= or 'same') in SA04-18
- H00J: plane trees and their rotations (cote 152): the admissibility rule, orientation torsors, rotation sheets, a permutation  | items SA10-18 SA20-7 | merged by: stated equal (= or 'same') in SA10-18
- H00N: binomial and lambda 'analysers' (cotes 153, 155): products, coaddition, comultiplication, divided powers, optional axiom | items SA11-5 SA20-16 | merged by: stated equal (= or 'same') in SA11-5

### Other agents' items that point to your topics (23)
- SA08-18 (SA08, H04T) -> SA04 SA04-9 [item id]: projective curves: the pointed torsor with a stabilizer, holomorphic splitting, the nonsplit jet bundle (proje | its cross_topic: SA32 cote 159 (projective connections, jet extensions): link; = H04T; related: SA32-5 (jet extensions), SA04-9 (H03F), theme TH-25
- SA20-12 (SA20, H00K) -> SA10 SA10-19 [item id]: the axioms of a tame topology on cote 120: the graph calculus, finite unions, categorical reconstruction, fini | its cross_topic: SA20-13/14/15 (cote 121); the o-minimal literature (van den Dries); the stratification research runs (link only); = H00K (SA10-19)
- SA20-15 (SA20, H00M) -> SA11 SA11-3 [item id]: later drafts on tame topology (121/049-073): canonical adapted partitions, incidence orders, conservativity, e | its cross_topic: = H00M (SA11-3)
- SA20-16 (SA20, H00N) -> SA11 SA11-5 [item id]: binomial and lambda 'analysers' (cotes 153, 155): products, coaddition, comultiplication, divided powers, opti | its cross_topic: = H00N (SA11-5)
- SA20-17 (SA20, H00O) -> SA11 SA11-6 [item id]: a Tannakian-type duality over a field extension k'/k (cotes 153, 155): pro-objects, the idealizer quotient, de | its cross_topic: = H00O (SA11-6)
- SA20-7 (SA20, H00J) -> SA10 SA10-18 [item id]: plane trees and their rotations (cote 152): the admissibility rule, orientation torsors, rotation sheets, a pe | its cross_topic: = H00J (SA10-18)
- SA20-8 (SA20, H05G) -> SA10 SA10-2 [item id]: the 'tubulure' and the 'ombre': where they occur (149/133, a dated 1975 étale-tubular passage), germs and neig | its cross_topic: = H05G (SA10-2, tubulure and ombre)
- SA20-9 (SA20, H00L) -> SA10 SA10-3 [item id]: the 'remords' and whether he resolved it: his own reconsideration, the calculation that convinced him, the Dec | its cross_topic: SA31 (149); = H00L (SA10-3)
- SA22-0 (SA22, H0KN) -> SA10 [cote 153]: 'Travaux de thèses' (cote 66, 1964): a numbered list of 28 thesis problems on four sheets, with later marginal | its cross_topic: the SGA editions (the 'Questions dans SGA' reference); SA20-17 (the Tannakian duality of cotes 153 and 155) for the fibre-functor and Saaved
- SA22-7 (SA22, H0KV) -> SA10 SA10-2 [item id]: coordinates from cutting data (B block): shadow comparison, tangent germs, the propagation tensor as a local n | its cross_topic: link H05G (SA10-2: the ombre on cote 67)
- SA23-24 (SA23, H0DD) -> SA01 [cote 93]: connections on fibre products; regular rings with non-free Omega^1 (cote 23, scans 33-50) | its cross_topic: cote 93 (connections, SA23-43/44)
- SA23-34 (SA23, H0DO) -> SA01 [cote 93]: Serre's 1967 paper on Galois groups attached to p-divisible groups (cote 161-5, scans 3-17) | its cross_topic: cote 93 (P93 X01 links); Tate, Driebergen 1966
- SA23-36 (SA23, H00D) -> SA01 [cote 93]: his notes on Barsotti-Tate groups and F-isocrystals: T_cr, filtered torsors, descent and Frobenius data, cohom | its cross_topic: cote 93 (crystals, SA23-44); cotes 159 and 64 (named by P93 X06); Hua modernised reading of 161-5
- SA23-38 (SA23, H0DR) -> SA01 [cote 93]: Quillen's tapis: formal categories and groupoids over a scheme, augmented pro-rings (cote 162-5) | its cross_topic: cote 93 scans 231-236 (stratifications, universal P, torsors); cote 161-5 (crystalline data)
- SA23-43 (SA23, H00B) -> SA01 [cote 93]: Picard-Fuchs equations and integrals: Gauss-Manin connection, period compatibility (cote 93, scans 219-230) | its cross_topic: cote 93 (outside SA23); MPL_93_002-046
- SA23-44 (SA23, H00C) -> SA01 [cote 93]: crystals and stratifications: formal Poincare lemma, the universal P, torsors, derived Hom (cote 93, scans 231 | its cross_topic: cote 93 (outside SA23); cote 162-5 (Quillen); MPL_93_002-046 item C30
- SA23-45 (SA23, H00E) -> SA01 [cote 93]: MPL_93 package documentary and cross-links (cotes 93, 161-5) | its cross_topic: cotes 93, 161-5, 159, 64
- SA31-4 (SA31, H0IS) -> SA10 SA10-8 [item id]: asphericity and exit paths for the boundary strata: the normal-bundle model, aspherical pieces, the sphere obs | its cross_topic: link H05L (SA10-8, exit paths and stratified homotopy types)
- SA32-2 (SA32, H0JE) -> SA01 [cote 93]: the folder's programme: uniformization of curves by canonical projective connections | its cross_topic: cotes 93, 64 (proposed by the dossier; RESULTS_STATE MPL_93 P01, P09); = H0JE; related: SA04-8 (H03E), SA04-9 (H03F), theme TH-25 (inbox 15:
- SA32-2 (SA32, H0JE) -> SA04 SA04-8 [item id]: the folder's programme: uniformization of curves by canonical projective connections | its cross_topic: cotes 93, 64 (proposed by the dossier; RESULTS_STATE MPL_93 P01, P09); = H0JE; related: SA04-8 (H03E), SA04-9 (H03F), theme TH-25 (inbox 15:
- SA32-2 (SA32, H0JE) -> SA04 SA04-9 [item id]: the folder's programme: uniformization of curves by canonical projective connections | its cross_topic: cotes 93, 64 (proposed by the dossier; RESULTS_STATE MPL_93 P01, P09); = H0JE; related: SA04-8 (H03E), SA04-9 (H03F), theme TH-25 (inbox 15:
- SA32-4 (SA32, H03F) -> SA01 [cote 93]: projective connections as second-order operators (opers) and their Schwarzian normalization | its cross_topic: = H03F (SA04-9, cote 93: projective connections and opers)
- SA32-4 (SA32, H03F) -> SA04 SA04-9 [item id]: projective connections as second-order operators (opers) and their Schwarzian normalization | its cross_topic: = H03F (SA04-9, cote 93: projective connections and opers)

### Notes of your topics without a PLACEMENT row (4 topics; see GLOBAL\COVERAGE.tsv)
- SA01: NOTES_INDEX rows unplaced 0; Pro packages missing from NOTES_INDEX and unplaced: none; Work folders unplaced: none; Codex/API folder notes on the sheets (inputs\SA01\codex\<folder>_notes.md, not the Work math notes) unplaced: J81-03
- SA03: NOTES_INDEX rows unplaced 0; Pro packages missing from NOTES_INDEX and unplaced: none; Work folders unplaced: K93-07; Codex/API folder notes on the sheets (inputs\SA03\codex\<folder>_notes.md, not the Work math notes) unplaced: K93-07
- SA04: NOTES_INDEX rows unplaced 0; Pro packages missing from NOTES_INDEX and unplaced: MPL_8_079-081+9+4+100; Work folders unplaced: K70-02 K70-04 K70-06 K77-05; Codex/API folder notes on the sheets (inputs\SA04\codex\<folder>_notes.md, not the Work math notes) unplaced: K93-07
- SA21: NOTES_INDEX rows unplaced 0; Pro packages missing from NOTES_INDEX and unplaced: none; Work folders unplaced: none; Codex/API folder notes on the sheets (inputs\SA21\codex\<folder>_notes.md, not the Work math notes) unplaced: J156-7-09 J156-7-11 J156-7-12 J156-7-13 J156-7-14 J156-8-01 J156-8-02 J156-8-04 J156-8-06 J156-8-07 J156-8-10 J156-8-11 J156-8-14 J156-8-15 J156-8-16 J156-9-01 J156-9-02 J156-9-03 J156-9-04 J156-9-05 J156-9-08 J156-9-09 J156-9-11 J156-9-14 J156-9-15 J156-9-16 J156-9-18

<!-- /AUTO -->
