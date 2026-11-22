# CSG unpublished-work and transcription finding aids

On 20 November 2026 we opened both CSG finding aids in the web tool and
retrieved their actual HTML. We read the early scientific entries, the
early correspondence descriptions and the archive-scope paragraphs.
We extracted and searched the full returned text of each page; this is
not a claim to have read every linked original. No original linked from
these two finding aids was newly inspected on this route.

The unpublished-work page explicitly presents a selection, not a complete
inventory. Its early scientific entries start with the July 1955
homological-algebra draft and proceed through algebra, bundles and
varieties. The transcription page's early correspondence points to the
Dixmier letters already audited separately. Neither returned text contains
Fredholm, Lidskii, nuclear-operator, trace or cote-1 keywords in the
recorded normalized search. This bounded catalogue result does not prove
that no such document exists elsewhere or in unlisted holdings.

The archive paragraphs describe the later transfers of the Montpellier
papers and a separate BnF collection of much later writing. Neither
description identifies or dates the target trace/genus-zero sheets.
The route therefore supplies no new manuscript-date witness and does not
make the open gate smaller. A specific dated duplicate, enclosure or
authorial reference would still be needed.

## Reproducible scope

- `https://csg.igrothendieck.org/unpublished-works/`: 251,320 bytes;
  SHA256 `7a404957e66d0d04c4b54252419c30a810599cc7c10b714f69566eeaca5ab126`;
  1,263 extracted text fragments and 297 actual links.
- `https://csg.igrothendieck.org/transcriptions/`: 257,190 bytes;
  SHA256 `5722ef4cbfcc0809f301c6c8b3a2ecf91981ae941334c0c0db75976995bee751`;
  1,493 extracted text fragments and 322 actual links.
- Exact retrieval outcomes: `logs/root_history_fetch15.json` and
  `logs/root_history_fetch16.json`. Web responses: `notes/root_history_web55.json`
  and `notes/root_history_web56.json`.
- `code/root_csg_catalogue_audit.py` records the complete keyword scope,
  output paths and elapsed time in `logs/root_csg_catalogue_audit.json`.
  An initial exploratory import of unavailable `bs4` failed before parsing;
  the completed extractor uses Python's standard library. Source-text and
  link caches stay with the other reproducible source caches.
