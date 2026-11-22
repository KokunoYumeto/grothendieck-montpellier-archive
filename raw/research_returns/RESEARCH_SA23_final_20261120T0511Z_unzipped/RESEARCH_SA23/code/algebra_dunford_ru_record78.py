"""Record the bounded Russian Dunford--Schwartz source audit; no paper/bib edits."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re
import time

start = time.monotonic()
base = Path(__file__).resolve().parents[1]
now = dt.datetime.now(dt.timezone.utc).isoformat()

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

source = base / "sources/algebra_dunford_ru1966.djvu"
textfile = base / "sources/algebra_dunford_ru1966.txt"
text = textfile.read_text()
terms = ["Гротенд", "Grothendieck", "Лидск", "Lidsk", "Фредгольм", "письм", "рукопис", "неопублик", "личн.*сообщ", "нулев.*род", "род.*нул"]
finding_hits = {}
segments = text.split("\f")
for term in terms:
    pat = re.compile(term, re.IGNORECASE)
    hits = []
    for n, segment in enumerate(segments, 1):
        matches = list(pat.finditer(segment))
        if matches:
            hits.append({"native_text_segment_ordinal_not_physical_page": n,
                         "contexts": [segment[max(0,m.start()-100):m.end()+220].replace("\n", " ") for m in matches]})
    finding_hits[term] = hits

visual = [1,2,3,5,6,7,8,328,329,330,753,755,970,971,993,994,1045,1047,1061,1062,1064]
manifest = {
    "recorded_utc": now,
    "task": "geo-H-history / Lead6 particular-sheet dating, bounded original Russian translation reading",
    "opened_index": "https://eqworld.ipmnet.ru/ru/library/mathematics/operators.htm",
    "index_web_ref": "turn748259498view0",
    "advertised_link_number": 16,
    "source_url": "https://eqworld.ipmnet.ru/ru/library/books/DanfordShvarc_t2_1966ru.djvu",
    "web_open_result": "400 unsupported image/vnd.djvu content type; not an access refusal",
    "ordinary_public_download_result": "HTTP 200; no account, access override or challenge bypass",
    "source": str(source.relative_to(base)),
    "bytes": source.stat().st_size,
    "sha256": sha(source),
    "physical_pages": 1064,
    "edition": "Russian translation, Mir, Moscow, 1966; the volume reproduces the English 1963 title page",
    "english_original_body_opened": False,
    "visual_physical_pages_read": visual,
    "rendered_but_not_visually_read": [4],
    "main_body_page_numbering": "Physical pages and printed numbers agree at the checked body, bibliography and index pages.",
    "native_text_warning": "Whole-file djvutxt skips the initial cover segment. Search ordinals are not physical pages. Selected page text was regenerated using explicit -page=n by script77; original printed labels checked visually.",
    "native_text_finding_aid": str(textfile.relative_to(base)),
    "native_text_sha256": sha(textfile),
    "native_text_searches": finding_hits,
    "visual_image_hashes": {str(n):sha(base / f"notes/algebra_dunford_ru1966_pages/page_{n:03d}.png") for n in visual},
    "raw_web_records": [f"notes/algebra_history_web{n}.json" for n in (180,183)],
    "retrieval_and_render_logs": ["logs/algebra_dunford_ru_fetch76.json", "logs/algebra_dunford_ru_render77.json"],
    "outcome": "No inspected passage identifies a dated received Grothendieck proof, letter, enclosure or the particular cote1 sheets; gate unchanged.",
    "limit": "Selected original page reading plus whole native-text searches, not visual reading of all 1064 pages; no assertion about the unopened English body."
}
(base / "notes/algebra_dunford_ru1966_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")

note = """# Dunford--Schwartz II: bounded audit of the original Russian translation

Recorded in the current run on 20 November 2026. Retrieval began 04:53:54 UTC; the selected original images were individually displayed and read by 04:58:20 UTC. The exact machine timestamps and hashes are in the accompanying logs/manifest.

## Result and scope

The inspected 1966 Russian edition supplies **no dated identification of a Grothendieck Hilbert trace/genus-zero proof, letter, enclosure, or the particular cote 1 sheets**. Its Fredholm historical subsection and the Grothendieck/Lidskii bibliography entries give ordinary publication references. The particular-sheet date gate is unchanged.

This is a successful new original-edition reading, unlike the earlier unsuccessful English-copy search. It is **not** a reading of the English 1963 body. The Russian editor expressly says that some inaccuracies were corrected and historical notes were added (printed p. 6). Therefore no statement here is silently transferred to the English edition.

## Provenance and access

The actual opened EqWorld operator-theory library page, https://eqworld.ipmnet.ru/ru/library/mathematics/operators.htm (web reference `turn748259498view0`), advertises the file as link 16:

https://eqworld.ipmnet.ru/ru/library/books/DanfordShvarc_t2_1966ru.djvu

The web reader returned an unsupported DjVu content-type error (400), not an access denial. An ordinary direct request to that advertised public link returned HTTP 200. No denied host was retried, and no account or access override was used. The downloaded original scan is `sources/algebra_dunford_ru1966.djvu`, 18,240,028 bytes, SHA256 `176dbdf4d51440456a1b8c7048d7db3a68b0a518a5b50b37d72533872ea52229`.

Physical p. 2 reproduces the English title page for *Linear Operators, Part II: Spectral Theory. Self Adjoint Operators in Hilbert Space*, Nelson Dunford and Jacob T. Schwartz, with assistance from W. G. Bade and R. G. Bartle, Interscience, 1963. Physical p. 3 is the Russian title/imprint: Mir, Moscow, 1966; translation by M. G. Gasymov, V. Ya. Lin and B. S. Mityagin, edited by A. G. Kostyuchenko. These are title-page facts within the Russian volume, not evidence of inspecting the separate English edition. The colophon (physical p. 1064) records submission to production on 22 February 1966 and authorization for printing on 30 August 1966. Those dates concern this edition only.

## Exact original-page reading

Every page in this table was individually displayed as an original image, not inferred from OCR. Body, bibliography, index and contents page numbers agree with the physical image numbers at the checked locations.

| Original pages | Scope actually read and result |
|---|---|
| Physical 1--3 | Cover and English/Russian title pages; edition identification above. |
| Printed 5--6 | Entire Russian editor's preface. General chapter survey, including Hilbert--Schmidt/Carleman material and a new Gohberg--Krein book; p. 6 says historical notes were added. No dated supplied Grothendieck proof or manuscript. |
| Printed 7--8 | Entire translated authors' preface, ending July 1963. Acknowledgments concern corrections, preparation and support; no Grothendieck trace manuscript identification. |
| Printed 328--330 | Chapter XI, section 11, notes and addenda; the complete subsection on Fredholm theory and eigenvalue localization, ending before the subsection on singular integrals. Carleman, Hille--Tamarkin and Smithies are cited for Hilbert--Schmidt theory; eigenvalue estimates and Schatten/von Neumann classes lead to Krein, Gohberg--Krein and Brodskii--Livshits on completeness, dissipative operators and subdiagonalization. No dated Grothendieck communication, manuscript, or distinctive supplied genus-zero proof is identified. |
| Printed 753, 755 | Both name-index body hits for Lidskii, in Chapter XIII's notes on ordinary differential operators. Lidskii [1] is included among differential-equation spectral references, with no trace manuscript or correspondence statement. |
| Printed 970--971 | Complete Grothendieck bibliography entry (items 1--7). It lists publications, including Memoir 16 and the Fredholm paper, with no manuscript/letter description. The actual scan prints the French Fredholm reference as volume 84 (1958), pp. 319--384, and the Russian translation as 2:5 (1958), pp. 51--103. These literal bibliographic data are retained here without silently correcting them; the already-opened French original establishes 1956 elsewhere in the project. This edition's date typo cannot date cote 1. |
| Printed 993--994 | Complete Lidskii bibliography entry, two items: the 1954 differential-equation solutions note and the 1958 completeness-of-root-subspaces paper. No received Grothendieck proof is mentioned. This entry is not the already-read 1959 trace note. |
| Printed 1045, 1047 | Name index: Grothendieck points only to the bibliography beginning at 970; Lidskii points to 753, 755, 993. All those target entries were checked as above. Index coverage is not an exhaustive absence proof. |
| Printed 1061--1062 | Contents locating Hilbert--Schmidt operators (XI.6, p. 168), compact-operator classes and generalized Carleman inequalities (XI.9, p. 251), subdiagonalization (XI.10, p. 281), notes (XI.11, p. 309), bibliography and name index. |
| Physical 1064 | Colophon and printing dates, as above. |

Physical p. 4 was rendered and its native text extracted, but was not visually read. The rest of the book was not read page by page. Full native-text searches were used solely as finding aids; exact patterns, contexts and original image hashes are in `notes/algebra_dunford_ru1966_manifest.json`. No claim of exhaustive visual reading is made.

## Reproducibility and page-index correction

`code/algebra_dunford_ru_fetch76.py` downloaded the file, extracted native text and rendered front matter. `code/algebra_dunford_ru_render77.py` verified 1064 physical pages and rendered the selected targets. All render/extract return codes in the saved logs are zero.

Whole-file `djvutxt` skips the initial cover text segment. Consequently the initial search-hit ordinals in fetch76 are **text-segment ordinals, not physical page numbers**. The original images were always correctly selected with explicit `ddjvu -page=n`. Script77 regenerated every selected page's text with explicit `djvutxt -page=n`; its log records this correction. This audit uses visually verified printed page numbers. The full-text manifest also labels search ordinals explicitly and does not convert them by an assumed global offset.

Records: `notes/algebra_history_web180.json`, `notes/algebra_history_web183.json`; `logs/algebra_dunford_ru_fetch76.json`, `logs/algebra_dunford_ru_render77.json`, `logs/algebra_dunford_ru_record78.json`; images and corrected per-page text in `notes/algebra_dunford_ru1966_pages/`.

No paper section or bibliography entry was changed for this bounded negative source result.
"""
(base / "notes/algebra_dunford_ru1966_source_audit.md").write_text(note)

followup = """# Bounded Gohberg--Krein / Lidskii follow-up search, 20 November 2026

This was a search for a new original historical/acknowledgment passage explicitly dating receipt of Grothendieck's Hilbert trace or genus-zero proof. Before searching, the existing `notes/geometry_Pietsch_Gohberg_documentary_route.md` and `notes/root_russian_translation_date_audit.md` were checked. The already-read original Gohberg--Krein 1965 passages, Pietsch 2007 passages and entire Lidskii 1959 note were not recounted as new reading. Previously denied Russian-translation and AMS routes were not retried.

Exact query payloads, retrieval timestamps and raw results are preserved in `notes/algebra_history_web178.json` through `notes/algebra_history_web182.json` (04:52:27--04:53:20 UTC). Variants included Russian Lidskii/Grothendieck memoirs/letters/proof terms; Gohberg/Krein/Grothendieck historical and correspondence terms; Lidskii's 1962 summability paper; and Volterra-operator references. Search results did not yield a new opened original early Gohberg--Krein or Lidskii communication. Metadata and snippets are not treated as reading those works.

Two distinct concrete pointers arose:

1. The official EqWorld operator library advertised the original 1966 Russian Dunford--Schwartz II scan. Root assigned that independent copy to this agent. It was successfully downloaded and read to the bounded scope documented in `notes/algebra_dunford_ru1966_source_audit.md` and its manifest. The English original body remains unopened.
2. A public institutional NBUV result identified O. V. Bulgakov's 2013 custodial survey of Krein correspondence, pp. 651--659 (search reference `turn343520075search7`), at the following actual advertised locator:

https://irbis-nbuv.gov.ua/cgi-bin/irbis_nbuv/cgiirbis_64.exe?C21COM=2&I21DBN=UJRN&IMAGE_FILE_DOWNLOAD=1&Image_file_name=PDF%2Fnpnbuimviv_2013_37_58.pdf&P21DBN=UJRN

This agent passed that pointer to root **without opening the underlying PDF**. Root explicitly took ownership of its reading and records any result separately. The related 2012 article, *Особисте листування М. Крейна: загальний огляд та інформативний потенціал*, *Архіви України* 6, pp. 100--106, was surfaced only as metadata. Neither is represented here as an original read by algebra_letters.

The search-only stage itself supplies no date witness. Its result is a bounded access/search record, not proof that no relevant correspondence exists. No mathematical section or bibliography file was changed.
"""
(base / "notes/algebra_gohberg_lidskii_followup_search.md").write_text(followup)

querymanifest = {"recorded_utc":now,"scope":"Bounded new Gohberg--Krein/Lidskii documentary search; no new original communication opened in this stage", "raw_records":[]}
for n in range(178,183):
    p=base/f"notes/algebra_history_web{n}.json"
    d=json.loads(p.read_text())
    querymanifest["raw_records"].append({"path":str(p.relative_to(base)),"sha256":sha(p),"retrieved_at":d.get("retrieved_at"),"query":d.get("query")})
querymanifest["krein_custodial_pdf_opened_by_this_agent"]=False
querymanifest["handoff_owner"]="/root"
(base / "notes/algebra_gohberg_lidskii_followup_manifest.json").write_text(json.dumps(querymanifest,ensure_ascii=False,indent=2)+"\n")

events = base / "notes/algebra_history_CHECK_EVENTS.tsv"
rows = [
    ["geo-H-history","2026-11-20","GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters","used and rechecked in this run","Distinct Gohberg-Krein/Lidskii follow-up queries checked against existing audits; no new original early communication opened. EqWorld independent translation pointer followed separately; NBUV Krein custodial survey pointer passed unopened to root. Previously denied endpoints not retried; no manuscript date witness from search results.","notes/algebra_gohberg_lidskii_followup_search.md;notes/algebra_gohberg_lidskii_followup_manifest.json;notes/algebra_history_web178.json;notes/algebra_history_web182.json"],
    ["geo-H-history","2026-11-20","GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters","used and rechecked in this run","Original Russian Dunford-Schwartz II (Mir1966) public scan opened; individually read title pages1-3, prefaces5-8, Fredholm historical subsection328-330, Lidskii hits753/755, bibliography970-971/993-994, index1045/1047, contents1061-1062 and colophon1064. No dated Grothendieck proof/letter/cote1 identification. Editor p6 explicitly adds historical notes; English body remains unopened. Native-text page ordinal correction recorded.","notes/algebra_dunford_ru1966_source_audit.md;notes/algebra_dunford_ru1966_manifest.json;logs/algebra_dunford_ru_fetch76.json;logs/algebra_dunford_ru_render77.json;logs/algebra_dunford_ru_record78.json"]
]
old=events.read_text()
with events.open("a") as f:
    for row in rows:
        line="\t".join(row)
        if line not in old:
            f.write(line+"\n")

outputs=["notes/algebra_dunford_ru1966_source_audit.md","notes/algebra_dunford_ru1966_manifest.json","notes/algebra_gohberg_lidskii_followup_search.md","notes/algebra_gohberg_lidskii_followup_manifest.json"]
log={"started_utc":now,"ended_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"elapsed_seconds":round(time.monotonic()-start,3),"outputs":[{"path":p,"sha256":sha(base/p),"bytes":(base/p).stat().st_size} for p in outputs],"events_appended":len(rows),"source_sha256_verified":sha(source)=="176dbdf4d51440456a1b8c7048d7db3a68b0a518a5b50b37d72533872ea52229","paper_and_bibliography_changed":False}
(base/"logs/algebra_dunford_ru_record78.json").write_text(json.dumps(log,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(log,ensure_ascii=False,indent=2))
