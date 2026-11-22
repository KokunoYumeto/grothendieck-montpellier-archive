# Lieberman original: bounded independent offprint/archive route

19 November 2026, approximately16:30–16:35UTC. Reviewer: GPT-6 Astra
(OpenAI), agent `part_b_cycles`.

## Outcome

The relevant original mathematical passage in David I. Lieberman,
*Numerical and Homological Equivalence of Algebraic Cycles on Hodge
Manifolds*, **American Journal of Mathematics90(2)(1968),366–374**, remains
**NOT OPENED**. No original thesis or offprint containing its complete
relevant statement was located in this bounded search. This preserves the
existing named-source gate; it is not a new mathematical gap in the
separately proved Kleiman-based argument.

The stopping condition is the absence of a further distinct advertised
source route in these results. It is not a claim that no public copy exists
anywhere. A relevant complete original theorem passage would suffice; no
requirement to inspect the whole article or thesis was imposed.

## Prior-route checks

Before any new request, the reviewer read the route records in
`notes/part_c_lieberman_original_followup.md`,
`notes/root_original_followup_03.md`,
`notes/part_b_source_followup_20261119.md`,
`notes/secondary_source_retrieval_20261119.md`, and
`notes/part_b_lieberman_variant_search.md`, including the later TIMDEX,
JSTOR issue/XML, corrupted introductory OCR and public-code-index updates.
The already denied/challenged JSTOR, private Internet Archive files,
MIT/Princeton catalogue forms, SciSpace PDF destination and LibCats query
were not retried. No contact, loan, login or author-copy request was sent.

## New web queries

One three-query batch tested a different offprint/archival angle:

1. `"Lieberman" "numerical" ("offprint" OR "tiré à part" OR "tirés-à-part")`
2. `"Lieberman" (site:archives.ihes.fr OR site:archives.umontpellier.fr OR site:patrimoine.bu.umontpellier.fr)`
3. `"Lieberman" "Hodge manifolds" ("collection" OR "Nachlass") -site:researchgate.net -site:scispace.com -site:arxiv.org`

Actual result references are `turn890473001search0`–`search9`. The results
were the already known publisher/DOI-only records, later citing works,
and unrelated offprint or surname hits. None advertised a new target
original or complete theorem preview. Those already exhausted result links
were not requested again.

The exact executed code-mode JavaScript is saved in
`code/part_b_lieberman_archival_queries1.js`, with its full result and
measured **1.015-second** tool-call duration in the matching output JSON.
This duration is not an estimate of the whole research interval.

## New public IHES archive route

The global IHES archive form had already been read during the distinct
Gabber search. Its saved ordinary GET form explicitly advertises action
`/search`, fields `query`, `query_type`, and the Item/File record controls.
The new utility reused that inspected form; no endpoint was guessed.

| New query | Actual public URL | Read result |
|---|---|---|
| Author surname | <https://archives.ihes.fr/search?query=Lieberman&query_type=exact_match&record_types%5B%5D=Item&record_types%5B%5D=File> | HTTP200; displayed2 results |
| Exact title fragment | <https://archives.ihes.fr/search?query=Numerical+and+Homological&query_type=exact_match&record_types%5B%5D=Item&record_types%5B%5D=File> | HTTP200; displayed0 results |

The two author results were followed at their actual advertised links:

| Advertised record | Identity actually read | Scope |
|---|---|---|
| <https://archives.ihes.fr/document/F3_3_2_3_1.pdf> | *Ouvrages de mathématiques et physique élaborés à l'IHES: année académique1975–1976*, authorIHES, annual/scientific reports collection, sourceF3.3.2.3/1; Lieberman appears among its subject tags | A publication-list catalogue record, not the1968 article or1966 thesis. Opened as `turn758444731view0`, lines18–30 |
| <https://archives.ihes.fr/document/M_72_04.pdf> | *La Théorie de HodgeIII*, authorDeligne, dateJanuary1972, sourceM/72/04; Lieberman appears among its subject tags | A different author's work, not the target original. Opened as `turn758444731view1`, lines18–32 |

Although both record URLs end in `.pdf`, the actual opened responses are
**HTML catalogue pages**. No PDF-content reading is claimed. The record
identities resolve both returned hits without treating an unrelated work
as Lieberman's original. The zero title result concerns only this specific
public archive query and its current metadata/indexing.

The exact executed public-HTTP utility is
`code/part_b_lieberman_ihes_public.py`. Its two requests ran concurrently,
starting at **2026-11-19T16:33:43.522122+00:00**, and the complete program
elapsed **10.013552460seconds**. The author and title requests individually
took10.012166673 and10.007139224seconds. The output JSON retains the actual
URLs, response statuses, byte counts, hashes, displayed counts, full parsed
text and advertised links. The corresponding public HTML/text records are
saved under `sources/part_b_lieberman_ihes_*`.

The two later web-tool opens are preserved as the exact executed
`code/part_b_lieberman_ihes_documents.js` and matching output JSON;
their measured tool-call duration was **0.889seconds**. This records two
open commands, not a claim about the search service's internal HTTP count.

## Counts, limitations and manuscript effect

- 3 new web-search queries in 1 timed tool call.
- 2 new ordinary public catalogue HTTP requests, both 200; neither requested
  a mathematical source file.
- 2 new web-tool record-open commands identifying the actual returned hits.
- 0 original mathematical pages obtained; 0 restricted files requested;
  0 mathematical finite checks or symbolic programs rerun.

No theorem, bibliography-opening status or mathematical premise was
changed. The programme inventory was updated from the saved records only.
The parent was informed of the exact negative result and the unchanged
source gate. The separately opened Kleiman originals remain the evidence
for the already proved mathematical application.
