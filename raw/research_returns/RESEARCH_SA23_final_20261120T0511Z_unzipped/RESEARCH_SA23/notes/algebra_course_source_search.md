# São Paulo course: distinct public-copy search

Checked on 20 November 2026 UTC, approximately 04:36–04:39. Existing statement: `geo-H-history`.

## Result and exact limit

**No original course pages, original foreword/preface, or original contents pages were obtained on this branch.** A public 1954/1958 French copy and a legitimate independent public copy of the 1973 English translation were sought. The opened sources supplied bibliographic metadata, not a dated identification of a trace/genus-zero draft. No claim about the contents of the unread course is made.

Before searching, `notes/geometry_editorial_course_date_audit.md` was read in full. The Circle `Ask.pdf` request notice, the dark Internet Archive item, and the denied Geotoppos route were not requested again. No account, outside contact, hidden file URL, or access workaround was used. The paper and bibliography remained unchanged.

## Sources actually opened or attempted

| Source | Actual access and scope | Consequence |
|---|---|---|
| CiNii BA06038655, https://ci.nii.ac.jp/ncid/BA06038655 | Complete public catalogue record opened through the web reader | Identifies the French second edition, Sociedade de Matemática de S. Paulo, 1958, 446 pages, and ten library holdings. It supplies no original course scan or preface. This is catalogue metadata only. |
| Google Books, https://books.google.com/books/about/Topological_vector_spaces.html?hl=en&id=nhOoAAAAIAAJ | Public 1973 English-edition record opened | Identifies Gordon and Breach, translation by Orlando Chaljub, 245 pages, ISBN0677300204/9780677300207. The record displays partial contents labels, including Foreword, and says no ebook is available. No image or full text of the original foreword or contents was exposed. This differs from geometry's previously opened 1964 French-edition record. |
| Official IME-USP Acervo Histórico Virtual, https://www.ime.usp.br/~acervo/ahv.php | New independently indexed repository route. The web reader reported an inaccessible redirect to users.ime.usp.br. One ordinary public request subsequently returned HTTP403 and was stopped. | The search index advertises a foreign-author collection including Grothendieck. No actual collection link list or course copy was opened. No request to an alternate endpoint was made after the403. |
| John Horváth, review of *Topological vector spaces*, Bulletin of the AMS82(4) (1976), 515–521, DOI10.1090/S0002-9904-1976-14076-1 | A distinct published-review pointer surfaced during the exact foreword search. Its advertised original PDF, https://www.ams.org/journals/bull/1976-82-04/S0002-9904-1976-14076-1/S0002-9904-1976-14076-1.pdf , returned403 on its first opening. This source route was stopped. | No original review pages were read. Search snippets in later literature referring to the preface were not promoted to a primary authorial statement. No claim about an early trace draft is based on them. |

## Bounded search coverage

The actual queries include exact English/French titles; the translator's name; academic-repository and IME-USP restrictions; a publisher-domain query; both 1973 ISBNs; and an exact foreword/contents query. Returned hits consisted of catalogues, modern papers citing the course, unrelated books with similar titles, general biographies, and unverified aggregators. None yielded an independently public original course copy suitable for inspection. No broad claim that such a copy cannot exist is made.

A search result for an unrelated publisher preview was not mistaken for Grothendieck's book merely because its bibliography cited him. Likewise, metadata mentioning a foreword does not constitute an opened foreword. The course's general publication or translation date cannot date the particular cote1 sheets.

## Reproducibility and source flags

- `notes/algebra_history_web160.json`–`166.json`: exact queries, opened URLs, returned results and timestamps. These preserve the unsuccessful new source attempts as well as the actual catalogue openings.
- `code/algebra_course_usp70.py`; `logs/algebra_course_usp70.json`: the one ordinary public IME-USP request, including HTTP403 outcome and11.14-second elapsed time. No HTML source cache was created because the request failed.
- `notes/algebra_course_query_manifest.json`: records the source boundary and links all raw outputs.
- `code/algebra_course_record71.py`; `logs/algebra_course_record71.json`: final bounded-search record and documentary event.
- **Opened:** the CiNii catalogue and Google Books metadata record. **Not opened:** the French course, English course foreword/contents, official repository contents, and Horváth's original review. No bibliography entry was added for an unread original.

The manuscript-date gate is unchanged. This branch reports an access-limited original-copy search, not an absence theorem about the course or another proof attempt.
