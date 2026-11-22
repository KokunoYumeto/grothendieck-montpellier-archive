# Pfluger source: independent Jubilee-title catalogue route

19 November2026,15:20–15:24UTC. Researcher: GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode, agent `part_b_cycles`.

## Outcome

The new public Internet Archive metadata route did **not** identify the desired separate Indian Mathematical Society Golden Jubilee volume, issued1961, or recover Pfluger's original mathematical article. The source requirement remains **NOT OPENED**. This is a bounded negative catalogue result, not a proof that no public copy exists and not a mathematical gap in the already proved sewing theorem.

The first two searches deliberately imposed **no Indian, Mathematical, date, language, or media-type restriction**. Thus they cover the possibility that a separate volume has a generic Jubilee title without the society name. All requested public metadata responses returned HTTP200; no protected or original content file was requested.

## Exact catalogue coverage

| Query | Reported hits | Actual inspected metadata coverage | Outcome |
|---|---:|---|---|
| `title:("Golden Jubilee")` |601|A final explicitly identifier-sorted single response contained601rows and601distinct identifiers.|No record identified the desired mathematical volume. Relevant date/title/subject candidates are discussed below.|
| `title:("Jubilee Commemoration")` |17|All17records returned in one response and their identity fields inspected.|No desired volume. The sole unqualified *Golden Jubilee Commemoration Volume* title is the unrelated1937education volume below.|
| Title/description phrase `1907-1958` or `1907–1958`, together with Jubilee in title/description |0|Complete empty response for this exact query.|No matching metadata; this does not cover every possible spelling, missing field, or title variant.|

The union of the first two complete returned record sets has **614distinct identifiers** (four overlap). The catalogue JSONs retain title, creator, date/year, publisher, description and media type where provided. The sorted601-row snapshot is `sources/part_b_pfluger_golden_jubilee_sorted.json`; the compact title/identity inventory is `sources/part_b_pfluger_jubilee_titles.tsv`. The separate17-row response is `sources/part_b_pfluger_jubilee_commemoration_title.json`.

### Pagination correction, retained rather than hidden

The initial Golden-Jubilee query returned250 of601reported hits. Two further unsorted pages returned250 and101rows, but deduplication yielded only505distinct identifiers. Consequently those three pages were **not** treated as an exhaustive inventory. A single new query with `sort[]=identifier asc` and a650-row cap returned all601distinct identifiers. This materially resolves the observed unstable-pagination problem; it is not a repeated request to an access-denied service. Both the incomplete initial outputs and the complete sorted snapshot are preserved.

## Candidate identities and access metadata

Forty-four records in the sorted snapshot matched the deliberately broad inspection terms `1907`, `1958`, `1961`, `mathem`, `Pfluger`, `Madras`, `Poona`, or `Jubilee Commemoration`. Their identity fields were read. All undated text-record titles were also inspected, so a missing year was not itself used to reject a plausible anonymous volume.

- The only `mathem`/`Pfluger` text match was **ERIC_ED036670**, the1970National Council of Teachers of Mathematics research-reporting/education abstracts. Its actual description and title make it a different work. There was no Pfluger match.
- The only unqualified **Golden Jubilee Commemoration Volume** title, identifier **in.ernet.dli.2015.402019**, was followed to its actual public item metadata: https://archive.org/metadata/in.ernet.dli.2015.402019 . That record identifies Khandwala,Vidyut; date/copyright1937; Hindi; education; and the Bombay Shreemati National Damodar Thackersey publisher. It is not the1961mathematical-society volume.
- The latter item's file manifest advertises `2015.402019.Golden-Jubilee.pdf` (12,229,764bytes) and `2015.402019.Golden-Jubilee_djvu.txt` (2,069,001bytes), neither carrying a private flag in the returned metadata. **Neither file was requested**, because the item's identity is unrelated. An absent private flag is not converted into a claim that a file was actually opened.
- Other generic or missing-date records are identified as the Madras Veterinary College, Madras Law Journal, Numismatic Society of India, religious organizations, schools, or other explicitly named institutions. The Numismatic Society item with a `dli.calcutta` identifier is not silently identified with either mathematical society. Neither the desired Indian Mathematical Society volume nor the separate Calcutta Mathematical Society1958–59volume was recovered in this route.
- The1958and1961date matches include the Botanical Society of America, the Society of Women Musicians, church anniversaries, a museum catalogue, and Hong Kong congress volumes on muscle receptors, phytochemistry or economics. They are not substituted for the mathematical source.

No original cover or content page was fetched from these unrelated candidates. The final result concerns catalogue identification only; the source's theorem statement, hypotheses and proof remain unread by this route.

## Programs, requests and recorded times

All four actual utilities and complete outputs are saved. There were **seven public metadata requests**, allHTTP200, and **zero item-content requests**.

| Saved utility | Requests and scope | Recorded whole-program elapsed |
|---|---|---:|
| `code/part_b_pfluger_jubilee_catalogues.py` |Three independent title/variant queries;250-row initial cap each.|8.43622527700063s|
| `code/part_b_pfluger_jubilee_pagination.py` |Two remaining Golden-Jubilee pages; detected only505distinct identifiers across601rows.|7.466723319004814s|
| `code/part_b_pfluger_jubilee_complete.py` |One sorted650-row-cap snapshot;601distinct records returned.|8.107388953001646s|
| `code/part_b_pfluger_generic_jubilee_identity.py` |One actual generic-title item's public identity/file-access metadata; no file fetch.|7.680070205999073s|

Per-request elapsed times for the initial parallel batch are8.19108510499791s,7.81409575699945s,8.43090239400044s; the two pagination requests took7.444623927003704s and7.183113942999626s. The last two utilities have one request each, so their displayed elapsed times are also their recorded request/processing intervals. These are source-discovery utilities, not mathematical finite checks. No unknown runtime is estimated, and their elapsed times are not presented as the entire wall time of this research interval.

## Limits

This route is complete for the two exact title queries at the observed metadata snapshot, after correcting the concrete pagination issue. It is not an exhaustive search of all Internet Archive full text, all alternative titles, all catalogues, or every privately held print copy. It gives no reason to bypass an access restriction or retrieve a restricted file. The parent's separate original-source gate remains unchanged, and the other ongoing public-catalogue searches may continue independently.
