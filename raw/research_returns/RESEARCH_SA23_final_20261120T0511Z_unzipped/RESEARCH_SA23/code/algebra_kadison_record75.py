from pathlib import Path
import json, datetime, hashlib, time

ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
note='''# Richard Kadison: public records and original early communications

Checked 20 November 2026 UTC, approximately 04:46–04:52. Existing statement: `geo-H-history`.

## Result and exact limit

**No opened source identifies or dates the cote 1 Hilbert trace/genus-zero proof.** Three genuine public finding-aid entries were located, but no original Kadison correspondence file or item-level description of a Grothendieck proof/enclosure was obtained. The bounded original-publication follow-up found no such identification in the passages checked. This does not establish that no relevant letter survives in the unexamined archive files.

The previously read 24 January 1955 Dixmier letter and its determinant inequality were checked only in the local audit to prevent duplication; they were not reread or counted as new evidence. Root owns the separate Schatten route, which was not pursued here.

## Public primary archival metadata actually opened

| Repository and collection | Exact public entry | Opened scope and limit |
|---|---|---|
| University of Pennsylvania, University Relations, News and Public Affairs Records, UPF8.5 | **Kadison, Richard V., 1963–1982; box 72, folder 8** | Collection overview/scope and exact entry read. The biographical files may contain CVs, releases, clippings, photographs and correspondence; this is not a catalogue of Kadison's personal mathematical papers. No underlying folder opened. |
| IAS, School of Mathematics records, SM | **Kadison, Richard Vincent, 1949–1956; box 14, folder 5**, Members, Visitors, Assistants series | Official web finding aid, overview, access conditions and exact entry read. No item-level mathematical description or digitized letter attached to this entry. |
| IAS, Director's Office: Member Files, DO.MEMBERS | **Kadison, Richard V. –M– 1950–51, 1951–52; box 70** | Official web finding aid, overview/scope, access conditions and exact entry read. General scope is applications, references, invitations and administrative correspondence, sometimes later correspondence. No underlying file opened. |

Actual URLs:

- https://archives.upenn.edu/collections/finding-aid/upf8_5/
- https://www.ias.edu/sites/default/files/library/page/SM.html
- https://www.ias.edu/sites/default/files/library/page/DO.MEMBERS.html

IAS access notes state a 30-year administrative closure and a separate recommendation-letter restriction. No private file was requested and no contact or account was used. The indexed SM and DO.MEMBERS URLs were new working public finding-aid locators, distinct from stale links in the earlier von Neumann/IAS route. Both opened successfully in the web reader; a later ordinary local preservation request returned **403** for each and was stopped without a retry or alternate endpoint. Their opened text is preserved in raw web records 173–174. Penn's public HTML downloaded successfully and is saved with its hash.

Exact-name and public IAS digital-repository searches found no original Kadison–Grothendieck letter. A historical address-directory result was not opened because it is not correspondence. Wrong-person Kadison-Buloff/YIVO and psychiatry hits were not followed. No claim is made to have read the thousands of unrelated finding-aid entries or all Kadison publications.

## Original publications opened through a university-hosted collection

The public collection index at https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison.html was opened. It links original scanned pages and separately labels a modern TeX version of the 1955 report. **The original scans were used; the modern TeX version was not opened.** Kadison's Penn publications page, https://www2.math.upenn.edu/~kadison/Papers.html, returned **403** on its first opening and was not retried.

### Fuglede–Kadison 1952

Bent Fuglede and Richard V. Kadison, *Determinant theory in finite factors*, **Annals of Mathematics (2) 55(3), May 1952, 520–530**. The original p.520 records **received 17 May 1951** and says its results were outlined in the authors' earlier note [4].

- Original: https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison/1950s/1952_DeterminantTheoryInFiniteFactors.pdf
- **Original pages visually read: 520, 525, 530** (physical PDF 1,6,11): introduction, Theorem 2/proof, closing discussion and complete bibliography. All 11 pages' extracted text was searched for Groth/letter/communication/acknowledgment/genus/Fredholm; those target terms produced no hits.
- Theorem 2 on p.525 concerns the **normalized trace in a finite factor**, places it in the spectral convex hull, and deduces zero trace for a generalized nilpotent. Its proof uses the determinant of an exponential. This is not the supplied manuscript's Hilbert trace-class Fredholm genus-zero argument, and no supplied Grothendieck proof is identified in the checked original passages.
- Local PDF: `sources/algebra_kadison_fuglede1952.pdf`; **838,415 bytes; SHA256 403af865f539289bdf34a0d5294195d77c7ee6580f0940b5991f7125243b108e**.

### Fuglede–Kadison 1951

Bent Fuglede and Richard V. Kadison, *On determinants and a property of the trace in finite factors*, **PNAS 37 (1951), 425–431**. The original p.425 records **communicated by M. H. Stone, 16 May 1951**.

- Original: https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison/1950s/1951_on_determinants_and_a_property_of_the_trace_in_finite_factors.pdf
- **Original pages visually read: 425, 430, 431** (physical1,6,7), including title/date and all final source notes. The complete seven-page extracted text was read/searched; original pages426–429 were not separately visually certified.
- This is the finite-factor determinant announcement cited in the 1952 paper. No Grothendieck proof, letter or enclosure is identified in the checked text. The opening portion of p.425 belongs to the preceding paper, and the lower portion of p.431 begins Mautner's next paper. **The 17 May 1951/Weyl communication line on p.431 belongs to Mautner, not Fuglede–Kadison.**
- Local PDF: `sources/algebra_kadison_fuglede1951.pdf`; **658,943 bytes; SHA256 731af957a5f9146fb4376c4e1dd1bb73160b156a550d456aa85c37e009315738**.

### Kadison 1955 report

Richard V. Kadison, *Report on operator algebras*, in *Report of an International Conference on Operator Theory and Group Representations, Arden House, Harriman, N.Y., 1955*, National Academy of Sciences–National Research Council Publication387, **pp.4–10**. The volume identification/year comes from the opened collection index; the retrieved seven-page excerpt contains the original article title, pagination and Columbia affiliation, but **not the volume title/imprint pages**.

- Original: https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison/1950s/1955_report_on_operator_algebras.pdf
- **Every original article page4,5,6,7,8,9,10 individually displayed/read.** The PDF has no useful text layer; empty keyword results in the retrieval log are therefore not evidence of absence. The conclusion rests on these seven visual readings.
- P.4 explains the limited conference-report scope and intentional omission of bibliographical references. P.7 discusses traces associated with finite factors; p.9 discusses Dixmier's centre-valued trace and Segal's integration theory. There is **no Grothendieck trace/genus-zero proof, dated supplied communication, or manuscript identification** in the seven pages. Nothing is inferred about informal conference discussions the report explicitly does not attempt to record.
- Local PDF: `sources/algebra_kadison_report1955.pdf`; **3,743,736 bytes; SHA256 ae1deabf21d3b8bded2a81923f04508a3c57c7f840b2034bb0bd7a7997994552**.

## Reproducibility and disposition

- `notes/algebra_history_web170.json`–`177.json`: actual queries, catalogue opens/finds, original links and results. The per-call approximate clock label for177 was corrected in the recording script; its exact execution second was not captured.
- `notes/algebra_kadison_query_manifest.json`: query inventory and access/reading scope.
- `code/algebra_kadison_fetch74.py`; `logs/algebra_kadison_fetch74.json`: every local request, HTTP result, hash, extraction and render. Retrieval/rendering took17.787seconds. The two IAS403 responses and Penn-publications403 are terminal for those local routes.
- `code/algebra_kadison_record75.py`; `logs/algebra_kadison_record75.json`: actual visual-reading inventory, record completion and allowed documentary event.

**Opened:** the three primary finding aids at the scope above, the collection index, and the original publication scans at the exact page scopes above. **Not opened:** underlying archive files, an original Kadison–Grothendieck letter, unrelated publications, the modern report transcription, or denied endpoints after their refusal. Paper and bibliography are unchanged. The particular-sheet date gate remains open.
'''
(ROOT/'notes'/'algebra_kadison_source_search.md').write_text(note)
queries=[]
for n in range(170,178):
 p=ROOT/'notes'/f'algebra_history_web{n}.json'
 x=json.loads(p.read_text())
 if n==177:
  x['retrieved_at']='2026-11-20, before 04:49:28 UTC; exact call completion second not captured'
  x['clock_label_correction']='The former 04:51Z label was an unmeasured approximate label and is replaced by the actual bounded completion time; raw query/result unchanged.'
  p.write_text(json.dumps(x,ensure_ascii=False,indent=2))
 queries.append({'raw_record':str(p.relative_to(ROOT)),'query':x.get('query')})
manifest={'recorded_utc':now,'statement':'geo-H-history','queries':queries,'finding_aids':'Primary public metadata read; underlying archive files not opened. IAS web-reader successful; later ordinary local requests403 stopped.','original_visual_pages':{'Fuglede_Kadison_1952':[520,525,530],'Fuglede_Kadison_1951':[425,430,431],'Kadison_report_1955':[4,5,6,7,8,9,10]},'text_scope':'1952 full extracted-text keyword search;1951 complete extracted text read/searched;1955 no useful text layer, all original images read.','result':'No dated supplied Grothendieck proof or identification of cote1 sheets found in opened scope. No inference about unseen archival files.','paper_bibliography_changed':False}
(ROOT/'notes'/'algebra_kadison_query_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
event='geo-H-history\t2026-11-20\tGPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters\tused and rechecked in this run\tKadison branch: primary Penn UPF8.5 and two IAS finding-aid entries read, metadata only; no underlying letters. Original1951 pages425/430/431 and1952 pages520/525/530 visually checked, complete extracted text searched; all seven original1955 report pages4-10 read. Finite-factor traces and conference scope distinguished from Hilbert Fredholm genus-zero proof. No dated manuscript identification. IAS local403 and Penn-publications403 stopped.\tnotes/algebra_kadison_source_search.md;notes/algebra_kadison_query_manifest.json;logs/algebra_kadison_fetch74.json;logs/algebra_kadison_record75.json\n'
ep=ROOT/'notes'/'algebra_history_CHECK_EVENTS.tsv'
if 'Kadison branch: primary Penn UPF8.5' not in ep.read_text():
 with ep.open('a') as f:f.write(event)
record={'utc':now,'elapsed_seconds':round(time.monotonic()-start,3),'result':'documentary branch complete; exact manuscript-date gate unchanged','actual_visual_pages':manifest['original_visual_pages'],'note_sha256':hashlib.sha256(note.encode()).hexdigest(),'paper_bibliography_changed':False,'clock_metadata_correction':'raw177 approximate label replaced by known execution bound; raw search data unchanged'}
(ROOT/'logs'/'algebra_kadison_record75.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2))
