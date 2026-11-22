from pathlib import Path
from datetime import datetime, timezone
import json, time

started = time.monotonic()
root = Path(__file__).resolve().parents[1]
path = root/'notes/algebra_earlynotices_source_audit.md'
text = path.read_text()
old = '''## Other selected notices: reading in progress

The exact selected originals and retrieval hashes are recorded in `logs/algebra_earlynotices_fetch65.json`. AG4 (1951,839–841), AG14 (1954,158–160), AG65 (Bourbaki69,193–200) and AG67 (Bourbaki113) have been retrieved and their full text extracted/searched. Their individual original-page reading is not yet certified in this initial record; a completion entry will distinguish exact scopes and edition dates. In particular, AG65's original header and AG67's final revision date must not be replaced by bibliography shorthand.
'''
new = '''## Remaining selected originals: complete bounded reading

Every text page of each selected work was individually displayed and read. This closes the five-source selection; it does not claim coverage of unrelated long papers in the bibliography.

| Original work | Actual visual scope and dated text | Result relevant to the requested proof |
|---|---|---|
| AG4, *Quelques résultats sur les espaces vectoriels topologiques*, CR 233 (1951), 839–841 | All three original pages 839–841; running header 15 October 1951 | The notice concerns locally convex spaces, weak compactness, integration, and a dual form of Nachbin's extension theorem. Its Köthe collaboration remark concerns the named locally convex-space question. No Hilbert spectral-trace/genus-zero assertion, proof, or identification of a supplied manuscript. |
| AG14, *Sur certains sous-espaces vectoriels de Lp*, Canadian Journal of Mathematics 6 (1954), 158–160 | All three original pages 158–160; receipt 27 October 1953 | Theorems concern closed subspaces of Lp and measure-theoretic consequences. The opening attributes the motivating question to H. Mirkil and E. Farah. No spectral trace/genus-zero argument or supplied-manuscript identification. The receipt dates this paper only. |
| AG65, *Produits tensoriels topologiques et espaces nucléaires*, Bourbaki exposé 69, 193–200 | All eight text pages 193–200, physical PDF 2–9; header December 1952; ending [Juin 1957] | The Hilbert paragraph on 195 describes polar decomposition with summable eigenvalues of the positive absolute-value operator, credited to Dixmier and Schatten. Theorem 6 on 200 asserts an entire Fredholm determinant of order zero and rapidly decreasing eigenvalues for bounded operators on quasi-complete nuclear spaces. These do not give the general nonnormal Hilbert trace/genus-zero proof. No supplied manuscript or cote 1 identification. |
| AG67, *Réarrangements de fonctions et inégalités de convexité dans les algèbres de von Neumann munies d'une trace*, Bourbaki exposé 113, 127–139 | All thirteen text pages 127–139, physical PDF 2–14; header March 1955; ending [Juin 1957] | Section 4, p.133, gives spectral integral/trace formulas for normal operators. The remark on 135 discusses defining a spectral measure for nonnormal operators and algebraic multiplicities in the compact Hilbert case. Section 6, p.138, invokes the classical Fredholm determinant series for inequalities; p.139 credits Weyl's eigenvalue/singular-value product inequalities and gives an exterior-power footnote. No general Hilbert genus-zero proof, distinctive sector argument, or supplied manuscript/date identification appears. |

### Edition and scope qualifications

The Numdam cover of AG65 labels the collected item 1954, while its text has a December 1952 seminar header and a June 1957 ending, and its bibliography includes the 1955 memoir. The cover of AG67 labels its collected item 1956, while its text has a March 1955 seminar header, a June 1957 ending, and a reference to Dixmier's 1957 book. **No claim is made that these surviving complete texts were physically printed, unchanged, in the year of their seminar headers or in the year assigned by the cover.** The original first printings were not collated. Their explicit source links are recorded below; their full mathematical text was read from the facsimiles actually retrieved.

The determinant discussed on AG67 p.138 is not a newly supplied proof of the genus-zero factorization. The cited Fredholm series is used to obtain inequalities. Likewise, the summable positive eigenvalues in AG65 p.195 must not be substituted for the eigenvalues of an arbitrary nonnormal trace-class operator. These distinctions are mathematical scope checks of the opened texts, not claims about unseen drafts.

### Exact opened files, URLs and hashes

- AG4: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-4.pdf ; local `sources/algebra_earlynotice_AG4.pdf`; 343208 bytes; SHA256 `1ec296035f4b2e46e5f6fe293a41dafc54d47d53dad0bd42f24082ba02b63f92`. Renders `algebra_earlynotice_AG4_page001.png`–`003.png`.
- AG14: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-14.pdf ; local `sources/algebra_earlynotice_AG14.pdf`; 346367 bytes; SHA256 `48874f8753c073f3b128993bc23312fd42a17f2fd8160dd70a8512b119122861`. Renders `algebra_earlynotice_AG14_page001.png`–`003.png`.
- AG65: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-65.pdf ; local `sources/algebra_earlynotice_AG65.pdf`; 898823 bytes; SHA256 `0e30358252226c1fb5a498c68ee5dc9a6fa9fe96091015720b28f292a8fd9665`. Text-page renders `algebra_earlynotice_AG65_page002.png`–`009.png`.
- AG67: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-67.pdf ; local `sources/algebra_earlynotice_AG67.pdf`; 1110547 bytes; SHA256 `313cf89d5f83e799e11ce552d3132219705bcfad5682ed52fa423873ce0fbc48`. Text-page renders `algebra_earlynotice_AG67_page002.png`–`014.png`.

All four PDFs were opened from public advertised links. Their complete extracted texts are adjacent `.txt` files and are a search aid, supplementary to the page-by-page visual readings. Two additional Numdam item URLs printed in the original covers were attempted by the web reader: https://www.numdam.org/item?id=SB_1951-1954__2__193_0 and https://www.numdam.org/item?id=SB_1954-1956__3__127_0 . Both were unavailable in that reader (`notes/algebra_history_web159.json`); no separate successful catalogue opening is claimed and neither failure limits the facsimiles already obtained.

### Independent AG5 comparison and resulting documentary conclusion

Geometry reported an independent individual visual reading of all three AG5 original pages, including the clear starred 3 December 1951 date; root independently checked the decisive p.1557 paragraph. Those current-run checks are recorded as documentary events. The new positive result is the **1951 printed announcement** of the Hilbert genus-zero assertion. None of the five selected originals gives a date or identification for the particular cote 1 proof sheets. This leaves that precise documentary gate open, without inventing a further gate about the already established published announcement.
'''
if old not in text:
    raise SystemExit('Expected initial pending paragraph missing; no changes made')
text = text.replace(old,new)
text += '''\n## Completion record\n\n`code/algebra_earlynotices_complete68.py` and `logs/algebra_earlynotices_complete68.json` record the actual final reading scopes and append only allowed documentary check events. `notes/algebra_earlynotices_query_manifest.json` links raw web results 158–159 and the actual bibliography annotations used for selection. Bibliography and paper-section files were not changed in this completion step, respecting the checkpoint freeze.\n'''
path.write_text(text,encoding='utf-8')
manifest = {
 'selection_source':'sources/algebra_history_AG_bibliotex.pdf actual PDF annotations, previously opened; logs/algebra_history_retro36.json; exact selection also retained in logs/algebra_earlynotices_fetch65.json',
 'raw_web':['notes/algebra_history_web158.json','notes/algebra_history_web159.json'],
 'retrieval_log':'logs/algebra_earlynotices_fetch65.json',
 'readings':[
   {'AG_item':4,'physical_pages':[1,2,3],'printed_pages':'839–841','visual':'all original text pages'},
   {'AG_item':5,'physical_pages':[1,2,3],'printed_pages':'1556–1558','visual':'all original text pages; enlarged running header; root independently1557; geometry independently all3'},
   {'AG_item':14,'physical_pages':[1,2,3],'printed_pages':'158–160','visual':'all original text pages'},
   {'AG_item':65,'physical_pages':list(range(2,10)),'printed_pages':'193–200','visual':'all original text pages'},
   {'AG_item':67,'physical_pages':list(range(2,15)),'printed_pages':'127–139','visual':'all original text pages'},
 ],
 'excluded_completed_team_sources':['1952 AIF summary','1954 CR pair','Memoir16','1956 metric résumé','1956 Fredholm paper','Bourbaki91'],
 'longer_bibliography_items_not_visually_read_in_this_branch':[6,7,8,9,10,17],
 'result':'Earlier1951 printed Hilbert genus-zero announcement without proof; no identified or dated cote1 manuscript supplied in selected sources.'
}
(root/'notes/algebra_earlynotices_query_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
rows = [
 ['geo-H-history','2026-11-20','GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters','used and rechecked in this run','All original text pages of AG4 (839-841), AG14 (158-160), Bourbaki69 (193-200) and Bourbaki113 (127-139) individually displayed/read. Distinguished positive singular-value and normal-operator trace assertions, nuclear-space order-zero theorem, determinant inequalities and Weyl inequalities from the general Hilbert genus-zero proof. Both Bourbaki texts end June1957 despite earlier headers. No supplied manuscript or particular-sheet date identification.','notes/algebra_earlynotices_source_audit.md;notes/algebra_earlynotices_query_manifest.json;logs/algebra_earlynotices_fetch65.json;logs/algebra_earlynotices_complete68.json'],
 ['geo-H-history','2026-11-20','GPT-6 Astra Pro (OpenAI), inherited effort, geometry_analysis','used and rechecked in this run','Geometry independently individually viewed all3 original AG5 pages1556-1558; confirmed1951 Hilbert genus-zero announcement without printed proof and clear starred3December1951 date; running-header qualification retained. Check reported directly to algebra_letters.','notes/algebra_earlynotices_source_audit.md;sources/algebra_earlynotice_AG5_page001.png;sources/algebra_earlynotice_AG5_page002.png;sources/algebra_earlynotice_AG5_page003.png'],
]
with (root/'notes/algebra_history_CHECK_EVENTS.tsv').open('a',encoding='utf-8') as f:
    for row in rows:f.write('\t'.join(row)+'\n')
out={'utc_recorded':datetime.now(timezone.utc).isoformat(),'notes_written':['notes/algebra_earlynotices_source_audit.md','notes/algebra_earlynotices_query_manifest.json'],'new_documentary_events':len(rows),'bibliography_or_sections_modified':False,'total_original_text_pages_read_in_selection':30,'elapsed_seconds':time.monotonic()-started}
(root/'logs/algebra_earlynotices_complete68.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
