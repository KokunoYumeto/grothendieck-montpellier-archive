# Original 1953 thesis: bounded public-source search

Recorded 2026-11-20 03:38 UTC. Investigator: algebra_letters, GPT-6 Astra Pro, inherited effort. This is a source-status audit for the existing `geo-H-history` / Lead 6 question. It does not introduce a new mathematical statement.

## Result

The public catalogue route now identifies a **specific physical holding** of the 1953 thesis, beyond the bibliographic record already opened by root. **No public original thesis scan or item-level comparison with cote 1 was opened.** No source inspected in this branch identifies the particular Hilbert trace/genus-zero proof sheets or supplies their date.

The decisive new details are: **RCR 751052113; exemplar 28780237X; shelfmark `Y Math 1953 (2) -4`**. The CCFr institutional record resolves that RCR to **Sorbonne Université, Bibliothèque de Sorbonne Université, Biologie–Chimie–Physique Recherche**, at **4, place Jussieu**. This is the BCPR holding; it must not be relabelled as the separate Mathématiques–Informatique Recherche library merely because both are at Jussieu.

## Actual primary records opened

| Source and exact URL | What was read | What it establishes |
|---|---|---|
| ABES public UNIMARC XML, <https://www.sudoc.fr/108391841.xml> | Full XML, HTTP 200, 5,348 bytes | Bibliographic metadata and one item record, including the exact shelfmark and exemplar number |
| ABES `multiwhere`, <https://www.sudoc.fr/services/multiwhere/108391841> | Full XML, HTTP 200, 267 bytes | One returned holding, RCR 751052113, short name `PARIS-BSU-BCPR` |
| CCFr institutional record, <https://ccfr.bnf.fr/portailccfr/ark:/16871/0027818> | Full web-reader record, especially lines 55–86 | Institutional name, Jussieu address and matching RCR; catalogue record last updated 23 March 2021 |

The services were located through the actual ABES documentation, not an invented private endpoint:

- <https://abes.fr/api-et-web-services/> lists the public Sudoc services.
- <https://github.com/abes-esr/openapi/blob/master/sudoc.yaml>, the documented `multiwhere` section, identifies `/services/multiwhere/{PPN}`.
- <https://abes.fr/reseau-sudoc/reutiliser-les-donnees-sudoc/formats-de-donnees-disponibles/> documents the `.xml` representation and preservation of provenance fields.

The original Sudoc HTML and RDF were already opened by root at <https://www.sudoc.fr/108391841> and <https://www.sudoc.fr/108391841.rdf>. They remain available under `sources/root_thesis_sudoc108391841.html` and `sources/root_thesis_sudoc108391841_rdf.html`. This branch independently read those saved records and then retrieved the additional public representations above.

### Exact XML locators

- Field `200$a`: the catalogue title literally reads **Produits tensoriels popologiques et espaces nucléaires**, retaining its apparent spelling error.
- Field `200$f`: Alexandre Grothendieck.
- Field `214`: Paris, Faculté des sciences, 1953.
- Field `215`: **1 vol. (130 f.); 30 cm**.
- Field `328`: thesis, Sciences. Mathématiques, Paris, Faculté des sciences, 1953.
- Field `034$0`: OCLC **493225354**.
- Field `930$5`: **751052113:28780237X**.
- Field `930$b`: **751052113**.
- Field `930$a`: **Y Math 1953 (2) -4**.
- No `856` field or digital-object link occurs in this retrieved XML.
- Field `801$b` is **Abes**, and `801$c` is **20231213**. These provenance fields were retained in the full saved XML.

The 2006 record creation, 2023 bibliographic modification and 2024 item modification timestamps are **catalogue metadata**, not dates of composition, transcription or deposit inferred for the mathematics. One holding returned by `multiwhere` is not a claim that there is only one surviving copy worldwide. The 130-folio extent is not an identification with cote 1, whose different archival object has not been collated against this thesis.

## Public digitization and catalogue follow-up

The actual public MIR library home, <https://www.math-info-paris.cnrs.fr/bibli/>, was opened to locate its advertised catalogue and digital-library links. Its linked Sorbonne Primo catalogue returned **403**:

<https://sorbonne-universite.primo.exlibrisgroup.com/discovery/search?vid=33BSU_INST%3A33BSU>

That route was stopped. No account, alternate restricted API, access challenge or proxy was attempted. The CCFr BCPR record points to the same catalogue host; no original thesis content is counted as opened there.

The independently public NUMiR entry actually linked by the library home is:

<https://www.numir.org/accueil/accueil.php>

The web reader returned **502 Bad Gateway**. One ordinary unauthenticated HTTP retrieval then returned **503 Service Unavailable**. The public link was not inspected successfully, and no claim about the contents of its collection follows. The separately advertised `ezproxy` link was not used.

Targeted public searches for the thesis and author under Sorbonne's heritage domain, NUMiR and Sorbonne Primo did not produce an original thesis scan. Search-result absence is not proof that a scan is unavailable elsewhere. Exact-title and folio-count searches previously performed by root were not treated as proof of nonexistence.

## Modern exhibition brochure: classified, not confused with a thesis facsimile

The public 37-page brochure at <https://exposition-grothendieck.org/wp-content/uploads/2025/05/Livret.pdf> was retrieved by ordinary HTTP after the web reader rejected its 42 MB size. Its full native text was searched, and two selected pages were rendered and **actually displayed and read**:

- Physical PDF page 5, printed p. 4: identifies the 2024–2025 Toulouse exhibition and lists image-source institutions.
- Physical PDF page 10, printed p. 9: a modern illustrated career timeline includes the 1953 thesis title. It is **not an original thesis cover, manuscript leaf or deposit record**.

Only these selected pages received direct visual inspection in this branch. The complete brochure was not visually collated page by page. Its modern chronology does not identify the cote 1 proof.

## Reproducibility

- Raw web searches and openings: `notes/algebra_history_web97.json` through `notes/algebra_history_web102.json`. These preserve exact queries and source responses, including the ABES documentation, CCFr record and access errors.
- Retrieval script: `code/algebra_history_thesis45.py`; output `logs/algebra_history_thesis45.json` and `.txt`. It fetched the two ABES records and brochure in 10.412 seconds, 03:33:19–03:33:29 UTC.
- NUMiR retrieval and brochure page-selection script: `code/algebra_history_thesis46.py`; output `logs/algebra_history_thesis46.json` and `.txt`.
- Exact field extraction, source hashes and current-run check-event script: `code/algebra_history_thesis47.py`; output `logs/algebra_history_thesis47.json` and `.txt`.
- Full saved ABES records: `sources/algebra_history_thesis_unimarc108391841.xml` and `sources/algebra_history_thesis_multiwhere108391841.xml`.
- Brochure: `sources/algebra_history_thesis_exhibition_livret.pdf`, corresponding `.txt`, and selected images `sources/algebra_history_thesis_exhibition_p005.png` and `sources/algebra_history_thesis_exhibition_p010.png`.

SHA-256 values:

- UNIMARC XML: `9f37c77516cf5a69b3531c04965db4524031ce7656c8c3c399b7b0f6952b9d54`.
- `multiwhere` XML: `dfb511656fa77bf3a181d4b4cc8bd623b5180065db9966821bb89078e44ad358`.
- Brochure PDF: `a613c74328a478c3d72aba818c95efe9d8c403e332a86afbf6a569fac7e1636a`.

## Effect on the open historical gate

The physical holding is now specified more precisely. The manuscript-dating gate is unchanged: it still requires a dated identification of the particular proof or leaves, or an actually inspected original whose contents establish that identification. No bibliography, mathematical section or result status was altered by this bounded search.
