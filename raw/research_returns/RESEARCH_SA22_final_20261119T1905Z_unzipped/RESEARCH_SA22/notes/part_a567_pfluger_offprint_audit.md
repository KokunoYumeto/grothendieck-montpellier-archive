# Bounded Pfluger offprint / collected-paper audit

Date: 2026-11-19, approximately15:28–15:37UTC. Agent: part_a567.

## Scope and prior exclusions

At root's request I first read `notes/root_original_followup_03.md`, `notes/part_c_pfluger_tdl_original_audit.md`, and `notes/part_b_pfluger_jubilee_catalogue_audit.md`. The task was one distinct bounded institutional offprint/reprint/collected-paper route, not a repeat of the publisher, Internet Archive journal OCR, TDL, or Golden Jubilee inventories. The exact target remains A. Pfluger, *Ueber die Konstruktion Riemannscher Flächen durch Verheftung*, J. Indian Math. Soc. (N.S.)24(1960),401–412, issued1961 according to later original bibliographies. The prompt's explicit source entry is `upload/PROMPT(20261119-110314).md:216`, “A. Pfluger (1960).”

No denied or challenged endpoint was retried. In particular I did not request the already429 ETH bitstream, gated publisher content, or unsuccessful TDL routes. Existing finding-aid results were recognized and not represented as new offprints.

## Actual original opened: Huber–Kühnau1994, not Pfluger1960

Root supplied an observed GDZ PDF link, initially described as “Pfluger–Kühnau.” The actual first mathematical page gives **Alfred Huber and Reiner Kühnau**, *Stabilität konformer Verheftung*, Commentarii Mathematici Helvetici69(1994),311–321. This bibliographic correction was sent to root immediately and is preserved here. The filename retains the discovery label only; it is not an assertion of authorship.

- Public URL: `https://gdz.sub.uni-goettingen.de/download/pdf/PPN358147735_0069/LOG_0024.pdf`.
- Web-open ref: `turn684206443view0`; earlier tool screenshots `turn959480405view0` and `turn959480405view1` were not visibly rendered in the agent response, so they are not the evidence claimed for the subsequent visual reading.
- Ordinary retrieval HTTP200,906314bytes,12PDFpages (archive cover plus11articlepages), SHA256 `93148e48d75a799b8cf5881e57546e39caada1cb41b9444a936995b26d5ce487`.
- `code/part_a567_pfluger_kuehnau_retrieval.py` and `_output.json`: full URL, status, hash, scope, total retrieval/render runtime9.517221836002136seconds.
- **Actually visually read** printed311and321 using local images `sources/part_a567_pfluger_kuehnau1994_pdf2.png` and `_pdf12.png`.

Printed311 introduces the circle welding equation and credits Lehto–Virtanen[9] and Pfluger[11] with quasisymmetry as a sufficient condition. It says the first four sections generally assume a continuously differentiable angular homeomorphism. This is an original later paper's attribution, not the original1960 theorem or its full hypotheses. The first-page footnote only records that the work arose during the second author's visit to ETH. Printed321 reference[11] explicitly lists Pfluger, J. Indian Math. Soc.(N.S.)24(1960),401–412(1961). Neither page supplies a target-offprint link, repository item number, or original1960 passage. The final addresses identify Huber in Zürich and Kühnau at Halle; I did not turn those postal addresses into speculative download URLs or send requests to people.

## Exact query records and results

Five preserved raw query/result files contain the complete actual query strings and engine outputs:

1. `code/part_a567_pfluger_offprint_queries.json`:2system1 queries for Pfluger/Verheftung with Sonderdruck/offprint/reprint and AlbertPfluger with Gesammelte/collectedpapers/Schriften. Relevant hits were the already read ETH finding aid and catalogues listing the1988 birthday volume. IAS also listed Kneser and Oka collected papers; CiNii's Hersch author record listed Pólya collected papers. None identifies Pfluger collected works. Main refs: `turn802983424search0`, `search1`, `search5`.
2. `code/part_a567_pfluger_offprint_variant_queries.json`:3system2 queries including Ueber/Über, Konstruktion, institutional/offprint terms, and Nachlass. Returned results were almost entirely unrelated physiology/engineering namesakes; this poor coverage is not evidence that no mathematical record exists. Ref group `turn855064927search*`.
3. `code/part_a567_pfluger_offprint_variant_verification.json`:2system1 verification queries for Sonderdruck and title variants with Sammlung/reprint/offprint. Returned later citations, Huber papers, and the1988 birthday volume; no target file. Ref group `turn956052653search*`.
4. `code/part_a567_pfluger_offprint_institutional_queries.json`:2system1 queries naming e-manuscripta/e-rara/ZORA or ETH/Swisscovery domains together with the title/Verheftung. Returned the existing ETH finding aid, an unrelated P.Pfluger dissertation, later citations, and the birthday volume. Ref group `turn651837624search*`.
5. `code/part_a567_pfluger_offprint_domain_query.json`:1system1 query with the explicit e-manuscripta/e-rara/ZORA domain filter. The returned results nevertheless included other domains, including HLS, a memorial notice, later papers, and the existing ETH finding aid. It is therefore **not** a completed inventory or reliable zero-result search of those catalogues. Ref group `turn746433753search*`.

Total:10search queries in5batches, with complete raw results saved. No search-tool program runtime was independently measured. There was one new original PDF retrieval, limited to identity/provenance reading of its first and last mathematical pages; no mathematical finite check was run.

## Outcome and exact negative scope

No advertised institutional offprint, reprint, or collected-paper copy of the1960 original was located in these returned results. This is a bounded discovery outcome, not a proof that no public copy exists. Hersch–Huber1988 is a birthday volume with a bibliography of Pfluger's works, not collected works or evidence of reprinting this article. The Huber–Kühnau1994 original closes only its own identity and later-attribution check. **Pfluger1960 remains unread; its named-source gate and all mathematical theorem statuses are unchanged.**
