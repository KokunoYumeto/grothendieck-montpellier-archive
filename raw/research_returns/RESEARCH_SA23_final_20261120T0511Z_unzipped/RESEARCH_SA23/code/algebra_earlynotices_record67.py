from pathlib import Path
from datetime import datetime, timezone
import json, time

start = time.monotonic()
root = Path(__file__).resolve().parents[1]
audit = r'''# Early functional-analysis notices: original-source audit

Checked on 2026-11-20. This bounded branch belongs to existing statement `geo-H-history`. The selection follows actual download annotations in the previously opened Grothendieck bibliography, not guessed filenames. The 1952 summary, 1954 CR pair, memoir, metric résumé and Fredholm paper were excluded because their relevant original text had already been checked by the team.

## New positive witness: AG5, CR233 (1951), 1556–1558

Alexander Grothendieck, *Sur une notion de produit tensoriel topologique d'espaces vectoriels topologiques, et une classe remarquable d'espaces vectoriels liée à cette notion*, Comptes rendus de l'Académie des sciences de Paris **233 (1951), 1556–1558**.

- Original facsimile actually opened: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-5.pdf
- Local PDF: `sources/algebra_earlynotice_AG5.pdf`, **344381 bytes**, SHA256 **05c7fcb7fc8a7c2f33df15954406a4faca00377b19b3e7aeaefc5dcdbd1c887a**.
- All three original pages, printed1556–1558, were individually displayed and visually read. Renders: `sources/algebra_earlynotice_AG5_page001.png` through `003.png`.
- The article starts part way down1556 and ends before Ostrowski's article on1558. Dates/footnotes belonging to neighboring articles were excluded.
- The starred note on1556 explicitly dates the presentation/session **3 December 1951**. The running header on1557 appears to print **19 December 1951**; its enlargement is preserved in `sources/algebra_earlynotice_AG5_header_enlarged.png`. That second reading has not been independently collated against an issue-level original record and is retained with this qualification, not silently replaced by a calendar inference. The year1951 and the separate starred date suffice for the announcement chronology.

### Exact mathematical and documentary scope

At **1557, §1, final paragraph**, Grothendieck announces that the Fredholm determinant of a trace operator is entire of genus at most one, and that it has genus zero when the underlying space is Hilbert or when the operator is the product of two trace operators. The preceding prose promises a detailed Fredholm exposition elsewhere. The short note supplies **no proof of this Hilbert genus-zero assertion**, and does not identify a supplied manuscript, letter, enclosure, or the cote1 sheets. At1558 the final paragraph separately announces genus zero for compact operators on nuclear Fréchet spaces. These are distinct scopes.

This is an earlier printed witness to the Hilbert genus-zero announcement than the1955/1956 publications previously compared. It changes the documented announcement chronology; it does **not** date the particular unpublished proof or prove that its distinctive argument was printed in1951. Root independently displayed/read1557 and confirmed both the italic genus-zero sentence and the promise of a detailed exposition elsewhere. No independent physical first-printing/issue collation is claimed.

Bibliography key: **algGrothendieckCR1951Tensor**, in `notes/algebra_earlynotices_references.bib`. A compact optional insertion is `sections/algebra_history_1951_insertion.tex`.

## Other selected notices: reading in progress

The exact selected originals and retrieval hashes are recorded in `logs/algebra_earlynotices_fetch65.json`. AG4 (1951,839–841), AG14 (1954,158–160), AG65 (Bourbaki69,193–200) and AG67 (Bourbaki113) have been retrieved and their full text extracted/searched. Their individual original-page reading is not yet certified in this initial record; a completion entry will distinguish exact scopes and edition dates. In particular, AG65's original header and AG67's final revision date must not be replaced by bibliography shorthand.

## Reproducibility and exact source flags

- Selection source: previously opened `sources/algebra_history_AG_bibliotex.pdf`; actual annotation extraction is retained in `logs/algebra_history_retro36.json`.
- `code/algebra_earlynotices_fetch65.py` and `logs/algebra_earlynotices_fetch65.json`: five independent ordinary public PDF requests, headers, bytes, SHA256, full text search and page renders. All returnedHTTP200. An advertised http link was upgraded to https on the same public host.
- `notes/algebra_history_web158.json`: web-reader openings of AG5,AG65,AG67. AG5 and AG65 opened; AG67 was unavailable in that reader, while the ordinary unauthenticated public download returnedHTTP200. There was no access-control refusal or bypass.
- `code/algebra_earlynotice_enlarge66.py` and `logs/algebra_earlynotice_enlarge66.json`: exact local page crops. The header enlargement was actually displayed/read; the other generated crop is not counted as a separate visual inspection unless explicitly recorded later.
- `code/algebra_earlynotices_record67.py` and `logs/algebra_earlynotices_record67.json`: this first reading record, bibliography, insertion and documentary events.

This branch uses original printed-page facsimiles; full-text extraction is a search aid. Every claim of visual reading above concerns an image actually displayed. No general negative conclusion is drawn about unread long papers, unseen sources, or an undated manuscript.
'''
bib = r'''@article{algGrothendieckCR1951Tensor,
  author = {Grothendieck, Alexander},
  title = {Sur une notion de produit tensoriel topologique d'espaces vectoriels topologiques, et une classe remarquable d'espaces vectoriels liée à cette notion},
  journal = {Comptes rendus de l'Académie des sciences de Paris},
  volume = {233},
  year = {1951},
  pages = {1556--1558},
  url = {https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-5.pdf},
  note = {Opened: all three original facsimile pages1556--1558 visually read. The starred presentation date is3December1951; the running header appears to read19December1951, not independently collated as an issue date. At1557, section1, last paragraph, the Hilbert genus-zero assertion is announced without proof; a detailed Fredholm exposition is promised elsewhere. No identification or date of the cote1 manuscript is supplied.}
}
'''
insertion = r'''The printed announcement already occurs in Grothendieck's1951
Comptes rendus note: at p.1557, the last paragraph of section1 asserts
genus zero for the Fredholm determinant in the Hilbert-space case, while
promising the detailed Fredholm exposition elsewhere.
\cite[p.~1557]{algGrothendieckCR1951Tensor}
The starred presentation date is3December1951; the running header appears
to read19December1951, a reading not independently collated at issue level.
The three-page notice gives no proof of the Hilbert assertion and identifies
no manuscript or enclosure. It therefore establishes an earlier printed
announcement, without dating the particular cote1 proof sheets.
'''
files = {
 'notes/algebra_earlynotices_source_audit.md': audit,
 'notes/algebra_earlynotices_references.bib': bib,
 'sections/algebra_history_1951_insertion.tex': insertion,
}
for rel, text in files.items():
    (root/rel).write_text(text, encoding='utf-8')
events = [
 ['geo-H-history','2026-11-20','GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters','used and rechecked in this run','All three original AG5 pages1556-1558 visually read. At1557 section1 final paragraph the Hilbert determinant genus-zero claim is announced and detailed Fredholm exposition promised elsewhere; no proof or supplied-manuscript identification. Starred3December1951 distinguished from uncollated running-header reading19December1951. Particular-sheet date gate unchanged.','notes/algebra_earlynotices_source_audit.md;logs/algebra_earlynotices_fetch65.json;logs/algebra_earlynotice_enlarge66.json;notes/algebra_history_web158.json'],
 ['geo-H-history','2026-11-20','GPT-6 Astra Pro (OpenAI), inherited effort, root','used and rechecked in this run','Root independently displayed/read original AG5 printed1557 and confirmed the italic Hilbert genus-zero assertion and preceding promise of detailed Fredholm exposition; running-header reading kept qualified.','notes/algebra_earlynotices_source_audit.md;sources/algebra_earlynotice_AG5_page002.png'],
]
with (root/'notes/algebra_history_CHECK_EVENTS.tsv').open('a',encoding='utf-8') as f:
    for row in events: f.write('\t'.join(row)+'\n')
log = {'utc_recorded':datetime.now(timezone.utc).isoformat(),'files_written':list(files),'events_appended':len(events),'elapsed_seconds':time.monotonic()-start,'source_reading':'AG5 all3 original pages; local header crop displayed; root independent1557 check reported directly'}
(root/'logs/algebra_earlynotices_record67.json').write_text(json.dumps(log,indent=2)+'\n')
print(json.dumps(log,indent=2))
