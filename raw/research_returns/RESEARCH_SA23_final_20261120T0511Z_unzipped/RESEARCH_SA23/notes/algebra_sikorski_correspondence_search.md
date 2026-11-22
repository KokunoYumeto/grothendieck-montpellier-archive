# Sikorski correspondence: bounded public-source search

Recorded 2026-11-20 03:23:20 UTC. Investigator: algebra_letters (GPT-6 Astra Pro, inherited effort).

## Question and conclusion

The original Grothendieck note *The trace of certain operators* states that it answers a letter from Roman Sikorski. Its receipt line is 20 June 1960. Could the original exchange, an enclosure, or a public item-level description identify the undated Hilbert trace/genus-zero proof in Montpellier cote 1?

**No such original letter or description was located in this bounded search.** The positive evidence remains the published note itself: it identifies Sikorski's question and uses the full Hilbert trace theorem, but supplies no date for the question and no identification of an older draft or enclosure. This negative search result does not imply that the correspondence is unpreserved, uncatalogued elsewhere, or absent from private/unpublished holdings.

## Primary institutional records actually opened

1. [IHES public Sikorski tag](https://archives.ihes.fr/items/browse?tags=SIKORSKI), opened as a complete 41-line public result page. It lists **four records**, all reports or seminar/visitor lists for **1966**, with no correspondence item. The two metadata records specifically opened were:
   - [F3.1.2.1/3](https://archives.ihes.fr/document/F3_1_2_1_3.pdf): visitors/permanent professors and statistics for 1966.
   - [F3.1.2.1/2](https://archives.ihes.fr/document/F3_1_2_1_2.pdf): seminar/conference list for 1966.
   
   Despite the URLs ending in .pdf, the opened responses were **HTML catalogue metadata**. These were not counted as original documents or original letters. The complete tag result, not just search-engine snippets, was checked.

2. [Official PAN archive inventory list](https://archiwum.pan.pl/index.php?Itemid=208&catid=17&id=511:spis-inwentarzy&option=com_content&view=article). The public page was opened in the web reader and then ordinarily downloaded. The complete downloaded HTML (HTTP 200, 511,640 bytes, SHA-256 `31e8b10cce00f6db213b07c984009654c4638ad61e9b5d8adadfe8864170c539`) was parsed with Python's standard HTML parser. Case-insensitive search of the full 30,433-character extracted text found **no “Sikors” occurrence**. The displayed mathematics rows include Zarankiewicz, Folkierski, Sierpiński, Steinhaus, Kuratowski and Mostowski; this establishes the scope of the finding-aid list examined, not the contents of every fonds.
   
   The web reader's `find` had also returned no Kuratowski match, whereas the complete downloaded page **does** contain Kuratowski, III–252. Accordingly, the negative Sikorski observation is based on the complete locally parsed page, **not** on the web reader's incomplete finding behavior. The source HTML, extracted text, retrieval script and output are preserved.

3. The PAN archive's public home/holdings-description navigation was opened. No reading-room appointment, request form, email, or other outside communication was submitted.

## Query record and exclusions

Raw outputs: `notes/algebra_history_web78.json` through `algebra_history_web84.json`. Queries covered English/French/Polish variants including:

- `Roman Sikorski Grothendieck correspondence 1960 letter archive`
- `Sikorski Grothendieck korespondencja archiwum`
- `"Grothendieck" "Sikorski" letter trace`
- `"Roman Sikorski" "archiwum"`
- `"Sikorskiego" "korespondencja" "Grothendieck"`
- `"Roman Sikorski" "spuścizna"`
- `site:archives.ihes.fr "SIKORSKI"`
- `"Sikorski" site:archiwum.pan.pl`
- `"Sikorskiego" "materiały" "archiwum"`, excluding Władysław/general
- `"Roman Sikorski" "letters"`
- `"Grothendieck" "Sikorski" "1960"`
- `"Grothendieck" "Sikorski" "correspondance"`
- `"Roman Sikorski" korespondencja archiwum matematyka`
- `site:archiwum.uw.edu.pl "Sikorski"`

Results about **Władysław Sikorski**, the general, were excluded from this mathematician's correspondence search. Roman Sikorski portrait metadata were not mistaken for correspondence. Restricted portrait assets, described as available only on institutional terminals, were not requested.

The adjacent 1961 publication *Remarks on Leżański's determinants*, Studia Mathematica 20, 145–161, DOI 10.4064/sm-20-2-145-161, was identified in publisher/search metadata. No original text or manuscript receipt of that article was inspected in this route, and no claim about its contents is made. Searches for its exact title produced no discriminating correspondence witness. Previously blocked ICM/publisher download endpoints were not retried.

## Reproducibility and stopping point

- Script: `code/algebra_history_sikorski41.py`.
- Outputs: `logs/algebra_history_sikorski41.json`, `.txt`.
- Sources: `sources/algebra_history_pan_inventory.html`, `.txt`.
- One initial run failed before any HTTP request because BeautifulSoup was unavailable. That original script and failure are retained under `algebra_history_sikorski41_initial_dependency_error`; the successful script uses only the Python standard library.
- Raw web result timestamps are recording times or explicitly bounded intervals, not invented publication dates.
- The existing original-paper audit is `notes/algebra_trace1961_source_audit.md`; citation key `algGrothendieckTrace1961`.

The bounded public route is now complete. The smallest remaining documentary requirement is still a **dated witness that actually identifies the cote 1 proof or its sheets**. The 1960 receipt of the separate published note is not that witness.

