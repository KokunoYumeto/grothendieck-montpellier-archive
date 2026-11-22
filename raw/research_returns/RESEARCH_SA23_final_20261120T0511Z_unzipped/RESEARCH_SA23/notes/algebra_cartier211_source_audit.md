# Cartier 211: exact proof-addition reference and one contemporary cited source

Checked on 2026-11-20. This branch belongs to existing statement `geo-H-history`. It follows an exact reference in a source already opened; it does not recertify the earlier retrospective/correspondence searches.

## Result

No dated identification of the cote 1 Hilbert trace/genus-zero proof was found. Cartier's entire exposé was directly read from the facsimile. A narrowly selected follow-up to its explicit reference [1] also gave no such witness in the pages actually checked.

## Cartier source: opened

Pierre Cartier, *Classes de formes bilinéaires sur les espaces de Banach*, Séminaire Bourbaki, exposé 211, **February 1961**, collected pagination **85–98**.

- Metadata: https://www.numdam.org/item/SB_1960-1961__6__85_0/
- Original-text facsimile: https://www.numdam.org/article/SB_1960-1961__6__85_0.pdf
- Author's publication list: https://www.ihes.fr/~/cartier/REFERENCES/seminaires.html , entry [110].
- Local PDF: `sources/algebra_cartier211_facsimile.pdf`.
- **1,241,413 bytes; SHA256 d4cc5cd557e0ca90eb35790aefc54d9e9e26fde8a881ddb9e79cf14dfa718111**.
- Fifteen physical PDF pages comprise the Numdam cover and fourteen text pages. **Every text page, PDF 2–15 / printed 85–98, was displayed individually and visually read.** Renders are `sources/algebra_cartier211_page002.png` through `015.png`.
- This is a facsimile, not a modern mathematical transcription. The header dates the exposé February 1961. Cartier's own bibliography identifies the collected SMF edition as 1995. The physical first printing was not collated; the dated seminar header and Grothendieck's actual 1961 reference are the evidence used.

### Exact content relevant to the question

The introduction (p.85) identifies the source as Grothendieck's 1956 metric résumé. Part I§3 (p.87) gives a finite-rank trace test and the Dixmier–Schatten singular-value representation. The other trace computation (p.94) uses a finite-rank projector. These are not the general Hilbert eigenvalue-sum assertion or a determinant/genus-zero proof. No supplied unpublished proof, dated letter, enclosure or cote 1 identification appears in the fourteen pages. The bibliography (p.98) lists four published sources. Cartier credits reference [1] for the corollary's proof at p.96.

The exact printed proof-addition reference was re-read at p.143 of Grothendieck's *The trace of certain operators*, in the previously saved original spread `sources/algebra_history_trace1961_original_p002.png`. It identifies Cartier211 and says it was added at proof correction. This dates that reference/use, not an older manuscript.

## The explicit reference [1]: bounded original follow-up

Ichiro Amemiya and Kôji Shiga, *On tensor products of Banach spaces*, **Kodai Mathematical Seminar Reports 9(4) (1957), 161–178**, DOI **10.2996/kmj/1138843934**.

- Publisher record actually opened: https://www.jstage.jst.go.jp/article/kodaimath1949/9/4/9_4_161/_article/-char/en
- Advertised original PDF actually downloaded: https://www.jstage.jst.go.jp/article/kodaimath1949/9/4/9_4_161/_pdf/-char/en
- The actual download link was followed from the opened issue listing; the web reader timed out, but an ordinary unauthenticated local retrieval returned HTTP200.
- Local original: `sources/algebra_amemiya_shiga1957.pdf`, **1,938,008 bytes**, SHA256 **15c64b91aa81a8d30f8c909c08367f5d74bebeeb8ba1c1322272e92cc8da66bd**.
- Full18-page text extracted/searched for names, trace/genus, communications, manuscripts and acknowledgments. **Only printed pp.161,166,178 were directly displayed/read**, including the complete introduction, one matching attribution, conclusion and full bibliography. The remaining pages were not visually certified.

The introduction presents independent proofs of results from the metric résumé; it does not acknowledge a supplied Grothendieck proof. Its receipt line is **12 September 1957**. The final bibliography contains three published Grothendieck works. No dated Hilbert trace/genus-zero manuscript identification occurs in the inspected pages or returned search contexts. Cartier's printed reference gives the range **161–186**; the publisher and original final page establish **161–178**. The receipt dates this paper, not cote 1.

## Reproducibility, search aid limitation and source flags

- Raw web148–153 and `notes/algebra_cartier_query_manifest.json` preserve queries, openings and the advertised download path.
- `code/algebra_cartier_fetch61.py`; `logs/algebra_cartier_fetch61.json`: original Cartier retrieval, SHA, full extraction and all-page rendering.
- `code/algebra_cartier_follow62.py`; `logs/algebra_cartier_follow62.json`: corrected local word-boundary search and Amemiya–Shiga retrieval/extraction/selected rendering.
- Script61 initially over-escaped the `Tr` word boundary. Script62 corrects that search locally without re-downloading Cartier. OCR still omits the p.94 trace formula; the actual visual reading identified it. Keyword counts are not treated as an exhaustive original-page inspection.
- `code/algebra_cartier_record63.py`; `logs/algebra_cartier_record63.json`: final actual-reading record and documentary event.
- Bibliography key **algCartier211** has an explicit Opened flag in `notes/algebra_cartier_references.bib`. Amemiya–Shiga metadata and exact partial scope are recorded here without adding an unused main-paper entry.

No outside communication, account, restricted retrieval, or access workaround was used. No mathematical theorem or priority claim was changed. The next assigned Dunford–Schwartz search is a separate branch and is not counted as part of this completed Cartier check.

