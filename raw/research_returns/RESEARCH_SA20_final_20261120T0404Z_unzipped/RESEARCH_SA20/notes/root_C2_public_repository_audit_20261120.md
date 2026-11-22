# C.2(b): public repository metadata audit

We completed this bounded root access check at 2026-11-20T02:01:13.571349+00:00. It does not change the original-source status.

We queried the public OpenAlex DOI work endpoint and Semantic Scholar DOI paper endpoint for 10.2307/1970720 and 10.2307/1970785. Both returned the exact requested title. OpenAlex reports closed access, no repository full text, and only the DOI landing page, with no PDF URL. Semantic Scholar likewise returns an empty openAccessPdf URL and CLOSED status. These are observed repository records, not a proof that no authorized copy exists elsewhere.

| Original | OpenAlex endpoint | Semantic Scholar record |
|---|---|---|
| Hartshorne1968 | https://api.openalex.org/works/https://doi.org/10.2307/1970720 | https://www.semanticscholar.org/paper/71030bdcc40ba626f436ffb23093a0ddaacffc12 |
| Ogus1973 | https://api.openalex.org/works/https://doi.org/10.2307/1970785 | https://www.semanticscholar.org/paper/b67006fddaa169ade6dd6ba635629049fc82e241 |

Fresh exact-title web searches again returned Annals metadata, the partial SciSpace introduction, author-profile bibliographies, and later citations. None supplies Hartshorne Proposition4.3/Theorem7.5 or Ogus Section3. Search references: turn719214133search0/1, turn375938768search1/2/3/4/5. We did not treat later mathematical papers as original-page evidence. No source-access upgrade or qualifying movement is claimed.

## Publisher HTML follow-up

At02:10–02:11UTC we also fetched both original Annals article landing pages successfully with HTTP200 and inspected their link targets. The download-related links were the DOI, the old JSTOR journal destination, and the generic `/pdf_information` page; we found no original-PDF target in that returned HTML. We then opened `/pdf_information` (source reference `turn931176362view0`), which contains generic Acrobat information only. A successful landing-page fetch is not an original-page opening. The exact requested original passages remain unopened.

## Bounded public archive-catalog follow-up

At02:29UTC we queried the public Internet Archive advanced-search JSON endpoint for the exact journal title and each requested year. The1968 query returned only `sim_annals-of-mathematics_1968_87_index`; the1973 query returned only `sim_annals-of-mathematics_1973_97_index`. Neither is the requested volume88 or98 article. Separate exact identifier queries for `jstor-1970720` and `jstor-1970785` both returned zero records. These are actual search results, not a claim that every possible archive copy has been exhausted. Fresh primary-source web searches returned the same Annals metadata and later citations, with no original-page upgrade. Source references: `turn228249183search0/2`, `turn850433987search0/10`.

At02:46UTC another bounded exact-title/PDF search again returned publisher
metadata and later citations (references `turn321351595search0` and
`turn321351595search3`). We then reconciled this with the earlier complete
access log `agents/singularities_duality/logs/C_original_source_pass_1750.md`.
That earlier log did identify the exact issues
`sim_annals-of-mathematics_1968-11_88_3` and
`sim_annals-of-mathematics_1973-09_98_2` through public metadata, but both
were access restricted and their TextPDF/DjVuTXT entries were private.
The later catalog searches finding only indexes do not supersede that
earlier metadata evidence. We did not request private files or infer that
the originals were absent from the archive. The theorem pages remain
unopened, and no movement is claimed.
