from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib,re
import fitz
root=Path(__file__).resolve().parents[1]
started=time.monotonic()
full=root/'sources/algebra_dieudonne_icm1966_volume.pdf'
doc=fitz.open(full)
extract=fitz.open()
extract.insert_pdf(doc,from_page=0,to_page=1)
extract.insert_pdf(doc,from_page=20,to_page=23)
small=root/'sources/algebra_dieudonne_icm1966_excerpt.pdf'
extract.save(small)
text='\n\f\n'.join(doc[i].get_text() for i in range(20,24))
(root/'sources/algebra_dieudonne_icm1966_article.txt').write_text(text)
note=r'''# Jean Dieudonné's 1966 Fields presentation: original-source audit

Checked on 20 November 2026 UTC, approximately 04:42–04:46. Existing statement: `geo-H-history`. This is a documentary reading of a first-person witness, not a new mathematical proof.

## Result

**No dated identification of the cote 1 Hilbert trace/genus-zero proof occurs in the original presentation.** All four original article pages were individually displayed and read. The exact functional-analysis passage is **p.24, second paragraph**. Dieudonné says that he has left the earlier topological-vector-space memoirs outside his discussion, refers broadly to the years **1950–55**, mentions nuclear spaces and distributions, and recalls personally observing Grothendieck's work during that period. It gives no trace/genus-zero assertion, distinctive proof, supplied letter, enclosure, or manuscript identification.

The final paragraph's comparison with **Hilbert** concerns mathematical style and generalization. It is not a claim about operators on Hilbert space. Neither that comparison nor the broad 1950–55 period dates the particular manuscript sheets.

## Exact original and reading scope

Jean Dieudonné, **Les travaux de Alexander Grothendieck**, in *Travaux du Congrès international des mathématiciens (Moscou, 1966)* / *Proceedings of International Congress of Mathematicians (Moscow, 1966)*, edited by I. G. Petrovsky, Moscow: Mir, **1968**, pp.**21–24**.

- Official original facsimile actually retrieved: https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1966.1/ICM1966.1.ocr.pdf
- Local full volume: `sources/algebra_dieudonne_icm1966_volume.pdf`.
- **73,319,440 bytes; SHA256 8f62ea3661d4cfbfccf8247432d9ca5928b8e23b6090066ef4d8c07b09613681; 728 physical PDF pages.**
- Actual original article reading: **physical/printed pages 21,22,23,24**, individually displayed through `sources/algebra_dieudonne_icm1966_page021.png`–`024.png`.
- Original title page, physical1, was displayed/read and confirms the1966 congress and Mir/Moscow1968 imprint. Physical2 was displayed/read and identifies editor I. G. Petrovsky. Physical3, a section divider, was also displayed; it adds no documentary dating information.
- The article's title and pagination are also located by the volume's extracted contents on physical723; that contents page was not visually certified. No claim is made to have visually read the rest of the728-page volume.
- A convenience excerpt preserving the original page images, title/imprint pages plus the four article pages, is `sources/algebra_dieudonne_icm1966_excerpt.pdf`. Its provenance and hash are recorded in `logs/algebra_dieudonne_record73.json`.
- Searchable article extraction: `sources/algebra_dieudonne_icm1966_article.txt`. Text search supplements, rather than substitutes for, the four original-page readings.

## Duplication check and other versions

Before retrieval, exact local-note searches for Dieudonné/Fields/ICM1966 and the presentation title found no previous audit of this text. The separate1989 *A. Grothendieck's early work (1950–1960)* was then found in `notes/category_correspondence_date_audit.md`, which records an earlier original reading of its functional-analysis pages299–300. That passage was **not read again or counted as a new source check**. Serre's1965 report and unrelated biography passages were not reread.

The opened CSG catalogue https://csg.igrothendieck.org/articles-and-books/ identifies the1966 talk and1968 proceedings. A search also surfaced a modern transcription at `https://iut-theory.org/divers/travauxdieud.pdf`, whose indexed opening explicitly attributes transcription to Mateo Carmona. That transcription was **not opened or used in place of the original**.

## Retrieval and records

- `notes/algebra_history_web167.json`: exact first-person witness search and official IMU locator.
- `notes/algebra_history_web168.json`: official-volume web opening rejected solely because its73,319,440-byte content exceeds the reader's size limit; successful CSG catalogue opening.
- `notes/algebra_history_web169.json`: exact catalogue location and the distinct1989 pointer, checked against the existing local audit before any further retrieval.
- `code/algebra_dieudonne_icm72.py`; `logs/algebra_dieudonne_icm72.json`: ordinary public official-volume request returnedHTTP200; full original saved, hashes, title matches, text extraction and targeted renders recorded. The web-reader size limit was not an access-control refusal. Total retrieval/extraction/render runtime:22.07seconds.
- `code/algebra_dieudonne_record73.py`; `logs/algebra_dieudonne_record73.json`: precise reading record, convenience excerpt, bounded keyword inventory and documentary event.
- `notes/algebra_dieudonne_query_manifest.json`: full operation/source boundary.

**Opened:** official original proceedings article and title/imprint pages, and the catalogue entry. **Not newly opened:** Dieudonné1989, Serre1965, or the modern1966 transcription. No outside contact, account, or restricted retrieval was used. No paper or bibliography entry was changed, because the exact manuscript-date conclusion is unchanged.
'''
(root/'notes/algebra_dieudonne1966_source_audit.md').write_text(note)
manifest={'utc_recorded':datetime.now(timezone.utc).isoformat(),'raw_web':[f'notes/algebra_history_web{n}.json' for n in range(167,170)],'prior_audit_check':{'1966_exact_title_or_Fields_ICM_local_md_tex_search':'no matches','1989_early_work_search':'matched category_correspondence_date_audit.md pp299–300; not reread'},'original_visual_pages':[1,2,3,21,22,23,24],'article_printed_pages':'21–24','functional_analysis_locator':'p.24 second paragraph','unread_volume_pages':'All pages other than specified visual scope; native extraction is not a visual reading certificate.','result':'General1950–55 recollection only, no specific trace/genus-zero proof or manuscript identification.'}
(root/'notes/algebra_dieudonne_query_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
row=['geo-H-history','2026-11-20','GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters','used and rechecked in this run','Individually displayed/read all original Dieudonne1966 ICM article pages21-24 plus title/imprint. Functional-analysis paragraph p24 gives only general1950-55 recollection and nuclear-space/distribution scope; no trace/genus-zero proof, supplied letter, enclosure or cote1 identification. Final Hilbert comparison is stylistic. Already-read1989 passage and Serre1965 report not repeated.','notes/algebra_dieudonne1966_source_audit.md;notes/algebra_dieudonne_query_manifest.json;logs/algebra_dieudonne_icm72.json;logs/algebra_dieudonne_record73.json']
with (root/'notes/algebra_history_CHECK_EVENTS.tsv').open('a') as f:f.write('\t'.join(row)+'\n')
out={'utc_recorded':datetime.now(timezone.utc).isoformat(),'excerpt_file':str(small.relative_to(root)),'excerpt_bytes':small.stat().st_size,'excerpt_sha256':hashlib.sha256(small.read_bytes()).hexdigest(),'visual_article_pages':[21,22,23,24],'visual_frontmatter_pages':[1,2,3],'article_keyword_occurrences':{s:len(re.findall(s,text,re.I)) for s in ['trace','genre','Fredholm','Lidsk','Hilbert','nucl','lettre','manuscrit']},'documentary_events_appended':1,'paper_or_bib_changed':False,'elapsed_seconds':time.monotonic()-started}
(root/'logs/algebra_dieudonne_record73.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
