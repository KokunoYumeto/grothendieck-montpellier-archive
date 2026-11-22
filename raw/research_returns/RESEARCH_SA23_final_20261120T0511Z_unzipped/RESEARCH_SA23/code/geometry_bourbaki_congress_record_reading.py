from pathlib import Path
import csv,json,datetime,hashlib,time,subprocess
root=Path(__file__).resolve().parents[1]; start=time.monotonic(); now=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=root/'notes/geometry_bourbaki_congress_date_audit.md'
old=p.read_text()
if '## Completed direct visual reading' in old: raise RuntimeError('already recorded')
addition='''
## Completed direct visual reading

Completed on 20 November 2026 after the 04:10 review, by geometry_analysis. The pending snapshot above is retained to distinguish source retrieval from actual reading. Every page in the following ranges was successfully displayed and read individually in small batches: record803 physical1–17 (modern cover plus all sixteen typed main pages), and record804 physical1–7 (modern cover plus all six typed main pages). The earlier truncated batch is not counted. Some line endings at the right edge of the record804 source scan are clipped; the relevant dates, report numbers and assignments cited below are readable. This is not a transcription certification of those clipped letters.

### Exact original-source links

- Record803 catalogue: http://web.archive.org/web/20251101165244/https://archives-bourbaki.ahp-numerique.fr/items/show/803
- Record803 original: http://web.archive.org/web/20240418092948if_/https://archives-bourbaki.ahp-numerique.fr/files/original/1541c01961de82a9b84f852b518a9d71.pdf
- Record804 catalogue: http://web.archive.org/web/20231205050739/http://archives-bourbaki.ahp-numerique.fr/items/show/804
- Record804 original: http://web.archive.org/web/20240418092923if_/https://archives-bourbaki.ahp-numerique.fr/files/original/e4fe41fb1c8334a56b27347b97d559a0.pdf

The PDFs' 2021 creation metadata date digitization, not the original minutes. Each original typed first page separately gives the congress dates reported here.

### Record803: La Tribu39, Sallières les Bains, 24June–7July1956

| Physical / typed page | Directly observed content relevant to the inquiry |
|---|---|
|1 / cover|Modern catalogue cover, PCT004; not an authorial dating inscription.|
|2 /1|Original heading dates the congress24June–7July1956 and lists a portion of spectral report230 among discussed texts.|
|3 /2|Anecdotes and editorial jokes; no target proof or enclosure.|
|4 /3|Anecdotes, a separate square/cube smooth-function joke, and Weil's organizational letter concerning founding members; that letter is not a trace-proof reference.|
|5 /4|Set-theoretic/category and algebra publication plans. Grothendieck is assigned a category/functor results fascicle.|
|6 /5|Algebra, topology and integration plans. Norms and traces here belong to semisimple algebra, not Hilbert operator trace.|
|7 /6|Homology, varieties and commutative algebra plans. Grothendieck's abstract varieties chapter is assigned.|
|8 /7|Under the analytic block, spectral partIa is set aside; partIb is described as written, with reading to finish inOctober1956; Dieudonné or Dixmier is to write partIc. No genus-zero theorem, Weyl attribution, particular proof or enclosure is identified.|
|9 /8|Varieties and principal-bundle programme; no trace draft.|
|10 /9|Further geometry and commutative algebra plans.|
|11 /10|Fractions, filtrations, completion and noetherian algebra.|
|12 /11|Integral extensions, normalization and related commutative algebra.|
|13 /12|Valuations and field-theory supplements.|
|14 /13|Algebra revision and categorical bundle definitions.|
|15 /14|Bundle definitions and administrative decisions; start of assignments.|
|16 /15|Dieudonné assigned spectral partIc, with no deadline; Grothendieck assigned categories/functors and abstract varieties. The next-congress programme includes the end of spectral partIb. Seminar plans concern other subjects.|
|17 /16|Remaining seminar programme, with no trace/genus-zero proof or enclosure identification.|

The main fascicle supplies dated identifier-level evidence for the existence and discussion of spectral partIb/report230. It does not collate the extant IECL report word for word and does not authenticate a date for its individual surviving passages. It supplies no link to cote1 physical79–80 or111–112. The remaining twenty PDF pages of independent appendices were not read; the catalogue explicitly describes those appendices as excluding spectral theory.

### Record804: La Tribu40, Amboise, 7–14October1956

| Physical / typed page | Directly observed content relevant to the inquiry |
|---|---|
|1 / cover|Modern catalogue cover PCT005.|
|2 /1|Original heading gives7–14October1956; contents list the continuation of spectral theory, report230. Norms and traces appear separately as AlgebraVIII section12, report251.|
|3 /2|Anecdotes, quadratic/sesquilinear forms and editorial discussion. Spectral-sequence jokes do not concern operator spectra.|
|4 /3|General editorial decisions, tensor products, module rank and algebra errata.|
|5 /4|Bundles, commutative algebra and assignments. Dieudonné is assigned spectral partIc.|
|6 /5|Remaining assignments: Grothendieck's abstract varieties chapter is dueFebruary1957; no Hilbert-trace proof assignment. Future-congress programme does not identify the target manuscript.|
|7 /6|Bourbaki seminar programme forDecember1956 andFebruary1957; no target trace/genus-zero proof or enclosure.|

All six typed main pages were inspected. No explicit Weyl/genus-zero/three-sector-proof discussion or identification of the Montpellier leaves was found in this range. The remaining sixteen appendix pages were not inspected; the catalogue expressly excludes a detailed spectral-theory appendix. Source clipping at some right margins is retained as a reading limitation, not repaired by conjecture.

## Result, failure and next step

Neither bounded main-minute reading supplies a dated identification of the particular proof sheets. Report circulation and Grothendieck's presence at the meetings do not provide that missing connection. The exact remaining gate is a dated document identifying the leaves or their distinctive argument, or an authenticated original inscription on the leaves. No general career-period inference is substituted. No formal mathematical movement or independent proof is claimed.

A potentially discriminating future source would be a specific letter or enclosure referenced by the spectral report's authors, rather than another generic dated congress list. No such enclosure is identified in these main minutes. The uninspected appendices and other correspondence remain outside this bounded conclusion.

## Preserved execution and reading records

- Metadata retrieval: `code/geometry_bourbaki_congress_records.py`, `logs/geometry_bourbaki_congress_records.json`, elapsed11.345892919009202seconds.
- Advertised wrapper/payload retrieval: `code/geometry_bourbaki_congress_pdfs.py`, `logs/geometry_bourbaki_congress_pdfs.json`, elapsed195.91935951801133seconds. The long transfer ran asynchronously; metadata and request-level timings are retained.
- Rendering: `code/geometry_bourbaki_congress_render.py`, logs `geometry_bourbaki_congress_render_803_1_17.json` (51.888459184003295seconds) and `geometry_bourbaki_congress_render_804_1_7.json` (10.903122047995566seconds).
- Images: `sources/geometry_bourbaki_congress_803_pages/page-01.png` through`page-17.png`, and analogous804pages01–07; every listed image was directly read.
- Native extraction attempts yielded only page separators and were not used as proof of content.
- This authored reading record: `code/geometry_bourbaki_congress_record_reading.py` and `logs/geometry_bourbaki_congress_reading.json`.
'''
p.write_text(old+addition)
tsv=root/'notes/manuscript_date_attempts.tsv'; before=tsv.read_bytes();rows=list(csv.DictReader(before.decode().splitlines(),delimiter='\t'))
for r in rows:
 if r['route'].startswith('Bourbaki congress minutes 803'):
  r.update(route='Bourbaki congress minutes 803 and804',evidence='Original covers and all16/6typed main pages directly read. Original headings date24June–7July1956 and7–14October1956; R230/partIb circulation and further partIc assignments are explicit.',failed_step='No target proof, Weyl/genus-zero discussion or manuscript enclosure identified in the main minutes.20/16appendix pages unread; some804right-edge text is clipped in the source.',next_step='A specific dated letter, enclosure or original inscription must connect the report or distinctive argument to the Montpellier leaves.',record='notes/geometry_bourbaki_congress_date_audit.md')
with tsv.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['route','evidence','failed_step','next_step','record'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
bib=root/'notes/geometry_docroute_references.bib'
if 'geoBourbakiTribu39' in bib.read_text(): raise RuntimeError('duplicate bibliography')
with bib.open('a') as f:
 f.write(r'''
@misc{geoBourbakiTribu39,
 author = {{Bourbaki}},
 title = {La Tribu no. 39: Compte rendu du congr{\`e}s des Tapis},
 year = {1956},
 howpublished = {Fonds Pierre Cartier, PCT 004},
 url = {http://web.archive.org/web/20240418092948if_/https://archives-bourbaki.ahp-numerique.fr/files/original/1541c01961de82a9b84f852b518a9d71.pdf},
 note = {Opened: actual archived original; modern cover and all sixteen typed main pages visually read. Original heading dates the congress 24 June--7 July 1956. Typed pp. 1,7,15 identify spectral report 230, part Ib and part Ic assignments. Remaining twenty appendix pages unread. No Montpellier trace-sheet identification found in the inspected main minutes.}
}
@misc{geoBourbakiTribu40,
 author = {{Bourbaki}},
 title = {La Tribu no. 40: Compte rendu du congr{\`e}s de l'intelligence peu commune},
 year = {1956},
 howpublished = {Fonds Pierre Cartier, PCT 005},
 url = {http://web.archive.org/web/20240418092923if_/https://archives-bourbaki.ahp-numerique.fr/files/original/e4fe41fb1c8334a56b27347b97d559a0.pdf},
 note = {Opened: actual archived original; modern cover and all six typed main pages visually read, with some clipped right-edge line endings in the source. Original heading dates the congress 7--14 October 1956. Typed pp. 1,4 identify continued spectral report 230 and part Ic assignment. Remaining sixteen appendix pages unread. No Montpellier trace-sheet identification found in the inspected main minutes.}
}
''')
outcome='Directly inspected congress803 cover+all16typed main pages and804 cover+all6typed main pages. Dated originals identify R230/partIb circulation and partIc assignments but no target trace/genus-zero proof or enclosure.20/16appendix pages unread;804source-edge clipping retained. Exact source/page audit: geometry_bourbaki_congress_date_audit.md. Documentary check only; date gate unchanged.'
with (root/'notes/geometry_CHECK_EVENTS.tsv').open('a') as f:
 for sid in ['geo-H-history','SA23-49']:
  f.write('\t'.join([sid,'2026-11-20','GPT-6 Astra Pro, inherited effort, geometry_analysis','used and rechecked in this run',outcome])+'\n')
record={'utc':now,'who':'geometry_analysis','reading_scope':{'803':{'physical_pages':list(range(1,18)),'original_typed_pages':list(range(1,17)),'unread_appendix_pages':20},'804':{'physical_pages':list(range(1,8)),'original_typed_pages':list(range(1,7)),'unread_appendix_pages':16,'source_limitation':'some right-edge line endings clipped'}},'date_gate':'unchanged','formal_movement':False,'route_rows':len(rows),'route_before_sha256':hashlib.sha256(before).hexdigest(),'route_after_sha256':hashlib.sha256(tsv.read_bytes()).hexdigest(),'note_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start}
(root/'logs/geometry_bourbaki_congress_reading.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
