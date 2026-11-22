# Reading the verification files

The fifteen diplomatic page files are in pages/. Their concatenation is K58-03_transcription.tex. The standalone wrapper uses the supplied PREAMBLE.tex. Page and source-line numbers in the registers refer to the individual page fragments.

| Material | Location within this return |
|---|---|
| Page files before the independent comparison | audit/first_pass/ |
| Hard-place readings and independent unusual words and accents | K58-03_blind.tsv and audit/blind_words.tsv |
| Localized differences, decisions and subsequent refinements | K58-03_blind_compare.md, audit/anchors.tsv and audit/blind_followup.tsv |
| Pre-witness page files and hashes | audit/frozen_pages/ and audit/frozen.sha256 |
| Frozen doubts, witness collations and final hashes | audit/frozen_places.tsv, audit/witness_places.tsv and audit/witness.sha256 |
| Mathematical notation and occurrences of indexed or raised i and j | audit/formulas.tsv and audit/indexed_i_j.tsv |
| Scope of mathematical checks | CHECK_EVENTS.tsv and audit/degree_checks.tsv |
| Times, structural checks and post-notes verification | progress.log and audit/balance_witness.tsv |

From the directory containing the standalone wrapper, these commands check the current sources without compiling them.

~~~sh
python3 assemble_and_check.py
python3 verify_stage.py check witness
python3 apply_witness.py
~~~

The third command verifies all preserved frozen page hashes and their assembled hash. Then it reconstructs each final page in memory using only the changes inside the original marked spans, and checks the result against the delivered page. The blind-comparison program can regenerate its report with the original pre-audit page files as its baseline.

The image crops live beside the output. To recreate them from the supplied scans, use the following command with Pillow installed. Both coordinate tables are included. The second table locates tighter rectangles within some of the enhanced crops. The crop names in the witness table point to the final inspection rectangles.

~~~sh
python3 recreate_crops.py /path/to/unpacked/scans --dest ../crops
~~~
